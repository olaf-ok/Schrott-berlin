# Review-Checkliste Relaunch schrott-berlin.de (für Review-Agenten)

Prüfe die gebaute Site in `outputs/site/` gegen diese Liste. Melde jeden Mangel mit Datei/URL + konkretem Befund + Schweregrad (KRITISCH / WICHTIG / KOSMETISCH).

## A. URL-Erhalt (KRITISCH)
- [ ] Alle 64 Original-URLs aus `reference/crawl/urls.txt` existieren als `<pfad>/index.html`
- [ ] Die 5 Redirect-Ziele existieren: /altmetall-berlin/, /altmetall-ankauf/, /altmetall-ankauf-berlin/, /schrotthandel/, /metall-ankauf-berlin/
- [ ] Keine URL umbenannt, kein Trailing-Slash-Verlust

## B. SEO
- [ ] Jede Seite: genau 1 H1, einzigartiger Title (50–60 Z.), einzigartige Meta-Description (140–155 Z.)
- [ ] Ziel-Keyword der alten Seite (siehe `reference/inventar/inventar.json` → alter Title) in neuem Title + H1 erhalten
- [ ] Canonical = https://schrott-berlin.de + Pfad
- [ ] sitemap.xml vollständig + konsistent; robots.txt korrekt; /danke/ + 404 noindex
- [ ] Interne Verlinkung: keine toten Links, jede Seite von mind. 1 anderer Seite erreichbar (Footer zählt), sinnvolle kontextuelle Links im Fließtext
- [ ] Alle Bilder: alt-Text, width/height, lazy loading (außer Hero)
- [ ] Überschriften-Hierarchie ohne Sprünge (h1→h2→h3)

## C. GEO (Generative Engine Optimization)
- [ ] Jede Seite: JSON-LD @graph mit RecyclingCenter/LocalBusiness (NAP, Geo, Öffnungszeiten, Logo, sameAs), WebSite, WebPage, BreadcrumbList
- [ ] Material-/Landing-/Service-Seiten: Service-Schema
- [ ] FAQ-Seiten: FAQPage-Schema — nur wenn FAQ auch sichtbar im HTML
- [ ] JSON-LD ist valide (json.loads) und konsistent mit sichtbarem Inhalt (keine Fantasie-Daten)
- [ ] robots.txt erlaubt GPTBot, PerplexityBot, ClaudeBot, Google-Extended, CCBot
- [ ] llms.txt vorhanden, korrekt, Links funktionieren
- [ ] NAP auf jeder Seite identisch: Soltauer Straße 27-29, 13509 Berlin, 030 43206315 bzw. 030 - 43 20 63 15, info@schrott-berlin.de, Mo–Fr 8–17
- [ ] Intro-Absätze beantworten die Kernfrage der Seite direkt (KI-zitierbar)
- [ ] Preis-/Ablauf-Infos in Listen/Tabellen, nicht verstreut

## D. Content-Treue & Qualität
- [ ] Keine erfundenen Fakten: keine €-Preise, keine erfundenen Standorte/Jahre/Zahlen (gegen `reference/inventar/texte/<slug>.txt` prüfen — Stichproben!)
- [ ] Bezirksseiten behaupten KEINEN Standort im Bezirk (nur Abholung; Schrottplatz ist in Reinickendorf)
- [ ] Impressum/Datenschutz: Rechtstexte 1:1 (Datenschutz-Wortzahl nahe Original ~4200)
- [ ] Zertifikate exakt wie in context/fakten.md
- [ ] Deutsch fehlerfrei, Sie-Anrede, konsistenter Ton
- [ ] Ähnliche Seiten kannibalisieren nicht (kupfer vs. kupfer-ankauf-berlin etc. haben unterschiedliche Winkel)

## E. Technik
- [ ] Valides HTML (Stichproben: Startseite, 1 Material, 1 Bezirk, Kontakt)
- [ ] Kein externes CDN/Google Fonts — alles selbst gehostet
- [ ] Kein JavaScript erforderlich für Kernfunktionen (Nav funktioniert per CSS)
- [ ] Seiten < 200 KB HTML, Bilder als WebP mit Maßen
- [ ] Formular: action=/contact.php, Honeypot, Pflichtfelder, Datenschutz-Checkbox
- [ ] favicon.ico + robots + sitemap im Root

## F. Design/A11y
- [ ] Markenfarben (#E2007A, Schwarz), Roboto/Roboto Slab, Logo im Header
- [ ] Mobile-First: Nav als Burger < 1024px, Tabellen scrollen horizontal
- [ ] Kontraste ≥ 4.5:1 für Fließtext, Fokus-Stile sichtbar, Skip-Link
- [ ] Footer: alle Linkgruppen + NAP + Zertifikate + Social
