# 术语管理（Terminology）

目标：专业英文术语不得在中文讲解中丢失，且要有规范化的表示、持久化与一致性校验。

## 规范表示

核心术语首次出现：`中文名称（Canonical English Term, ABBR）`。

示例：`选择压力（Selection Pressure）`、`遗传算法（Genetic Algorithm, GA）`、`模拟二进制交叉（Simulated Binary Crossover, SBX）`。

后续正文允许优先使用英文 canonical term 或缩写（`Selection Pressure` / `GA` / `SBX`）。不要为了中文流畅度删除英文 canonical term。

## 不强制翻译

Algorithm / API / Paper / Library / Tool / Formal Method 名称保留官方英文名，中文只作辅助解释。

## Glossary（术语索引）

存储于 `_meta/terminology.yaml`。每个 term 至少包含：

```yaml
- id: T01
  canonical_en: Selection Pressure
  zh: 选择压力
  abbreviation: SP
  aliases: [选择压力]
  definition: 进化算法中，选择压力越大，适应度高的个体越容易留下后代。
  source_definition: 来自课件/文档的原句或摘要。
  first_occurrence: page/basics/xxx.md
  related_concepts: [C02, C03]
```

## 正文渲染约定

- 有缩写：`选择压力（Selection Pressure, SP）`。
- 无缩写：`选择压力（Selection Pressure）`。
- 页面第一次用到某术语时使用完整形式；之后可用缩写。
- 术语定义优先来自 source；Agent 的补全属于 explanation，不要把 Agent 解释写成 source 原话。

## Terminology QA（validator 执行）

- 同一英文术语是否出现多个中文译名。
- abbreviation 是否先定义后使用。
- 核心英文术语是否丢失（页面只写中文、没有 canonical_en 也没有缩写）。
- source 中重要 terminology 是否未进入 Wiki（coverage audit 检查）。
- canonical term 是否被擅自改写。