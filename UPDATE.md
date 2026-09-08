你需要对以下 GitHub 仓库进行一次完整的架构升级：

Repository:
https://github.com/Kytolly/skill-tutorial-wiki
~/.agents/skills/skill-tutorial-wiki
目标不是简单修改几个 prompt，也不是只增加几条写作规则。

你需要把当前的：

    Tutorial Wiki Generator

升级为：

    Multi-Mode Evidence-Grounded Learning & Documentation Wiki Builder

============================================================
0. 总体目标
============================================================

当前 Skill 已经较好实现：

- Markdown Wiki 工程结构
- Home / Sidebar / META
- 增量更新
- 分级教程
- 新手友好解释
- 联网调研
- 基础来源记录
- 图片 caption / URL / access date
- Mermaid
- MkDocs 本地预览
- GitHub Wiki 发布
- changelog
- 页面互链

这些能力原则上应保留，不要为了重构而破坏。

当前最大问题是：

1. 默认把所有 Wiki 都当成“新手教程”。
2. 缺乏应用场景（Wiki Mode）区分。
3. 专业英文术语容易在中文讲解中丢失。
4. Source 只是页面末尾的来源，而不是 Claim-level Evidence。
5. PDF/PPT 中图片、图表、公式、视觉关系没有被视为一等信息。
6. Figure 只是配图，没有 Figure → Claim → Concept → Source 的证据链。
7. 没有明确区分：
   - source-derived content
   - explanation
   - inference
   - external extension
8. Course Wiki 容易被“最小必要知识”原则过度压缩。
9. 缺乏 Source Coverage / Evidence Coverage / Figure Coverage / Terminology Coverage QA。
10. 页面之间主要只有 Navigation Graph，没有真正的 Knowledge Graph。
11. 缺乏“为什么需要这个方法 → 它解决什么 → 又带来什么问题 → 什么时候选择它”的教学逻辑。
12. 课程讲义、项目文档、实验室 SOP、技术教程等场景不能共享完全相同的模板和 source policy。

请一次性完成下面所有功能。

不要只写设计文档。
需要实际修改 SKILL.md、references、templates、脚本和测试，使新架构真正可以执行。

============================================================
1. 第一层架构：Wiki Mode
============================================================

Skill 入口首先判断 Wiki 的应用场景。

至少支持：

1. course
   课程讲义 / Lecture Notes / Course Knowledge Base

2. project-docs
   项目文档 / Software Project Documentation

3. lab-handbook
   实验室守则 / SOP / Safety Handbook

4. technical-tutorial
   技术入门教程 / Getting Started / Learning Guide

5. research-kb
   研究领域知识库 / Literature & Concept Knowledge Base

6. api-docs
   API / SDK / Tool Documentation

7. experiment-kb
   实验记录 / Experiment Knowledge Base

8. onboarding
   团队 Onboarding / Internal Knowledge Base

9. policy-procedure
   规章制度 / Policy / Procedure

10. custom
   用户自定义模式

------------------------------------------------------------
1.1 Mode Detection
------------------------------------------------------------

如果能够从用户请求、已有目录、文件和上下文中高置信度推断 mode：

    自动选择。

如果不能：

    不要自行猜测。

给用户 2–4 个最可能的 Wiki Mode，
每个用一句话解释：

- 内容组织方式
- source policy
- completeness policy
- 适用情况

然后等待用户确认。

这是一个真正的 confirmation gate。

用户确认前不要开始大规模生成 Wiki。

------------------------------------------------------------
1.2 META
------------------------------------------------------------

_META.md 至少新增：

wiki_mode:
audience:
source_policy:
source_hierarchy:
terminology_policy:
evidence_policy:
figure_policy:
completeness_policy:
external_knowledge_policy:
last_source_audit:
last_coverage_audit:

============================================================
2. 不同 Mode 使用不同 Policy
============================================================

不要再让所有 Wiki 使用同一套“类比 + 最小必要知识”规则。

------------------------------------------------------------
2.1 Course Mode
------------------------------------------------------------

核心目标：

    Source-faithful completeness + teaching-oriented reconstruction

