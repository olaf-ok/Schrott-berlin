# Projekt-State: Schrott-Berlin-2026

**Letztes Update:** 2026-09-03 (Re-Deploy Content-Fixes)

## Projektkontext & Ziele
Kompletter Relaunch von schrott-berlin.de (Peglow Schrott und Metallhandel e.K., Berlin-Reinickendorf). Autonomer Auftrag. Original-Site unangetastet, kein Deployment. Auftrag: `context/auftrag-relaunch.md`, Fakten/NAP: `context/fakten.md`.

## Aktueller Status: 🚀 LIVE auf schrott-berlin.de (seit 01.09.2026)
Olaf hat den VHost schrott-berlin.de (+www) auf WEB_NEW_2026 umgestellt. Datenschutzerklärung angepasst, Livegang-Stand von Olaf abgenommen („soweit passt alles", 01.09.). Am 01.09. Umami-Tracking eingebaut, Sitemap-Datum auf 2026-09-01 gesetzt, neu deployt und live verifiziert (Umami-Script auf allen Seiten, kein X-Robots-noindex, 5 kritische Redirect-Ziele 200, 404 ok, www→non-www 301, 11 Zusatzdomains 301 → schrott-berlin.de).

### Umami (Analytics, seit 01.09.2026)
Umami Cloud, Script `https://cloud.umami.is/script.js`, Website-ID `45a317fa-d574-44ad-a0a6-168a7bc6a133`. Konfiguration in `outputs/site.json` → Schlüssel `umami` (src + website_id); `templates.py` `base()` rendert das `<script defer>` im Head nur wenn beide Werte gesetzt sind. Cookielos → kein Banner nötig, aber Datenschutzerklärung muss Umami nennen (s. offene Punkte).

### Sitemap
`build.py` → `TODAY` hardcodiert (aktuell 2026-09-01), gilt als lastmod für alle 63 Sitemap-URLs (/danke/ ausgeschlossen). Bei inhaltlichen Änderungen bewusst hochsetzen. Live: https://schrott-berlin.de/sitemap.xml — in Search Console einreichen (Property schrott-berlin.de → Sitemaps → `sitemap.xml`).

## Historie: Design vom Kunden abgenommen (12.08.2026 Abend)
Interaktiver Walkthrough abgeschlossen, alle Entscheidungen auf alle 64 Seiten übertragen, Olaf: „so lassen wir es erst einmal". Finale QA: 0 Fehler. Vollständiger Bericht: **`outputs/ABSCHLUSSBERICHT.md`**
Zuletzt: Heros überall im Startseiten-Stil (+ §56-Plakette, Rechtsseiten ohne Preis-CTA), Footer-Socials als Icons.

- 64/64 URLs 1:1 erhalten (inkl. 5 Redirect-Ziele), statische HTML-Site in `outputs/site/`
- Stack: eigener Python-Stdlib-Generator (build.py + templates.py + content/*.json), kein Framework
- SEO+GEO komplett (Schema.org RecyclingCenter/Service/FAQPage/Breadcrumb überall, llms.txt, KI-robots.txt, FAQ-Blöcke, NAP-Konsistenz)
- 3 Schwerpunktseiten ausgebaut: /edelstahl/ (938 W.), /aluminium/ (912 W.), /mischschrott/ (869 W.)
- 3 Review-Runden durchlaufen; qa_check.py final: 0 Fehler / 0 Warnungen
- Performance: Home-HTML 139→21 KB, ~7 Requests, kein JS, kein Cookie-Banner nötig

## Ansehen / Bauen
- Ansehen: `cd outputs/site && python3 -m http.server 8080` → http://localhost:8080
- Bauen: `cd outputs && python3 build.py` · QA: `python3 qa_check.py`
- Screenshots alt/neu: `outputs/screenshots/`

## Entscheidungen (Begründungen im Bericht §3, §7, §8)
- Statischer Generator statt WP/Framework (CWV, Wartungsfreiheit, Mittwald-kompatibel)
- Edelstahl/Aluminium/Mischschrott: bestehende dünne Seiten ausgebaut statt neuer URLs
- Unbelegte „kostenlos"-Abholung-Versprechen entfernt (Original behauptet das nicht)
- /danke/ noindex + aus Sitemap; 404.html neu; Nav-Reihenfolge leicht optimiert

## Offene Punkte NACH Livegang (Stand 01.09.2026)
1. **Datenschutzerklärung am 01.09.2026 an neue Technik angepasst** (`outputs/content/datenschutz.json`, live): Mittwald statt Strato, keine Cookies/kein Consent-Tool, lokale Fonts, statische OSM-Karte, Umami Cloud (cookielos, Art. 6 I f, SCC), WhatsApp/Social nur als Links, Aufsichtsbehörde Alt-Moabit 59-61. **Vom Kunden/Juristen zu bestätigen:** AVV mit Mittwald und Umami tatsächlich geschlossen? Umami-Region (US vs. EU) und Firmensitz stimmen? Allgemeine Rechtstexte (Betroffenenrechte, Bewerbungen) wurden nicht neu geprüft.
2. **schrottplatzberlin.de + www.schrottplatzberlin.de** (Olaf kümmert sich selbst, Stand 01.09.): VHost auf Mittwald hat kein Ziel (`useDefaultPage` → „Keine Website hinterlegt"), alle anderen Zusatzdomains zeigen auf WordPress-Installation `eb17f9ae…` und leiten 301 auf schrott-berlin.de. Fix: gleiches Ziel setzen oder (langfristig) Host-Redirect in `.htaccess` der neuen App, sobald WordPress abgeschaltet wird.
3. contact.php-Mailversand auf Mittwald testen
4. Geo-Koordinaten (52.5877/13.3126 = Annahme) verifizieren
5. Search Console: Sitemap eingereicht? (Olaf macht das manuell) · neu.schrott-berlin.de weiterhin noindex, kann bleiben oder gelöscht werden
6. Optional: Reviews-Auto-Update per Places-API-Build-Schritt
7. WordPress-App „Schrott Berlin 2026" (a-gsgtf5) erst abschalten, wenn Punkt 2 gelöst ist (sie bedient die 301s der Zusatzdomains)

## Design-Walkthrough mit Olaf (12.08.2026) — ABGESCHLOSSEN
Startseite gemeinsam finalisiert und auf alle 64 Seiten übertragen. Kern-Entscheidungen: 1 Hero-CTA, Anfahrt im Menü, Stats-Kacheln, Inhaber-Foto neben Intro (philip-peglow-schrottplatz.webp + Namens-Plakette), Metall-Karussell als Endlos-Film (peg-carousel, generisches JS in base), 3-Schritte-Kacheln, echte Google-Reviews (7 Stück aus Trustindex der Alt-Site, in site.json, auch auf uber-uns/peglow-schrott), OSM-Karte selbst gehostet (Build-Zeit-Stitch, Attribution Pflicht!) auf Home/Anfahrt/Einzugsgebiete/Kontakt, FAQ+NAP 50/50, Related-Pills dezent, Footer full-width, feine Stroke-Icons. Kein Review-Schema (self-serving). Neuer offener Punkt: Reviews statisch → optional Places-API-Build-Schritt.

## Redesign „Soft-Industrial" (12.08.2026, nach Design-Handoff)
Design-Handoff `reference/design_handoff_peglow_startseite/` vollständig umgesetzt: weißer Header + Telefon-CTA, Hero-Foto-Karte mit Panel + §56-Plakette, Stats-Chips, Material-Grid (9 Foto-Karten), Warnstreifen, Container-Feature, helle NAP-Karte mit Gebäudefoto, Footer mit Rundung + Tagline, mobile Sticky-Anruf-Leiste. Abweichungen vom Prototyp (H1-SEO-Wortlaut, 9 statt 6 Material-Karten, kein „Bauschutt", Original-FAQs) im Bericht-Nachtrag begründet. QA: 0/0.

## SEO-Fixes nach Semrush-Abgleich (13.08.2026) — ERLEDIGT
Alle 5 Fixes umgesetzt + deployt (Details: ABSCHLUSSBERICHT.md): /schrottpreise/ auf „Aktuelle Schrottpreise – Tabelle" geschärft, Preis-FAQs auf 6 Materialseiten, Schrotthändler/Schrottannahme/Schrottentsorgung auf Startseite, Eisenbahnschienen//Altmetall-verkaufen/Zink-Schrott-Fixes. Außerdem: „Abholung (gegen Aufpreis)" überall, Falkensee aus Umland-Aufzählungen raus, Hero-Subline gekürzt. Alles live auf neu.schrott-berlin.de. ToDo-Liste leer.

## Mittwald-Deployment (13.08.2026)
Neue Site in mStudio-Projekt „Schrott Berlin" (p-asttdj) in die vom Kunden angelegte PHP-App **WEB_NEW_2026** (a-mcg9tb, Pfad `/home/p-asttdj/html/webnew2026/`) per rsync deployt — 64 Seiten + sitemap/robots/llms/contact.php/.htaccess (404 + Caching). WordPress-App „Schrott Berlin 2026" (a-gsgtf5) unangetastet; damals zeigten alle VHosts noch auf WordPress. **01.09.2026: schrott-berlin.de + www zeigen jetzt auf WEB_NEW_2026 (von Olaf umgestellt), Site ist live.** Vorschau-VHost **https://neu.schrott-berlin.de** → WEB_NEW_2026 angelegt (VHost 6fe2ca14, per mw-CLI; MCP-Tool-Parameter pathToApp war buggy). DNS-Zone auto-erstellt. `.htaccess` setzt X-Robots-Tag noindex NUR für Host neu.schrott-berlin.de (deaktiviert sich bei Domain-Umstellung selbst). Re-Deploy: `cd outputs && python3 build.py && rsync -rlptz --delete site/ "info@ok-marked.com@p-asttdj@ssh.altgemeinde.project.host:/home/p-asttdj/html/webnew2026/"`. Hinweis: 10 versehentliche „* 2"-Finder-Duplikate in site/ wurden durch frischen Build entfernt.

## Content-Fix: „kostenlose" Abholung korrigiert (03.09.2026)
Olaf hat per WhatsApp-Screenshot markiert, dass der Startseiten-Intro-Satz „Auf Wunsch holen wir Ihren Schrott in ganz Berlin und im gesamten Berliner Umland ab." fälschlich eine kostenlose Abholung suggeriert (Abholung ist kostenpflichtig). Home-Intro nach Olafs Formulierungsvorschlag angepasst (Abholservice kostenpflichtig, Kosten vorab transparent). Auf Olafs Wunsch danach sitehweit geprüft und an **allen** weiteren Fundstellen ohne Kostenhinweis ergänzt (Zusatz „(gegen Aufpreis)" bzw. bei der Meta-Description „(Aufpreis)" wegen Zeichenlimit):
`_home.json` (Intro + FAQ), `schrott-ankauf.json`, `anfahrt.json`, `aluminium.json` (Intro + FAQ), `aluminium-guss.json`, `bremsscheiben.json`, `zink-ankauf-berlin.json`, `altmetall-reinickendorf.json`, `metall-schrott.json`, `blei-ankauf.json` (Intro + FAQ), `schienen.json` (Intro + FAQ), `mischschrott.json`, `edelstahl.json` (Intro + Text + FAQ), `kabel-schrott.json`, `kupfer.json`, `uber-uns.json`, `messing-schrott.json` (Text + FAQ), `brennerschrott.json` (Intro + FAQ), `einzugsgebiete.json` (Meta-Description + Schema-Description). ~25 Textstellen in 19 Dateien. Seiten mit vorhandenem Kostenhinweis im selben Absatz (`kontakt.json`, `kupfer-ankauf-berlin.json`, Bremsscheiben-Leistungsblock) unverändert gelassen.
Build (`python3 build.py`) + QA (`python3 qa_check.py`): 0 Fehler / 0 Warnungen.
**Noch NICHT deployt** — wartet auf Olafs OK (Re-Deploy-Befehl s. Abschnitt „Mittwald-Deployment").

## Content-Fix: Abholung komplett auf Container-Modell korrigiert (03.09.2026)
Olaf hat nach dem ersten Fix (s.o.) klargestellt: **Peglow holt niemals persönlich losen Schrott ab.** Es gibt ausschließlich Container zum Selbstbeladen (Absetz-/Abrollcontainer), die aufgestellt und nach Befüllung durch den Kunden wieder abgeholt werden. Alle Formulierungen im Sinne von „wir holen Ihren Schrott/Ihr Material persönlich ab" waren sachlich falsch und wurden sitehweit auf Container-Sprache umgestellt — „wir holen den Container ab" (nach Befüllung) blieb überall unverändert stehen, das ist korrekt.

**Containergröße vom Kunden bestätigt:** kleinste Größe ist **5 m³** (nicht 3, nicht 7) — durchgängig „5–30 m³" auf der ganzen Seite.

**Umsetzung:** Auf Olafs Wunsch 4 Formulierungsvarianten (A–D) erstellt und freigegeben („Nimm A und B vorrangig aber auch C und D, passe es überall an"). A/B (Kernformulierungen „Container zum Selbstbeladen (5–30 m³)" bzw. „wir stellen einen Container auf und holen ihn nach der Befüllung wieder ab") als Standard verwendet, C/D (Container-Service, Container-Turnus, Containeraufstellung) zur Abwechslung eingestreut.

**Geänderte Dateien** (alle 64 Content-Dateien geprüft, betroffen waren u. a.): alle 17 `schrottplatz-*.json` (Bezirksseiten, komplett durchgearbeitet: Title/Meta/H1/Hero/Intro/Sections/Checklist/FAQ/Schema/CTA), `kupfer-ankauf-berlin.json` und `zink-ankauf-berlin.json` (komplette Neufassung, Grundthema war „mit Abholung"), `edelstahl.json`, `aluminium-guss.json`, `guss.json`, `messing-schrott.json`, `mischschrott.json`, `schrott-reinickendorf.json`, `brennerschrott.json` (CTA-Heading), `_home.json` (Checklist + Ablauf-Schritt), sowie `messing.json`, `metall-ankauf.json`, `schrotthandel.json`, `kabel.json`, `schrottpreise.json`, `zink.json`, `eisen-schrott.json`, `metallhandel-berlin.json`, `schrott-verkaufen.json`, `kupfer.json`, `schrott-ankauf.json` (auch „ab etwa 3 m³" → „ab etwa 5 m³"), `peglow-schrott.json`, `metall-schrott.json`, `schienen.json`, `moniereisen.json`, `kabel-schrott.json`, `altmetall-ankauf.json`, `altmetall-reinickendorf.json` (Link-Labels „mit Abholung" → „mit Container"). Mehrere Meta-Descriptions dabei ans 165-Zeichen-Limit angepasst (u. a. Friedrichshain, Neukölln, Kabel-Schrott, Zink-Ankauf, Edelstahl, Charlottenburg, Wilmersdorf, Kreuzberg).

**Bewusst unverändert gelassen:** `container.json` (Container-Landingpage selbst — alle 8 „Abholung"-Treffer beziehen sich korrekt auf die Container-Abholung nach Befüllung), legitime Bezirksseiten-Formulierungen wie „wir stellen ihn auf und holen ihn nach der Befüllung wieder ab", `kupfer-raff.json`/`messing-raff.json`/`ankauf.json`/`metall-ankauf-berlin.json` (schon korrekt), Rechts-/Utility-Seiten ohne Abholungs-Bezug.

Build (`python3 build.py`) + QA (`python3 qa_check.py`): **0 Fehler / 0 Warnungen** (65 Seiten geprüft, ein Meta-Description-Warning bei Kreuzberg im Zuge dessen noch gefunden und gekürzt).
**Deployt am 03.09.2026** (Olafs OK) — live auf schrott-berlin.de verifiziert (Home-Intro „kostenpflichtig", `/kupfer-ankauf-berlin/` „Container zum Selbstbeladen" 10× wie im Build).

**Offene Frage für Olaf:** Die Container-Maßtabelle auf `container.json` (Abmessungen L×B×H) zeigt für die kleinste Größe noch die alten Werte (vorher als 7 m³ angenommen). Da jetzt 5 m³ als kleinste Größe bestätigt ist, müssen die genauen Maße (L×B×H) noch mit Olaf abgeglichen werden, bevor die Tabelle final stimmt — wurde in diesem Durchgang nicht angefasst, um keine Zahlen zu erfinden.


## Git-Backup (03.09.2026)
Lokales Repo initialisiert, Push nach `https://github.com/olaf-ok/Schrott-berlin.git` (Branch `main`). SSH-Key `github_olaf_ok` wurde von GitHub abgelehnt, daher HTTPS via `gh`-Credential-Helper. Künftige Backups: `git add -A && git commit -m "..." && git push`.

## Behobene Bugs
- 01.09.2026: `render_legal()` in templates.py gab das `intro`-Feld nie aus → Verantwortlicher-Block der Datenschutzerklärung fehlte seit Relaunch. Behoben, Impressum zeigt seitdem ebenfalls sein Intro.
- 03.09.2026: `header_html()` in templates.py enthielt einen Backslash in einer f-string-Expression → SyntaxError unter Python 3.10 (System-Python auf Olafs Mac, Build funktionierte bislang nur in einer neueren Python-Umgebung). Fix: Bedingung in eine Variable ausgelagert, Build läuft jetzt auch lokal mit Python 3.10.12.

## Vorfall-Log
- Content-Agent für Bezirksseiten wurde durch monatliches API-Spend-Limit abgebrochen → 5 Seiten manuell nachgeschrieben, Reviews inline statt per Agent durchgeführt

## Deploy-Weg geklärt (14.09.2026)
Olaf fragte, ob er Änderungswünsche im Chat geben kann und Claude live stellen kann. **Ja — verifiziert am 14.09.2026:**
- **Kein Mittwald-MCP nötig und keiner vorhanden** (Refresh der MCP-Server zeigt keinen Mittwald-Server; installierte Extensions: chrome-control, filesystem, notes, pdf-server). Die Mittwald-**CLI** `mw` ist auf dem Mac installiert (/opt/homebrew/bin/mw, v1.20.1) — für VHost-/App-Verwaltung, nicht für Datei-Deploy.
- **Deploy läuft über Desktop-Commander** (MCP mit vollem Mac-Zugriff): `start_process` führt Befehle in Olafs echtem Benutzerkonto aus, damit stehen die SSH-Keys in `~/.ssh` zur Verfügung. SSH zum Mittwald-Host getestet: **funktioniert** (`SSH_OK`).
- **NICHT möglich** ist der Weg über die Cowork-Linux-VM (`device_bash`): die hat ein eigenes, leeres `$HOME` ohne Olafs SSH-Keys → `Permission denied (publickey)`. Deshalb immer Desktop-Commander für Deploys verwenden.
- Ablauf: `cd ~/Documents/Code/Schrott-Berlin-2026/outputs && python3 build.py && python3 qa_check.py` → Ergebnis Olaf zeigen → nach OK `rsync -rlptz --delete site/ "info@ok-marked.com@p-asttdj@ssh.altgemeinde.project.host:/home/p-asttdj/html/webnew2026/"` (bzw. `./deploy.sh`, das alle drei Schritte macht).
- Stand 14.09.2026: Build + QA 0/0, rsync-Dry-Run zeigt 72 Dateien nur mit `<f..t....` = **reine Timestamp-Differenz, inhaltlich identisch** mit dem Live-Stand. Es steht also nichts Unveröffentlichtes an.
- Hinweis: Python auf dem Mac ist inzwischen 3.14.6, Build läuft fehlerfrei.

## SEO-Arbeiten 14.09.2026 (deployt)
**Anlass:** Auswertung der Entwicklung seit dem Relaunch (01.09.) gegen die Zeit davor.

**Änderungen im Repo:**
- `related`-Verlinkung in 14 Content-Dateien ergänzt. Vorher/nachher (live geprüft): `/ankauf/` 0→6 verlinkende Seiten, `/schrott-reinickendorf/` 1→3, `/altmetall-reinickendorf/` 2→3, `/moniereisen/` →4, `/brennerschrott/` →4, `/schrottplatz-berlin/` →14.
- `schrottpreise.json`: Title, Meta und H1 versprachen eine Preistabelle, die die Seite nicht hat (H2 dort: „Warum gibt es bei uns keine feste Preisliste?"). Neu: „Schrottpreise Berlin – aktueller Tagespreis | Peglow", H1 „Schrottpreise in Berlin – aktuelle Tagespreise für Ihr Material", Meta mit dem WhatsApp-Weg. Kein Tabellen-Versprechen mehr.
- `moniereisen.json` und `peglow-schrott.json`: Meta-Description von je 160 auf ~135 Zeichen gekürzt.
- `build.py`: `TODAY` stand fest auf `date(2026, 9, 1)` — die Sitemap meldete nach jedem Deploy „nichts geändert". Jetzt `date.today()`. Nebenwirkung: Jeder Build ändert alle 63 `lastmod`-Werte.

**Zwischenfall beim Deploy:** 66 leere Duplikat-Ordner (`ankauf 2`, `zink 2`, `schrottpreise 3` …) und 8 Duplikat-Dateien (`.htaccess 2`, `sitemap 2.xml`, `robots 2.txt`, `index 2.html` …) lagen in `site/` und sind beim ersten rsync auf den Server gewandert. Lokal per `rmdir` entfernt, zweiter rsync mit `--delete` hat sie serverseitig gelöscht. Live als 404 verifiziert, Server hat 67 Ordner / 0 Duplikate. **Sie entstehen nicht beim Build** — ein sauberer Build danach erzeugte null. Pflichtprüfung vor jedem Deploy: `find site -maxdepth 1 -name "* [0-9]*" | wc -l`.

**Nicht geändert, bewusst:** `.htaccess`. Der geplante „ein Hop statt zwei"-Fix wäre wirkungslos — in `htaccess.src` steht gar kein Redirect, die Kette 308→301 kommt vom Mittwald-Stack und greift vor Apache.

**Außerhalb des Repos erledigt:** Google Business Profile zeigte als Website auf `http://www.schrott-berlin.de/` → auf `https://schrott-berlin.de/` geändert. Semrush Position Tracking von 71 auf 87 Keywords erweitert. Search Console: Sitemap neu eingereicht, Indexierung für `/schrottpreise/` und `/moniereisen/` beantragt. Details im Projektstatus unter `ZENTRALES BRAIN/03 Kundenprojekte/Peglow Schrott/Projekte/Webseite/SEO/`.
