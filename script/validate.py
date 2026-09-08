#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA validator: evidence/terminology/figure/equation/link/meta consistency.

Usage:
    python3 script/validate.py --wiki-root <path> [--out build/qa-report.json] [--markdown docs/qa-report.md]

Environment:
    WIKI_ROOT=<path>  # alternative to --wiki-root
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wiki_common import (
    ALLOWED_MODES, page_dir, meta_dir, load_yaml, load_list, index_by_id,
    iter_md_files, read_text, meta_field, find_id_refs, figure_markers,
    equation_markers, wikilinks, page_basenames,
)


REQUIRED_META_FIELDS = [
    "wiki_mode", "audience", "source_policy", "source_hierarchy",
    "terminology_policy", "evidence_policy", "figure_policy",
    "completeness_policy", "external_knowledge_policy",
    "last_source_audit", "last_coverage_audit",
]


def collect_pages(root):
    pdir = page_dir(root)
    pages = []
    for path in iter_md_files(pdir):
        rel = os.path.relpath(path, pdir).replace(os.sep, "/")
        pages.append({"path": path, "rel": rel, "name": os.path.basename(path)[:-3], "text": read_text(path)})
    return pages


def check(cid, name, status, detail="", items=None):
    return {"id": cid, "name": name, "status": status, "detail": detail, "items": items or []}


