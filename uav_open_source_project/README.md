# UAV-Agent-skill-for-Detect

一个面向智能体调用的无人机目标检测 Skill。  
该 Skill 基于 **RK3588 + RKNN** 推理环境封装，使用自训练导出的 `UAV.rknn` 权重，对图像、视频或摄像头输入进行目标检测，并返回检测结果与可视化输出。

---

## What is this?

`UAV-Agent-skill-for-Detect` 不是一个普通的目标检测示例仓库，而是一个**可封装为 Skill 的智能体检测工具项目**。

它的目标是让智能体在接收到类似如下请求时，能够自动调用检测能力：

- “帮我检测这张图里有没有无人机”
- “分析这个视频中的目标”
- “对摄像头画面进行实时检测”
- “输出检测框和类别信息”

该项目适合作为：

- ChatGPT Skill
- Agent tool backend
- MCP 工具封装的基础检测模块
- GitHub 开源技能项目模板

---

## Skill Capability

本 Skill 提供以下能力：

- 对单张图片进行无人机目标检测
- 对视频文件逐帧检测
- 对实时摄像头流进行检测
- 返回结构化检测结果
- 输出带检测框的可视化结果
- 支持 RK3588 上的 RKNN 模型推理
- 支持替换为你自己的 `UAV.rknn` 模型

---

## Typical Agent Use Cases

当智能体遇到以下任务时，可以调用本 Skill：

- 用户上传一张图片，请求识别其中的无人机目标
- 用户提供视频，请求分析其中是否存在目标
- 用户要求输出检测框位置、类别和置信度
- 用户希望保存检测后的结果图或结果视频
- 用户需要在 RK3588 设备上运行边缘检测任务

---

## Input

本 Skill 支持以下输入形式：

### 1. Image
输入一张图片文件路径，例如：

```json
{
  "image_path": "assets/demo/test.jpg"
}

可以，下面这份就是**可一键替换**的最终版 `README.md`。
它已经把项目定位明确成：

* **一个面向智能体调用的 UAV 检测 Skill**
* 不是普通 demo 仓库
* 兼顾 GitHub 开源展示、用户使用、后续 Skill/MCP 扩展

你直接把你仓库里的 `README.md` 全部删掉，替换成下面这份即可。

---

````markdown
# UAV-Agent-skill-for-Detect

一个面向智能体调用的无人机目标检测 Skill 项目。  
本项目基于 **RK3588 + RKNN** 推理环境构建，使用自训练导出的 `UAV.rknn` 模型，实现对图片、视频和摄像头输入的目标检测，并可作为 **Skill / Agent Tool / MCP 能力模块** 集成到智能体系统中。

---

## Overview

`UAV-Agent-skill-for-Detect` 的核心目标，不是提供一个普通的目标检测示例，而是将 RK3588 上的无人机检测能力，封装成一个**可被智能体调用的视觉检测 Skill**。

它适用于以下场景：

- 智能体收到图片后，需要判断其中是否存在无人机目标
- 智能体收到视频后，需要分析视频中的目标信息
- 智能体需要返回结构化检测结果，例如类别、置信度和检测框
- 智能体需要生成带检测框的可视化结果图或结果视频
- 需要把 RK3588 边缘端视觉能力封装成一个可分发、可复用、可开源的 Skill 工程

本项目可以作为以下用途的基础模板：

- ChatGPT Skill
- 智能体检测工具
- Agent Workflow 中的视觉节点
- MCP 服务封装前的检测核心模块
- GitHub 开源的技能型项目模板

---

## Skill Positioning

这个项目的定位是：

> **将基于 RK3588 + RKNN 的无人机目标检测能力，封装为一个可被智能体触发和调用的 Skill。**

这意味着项目不仅仅提供推理代码，还强调：

- Skill 化封装
- Agent 可调用
- 输入输出标准化
- 模型依赖清晰
- 易于二次集成
- 易于开源和分发

---

## Core Capabilities

本 Skill 当前支持以下能力：

- 单张图片目标检测
- 视频逐帧目标检测
- 摄像头实时检测
- 检测框可视化输出
- 结构化检测结果输出
- RK3588 边缘端部署
- RKNN 模型推理
- 多线程推理池加速
- 可替换自训练 `UAV.rknn` 模型

---

## Typical Agent Use Cases

当智能体遇到以下用户请求时，可以调用本 Skill：

- “帮我检测这张图里有没有无人机”
- “分析这个视频里的目标”
- “输出检测框位置和置信度”
- “实时检测摄像头画面中的目标”
- “保存检测后的结果图”
- “基于边缘设备完成视觉目标检测”

---

## Supported Input Types

本 Skill 支持以下输入形式。

### 1. Image Input

输入一张图片路径，例如：

```json
{
  "image_path": "assets/demo/test.jpg"
}
````

