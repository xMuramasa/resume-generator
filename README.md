# resume

Markdown resume → PDF via headless Chrome. Stdlib only — no venv, no dependencies.

## Setup

```sh
cp .env.example .env   # then adjust the paths
```

| Variable     | What it is                        |
|--------------|-----------------------------------|
| `RESUME_SRC` | Directory with resume `.md` files |
| `RESUME_OUT` | Output directory for PDFs         |
| `CHROME_BIN` | Path to the Chrome binary         |

All three are required. Real environment variables take precedence over `.env`.

## Usage

```sh
python3 main.py              # builds every .md in RESUME_SRC (except README.md)
python3 main.py my-cv.md     # builds specific files
```

PDFs land in `RESUME_OUT`; intermediate HTML goes to a temp dir and is cleaned up.

## Layout

```
main.py             entry point: config, .env loading, orchestration
markdown.py         minimal md -> html (headings, lists, bold/em/links)
pdf.py              html -> pdf via headless Chrome
templates/resume.html   page skeleton + CSS ($body placeholder)
```

Styling lives in `templates/resume.html`. The markdown parser is deliberately
minimal — if you need tables or nested lists, that's when to reach for a real
markdown library.