def run_checks(root):
    pdir = page_dir(root)
    pages = collect_pages(root)
    all_text = "\n".join(p["text"] for p in pages)
    meta_mode = meta_field(root, "wiki_mode")
    checks = []

    # 1. mode compliance
    if meta_mode in ALLOWED_MODES:
        detail = "mode = " + meta_mode
        if meta_mode == "custom" and not meta_field(root, "custom_reason"):
            checks.append(check("mode_compliance", "Mode compliance", "error", "custom mode requires custom_reason"))
        else:
            checks.append(check("mode_compliance", "Mode compliance", "pass", detail))
    else:
        checks.append(check("mode_compliance", "Mode compliance", "error", "missing/invalid wiki_mode: " + str(meta_mode)))

    # 2. META completeness
    missing = [f for f in REQUIRED_META_FIELDS if not meta_field(root, f)]
    if missing:
        checks.append(check("meta_completeness", "META completeness", "error", "missing fields", missing))
    else:
        checks.append(check("meta_completeness", "META completeness", "pass"))

    # 3/4. terminology
    terms = load_list(root, "terminology.yaml")
    term_by_id = index_by_id(terms)
    term_errors = [t["id"] for t in terms if not (t.get("id") and t.get("canonical_en") and t.get("zh") and t.get("definition"))]
    if term_errors:
        checks.append(check("terminology_consistency", "Terminology consistency", "error", "terms missing required fields", term_errors))
    else:
        checks.append(check("terminology_consistency", "Terminology consistency", "pass"))
    lost = []
    for t in terms:
        en = t.get("canonical_en") or ""
        abbr = t.get("abbreviation") or ""
        if en and en not in all_text and (not abbr or abbr not in all_text):
            lost.append(t["id"])
    if lost:
        checks.append(check("terminology_preservation", "English terminology preservation", "warn", "canonical English/abbrev not found in pages", lost))
    else:
        checks.append(check("terminology_preservation", "English terminology preservation", "pass"))
    abbrev_missing = []
    for t in terms:
        if t.get("abbreviation"):
            abbr = t["abbreviation"]
            en = t.get("canonical_en", "")
            if abbr not in all_text or (en and en not in all_text):
                abbrev_missing.append(t["id"])
    if abbrev_missing:
        checks.append(check("abbreviation_definition", "Abbreviation definition", "warn", "abbrev used but canonical_en not present", abbrev_missing))
    else:
        checks.append(check("abbreviation_definition", "Abbreviation definition", "pass"))

    # 5/6. claims + evidence
    claims = load_list(root, "claims.yaml")
    claim_by_id = index_by_id(claims)
    evidence = load_list(root, "evidence.yaml")
    evidence_by_id = index_by_id(evidence)
    unsupported = []
    ev_missing = []
    for p in pages:
        for cid in find_id_refs(p["text"], "C"):
            claim = claim_by_id.get("C" + cid)
            if not claim or not claim.get("evidence_ids"):
                unsupported.append({"page": p["rel"], "claim": "C" + cid})
        for eid in find_id_refs(p["text"], "E"):
            if "E" + eid not in evidence_by_id:
                ev_missing.append({"page": p["rel"], "evidence": "E" + eid})
    if unsupported:
        checks.append(check("unsupported_claim", "Unsupported claim detection", "error", "claims referenced without evidence", unsupported))
    else:
        checks.append(check("unsupported_claim", "Unsupported claim detection", "pass"))
    if ev_missing:
        checks.append(check("evidence_integrity", "Evidence ID integrity", "error", "evidence refs not in evidence.yaml", ev_missing))
    else:
        checks.append(check("evidence_integrity", "Evidence ID integrity", "pass"))
    no_source = [e["id"] for e in evidence if not (e.get("source_url") or e.get("source_file") or e.get("source_locator"))]
    if no_source:
        checks.append(check("evidence_source", "Evidence source coverage", "warn", "evidence missing source_url/file", no_source))
    else:
        checks.append(check("evidence_source", "Evidence source coverage", "pass"))

    # 7/8/9/10. figures
    figures = load_list(root, "figures.yaml")
    fig_by_id = index_by_id(figures)
    fig_bad = []
    fig_missing_expl = []
    fig_broken = []
    derived_missing = []
    for p in pages:
        for fid in figure_markers(p["text"]):
            fig = fig_by_id.get(fid)
            if not fig:
                fig_bad.append({"page": p["rel"], "figure": fid})
            else:
                if not (fig.get("explanation") and fig.get("what_to_notice")):
                    fig_missing_expl.append({"figure": fid, "page": p["rel"]})
                if not (fig.get("source") or fig.get("source_url") or fig.get("local_asset") or fig.get("source_type")):
                    fig_bad.append({"page": p["rel"], "figure": fid})
                if fig.get("local_asset") and not os.path.exists(os.path.join(root, fig["local_asset"])):
                    fig_broken.append({"figure": fid, "asset": fig["local_asset"]})
                if fig.get("source_type") in ("generated_diagram", "derived") and not fig.get("derived_from"):
                    derived_missing.append({"figure": fid})
    if fig_bad:
        checks.append(check("figure_explanation_coverage", "Figure explanation/source coverage", "error", "figure missing or without source", fig_bad))
    else:
        checks.append(check("figure_explanation_coverage", "Figure explanation/source coverage", "pass"))
    if fig_missing_expl:
        checks.append(check("figure_explanation", "Figure explanation coverage", "error", "figure without explanation", fig_missing_expl))
    else:
        checks.append(check("figure_explanation", "Figure explanation coverage", "pass"))
    if fig_broken:
        checks.append(check("broken_figure_links", "Broken figure links", "error", "local asset missing", fig_broken))
    else:
        checks.append(check("broken_figure_links", "Broken figure links", "pass"))
    if derived_missing:
        checks.append(check("derived_mermaid", "Derived Mermaid marking", "error", "derived figure lacks derived_from", derived_missing))
    else:
        checks.append(check("derived_mermaid", "Derived Mermaid marking", "pass"))

    # 11. equations
    eqs = load_list(root, "equations.yaml")
    eq_by_id = index_by_id(eqs)
    eq_bad = []
    for p in pages:
        for eqid in equation_markers(p["text"]):
            eq = eq_by_id.get(eqid)
            if not eq or not (eq.get("latex") and eq.get("source") and eq.get("explanation")):
                eq_bad.append({"page": p["rel"], "equation": eqid})
    if eq_bad:
        checks.append(check("equation_source_coverage", "Equation source coverage", "error", "equation missing or without source", eq_bad))
    else:
        checks.append(check("equation_source_coverage", "Equation source coverage", "pass"))

    # 12. broken wiki links
    known = page_basenames(pdir) | {"Home"}
    dead = []
    for p in pages:
        for link in wikilinks(p["text"]):
            if link not in known and not link.endswith(".md"):
                dead.append({"page": p["rel"], "link": link})
    if dead:
        checks.append(check("dead_wiki_links", "Dead Wiki links", "error", "links without matching page", dead))
    else:
        checks.append(check("dead_wiki_links", "Dead Wiki links", "pass"))

    # 13. sidebar completeness
    sidebar_path = os.path.join(pdir, "_Sidebar.md")
    sidebar_text = read_text(sidebar_path) if os.path.isfile(sidebar_path) else ""
    listed = wikilinks(sidebar_text) if sidebar_text else set()
    not_listed = [p["name"] for p in pages if p["name"] not in ("Home", "_Sidebar", "_META", "_Footer") and p["name"] not in listed]
    if not_listed:
        checks.append(check("sidebar_completeness", "Sidebar completeness", "error", "pages not in _Sidebar", not_listed))
    else:
        checks.append(check("sidebar_completeness", "Sidebar completeness", "pass"))

    # 14. home completeness
    home_path = os.path.join(pdir, "Home.md")
    if os.path.isfile(home_path):
        home_text = read_text(home_path)
        if not wikilinks(home_text):
            checks.append(check("home_completeness", "Home completeness", "warn", "Home has no page links"))
        else:
            checks.append(check("home_completeness", "Home completeness", "pass"))
    else:
        checks.append(check("home_completeness", "Home completeness", "error", "Home.md missing"))

    # 15. knowledge graph / orphan concept
    concepts = load_list(root, "concepts.yaml")
    concept_by_id = index_by_id(concepts)
    orphan = [c["id"] for c in concepts if not c.get("page") or not os.path.exists(os.path.join(root, c["page"]))]
    if orphan:
        checks.append(check("orphan_concept", "Orphan concept", "warn", "concept missing page/file", orphan))
    else:
        checks.append(check("orphan_concept", "Orphan concept", "pass"))
    broken_rel = []
    for c in concepts:
        for rel in c.get("related") or []:
            if rel.get("concept_id") not in concept_by_id:
                broken_rel.append({"concept": c["id"], "ref": rel.get("concept_id")})
    if broken_rel:
        checks.append(check("broken_concept_relation", "Knowledge graph relations", "error", "relation to missing concept", broken_rel))
    else:
        checks.append(check("broken_concept_relation", "Knowledge graph relations", "pass"))

    # 16. provenance header
    no_prov = [p["rel"] for p in pages if p["name"] not in ("Home", "_Sidebar", "_META", "_Footer") and "> provenance:" not in p["text"]]
    if no_prov:
        checks.append(check("source_vs_explanation_separation", "Source vs explanation separation", "warn", "pages missing provenance header", no_prov))
    else:
        checks.append(check("source_vs_explanation_separation", "Source vs explanation separation", "pass"))

    # 17. visual evidence status
    status = load_yaml(os.path.join(meta_dir(root), "status.yaml"))
    if isinstance(status, dict) and status.get("visual_evidence_status") == "unverified":
        checks.append(check("visual_evidence", "Visual evidence status", "warn", "visual extraction unavailable; not verified"))
    else:
        checks.append(check("visual_evidence", "Visual evidence status", "pass"))

    return checks


