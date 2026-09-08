# skill-wiki

一个 AI skill：**多模式、证据锚定的学习与文档 Wiki 构建器**。搜集互联网/课程/项目/实验/API 知识，生成新手友好的中文分级讲义，并以 **本地 mkdocs 预览 + GitHub Wiki 发布** 方式组织成可导航、可追溯、可持续更新的文档站点。

> 本仓库 fork 自 [tutorial-skill](https://github.com/YanZephyr14/tutorial-skill)，在“零基础单篇教程”能力之上，扩展为多模式证据锚定的 Wiki 构建器。

## 它能做什么？

- **多 Mode**：course / project-docs / lab-handbook / technical-tutorial / research-kb / api-docs / experiment-kb / onboarding / policy-procedure / custom。
- **Mode 确认门槛**：模式不明确时给候选并等用户确认，不擅自生成。
- **Claim → Evidence → Source 追踪**：每条重要知识声明可追溯。
- **术语管理**：`中文（Canonical English Term, ABBR）`，保留官方英文名。
- **图片/公式作为一等知识**：Figure Object + Figure Explanation，Equation Object + provenance。
- **知识图谱**：概念关系（prerequisite / tradeoff_with / implements 等）+ 孤儿概念检测。
- **覆盖度审计**：Source vs Wiki outline 比较，输出 missing/covered/omitted。
- **QA 校验**：`script/validate.py` 输出机器可读（JSON）+ 人可读（Markdown）报告。
- **本地预览 + GitHub Wiki 发布**：`script/serve.sh`、`script/publish-wiki.sh`。
- **legacy 迁移**：`script/migrate.py` 自动为旧 wiki 建立 `_meta/` 并标记 `legacy-unverified`。

## 核心原则

- **Every important knowledge claim should be traceable.**
- **Every important figure should be interpretable and traceable.**
- 不要把所有 Wiki 都当“新手教程”。
- 不要用通用知识静默“修正”课程/规范。
- 不要为了中文流畅度删除英文 canonical terminology。

## 项目结构（标准）

```text
<wiki-root>/
├── page/                  # 唯一真相：源页面（Markdown），按分级子目录组织
├── _meta/                 # 内容元数据：terminology/evidence/claims/concepts/figures/equations/inventory/status
├── script/                # 工具：build.py / serve.sh / validate.py / coverage.py / migrate.py / publish-wiki.sh / mkdocs.yml
├── test/                  # fixtures + 自动化测试
├── docs/                  # 生成文档（capability-matrix.md 等）
├── build/                 # 构建产物（gitignore）
└── README.md / LICENSE / .gitignore
```

详见 [references/project-structure.md](references/project-structure.md)。

## 快速开始

安装后，用自然语言触发：

```text
帮我为 Git 建立 technical-tutorial 模式的知识库，先只写入门导论
```

```text
把这门课的 PPT 整理成 course 模式的讲义，保留所有考试内容
```

```text
为 StackForce 机器狗建立 lab-handbook + technical-tutorial 混合 wiki
```

模式不明确时，skill 会给你 2–4 个候选并等你确认。

## 安装

### 全局安装

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

## 工作流

```text
理解目标 → 检测 Wiki Mode →（歧义则确认）→ 加载 mode policy → 盘点现有 Wiki/来源
→ 建立 Source Hierarchy → 提取 术语/声明/证据/图/公式 → 构建证据/知识/图/术语图谱
→ 覆盖度审计 → 规划页面 → 生成/更新页面与 _meta → 运行 validate + coverage → 本地预览 → 报告
```

## 常用命令

```bash
# 校验（机器 + 人可读 QA）
python3 script/validate.py --wiki-root .

# 覆盖度审计
python3 script/coverage.py --wiki-root .

# legacy 迁移
python3 script/migrate.py --wiki-root .

# 本地预览
./script/serve.sh

# 发布到 GitHub Wiki
./script/publish-wiki.sh
```

## Mode 一览

| Mode | 典型场景 | Completeness |
|------|----------|--------------|
| course | 讲义/课件 | source-faithful completeness |
| project-docs | 项目文档 | architecture/interface completeness |
| lab-handbook | 实验室守则/SOP | rule-complete |
| technical-tutorial | 入门教程 | minimum viable learning path |
| research-kb | 研究知识库 | evidence/literature coverage |
| api-docs | API 文档 | interface completeness |
| experiment-kb | 实验记录 | reproducibility |
| onboarding | 团队 onboarding | role-targeted completeness |
| policy-procedure | 规章制度 | rule-complete |
| custom | 用户自定义 | 由用户声明 |

详细 policy 见 [references/modes/](references/modes/)。

## 仓库结构

```text
├── SKILL.md                       skill 主入口（mode detection + workflow）
├── README.md                      本文件
├── LICENSE
├── references/
│   ├── modes/                     每种 wiki mode 的 policy
│   ├── mode-detection.md          模式检测与确认门槛
│   ├── terminology.md             术语管理
│   ├── evidence-model.md          Claim/Evidence 模型
│   ├── figure-model.md            图片模型
│   ├── equation-model.md          公式模型
│   ├── knowledge-graph.md         知识图谱
│   ├── coverage-audit.md          覆盖度审计
│   ├── qa.md                      QA 清单
│   ├── visual-understanding.md    PDF/PPT 视觉理解
│   ├── provenance.md              provenance/迁移
│   ├── project-structure.md       项目结构
│   ├── page-templates.md          页面模板
│   ├── wiki-conventions.md        Wiki 命名/导航/更新
│   ├── figure-conventions.md      配图与 Mermaid 规范
│   ├── research-and-sources.md    调研与来源记录
│   ├── build-and-publish.md       本地预览与发布
│   └── templates/                 可复制的脚本与配置模板
├── script/                        可直接运行的校验/覆盖/迁移/构建/预览/发布脚本
├── test/                          4 类 fixture + 自动化测试
├── docs/capability-matrix.md      能力矩阵
└── examples/minimal-wiki/         完整的最小 Wiki 示例（含 _meta）
```

## 测试

```bash
python3 -m unittest discover -s test -p "test_*.py" -v
```

覆盖：4 类合法 fixture 校验/覆盖通过、故意的负向检测（unsupported claim / figure 无说明 / broken link / META 缺失 / 术语丢失）、legacy 迁移。

## 与上游的关系

本仓库是 [tutorial-skill](https://github.com/YanZephyr14/tutorial-skill) 的 fork，保留了单篇教程的类比优先、需求驱动、真实案例原则，并扩展为多模式证据锚定 Wiki 构建器。

## License

MIT

