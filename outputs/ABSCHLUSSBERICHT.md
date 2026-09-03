# Abschlussbericht: Relaunch schrott-berlin.de

**Kunde:** Peglow Schrott und Metallhandel e.K., Soltauer Straße 27-29, 13509 Berlin-Reinickendorf
**Datum:** 12.08.2026 · **Status:** Fertig zur Abnahme — **nicht deployed**, Live-Seite unverändert

---

## 1. Ergebnis in Kürze

- **Alle 64 Original-URLs 1:1 erhalten** (inkl. der 5 kritischen Redirect-Ziele) — kein einziger Pfad geändert
- Kompletter Neuaufbau als **statische HTML-Site** (kein WordPress, kein JavaScript-Zwang, kein Cookie-Banner nötig)
- **SEO:** Alle Ziel-Keywords in Titles/H1s erhalten und geschärft, einzigartige Metas, saubere interne Verlinkung
- **GEO:** Vollständiges Schema.org auf jeder Seite (RecyclingCenter/LocalBusiness, Service, FAQPage, BreadcrumbList), llms.txt, KI-Crawler-freundliche robots.txt, FAQ-Blöcke auf allen relevanten Seiten, identische NAP auf jeder Seite
- **Performance:** Startseiten-HTML von 139 KB → 21 KB; ~7 Requests statt 25+; Median-Erstaufruf ~200 KB (nach Font-Dedupe)
- **3 Schwerpunkt-Seiten ausgebaut:** /edelstahl/, /aluminium/, /mischschrott/ (existierten bereits als dünne Seiten → auf 850–950 Wörter Ratgeber-Qualität ausgebaut)
- 3 Self-Review-Runden durchlaufen, alle Befunde behoben, automatisierte QA: **0 Fehler, 0 Warnungen**

## 2. Lokal ansehen

```bash
cd /Users/olafkranz/Documents/Code/Schrott-Berlin-2026/outputs/site
python3 -m http.server 8080
# → http://localhost:8080
```

Neu bauen nach Änderungen: `cd outputs && python3 build.py` · QA: `python3 qa_check.py`

## 3. Stack-Entscheidung + Begründung

**Gewählt: Eigener statischer Generator (Python-Stdlib, ~600 Zeilen) → reines HTML/CSS.**

| Kriterium | Statisch (gewählt) | WordPress/Elementor (alt) |
|---|---|---|
| Core Web Vitals | Optimal (kein JS, 1 CSS, selbstgehostete Fonts) | 25+ Assets, Plugin-Overhead |
| Sicherheit/Wartung | Keine Updates, keine Angriffsfläche | Ständige Plugin-/Core-Updates |
| Hosting | Jeder Mittwald-Webspace (statisch + 1 PHP-Datei) | PHP+MySQL nötig |
| URL-Erhaltung | Trivial exakt (`pfad/index.html`) | — |
| Cookie-Banner | **Nicht nötig** (keine externen Dienste) | Nötig (Google Fonts/Maps etc.) |
| Redaktion | Content = einfache JSON-Dateien je Seite | WYSIWYG |

Bewusst **kein** Framework (Astro/Next/Eleventy): 64 inhaltsgetriebene Seiten ohne Interaktivität brauchen keine npm-Abhängigkeitskette. Der Generator ist in 10 Minuten verstanden (`build.py`, `templates.py`, `site.json`, `content/*.json`). Einzige dynamische Komponente: `contact.php` für das Kontaktformular (Mittwald unterstützt PHP).

**Trade-off (transparent):** Inhaltspflege erfordert JSON-Editieren + Build statt WYSIWYG. Für eine Seite mit seltenen Textänderungen angemessen; ein Git-basierter Workflow oder späterer Headless-CMS-Anschluss ist möglich.

## 4. URL-Mapping (alt → neu)

**Alle 64 URLs identisch übernommen — kein Mapping nötig, keine URL entfällt.**
Vollständige Liste: `reference/crawl/urls.txt` = Inhalt der neuen `sitemap.xml` (minus `/danke/`, s. u.).

