import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from uav_detector.detector import detect_image


def parse_args():
    parser = argparse.ArgumentParser(description='Run RKNN UAV detector on a single image')
    parser.add_argument('--image', required=True, help='输入图片路径')
    parser.add_argument('--model', default=str(ROOT / 'assets/models/UAV.rknn'), help='RKNN 模型路径')
    parser.add_argument('--output', default=str(ROOT / 'output.jpg'), help='输出图片路径')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    detect_image(model_path=args.model, image_path=args.image, output_path=args.output)
    print(f'推理完成，结果已保存到: {args.output}')
