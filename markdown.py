"""Minimal markdown -> HTML for resume files (headings, lists, bold/em/links)."""
import html
import re


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


if __name__ == "__main__":
    assert md_to_html("## **X**\n* a [b](c)") == \
        '<h2><strong>X</strong></h2>\n<ul>\n<li>a <a href="c">b</a></li>\n</ul>'
    print("ok")
