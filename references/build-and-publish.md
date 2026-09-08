# 本地预览与远端发布

本文定义“本地能看、远端能发”与“能校验、能审计”的标准做法。模板/脚本在 `references/templates/`，当前仓库在 `script/` 也有可直接运行的副本。

## 校验与覆盖度（新增）

生成/更新前后应运行：

```bash
python3 script/validate.py --wiki-root .
python3 script/coverage.py --wiki-root .
```

- validate.py 输出 `build/qa-report.json`（机器可读）与 stdout 总结。
- coverage.py 输出 `build/coverage-report.json` 与 `docs/coverage-report.md`。
- 发布前先跑 validate，修复 error 级问题。

## 本地预览（mkdocs-material）

1. 建 venv 并安装：

```bash
python3 -m venv build/preview/.venv
build/preview/.venv/bin/pip install "mkdocs-material>=9.7"
```

2. 运行：

```bash
./script/serve.sh
```

3. 打开 `http://127.0.0.1:8000/`。

`build.py` 规则：

- 遍历 `page/**/*.md`，把 `[[页名]]` 转成 `[页名](页名.md)`（Home → index.md）。
- 拍平到 `build/preview/docs/`（仅 `page/` 内容；`_meta/` 不参与预览渲染，但被 validator/coverage 消费）。
- 跳过 `_Sidebar.md`、`_Footer.md`。

## 远端发布（GitHub Wiki）

```bash
./script/publish-wiki.sh
```

- 发布后访问：`https://github.com/<owner>/<repo>/wiki`。
- 判断是否已发布：`git ls-remote https://github.com/<owner>/<repo>.wiki.git`。

## 已知坑

1. **私有仓库 + 免费计划没有 GitHub Wiki**（公开仓库免费；私有需 Pro/Team/Enterprise 或转公开）。此时只用本地预览。
2. mkdocs 的 `-f` 必须放在子命令后：`mkdocs serve -f <config>`。
3. `build/` 必须进 `.gitignore`。
4. `page/` 内 basename 必须唯一（拍平依赖 basename）。
5. GitHub Wiki 特殊文件 `Home.md`、`_Sidebar.md`、`_Footer.md` 必须在 `page/` 根。
6. `_meta/` 与 `docs/` 会提交；`build/` 不提交。
7. 图片发布到 GitHub Wiki 需单独托管或同步；否则本地预览有图、Wiki 无图。

## 模板清单

- `references/templates/build.py`、`serve.sh`、`publish-wiki.sh`、`mkdocs.yml`、`.gitignore`
- `references/templates/validate.py`、`coverage.py`、`migrate.py`