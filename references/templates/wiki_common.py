#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared helpers for skill-tutorial-wiki tooling."""
import os
import re
import sys
import yaml

ALLOWED_MODES = [
    "course", "project-docs", "lab-handbook", "technical-tutorial", "research-kb",
    "api-docs", "experiment-kb", "onboarding", "policy-procedure", "custom",
]


def wiki_root_from_args(argv=None):
    """Return wiki root from --wiki-root/--root or env or cwd."""
    import argparse
    argv = list(argv if argv is not None else sys.argv[1:])
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--wiki-root", "--root", dest="wiki_root", default=None)
    args, _ = parser.parse_known_args(argv)
    if args.wiki_root:
        return os.path.abspath(args.wiki_root)
    if os.environ.get("WIKI_ROOT"):
        return os.path.abspath(os.environ["WIKI_ROOT"])
    return os.path.abspath(os.getcwd())


def page_dir(root):
    """Return directory that holds markdown pages under wiki root."""
    p = os.path.join(root, "page")
    if os.path.isdir(p):
        return p
    # legacy: wiki root itself is the page dir
    if any(f.endswith(".md") for f in os.listdir(root)):
        return root
    return p


def meta_dir(root):
    return os.path.join(root, "_meta")


def load_yaml(path):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def iter_md_files(pdir):
    for dirpath, _, files in os.walk(pdir):
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(dirpath, f)


def page_basenames(pdir):
    names = set()
    for path in iter_md_files(pdir):
        base = os.path.basename(path)[:-3]
        if base not in ("_Sidebar", "_Footer", "_META", "Home"):
            names.add(base)
    return names


def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def meta_field(root, key):
    """Parse a simple `- key: value` line from _META.md."""
    path = os.path.join(page_dir(root), "_META.md")
    if not os.path.isfile(path):
        return None
    text = read_text(path)
    m = re.search(r"^\s*-\s*" + re.escape(key) + r"\s*[:：]\s*(.*)$", text, re.M)
    return m.group(1).strip() if m else None


def find_id_refs(text, prefix):
    """Return set of ids referenced like [C01], [E01], [F01], [EQ01]."""
    return set(re.findall(r"\[" + prefix + r"(\d+)\]", text, re.I))


def figure_markers(text):
    return set(re.findall(r"<!-- FIGURE:\s*(F\d+)\s*-->", text, re.I))


def equation_markers(text):
    return set(re.findall(r"<!-- EQUATION:\s*(EQ\d+)\s*-->", text, re.I))


def wikilinks(text):
    return set(re.findall(r"\[\[([^]]+)\]\]", text))


def load_list(root, name):
    data = load_yaml(os.path.join(meta_dir(root), name))
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for k in ("terms", "evidence", "claims", "concepts", "figures", "equations", "items"):
            if isinstance(data.get(k), list):
                return data[k]
    return []


def index_by_id(items):
    return {it.get("id"): it for it in items if it.get("id")}