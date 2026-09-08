#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Local preview build: flatten page/** and convert [[links]] for mkdocs.

Usage:
    python3 script/build.py [--wiki-root <path>] [--docs <path>]

Output: <wiki-root>/build/preview/docs (flattened, wiki-link converted).
Only page/ content is built; _meta/ is metadata (not rendered) but is used by
validate.py / coverage.py.
"""
import argparse
import os
import shutil

SKIP = {"_Sidebar.md", "_Footer.md"}


def target_name(name):
    return "index.md" if name == "Home" else name + ".md"


def convert(text):
    out = []
    i, n = 0, len(text)
    while i < n:
        if text.startswith("[[", i):
            j = text.find("]]", i)
            if j != -1:
                name = text[i + 2:j].strip()
                out.append("[{}]({})".format(name, target_name(name)))
                i = j + 2
                continue
        out.append(text[i])
        i += 1
    return "".join(out)


def page_dir(root):
    p = os.path.join(root, "page")
    if os.path.isdir(p):
        return p
    return root


def build(root):
    src = page_dir(root)
    dst = os.path.join(root, "build", "preview", "docs")
    shutil.rmtree(dst, ignore_errors=True)
    os.makedirs(dst, exist_ok=True)
    for dirpath, _, files in os.walk(src):
        for f in files:
            if not f.endswith(".md") or f in SKIP:
                continue
            path = os.path.join(dirpath, f)
            text = convert(open(path, encoding="utf-8").read())
            name = "index.md" if f == "Home.md" else f
            with open(os.path.join(dst, name), "w", encoding="utf-8") as out:
                out.write(text)
            print("built", name)
    css_dir = os.path.join(dst, "stylesheets")
    os.makedirs(css_dir, exist_ok=True)
    with open(os.path.join(css_dir, "extra.css"), "w", encoding="utf-8") as out:
        out.write(".md-typeset .grid.cards > ul > li { border-radius: 0.5rem; }\n.md-typeset .wiki-meta { color: var(--md-default-fg-color--light); font-size: 0.82rem; }\n")
    print("built stylesheets/extra.css")


def main(argv=None):
    import sys
    argv = list(argv if argv is not None else sys.argv[1:])
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki-root", "--root", dest="root", default=None)
    args = ap.parse_args(argv)
    root = os.path.abspath(args.root) if args.root else os.path.abspath(os.getcwd())
    build(root)


if __name__ == "__main__":
    main()
