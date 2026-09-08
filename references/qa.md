# QA / Automated Checks

validator 输出机器可读（JSON）和可读（Markdown）两份 QA report。

## 检查清单

```text
[ ] Mode compliance
[ ] Source hierarchy compliance
[ ] Terminology consistency
[ ] English terminology preservation
[ ] Abbreviation definition
[ ] Claim evidence coverage
[ ] Unsupported claim detection
[ ] Figure explanation coverage
[ ] Figure source coverage
[ ] Broken figure links
[ ] Equation source coverage
[ ] Source vs explanation separation
[ ] Missing source section
[ ] Missing source figure
[ ] Missing equation
[ ] Missing example
[ ] Missing terminology
[ ] Orphan concept
[ ] Dead Wiki links
[ ] Sidebar completeness
[ ] Home completeness
[ ] META completeness
[ ] Course LO coverage
[ ] Stale external source
```

（外部 URL 有效性、Stale external source 需要联网，runner 无网络时标记 `unverified`，不当作通过。）

## 输出约定

`script/validate.py` 生成：

- stdout：人类可读总结。
- `build/qa-report.json`：机器可读（checks 数组、errors/warnings、summary）。
- 可选 `docs/qa-report.md`：人类可读详细报告。

## 报告字段

每项 check 至少包含：`id`, `name`, `status`（pass/warn/error/skip）, `detail`, `items`。