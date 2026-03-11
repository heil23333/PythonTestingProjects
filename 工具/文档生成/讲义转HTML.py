#!/usr/bin/env python3

from __future__ import annotations

import html
import re
import sys
from pathlib import Path


CSS = """
@page {
  size: A4;
  margin: 18mm 16mm 18mm 16mm;
}

:root {
  --ink: #1f2937;
  --muted: #6b7280;
  --line: #d9e1ea;
  --soft: #f6f8fb;
  --panel: #eef6f7;
  --accent: #0f766e;
  --accent-deep: #115e59;
  --code-bg: #0f172a;
  --code-ink: #e2e8f0;
}

html, body {
  margin: 0;
  padding: 0;
  color: var(--ink);
  background: #ffffff;
  font-family: "PingFang SC", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif;
  line-height: 1.72;
  font-size: 12pt;
}

body {
  padding: 0;
}

.cover {
  break-after: page;
  padding: 24mm 10mm 10mm;
}

.cover-kicker {
  color: var(--accent);
  font-size: 11pt;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 12pt;
}

.cover h1 {
  font-size: 28pt;
  line-height: 1.2;
  margin: 0 0 14pt;
  color: #0b1324;
}

.cover .summary {
  color: var(--muted);
  font-size: 13pt;
  max-width: 30em;
}

.cover .meta {
  margin-top: 22pt;
  padding: 14pt 16pt;
  border: 1px solid var(--line);
  border-radius: 14pt;
  background: linear-gradient(180deg, #f8fffe, #f4f7fb);
}

.cover .meta p {
  margin: 4pt 0;
}

.content {
  counter-reset: h2;
}

h1 {
  font-size: 22pt;
  margin: 0 0 16pt;
  color: #0b1324;
}

h2 {
  font-size: 17pt;
  margin: 24pt 0 10pt;
  padding-bottom: 6pt;
  border-bottom: 1.4pt solid var(--line);
  color: var(--accent-deep);
  page-break-after: avoid;
}

h3 {
  font-size: 13.5pt;
  margin: 16pt 0 6pt;
  color: #0b1324;
  page-break-after: avoid;
}

h4 {
  font-size: 12.5pt;
  margin: 12pt 0 4pt;
  color: #10233f;
}

p {
  margin: 8pt 0;
}

ul, ol {
  margin: 8pt 0 10pt 18pt;
  padding: 0;
}

li {
  margin: 3pt 0;
}

hr {
  border: 0;
  border-top: 1pt solid var(--line);
  margin: 16pt 0;
}

pre {
  background: var(--code-bg);
  color: var(--code-ink);
  padding: 12pt 14pt;
  border-radius: 10pt;
  overflow-wrap: anywhere;
  white-space: pre-wrap;
  font: 10.5pt/1.55 "SFMono-Regular", "Menlo", "Consolas", monospace;
}

code {
  font-family: "SFMono-Regular", "Menlo", "Consolas", monospace;
  font-size: 0.94em;
  background: #eef2f7;
  padding: 1pt 4pt;
  border-radius: 4pt;
}

pre code {
  background: transparent;
  padding: 0;
}

blockquote {
  margin: 10pt 0;
  padding: 8pt 12pt;
  border-left: 3pt solid var(--accent);
  background: var(--panel);
  color: #23414e;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 12pt 0;
  font-size: 10.8pt;
}

th, td {
  border: 1pt solid var(--line);
  padding: 7pt 8pt;
  vertical-align: top;
}

th {
  background: #edf5f4;
  text-align: left;
}

.callout {
  margin: 12pt 0;
  padding: 10pt 12pt;
  background: #f8fbff;
  border: 1pt solid #d7e4f2;
  border-radius: 10pt;
}

.note-title {
  font-weight: 700;
  color: var(--accent-deep);
}

.toc {
  margin: 0 0 20pt;
  padding: 12pt 14pt;
  border: 1pt solid var(--line);
  border-radius: 12pt;
  background: var(--soft);
}

.toc h2 {
  margin-top: 0;
  border-bottom: 0;
  padding-bottom: 0;
}

.toc ul {
  margin-bottom: 0;
}

.section-break {
  break-before: page;
}
"""


