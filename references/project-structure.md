# 项目结构规范

本文定义 wiki 项目的标准目录结构。目标：**清晰、解耦、可扩展、职责分明**。

## 标准结构

```text
<wiki-root>/
├── page/                  # 唯一真相：教程源页面（Markdown）
│   ├── Home.md            # 领域总览 + 学习地图（Knowledge Map）
│   ├── _Sidebar.md        # 完整导航树（GitHub Wiki 用）
│   ├── _META.md           # 状态：mode、受众、policy、页面清单、changelog
│   ├── _Footer.md         # 版权/反馈（可选）
│   ├── assets/            # 本地图片/图床素材
│   │   ├── images/
│   │   └── figures/
│   └── <grade>/           # 同一分级同一目录
│       └── <topic>.md
├── _meta/                 # 内容元数据（committed，被 validator/coverage/build 消费）
│   ├── terminology.yaml   # 术语索引
│   ├── evidence.yaml      # Evidence Object
│   ├── claims.yaml        # Claim Object
│   ├── concepts.yaml      # 概念 + Knowledge Graph 关系
│   ├── figures.yaml       # Figure Object
│   ├── equations.yaml     # Equation Object
│   ├── source-inventory.yaml
│   ├── omissions.yaml
│   └── status.yaml        # 迁移/视觉提取状态
├── plugin/                # 扩展位：插件（预留，.gitkeep 占位）
├── script/                # 版本化脚本（构建/预览/发布/校验/覆盖度/迁移）
│   ├── build.py           # page/** → build/preview/docs（拍平+转 [[链接]]）
│   ├── serve.sh           # 本地预览入口
│   ├── publish-wiki.sh    # 拍平推送到 GitHub Wiki
│   ├── validate.py        # QA / 一致性校验（机器+人类可读）
│   ├── coverage.py        # Source vs Wiki 覆盖度审计
│   ├── migrate.py         # legacy → 新元数据迁移
│   └── mkdocs.yml         # 本地预览配置
├── test/                  # fixtures + 自动化测试
│   ├── fixtures/
│   │   ├── course/
│   │   ├── project-docs/
│   │   ├── lab-sop/
│   │   └── technical-tutorial/
│   └── test_skill.py
├── docs/                  # 生成/维护文档（capability-matrix.md 等）
├── build/                 # 构建产物（.gitignore 忽略，不提交）
│   └── preview/
├── README.md
├── LICENSE
└── .gitignore
```

## 职责边界（解耦原则）

| 目录 | 职责 | 谁改 | 是否提交 |
|------|------|------|----------|
| `page/` | 教程内容（唯一真相） | 内容编辑 | ✅ |
| `_meta/` | 内容元数据与证据/术语/图/公式/覆盖度 | 内容编辑 | ✅ |
| `script/` | 构建/预览/发布/校验/覆盖度/迁移工具 | 工具维护 | ✅ |
| `build/` | 生成产物（.venv/docs/site/log） | 脚本自动 | ❌ |
| `plugin/`、`test/` | 扩展槽位与测试 | 按需 | ✅ |

规则：**内容只改 page/ 与 _meta/，工具只改 script/，产物只在 build/**。

## 为什么这样设计

- `page/` 与构建解耦：换渲染器（mkdocs/docsify/GitHub Wiki）都不动内容。
- `_meta/` 是 evidence/terminology/figure 的持久化层，被 validation/coverage/build 真实消费。
- `script/` 版本化：换机器也能复现预览、校验与发布。
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
__pycache__/
*.py[cod]
```

注意：`_meta/` 会提交，不放入 .gitignore。