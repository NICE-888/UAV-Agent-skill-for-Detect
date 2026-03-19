from .config import CLASSES, IMG_SIZE, OBJ_THRESH, NMS_THRESH
from .detector import detect_image, run_video_detection
from .rknn_pool import RknnPoolExecutor

__all__ = [
    'CLASSES',
    'IMG_SIZE',
    'OBJ_THRESH',
    'NMS_THRESH',
    'detect_image',
    'run_video_detection',
    'RknnPoolExecutor',
]
