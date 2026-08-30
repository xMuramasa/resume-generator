#!/bin/sh
# Module self-checks + one end-to-end generation from samples/ into a temp dir.
# Usage: sh smoke.sh   (override the interpreter with PYTHON=..., Chrome with CHROME_BIN=...)
set -e
cd "$(dirname "$0")"
PY=${PYTHON:-python3}

$PY markdown.py
$PY resume.py

out=$(mktemp -d)
RESUME_SRC=samples RESUME_OUT="$out" \
CHROME_BIN="${CHROME_BIN:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}" \
    $PY main.py

for f in resume.md resume.html resume.pdf; do
    [ -s "$out/$f" ] || { echo "missing or empty: $out/$f" >&2; exit 1; }
done
diff samples/resume.md "$out/resume.md"
echo "smoke ok -> $out"
