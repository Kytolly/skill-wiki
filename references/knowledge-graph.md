# 知识图谱（Knowledge Graph）

页面互链只是 Navigation Graph。新增 Knowledge Graph，记录概念之间的语义关系。

## Concept Relationship 类型

至少支持：`prerequisite`, `derived_from`, `part_of`, `alternative_to`, `solves`, `causes`, `tradeoff_with`, `uses`, `represented_by`, `measured_by`, `implemented_by`, `related_to`。

## 存储（`_meta/concepts.yaml`）

```yaml
- id: C02
  name_zh: 选择压力
  name_en: Selection Pressure
  aliases: [选择压力]
  definition_zh: 进化算法中影响收敛速度与多样性的机制。
  page: page/basics/xxx.md
  evidence_ids: [E01]
  figure_ids: [F01]
  equation_ids: [EQ01]
  related: [
    {concept_id: C01, relation: prerequisite}
    {concept_id: C03, relation: tradeoff_with}
  ]
```

## 关系图

支持 Concept → Equation / Figure / Evidence / Example / Exercise / Lecture/Page。

## 生成物（validator/coverage 输出）

- Concept Dependency Graph（markdown/mermaid 列表）
- Backlinks
- Related Concepts
- Orphan Concept report（概念无 page / 无证据 / 无关联）
- Broken relation report（relation 指向不存在的 concept_id）