### 2. Video Input

输入一个视频路径，例如：

```json
{
  "video_path": "assets/demo/test.mp4"
}
```

### 3. Camera Stream Input

输入摄像头索引，例如：

```json
{
  "camera_id": 0
}
```

---

## Output Format

本 Skill 的输出分为两类。

### 1. Structured Detection Result

用于给智能体或上层系统消费的结构化结果，例如：

```json
{
  "ok": true,
  "input_type": "image",
  "detections": [
    {
      "class_name": "uav",
      "confidence": 0.91,
      "bbox": [523, 218, 641, 302]
    }
  ]
}
```

字段说明：

* `ok`：是否执行成功
* `input_type`：输入类型，例如 `image` / `video` / `camera`
* `detections`：检测结果列表
* `class_name`：检测类别名称
* `confidence`：置信度
* `bbox`：边界框坐标，格式为 `[x1, y1, x2, y2]`

### 2. Visualization Output

可视化输出包括：

* 带检测框的图片
* 带检测框的视频
* 实时检测窗口显示结果

---

## Project Structure

```text
UAV-Agent-skill-for-Detect/
├── README.md                      # 项目说明（面向用户）
├── LICENSE                        # 开源许可证
├── requirements.txt               # Python 依赖
├── SKILL.md                       # Skill 主说明文件
├── main.py                        # 项目主入口
├── func.py                        # 后处理、NMS、绘框等核心逻辑
├── rknnpool.py                    # RKNN 多线程推理池
├── agents/
│   └── openai.yaml                # Skill 元数据
├── scripts/
│   ├── infer_image.py             # 单图检测入口
│   └── run_detector.py            # 视频/摄像头检测入口
├── src/
│   └── uav_detector/
│       ├── config.py              # 配置项
│       ├── postprocess.py         # 解码、NMS、绘框
│       ├── rknn_pool.py           # 推理池封装
│       └── pipeline.py            # 检测流程封装
├── docs/
│   ├── deployment.md              # 部署说明
│   └── release-guide.md           # 发布说明
└── assets/
    ├── demo/                      # 示例数据
    └── models/
        └── UAV.rknn               # 模型文件（需自行放入）
```

---

## Runtime Requirements

运行本 Skill 需要以下环境。

### Hardware

* RK3588 设备

### Operating System

* Linux

### Python

* Python 3.8 或更高版本

### Dependencies

* OpenCV
* NumPy
* RKNN Runtime / RKNN Toolkit Lite

> 注意：RKNN 相关运行环境需要根据你的 RK3588 系统版本自行安装。

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/hytAccept/UAV-Agent-skill-for-Detect.git
cd UAV-Agent-skill-for-Detect
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Prepare the Model File

将你的模型权重文件 `UAV.rknn` 放到：

```text
assets/models/UAV.rknn
```

如果缺少该文件，Skill 无法执行实际推理。

---

## Model Weights

本仓库默认**不直接包含模型权重文件**。
这是为了避免将大文件长期写入 Git 历史，同时也方便独立更新模型版本。

你需要：

1. 准备你自己的 `UAV.rknn`
2. 放入以下目录：

```text
assets/models/UAV.rknn
```

推荐的开源发布方式：

* 仓库中仅保留源码和说明文档
* 模型文件通过 **GitHub Releases** 发布
* 用户从 Release 页面下载模型并手动放入 `assets/models/`

---

## Quick Start

### Run Main Entry

```bash
python main.py
```

适合快速测试主流程。

---

### Run Single Image Detection

```bash
python scripts/infer_image.py
```

适合对单张图片执行检测。

---

### Run Video or Camera Detection

```bash
python scripts/run_detector.py
```

适合：

* 视频文件检测
* 摄像头实时检测

---

## How the Skill Works

本 Skill 的内部处理流程如下：

