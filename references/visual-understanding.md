# PDF / PPT / 文档视觉理解（Visual Capability-Aware Workflow）

PDF / PPT / document ingestion 不允许只做 text extraction。必须按能力分级处理：

## 每页/每页 slide 分析

每页至少分析：slide/page number、headings、body text、equations、tables、figures、plots、diagrams、screenshots、arrows、highlighting、annotations、spatial relationships。

## Visual-only content

如果某页 extracted text 很少但有图，**不能判定为“没有内容”**，必须读取 rendered page。

## Capability-aware 分级

- IF runtime 支持 rendered-page/image inspection（如 modlens、视觉模型、OCR+layout）：必须读取 visual layer，记录 visual_summary。
- ELSE：标记 `visual_evidence_status: unverified`，不得假装已检查图片。coverage report 明确列出该项。

## Slide Evidence Record

每页可形成：

```yaml
slide_number: 15
text_summary: ...
visual_summary: ...
key_claims: [C01]
terms: [选择压力]
equations: [EQ01]
figures: [F01]
tables: []
scope_notes: []
```

## 实现边界

- 无法自动裁图时，可生成 extraction manifest，但状态标为 `Specified/Partial`，不得标为 `Implemented`。
- Modlens / OCR / 布局模型属于 runtime 能力；Skill 只提供 workflow 与记录规范，不凭空创造底层工具。