Die 5 kritischen Redirect-Ziel-URLs (extern per 301 angebunden) — alle vorhanden und geprüft:
`/altmetall-berlin/` · `/altmetall-ankauf/` · `/altmetall-ankauf-berlin/` · `/schrotthandel/` · `/metall-ankauf-berlin/`

Neu hinzugekommen (kein Ersatz, nur Ergänzung): `/404.html` (gab es nicht). `/danke/` ist jetzt `noindex` und aus der Sitemap genommen (Formular-Dankeseite gehört nicht in den Index — Verbesserung).

## 5. SEO-Checkliste

| Punkt | Status |
|---|---|
| Title-Tags: einzigartig, 50–60 Z., Kern-Keyword der Altseite erhalten | ✅ skriptgeprüft auf allen 64 Seiten |
| Meta-Descriptions: einzigartig, 140–155 Z., mit CTA/Telefonnummer | ✅ |
| Genau eine H1 je Seite, sprechend statt Ein-Wort (alt: „Kupfer" → neu: „Kupfer-Ankauf in Berlin: Millberry, Rohre & mehr") | ✅ |
| Überschriften-Hierarchie ohne Sprünge | ✅ skriptgeprüft |
| Canonical-Tags auf jeder Seite | ✅ |
| sitemap.xml (konsistent zur Site) + robots.txt | ✅ |
| Interne Verlinkung: 0 tote Links, Footer-Silostruktur + 3–10 Kontextlinks je Seite | ✅ skriptgeprüft |
| Bild-Alt-Texte, width/height, lazy loading (Hero: eager + fetchpriority=high + preload) | ✅ |
| Ladezeit/CWV: 1 CSS (16 KB), 2 Variable Fonts (72 KB), kein JS, WebP-Bilder | ✅ |
| Kannibalisierungs-Check ähnlicher Seiten (kupfer vs. kupfer-ankauf-berlin, Altmetall-Trio …) | ✅ Shingle-Analyse: nur NAP-Boilerplate überlappt |
| Content-Lücken ergänzt | ✅ s. Abschnitt 7 |
| Top-Keywords (schrott ankauf berlin, berlin schrotthandel, schrottplatz berlin, altmetall verkaufen, messing ankauf berlin, schrottpreise, kupfer preis pro kg) | ✅ jeweils dedizierte Seite, Keyword in Title+H1+Intro |

## 6. GEO-Checkliste (Generative Engine Optimization)

| Punkt | Status |
|---|---|
| LocalBusiness-Schema (Typ `RecyclingCenter`) auf **jeder** Seite: NAP, Geo-Koordinaten, Öffnungszeiten, Logo, sameAs (FB/IG), Zertifikats-Infos | ✅ (alte Seite hatte nur ein generisches `WebSite`-Schema!) |
| Service-Schema auf allen Material-/Landing-/Service-Seiten | ✅ |
| FAQPage-Schema, konsistent mit sichtbarem FAQ (3–5 Fragen je Seite) | ✅ 60 Seiten mit FAQ |
| BreadcrumbList auf allen Unterseiten | ✅ |
| KI-zitierbare Intro-Absätze (Direktantwort, Entität + Ort + Leistung in einem Absatz) | ✅ auf jeder Seite |
| Preis-/Ablauf-Infos in Tabellen/Listen (Materialtabellen, 3-/4-Schritte-Abläufe) | ✅ |
| robots.txt erlaubt explizit: GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, Perplexity-User, ClaudeBot, Claude-User, anthropic-ai, Google-Extended, CCBot, Bytespider, Applebot-Extended | ✅ |
| llms.txt im Root (Angebot, Standort, Einzugsgebiet, Preislogik, alle wichtigen Unterseiten) | ✅ |
| NAP-Konsistenz: identische Adresse/Telefon/Öffnungszeiten auf jeder Seite (Header, NAP-Box, Footer, Schema) | ✅ skriptgeprüft |

