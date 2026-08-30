# 项目结构规范

本文定义 wiki 项目的标准目录结构。目标：**清晰、解耦、可扩展、职责分明**。

## 标准结构

```text
<wiki-root>/
├── page/                  # 唯一真相：教程源页面（Markdown）
│   ├── Home.md            # 领域总览 + 学习地图
│   ├── _Sidebar.md        # 完整导航树（GitHub Wiki 用）
│   ├── _META.md           # 状态：主题、分级、页面清单、changelog
│   ├── _Footer.md         # 版权/反馈（可选）
│   └── <grade>/           # 同一分级同一目录
│       └── <topic>.md     # 页面文件名=主题，不带分级前缀
├── plugin/                # 扩展位：插件（预留，.gitkeep 占位）
├── script/                # 版本化脚本（构建/预览/发布）
│   ├── build.py           # page/** → build/preview/docs（拍平+转 [[链接]]）
│   ├── serve.sh           # 本地预览入口
│   ├── publish-wiki.sh    # 拍平推送到 GitHub Wiki
│   └── mkdocs.yml         # 本地预览配置
├── test/                  # 扩展位：测试（预留，.gitkeep 占位）
├── build/                 # 构建产物（.gitignore 忽略，不提交）
│   └── preview/           # .venv / docs / site / 日志
├── README.md
├── LICENSE
└── .gitignore
```

## 职责边界（解耦原则）

| 目录 | 职责 | 谁改 | 是否提交 |
|------|------|------|----------|
| `page/` | 教程内容（唯一真相） | 内容编辑 | ✅ |
| `script/` | 构建/预览/发布工具 | 工具维护 | ✅ |
| `build/` | 生成产物（.venv/docs/site/log） | 脚本自动 | ❌ |
| `plugin/`、`test/` | 扩展槽位 | 按需 | ✅（.gitkeep） |

规则：**内容只改 page/，工具只改 script/，产物只在 build/**。

## 为什么这样设计

- `page/` 与构建解耦：换渲染器（mkdocs/docsify/GitHub Wiki）都不动内容。
- `script/` 版本化：换机器也能复现预览与发布。
- `build/` 可随时删除重建：`rm -rf build && ./script/serve.sh`。
- `plugin/`、`test/` 给未来扩展留位置，不塞进 page/。

## .gitignore 模板

见 `references/templates/.gitignore`，至少忽略：

```text
build/
.venv/
.obsidian/
site/
docs/
*.log
```
