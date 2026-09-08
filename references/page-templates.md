# Wiki 页面模板

本文件定义页面写作结构。不同 wiki mode 会采用不同侧重点：**先加载 `references/modes/<mode>.md`，再用本文件里的通用骨架**。

## 通用页头（每个页面都要有）

```text
# 页面标题（主题名，不带分级前缀）

> 本页属于：<grade 显示名>（例如：入门 / basics）
> 前置知识：无（或列出 Wiki 链接）
> 预计阅读时间：10 分钟
> provenance: <source-derived / agent-explanation / external-research / user-correction / derived / legacy-unverified>
> last_verified: <YYYY-MM-DD>
```

## 内容来源视觉标签

正文中必须明确区分：

- 📘 **Source / Slides**：来源直接支持。
- 💡 **Explanation**：Agent 对 source 的教学解释。
- 🔍 **Inference**：Agent 结合多个 evidence 的推导。
- 🌐 **External Reference**：来自课件/文档之外。
- 🧪 **Example**：示例。
- ⚠️ **Outside Scope**：课件明确说明不在范围。

禁止把 Explanation / Inference 写成“老师原话”。

## 术语惯例

核心术语首次出现：`中文（Canonical English Term, ABBR）`。之后允许用英文或缩写。规则见 references/terminology.md。

## 页面类型与模板

### 1. 概念理解型（讲义页）

适合“这是什么、为什么需要、怎么理解”。Course / Research KB 常用此结构。

```text
## 🎯 为什么需要这个？
用真实场景引出需求。

## 💡 一个类比
用生活中的事物建立直觉。

## 🐍 最小必要知识
只讲够用的部分；Course Mode 请改为“来源忠实重建”，不要用最小必要知识删除课件内容。

## 🖼️ 图解
配图 + Figure Explanation + 来源（规范见 references/figure-model.md）。

## 📝 代码/操作示例（如有）
完整可运行示例，带逐行中文注释。

## ✨ Evidence
列出本页引用的 Claim→Evidence→Source。

## ✏️ 小练习
2-3 道题，答案用 <details> 折叠。
```

### 2. 工具使用型（教程页）

适合“安装、操作、跑通”。Technical Tutorial / SDK / Project Docs 常用。

```text
## 这是什么工具？
一句话定义 + 类比 + 它能解决什么问题。

## 核心概念
每个概念：是什么 + 类比 + 示例，用表格整理。

## 快速上手
安装/配置步骤 + 验证方法 + 第一次使用的完整示例。

## 主要功能详解
每个功能：什么时候用 + 怎么用 + 示例。

## 完整工作流程
流程图（Mermaid 优先）+ 每步说明。

## 常见问题 FAQ
覆盖 5-10 个高频问题。

## 速查卡片
表格或代码块。

## ✨ Evidence
列出涉及的接口/命令/配置的来源证据。
```

### 3. 混合型页面

先理解概念，再动手操作。上半部分用讲义页结构，下半部分用教程页结构。

### 4. 硬件实验页（新增）

用于 Lab / Project / Robot 等实体实验：

```text
## 实验目标与完成标准
## 所需物料 / 工具 / 软件版本
## 硬件连接（接线图/引脚图）
## 固件与软件准备
## 操作步骤（烧录、上电、运行）
## 预期现象
## 可调参数（offset / PID / 速度）
## 常见故障与排查
## 安全提示
## 验证练习（带答案）
```

## 通用页脚（每个页面都要有）

```text
## 本章小结
用 3-5 句话回顾本页要点。

## 下一步
- 上一页：[[页面名]]（第一页可写“无”）
- 下一页：[[页面名]]（最后一页可写“返回 Home”）
- 返回：[[Home]]

## 更新日志
- 日期：本次新增/修改了什么
```

## 配图要求

- 每张图必须有 caption + 来源 + 访问日期。
- `<!-- FIGURE: F01 -->` 标记在图片前。
- 详细见 references/figure-model.md。

## 公式要求

- 重要公式前加 `<!-- EQUATION: EQ01 -->`。
- 公式要有 source、symbols、explanation。详细见 references/equation-model.md。

## 写作要求

- 每个核心概念都要有类比（technical-tutorial 强调；project-docs / lab-handbook 不强求生活类比）。
- 代码逐行中文注释。
- 专业名词都要保留 canonical English term 并解释或链接。
- 用表格整理对比信息。
- 流程图优先 Mermaid（本地预览渲染）或 ASCII。
- 练习以“读懂/会用”为主，答案用 <details> 折叠。
- 链接使用 `[[页面名]]`，页面名 = 文件名（不带 .md、不带分级前缀），与 _Sidebar.md 保持一致。