优先级：

Course Material
>
Official Documentation
>
Primary Academic Paper
>
Authoritative Secondary Source
>
Trusted Web Source
>
General Model Knowledge

规则：

- Lecture slides / notes 是课程事实的最高优先级。
- 不允许用通用知识静默“修正”老师课件。
- 如果外部知识与课件不同，明确并列。
- 完整保留 examinable content。
- 不使用“最小必要知识”原则删除课件内容。
- 提取 Learning Objectives。
- 提取 Discussion / Example / Recap。
- 提取老师明确说的 “not in scope”。
- 提取公式、手算、流程、图。
- 建立 Lecture → Concept → Evidence。
- 建立跨 Lecture prerequisite / dependency。
- 支持 Exam Checklist：
  - 必须理解
  - 必须手算
  - 必须记忆
  - 了解即可
  - Slides explicitly out of scope
- 自动生成 Course Overview。
- Course Overview 必须是真正的知识地图，而不只是导航页。

------------------------------------------------------------
2.2 Project Docs Mode
------------------------------------------------------------

重点：

- Architecture
- Module
- API
- CLI
- Configuration
- Data flow
- Build / Deploy
- Design decision
- Troubleshooting
- Version / Migration
- Source-code traceability
- README / code / issue / official docs provenance

不要强制生活类比。

------------------------------------------------------------
2.3 Lab Handbook / SOP Mode
------------------------------------------------------------

重点：

- Rule completeness
- Safety first
- Procedure
- Checklist
- Equipment
- Emergency
- Incident
- Responsibility
- Revision history

支持：

MUST
SHOULD
MAY

不要让 Agent 擅自改写安全规则的规范含义。

不要为了“新手友好”弱化警告。

------------------------------------------------------------
2.4 Technical Tutorial Mode
------------------------------------------------------------

保留现有 Skill 的强项：

- Why first
- analogy
- beginner explanation
- minimal runnable demo
- FAQ
- exercises
- learning path
- quick reference

这里可以继续使用 minimum viable knowledge。

------------------------------------------------------------
2.5 Research KB Mode
------------------------------------------------------------

重点：

- Concept
- Paper
- Method
- Evidence
- Competing definitions
- Historical development
- Open questions
- Paper → Claim
- Claim → Evidence
- Related work graph

------------------------------------------------------------
2.6 其他 Mode
------------------------------------------------------------

为 api-docs / experiment-kb / onboarding / policy-procedure
分别定义合理的：

- page templates
- source hierarchy
- completeness policy
- terminology policy
- evidence policy
- QA checklist

============================================================
3. Terminology Management
============================================================

新增完整的专业术语管理系统。

当前“专业名词要解释”远远不够。

------------------------------------------------------------
3.1 Canonical Terminology
------------------------------------------------------------

核心术语首次出现：

    中文名称（Canonical English Term, ABBR）

例如：

    选择压力（Selection Pressure）
    遗传算法（Genetic Algorithm, GA）
    模拟二进制交叉（Simulated Binary Crossover, SBX）

后续正文允许优先使用：

    Selection Pressure
    GA
    SBX

不要为了中文流畅度删除英文 canonical terminology。

------------------------------------------------------------
3.2 不强制翻译
------------------------------------------------------------

Algorithm / API / Paper / Library / Tool / Formal Method 名称：

保留官方英文名称。

中文只作为辅助解释。

------------------------------------------------------------
3.3 Glossary
------------------------------------------------------------

新增术语索引。

每个 term 至少有：

id
canonical_en
zh
abbreviation
aliases
definition
source_definition
first_occurrence
related_concepts

------------------------------------------------------------
3.4 Terminology QA
------------------------------------------------------------

自动检查：

- 同一英文术语是否出现多个中文译名
- abbreviation 是否先定义后使用
- 核心英文术语是否丢失
- source 中存在的重要 terminology 是否未进入 Wiki
- canonical term 是否被擅自改写

============================================================
4. Evidence Model
============================================================

这是 2.0 的核心。

不要再把“来源”仅仅理解成页面末尾几个 URL。

引入：

    Evidence Object