def inline_markup(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+?)`", r"<code>\1</code>", text)
    return text


def is_table_delimiter(line: str) -> bool:
    stripped = line.strip()
    if "|" not in stripped:
        return False
    parts = [part.strip() for part in stripped.strip("|").split("|")]
    return all(part and set(part) <= {"-", ":"} for part in parts)


def render_table(lines: list[str]) -> str:
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines]
    header = rows[0]
    body = rows[2:] if len(rows) > 2 and is_table_delimiter(lines[1]) else rows[1:]
    html_parts = ["<table>", "<thead><tr>"]
    html_parts.extend(f"<th>{inline_markup(cell)}</th>" for cell in header)
    html_parts.append("</tr></thead><tbody>")
    for row in body:
        html_parts.append("<tr>")
        for cell in row:
            html_parts.append(f"<td>{inline_markup(cell)}</td>")
        html_parts.append("</tr>")
    html_parts.append("</tbody></table>")
    return "".join(html_parts)


def render_markdown(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    paragraph: list[str] = []
    bullet_stack: list[str] = []
    code_lines: list[str] = []
    in_code = False
    i = 0

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            joined = " ".join(part.strip() for part in paragraph if part.strip())
            if joined:
                out.append(f"<p>{inline_markup(joined)}</p>")
            paragraph = []

    def close_lists() -> None:
        nonlocal bullet_stack
        while bullet_stack:
            out.append(f"</{bullet_stack.pop()}>")

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_paragraph()
            close_lists()
            if in_code:
                code_html = html.escape("\n".join(code_lines))
                out.append(f"<pre><code>{code_html}</code></pre>")
                code_lines = []
                in_code = False
            else:
                in_code = True
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        if not stripped:
            flush_paragraph()
            close_lists()
            i += 1
            continue

        if stripped == "---":
            flush_paragraph()
            close_lists()
            out.append("<hr />")
            i += 1
            continue

        if stripped.startswith("> "):
            flush_paragraph()
            close_lists()
            out.append(f"<blockquote>{inline_markup(stripped[2:].strip())}</blockquote>")
            i += 1
            continue

        if stripped.startswith("#"):
            flush_paragraph()
            close_lists()
            level = len(stripped) - len(stripped.lstrip("#"))
            content = stripped[level:].strip()
            level = min(level, 4)
            out.append(f"<h{level}>{inline_markup(content)}</h{level}>")
            i += 1
            continue

        if "|" in stripped and i + 1 < len(lines) and is_table_delimiter(lines[i + 1]):
            flush_paragraph()
            close_lists()
            table_lines = [lines[i], lines[i + 1]]
            i += 2
            while i < len(lines) and "|" in lines[i]:
                table_lines.append(lines[i])
                i += 1
            out.append(render_table(table_lines))
            continue

        if re.match(r"^\d+\.\s+", stripped):
            flush_paragraph()
            if not bullet_stack or bullet_stack[-1] != "ol":
                close_lists()
                out.append("<ol>")
                bullet_stack.append("ol")
            item = re.sub(r"^\d+\.\s+", "", stripped)
            out.append(f"<li>{inline_markup(item)}</li>")
            i += 1
            continue

        if stripped.startswith("- "):
            flush_paragraph()
            if not bullet_stack or bullet_stack[-1] != "ul":
                close_lists()
                out.append("<ul>")
                bullet_stack.append("ul")
            out.append(f"<li>{inline_markup(stripped[2:].strip())}</li>")
            i += 1
            continue

        paragraph.append(line)
        i += 1

    flush_paragraph()
    close_lists()
    return "\n".join(out)


def build_cover(title: str) -> str:
    return f"""
    <section class="cover">
      <div class="cover-kicker">Python API Automation</div>
      <h1>{html.escape(title)}</h1>
      <p class="summary">Day 1 讲义与配套练习，覆盖接口测试基础概念、HTTP 请求与响应、鉴权机制、文档阅读、手工调试与测试点设计。</p>
      <div class="meta">
        <p><strong>适用阶段：</strong> 7 天速成计划第 1 天</p>
        <p><strong>使用方式：</strong> 先学习讲义，再完成随堂检查和综合练习</p>
        <p><strong>输出目标：</strong> 调通接口、写出测试点、能进入第 2 天 <code>requests</code> 实战</p>
      </div>
    </section>
    """


def build_toc() -> str:
    items = [
        "本日学习目标",
        "接口与接口测试",
        "HTTP 与请求响应基础",
        "认证机制",
        "接口文档阅读",
        "手工调试流程",
        "测试点拆解",
        "配套练习与课后作业",
    ]
    toc_items = "".join(f"<li>{html.escape(item)}</li>" for item in items)
    return f"""
    <section class="toc">
      <h2>目录</h2>
      <ul>{toc_items}</ul>
    </section>
    """


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: markdown_handout_to_html.py <input.md> <output.html>", file=sys.stderr)
        return 1

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    source = input_path.read_text(encoding="utf-8")
    body = render_markdown(source)
    title_match = re.search(r"^#\s+(.+)$", source, flags=re.M)
    title = title_match.group(1).strip() if title_match else input_path.stem

    html_doc = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)}</title>
  <style>{CSS}</style>
</head>
<body>
  {build_cover(title)}
  <main class="content">
    {build_toc()}
    {body}
  </main>
</body>
</html>
"""
    output_path.write_text(html_doc, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
