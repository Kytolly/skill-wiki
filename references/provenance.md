# Provenance（来源标注与版本）

## 页面级 changelog

保留现有 `## 更新日志`。

## Section-level provenance

页面内每个内容来源用以下标签标注：

- `source-derived`：来自源。
- `agent-explanation`：Agent 解释。
- `external-research`：外部资料。
- `user-correction`：用户纠正。
- `derived`：衍生/重绘。

## 版本与陈旧标记

- 页面或 section 记录 `source_version`、`last_verified`、`stale_flag`。
- 内容主要来自课程幻灯片时，标注 `source_version` 与 `last_verified`。
- 外部来源长期未复核时置 `stale_flag: true`，并在页面顶部提示。

## 迁移（legacy）

- 已有页面没有 `_meta/` 时：标 `provenance: legacy-unverified`，而不是删除。
- migrate.py 检测 legacy wiki 并生成迁移计划：新增 `_meta/` 骨架 + 在 `_META.md` 记录迁移状态。