------------------------------------------------------------
4.1 Evidence Object
------------------------------------------------------------

建议 schema：

id:
source_type:
source_title:
source_file:
source_url:
source_locator:
source_date:
accessed_at:
claim_ids:
figure_ids:
extraction_method:
confidence:
license:
notes:

source_type 至少支持：

course_slide
course_note
user_document
official_documentation
primary_paper
book
project_source
web_page
external_image
generated_diagram
derived
user_statement

source_locator 支持：

slide number
PDF page
section
heading
figure number
table number
code file + line
URL fragment
repository commit

------------------------------------------------------------
4.2 Claim Object
------------------------------------------------------------

重要知识声明应能映射到 Evidence。

schema 可包含：

id:
claim:
claim_type:
concept_ids:
evidence_ids:
status:
confidence:

claim_type：

source-derived
explanation
inference
external-extension

------------------------------------------------------------
4.3 强制区分内容来源
------------------------------------------------------------

Wiki 应支持视觉标签：

📘 Source / Slides
💡 Explanation
🔍 Inference
🌐 External Reference
🧪 Example
⚠️ Outside Scope

规则：

Source-derived:
    来源直接支持。

Explanation:
    Agent 对 source 的教学解释。

Inference:
    Agent 根据多个 evidence 推导。

External:
    来自课件之外。

禁止把 Explanation / Inference 写成“老师原话”。

============================================================
5. Claim → Evidence Traceability
============================================================

重要 claim 必须支持：

Claim
 ↓
Evidence
 ↓
Source

例如：

    Selection Pressure 太高可能导致 premature convergence. [E034]

Evidence：

E034
Source type: course_slide
Lecture 4
Slide 15
Relevant statement: ...

页面正文不应该被大量 source metadata 打断。

正文负责教学。

Evidence block / expandable section 负责验证。

支持：

- inline evidence reference
- page evidence list
- evidence backlink
- source page
- source locator

自动检测：

    Unsupported important claim

============================================================
6. Source Hierarchy
============================================================

每个 Mode 有自己的 Source Hierarchy。

来源冲突时：

不要自动融合。

显示：

Source A says:
Source B says:

Course Mode 特别要求：

    Course Material 永远单独保留。

External correction 只能作为：

    External Note

不能静默替换课程内容。

============================================================
7. PDF / PPT / Document Visual Understanding
============================================================

这是强制要求。

PDF / PPT / document ingestion 不允许只读取 text extraction。

必须同时考虑：

    Text Layer
    +
    Rendered Page
    +
    Visual Interpretation

------------------------------------------------------------
7.1 Slide/Page extraction
------------------------------------------------------------

每页至少分析：

slide/page number
headings
body text
equations
tables
figures
plots
diagrams
screenshots
arrows
highlighting
annotations
spatial relationships

------------------------------------------------------------
7.2 Visual-only content
------------------------------------------------------------

如果某页 extracted text 很少，
但有图：

不能判定为“没有内容”。

必须读取 rendered page。

------------------------------------------------------------
7.3 Slide Evidence Record
------------------------------------------------------------

每页可形成：

slide_number:
text_summary:
visual_summary:
key_claims:
terms:
equations:
figures:
tables:
scope_notes:

============================================================
8. Figure / Image as First-Class Knowledge
============================================================

当前 Skill 的：

    caption + source URL

保留。

但新增 Figure Object。

------------------------------------------------------------
8.1 Figure Object
------------------------------------------------------------

至少：

id:
caption:
source_type:
source:
source_locator:
page_url:
direct_image_url:
local_asset:
license:
accessed_at:
concept_ids:
claim_ids:
explanation:
what_to_notice:
related_figures:

------------------------------------------------------------
8.2 Figure Explanation
------------------------------------------------------------

每张关键教学图必须回答：

1. 图展示什么？
2. 应该重点看哪里？
3. 每个轴 / 节点 / 箭头 / 区域是什么意思？
4. 图支持什么 claim？
5. 和哪个 concept 对应？
6. 为什么这张图值得放在这里？

禁止：

    插一张图 + caption + source

