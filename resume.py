"""Resume JSON: schema validation + JSON -> Markdown.

Schema (all values are strings unless noted; inline markdown is allowed in any
text field — `**bold**`, `*em*`, `[label](url)`):

    {
      "name":     "Jane Doe",              # required
      "title":    "Backend Engineer",      # optional, rendered bold
      "location": "Santiago, CL",          # optional
      "contact":  [{"text": "...", "url": "..."}],   # optional, url optional
      "sections": [                        # required, non-empty
        {
          "title":   "Experience",         # required
          "text":    "intro paragraph",    # optional
          "bullets": ["..."],              # optional, list of strings
          "entries": [                     # optional
            {
              "title": "Senior Backend Engineer",  # required
              "org":   "Acme Corp",                # optional
              "dates": "2022 — present",           # optional
              "meta":  "(2022 — present) | Remote",# optional, right-aligned
              "text":  "...",                      # optional
              "bullets": ["..."]                   # optional
            }
          ]
        }
      ]
    }

`title · org · dates` become one heading line. Use `meta` instead when you want
the detail right-aligned on the heading (needs " | " in it, see markdown.py).
"""
import json
import pathlib

DOC_KEYS = {"name", "title", "location", "contact", "sections"}
CONTACT_KEYS = {"text", "url"}
SECTION_KEYS = {"title", "text", "bullets", "entries"}
ENTRY_KEYS = {"title", "org", "dates", "meta", "text", "bullets"}
LIST_KEYS = {"contact", "sections", "entries", "bullets"}


def _obj(value, where, allowed, required):
    if not isinstance(value, dict):
        raise ValueError(f"{where}: expected an object, got {type(value).__name__}")
    unknown = sorted(set(value) - allowed)
    if unknown:
        raise ValueError(f"{where}: unknown key(s) {unknown}; allowed {sorted(allowed)}")
    for key in required:
        if not isinstance(value.get(key), str) or not value[key].strip():
            raise ValueError(f"{where}.{key}: required, must be a non-empty string")
    for key, val in value.items():
        if key not in LIST_KEYS and not isinstance(val, str):
            raise ValueError(f"{where}.{key}: expected a string, got {type(val).__name__}")
    return value


def _list(value, where, required=False):
    if value is None:
        if required:
            raise ValueError(f"{where}: required, must be a non-empty list")
        return []
    if not isinstance(value, list) or (required and not value):
        raise ValueError(f"{where}: expected a{' non-empty' if required else ''} list")
    return value


def _strings(value, where):
    items = _list(value, where)
    for i, item in enumerate(items):
        if not isinstance(item, str):
            raise ValueError(f"{where}[{i}]: expected a string, got {type(item).__name__}")
    return items


def validate(doc):
    """Raise ValueError with a JSON path if `doc` does not match the schema."""
    _obj(doc, "resume", DOC_KEYS, ("name",))
    for i, contact in enumerate(_list(doc.get("contact"), "resume.contact")):
        _obj(contact, f"resume.contact[{i}]", CONTACT_KEYS, ("text",))
    for s, section in enumerate(_list(doc.get("sections"), "resume.sections", required=True)):
        at = f"resume.sections[{s}]"
        _obj(section, at, SECTION_KEYS, ("title",))
        _strings(section.get("bullets"), f"{at}.bullets")
        for e, entry in enumerate(_list(section.get("entries"), f"{at}.entries")):
            _obj(entry, f"{at}.entries[{e}]", ENTRY_KEYS, ("title",))
            _strings(entry.get("bullets"), f"{at}.entries[{e}].bullets")
    return doc


def load(path):
    """Read and validate a resume JSON file."""
    try:
        doc = json.loads(pathlib.Path(path).read_text())
    except json.JSONDecodeError as e:
        raise ValueError(f"{path}: invalid JSON: {e}") from None
    try:
        return validate(doc)
    except ValueError as e:
        raise ValueError(f"{path}: {e}") from None


def _link(contact):
    return f"[{contact['text']}]({contact['url']})" if contact.get("url") else contact["text"]


def _body(node, lines):
    """Shared tail of a section/entry: optional paragraph, then bullets."""
    if node.get("text"):
        lines += [node["text"], ""]
    if node.get("bullets"):
        lines += [f"* {b}" for b in node["bullets"]] + [""]


def to_markdown(doc):
    """Render a validated resume dict as the markdown the template expects."""
    validate(doc)
    lines = [f"# {doc['name']}", ""]
    headline = " — ".join(
        filter(None, (f"**{doc['title']}**" if doc.get("title") else "", doc.get("location")))
    )
    if headline:
        lines.append(headline)
    if doc.get("contact"):
        lines.append(" · ".join(_link(c) for c in doc["contact"]))
    if len(lines) > 2:  # blank line closing the header block, if there was one
        lines.append("")
    lines += ["---", ""]
    for section in doc["sections"]:
        lines += [f"## {section['title']}", ""]
        _body(section, lines)
        for entry in section.get("entries", []):
            lines.append(
                "### " + " · ".join(filter(None, (entry["title"], entry.get("org"), entry.get("dates"))))
            )
            if entry.get("meta"):
                lines.append(f"*{entry['meta']}*")
            lines.append("")
            _body(entry, lines)
    return "\n".join(lines).rstrip("\n") + "\n"


if __name__ == "__main__":
    sample = pathlib.Path(__file__).parent / "samples"
    # the shipped sample json must render byte-for-byte to the shipped sample md
    assert to_markdown(load(sample / "resume.json")) == (sample / "resume.md").read_text()

    assert to_markdown({"name": "X", "sections": [{"title": "S", "bullets": ["a"]}]}) == \
        "# X\n\n---\n\n## S\n\n* a\n"
    assert to_markdown({
        "name": "X",
        "title": "Dev",
        "location": "Chile",
        "contact": [{"text": "me", "url": "mailto:me"}, {"text": "plain"}],
        "sections": [{"title": "S", "entries": [{"title": "R", "meta": "(2024) | City"}]}],
    }) == "# X\n\n**Dev** — Chile\n[me](mailto:me) · plain\n\n---\n\n## S\n\n### R\n*(2024) | City*\n"

    for bad, expect in [
        ({}, "resume.name"),
        ({"name": "X"}, "resume.sections"),
        ({"name": "X", "sections": []}, "resume.sections"),
        ({"name": "X", "nope": 1, "sections": [{"title": "S"}]}, "unknown key(s) ['nope']"),
        ({"name": "X", "sections": [{"title": "S", "bullets": [1]}]}, "bullets[0]"),
        ({"name": "X", "sections": [{"title": "S", "entries": [{"org": "A"}]}]}, "entries[0].title"),
        ({"name": "X", "sections": [{"title": 1}]}, "sections[0].title"),
    ]:
        try:
            validate(bad)
        except ValueError as e:
            assert expect in str(e), f"{expect!r} not in {e}"
        else:
            raise AssertionError(f"expected ValueError for {bad}")
    print("ok")
