# 配图与 Mermaid 规范

清晰的 figure/illustration 是教程的关键。本文件规定配图优先级与用法。

## 优先级

1. **官方图**：官方文档/仓库里的截图、架构图、示意图（记录来源 URL + 访问日期）。
2. **可验证的网络图**：权威网站/知名博客的图，带来源 URL + 访问日期 + 许可（尽量选可商用的）。
3. **自制 Mermaid**：找不到可靠图时，用 Mermaid 画流程图/时序图/架构图/状态图。
4. 严禁编造图片 URL；找不到可靠图就 Mermaid 或文字描述。

## 图片规范

- 每张图必须有 caption：`图 1 某某架构图`。
- caption 后附来源与访问日期：`来源：<url>（访问于 YYYY-MM-DD）`。
- 本地化：重要图片下载到 `page/assets/images/`（或 `page/<grade>/assets/`），用相对路径引用；外链图片有失效风险。
- 发布注意：`publish-wiki.sh` 只复制 `*.md`；图片如需随 GitHub Wiki 发布，要单独托管（图床/仓库附件）或嵌入相对路径并同步发布。

## Mermaid 规范

- 本地 mkdocs 预览：mkdocs.yml 启用 `pymdownx.superfences` 并开启 mermaid（模板已配好），fenced code 标注 `mermaid`。
- GitHub Wiki **不渲染 Mermaid**：Mermaid 块会显示为代码。二选一：
  1. 接受"预览渲染、Wiki 显示代码"的降级；
  2. 把 Mermaid 导出为 PNG 放进 assets，再按图片规范引用。
- 复杂流程用 Mermaid；简单结构可用 ASCII 图。

示例（本地预览会渲染成图）：

```mermaid
flowchart LR
  A[主题确认] --> B[联网调研] --> C[生成页面] --> D[本地预览] --> E[发布]
```
