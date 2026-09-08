# Mode: project-docs

## 适用场景
- 软件/框架/工具的项目文档
- 从 README / code / issue / official docs 重建文档
- 需要 Code→Docs traceability

## 内容组织
- Architecture → Module → API → Config → Data flow → Build/Deploy → Troubleshooting
- Design Decision Records 单独成页
- README/code/issue/official docs provenance 记录

## Source Hierarchy（优先级从高到低）
1. Source Code / Repo README
2. Official Documentation
3. Design Decision / ADR
4. Issue / Discussion
5. Trusted Web Source
6. General Model Knowledge

## Completeness Policy

Architecture/interface completeness：接口、配置、数据流、版本迁移必须完整，不追求初学者友好。

## Terminology Policy

保留模块/API/CLI 的官方英文名，不强行翻译；中文只作解释。

## Evidence Policy

每个接口/配置/行为 claim 都要能追溯到 code 行、README 或官方文档；给出 source_locator（文件+行/章节）。

## Figure Policy

架构图优先官方图；自绘架构图必须标注 derived_from 的来源证据，不当作 source evidence。

## 页面结构与特殊元素
- Architecture diagram
- Module index
- API reference
- Config reference
- Data flow
- Build / Deploy
- Design decision records
- Known issues
- Troubleshooting
- Migration guide

## QA 重点
- [ ] Code→Docs traceability 存在
- [ ] 接口/配置无遗漏
- [ ] 设计决策有来源
- [ ] 版本/迁移信息完整
- [ ] Known issue 有出处
