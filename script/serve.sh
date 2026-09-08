#!/usr/bin/env bash
# 本地 wiki 网页预览：生成 docs 并用 mkdocs-material 启动。
# 用法：./script/serve.sh [--root <wiki-root>]  或  WIKI_ROOT=<path> ./script/serve.sh
set -euo pipefail
ROOT="${1:-${WIKI_ROOT:-$(pwd)}}"
if [ "${1:-}" = "--root" ]; then ROOT="$2"; fi
cd "${ROOT}"
python3 "${ROOT}/script/build.py" --wiki-root "${ROOT}"
exec "${ROOT}/build/preview/.venv/bin/mkdocs" serve -f "${ROOT}/script/mkdocs.yml" -a 127.0.0.1:8000