# 分级方案与目录组织

本文件定义 skill-tutorial-wiki 的分级规则。原则：**分级服务于模式与任务，不硬套固定五级**。

## 默认：按任务自定

先确定 wiki mode（见 references/mode-detection.md），再按任务需要选择分级。看任务需要几次“能力台阶”。

## 选择流程

1. 判断能力台阶数：一般 3–5 级；过多拆子级，过少合并。
2. 选命名方案（可混用，但要一致）：
   - 阶段式：`basics / practice / tuning / deployment`
   - 能力式：`intro / fundamentals / advanced / expert`
   - 项目式：`setup / task1 / task2 / optimize`
   - 通用五级：`L0 / L1 / L2 / L3 / L4`（仅在确实匹配时用）
3. 为每级写一句“学完后能做什么”，写入该级目录的完成标准。
4. 确认后写入 `_META.md`，并在 `Home.md` 说明分级依据。

## 目录硬约束（关键）

- **同一分级 = 同一目录**：`page/<grade-slug>/`。
- grade-slug 用 ASCII 小写短横线；中文显示名在 `_Sidebar.md` / `mkdocs.yml` / `_META.md` 映射。
- 页面文件名只表达主题，**不带分级前缀**。
- 导航（`_Sidebar` 与 mkdocs `nav`）按分级目录生成。

## 学习曲线约束（必须遵守）

- 每级只引入 5–7 个新核心概念；其余是上一级复习或本级展开。
- 每页开头列前置知识，且前置知识能链接到已有页面。
- 出现未解释术语：在本页解释或链接到解释页。
- 跨度太大时拆子级或多页；层级跨越不能陡峭。

## 按 mode 的完整性策略

- course：source-faithful completeness，不使用“最小必要知识”删除课件内容。
- lab-handbook / policy-procedure：rule-complete。
- project-docs：architecture/interface completeness。
- technical-tutorial：minimum viable learning path allowed。
- research-kb：evidence / literature coverage oriented。

完整规则见 `references/modes/<mode>.md`。

## 行业标准映射

领域有公认标准时优先映射并说明；没有则自定并说明依据。常见映射：编程（初/中/高/架构/专家）、云（Foundational→Specialty）、数据/AI（入门→专家）、外语（CEFR）、安全（入门→专家）。

## 默认起始与目标

- 用户未指定时，默认只生成最低一级导论；technical-tutorial/lab 按 mode 默认策略。
- 后续按用户显式提示推进（继续下一级、补全某级等）。