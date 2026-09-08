# 覆盖度审计（Coverage Audit）

实现 Source Outline vs Wiki Outline 的比较，检测缺失内容并生成报告。

## Source Inventory（`_meta/source-inventory.yaml`）

```yaml
- id: S01
  item_type: section
  item_name: 选择压力的定义
  source: Lecture 4
  locator: "slide 15"
  expected_page: page/basics/xxx.md
  status: covered
  omission_reason: null
```

## Omissions（`_meta/omissions.yaml`）

被显式跳过/延后的条目放在这里，避免被误判为缺失：

```yaml
- id: S02
  item_type: section
  item_name: 与下一讲重叠的章节
  source: Lecture 5
  omission_reason: 内容与实操页重复，延后到专项页。
```

## 比较逻辑

1. 从 source-inventory 读取源侧条目。
2. 从 page/ 提取已覆盖条目（依据 status / 页面 markers / 标题）。
3. 对每个条目：covered / omitted / missing。
4. missing 且无 omission_reason 时报告 MISSING。

## 检测项

Missing section / figure / equation / table / example / terminology / learning objective / evidence。

## 输出

- 人类可读：`docs/coverage-report.md`。
- 机器可读：`build/coverage-report.json`（status、missing 列表、覆盖率）。
- coverage.py 直接实现。