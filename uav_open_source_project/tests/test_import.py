from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from uav_detector import IMG_SIZE, OBJ_THRESH

print('IMG_SIZE =', IMG_SIZE)
print('OBJ_THRESH =', OBJ_THRESH)
