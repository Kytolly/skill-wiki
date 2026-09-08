#!/usr/bin/env bash
# 一键把 page/ 下的 GitHub Wiki 页面拍平并发布到 <repo>.wiki.git
# 前置：仓库 Wikis 功能已开启（公开仓库免费可用；私有仓库需 Pro/Team/Enterprise 或转公开）
# 用法：./script/publish-wiki.sh [--root <wiki-root>]   WIKI_URL=... 可覆盖
set -euo pipefail
ROOT="${1:-${WIKI_ROOT:-$(pwd)}}"
if [ "${1:-}" = "--root" ]; then ROOT="$2"; fi
WIKI_URL="${WIKI_URL:-https://github.com/<OWNER>/<REPO>.wiki.git}"
PAGE_DIR="${ROOT}/page"
TMP_DIR="$(mktemp -d)"
echo "==> 页面目录: $PAGE_DIR"
echo "==> 临时仓库: $TMP_DIR"
git init -b master "$TMP_DIR" >/dev/null
while IFS= read -r f; do
  cp "$f" "$TMP_DIR/$(basename "$f")"
done < <(find "$PAGE_DIR" -type f -name "*.md" | sort)
cd "$TMP_DIR"
git add -A
git -c user.name="${GIT_AUTHOR_NAME:-your-name}" \
    -c user.email="${GIT_AUTHOR_EMAIL:-you@example.com}" \
    commit -m "publish wiki" >/dev/null
git remote add origin "$WIKI_URL"
echo "==> 推送到 $WIKI_URL"
git push -u origin master
echo "==> 完成。访问: ${WIKI_URL%.wiki.git}/wiki"