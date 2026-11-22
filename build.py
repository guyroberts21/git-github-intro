#!/usr/bin/env python3
"""Build the slide deck: slides.md + deck.css + template.html  ->  _site/index.html

Run:  python3 build.py      (no installs needed)
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent
DEFAULT_FOOT = "Git & GitHub · Introduction"

ICONS = {
    "Book": '<path d="M4 5v15a2 2 0 0 1 2-2h14V3H6a2 2 0 0 0-2 2z"/><path d="M8 7h8M8 11h8"/>',
    "Users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c0-3.6 2.9-6 6.5-6s6.5 2.4 6.5 6"/><circle cx="17.5" cy="9" r="2.5"/><path d="M17 14.2c2.8.2 4.5 2.1 4.5 4.8"/>',
    "Clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "Lightning": '<path d="M13 2L4 14h7l-1 8 9-12h-7l1-8z"/>',
    "Lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    "Verified": '<path d="M12 2l2.4 2 3.1-.2 1 3 2.6 1.8-1 3 1 3-2.6 1.8-1 3-3.1-.2L12 22l-2.4-2-3.1.2-1-3L2.9 15.4l1-3-1-3 2.6-1.8 1-3 3.1.2L12 2z"/><path d="M8.5 12l2.5 2.5L15.5 9.5"/>',
    "Globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/>',
    "Check": '<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.7 2.7L16 9.5"/>',
    "Activity": '<path d="M3 12h4l3-8 4 16 3-8h4"/>',
}

ARROW = ('<svg class="arrow" width="56" height="28" viewBox="0 0 56 28" style="flex:none" '
         'aria-hidden="true"><path d="M0 9h34V0l22 14-22 14V19H0z" fill="#7EE2A8"/></svg>')

COVER_SVG = '''<svg viewBox="0 0 792 192" width="792" height="192" aria-label="A branch splitting off the main line of work and merging back in" xmlns="http://www.w3.org/2000/svg" style="position:absolute;left:1000px;top:680px;width:792px;height:192px">
<path d="M0 150 H792" stroke="#7EE2A8" stroke-width="6" fill="none"/>
<path d="M200 150 C250 150 230 50 290 50 H500 C560 50 540 150 590 150" stroke="#F2B84B" stroke-width="6" fill="none"/>
<circle cx="60" cy="150" r="14" fill="#0F1419" stroke="#7EE2A8" stroke-width="6"/>
<circle cx="200" cy="150" r="14" fill="#0F1419" stroke="#7EE2A8" stroke-width="6"/>
<circle cx="340" cy="50" r="14" fill="#0F1419" stroke="#F2B84B" stroke-width="6"/>
<circle cx="450" cy="50" r="14" fill="#0F1419" stroke="#F2B84B" stroke-width="6"/>
<circle cx="590" cy="150" r="14" fill="#0F1419" stroke="#7EE2A8" stroke-width="6"/>
<circle cx="730" cy="150" r="14" fill="#0F1419" stroke="#7EE2A8" stroke-width="6"/>
</svg>'''

TH = "text-align:left;padding:18px 24px;color:#F4F5F2;font-weight:600"
TD = "padding:18px 24px"


class SlideError(Exception):
    pass


def esc(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def icon_svg(name):
    if name not in ICONS:
        raise SlideError(f"Unknown icon '{name}'. Choose from: {', '.join(ICONS)}")
    return ('<svg class="ic" width="56" height="56" viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true">' + ICONS[name] + '</svg>')


# ---------- parsing ----------

def parse(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    slides = []
    for block in re.split(r"^---\s*$", text, flags=re.M):
        block = block.strip()
        if not block:
            continue
        notes = ""
        m = re.search(r"^Notes:[ \t]*", block, flags=re.M)
        if m:
            notes = block[m.end():].strip()
            block = block[:m.start()].strip()
        head, _, body = block.partition("\n\n")
        meta = {}
        for line in head.splitlines():
            k, sep, v = line.partition(":")
            if not sep:
                raise SlideError(f"Header line without a colon: '{line}'")
            meta[k.strip().lower()] = v.strip()
        for req in ("id", "layout", "theme"):
            if req not in meta:
                raise SlideError(f"A slide is missing '{req}:' (header starts: {head[:60]!r})")
        slides.append({"meta": meta, "body": body.strip("\n"), "notes": notes})
    return slides


def sections(lines):
    """Split body lines on '### Heading'. Returns (intro_lines, [section dicts])."""
    intro, secs, cur = [], [], None
    for line in lines:
        if line.startswith("### "):
            cur = {"title": line[4:].strip(), "attrs": {}, "lines": []}
            secs.append(cur)
        elif cur is None:
            intro.append(line)
        else:
            cur["lines"].append(line)
    for s in secs:
        ls = s["lines"]
        while True:
            while ls and not ls[0].strip():
                ls.pop(0)
            m = re.match(r"^(icon|tag):\s*(.*)$", ls[0]) if ls else None
            if not m:
                break
            s["attrs"][m.group(1)] = m.group(2).strip()
            ls.pop(0)
        s["text"] = " ".join(x.strip() for x in ls if x.strip())
    return intro, secs


def split_callout(body):
    keep, call = [], []
    for line in body.splitlines():
        if line.startswith(">"):
            call.append(line[1:].strip())
        else:
            keep.append(line)
    return keep, " ".join(call)


def bullets(lines):
    return [re.sub(r"^\s*[-*]\s+", "", l) for l in lines if re.match(r"^\s*[-*]\s+", l)]


def numbered(lines):
    return [re.sub(r"^\s*\d+[.)]\s+", "", l) for l in lines if re.match(r"^\s*\d+[.)]\s+", l)]


def paragraph(lines):
    return " ".join(l.strip() for l in lines
                    if l.strip() and not re.match(r"^\s*([-*]|\d+[.)])\s+", l))


# ---------- rendering ----------

def card(s, num=None):
    out = ['<div class="card">']
    if num is not None:
        out.append(f'<p class="num">{num:02d}</p>')
    if "icon" in s["attrs"]:
        out.append(icon_svg(s["attrs"]["icon"]))
    if "tag" in s["attrs"]:
        out.append(f'<p class="tag">{esc(s["attrs"]["tag"])}</p>')
    out.append(f'<h3>{esc(s["title"])}</h3>')
    out.append(f'<p>{esc(s["text"])}</p>')
    out.append("</div>")
    return "\n".join(out)


def render(slide):
    m, layout = slide["meta"], slide["meta"]["layout"]
    sid, theme = m["id"], m["theme"]
    eyebrow = f'<p class="eyebrow">{esc(m["eyebrow"])}</p>' if m.get("eyebrow") else ""
    title = m.get("title", "")
    h2 = f"<h2>{esc(title)}</h2>"
    parts = []
    foot = m.get("foot", DEFAULT_FOOT)

    lines, callout = split_callout(slide["body"])

    if layout == "cover":
        foot = "none"
        lead = paragraph(lines)
        parts = [COVER_SVG, eyebrow,
                 f'<h1 style="width:1500px">{esc(title)}</h1>',
                 f'<p class="lead" style="width:1200px;margin-top:40px">{esc(lead)}</p>',
                 '<div class="spacer"></div>',
                 f'<p class="meta">{esc(m.get("meta", ""))}</p>']

    elif layout in ("cards", "numbered", "grid"):
        _, secs = sections(lines)
        cls = {"cards": "cards", "numbered": "cards four", "grid": "grid"}[layout]
        cards = [card(s, i + 1 if layout == "numbered" else None) for i, s in enumerate(secs)]
        parts = [eyebrow, h2, f'<div class="{cls}">', *cards, "</div>"]

    elif layout == "split":
        _, secs = sections(lines)
        by = {s["title"].strip().lower(): s for s in secs}
        if "files" not in by or "pains" not in by:
            raise SlideError(f"Slide '{sid}': split layout needs '### Files' and '### Pains'")
        files = [f'<p class="file">{esc(x)}</p>' for x in bullets(by["files"]["lines"])]
        pains = [f'<p class="pain">{esc(x)}</p>' for x in bullets(by["pains"]["lines"])]
        parts = [eyebrow, h2, '<div class="split">', '<div class="files">', *files, "</div>",
                 '<div class="pains">', *pains, "</div>", "</div>"]

    elif layout == "table":
        rows = []
        for l in lines:
            l = l.strip()
            if l.startswith("|") and not re.match(r"^\|[\s:|-]+\|?$", l):
                rows.append([c.strip() for c in l.strip("|").split("|")])
        if len(rows) < 2:
            raise SlideError(f"Slide '{sid}': table layout needs a markdown table")
        w = [int(x) for x in m.get("widths", "50/50").split("/")]
        hd = "".join(f'<th style="width:{w[i]}%;{TH}">{esc(c)}</th>' for i, c in enumerate(rows[0]))
        out = ['<table class="jt">', f'<tr class="hd">{hd}</tr>']
        for i, r in enumerate(rows[1:]):
            cls = ' class="band"' if i % 2 == 1 else ""
            tds = "".join(f'<td style="{TD}">{esc(c)}</td>' for c in r)
            out.append(f"<tr{cls}>{tds}</tr>")
        out.append("</table>")
        parts = [eyebrow, h2, *out]

    elif layout == "flow":
        steps = []
        for item in numbered(lines):
            t, _, d = item.partition("|")
            steps.append((t.strip(), d.strip()))
        out = ['<div class="flow">']
        for i, (t, d) in enumerate(steps):
            if i:
                out.append(ARROW)
            out.append(f'<div class="step"><p class="badge">{i + 1}</p>'
                       f'<p class="t">{esc(t)}</p><p class="d">{esc(d)}</p></div>')
        out.append("</div>")
        parts = [eyebrow, h2, *out]

    elif layout == "demo":
        items = [f"<li>{esc(x)}</li>" for x in numbered(lines)]
        note = paragraph(lines)
        parts = [eyebrow, f'<h1 style="width:1500px">{esc(title)}</h1>',
                 '<ol class="demo-list">', *items, "</ol>",
                 f'<p style="margin-top:40px;font-weight:600">{esc(note)}</p>']

    elif layout == "prompts":
        lead = paragraph(lines)
        cards = [f'<div class="card">\n<p style="font-weight:600;color:#1A2330">{esc(x)}</p>\n</div>'
                 for x in bullets(lines)]
        parts = [eyebrow, h2, f'<p class="lead" style="margin-bottom:48px">{esc(lead)}</p>',
                 '<div class="cards">', *cards, "</div>"]

    elif layout == "rows":
        _, secs = sections(lines)
        out = ['<div class="rows">']
        for i, s in enumerate(secs):
            out += ['<div class="row">', f'<p class="badge">{i + 1}</p>', '<div class="col">',
                    f'<h3>{esc(s["title"])}</h3>', f'<p>{esc(s["text"])}</p>', "</div>", "</div>"]
        out.append("</div>")
        parts = [eyebrow, h2, *out]

    else:
        raise SlideError(f"Slide '{sid}': unknown layout '{layout}'")

    if callout:
        parts.append(f'<p class="callout">{esc(callout)}</p>')
    if foot.lower() != "none":
        parts.append(f'<p class="foot">{esc(foot)}</p>')
    inner = "\n".join(p for p in parts if p)
    return f'<section id="{sid}" class="{theme}">\n{inner}\n</section>'


def main():
    try:
        slides = parse((ROOT / "slides.md").read_text(encoding="utf-8"))
        rendered = [render(s) for s in slides]
    except SlideError as e:
        sys.exit(f"Error in slides.md: {e}")
    tpl = (ROOT / "template.html").read_text(encoding="utf-8")
    css = (ROOT / "deck.css").read_text(encoding="utf-8")
    page = tpl.replace("%%CSS%%", css).replace("%%SLIDES%%", "\n".join(rendered))
    out = ROOT / "_site"
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(page, encoding="utf-8")
    print(f"Built {len(rendered)} slides -> _site/index.html")
    left = sorted({p for s in slides for p in re.findall(r"\[[^\]]+\]", s["body"] + " ".join(s["meta"].values()))})
    if left:
        print("Reminder - placeholders still to fill in: " + ", ".join(left))


if __name__ == "__main__":
    main()
