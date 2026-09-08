#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legacy wiki migration: detect missing _meta/ and create skeleton metadata.

Usage:
    python3 script/migrate.py --wiki-root <path> [--dry-run]

Behavior:
    - If _meta/ is absent or empty, create it with empty YAML skeletons.
    - Mark a legacy wiki with provenance: legacy-unverified in _META.md and
      set _meta/status.yaml legacy_unverified: true.
    - Idempotent: a second run is a no-op.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wiki_common import page_dir, meta_dir, read_text


SKELETON_FILES = {
    "terminology.yaml": "terms: []\n",
    "evidence.yaml": "evidence: []\n",
    "claims.yaml": "claims: []\n",
    "concepts.yaml": "concepts: []\n",
    "figures.yaml": "figures: []\n",
    "equations.yaml": "equations: []\n",
    "source-inventory.yaml": "items: []\n",
    "omissions.yaml": "items: []\n",
    "status.yaml": "legacy_unverified: true\nvisual_evidence_status: unverified\n",
}


def has_meta(root):
    d = meta_dir(root)
    return os.path.isdir(d) and any(fname.endswith(".yaml") for fname in os.listdir(d))


def migrate(root, dry_run=False):
    reports = []
    if has_meta(root):
        return {"migrated": False, "detail": "_meta/ already present", "reports": reports}
    d = meta_dir(root)
    if not dry_run:
        os.makedirs(d, exist_ok=True)
        for name, body in SKELETON_FILES.items():
            path = os.path.join(d, name)
            if not os.path.exists(path):
                with open(path, "w", encoding="utf-8") as f:
                    f.write(body)
                reports.append("created _meta/" + name)
    # update _META.md
    meta_path = os.path.join(page_dir(root), "_META.md")
    if os.path.isfile(meta_path):
        text = read_text(meta_path)
        if "provenance: legacy-unverified" not in text:
            if not dry_run:
                with open(meta_path, "w", encoding="utf-8") as f:
                    if not text.endswith("\n"):
                        text += "\n"
                    f.write(text + "- provenance: legacy-unverified\n- legacy_migrated: true\n")
            reports.append("updated _META.md (provenance: legacy-unverified)")
    return {"migrated": True, "detail": "legacy wiki migrated", "reports": reports}


def main(argv=None):
    argv = list(argv if argv is not None else sys.argv[1:])
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki-root", "--root", dest="root", default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    root = os.path.abspath(args.root) if args.root else os.path.abspath(os.getcwd())
    result = migrate(root, dry_run=args.dry_run)
    print("migrated:", result["migrated"])
    print("detail:", result["detail"])
    for r in result["reports"]:
        print("  ", r)
    return 0


if __name__ == "__main__":
    sys.exit(main())
