# 证据模型（Evidence Model）

核心原则：`Every important knowledge claim should be traceable.`

不再把“来源”理解为页面末尾几个 URL，而是为每条重要知识声明建立 Claim → Evidence → Source 的可追踪链。

## Evidence Object（`_meta/evidence.yaml`）

```yaml
- id: E01
  source_type: course_slide
  source_title: Lecture 4 - 选择压力
  source_file: lecture04.pdf
  source_url: https://example.com/lecture04
  source_locator: "slide 15"
  source_date: "2026-01-01"
  accessed_at: "2026-01-02"
  claim_ids: [C01, C02]
  figure_ids: [F01]
  extraction_method: text-layer + rendered-page
  confidence: high
  license: "CC BY-NC"
  notes: "老师口头补充，PPT 未写"
```

source_type 支持：`course_slide`, `course_note`, `user_document`, `official_documentation`, `primary_paper`, `book`, `project_source`, `web_page`, `external_image`, `generated_diagram`, `derived`, `user_statement`。

source_locator 支持：`slide number`, `PDF page`, `section`, `heading`, `figure number`, `table number`, `code file + line`, `URL fragment`, `repository commit`。

## Claim Object（`_meta/claims.yaml`）

```yaml
- id: C01
  claim: 选择压力过高可能导致过早收敛。
  claim_type: source-derived
  concept_ids: [C02]
  evidence_ids: [E01, E02]
  status: verified
  confidence: high
```

## 四种内容来源的视觉标签

页面正文用以下标签明确区分内容来源：

- 📘 Source / Slides：来源直接支持。
- 💡 Explanation：Agent 对 source 的教学解释。
- 🔍 Inference：Agent 结合多个 evidence 的推导。
- 🌐 External Reference：来自课件/文档之外。
- 🧪 Example：示例。
- ⚠️ Outside Scope：课件明确说明不在范围。

禁止把 Explanation / Inference 写成“老师原话”。

## 正文引用约定

- 重要声明在正文用 `[C01]`、`[E01]` 形式的 inline evidence/claim reference。
- 页面末尾可放 Evidence Block，列出本页引用的 Claim/Evidence/Source。
- source metadata 不要大面积打断正文；教学在正文，验证放 Evidence Block / `<details>`。

## Claim → Evidence → Source 渲染示例

```text
选择压力太高可能导致 premature convergence。[C01]

## Evidence
<details><summary>E01</summary>
Source type: course_slide
Lecture 4 / Slide 15
Relevant statement: ...
</details>
```

## 自动检测（validator）

- Unsupported important claim：页面引用了 `[Cxx]`，但 claims.yaml 缺失，或 claim.evidence_ids 为空。
- Evidence ID 缺失：`[Exx]` 在 evidence.yaml 中找不到。
- Evidence 指向缺失 source：evidence.source_url/source_file 均缺失。