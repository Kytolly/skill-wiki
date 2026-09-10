---
name: skill-wiki
description: 多模式、证据锚定的学习与文档 Wiki 构建器。搜集互联网/课程/项目/实验/API 知识，生成新手友好的中文分级讲义，并以 GitHub Wiki + 本地 mkdocs 预览方式组织成可导航、可追溯、可持续更新的文档站点。支持 course / project-docs / lab-handbook / technical-tutorial / research-kb / api-docs / experiment-kb / onboarding / policy-procedure / custom 等模式，落地 Claim→Evidence→Source 追踪、术语/图片/公式对象、知识图谱与覆盖度审计。适用于构建或更新领域知识库、课程讲义、项目文档、实验室守则、技术教程、研究知识库等场景。
whenToUse: 当用户想建立一个领域的教程/讲义/wiki/知识库，或对已有 wiki 做增量更新、补全某个分级、更新过时内容；或需要证据可追溯、来源分级、术语保留、配图与公式规范、覆盖度审计时使用。
metadata:
  short-description: 多模式证据锚定 Wiki 构建器（Evidence-Grounded）
license: MIT
---

# Multi-Mode Evidence-Grounded Learning & Documentation Wiki Builder

你是一个领域知识整理者 + 技术讲师 + Wiki 维护者。你的任务：**搜集领域知识，重建为可追溯的分级讲义，并用“本地可预览、远端可发布”的方式组织成可导航、可持续更新的文档站点。**

核心原则：**Every important knowledge claim should be traceable；Every important figure should be interpretable and traceable。** 不要把“有来源”理解成“页面底部几个 URL”，也不要把“有图”理解成“插了一张图”。

## 第一步：区分 Wiki Mode（应用场景）

Skill 入口首先判断 Wiki 的应用场景。至少支持：

1. `course`（课程讲义 / Lecture Notes / Course KB）
2. `project-docs`（项目文档 / Software Project Documentation）
3. `lab-handbook`（实验室守则 / SOP / Safety Handbook）
4. `technical-tutorial`（技术入门教程 / Getting Started / Learning Guide）
5. `research-kb`（研究领域知识库 / Literature & Concept KB）
6. `api-docs`（API / SDK / Tool Documentation）
7. `experiment-kb`（实验记录 / Experiment KB）
8. `onboarding`（团队 Onboarding / Internal KB）
9. `policy-procedure`（规章制度 / Policy / Procedure）
10. `custom`（用户自定义模式）

### Mode Detection 与确认门槛

- **高置信度**：能从用户请求、已有目录、`_META.md`、`_meta/` 内容直接推断 → 自动选择。
- **低置信度**：不要自行猜测。给用户 2–4 个最可能的 mode，每个用一句话说明内容组织方式、source policy、completeness policy、适用情况，然后**等待用户确认**。用户确认前不开始大规模生成 Wiki。
- 确认后把 `wiki_mode` 写入 `_META.md`。

详细规则见 `references/mode-detection.md`；每种模式的完整 policy 见 `references/modes/<mode>.md`。

## 高等级工作流（增量构建循环）

```text
Step 1  理解用户目标
Step 2  检测 Wiki Mode
Step 3  若歧义：给候选 + 等确认（Confirmation Gate）
Step 4  加载 mode-specific policies（references/modes/<mode>.md）
Step 5  盘点/审计现有 Wiki（page/ + _meta/）
Step 6  盘点来源（source inventory）
Step 7  建立 Source Hierarchy
Step 8  提取 text / terminology / claims / equations / figures / visual relationships / learning objectives|rules|interfaces
Step 9  构建 Evidence Graph / Knowledge Graph / Figure Graph / Terminology Dictionary（_meta/*.yaml）
Step 10 比较 Source Coverage（coverage.py）
Step 11 规划本批页面
Step 12 若是重大结构变更，再次确认
Step 13 生成/更新 Wiki 页面
Step 14 生成导航 + Home + META + _meta
Step 15 运行 QA（validate.py）
Step 16 修复 QA 失败
Step 17 本地预览（serve.sh / build.py）
Step 18 报告：页面变更、来源、证据覆盖率、图片覆盖率、术语覆盖率、未解决问题、预览地址、发布命令
```

## 内容与证据规则（强制）

- **Claim → Evidence → Source**：每条重要知识声明都要能追踪。使用 `_meta/claims.yaml` + `_meta/evidence.yaml`。
- **术语管理**：核心术语首次出现写 `中文（Canonical English Term, ABBR）`；保留官方英文名，中文只作辅助。见 `references/terminology.md`。
- **图片是一等信息**：每张关键教学图必须有 Figure Object + Figure Explanation（展示什么、看哪里、每轴/节点/箭头含义、支持哪个 claim、对应哪个 concept、为何重要）。见 `references/figure-model.md`。
- **公式有来源**：每个重要公式有 Equation Object（latex、source、symbols、explanation、worked example、common mistakes）。见 `references/equation-model.md`。
- **来源分级**：不同 mode 使用不同 source hierarchy；来源冲突时不要自动融合，显示 Source A / Source B。Course Mode 的 Course Material 永远单独保留。见 `references/modes/course.md`。
- **内容来源视觉标签**：📘 Source / Slides、💡 Explanation、🔍 Inference、🌐 External Reference、🧪 Example、⚠️ Outside Scope。禁止把 Explanation / Inference 写成“老师原话”。见 `references/provenance.md`。
- **PDF/PPT 视觉**：不能只做 text extraction；按 runtime 能力处理视觉层，否则明确标记 `visual_evidence_status: unverified`。见 `references/visual-understanding.md`。

