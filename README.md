# resume

JSON resume → HTML + Markdown + PDF (PDF via headless Chrome). Stdlib only — no
venv, no dependencies.

**Demo:** [samples/resume.json](samples/resume.json) →
[samples/resume.md](samples/resume.md) · [samples/resume.pdf](samples/resume.pdf)

## Setup

```sh
cp .env.example .env   # then adjust the paths
```

| Variable     | What it is                          |
|--------------|-------------------------------------|
| `RESUME_SRC` | Directory with resume `.json` files |
| `RESUME_OUT` | Output directory                    |
| `CHROME_BIN` | Path to the Chrome binary           |

All three are required. Real environment variables take precedence over `.env`.

## Usage

```sh
python3 main.py              # builds every .json in RESUME_SRC
python3 main.py my-cv.json   # builds specific files
sh smoke.sh                  # self-checks + end-to-end run on samples/
```

Each input writes three files to `RESUME_OUT`: `<name>.md`, `<name>.html`,
`<name>.pdf`.

## Resume JSON

Every text field accepts inline markdown: `**bold**`, `*em*`, `[label](url)`.

| Field      | Type                    | Required | Notes                                       |
|------------|-------------------------|----------|---------------------------------------------|
| `name`     | string                  | yes      | the `# ` heading                            |
| `title`    | string                  | no       | rendered bold on the headline               |
| `location` | string                  | no       | joined to `title` with an em dash           |
| `contact`  | list of `{text, url?}`  | no       | one line, items joined with `·`             |
| `sections` | list of sections        | yes      | non-empty                                   |

A **section** is `{title, text?, bullets?, entries?}` — `title` required,
`bullets` a list of strings. An **entry** is `{title, org?, dates?, meta?,
text?, bullets?}`; `title · org · dates` become one `### ` heading. Use `meta`
instead (it must contain ` | `) when you want the detail right-aligned on the
heading line, e.g. `"meta": "(2024 — present) | Santiago"`.

Unknown keys are rejected, so typos fail loudly with a JSON path:

```
error: samples/resume.json: resume.sections[1].entries[0]: unknown key(s) ['dats']
```

Minimal example:

```json
{
  "name": "Jane Doe",
  "title": "Backend Engineer",
  "contact": [{ "text": "jane@example.com", "url": "mailto:jane@example.com" }],
  "sections": [
    {
      "title": "Experience",
      "entries": [
        {
          "title": "Senior Backend Engineer",
          "org": "Acme Corp",
          "dates": "2022 — present",
          "bullets": ["Ran the ingestion pipeline moving **40M events/day**"]
        }
      ]
    },
    { "title": "Skills", "bullets": ["**Languages:** Python, Go, SQL"] }
  ]
}
```

## Markdown input

Still supported for old files, but only when passed explicitly — the directory
scan only picks up `.json`:

```sh
python3 main.py old-cv.md
```

## Layout

```
main.py             entry point: config, .env loading, orchestration
resume.py           resume JSON: schema validation + json -> markdown
markdown.py         minimal md -> html (headings, lists, bold/em/links)
pdf.py              html -> pdf via headless Chrome
templates/resume.html   page skeleton + CSS ($body placeholder)
smoke.sh            self-checks + end-to-end run
```

Styling lives in `templates/resume.html`. The markdown parser is deliberately
minimal — if you need tables or nested lists, that's when to reach for a real
markdown library.
