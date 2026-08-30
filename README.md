# skill-tutorial-wiki

一个 AI skill：搜集互联网上的领域知识，生成**新手友好的中文分级讲义**，并以 **GitHub Wiki** 方式组织成可独立访问、可导航、可持续更新的文档站点。

> 本仓库 fork 自 [tutorial-skill](https://github.com/YanZephyr14/tutorial-skill)，在其“零基础单篇教程”能力之上，扩展为“分级讲义 + Wiki 持续更新”。

## 它能做什么？

- 为任意领域建立分级知识库：L0 概念启蒙 → L1 入门 → L2 进阶 → L3 高级 → L4 专家。
- 按行业标准划分层级，学习曲线平缓，必要时自动拆分更多层级。
- 输出 GitHub Wiki 结构：Home、_Sidebar、_META 和分级页面，互相链接、可持续更新。
- 首次只生成 L0 导论（含如何安装、如何运行已有 demo），之后按需增量生成更高层级。
- 更新已有页面时采用合并更新，保留有效内容并记录 changelog。

## 分级模型

| 层级 | 定位 | 读者完成后能做什么 | 典型行业映射 |
|------|------|--------------------|--------------|
| L0 概念启蒙 | 零基础建立心智模型 | 说清领域是什么、能跑通官方 demo | 科普 / 导论 |
| L1 入门 | 会做最小真实任务 | 独立完成最小可用任务 | 初级 / Associate / A2 |
| L2 进阶 | 能处理常见任务 | 理解原理与边界，会调试和选型 | 中级 / Professional / B1-B2 |
| L3 高级 | 能设计与权衡 | 架构设计、性能优化、复杂系统 | 高级 / 架构师 / C1 |
| L4 专家 | 能看穿本质并创新 | 追踪前沿、方法论输出、指导他人 | 专家 / Specialty / C2 |

详细规则见 [references/level-framework.md](references/level-framework.md)。

## 输出结构

```text
Home.md              领域总览 + 分级学习地图
_Sidebar.md          完整导航树
_Footer.md           版权/反馈（可选）
_META.md             状态：页面清单、层级、更新日期、changelog
L0-...md             概念启蒙页
L1-...md             入门页
L2-...md             进阶页
...
```

页面写作模板见 [references/page-templates.md](references/page-templates.md)，Wiki 命名与链接规则见 [references/wiki-conventions.md](references/wiki-conventions.md)。

## 快速开始

安装后，用自然语言触发：

```text
帮我为 Docker 建立一个 GitHub Wiki 知识库
```

```text
为 Git 生成一份零基础学习路线，先只写 L0 导论
```

```text
继续生成 L1，补全 Git 分支与合并
```

默认首批只会生成 L0 导论；你可以显式要求“继续生成下一级”、“补全 L2”、“从 L3 开始”等。

## 安装

### 全局安装（所有项目可用）

```bash
mkdir -p ~/.claude/skills
cd ~/.claude/skills
git clone https://github.com/Kytolly/skill-tutorial-wiki.git skill-tutorial-wiki
```

### 项目内安装

```bash
mkdir -p .claude/skills
cd .claude/skills
git clone https://github.com/Kytolly/skill-tutorial-wiki.git skill-tutorial-wiki
```

其他 AI 工具请找到对应 skills 目录后 `git clone`。

## 工作流程

```text
明确领域与层级 → 盘点现有 Wiki → 规划本批页面（等你确认）→ 联网调研 → 生成页面并更新导航/状态 → 自查修复 → 报告增量结果
```

详细流程见 [SKILL.md](SKILL.md)。

## 仓库结构

```text
├── SKILL.md                         skill 主入口
├── README.md                        本文件
├── LICENSE
├── references/                      渐进式加载的详细规范
│   ├── level-framework.md           分级模型与行业映射
│   ├── page-templates.md            页面模板
│   ├── wiki-conventions.md          Wiki 命名、导航、更新规则
│   └── research-and-sources.md      联网调研与来源记录
└── examples/
    └── minimal-wiki/                最小 Wiki 样例
```

## 自定义

- 修改分级标准：编辑 `references/level-framework.md`。
- 修改页面模板：编辑 `references/page-templates.md`。
- 修改调研工具：编辑 `references/research-and-sources.md`。
- 修改写作风格：编辑 `references/page-templates.md` 末尾的“写作要求”。

## 与上游的关系

本仓库是 [tutorial-skill](https://github.com/YanZephyr14/tutorial-skill) 的 fork，保留了单篇教程的类比优先、需求驱动、真实案例三大写作原则，并新增了分级与 Wiki 持续更新能力。

## License

MIT