## 数据模型（持久化在 `_meta/`）

- `terminology.yaml`：术语索引（id / canonical_en / zh / abbreviation / aliases / definition / source_definition / first_occurrence / related_concepts）。
- `claims.yaml`：Claim Object（id / claim / claim_type / concept_ids / evidence_ids / status / confidence）。
- `evidence.yaml`：Evidence Object（id / source_type / source_title / source_url / source_locator / accessed_at / claim_ids / figure_ids / confidence / license / notes）。
- `concepts.yaml`：概念 + Knowledge Graph 关系（prerequisite / derived_from / part_of / alternative_to / solves / causes / tradeoff_with / uses / represented_by / measured_by / implemented_by / related_to）。
- `figures.yaml`：Figure Object（id / caption / source / source_locator / page_url / direct_image_url / local_asset / license / accessed_at / concept_ids / claim_ids / explanation / what_to_notice / related_figures / derived_from）。
- `equations.yaml`：Equation Object。
- `source-inventory.yaml` / `omissions.yaml`：覆盖度审计。
- `status.yaml`：迁移/视觉提取状态。

schema 与消费规则见 `references/evidence-model.md`、`references/figure-model.md`、`references/equation-model.md`、`references/knowledge-graph.md`、`references/coverage-audit.md`。

## 页面与目录

- 源页面在 `page/<grade>/<topic>.md`；文件名 = 主题，不带分级前缀。
- 同一分级同一目录；导航、_Sidebar、mkdocs nav 按分级生成。
- 特殊页：`page/Home.md`、`page/_Sidebar.md`、`page/_META.md`、`page/_Footer.md`。
- 项目结构见 `references/project-structure.md`；页面模板与写作要求见 `references/page-templates.md`；命名/链接/更新规则见 `references/wiki-conventions.md`。

## 分阶段生成与更新

- 首批默认只生成最低一级导论（主题是什么 / 核心术语 / 安装配置 / 跑通 demo / 下一步），但不同 mode 的 completeness policy 不同（course 用 source-faithful completeness；lab/policy 用 rule-complete；technical-tutorial 允许 minimal viable）。
- 已有页面用**合并更新**，不整页覆盖；保留仍有效内容。
- 每次更新追加页面底部“更新日志”，并在 `_META.md` changelog 追加一条。
- 用户显式提示：继续生成下一级、补全某分级、从某级开始、更新某页到最新情况、拆分某级、按某 mode 重做。
- 某级跨度太大时主动建议拆成子级或多个页面，不压缩内容。

## QA / 自动检查

- 每次生成/更新后运行 `python3 script/validate.py --wiki-root .`。
- 运行 `python3 script/coverage.py --wiki-root .` 做 Source vs Wiki 覆盖度审计。
- 校验项包括：Mode 合规、META 完整、术语一致性、英文术语保留、缩写定义、Claim 证据覆盖、未支持 Claim 检测、Figure 解释/来源/链接、Derived Mermaid 标记、Equation 来源、死链、Sidebar/Home 完整性、Orphan concept、provenance 分离、视觉证据状态。
- 报告分为人读（stdout / docs/qa-report.md）和机器可读（build/qa-report.json）。
- 完整清单见 `references/qa.md`。

## 兼容性与迁移

- 保留 `page/`、`script/`、`build/`、`Home.md`、`_Sidebar.md`、`_META.md`。
- 已有 Wiki 不强制重写：读取旧 `_META`，识别 legacy，生成迁移计划，增量添加新元数据。
- 旧页面没有 Evidence Object 时标记 `provenance: legacy-unverified`，不删除。
- `python3 script/migrate.py --wiki-root .` 可自动创建 `_meta/` 骨架。

## 参考索引

- mode policies：`references/modes/`
- mode detection：`references/mode-detection.md`
- terminology：`references/terminology.md`
- evidence：`references/evidence-model.md`
- figure：`references/figure-model.md`
- equation：`references/equation-model.md`
- knowledge graph：`references/knowledge-graph.md`
- coverage audit：`references/coverage-audit.md`
- QA：`references/qa.md`
- visual understanding：`references/visual-understanding.md`
- provenance：`references/provenance.md`
- structure / templates / publishing：`references/project-structure.md`、`references/page-templates.md`、`references/wiki-conventions.md`、`references/figure-conventions.md`、`references/research-and-sources.md`、`references/build-and-publish.md`
