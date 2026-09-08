# 联网调研与来源记录规范

目标：为 Source hierarchy 提供可追踪证据；不再把来源当作“页面底部几个 URL”。

## 调研前：确定 mode 与 source policy

先确认 `wiki_mode`，再按 `references/modes/<mode>.md` 加载该模式的 source hierarchy 与 completeness policy。不同 mode 对来源优先级要求不同。

## 调研目标

- 确认本批页面技术信息准确且最新。
- 获取真实、可运行的代码示例和官方用法。
- 记录能支撑每条重要 claim 的 Evidence Object。
- 找到配图素材，并记录 figure 来源。

## 调研方式（按可用工具选择）

- 用可用的联网搜索工具（web_search / Tavily / WebSearch 等）搜索。
- 抓取官方文档、官方教程、权威教材或知名社区教程。
- 涉及编程库/框架时查询最新文档与版本说明。
- 视觉证据（PDF/PPT）按 references/visual-understanding.md 处理：有渲染能力就读视觉层，否则标记 unverified。

## 证据记录

- 为每个重要 source 创建 Evidence Object（`_meta/evidence.yaml`）：source_type、source_title、source_locator、source_url/source_file、accessed_at、claim_ids、figure_ids。
- 为每条重要声明创建 Claim Object（`_meta/claims.yaml`），标 claim_type（source-derived / explanation / inference / external-extension）。
- 关键事实（版本号、命令、API 名称）必须有 source；不确定时立即搜索确认，不要猜。

## 来源冲突

- 冲突时不要自动融合；显示 Source A says / Source B says。
- Course Mode：Course Material 永远单独保留，外部 correction 只能作为 External Note，不能静默替换课程内容。

## 版本与时效性

- 涉及软件安装时写明 OS、版本或“当前最新稳定版”及验证日期。
- 安装步骤要能被新手照着跑通。
- 示例代码优先官方 demo 或最小可复现示例。
- 每个 Evidence 记录 `accessed_at`；长期未复核的来源在 coverage/QA 中标 `stale_flag`。