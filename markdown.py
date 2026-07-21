"""Minimal markdown -> HTML for resume files (headings, lists, bold/em/links)."""
import html
import re


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    return text


META_RE = re.compile(r"^\*(?!\*)(.+?)(?<!\*)\*$")


def md_to_html(md):
    lines = md.splitlines()
    out, in_list = [], False
    i, n = 0, len(lines)
    while i < n:
        line = lines[i].strip()
        if in_list and not line.startswith("* "):
            out.append("</ul>")
            in_list = False
        if not line or line == "---":
            i += 1
            continue
        if line.startswith("* "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(line[2:])}</li>")
        elif m := re.match(r"(#{1,3}) (.+)", line):
            level = len(m.group(1))
            nxt = lines[i + 1].strip() if i + 1 < n else ""
            meta = META_RE.match(nxt) if " | " in nxt else None
            if meta:
                out.append(
                    f'<h{level} class="entry"><span>{inline(m.group(2))}</span>'
                    f'<span class="meta">{inline(meta.group(1))}</span></h{level}>'
                )
                i += 2
                continue
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
        else:
            out.append(f"<p>{inline(line)}</p>")
        i += 1
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


if __name__ == "__main__":
    assert md_to_html("## **X**\n* a [b](c)") == \
        '<h2><strong>X</strong></h2>\n<ul>\n<li>a <a href="c">b</a></li>\n</ul>'
    assert md_to_html("### **Role** - Co\n*(2024 – Present) | City*\n* did stuff") == \
        '<h3 class="entry"><span><strong>Role</strong> - Co</span>'\
        '<span class="meta">(2024 – Present) | City</span></h3>\n'\
        '<ul>\n<li>did stuff</li>\n</ul>'
    print("ok")