def summarize(checks):
    counts = {"error": 0, "warn": 0, "pass": 0}
    for c in checks:
        counts[c["status"]] = counts.get(c["status"], 0) + 1
    return counts


def main(argv=None):
    argv = list(argv if argv is not None else sys.argv[1:])
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki-root", "--root", dest="root", default=None)
    ap.add_argument("--out", default="qa-report.json")
    ap.add_argument("--markdown", default=None)
    args = ap.parse_args(argv)
    root = os.path.abspath(args.root) if args.root else os.path.abspath(os.getcwd())
    checks = run_checks(root)
    summary = summarize(checks)
    out_path = args.out if os.path.isabs(args.out) else os.path.join(root, "build", args.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    report = {"summary": summary, "checks": checks}
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    if args.markdown:
        md_path = args.markdown if os.path.isabs(args.markdown) else os.path.join(root, "docs", args.markdown)
        os.makedirs(os.path.dirname(md_path), exist_ok=True)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("# QA Report\n\n")
            f.write("| Check | Status | Detail |\n|---|---|---|\n")
            for c in checks:
                f.write("| {} | {} | {} |\n".format(c["id"], c["status"], c["detail"].replace("|", "\\|")))
    print("QA summary: {}".format(summary))
    for c in checks:
        if c["status"] in ("error", "warn"):
            print("  [{}] {}: {}".format(c["status"].upper(), c["id"], c["detail"]))
    print("JSON -> {}".format(out_path))
    return 0 if summary.get("error", 0) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
