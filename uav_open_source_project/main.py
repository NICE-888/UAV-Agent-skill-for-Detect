import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'src'
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from uav_detector.detector import run_video_detection


def parse_args():
    parser = argparse.ArgumentParser(description='RK3588 UAV detector video entrypoint')
    parser.add_argument('--source', default='./720p60hz.mp4', help='视频路径或摄像头编号，摄像头可填 0')
    parser.add_argument('--model', default='assets/models/UAV.rknn', help='RKNN 模型路径')
    parser.add_argument('--tpes', type=int, default=3, help='线程池大小 / NPU 并发数')
    parser.add_argument('--save-path', default='', help='结果视频保存路径，可选')
    parser.add_argument('--no-show', action='store_true', help='不弹窗显示推理结果')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    run_video_detection(
        model_path=args.model,
        source=args.source,
        tpes=args.tpes,
        save_path=args.save_path or None,
        show=not args.no_show,
    )