然后完全不解释。

------------------------------------------------------------
8.3 Lecture Screenshot
------------------------------------------------------------

课程讲义图必须保存：

Lecture
Slide/Page
Figure region
Source file

必要时裁切关键 figure，
而不是只能整页截图。

------------------------------------------------------------
8.4 External Image
------------------------------------------------------------

同时记录：

page_url
direct_image_url
license / attribution
access_date

禁止只保存 direct image URL。

============================================================
9. Figure Citation Graph
============================================================

建立：

Concept
 ↕
Figure
 ↕
Claim
 ↕
Evidence
 ↕
Source

支持：

- Concept → Figure
- Figure → Concept
- Figure → Claim
- Figure → Source Slide
- Figure → Original URL
- Figure → Related Figure
- Source → Figure backlink

生成：

    Figure Index

Course Mode 可生成：

    课程关键图索引

============================================================
10. Mermaid / Derived Diagram
============================================================

Mermaid 是：

    Derived Illustration

不是 source evidence。

必须标记：

    本图由 Wiki 根据 E12/E13/E14 重绘

并保存：

derived_from:
  - E12
  - E13

如果 Mermaid 是 Agent 自己的教学抽象：

明确标：

    Conceptual illustration; not present in source.

============================================================
11. Equation Management
============================================================

新增 Equation Object。

至少：

id:
latex:
source:
source_locator:
concept_ids:
symbols:
explanation:
worked_example:
common_mistakes:

------------------------------------------------------------
11.1 公式展示
------------------------------------------------------------

每个重要公式尽可能包含：

Formal equation

Meaning

Symbol table

Intuition

Worked example

Common mistake

Source

------------------------------------------------------------
11.2 Source Fidelity
------------------------------------------------------------

不要静默“修正”老师公式。

如果怀疑公式有 typo：

Slides:
    原公式

External / Inference:
    可能存在的问题

分开写。

============================================================
12. Teaching-Oriented Reconstruction
============================================================

页面不能只是：

Definition
Formula
Example

对于重要方法，优先使用：

Why do we need it?
        ↓
What problem does it solve?
        ↓
Core intuition
        ↓
Formal definition
        ↓
Algorithm / Equation
        ↓
Worked example
        ↓
What problem does it introduce?
        ↓
Alternatives
        ↓
When should I use it?
        ↓
When should I not use it?
        ↓
Common mistakes
        ↓
Connection to other concepts
        ↓
Evidence
        ↓
Exam / Practice checklist（若 mode 适用）

不是每页机械套全部 section。

根据页面性质选择。

============================================================
13. Method Selection Guide
============================================================

对于存在多个 alternatives 的领域：

自动生成 decision guide。

例如：

Representation:

Boolean
 → Binary

Discrete integer
 → Integer

Continuous
 → Real

Order / adjacency
 → Permutation

Program / expression
 → Tree

再例如：

Need local fitness only?
 → Tournament

Need probability proportional to absolute fitness?
 → FPS

此功能应适用于任何领域，
不只 EA。

============================================================
14. Knowledge Graph
============================================================

当前页面互链是 Navigation Graph。

新增 Knowledge Graph。

Concept relationship 至少支持：

prerequisite
derived_from
part_of
alternative_to
solves
causes
tradeoff_with
uses
represented_by
measured_by
implemented_by
related_to

并支持：

Concept → Equation
Concept → Figure
Concept → Evidence
Concept → Example
Concept → Exercise
Concept → Lecture/Page

生成：

- Concept Dependency Graph
- Backlinks
- Related Concepts
- Orphan Concept report

============================================================
15. Course Overview / Domain Overview
============================================================

Home 不应该只是页面目录。

Course Mode 的 Home 应展示：

1. 课程核心问题
2. 课程 storyline
3. 全局 knowledge map
4. Lecture → Concept mapping
5. 核心 trade-offs
6. Learning Objective coverage
7. 当前覆盖进度
8. Exam / revision entry points
9. 页面导航

例如：

Real Problem
 ↓
Optimization as Search
 ↓
Evolutionary Algorithm
 ↓
Representation
 ↓
