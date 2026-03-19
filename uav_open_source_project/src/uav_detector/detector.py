from __future__ import annotations

import time
from pathlib import Path
from typing import Optional

import cv2
import numpy as np

from .config import IMG_SIZE
from .postprocess import draw, letterbox, yolov8_post_process
from .rknn_pool import RknnPoolExecutor


def preprocess_bgr_image(image: np.ndarray):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    rgb, ratio, padding = letterbox(rgb, new_shape=(IMG_SIZE, IMG_SIZE))
    rgb = np.expand_dims(rgb, 0)
    return rgb, ratio, padding


def infer_frame(rknn_lite, image: np.ndarray):
    model_input, ratio, padding = preprocess_bgr_image(image)
    outputs = rknn_lite.inference(inputs=[model_input], data_format=['nhwc'])
    boxes, classes, scores = yolov8_post_process(outputs)
    output = image.copy()
    if boxes is not None:
        draw(output, boxes, scores, classes, ratio, padding)
    return output


def detect_image(model_path: str, image_path: str, output_path: Optional[str] = None):
    from .rknn_pool import init_rknn

    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"无法读取图片: {image_path}")

    rknn_lite = init_rknn(model_path, 0)
    try:
        result = infer_frame(rknn_lite, image)
    finally:
        rknn_lite.release()

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        cv2.imwrite(output_path, result)
    return result


def run_video_detection(model_path: str, source: str, tpes: int = 3, save_path: Optional[str] = None, show: bool = True):
    cap = cv2.VideoCapture(0 if str(source) == '0' else source)
    if not cap.isOpened():
        raise RuntimeError(f"无法打开输入源: {source}")

    pool = RknnPoolExecutor(model_path=model_path, tpes=tpes, func=infer_frame)

    writer = None
    if save_path:
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) or 640
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) or 480
        fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        writer = cv2.VideoWriter(save_path, fourcc, fps, (width, height))

    try:
        if cap.isOpened():
            for _ in range(tpes + 1):
                ret, frame = cap.read()
                if not ret:
                    raise RuntimeError("视频预热失败：读取不到足够帧")
                pool.put(frame)

        frames = 0
        loop_time = time.time()
        init_time = time.time()

        while cap.isOpened():
            frames += 1
            ret, frame = cap.read()
            if not ret:
                break
            pool.put(frame)
            result, flag = pool.get()
            if not flag:
                break

            if writer is not None:
                writer.write(result)

            if show:
                cv2.imshow('uav-detector', result)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            if frames % 30 == 0:
                print(f"30帧平均帧率:\t{30 / (time.time() - loop_time):.2f} 帧")
                loop_time = time.time()

        total_fps = frames / max(time.time() - init_time, 1e-6)
        print(f"总平均帧率\t{total_fps:.2f}")
        return total_fps
    finally:
        cap.release()
        if writer is not None:
            writer.release()
        cv2.destroyAllWindows()
        pool.release()
