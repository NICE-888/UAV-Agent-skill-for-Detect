# RK3588 部署说明

## 1. 系统准备

确保设备已安装：

- Python 3.8+
- OpenCV
- NumPy
- RKNN Lite Runtime

## 2. 目录准备

将模型放到：

```text
assets/models/UAV.rknn
```

## 3. 图片推理

```bash
python scripts/infer_image.py --image ./test.jpg --model assets/models/UAV.rknn --output ./output.jpg
```

## 4. 视频推理

```bash
python scripts/run_detector.py --source ./demo.mp4 --model assets/models/UAV.rknn --save-path ./result.mp4
```

## 5. 摄像头推理

```bash
python scripts/run_detector.py --source 0 --model assets/models/UAV.rknn
```

## 6. 发布前建议修改

- 把 `src/uav_detector/config.py` 中的 `CLASSES` 改成你的真实训练类别
- 把 README 中的示例图替换成你自己的无人机检测效果图
- 把 `UAV.rknn` 作为 Release 附件发布，而不是提交进 Git 仓库