Population
 ↓
Evaluation
 ↓
Selection
 ↓
Variation
 ↓
Constraint Handling
 ↓
New Population

并解释每一讲在这张图哪里。

============================================================
16. Completeness Policy
============================================================

不同 Mode：

course:
    source-faithful completeness

lab-handbook:
    rule-complete

project-docs:
    architecture/interface completeness

technical-tutorial:
    minimum viable learning path allowed

research-kb:
    evidence / literature coverage oriented

------------------------------------------------------------
16.1 Coverage Audit
------------------------------------------------------------

实现 Source Outline vs Wiki Outline 比较。

检测：

Missing section
Missing figure
Missing equation
Missing table
Missing example
Missing terminology
Missing learning objective
Missing evidence

生成：

Coverage Report

============================================================
17. Course Learning Objective Support
============================================================

Course Mode 新增：

Learning Objective extraction

LO → Lecture
LO → Concept
LO → Wiki Page
LO → Exercise

生成：

Learning Objective Coverage %

同时支持：

Exam Scope

Must understand
Must calculate
Must memorize
Know conceptually
Slides explicitly out of scope

不要根据模型常识擅自宣布考试范围。

必须基于课程 source 或明确标：

    Wiki study recommendation

============================================================
18. Project Documentation Special Features
============================================================

实现：

Code → Docs traceability

Architecture diagram source

API reference

Config reference

Design decision records

Version / commit provenance

Known issue

Troubleshooting

Migration guide

README / source / issue / official docs relationship

============================================================
19. Lab / SOP Special Features
============================================================

实现：

Rule ID

Severity

Applicability

Responsible role

Procedure

Prerequisite

Required PPE

Warning

Emergency action

Revision history

Source authority

不得为了“解释得更自然”改变规范语义。

============================================================
20. Provenance
============================================================

页面级 changelog 保留。

进一步支持 section-level provenance：

source-derived
agent-explanation
external-research
user-correction
derived

支持：

Source version
Last verified
Stale flag

============================================================
21. QA / Automated Checks
============================================================

扩展当前 self-check。

至少实现以下 QA：

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
[ ] External source URL validity
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

输出机器可读和人可读 QA report。

============================================================
22. Tests
============================================================

当前仓库已经有 test/ 扩展位。

真正使用它。

至少增加 fixtures：

1. Course lecture fixture
   - 有 text
   - 有 figure
   - 有 equation
   - 有 “out of scope”
   - 有英文 terminology

2. Project docs fixture

3. Lab SOP fixture

4. Technical tutorial fixture

测试：

- Mode detection
- terminology preservation
- source hierarchy
- evidence graph
- figure graph
- coverage audit
- broken links
- META consistency
- build compatibility

============================================================
23. Backward Compatibility
============================================================

必须保留：

page/
script/
build/

Home.md
_Sidebar.md
_META.md

已有 Wiki 不应被强制重写。

升级时：

读取旧 META
识别 legacy project
生成 migration plan
增量添加新 metadata

旧页面没有 Evidence Object 时：

标记：

    provenance: legacy-unverified

而不是删除。

============================================================
24. Project Structure
============================================================

可以扩展，但不要破坏现有职责边界。

建议增加：

references/
    modes/
        course.md
        project-docs.md
        lab-handbook.md
        technical-tutorial.md
        research-kb.md
        api-docs.md
        experiment-kb.md
        onboarding.md
        policy-procedure.md

    terminology.md
    evidence-model.md
    figure-model.md
    equation-model.md
    knowledge-graph.md
    coverage-audit.md
    qa.md

templates/
或 references/templates/

page/
    assets/
        images/
        figures/

可根据当前仓库实际结构调整。

============================================================
25. SKILL.md 重构
============================================================

SKILL.md 不要塞入所有细节。

它应该负责：

1. Skill purpose
2. Mode detection
3. Confirmation gate
4. High-level workflow
5. Mode policy loading
6. Source ingestion
7. Evidence extraction
8. Knowledge reconstruction
9. Page generation
10. QA
11. Preview
12. Publish

具体规则拆到 references。

