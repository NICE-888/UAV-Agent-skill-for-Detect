# UAV-Agent-skill-for-Detect

基于 RK3588 + RKNN 的无人机目标检测开源项目骨架，适合部署在 Rockchip RK3588 设备上进行图片、视频和摄像头推理。

## 项目特点

- 基于 `rknnlite` 的 RKNN 推理
- 支持 RK3588 NPU 多核并行
- 保留你现有的后处理、DFL、NMS 和绘框流程
- 支持单图、视频、摄像头三种输入
- 已预留 `UAV.rknn` 模型位置，便于后续发布到 GitHub Releases

## 目录结构

```text
UAV-Agent-skill-for-Detect/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── main.py
├── scripts/
│   ├── infer_image.py
│   └── run_detector.py
├── src/
│   └── uav_detector/
│       ├── __init__.py
│       ├── config.py
│       ├── detector.py
│       ├── postprocess.py
│       └── rknn_pool.py
├── docs/
│   ├── deployment.md
│   └── release-guide.md
├── assets/
│   ├── demo/
│   │   └── README.md
│   └── models/
│       └── README.md
└── tests/
    └── test_import.py
```

## 环境要求

- Python 3.8+
- RK3588 / RK356x 等 Rockchip NPU 平台
- `rknn-toolkit-lite2` 或对应 `rknnlite` 运行环境
- OpenCV
- NumPy

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 放置模型

将你训练导出的 `UAV.rknn` 放到：

```text
assets/models/UAV.rknn
```

### 3. 运行视频检测

```bash
python main.py --source ./demo.mp4 --model assets/models/UAV.rknn
```

### 4. 运行图片检测

```bash
python scripts/infer_image.py --image ./test.jpg --model assets/models/UAV.rknn --output ./output.jpg
```

## 关于类别名

当前代码默认继承了你上传文件中的 COCO 类别列表，因此你在发布前应把 `src/uav_detector/config.py` 中的 `CLASSES` 改成你真实训练时的类别，例如：

```python
CLASSES = ("uav",)
```

## 模型权重发布建议

不建议把 `UAV.rknn` 直接提交到 Git 仓库。
推荐做法：

1. 源码推送到 GitHub 仓库
2. 在 GitHub Releases 中上传 `UAV.rknn`
3. 在 README 中说明下载方式

## 致谢

后处理结构基于 Rockchip RKNN Toolkit 示例演化而来，并保留了你的 DFL、NMS、多线程推理池实现思路。
