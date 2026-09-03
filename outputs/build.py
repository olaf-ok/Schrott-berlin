#!/usr/bin/env python3
"""Statischer Site-Generator für den Relaunch schrott-berlin.de.
Aufruf: python3 build.py  (aus outputs/). Ergebnis in outputs/site/."""
import json
import os
import shutil
import struct
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import templates  # noqa: E402

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
CONTENT = os.path.join(BASE, "content")
STATIC = os.path.join(BASE, "static")
ASSETS = os.path.join(ROOT, "reference", "design", "assets")
OUT = os.path.join(BASE, "site")

TODAY = date(2026, 9, 1).isoformat()  # Livegang + Umami-Einbau


# ------------------------------------------------------------ Bildmaße -----

def image_size(path):
    """Liest Breite/Höhe aus PNG- und WebP-Headern (stdlib only)."""
    with open(path, "rb") as f:
        head = f.read(64)
    if head[:8] == b"\x89PNG\r\n\x1a\n":
        w, h = struct.unpack(">II", head[16:24])
        return w, h
    if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        fmt = head[12:16]
        if fmt == b"VP8 ":
            w = struct.unpack("<H", head[26:28])[0] & 0x3FFF
            h = struct.unpack("<H", head[28:30])[0] & 0x3FFF
            return w, h
        if fmt == b"VP8L":
            bits = struct.unpack("<I", head[21:25])[0]
            return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
        if fmt == b"VP8X":
            w = int.from_bytes(head[24:27], "little") + 1
            h = int.from_bytes(head[27:30], "little") + 1
            return w, h
    return None, None


# --------------------------------------------------------------- Build -----

