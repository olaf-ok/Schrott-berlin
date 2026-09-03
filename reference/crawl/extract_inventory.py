#!/usr/bin/env python3
"""Extrahiert SEO-/Content-Inventar aus den gecrawlten HTML-Seiten (nur stdlib)."""
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

PAGES_DIR = "reference/crawl/pages"
OUT_DIR = "reference/inventar"
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(f"{OUT_DIR}/texte", exist_ok=True)

BLOCK_TAGS = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "td", "th", "div",
              "section", "article", "br", "tr", "ul", "ol", "table", "footer", "header"}
SKIP_TAGS = {"script", "style", "noscript", "template", "svg"}


class Extractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.meta_description = ""
        self.meta_robots = ""
        self.canonical = ""
        self.og = {}
        self.headings = []          # (tag, text)
        self.images = []            # (src, alt)
        self.links = []             # (href, text)
        self.forms = []             # list of dicts
        self.jsonld = []
        self.text_parts = []
        self._stack = []
        self._in_title = False
        self._heading_buf = None    # (tag, [parts])
        self._link_buf = None       # (href, [parts])
        self._form = None
        self._in_jsonld = False
        self._jsonld_buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self._stack.append(tag)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            name = (a.get("name") or "").lower()
            prop = (a.get("property") or "").lower()
            if name == "description":
                self.meta_description = a.get("content", "")
            elif name == "robots":
                self.meta_robots = a.get("content", "")
            elif prop.startswith("og:"):
                self.og[prop] = a.get("content", "")
        elif tag == "link" and (a.get("rel") or "").lower() == "canonical":
            self.canonical = a.get("href", "")
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._heading_buf = (tag, [])
        elif tag == "img":
            self.images.append((a.get("src") or a.get("data-src") or "", a.get("alt", "")))
        elif tag == "a" and a.get("href"):
            self._link_buf = (a["href"], [])
        elif tag == "form":
            self._form = {"action": a.get("action", ""), "method": a.get("method", "get"), "fields": []}
        elif tag in ("input", "textarea", "select") and self._form is not None:
            self._form["fields"].append({
                "tag": tag, "type": a.get("type", ""), "name": a.get("name", ""),
                "placeholder": a.get("placeholder", ""), "required": "required" in a})
        elif tag == "script" and (a.get("type") or "").lower() == "application/ld+json":
            self._in_jsonld = True
            self._jsonld_buf = []
        if tag in BLOCK_TAGS:
            self.text_parts.append("\n")

    def handle_endtag(self, tag):
        if self._stack and self._stack[-1] == tag:
            self._stack.pop()
        if tag == "title":
            self._in_title = False
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self._heading_buf:
            text = " ".join("".join(self._heading_buf[1]).split())
            if text:
                self.headings.append((self._heading_buf[0], text))
            self._heading_buf = None
        elif tag == "a" and self._link_buf:
            text = " ".join("".join(self._link_buf[1]).split())
            self.links.append((self._link_buf[0], text))
            self._link_buf = None
        elif tag == "form" and self._form is not None:
            self.forms.append(self._form)
            self._form = None
        elif tag == "script" and self._in_jsonld:
            raw = "".join(self._jsonld_buf).strip()
            if raw:
                try:
                    self.jsonld.append(json.loads(raw))
                except json.JSONDecodeError:
                    self.jsonld.append({"_parse_error": raw[:500]})
            self._in_jsonld = False

    def handle_data(self, data):
        if self._in_jsonld:
            self._jsonld_buf.append(data)
            return
        if any(t in SKIP_TAGS for t in self._stack):
            return
        if self._in_title:
            self.title += data
        if self._heading_buf is not None:
            self._heading_buf[1].append(data)
        if self._link_buf is not None:
            self._link_buf[1].append(data)
        self.text_parts.append(data)


def clean_text(parts):
    text = "".join(parts)
    lines = [" ".join(l.split()) for l in text.split("\n")]
    out = []
    for l in lines:
        if l and (not out or out[-1] != l):
            out.append(l)
    return "\n".join(out)


inventory = {}
for fname in sorted(os.listdir(PAGES_DIR)):
    if not fname.endswith(".html"):
        continue
    slug = fname[:-5]
    with open(os.path.join(PAGES_DIR, fname), encoding="utf-8", errors="replace") as f:
        raw = f.read()
    ex = Extractor()
    try:
        ex.feed(raw)
    except Exception as e:
        print(f"WARN {fname}: {e}", file=sys.stderr)
    url_path = "/" if slug == "_home" else "/" + slug.replace("_", "/") + "/"
    internal = sorted({re.sub(r"#.*$", "", h) for h, t in ex.links
                       if h.startswith("https://schrott-berlin.de") or (h.startswith("/") and not h.startswith("//"))})
    text = clean_text(ex.text_parts)
    with open(f"{OUT_DIR}/texte/{slug}.txt", "w", encoding="utf-8") as f:
        f.write(text)
    inventory[url_path] = {
        "slug": slug,
        "title": " ".join(ex.title.split()),
        "title_len": len(" ".join(ex.title.split())),
        "meta_description": ex.meta_description,
        "meta_desc_len": len(ex.meta_description),
        "meta_robots": ex.meta_robots,
        "canonical": ex.canonical,
        "og": ex.og,
        "headings": [{"tag": t, "text": x} for t, x in ex.headings],
        "h1_count": sum(1 for t, _ in ex.headings if t == "h1"),
        "images": [{"src": s, "alt": a} for s, a in ex.images if s and not s.startswith("data:")],
        "internal_links": internal,
        "forms": ex.forms,
        "jsonld_types": [d.get("@type", d.get("@graph", [{}])[0].get("@type", "?") if isinstance(d.get("@graph"), list) else "?") if isinstance(d, dict) else "?" for d in ex.jsonld],
        "jsonld": ex.jsonld,
        "word_count": len(text.split()),
    }

with open(f"{OUT_DIR}/inventar.json", "w", encoding="utf-8") as f:
    json.dump(inventory, f, ensure_ascii=False, indent=1)

# Kompakte Übersicht als Markdown
with open(f"{OUT_DIR}/uebersicht.md", "w", encoding="utf-8") as f:
    f.write("# URL-Inventar schrott-berlin.de (Crawl 2026-08-12)\n\n")
    f.write("| URL | Title (Len) | Desc-Len | H1 | Wörter | Bilder | Schema |\n|---|---|---|---|---|---|---|\n")
    for path, d in sorted(inventory.items()):
        h1 = next((h["text"] for h in d["headings"] if h["tag"] == "h1"), "—")
        schema = ",".join(str(t) for t in d["jsonld_types"]) or "—"
        f.write(f"| {path} | {d['title'][:60]} ({d['title_len']}) | {d['meta_desc_len']} | {h1[:50]} | {d['word_count']} | {len(d['images'])} | {schema[:40]} |\n")

print(f"OK: {len(inventory)} Seiten inventarisiert")