## 7. Neue/ausgebaute Seiten (Content-Lücken)

Wichtige Erkenntnis aus dem Crawl: `/edelstahl/`, `/aluminium/`, `/mischschrott/` **existierten bereits** als dünne Seiten (~450–510 Wörter). **Entscheidung:** ausbauen statt neue URLs anlegen — vermeidet Kannibalisierung und nutzt vorhandene URL-Historie.

| Seite | Ziel-Keyword (SV/Monat) | Alt | Neu |
|---|---|---|---|
| /edelstahl/ | edelstahl ankauf (~2.900) | 456 Wörter | 938 Wörter: V2A/V4A, Magnet-Test, Sorten-Tabelle, 5 FAQ |
| /aluminium/ | aluminium ankauf (~2.400) | 508 Wörter | 912 Wörter: Sorten, Reinheitsgrade, Abgrenzung Alu-Guss, 5 FAQ |
| /mischschrott/ | mischschrott (~1.900) | 438 Wörter | 869 Wörter: 10-%-Regel, rein/nicht-rein-Tabelle, Container, 5 FAQ |

## 8. Getroffene Annahmen (bitte prüfen!)

1. **Geo-Koordinaten** 52.5877 / 13.3126 für Soltauer Str. 27-29 sind geschätzt — vor Livegang mit Google Maps exakt verifizieren (Schema + ggf. Karte).
2. **„Kostenlose Abholung" entfernt:** Die Original-Site verspricht das nirgends; alle vom Text-Team erzeugten „kostenlos"-Formulierungen wurden auf neutrale Formulierungen zurückgebaut. Falls die Abholung tatsächlich kostenlos ist: gern wieder einbauen (starkes Verkaufsargument!).
3. **Impressum:** Gestaltungs-Credit „CTI New Media GmbH" (alte Agentur) nicht übernommen; „© 2019" → „© 2026" aktualisiert. Bitte bestätigen.
4. **E-Mail-Schreibweise** vereinheitlicht auf `info@schrott-berlin.de` (Original teils „schrott-Berlin.de").
5. **Sachfehler im Original korrigiert:** Zink-Seite nannte fälschlich „Messing" als Rostschutz; Blei-Seite nannte „Kupfer" als gesundheitsschädlich (gemeint war Blei). Beides sinnwahrend berichtigt.
6. **Elektroschrott** wird nirgends als Ankaufsleistung behauptet (war im Alt-Text nur als Kategorie erwähnt, nicht in fakten belegt).
7. Nav-Reihenfolge leicht geändert (Schrottpreise vor Container/Einzugsgebiete) — folgt Nutzer-Priorität.

## 9. Offene Punkte vor Livegang (dein Part / Freigabe nötig)

1. **Datenschutzerklärung juristisch anpassen:** Text wurde 1:1 übernommen, beschreibt aber die ALTE Technik (Google Fonts/Analytics/Maps/Tag Manager, Facebook-Plugins, Cookie-Tool) — die neue Site lädt **nichts davon**. Außerdem enthält das Original einen Copy-Paste-Fehler („Akkord Film Produktion GmbH" im Maps-Abschnitt). → Datenschutz-Generator/Anwalt.
2. **contact.php testen:** `mail()`-Versand auf dem Mittwald-Tarif prüfen (Empfänger: info@schrott-berlin.de, Honeypot + Pflichtfelder eingebaut); ggf. auf SMTP umstellen.
3. **Google Maps:** Alte Kontakt-/Anfahrtsseite hatte ein Maps-Embed; neue Site verlinkt stattdessen extern (kein Consent-Problem). Falls Embed gewünscht → Consent-Lösung nötig.
4. **Kundenbewertungen:** Sektion „Das sagen unsere Kunden" (alte Site, vermutlich Google-Reviews-Plugin) wurde nicht übernommen — Quelle unklar/extern. Optional nachrüsten (z. B. statisch gepflegte Zitate + Review-Schema).
5. **Ostern-/Aktionsbild** (`ostern-schrott-berlin.jpg`, April 2026) nicht übernommen — saisonal veraltet.
6. Beim Livegang: bestehende 301-Weiterleitungen der Zusatz-Domains unverändert lassen (Ziel-URLs existieren alle weiter); alte WordPress-Instanz erst nach Verifikation abschalten; Search Console: neue sitemap.xml einreichen.

## 10. Die 3 Review-Runden

| Runde | Fokus | Befunde → Maßnahmen |
|---|---|---|
| 1 | Visuell/Technik (Screenshots Desktop+Mobil, Overflow-Diagnose) | Desktop-Nav brach 2-zeilig um → Breakpoint/Kompaktierung; 10 generische Hero-Bilder → thematisch passende Motive; Mobil-„Overflow" als Headless-Chrome-Artefakt entlarvt (DOM-Messung: sauber) |
| 2 | Content-Treue/SEO (Shingle-Analyse, Keyword-Erhalt, Faktencheck) | **11 Dateien + llms.txt mit unbelegtem „kostenlos"-Versprechen** → neutralisiert; 2 Meta-Descriptions angepasst; Rechtstexte wortgetreu bestätigt; keine €-Preise; Kannibalisierung: nur NAP-Boilerplate |
| 3 | Finale Verifikation (Alt/Neu-Vergleich, Performance, Schema) | Font-Dedupe (3×37 KB identische Variable Fonts → 1 Datei, −110 KB); JSON-LD-Stichprobe valide; Alt/Neu-Screenshots je Seitentyp erstellt; QA final: 0/0 |

Automatisierte Checks (`qa_check.py`, bei jedem Build): URL-Erhalt (64/64), Redirect-Ziele, Title/Desc-Einzigartigkeit+Länge, H1-Anzahl, Canonicals, tote Links (0), Bilder (alt/width/height), JSON-LD-Validität + FAQ-Konsistenz, NAP auf jeder Seite, Sitemap-Konsistenz, KI-Crawler in robots.txt.

## 11. Projektstruktur

```
outputs/
├── site/                  ← FERTIGE SITE (das Deployment-Artefakt)
├── content/*.json         ← Inhalte je Seite (64 Dateien)
├── build.py               ← Generator (erzeugt site/ komplett neu)
├── templates.py           ← HTML-Templates + Schema.org
├── site.json              ← Globale Daten (NAP, Nav, Footer)
├── static/css|fonts/      ← Design-Assets
├── contact.php            ← Formular-Handler (Quelle)
├── qa_check.py            ← Automatisierte QA
├── content-spec.md        ← Doku Content-Format
├── review-checkliste.md   ← Review-Kriterien
├── screenshots/           ← alt_*.png / neu_*.png Vergleiche
└── ABSCHLUSSBERICHT.md    ← dieses Dokument

reference/                 ← Komplette Kopie & Inventar der Alt-Site (Crawl 12.08.2026)
context/                   ← Auftrag, Fakten/NAP, Projektstand
```

## 12. Anmerkung zur Arbeitsweise

Geplant waren Review-Runden per Subagent; nach dem Spend-Limit-Abbruch des Bezirksseiten-Agenten (5 Seiten von mir direkt nachgeschrieben) habe ich die 3 Review-Runden selbst mit Skript-Unterstützung durchgeführt — inhaltlich identisches Prüfprogramm laut `review-checkliste.md`.

---

## Nachtrag 12.08.2026: Redesign „Soft-Industrial" (Design-Handoff)

Nach Kundenfeedback („zu dunkel, emotionslos") wurde das Design gemäß Handoff `reference/design_handoff_peglow_startseite/` komplett überarbeitet:

- **Header:** weiß, schlanke Nav (Ankauf · Schrottpreise · Container · Bezirke · Kontakt) + Telefon-CTA-Button; Topbar entfernt
- **Hero:** Foto-Karte (Radius 12) mit hellem, sattem Bild, Textschutz-Verlaufspanel links (58 %), rotierte Zertifikats-Plakette „§56 KrWG" (CSS-Animation, reduced-motion-sicher)
- **Startseite neu komponiert:** Stats-Chips (20+ Jahre / 3–30 m³ / Mo–Fr 8–17) → Material-Grid mit 9 Foto-Karten (alle Links erhalten) → Warnstreifen-Trenner (schwarz/magenta) → Container-Feature (2-spaltig, LKW-Foto, Häkchenliste) → Textsektionen → FAQ+NAP zweispaltig
- **NAP-Karte:** hell (statt dunkel), mit Gebäudefoto, auf allen Seiten
- **Footer:** abgerundete obere Ecken, Tagline „Wir gehören zum alten Eisen.", Korn-Textur AUS (Kundenstand)
- **Mobil:** Sticky-Leiste „☎ Anrufen | 💬 WhatsApp" am unteren Rand (CI-Pflicht), Grids stapeln, Plakette ausgeblendet
- **Hover-Zustände:** durchgängig reine Farbwechsel (Kundenentscheidung, keine Transforms)

**Abweichungen vom Prototyp (begründet):**
1. H1 der Startseite behält den SEO-Wortlaut („Schrott-Ankauf in Berlin – Ihr Schrotthandel in Reinickendorf", zweizeilig mit Magenta-Akzent) statt Prototyp-Platzhalter „SCHROTT BRINGT BARES GELD." — README §CI verbietet Inhaltsänderungen; Rankings hängen an der H1.
2. Header-Nav um „Schrottpreise" ergänzt (5 statt 4 Punkte) — wichtigste Conversion-/Ranking-Seite.
3. Material-Grid mit 9 statt 6 Karten — erhält alle bestehenden internen Links der Startseite (SEO).
4. Container-Checkliste ohne „Bauschutt" (Prototyp-Text) — nicht durch Originalinhalte belegt; Peglow-Container sind laut /container/ für Schrott/Metall.
5. FAQ-Wortlaute der Live-Inhalte beibehalten (FAQPage-Schema muss dem sichtbaren Text entsprechen); Prototyp-FAQs waren Platzhalter.

QA nach Redesign: 64/64 URLs, 0 Fehler, 0 Warnungen.

**Design-Iterationen nach Kundenfeedback (12.08.2026):** Footer full-width schwarz (Inhalt bleibt auf Containerbreite); alle Emoji-Icons durch feine Inline-Stroke-SVGs (Feather-Stil, ISC-Lizenz, kein CDN) ersetzt — Telefon/Chat/Mail/Uhr/Häkchen/Plus/Pfeil, inkl. CSS-Masken für Pseudo-Elemente.

## Nachtrag: Interaktiver Design-Walkthrough mit Kunde (12.08.2026)

Startseite Abschnitt für Abschnitt mit dem Kunden finalisiert, alle Entscheidungen auf sämtliche Seiten übertragen:
- Hero: nur noch ein CTA („Jetzt Preis erfragen"), Anfahrt im Hauptmenü, §56-Plakette lesbarer + auch mobil
- Stats-Kacheln (20+ Jahre Erfahrung / 3–30 m³ / Mo–Fr 8–17 Uhr), Intro als 2 Spalten mit Inhaber-Foto (Philip Peglow, Namens-Plakette mit Logo)
- Metall-Karussell: 9 Foto-Kacheln mit pinkem Namens-Streifen, fortlaufender Film-Lauf (Endlos-Schleife), Punktnavi + Pfeile, Apple-Stil
- 3-Schritte-Kacheln (1→2→3 mit Pfeilen), Leistungen direkt darunter, Container-Feature 50/50
- Google-Bewertungen: 7 echte Reviews aus dem Trustindex-Widget der Alt-Site extrahiert, als Karussell (auch auf /uber-uns/ und /peglow-schrott/); kein Review-Schema (Google-Guideline „self-serving")
- Karte: echte OSM-Karte (Build-Zeit-Kachel-Stitch, selbst gehostet, © OpenStreetMap-Mitwirkende, Peglow-Pin) + „Route in Google Maps öffnen"-Link — kein Embed, kein Cookie-Banner nötig; auf Startseite (50/50 neben „Wo ist Peglow"), /anfahrt/, /einzugsgebiete/, /kontakt/
- FAQ + Kontaktbox 50/50, Überschrift bündig; Kontaktbox mit Handy-Zeile + Buttons Kontaktformular/WhatsApp (grün)
- Einheitlicher Abstands-Rhythmus (~72px), Related als dezente zentrierte Pills, feine Stroke-Icons überall, Footer full-width
- Offener Punkt neu: Google-Reviews sind statisch — Auto-Aktualisierung optional via Places API als Build-Schritt

## Design-Finalisierung abgeschlossen (12.08.2026, Abend)

Letzte Runde mit dem Kunden abgenommen:
- Heros auf ALLEN Seiten im Startseiten-Stil (Kicker, zweizeilige H1 mit Magenta-Akzent, Subline, CTA, §56-Plakette unten rechts — auch mobil); Ausnahme: Rechtsseiten ohne Preis-CTA
- Panel-Verlauf leicht verstärkt für helle Hero-Bilder
- Footer-Socials als Facebook-/Instagram-Icons (Simple Icons, CC0) statt Buttons
- Stand vom Kunden abgenommen: „so lassen wir es erst einmal"

## Deployment auf Vorschau-Domain (13.08.2026)

Site in Mittwald-App WEB_NEW_2026 (Projekt p-asttdj) deployt, VHost **https://neu.schrott-berlin.de** angelegt (DNS-Zone auto, Let's-Encrypt-Zertifikat ausgestellt, alle Checks 200). `.htaccess`: 404-Seite, Asset-Caching, X-Robots-Tag noindex nur für den Vorschau-Host. Live-Domains zeigen unverändert auf WordPress. Re-Deploy: build.py + rsync (siehe project-state.md).

## SEO-Fixes nach Semrush-Abgleich (13.08.2026)

Datenbasis: Semrush Organic Research (Projekt „Peglow Schrott"). Umgesetzt:
1. **/schrottpreise/**: Title/H1 „Aktuelle Schrottpreise Berlin – Tabelle & Tagespreise", Tabellen-Caption mit „Tabelle", Textergänzung Kupfer-Schrottpreis/Stahlschrott/Metallschrott, neue FAQ „Gibt es eine aktuelle Schrottpreise-Tabelle?" (Ziel: kupfer schrottpreis 5.400, schrottpreis aktuell 3.600, aktuelle schrottpreise 3.600, stahl 2.400, tabelle 1.900, metallschrott 1.900)
2. **Preis-FAQ auf 6 Materialseiten** (edelstahl ← Pos. 15 bei 2.400 SV, guss, aluminium inkl. „Aluschrott" im Text, messing, mischschrott, kupfer „Was kostet Kupfer pro kg?") — Antworten ohne €-Beträge, LME/Reinheit/Menge + Tagespreis-Telefonverweis; Überlappungs-Check der Antworten max. 5 %
3. **Startseite**: Absatz in „Warum Peglow?" mit Berliner Schrotthändler / Schrottannahme / „Schrottplatz in der Nähe" / Schrottentsorgung
4. **/schienen/**: „Eisenbahnschienen" in Title/H1/Text · **/schrott-verkaufen/**: „Altmetall verkaufen" in Title/H1 · **/zink-ankauf-berlin/**: „Zink-Schrott" in H1
5. QA 0/0, Titles 48–57, Metas 142–154 Zeichen, deployt auf neu.schrott-berlin.de

Zudem umgesetzt (Kundenfreigaben): „Abholung (gegen Aufpreis)" an 162+ Stellen inkl. llms.txt und prominenter Titles/Metas/Heros; „Umland und Falkensee"-Aufzählungen zu „gesamtes Berliner Umland" bereinigt (Falkensee-Bezirksseite unangetastet); Hero-Subline Startseite ohne „Anlieferung auf die Waage".
