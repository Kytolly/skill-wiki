# Mode: course

## 适用场景
- 大学/网课/培训课程的讲义、课件整理
- 老师 PPT/讲义已提供，需要忠实重建 + 教学化编排
- 需要考试范围与学习目标提取

## 内容组织
- Lecture → Concepts → Evidence 为主线
- 每讲独立页面，跨讲建立 prerequisite 依赖
- Course Overview 必须是真知识地图，不是导航页

## Source Hierarchy（优先级从高到低）
1. Course Material（幻灯片/讲义/笔记）
2. Official Documentation
3. Primary Academic Paper
4. Authoritative Secondary Source
5. Trusted Web Source
6. General Model Knowledge

## Completeness Policy

Source-faithful completeness：完整保留 examinable content，不因“最小必要知识”删除课件内容。

## Terminology Policy

保留课件英文 canonical term，中文只作辅助；老师使用的中英混排原样保留。

## Evidence Policy

课件是最高优先级来源；外部知识只能作为 External Note 并列，不得静默替换课件内容。

## Figure Policy

课件图/公式/表格是一等信息，必须记录 slide/page + figure region，并做 Figure Explanation。

## 页面结构与特殊元素
- 每页提取 Learning Objectives
- 提取 Discussion / Example / Recap
- 提取老师明确说的 “not in scope”
- 提取公式、手算、流程、图
- Exam Checklist：必须理解 / 必须手算 / 必须记忆 / 了解即可 / 明确 out of scope

## QA 重点
- [ ] Learning Objectives 已提取
- [ ] Examinable content 无遗漏
- [ ] 外部知识与课件并列而非替换
- [ ] 英文术语保留
- [ ] 公式/图/表来源可追踪
- [ ] 跨讲 prerequisite 已建立
