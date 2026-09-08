#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate minimal but valid fixtures for course/project-docs/lab-sop/technical-tutorial.

Usage:
    python3 test/_gen_fixtures.py
"""
import os
import yaml

BASE = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(BASE, "fixtures")

REQUIRED_META = {
    "wiki_mode": "technical-tutorial",
    "audience": "零基础开发者",
    "source_policy": "official docs first",
    "source_hierarchy": "official > trusted web > general",
    "terminology_policy": "preserve canonical English",
    "evidence_policy": "every important claim traceable",
    "figure_policy": "official figure first, else Mermaid",
    "completeness_policy": "minimum viable learning path",
    "external_knowledge_policy": "merge update, never silently replace",
    "last_source_audit": "2026-01-02",
    "last_coverage_audit": "2026-01-02",
}


def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def dump_yaml(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(obj, f, allow_unicode=True, sort_keys=False)


def meta_md(mode, extra=None):
    lines = [
        "# Wiki 状态",
        "",
        "- 领域：%s" % ("示例领域 " + mode),
        "- 读者：%s" % REQUIRED_META["audience"],
        "- wiki_mode: %s" % mode,
    ]
    for k, v in REQUIRED_META.items():
        if k == "wiki_mode":
            continue
        lines.append("- %s: %s" % (k, v))
    if extra:
        for k, v in extra.items():
            lines.append("- %s: %s" % (k, v))
    lines.extend([
        "",
        "## 页面清单",
        "- [x] basics/示例页面（2026-01-02）",
        "",
        "## changelog",
        "- 2026-01-02：创建 fixture（%s）。" % mode,
    ])
    return "\n".join(lines)


def make_technical(root):
    # page
    write_file(os.path.join(root, "page", "Home.md"),
        "# 示例教程\n\n| 分级 | 目标 | 页面 |\n|------|------|------|\n| 入门（basics） | 理解并跑通 | [[示例页面]] |\n")
    write_file(os.path.join(root, "page", "_Sidebar.md"),
        "**Home**\n\n**入门（basics）**\n- [[示例页面]]\n")
    write_file(os.path.join(root, "page", "basics", "示例页面.md"),
        "# 示例页面\n\n> 本页属于：入门（basics）\n> provenance: source-derived\n> last_verified: 2026-01-02\n\n"
        "## 核心概念\n\n示例（Example Protocol）是一种协议。[C01]\n\n## 证据\n\n[E01] 来自官方文档。\n")
    write_file(os.path.join(root, "page", "_META.md"), meta_md("technical-tutorial"))
    for p in ["basics"]:
        pass
    # meta
    dump_yaml(os.path.join(root, "_meta", "terminology.yaml"),
        {"terms": [{"id": "T01", "canonical_en": "Example Protocol", "zh": "示例协议",
                    "abbreviation": None, "aliases": [], "definition": "一个示例协议。",
                    "source_definition": "官方定义。", "first_occurrence": "page/basics/示例页面.md", "related_concepts": ["C01"]}]})
    dump_yaml(os.path.join(root, "_meta", "claims.yaml"),
        {"claims": [{"id": "C01", "claim": "示例协议用于传输消息。", "claim_type": "source-derived",
                     "concept_ids": ["C01"], "evidence_ids": ["E01"], "status": "verified", "confidence": "high"}]})
    dump_yaml(os.path.join(root, "_meta", "evidence.yaml"),
        {"evidence": [{"id": "E01", "source_type": "official_documentation", "source_title": "官方文档",
                       "source_url": "https://example.com/docs", "source_locator": "section 2",
                       "accessed_at": "2026-01-02", "claim_ids": ["C01"], "figure_ids": [], "confidence": "high"}]})
    dump_yaml(os.path.join(root, "_meta", "concepts.yaml"),
        {"concepts": [{"id": "C01", "name_zh": "示例协议", "name_en": "Example Protocol", "aliases": [],
                       "definition_zh": "一个示例协议。", "page": "page/basics/示例页面.md",
                       "evidence_ids": ["E01"], "figure_ids": [], "equation_ids": [], "related": []}]})
    dump_yaml(os.path.join(root, "_meta", "figures.yaml"), {"figures": []})
    dump_yaml(os.path.join(root, "_meta", "equations.yaml"), {"equations": []})
    dump_yaml(os.path.join(root, "_meta", "source-inventory.yaml"),
        {"items": [{"id": "S01", "item_type": "section", "item_name": "示例协议", "source": "官方文档",
                    "locator": "section 2", "expected_page": "page/basics/示例页面.md", "status": "covered", "expect_keywords": ["Example Protocol"]}]})
    dump_yaml(os.path.join(root, "_meta", "omissions.yaml"), {"items": []})
    dump_yaml(os.path.join(root, "_meta", "status.yaml"),
        {"legacy_unverified": False, "visual_evidence_status": "verified"})


def make_course(root):
    # page
    write_file(os.path.join(root, "page", "Home.md"),
        "# 课程讲义\n\n| 讲次 | 内容 |\n|------|------|\n| L4 | [[选择压力]] |\n")
    write_file(os.path.join(root, "page", "_Sidebar.md"),
        "**Home**\n\n**第 4 讲**\n- [[选择压力]]\n")
    write_file(os.path.join(root, "page", "L4", "选择压力.md"),
        "# 选择压力\n\n> 本页属于：第 4 讲\n> provenance: source-derived\n> last_verified: 2026-01-02\n\n"
        "## 学习目标\n\n- 理解选择压力（Selection Pressure, SP）。\n\n"
        "## 核心概念\n\n选择压力过高会导致过早收敛（premature convergence）。[C01]\n\n"
        "<!-- FIGURE: F01 -->\n\n![图 1 选择压力示意](assets/images/F01.png)\n\n"
        "<!-- EQUATION: EQ01 -->\n\n$$P_i = f_i / \\sum_j f_j$$\n\n"
        "## 考试范围\n\n- [ ] 必须理解：选择压力\n- [ ] 必须记忆：定义\n")
    write_file(os.path.join(root, "page", "_META.md"), meta_md("course", {"custom_reason": "课程讲义"}))
    write_file(os.path.join(root, "page", "assets", "images", "F01.png"), "PLACEHOLDER")
    dump_yaml(os.path.join(root, "_meta", "terminology.yaml"),
        {"terms": [{"id": "T01", "canonical_en": "Selection Pressure", "zh": "选择压力",
                    "abbreviation": "SP", "aliases": [], "definition": "影响收敛与多样性的机制。",
                    "source_definition": "课件定义。", "first_occurrence": "page/L4/选择压力.md", "related_concepts": ["C01"]}]})
    dump_yaml(os.path.join(root, "_meta", "claims.yaml"),
        {"claims": [{"id": "C01", "claim": "选择压力过高可能导致过早收敛。", "claim_type": "source-derived",
                     "concept_ids": ["C01"], "evidence_ids": ["E01"], "status": "verified", "confidence": "high"}]})
    dump_yaml(os.path.join(root, "_meta", "evidence.yaml"),
        {"evidence": [{"id": "E01", "source_type": "course_slide", "source_title": "Lecture 4",
                       "source_locator": "slide 15", "source_date": "2026-01-01", "accessed_at": "2026-01-02",
                       "claim_ids": ["C01"], "figure_ids": ["F01"], "confidence": "high"}]})
    dump_yaml(os.path.join(root, "_meta", "concepts.yaml"),
        {"concepts": [{"id": "C01", "name_zh": "选择压力", "name_en": "Selection Pressure", "aliases": [],
                       "definition_zh": "影响收敛与多样性的机制。", "page": "page/L4/选择压力.md",
                       "evidence_ids": ["E01"], "figure_ids": ["F01"], "equation_ids": ["EQ01"], "related": []}]})
    dump_yaml(os.path.join(root, "_meta", "figures.yaml"),
        {"figures": [{"id": "F01", "caption": "选择压力示意", "source_type": "course_slide", "source": "Lecture 4",
                      "source_locator": "slide 15 figure", "local_asset": "page/assets/images/F01.png",
                      "license": "CC BY-NC", "accessed_at": "2026-01-02", "concept_ids": ["C01"], "claim_ids": ["C01"],
                      "explanation": "横轴是多样性，纵轴是适应度。", "what_to_notice": "压力过大时迅速收敛。",
                      "related_figures": [], "derived_from": []}]})
    dump_yaml(os.path.join(root, "_meta", "equations.yaml"),
        {"equations": [{"id": "EQ01", "latex": "P_i = f_i / \\sum_j f_j", "source": "Lecture 5", "source_locator": "公式 3",
                        "concept_ids": ["C01"], "symbols": ["P_i", "f_i"], "explanation": "个体选中概率。"}]})
    dump_yaml(os.path.join(root, "_meta", "source-inventory.yaml"),
        {"items": [
            {"id": "S01", "item_type": "section", "item_name": "选择压力", "source": "Lecture 4", "expected_page": "page/L4/选择压力.md", "expect_keywords": ["选择压力"]},
            {"id": "S02", "item_type": "figure", "item_name": "选择压力示意", "source": "Lecture 4", "expected_page": "page/L4/选择压力.md", "item_marker": "FIGURE: F01"},
            {"id": "S03", "item_type": "equation", "item_name": "选择概率公式", "source": "Lecture 5", "expected_page": "page/L4/选择压力.md", "item_marker": "EQUATION: EQ01"},
        ]})
    dump_yaml(os.path.join(root, "_meta", "omissions.yaml"), {"items": []})
    dump_yaml(os.path.join(root, "_meta", "status.yaml"),
        {"legacy_unverified": False, "visual_evidence_status": "verified"})


def make_project(root):
    write_file(os.path.join(root, "page", "Home.md"), "# 项目文档\n\n- [[架构]]\n")
    write_file(os.path.join(root, "page", "_Sidebar.md"), "**Home**\n\n- [[架构]]\n")
    write_file(os.path.join(root, "page", "docs", "架构.md"),
        "# 架构\n\n> provenance: source-derived\n> last_verified: 2026-01-02\n\n## 模块\n\n入口模块（Entry Module）负责启动。[C01]\n")
    write_file(os.path.join(root, "page", "_META.md"), meta_md("project-docs"))
    dump_yaml(os.path.join(root, "_meta", "terminology.yaml"),
        {"terms": [{"id": "T01", "canonical_en": "Entry Module", "zh": "入口模块", "abbreviation": None,
                    "aliases": [], "definition": "负责启动的模块。", "source_definition": "代码注释。",
                    "first_occurrence": "page/docs/架构.md", "related_concepts": ["C01"]}]})
    dump_yaml(os.path.join(root, "_meta", "claims.yaml"),
        {"claims": [{"id": "C01", "claim": "入口模块负责启动。", "claim_type": "source-derived",
                     "concept_ids": ["C01"], "evidence_ids": ["E01"], "status": "verified", "confidence": "high"}]})
    dump_yaml(os.path.join(root, "_meta", "evidence.yaml"),
        {"evidence": [{"id": "E01", "source_type": "project_source", "source_title": "main.py",
                       "source_file": "src/main.py", "source_locator": "main.py:12", "accessed_at": "2026-01-02",
                       "claim_ids": ["C01"], "figure_ids": [], "confidence": "high"}]})
    dump_yaml(os.path.join(root, "_meta", "concepts.yaml"),
        {"concepts": [{"id": "C01", "name_zh": "入口模块", "name_en": "Entry Module", "aliases": [],
                       "definition_zh": "负责启动的模块。", "page": "page/docs/架构.md",
                       "evidence_ids": ["E01"], "figure_ids": [], "equation_ids": [], "related": []}]})
    dump_yaml(os.path.join(root, "_meta", "figures.yaml"), {"figures": []})
    dump_yaml(os.path.join(root, "_meta", "equations.yaml"), {"equations": []})
    dump_yaml(os.path.join(root, "_meta", "source-inventory.yaml"),
        {"items": [{"id": "S01", "item_type": "section", "item_name": "入口模块", "expected_page": "page/docs/架构.md"}]})
    dump_yaml(os.path.join(root, "_meta", "omissions.yaml"), {"items": []})
    dump_yaml(os.path.join(root, "_meta", "status.yaml"),
        {"legacy_unverified": False, "visual_evidence_status": "verified"})


def make_sop(root):
    write_file(os.path.join(root, "page", "Home.md"), "# 实验室守则\n\n- [[设备操作SOP]]\n")
    write_file(os.path.join(root, "page", "_Sidebar.md"), "**Home**\n\n- [[设备操作SOP]]\n")
    write_file(os.path.join(root, "page", "sop", "设备操作SOP.md"),
        "# 设备操作 SOP\n\n> provenance: source-derived\n> last_verified: 2026-01-02\n\n"
        "## 规则\n\n- R01（MUST）：操作前必须佩戴 PPE。[C01]\n- R02（SHOULD）：定期检查设备。\n\n"
        "## 应急\n\n- 遇漏电立即断电并上报。\n")
    write_file(os.path.join(root, "page", "_META.md"), meta_md("lab-handbook"))
    dump_yaml(os.path.join(root, "_meta", "terminology.yaml"),
        {"terms": [{"id": "T01", "canonical_en": "PPE", "zh": "个人防护装备", "abbreviation": "PPE",
                    "aliases": [], "definition": "个人防护装备。", "source_definition": "安全守则。",
                    "first_occurrence": "page/sop/设备操作SOP.md", "related_concepts": ["C01"]}]})
    dump_yaml(os.path.join(root, "_meta", "claims.yaml"),
        {"claims": [{"id": "C01", "claim": "操作前必须佩戴 PPE。", "claim_type": "source-derived",
                     "concept_ids": ["C01"], "evidence_ids": ["E01"], "status": "verified", "confidence": "high"}]})
    dump_yaml(os.path.join(root, "_meta", "evidence.yaml"),
        {"evidence": [{"id": "E01", "source_type": "official_documentation", "source_title": "实验室安全守则",
                       "source_locator": "第 1 节", "accessed_at": "2026-01-02", "claim_ids": ["C01"], "figure_ids": [], "confidence": "high"}]})
    dump_yaml(os.path.join(root, "_meta", "concepts.yaml"),
        {"concepts": [{"id": "C01", "name_zh": "PPE", "name_en": "PPE", "aliases": [],
                       "definition_zh": "个人防护装备。", "page": "page/sop/设备操作SOP.md",
                       "evidence_ids": ["E01"], "figure_ids": [], "equation_ids": [], "related": []}]})
    dump_yaml(os.path.join(root, "_meta", "figures.yaml"), {"figures": []})
    dump_yaml(os.path.join(root, "_meta", "equations.yaml"), {"equations": []})
    dump_yaml(os.path.join(root, "_meta", "source-inventory.yaml"),
        {"items": [{"id": "S01", "item_type": "rule", "item_name": "佩戴PPE", "expected_page": "page/sop/设备操作SOP.md", "expect_keywords": ["PPE"]}]})
    dump_yaml(os.path.join(root, "_meta", "omissions.yaml"), {"items": []})
    dump_yaml(os.path.join(root, "_meta", "status.yaml"),
        {"legacy_unverified": False, "visual_evidence_status": "verified"})


def main():
    for folder, fn in [
        ("course", make_course),
        ("project-docs", make_project),
        ("lab-sop", make_sop),
        ("technical-tutorial", make_technical),
    ]:
        root = os.path.join(FIX, folder)
        os.makedirs(root, exist_ok=True)
        fn(root)
        print("generated", folder)


if __name__ == "__main__":
    main()
