# UAV-Agent-skill-for-Detect

基于 **RK3588 + RKNN** 的无人机目标检测项目。  
本项目提供一个可部署在边缘设备上的目标检测推理方案，支持使用你自训练导出的 `UAV.rknn` 模型进行图像、视频和摄像头输入的检测。

## Features

- 基于 **RK3588** 平台部署
- 使用 **RKNN** 模型推理
- 支持 **图像 / 视频 / 摄像头** 输入
- 集成 **多线程推理池**，提升检测吞吐
- 适合边缘端无人机目标检测场景
- 支持替换为你自己的 `UAV.rknn` 权重

---

## Project Overview

本项目主要用于在 RK3588 设备上运行无人机目标检测模型。  
核心流程包括：

1. 读取图像 / 视频流
2. 送入 RKNN 模型进行推理
3. 对模型输出进行后处理（解码、筛选、NMS）
4. 在结果图像上绘制检测框
5. 输出可视化检测结果

---

## Project Structure

```text
UAV-Agent-skill-for-Detect/
├── README.md                  # 项目说明
├── LICENSE                    # 开源许可证
├── requirements.txt           # Python 依赖
├── main.py                    # 主入口
├── func.py                    # 后处理、绘框等核心逻辑
├── rknnpool.py                # RKNN 多线程推理池
├── scripts/
│   ├── infer_image.py         # 单张图片推理示例
│   └── run_detector.py        # 视频/摄像头推理示例
├── src/
│   └── uav_detector/          # 模块化源码
├── docs/
│   ├── deployment.md          # 部署说明
│   └── release-guide.md       # 发布说明
└── assets/
    ├── demo/                  # 示例数据
    └── models/                # 模型权重目录
