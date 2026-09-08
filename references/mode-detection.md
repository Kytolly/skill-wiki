# Wiki Mode 检测与确认门槛（Confirmation Gate）

## 检测策略

Skill 入口首先判断 Wiki 应用场景（mode）。

- 高置信度：从用户请求、已有目录、`_META.md`、`_meta/` 内容可直接推断 → 自动选择。
- 低置信度：**不要自行猜测**。给出 2–4 个最可能的 mode，每个用一句话解释内容组织方式、source policy、completeness policy、适用情况，然后等待用户确认。

用户确认前不要开始大规模生成 Wiki。

## 支持的模式

course / project-docs / lab-handbook / technical-tutorial / research-kb / api-docs / experiment-kb / onboarding / policy-procedure / custom。

每个模式的完整 policy 见 `references/modes/<mode>.md`。

## 确认后动作

- 把 `wiki_mode` 写入 `_META.md`。
- 按对应 mode 的 policy 加载 `references/modes/<mode>.md`。
- 若目标目录已是 legacy wiki，先读取旧 `_META` 并生成迁移计划（见 references/provenance.md / migrate.py）。