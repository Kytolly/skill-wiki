# 图片 / 视觉知识模型（Figure Model）

核心原则：`Every important figure should be interpretable and traceable.`

## Figure Object（`_meta/figures.yaml`）

```yaml
- id: F01
  caption: 选择压力与种群多样性的关系
  source_type: course_slide
  source: Lecture 4, Slide 15
  source_locator: "figure region：右下图"
  page_url: https://example.com/page
  direct_image_url: https://example.com/img.png
  local_asset: page/assets/images/F01.png
  license: "CC BY-NC"
  accessed_at: "2026-01-02"
  concept_ids: [C02]
  claim_ids: [C01]
  explanation: 横轴是种群多样性，纵轴是适应度；箭头表示选择压力增大的方向。
  what_to_notice: 注意曲线在压力过大时迅速收敛到局部最优。
  related_figures: [F02]
  derived_from: []
```

## Figure Explanation 必须回答的问题

1. 图展示什么？
2. 应该重点看哪里？
3. 每个轴 / 节点 / 箭头 / 区域是什么意思？
4. 图支持什么 claim？
5. 和哪个 concept 对应？
6. 为什么这张图值得放在这里？

禁止：只插 `![图](...)` + caption + source，然后完全不解释。

## 页面内引用约定

- 在图片所在行前加 `<!-- FIGURE: F01 -->`，validator 据此定位。
- 配图必须有 caption + 来源 + 访问日期。
- Course Mode 的课件图要记录 Lecture / Slide / Page / Figure region；必要时裁切关键 figure 而非整页截图。

## External Image 规则

外部图片必须同时记录 `page_url`、`direct_image_url`、`license/attribution`、`access_date`。禁止只保存 direct image URL。

## Derived Mermaid / 重绘图

- Mermaid 是 Derived Illustration，不是 source evidence。
- 必须标注：`本图由 Wiki 根据 E12/E13/E14 重绘`，并保存 `derived_from: [E12, E13]`。
- 如果 Mermaid 是 Agent 自己的教学抽象，明确标注：`Conceptual illustration; not present in source.`

## Figure Citation Graph

建立 Concept ↔ Figure ↔ Claim ↔ Evidence ↔ Source。支持 Concept→Figure、Figure→Claim、Figure→Source Slide、Figure→Original URL、Figure→Related Figure。

生成 `Figure Index`（validator/coverage 输出），Course Mode 可生成“课程关键图索引”。