============================================================
26. 新工作流
============================================================

最终 workflow 应大致为：

Step 1
Understand user goal

Step 2
Detect Wiki Mode

Step 3
If ambiguous:
    ask user
    WAIT FOR CONFIRMATION

Step 4
Load mode-specific policies

Step 5
Audit existing Wiki

Step 6
Inventory sources

Step 7
Establish source hierarchy

Step 8
Extract:
    text
    terminology
    claims
    equations
    figures
    visual relationships
    learning objectives / rules / interfaces depending on mode

Step 9
Build:
    Evidence Graph
    Knowledge Graph
    Figure Graph
    Terminology Dictionary

Step 10
Compare Source Coverage

Step 11
Plan pages

Step 12
Ask for confirmation if this is a substantial structural change

Step 13
Generate/update Wiki

Step 14
Generate navigation + Home + META

Step 15
Run QA

Step 16
Fix QA failures

Step 17
Build local preview

Step 18
Report:
    pages changed
    sources
    evidence coverage
    figure coverage
    terminology coverage
    unresolved issues
    preview
    publish command

============================================================
27. 一个非常重要的原则
============================================================

不要把：

    “有来源”

理解为：

    “页面底部有几个 URL”。

新版 Skill 的核心原则必须是：

    Every important knowledge claim should be traceable.

也不要把：

    “有图片”

理解为：

    “Markdown 里插入了一张图”。

而是：

    Every important figure should be interpretable and traceable.

也不要把：

    “中文教程”

理解为：

    “把英文专业术语全部翻译成中文”。

而是：

    Chinese explanation + preserved canonical terminology.

也不要把：

    “课程总结”

理解为：

    “把 PPT 压缩成最短笔记”。

而是：

    Source-faithful reconstruction + teaching-oriented explanation.

============================================================
28. Definition of Done
============================================================

只有满足以下条件才算完成本次升级：

1. 所有 Mode 都有明确 policy。
2. Mode 不明确时存在 confirmation gate。
3. Course Mode 不再使用 minimum-knowledge completeness。
4. Terminology 有正式 schema 和 QA。
5. Evidence Object 已落地。
6. Claim → Evidence 已落地。
7. Figure Object 已落地。
8. Figure → Claim → Source 已落地。
9. PDF/PPT visual-content workflow 已写入 Skill。
10. Derived Mermaid 与 source figure 明确区分。
11. Equation provenance 已落地。
12. Knowledge Graph 已定义。
13. Coverage Audit 已实现。
14. QA 已扩展。
15. 至少有 Course / Project / SOP / Tutorial fixtures/tests。
16. legacy Wiki 可迁移。
17. 本地 preview 仍可运行。
18. GitHub Wiki publish workflow 不被破坏。
19. README 更新。
20. SKILL.md 与 references 不矛盾。
21. 所有新增功能都有实际规则/模板/脚本/测试支撑，
    不能只在 README 宣称支持。

============================================================
29. 实施方式
============================================================

开始前：

- 阅读整个 repository。
- 列出当前结构和已有能力。
- 不要假定现有实现只有 SKILL.md。
- 检查所有 references / scripts / templates / tests。
- 判断哪些可以复用。

然后直接实施。

除非遇到真正影响架构、无法从上述需求推断的选择，
否则不要频繁询问用户。

遇到此类重大歧义时：

- 给出 2–3 个方案
- 说明 trade-off
- 等待确认

不要为了确认小细节中断工作。

============================================================
30. 最终交付报告
============================================================

完成后不要只说“Done”。

输出：

A. Architecture changes

B. Files added

C. Files modified

D. Wiki Modes implemented

E. Evidence model

F. Terminology model

G. Figure / visual model

H. Knowledge graph

I. Coverage / QA system

J. Tests added and test results

K. Backward compatibility / migration

L. Remaining limitations

M. Example:
展示一个 Course Mode 页面从：

    source slide

到：

    claim
    evidence
    terminology
    figure explanation
    cross-lecture connection

的完整链路。

最后给出：

    git diff --stat
    test results
    local preview verification result

