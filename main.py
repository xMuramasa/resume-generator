#!/usr/bin/env python3
"""Markdown resume -> PDF via headless Chrome.

Usage: python3 main.py [file.md ...]
Config, from the environment or ./.env (see .env.example):
  RESUME_SRC  dir with resume .md files
  RESUME_OUT  output dir for pdfs
  CHROME_BIN  Chrome binary

Stdlib only — no venv/requirements needed.
Intermediate HTML goes to a temp dir; only PDFs land in RESUME_OUT.
"""
import os
import pathlib
import string
import subprocess
import sys
import tempfile

from markdown import md_to_html
from pdf import html_to_pdf

ROOT = pathlib.Path(__file__).parent
ENV_KEYS = ("RESUME_SRC", "RESUME_OUT", "CHROME_BIN")


def load_env(path):
    """Minimal .env loader: KEY=VALUE lines; real environment wins."""
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip().strip("'\""))


def config():
    load_env(ROOT / ".env")
    missing = [k for k in ENV_KEYS if not os.environ.get(k)]
    if missing:
        sys.exit(
            f"error: missing env vars: {', '.join(missing)}"
            " — set them in the environment or in .env (see .env.example)"
        )
    return tuple(pathlib.Path(os.environ[k]).expanduser() for k in ENV_KEYS)


def build(md_path, tmp_dir, out, chrome, template):
    page = template.substitute(body=md_to_html(md_path.read_text()))
    html_path = tmp_dir / f"{md_path.stem}.html"
    html_path.write_text(page)
    pdf_path = out / f"{md_path.stem}.pdf"
    html_to_pdf(html_path, pdf_path, chrome)
    print(f"{md_path.name} -> {pdf_path}")


def main():
    src, out, chrome = config()
    template = string.Template((ROOT / "templates" / "resume.html").read_text())
    files = [pathlib.Path(f) for f in sys.argv[1:]] or sorted(
        p for p in src.glob("*.md") if p.name.lower() != "readme.md"
    )
    if not files:
        sys.exit(f"error: no .md files in {src} (check RESUME_SRC)")
    out.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for f in files:
            if not f.is_file():
                sys.exit(f"error: {f} not found")
            try:
                build(f, pathlib.Path(tmp), out, chrome, template)
            except FileNotFoundError:
                sys.exit(f"error: chrome not found at {chrome} (check CHROME_BIN)")
            except subprocess.CalledProcessError as e:
                detail = e.stderr.decode(errors="replace").strip()[-300:]
                sys.exit(f"error: chrome failed on {f.name}: {detail}")


if __name__ == "__main__":
    main()
