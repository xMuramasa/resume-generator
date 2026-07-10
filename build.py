#!/usr/bin/env python3
"""Markdown resume -> PDF via headless Chrome.

Usage: python3 build.py [file.md ...]
Env:   RESUME_SRC  dir with resume .md files (default: ~/Github/personal/xMuramasa)
       RESUME_OUT  output dir for html/pdf   (default: this script's dir)
       CHROME_BIN  Chrome binary             (default: macOS Google Chrome path)
"""
import html
import os
import pathlib
import re
import subprocess
import sys

CHROME = os.environ.get(
    "CHROME_BIN", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)
SRC = pathlib.Path(
    os.environ.get("RESUME_SRC", "~/Github/personal/xMuramasa")
).expanduser()
OUT = pathlib.Path(
    os.environ.get("RESUME_OUT", pathlib.Path(__file__).parent)
).expanduser()

CSS = """
@page { size: letter; margin: 1.5cm 1.7cm; }
* { margin: 0; padding: 0; }
body {
  font: 10pt/1.4 "Helvetica Neue", Helvetica, Arial, sans-serif;
  color: #222;
}
h1 { font-size: 20pt; text-align: center; letter-spacing: 2px; color: #1a365d; }
h1 + p { text-align: center; margin-bottom: 4pt; }
h2 {
  font-size: 11pt; text-transform: uppercase; letter-spacing: 1.5px;
  color: #1a365d; border-bottom: 1.5px solid #1a365d;
  margin: 12pt 0 5pt; padding-bottom: 2pt;
  break-after: avoid;
}
h3 { font-size: 10.5pt; margin-top: 8pt; break-after: avoid; }
h3 + p { color: #555; margin-bottom: 2pt; }
p { margin: 2pt 0; }
ul { margin: 2pt 0 2pt 14pt; }
li { margin: 2.5pt 0; break-inside: avoid; }
a { color: inherit; }
strong { color: #1a365d; }
"""


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    return text


def md_to_html(md):
    out, in_list = [], False
    for line in md.splitlines():
        line = line.strip()
        if in_list and not line.startswith("* "):
            out.append("</ul>")
            in_list = False
        if not line or line == "---":
            continue
        if line.startswith("* "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(line[2:])}</li>")
        elif m := re.match(r"(#{1,3}) (.+)", line):
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
        else:
            out.append(f"<p>{inline(line)}</p>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def build(md_path):
    md_path = pathlib.Path(md_path)
    body = md_to_html(md_path.read_text())
    page = f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>\n{body}'
    html_path = OUT / f"{md_path.stem}.html"
    html_path.write_text(page)
    pdf_path = OUT / f"{md_path.stem}.pdf"
    subprocess.run(
        [CHROME, "--headless", f"--print-to-pdf={pdf_path}",
         "--no-pdf-header-footer", html_path.resolve().as_uri()],
        check=True, capture_output=True,
    )
    print(f"{md_path.name} -> {pdf_path}")


if __name__ == "__main__":
    assert md_to_html("## **X**\n* a [b](c)") == \
        '<h2><strong>X</strong></h2>\n<ul>\n<li>a <a href="c">b</a></li>\n</ul>'
    files = sys.argv[1:] or [
        p for p in sorted(SRC.glob("*.md")) if p.name.lower() != "readme.md"
    ]
    for f in files:
        build(f)