不要把未实现功能描述成已实现。
任何由于当前运行环境、GitHub Wiki 或工具限制而无法完整实现的能力，
必须明确列入 Remaining limitations。

============================================================
31. IMPLEMENTATION CONTRACT — 抽象要求必须操作化
============================================================

本任务中的要求有很多是 capability-level requirements，而不是已经替你
设计好的具体实现。

你有责任继续完成 requirements engineering。

不要因为用户只描述了一个抽象能力，就只创建一份 Markdown 规范并宣称完成。

对于每个 requirement，你必须自行将其 operationalize 为：

Requirement
    ↓
Behavioral Specification
    ↓
Data Model / State
    ↓
Workflow Integration
    ↓
Persistent Artifact
    ↓
Validation / QA
    ↓
Automated Test

只有能够走通这条链的功能才允许标记为“Implemented”。

------------------------------------------------------------
31.1 三种实现状态
------------------------------------------------------------

最终报告中，每项 capability 只能标记：

IMPLEMENTED
    已经进入实际 workflow，有真实 artifact，并有验证或测试。

SPECIFIED
    已经定义规则/schema，但当前架构或工具限制导致无法真正执行。

PLANNED
    只有设计方向，没有完成。

严禁把 SPECIFIED 写成 IMPLEMENTED。

------------------------------------------------------------
31.2 什么不算实现
------------------------------------------------------------

以下情况不能称为“Implemented”：

