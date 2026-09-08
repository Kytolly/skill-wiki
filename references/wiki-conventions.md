# GitHub Wiki 组织规范

本文件定义页面命名、导航、链接、provenance 与更新规则。目录结构与元数据见 references/project-structure.md。

## 目录结构（源文件在 page/ 内，元数据在 _meta/ 内）

```text
page/
├── Home.md             领域总览 + 知识地图
├── _Sidebar.md         完整导航树
├── _Footer.md          版权/反馈（可选）
├── _META.md            状态：mode、受众、policy、页面清单、changelog
└── <grade>/<topic>.md
_meta/
├── terminology.yaml / evidence.yaml / claims.yaml / concepts.yaml
├── figures.yaml / equations.yaml / source-inventory.yaml / omissions.yaml
└── status.yaml
```

## 页面命名规则

- 分级目录名（grade slug）：ASCII 小写短横线。
- 页面文件名：主题名，不带分级前缀。
- `page/` 内 basename 必须唯一（预览与发布都会拍平）。
- 同一页面在 `_Sidebar.md`、正文链接、`_META.md`、`_meta/*.yaml` 的 page 字段中一致。

## Home.md 的职责

- 一句话说明讲什么、给谁看、采用哪种 wiki_mode。
- 给出知识地图：分级/阶段目标、主要页面、完成标准。
- 说明分级与 mode 的 source/completeness policy。
- 链接已有页面；未生成的分级标注“规划中”。

## _Sidebar.md 的职责与格式

```text
**Home**

**入门（basics）**
- [[Git是什么与第一次提交]]

**规划中**
- 实战（practice）
```

规则：侧边栏反映真实完成状态；“规划中”只列分级名，不创建死链。

## _META.md 的职责

至少包含：

- 领域名称、目标读者、wiki_mode、audience。
- 各项 policy：source_policy、source_hierarchy、terminology_policy、evidence_policy、figure_policy、completeness_policy、external_knowledge_policy。
- `last_source_audit`、`last_coverage_audit`。
- 页面清单：页面名、所属分级目录、状态、最后更新日期。
- changelog。

示例：

```text
# Wiki 状态

- 领域：Git
- 读者：零基础
- wiki_mode: technical-tutorial
- audience: 零基础开发者
- source_policy: official docs first
- source_hierarchy: official > trusted web > general
- terminology_policy: preserve canonical English
- evidence_policy: every important claim traceable
- figure_policy: official figure first, else Mermaid
- completeness_policy: minimum viable learning path
- external_knowledge_policy: merge update, never silently replace
- last_source_audit: 2026-01-02
- last_coverage_audit: 2026-01-02

## 页面清单
- [x] basics/Git是什么与第一次提交（2026-01-01）

## changelog
- 2026-01-02：升级为 evidence-grounded mode。
```

## 链接规则

- 互链用 `[[页面名]]`，页面名 = 文件名去 .md。
- 每页有“上一页 / 下一页 / 返回 Home”。
- 不创建指向不存在页面的链接。
- 外部资料用普通 Markdown 链接，注明访问日期。

## Provenance 与更新规则

- 页面级 `## 更新日志` 保留。
- section-level provenance 标签见 references/provenance.md（source-derived / agent-explanation / external-research / user-correction / derived）。
- 已有页面用合并更新，不整页覆盖。
- 更新后在 `_META.md` changelog 追加一条，并更新 `last_verified`。
- legacy 页面无 `_meta/` 证据时标 `provenance: legacy-unverified`，不删除。