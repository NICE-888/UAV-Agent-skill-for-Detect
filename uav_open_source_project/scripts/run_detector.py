import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from uav_detector.detector import run_video_detection


def parse_args():
    parser = argparse.ArgumentParser(description='Run RKNN UAV detector on video or camera')
    parser.add_argument('--source', required=True, help='视频路径或摄像头编号 0')
    parser.add_argument('--model', default=str(ROOT / 'assets/models/UAV.rknn'), help='RKNN 模型路径')
    parser.add_argument('--tpes', type=int, default=3, help='并发线程数')
    parser.add_argument('--save-path', default='', help='保存结果视频，可选')
    parser.add_argument('--no-show', action='store_true', help='不显示窗口')
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