- 只在 SKILL.md 增加一句要求
- 只新增 references/*.md
- 只提供 YAML 示例
- 只提供 schema，但没有 consumer
- 只增加模板，但 workflow 不会使用
- 只增加 QA checklist，但没有实际检查机制
- 只写测试计划，没有测试
- README 声称支持，但没有代码/工作流
- Agent“理论上可以做到”，但 Skill 没有明确执行路径

------------------------------------------------------------
31.3 什么算实现
------------------------------------------------------------

例如：

“Terminology Preservation”

至少应该有：

1. terminology extraction rule
2. canonical terminology representation
3. persistence mechanism
4. page-generation consumption rule
5. first-use rendering rule
6. consistency validator
7. fixture
8. automated test

“Evidence Traceability”

至少应该有：

1. Evidence schema
2. Claim schema
3. stable ID generation
4. persistence
5. Claim → Evidence relation
6. page rendering
7. backlink/source rendering
8. orphan/unsupported claim validation
9. fixture
10. automated test

“Figure Understanding”

至少应该有：

1. source figure discovery/extraction workflow
2. Figure metadata schema
3. Figure explanation schema
4. Figure → Claim relation
5. Figure → Concept relation
6. Figure → Source relation
7. rendering convention
8. missing-explanation validator
9. fixture containing visual content
10. test

“Course Coverage”

至少应该有：

1. source inventory
2. source-outline extraction
3. Wiki-outline extraction
4. comparison logic
5. missing-item classification
6. human-readable report
7. machine-readable report
8. fixture
9. automated test

------------------------------------------------------------
31.4 Agent 必须自行补全实现细节
------------------------------------------------------------

不要等待用户替你设计：

- ID strategy
- metadata storage format
- directory layout details
- schema fields
- validator architecture
- CLI interface
- report format
- migration mechanics
- fixture format
- test organization

在不违反已有 repository architecture 的前提下，
选择合理、简单、可维护的实现。

优先：

simple
explicit
testable
portable
backward-compatible

避免为了“架构漂亮”引入不必要的复杂数据库或大型依赖。

Markdown/YAML/JSON + Python validators 如果足够，就优先使用。

------------------------------------------------------------
31.5 Feature Acceptance Tests
------------------------------------------------------------

每个 P0/P1 capability 必须定义至少一个 acceptance test：

Given:
    一个最小输入 fixture

When:
    Skill workflow / validator / builder 被执行

Then:
    应产生明确 artifact

And:
    validator 应能检测故意制造的错误

例如 Terminology：

Given:
    source 中出现 "Selection Pressure"

When:
    页面只写“选择压力”且没有 canonical English term

Then:
    terminology QA 应产生 warning/error

例如 Evidence：

Given:
    页面包含一个 important claim，但没有 evidence_id

Then:
    evidence QA 必须报告 unsupported claim

例如 Figure：

Given:
    一个 source figure 已被加入页面

When:
    figure 没有 explanation 或 source locator

Then:
    figure QA 必须失败或 warning

例如 Course Coverage：

Given:
    source inventory 有 Figure F03

When:
    Wiki 没有对应 figure，也没有 explicit omission reason

Then:
    coverage report 必须标记 F03 missing

------------------------------------------------------------
31.6 Negative Tests
------------------------------------------------------------

不能只测试 happy path。

必须至少测试：

- terminology alias conflict
- undefined abbreviation
- evidence ID missing
- evidence points to missing source
- figure has no explanation
- figure has no source
- external image has direct URL but no page URL
- derived Mermaid incorrectly marked as source evidence
- equation missing provenance
- dead concept relation
- missing Wiki page
- source content omitted
- Course external knowledge silently replacing slide content

------------------------------------------------------------
31.7 Capability Matrix
------------------------------------------------------------

实现完成后生成：

docs/capability-matrix.md
或项目中更合理的位置。

格式至少包括：

| Capability | Mode | Specification | Runtime/Workflow | Validator | Tests | Status |
|---|---|---|---|---|---|---|

Status 只能：

Implemented
Specified
Planned

这样用户可以真正知道 Skill 当前“会什么”，而不是看 README 猜。

============================================================
32. 不要过度工程化
============================================================

虽然要求完整落地，但不要为了满足“Evidence Graph”这个名字就引入：

Neo4j
PostgreSQL
复杂 Web backend
大型 frontend framework

除非现有项目确实需要。

这个 Skill 本质仍然应该：

portable
repository-native
Markdown-first
Git-friendly

推荐：

Markdown
YAML
JSON
Python scripts

例如可以使用：

_meta/
    terminology.yaml
    evidence.yaml
    concepts.yaml
    figures.yaml
    equations.yaml

具体结构由你根据现有 repository 决定。

关键是：

这些 metadata 必须真的被 generation / validation / build workflow 使用，
不能成为没人读取的 sidecar files。

============================================================
33. Skill Runtime 与辅助工具边界
============================================================

注意区分：

A. Skill instructions
    告诉 Agent 如何执行知识重建。

B. Repository tooling
    做 deterministic、适合自动化的事情。

例如：

适合 Skill reasoning：
- 判断 Wiki Mode
- 理解一张教学图的含义
- 判断某 claim 是否是 inference
- 建立概念之间的语义关系
- 解释公式
- 判断 source hierarchy

适合 script：
- ID generation
- schema validation
- broken-link checking
- terminology consistency scanning
- evidence reference integrity
- figure asset existence
- coverage diff
- META consistency
- report generation

不要试图用 regex/script 完成需要语义理解的任务。

也不要把 deterministic integrity checks 全部留给 LLM 自查。

============================================================
34. Visual Capability 的现实边界
============================================================

Skill 本身不能凭空创造底层工具能力。

因此 PDF/PPT Visual Understanding 必须设计成 capability-aware workflow：

IF runtime supports rendered-page/image inspection:
    必须读取 visual layer。

ELSE:
    标记 visual extraction unavailable，
    不得假装已检查图片，
    coverage report 标记：
        visual_evidence_status: unverified

同理：

如果 runtime 无法自动裁图，
可以生成 extraction manifest，
但必须将状态标记为 Specified/Partial，而不是 Implemented。

============================================================
35. 最终要求：用真实端到端示例证明
============================================================

不要只运行 unit tests。

至少创建 4 个最小 end-to-end fixtures：

Course
Project Docs
Lab SOP
Technical Tutorial

对每一个运行完整或最接近完整的 workflow。

Course fixture 必须证明：

source
  ↓
terminology
  ↓
claim
  ↓
evidence
  ↓
figure
  ↓
concept
  ↓
Wiki page
  ↓
coverage report
  ↓
QA

最终报告展示实际生成结果路径。

如果其中任何一步没有真正发生，
对应 capability 不得标记 Implemented。
