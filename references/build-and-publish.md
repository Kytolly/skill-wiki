# 本地预览与远端发布

本文定义"本地能看、远端能发"的标准做法。模板文件在 `references/templates/`。

## 本地预览（mkdocs-material）

原理：源页面用 GitHub Wiki 的 `[[页名]]` 链接，mkdocs 不识别，所以 `build.py` 先把 `page/**` 拍平并转换链接，再交给 mkdocs 渲染。

1. 在 `build/preview/` 建 venv 并安装 mkdocs-material：

```bash
python3 -m venv build/preview/.venv
build/preview/.venv/bin/pip install "mkdocs-material>=9.7"
```

2. 运行预览：

```bash
./script/serve.sh        # 内部：build.py 生成 docs → mkdocs serve -a 127.0.0.1:8000
```

3. 打开 `http://127.0.0.1:8000/`。

`build.py` 规则：

- 遍历 `page/**/*.md`，把 `[[页名]]` 转成 `[页名](页名.md)`（`Home` → `index.md`）。
- 拍平到 `build/preview/docs/`（要求 page 内 basename 唯一）。
- 跳过 `_Sidebar.md`、`_Footer.md`（只给 GitHub Wiki 用；mkdocs 导航来自 mkdocs.yml）。

## 远端发布（GitHub Wiki）

GitHub Wiki 是独立仓库 `<repo>.wiki.git`（分支 `master`），要求**扁平结构**。`publish-wiki.sh` 负责把 `page/**/*.md` 拍平（按 basename）复制到临时仓库并推送。

```bash
./script/publish-wiki.sh
```

- 发布后访问：`https://github.com/<owner>/<repo>/wiki`。
- 判断是否已发布：`git ls-remote https://github.com/<owner>/<repo>.wiki.git`；返回 commit=已发布，`Repository not found`=未发布。

## 已知坑（务必记录）

1. **私有仓库 + 免费计划没有 GitHub Wiki**（公开仓库免费可用；私有仓库 Wiki 需 Pro/Team/Enterprise 或转公开）。此时只用本地预览。
2. mkdocs 的 `-f` 必须放在子命令后：`mkdocs serve -f <config>`，不能 `mkdocs -f <config> serve`。
3. `build/` 必须进 `.gitignore`，避免把 venv/产物提交进仓库。
4. `page/` 内所有页面 basename 必须唯一（拍平依赖 basename），发布/构建前做冲突检查。
5. GitHub Wiki 特殊文件 `Home.md`、`_Sidebar.md`、`_Footer.md` 必须放在 `page/` 根，拍平后落在 wiki 根。

## 模板清单

- `references/templates/build.py`
- `references/templates/serve.sh`
- `references/templates/publish-wiki.sh`
- `references/templates/mkdocs.yml`
- `references/templates/.gitignore`
