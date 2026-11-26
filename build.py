#!/usr/bin/env python3
"""Build 'I Know, But I Can Do Nothing'.

Outputs (all from chapters/*.md, the single source of truth):
  docs/         GitHub Pages site (multi-page: index + one page per chapter)
  preview.html  Single-page preview (cover + contents + Chapter 1 in full)
  book.epub     Kindle EPUB, built with pandoc

Run:  python3 build.py
"""
import shutil
import subprocess
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
CHAPTERS_DIR = ROOT / "chapters"
DOCS_DIR = ROOT / "docs"
TITLE = "I Know, But I Can Do Nothing"
TAGLINE = "But you can make it better."
AUTHOR = "Venkata Sandeep Dhullipalla"


def parse_chapter(path):
    text = path.read_text()
    title = text.splitlines()[0].lstrip("# ").strip()
    forthcoming = "being written" in text
    return title, text, forthcoming


def md_to_html(text):
    # First line is the chapter title; it becomes the page heading, not body.
    body = "\n".join(text.splitlines()[1:])
    return markdown.markdown(body, extensions=["smarty"])


def page_shell(page_title, body_html, css_href="style.css"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page_title} | {TITLE}</title>
<link rel="stylesheet" href="{css_href}">
</head>
<body>
<div class="wrap">
{body_html}
</div>
</body>
</html>
"""


def build_site(chapters):
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir(parents=True)
    shutil.copy(ROOT / "assets" / "style.css", DOCS_DIR / "style.css")

    # Index: cover + about + contents.
    toc_items = []
    for i, (path, title, _text, forthcoming) in enumerate(chapters, 1):
        slug = path.stem
        status = "Coming soon" if forthcoming else "Read"
        cls = "soon" if forthcoming else ""
        toc_items.append(
            f'<li><span><span class="n">Chapter {i}</span> &nbsp;'
            f'<a href="{slug}.html">{title.split(": ", 1)[-1]}</a></span>'
            f'<span class="st {cls}">{status}</span></li>'
        )
    index_body = f"""
<div class="topnav"><a href="index.html">{TITLE}</a></div>
<div class="cover">
<div class="kicker">A book of small better days</div>
<h1>{TITLE}</h1>
<p class="tagline">{TAGLINE}</p>
<p class="author">by {AUTHOR}</p>
</div>
<hr class="rule">
<p>We all have those moments. You know the right thing, and you feel you can do nothing about it. Someone is pressured in a meeting. Someone helpless is treated badly. The room goes quiet, and you go quiet with it.</p>
<p>This book is about the minute after that moment. One minute of thought, one small decent move, and the day gets better, not just for one person, but for everyone in the room.</p>
<p>Each chapter is one everyday situation, told as a short story: the moment, the one-minute pause, the small better move, and why it worked.</p>
<hr class="rule">
<h2>Contents</h2>
<ul class="toc">
{''.join(toc_items)}
</ul>
<hr class="rule">
<p class="small">Read it here, or on a Kindle: the same chapters are published as an EPUB, free to send to any Kindle from the book's repository.</p>
"""
    (DOCS_DIR / "index.html").write_text(page_shell(TITLE, index_body))

    # One page per chapter, with previous / next navigation.
    for i, (path, title, text, forthcoming) in enumerate(chapters):
        slug = path.stem
        body = md_to_html(text)
        nav = []
        if i > 0:
            prev = chapters[i - 1]
            nav.append(
                f'<a href="{prev[0].stem}.html">&larr; {prev[1].split(": ", 1)[-1]}</a>'
            )
        else:
            nav.append("<span></span>")
        nav.append('<a href="index.html">Contents</a>')
        if i < len(chapters) - 1:
            nxt = chapters[i + 1]
            nav.append(
                f'<a href="{nxt[0].stem}.html">{nxt[1].split(": ", 1)[-1]} &rarr;</a>'
            )
        else:
            nav.append("<span></span>")
        chap_body = f"""
<div class="topnav"><a href="index.html">{TITLE}</a></div>
<h1 class="chapter">{title}</h1>
{body}
<div class="chapternav">{''.join(f'<span>{n}</span>' for n in nav)}</div>
"""
        (DOCS_DIR / f"{slug}.html").write_text(
            page_shell(title, chap_body)
        )
    return len(chapters)


def build_preview(chapters):
    css = (ROOT / "assets" / "style.css").read_text()
    written = [(p, t, x, f) for p, t, x, f in chapters if not f]
    body_parts = []
    for _path, title, text, _forth in written:
        body_parts.append(f'<h1 class="chapter">{title}</h1>\n{md_to_html(text)}')
    body_html = "\n<hr class=\"rule\">\n".join(body_parts)
    toc_items = []
    for i, (path, t, _tx, forthcoming) in enumerate(chapters, 1):
        status = "Coming soon" if forthcoming else "Chapter 1 is below"
        toc_items.append(
            f'<li><span><span class="n">Chapter {i}</span> &nbsp;'
            f'{t.split(": ", 1)[-1]}</span>'
            f'<span class="st">{status}</span></li>'
        )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE} | Preview</title>
<style>{css}</style>
</head>
<body>
<div class="wrap">
<div class="cover">
<div class="kicker">A book of small better days</div>
<h1>{TITLE}</h1>
<p class="tagline">{TAGLINE}</p>
<p class="author">by {AUTHOR}</p>
</div>
<hr class="rule">
<p>We all have those moments. You know the right thing, and you feel you can do nothing about it. This book is about the minute after that moment: one minute of thought, one small decent move, and the day gets better for everyone in the room.</p>
<hr class="rule">
<h2>Contents</h2>
<ul class="toc">
{''.join(toc_items)}
</ul>
<hr class="rule">
{body_html}
</div>
</body>
</html>
"""
    (ROOT / "preview.html").write_text(html)


def build_epub(chapters):
    files = [str(p) for p, _t, _x, _f in chapters]
    cmd = [
        "pandoc", "-o", str(ROOT / "book.epub"),
        "--metadata", f"title={TITLE}",
        "--metadata", f"author={AUTHOR}",
        "--metadata", "language=en",
        "--toc", "--toc-depth=1", "--split-level=1",
    ] + files
    subprocess.run(cmd, check=True)


def main():
    chapters = []
    for path in sorted(CHAPTERS_DIR.glob("*.md")):
        title, text, forthcoming = parse_chapter(path)
        chapters.append((path, title, text, forthcoming))
    n = build_site(chapters)
    build_preview(chapters)
    build_epub(chapters)
    print(f"Built {n} chapters.")
    print(f"Site:    {DOCS_DIR}/index.html")
    print(f"Preview: {ROOT}/preview.html")
    print(f"Kindle:  {ROOT}/book.epub")


if __name__ == "__main__":
    main()
