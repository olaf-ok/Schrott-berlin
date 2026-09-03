#!/usr/bin/env python3
"""QA-Prüfung der gebauten Site (outputs/site/): URL-Erhalt, Links, SEO, Schema, Bilder."""
import json
import os
import re
import sys
from html.parser import HTMLParser

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
SITE = os.path.join(BASE, "site")

errors = []
warnings = []


def err(page, msg):
    errors.append(f"[{page}] {msg}")


def warn(page, msg):
    warnings.append(f"[{page}] {msg}")


class Check(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._in_title = False
        self.meta_desc = None
        self.canonical = None
        self.h1 = []
        self._h1_buf = None
        self.links = []
        self.images = []       # (src, alt, w, h, loading)
        self.jsonld_raw = []
        self._in_jsonld = False
        self._buf = []
        self.lang = None
        self.robots = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            if (a.get("name") or "").lower() == "description":
                self.meta_desc = a.get("content", "")
            if (a.get("name") or "").lower() == "robots":
                self.robots = a.get("content", "")
        elif tag == "link" and (a.get("rel") or "").lower() == "canonical":
            self.canonical = a.get("href")
        elif tag == "h1":
            self._h1_buf = []
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "img":
            self.images.append((a.get("src", ""), a.get("alt"), a.get("width"),
                                a.get("height"), a.get("loading")))
        elif tag == "script" and (a.get("type") or "") == "application/ld+json":
            self._in_jsonld = True
            self._buf = []

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "h1" and self._h1_buf is not None:
            self.h1.append(" ".join("".join(self._h1_buf).split()))
            self._h1_buf = None
        elif tag == "script" and self._in_jsonld:
            self.jsonld_raw.append("".join(self._buf))
            self._in_jsonld = False

    def handle_data(self, d):
        if self._in_title:
            self.title += d
        if self._h1_buf is not None:
            self._h1_buf.append(d)
        if self._in_jsonld:
            self._buf.append(d)


def collect_pages():
    pages = {}
    for dirpath, _dirs, files in os.walk(SITE):
        for f in files:
            if f == "index.html":
                rel = os.path.relpath(dirpath, SITE)
                path = "/" if rel == "." else "/" + rel.replace(os.sep, "/") + "/"
                pages[path] = os.path.join(dirpath, f)
            elif f == "404.html" and dirpath == SITE:
                pages["/404.html"] = os.path.join(dirpath, f)
    return pages


def main():
    pages = collect_pages()

    # 1. URL-Erhalt gegen Original-Sitemap
    orig = set()
    with open(os.path.join(ROOT, "reference", "crawl", "urls.txt")) as f:
        for line in f:
            u = line.strip().replace("https://schrott-berlin.de", "")
            if u:
                orig.add(u if u.endswith("/") else u + "/")
    for u in sorted(orig):
        if u not in pages:
            err("URL-ERHALT", f"Original-URL fehlt in neuer Site: {u}")

    # Kritische Redirect-Ziele
    for u in ["/altmetall-berlin/", "/altmetall-ankauf/", "/altmetall-ankauf-berlin/",
              "/schrotthandel/", "/metall-ankauf-berlin/"]:
        if u not in pages:
            err("REDIRECT-ZIEL", f"KRITISCH: {u} fehlt!")

    titles = {}
    descs = {}

    for path, file in sorted(pages.items()):
        html_src = open(file, encoding="utf-8").read()
        c = Check()
        c.feed(html_src)

        if c.lang != "de":
            err(path, "html[lang] fehlt oder != de")

        # Title / Description
        t = c.title.strip()
        if not t:
            err(path, "Kein <title>")
        elif path not in ("/404.html", "/danke/", "/impressum/", "/datenschutz/"):
            if not 35 <= len(t) <= 65:
                warn(path, f"Title-Länge {len(t)}: {t!r}")
        if t in titles:
            err(path, f"Doppelter Title (auch auf {titles[t]}): {t!r}")
        titles[t] = path
        d = (c.meta_desc or "").strip()
        if not d:
            err(path, "Keine Meta-Description")
        elif path not in ("/404.html", "/danke/"):
            if not 80 <= len(d) <= 165:
                warn(path, f"Description-Länge {len(d)}")
            if d in descs:
                err(path, f"Doppelte Description (auch auf {descs[d]})")
            descs[d] = path

        # H1
        if len(c.h1) != 1:
            err(path, f"H1-Anzahl = {len(c.h1)} (muss 1 sein)")

        # Canonical
        expected = "https://schrott-berlin.de" + ("" if path == "/404.html" else path)
        if path != "/404.html" and c.canonical != expected:
            err(path, f"Canonical falsch: {c.canonical!r} != {expected!r}")

        # noindex-Pflicht
        if path in ("/danke/", "/404.html") and "noindex" not in (c.robots or ""):
            err(path, "noindex fehlt")

        # Links intern prüfen
        for href in c.links:
            if href.startswith(("http://", "https://", "mailto:", "tel:", "#")):
                if href.startswith("https://schrott-berlin.de"):
                    href = href.replace("https://schrott-berlin.de", "") or "/"
                else:
                    continue
            href = href.split("#")[0].split("?")[0]
            if not href:
                continue
            if href.endswith("/"):
                if href not in pages:
                    err(path, f"Toter interner Link: {href}")
            else:
                target = os.path.join(SITE, href.lstrip("/"))
                if not os.path.exists(target):
                    err(path, f"Tote Datei-Referenz: {href}")

        # Bilder
        for src, alt, w, h, loading in c.images:
            if alt is None:
                err(path, f"img ohne alt-Attribut: {src}")
            if src.startswith("/"):
                target = os.path.join(SITE, src.lstrip("/"))
                if not os.path.exists(target):
                    err(path, f"Bild fehlt: {src}")
            if not w or not h:
                warn(path, f"img ohne width/height: {src}")

        # JSON-LD
        if path not in ("/404.html",):
            if not c.jsonld_raw:
                err(path, "Kein JSON-LD")
            for raw in c.jsonld_raw:
                try:
                    data = json.loads(raw)
                    graph = data.get("@graph", [])
                    types = {t for node in graph for t in
                             (node["@type"] if isinstance(node["@type"], list) else [node["@type"]])}
                    if "LocalBusiness" not in types:
                        err(path, "LocalBusiness fehlt im JSON-LD")
                    if path != "/404.html" and "WebPage" not in types:
                        err(path, "WebPage fehlt im JSON-LD")
                    # FAQ-Konsistenz: FAQPage nur wenn FAQ sichtbar
                    if "FAQPage" in types and "<summary>" not in html_src:
                        err(path, "FAQPage-Schema ohne sichtbares FAQ")
                except json.JSONDecodeError as e:
                    err(path, f"JSON-LD parse error: {e}")

        # NAP-Konsistenz
        if path != "/404.html":
            if "Soltauer Straße 27-29" not in html_src:
                err(path, "NAP: Adresse fehlt")
            if "43 20 63 15" not in html_src and "43206315" not in html_src:
                err(path, "NAP: Telefonnummer fehlt")

    # Root-Dateien
    for f in ["sitemap.xml", "robots.txt", "llms.txt", "404.html", "favicon.ico"]:
        if not os.path.exists(os.path.join(SITE, f)):
            err("ROOT", f"{f} fehlt")

    # Sitemap-Konsistenz
    sm = open(os.path.join(SITE, "sitemap.xml")).read()
    sm_urls = set(re.findall(r"<loc>https://schrott-berlin\.de(/[^<]*)</loc>", sm))
    for u in sm_urls:
        if u not in pages:
            err("SITEMAP", f"Sitemap-URL ohne Seite: {u}")
    for u in pages:
        if u not in sm_urls and u not in ("/404.html", "/danke/"):
            err("SITEMAP", f"Seite fehlt in Sitemap: {u}")

    # robots.txt: KI-Crawler
    rb = open(os.path.join(SITE, "robots.txt")).read()
    for bot in ["GPTBot", "PerplexityBot", "ClaudeBot", "Google-Extended", "CCBot"]:
        if bot not in rb:
            err("ROBOTS", f"KI-Crawler fehlt: {bot}")

    print(f"Seiten geprüft: {len(pages)}")
    print(f"FEHLER: {len(errors)}")
    for e in errors:
        print("  ✗", e)
    print(f"WARNUNGEN: {len(warnings)}")
    for w in warnings:
        print("  ⚠", w)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
