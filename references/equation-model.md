# 公式管理（Equation Model）

## Equation Object（`_meta/equations.yaml`）

```yaml
- id: EQ01
  latex: "P_i = f_i / \\sum_j f_j"
  source: Lecture 5, Slide 8
  source_locator: "公式 3"
  concept_ids: [C03]
  symbols: [P_i, f_i, f_j]
  explanation: P_i 是个体被选中的概率，f_i 是适应度。
  worked_example: "f = [2, 4]，sum=6，则 P = [1/3, 2/3]"
  common_mistakes: ["忘记归一化", "把 f_j 写成 f_i"]
```

## 公式展示

每个重要公式尽可能包含：Formal equation → Meaning → Symbol table → Intuition → Worked example → Common mistake → Source。

## 页面内引用约定

- 在公式块前加 `<!-- EQUATION: EQ01 -->`，validator 据此定位。

## Source Fidelity

- 不要静默“修正”老师公式。
- 若怀疑公式有 typo：分开写 Slides 原公式 + External/Inference 的可能问题，不要合并。