def main():
    site = json.load(open(os.path.join(BASE, "site.json"), encoding="utf-8"))
    dom = site["domain"]

    # Seiten laden
    pages = []
    for fn in sorted(os.listdir(CONTENT)):
        if fn.endswith(".json"):
            p = json.load(open(os.path.join(CONTENT, fn), encoding="utf-8"))
            p["_slug"] = fn[:-5]
            pages.append(p)
    paths = {p["path"] for p in pages}
    print(f"{len(pages)} Content-Seiten geladen")

    # Bildmaße
    img_dims = {}
    for fn in os.listdir(ASSETS):
        w, h = image_size(os.path.join(ASSETS, fn))
        if w:
            img_dims[fn] = (w, h)

    # Ausgabeverzeichnis frisch aufsetzen
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    # Statische Dateien
    shutil.copytree(os.path.join(STATIC, "css"), os.path.join(OUT, "css"))
    shutil.copytree(os.path.join(STATIC, "fonts"), os.path.join(OUT, "fonts"))
    shutil.copytree(ASSETS, os.path.join(OUT, "img"))
    imgsrc = os.path.join(STATIC, "img_src")
    if os.path.isdir(imgsrc):
        for fn in os.listdir(imgsrc):
            shutil.copy(os.path.join(imgsrc, fn), os.path.join(OUT, "img", fn))
    fav = os.path.join(ROOT, "reference", "design", "favicon.ico")
    if os.path.exists(fav):
        shutil.copy(fav, os.path.join(OUT, "favicon.ico"))
    php = os.path.join(BASE, "contact.php")
    if os.path.exists(php):
        shutil.copy(php, os.path.join(OUT, "contact.php"))
    hta = os.path.join(BASE, "htaccess.src")
    if os.path.exists(hta):
        shutil.copy(hta, os.path.join(OUT, ".htaccess"))

    # Seiten rendern
    for p in pages:
        html_out = templates.render_page(p, site, img_dims)
        rel = p["path"].strip("/")
        target_dir = os.path.join(OUT, rel) if rel else OUT
        os.makedirs(target_dir, exist_ok=True)
        with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_out)

    # 404
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(templates.render_404(site, img_dims))

    # sitemap.xml (ohne noindex-Seiten: /danke/)
    urls = sorted(p["path"] for p in pages if p["path"] != "/danke/")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        prio = "1.0" if u == "/" else "0.8"
        sm.append(f"  <url><loc>{dom}{u}</loc><lastmod>{TODAY}</lastmod><priority>{prio}</priority></url>")
    sm.append("</urlset>")
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm))

    # robots.txt — KI-Crawler explizit erlaubt (GEO)
    robots = f"""# robots.txt – schrott-berlin.de (Relaunch 2026)
# Klassische Suchmaschinen
User-agent: *
Allow: /
Disallow: /danke/

# KI-Crawler ausdrücklich erlaubt (Generative Engine Optimization)
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: CCBot
Allow: /

User-agent: Bytespider
Allow: /

User-agent: Applebot-Extended
Allow: /

Sitemap: {dom}/sitemap.xml
"""
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(robots)

    # llms.txt (GEO-Übersicht für KI-Systeme)
    c = site["company"]
    mat_links = "\n".join(
        f"- [{l}]({dom}{h})" for l, h in site["footer_cols"][0]["links"])
    dist_links = "\n".join(
        f"- [Schrottplatz {l}]({dom}{h})" for l, h in site["footer_cols"][1]["links"])
    svc_links = "\n".join(
        f"- [{l}]({dom}{h})" for l, h in site["footer_cols"][2]["links"])
    llms = f"""# Peglow Schrott und Metallhandel e.K. – Schrott- & Metall-Ankauf Berlin

> Schrotthandel und Metall-Ankauf in Berlin-Reinickendorf. Ankauf von Kupfer, Messing,
> Zink, Blei, Aluminium, Edelstahl, Eisen, Kabeln und Mischschrott zu tagesaktuellen
> Preisen. Abholung (gegen Aufpreis) in ganz Berlin und im gesamten Berliner Umland.
> Zertifizierter Entsorgungsfachbetrieb (§56 KrWG).

## Standort & Kontakt
- Firma: {c["legal_name"]} (Inhaber: {c["owner"]})
- Adresse: {c["street"]}, {c["zip"]} {c["city"]} (Reinickendorf)
- Telefon: {c["phone"]} | WhatsApp: {c["whatsapp"]} | E-Mail: {c["email"]}
- Öffnungszeiten: Montag–Freitag 8:00–17:00 Uhr, Wochenende geschlossen
- Website: {dom}/

## Leistungen
- Schrott-Ankauf und Altmetall-Ankauf mit Barzahlung bzw. Vergütung nach tagesaktuellen Preisen
- Abholung im gesamten Berliner Stadtgebiet und Berliner Umland (gegen Aufpreis)
- Selbstanlieferung am Schrottplatz Soltauer Straße 27-29 möglich
- Containerdienst (Absetzcontainer) für Metallschrott
- Ankaufspreise: tagesaktuell, abhängig von Börsenkursen (LME), Sorte, Reinheit und Menge – telefonische Auskunft unter {c["phone"]}

## Wichtige Seiten
- [Startseite]({dom}/)
- [Schrott-Ankauf]({dom}/schrott-ankauf/)
- [Aktuelle Schrottpreise]({dom}/schrottpreise/)
- [Container mieten]({dom}/container/)
- [Einzugsgebiete]({dom}/einzugsgebiete/)
- [Anfahrt]({dom}/anfahrt/)
- [Kontakt]({dom}/kontakt/)

## Material-Ankauf
{mat_links}

## Einzugsgebiet (Abholung)
{dist_links}

## Ankauf & Service
{svc_links}
"""
    open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8").write(llms)

    # Validierung: URL-Erhalt gegen Original-Sitemap
    orig = set()
    with open(os.path.join(ROOT, "reference", "crawl", "urls.txt")) as f:
        for line in f:
            u = line.strip().replace("https://schrott-berlin.de", "")
            if u:
                orig.add(u if u.endswith("/") else u + "/")
    missing = sorted(orig - paths)
    extra = sorted(paths - orig)
    print(f"Original-URLs: {len(orig)} | Neu gebaut: {len(paths)}")
    if missing:
        print("FEHLEND (kritisch!):", missing)
    if extra:
        print("Zusätzlich (ok wenn gewollt):", extra)
    print(f"Build fertig → {OUT}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
