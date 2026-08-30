# skill-tutorial-wiki

一个 AI skill：搜集互联网领域知识，生成**新手友好的中文分级讲义**，并以 **GitHub Wiki** 方式组织成可导航、可独立访问、可持续更新的文档站点。

> 本仓库 fork 自 [tutorial-skill](https://github.com/YanZephyr14/tutorial-skill)，在其"零基础单篇教程"能力之上，扩展为"分级讲义 + 本地预览 + GitHub Wiki 持续更新"。

## 它能做什么？

- **主题确认**：主题模糊时先用选项让用户确认（覆盖范围 / 目标读者 / 难度）。
- **分级自定**：不硬套 L0–L5，按任务自定（如 `basics / practice / advanced`），同一分级同一目录。
- **标准项目结构**：`page/`（内容，唯一真相）+ `script/`（脚本）+ `build/`（产物，gitignore）+ `plugin/`、`test/`（扩展位）。
- **本地预览**：mkdocs-material，一条命令 `./script/serve.sh` 起本地站点。
- **远端发布**：`./script/publish-wiki.sh` 一键把 `page/**` 拍平推送到 GitHub Wiki。
- **配图规范**：官方图优先，找不到可靠图用 Mermaid。
- **增量更新**：合并更新 + changelog。

## 项目结构（标准）

```text
<wiki-root>/
├── page/            # 源页面（唯一真相），按分级子目录组织
├── script/          # 版本化脚本：build.py / serve.sh / publish-wiki.sh / mkdocs.yml
├── build/           # 构建产物（gitignore）：preview/.venv docs site
├── plugin/          # 扩展位（预留）
├── test/            # 扩展位（预留）
└── README.md / .gitignore / LICENSE
```

详见 [references/project-structure.md](references/project-structure.md)。

## 快速开始

安装后，用自然语言触发：

```text
帮我为 Docker 建立一个 GitHub Wiki 知识库
```

```text
为 Git 生成一份零基础学习路线，先只写入门级导论
```

```text
继续生成下一级，补全分支与合并
```

默认首批只生成最低一级导论；你可以显式要求"继续生成下一级"、"补全某级"等。

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
确认主题与分级 → 盘点现有 Wiki → 规划本批页面（等确认）→ 联网调研
→ 生成页面并更新导航/状态 → 本地预览自检 → 报告（预览地址 + 发布命令）
```

详细流程见 [SKILL.md](SKILL.md)。

## 仓库结构

```text
├── SKILL.md                         skill 主入口
├── README.md                        本文件
├── LICENSE
├── references/                      渐进式加载的详细规范
│   ├── level-framework.md           分级方案与目录组织
│   ├── project-structure.md         项目结构规范
│   ├── page-templates.md            页面模板
│   ├── wiki-conventions.md          命名、导航、链接、更新规则
│   ├── research-and-sources.md      联网调研与来源记录
│   ├── figure-conventions.md        配图与 Mermaid 规范
│   ├── build-and-publish.md         本地预览与远端发布
│   └── templates/                   build.py / serve.sh / publish-wiki.sh / mkdocs.yml / .gitignore
└── examples/
    └── minimal-wiki/                最小 Wiki 样例
```

## 自定义

- 修改分级方案：编辑 `references/level-framework.md`。
- 修改页面模板：编辑 `references/page-templates.md`。
- 修改项目结构：编辑 `references/project-structure.md`。
- 修改配图规则：编辑 `references/figure-conventions.md`。
- 修改预览/发布脚本：编辑 `references/templates/`。
- 修改调研工具：编辑 `references/research-and-sources.md`。

## 与上游的关系

本仓库是 [tutorial-skill](https://github.com/YanZephyr14/tutorial-skill) 的 fork，保留了单篇教程的类比优先、需求驱动、真实案例三大写作原则，并新增分级、项目结构、预览发布与配图能力。

## License

MIT
