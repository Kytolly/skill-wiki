#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Coverage audit: compare source inventory against wiki outline.

Usage:
    python3 script/coverage.py --wiki-root <path> [--out build/coverage-report.json] [--markdown docs/coverage-report.md]

Reads:
    _meta/source-inventory.yaml   (list of expected items)
    _meta/omissions.yaml          (explicitly skipped items)

For each item, determines covered / omitted / missing and writes a report.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wiki_common import page_dir, meta_dir, load_yaml, load_list, read_text, iter_md_files, figure_markers, equation_markers, find_id_refs, index_by_id


def load_omission_ids(root):
    items = load_list(root, "omissions.yaml")
    return {it.get("id") for it in items if it.get("id")}


def page_text_map(root):
    pdir = page_dir(root)
    mapping = {}
    for path in iter_md_files(pdir):
        rel = os.path.relpath(path, pdir).replace(os.sep, "/")
        mapping[rel] = read_text(path)
    return mapping


def item_covered_in(text, item):
    """Heuristic: item is covered if its marker/keywords/name are present."""
    marker = item.get("item_marker")
    if marker:
        # item_marker looks like "FIGURE: F01", "EQUATION: EQ01", "CLAIM: C01", "TERM: T01"
        if marker.startswith("MARKER "):
            return marker[7:] in text
        return ("<!-- " + marker.split(":", 1)[0].strip().upper() + ": " + marker.split(":", 1)[1].strip() + " -->") in text
    norm_text = text.replace(" ", "").replace("\u3000", "")
    name = item.get("item_name") or ""
    if name and name.replace(" ", "") in norm_text:
        return True
    for kw in item.get("expect_keywords") or []:
        if kw in text:
            return True
    itype = item.get("item_type")
    if itype == "claim" and item.get("claim_id"):
        return ("[" + item["claim_id"] + "]") in text
    if itype == "figure" and item.get("figure_id"):
        return ("<!-- FIGURE: " + item["figure_id"] + " -->") in text
    if itype == "equation" and item.get("equation_id"):
        return ("<!-- EQUATION: " + item["equation_id"] + " -->") in text
    if itype == "terminology" and item.get("term_id"):
        return ("<!-- TERM: " + item["term_id"] + " -->") in text or item.get("canonical_en") in text
    return False


def run_coverage(root):
    items = load_list(root, "source-inventory.yaml")
    if not items:
        return {
            "items": [],
            "summary": {"total": 0, "covered": 0, "omitted": 0, "missing": 0, "coverage_pct": 100.0},
            "missing": [],
        }
    pages = page_text_map(root)
    omit_ids = load_omission_ids(root)
    result_items = []
    missing = []
    for it in items:
        status = it.get("status")
        if status == "omitted" or it.get("id") in omit_ids:
            st = "omitted"
        else:
            expected = it.get("expected_page")
            if expected and expected in pages:
                covered = item_covered_in(pages[expected], it)
            else:
                covered = any(item_covered_in(t, it) for t in pages.values())
            st = "covered" if covered else "missing"
            if st == "missing":
                missing.append(it)
        result_items.append({**it, "coverage_status": st})
    total = len(result_items)
    covered = sum(1 for x in result_items if x["coverage_status"] == "covered")
    omitted = sum(1 for x in result_items if x["coverage_status"] == "omitted")
    missing_n = sum(1 for x in result_items if x["coverage_status"] == "missing")
    pct = (covered / total * 100.0) if total else 100.0
    return {
        "items": result_items,
        "summary": {"total": total, "covered": covered, "omitted": omitted, "missing": missing_n, "coverage_pct": round(pct, 1)},
        "missing": missing,
    }


def main(argv=None):
    argv = list(argv if argv is not None else sys.argv[1:])
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki-root", "--root", dest="root", default=None)
    ap.add_argument("--out", default="coverage-report.json")
    ap.add_argument("--markdown", default=None)
    args = ap.parse_args(argv)
    root = os.path.abspath(args.root) if args.root else os.path.abspath(os.getcwd())
    report = run_coverage(root)
    out_path = args.out if os.path.isabs(args.out) else os.path.join(root, "build", args.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    if args.markdown:
        md_path = args.markdown if os.path.isabs(args.markdown) else os.path.join(root, "docs", args.markdown)
        os.makedirs(os.path.dirname(md_path), exist_ok=True)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("# Coverage Report\n\n")
            f.write("Total: **{}**  Covered: **{}**  Omitted: **{}**  Missing: **{}**  Coverage: **{}%**\n\n".format(
                report["summary"]["total"], report["summary"]["covered"], report["summary"]["omitted"], report["summary"]["missing"], report["summary"]["coverage_pct"]))
            f.write("| Item | Type | Status | Page |\n|---|---|---|---|\n")
            for x in report["items"]:
                f.write("| {} | {} | {} | {} |\n".format(x.get("id", ""), x.get("item_type", ""), x["coverage_status"], x.get("expected_page", "")))
    print("Coverage summary: {}".format(report["summary"]))
    for m in report["missing"]:
        print("  MISSING: {} [{}] expected_page={}".format(m.get("item_name"), m.get("item_type"), m.get("expected_page")))
    print("JSON -> {}".format(out_path))
    return 0 if report["summary"]["missing"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
