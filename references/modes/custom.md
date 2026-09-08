# Mode: custom

## 适用场景
- 上述模式都不完全适用
- 用户明确要求自定义

## 内容组织
- 由用户在 _META 中声明：目标、组织形式、来源优先级、完整性策略、术语/证据/图片策略

## Source Hierarchy（优先级从高到低）
1. 由用户在 _META.source_hierarchy 中声明

## Completeness Policy

由用户在 _META.completeness_policy 中声明。

## Terminology Policy

由用户在 _META.terminology_policy 中声明。

## Evidence Policy

由用户在 _META.evidence_policy 中声明。

## Figure Policy

由用户在 _META.figure_policy 中声明。

## 页面结构与特殊元素
- 复用最接近的 mode 模板，或由用户指定；_META 中必须有“自定义依据”说明

## QA 重点
- [ ] mode=custom 必须存在补充说明，否则判为不完整