1. 接收输入源（图片 / 视频 / 摄像头）
2. 对输入进行预处理
3. 将数据送入 RKNN 模型
4. 获取推理输出
5. 对输出进行解码
6. 进行阈值筛选
7. 执行 NMS 去除重复框
8. 生成结构化检测结果
9. 输出可视化检测图像或视频

---

## Integrating as a Skill

如果你希望将本项目作为一个真正的 Skill 供智能体调用，建议至少保留以下文件：

* `SKILL.md`
* `agents/openai.yaml`
* 检测脚本
* 模型说明
* 输入输出格式说明

智能体在接收到视觉检测相关任务时，可以根据 `SKILL.md` 中的描述触发该 Skill，并通过项目中的脚本或接口完成检测任务。

---

## Integrating as an Agent Tool

本项目也可以进一步作为 Agent Tool 使用。
推荐封装出的能力接口包括：

* `detect_image`
* `detect_video`
* `detect_stream`
* `get_model_info`

如果你后续希望将本项目扩展为：

* 本地工具
* 远程检测服务
* MCP Server
* Agent Workflow 视觉节点

本仓库可作为检测核心模块直接复用。

---

## How to Use Your Own Model

如果你希望替换为自己的 RKNN 模型，请按以下步骤操作：

1. 将模型命名为 `UAV.rknn`
2. 放到：

```text
assets/models/UAV.rknn
```

3. 修改类别名称配置
4. 根据需要调整：

   * 置信度阈值
   * NMS 阈值
   * 输入尺寸
   * 推理线程数

> 注意：如果你的训练类别与默认类别配置不一致，请务必同步修改配置，否则输出标签可能不正确。

---

## Example Usage Flow

一个典型的使用流程如下：

1. 准备 RK3588 运行环境
2. 安装 Python 依赖
3. 将 `UAV.rknn` 放到 `assets/models/`
4. 执行图片、视频或摄像头检测脚本
5. 获取结构化检测结果
6. 输出检测框可视化结果
7. 将本能力接入智能体系统或工作流

---

## Demo Assets

你可以在 `assets/demo/` 中放置：

* 输入图片
* 输出结果图
* 测试视频
* 演示截图

建议在仓库首页加入效果图，例如：

```markdown
![demo](assets/demo/result.jpg)
```

这样用户进入仓库后可以快速理解项目效果。

---

## Important Notes

* 本项目依赖 RKNN 运行环境
* 本项目主要面向 RK3588 平台
* 本项目必须提供 `UAV.rknn` 模型文件才能运行
* 请确保类别配置与实际模型训练类别一致
* 若后续作为智能体工具使用，建议继续封装标准接口
* 若后续作为 MCP 能力发布，建议进一步增加 API / MCP 层

---

## Recommended Open-Source Release Strategy

建议公开仓库时包含以下内容：

* Skill 项目结构
* 推理源码
* 使用说明
* 示例资源
* 配置说明
* 打包与发布说明

建议不要长期把模型权重直接纳入 Git 历史，而是采用：

* GitHub Releases
* 独立下载链接
* 单独模型仓库

---

## Known Limitations

当前版本的限制包括：

* 仅支持 RKNN 模型格式
* 主要适配 RK3588 平台
* 默认示例配置可能需要根据你的模型做调整
* 当前版本主要聚焦检测核心能力，未内置标准化 HTTP API
* 当前版本可作为 Skill 基础能力，但如果要上 MCP 市场，仍建议继续封装远程服务层

---

## Roadmap

后续可扩展方向包括：

* 批量图片检测
* JSON 结果导出
* 检测日志输出
* HTTP API 封装
* MCP Server 封装
* Agent Tool Schema 标准化
* 自动生成检测摘要
* 与多模态智能体工作流集成

---

## Release

推荐通过 GitHub Releases 发布以下内容：

* `UAV.rknn`
* 示例图片
* 示例视频
* 版本更新说明
* 项目打包文件

---

## License

This project is licensed under the MIT License.

---

## Acknowledgement

本项目用于将 RK3588 上的无人机目标检测能力，封装为一个可供智能体调用的 Skill / Tool。
适用于边缘视觉检测场景、智能体集成场景以及后续 MCP 化扩展场景。

如果这个项目对你有帮助，欢迎 Star、Fork 和提出改进建议。

```

