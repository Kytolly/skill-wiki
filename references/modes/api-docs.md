# Mode: api-docs

## 适用场景
- API/SDK/CLI/库文档
- 从官方文档/源码生成接口文档
- 需要调用示例与参数说明

## 内容组织
- Endpoint/Function → 参数 → 返回 → 错误 → 示例 → 版本
- Config reference
- Changelog

## Source Hierarchy（优先级从高到低）
1. Official Documentation / Spec
2. Source Code / Type definitions
3. SDK Source
4. Trusted Web Source
5. General Model Knowledge

## Completeness Policy

Interface completeness：所有公开接口、参数、返回、错误码、版本差异必须完整。

## Terminology Policy

保留 API/参数/类名官方英文；中文解释。

## Evidence Policy

每个接口的签名、参数、行为、错误码要能追溯到官方文档或源码行。

## Figure Policy

示例图/架构图官方优先；Mermaid 标注 derived_from。

## 页面结构与特殊元素
- API reference
- Params table
- Return/error table
- Example
- Config reference
- Version/changelog

## QA 重点
- [ ] 接口无遗漏
- [ ] 参数/返回/错误完整
- [ ] 示例可运行
- [ ] 版本与变化记录
- [ ] 签名可溯源
