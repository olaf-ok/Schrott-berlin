# CI-Vorgaben: Peglow Schrott & Metall (schrott-berlin.de)

> Briefing-Datei für Design-KI / Designer. Stand: 12.08.2026.
> Ziel: Bestehende Markenidentität schärfen und visuell deutlich mutiger umsetzen — kein Rebranding!

## 1. Marke & Charakter

- **Unternehmen:** Peglow Schrott und Metallhandel e.K. — Schrottplatz & Metall-Ankauf, Berlin-Reinickendorf, seit über 20 Jahren
- **Markenkern:** ehrlich, direkt, bodenständig, Berliner Schnauze mit Humor („Wir gehören zum alten Eisen!"), Familienbetrieb statt Konzern
- **Zielgruppe:** Handwerker, Werkstätten, Bauunternehmen, Privatleute mit Keller-/Haushaltsauflösung
- **Gefühl, das die Seite auslösen soll:** „Die wissen, was mein Schrott wert ist, und zahlen fair — da fahr ich hin."
- **Design-Richtung:** industriell, robust, kontrastreich, plakativ. Denk: Werkhalle, Stahl, Warnmarkierungen, Stempel/Plaketten — NICHT: Startup, Corporate, cleanes SaaS.

## 2. Logo

- Datei: `reference/design/assets/LOGO_neu-Out-line.png` (352×132, transparent)
- Wortmarke „PEGLOW" in Schwarz, integriertes **magenta Krokodil-Maskottchen**, das einen Stahlträger trägt, Subline „SCHROTT·METALL"
- Das Krokodil ist der größte visuelle Schatz der Marke → darf gern prominenter/verspielter eingesetzt werden (Illustrationen, Icons, 404-Seite, Trennelemente) — aber nie verzerren, nie umfärben
- Auf dunklem Grund: weiße Version nötig (existiert noch nicht → erstellen oder Logo auf weißer Plakette platzieren)

## 3. Farben

| Rolle | Wert | Verwendung |
|---|---|---|
| **Primär/Akzent: Peglow-Magenta** | `#E2007A` | CTAs, Preise, Highlights, Maskottchen — die Signalfarbe, mutig einsetzen |
| Magenta dunkel | `#B30061` | Hover, Verläufe |
| **Schwarz/Ink** | `#131316` | Headlines, Header/Footer, große Flächen — die Basis |
| Stahl-Anthrazit | `#26262B` / `#38383F` | Sektionen, Hero-Overlays |
| Zink-Hellgrau | `#F2F2F4` (Linien `#DEDEE3`) | Hintergrundflächen, Karten |
| Weiß | `#FFFFFF` | Text auf dunkel, Grundfläche |
| Text | `#3A3A40` (nie heller als `#5C5C64`) | Fließtext, Kontrast ≥ 4.5:1 |

Prinzip: **Schwarz dominiert, Magenta knallt punktuell** (10–15 % Flächenanteil). Kein Bunt-Mix, keine Pastelltöne, keine Verläufe außer Magenta→Magenta-dunkel.

## 4. Typografie

- **Headlines:** Roboto Slab 600/700 — groß, schwer, plakativ (H1 gern 3–4 rem, eng gesetzt). Slab = industrieller Charakter, unbedingt behalten
- **Text/UI:** Roboto 400/500/700
- Beide liegen als selbst gehostete Variable Fonts in `outputs/static/fonts/` — **keine Google-Fonts-CDN-Einbindung** (DSGVO)
- Erlaubte Stilmittel: VERSALIEN mit Letterspacing für Labels/Kicker, Magenta-Unterstreichungen/Marker-Effekte, große Zahlen (Preise, „20+ Jahre", „3–30 m³")

## 5. Bildsprache

- **Nur echte Betriebsfotos** (liegen in `reference/design/assets/`): LKW mit Container, Gabelstapler, Bagger, Schrottschere, Gebäude mit Peglow-Graffiti, Material-Nahaufnahmen (Kupfer, Messing, Zink …)
- **Behandlung: HELL, satt, emotional!** Fotos sind der Stolz des Betriebs — zeigen, nicht verstecken. Kräftige Sättigung, warmes Licht, hoher Kontrast. Abdunkelung NUR partiell dort, wo Text draufliegt (z. B. Verlaufspanel links), nie flächig. Optional Magenta-Lichtakzent statt Grau-Overlay. **No-Go: flächige dunkle Overlays, die das Bild ersticken (wirkt langweilig/emotionslos).**
- **Keine Stock-Business-Fotos, keine KI-generierten Menschen**
- Grafische Zutaten, die zur Marke passen: schraffierte Warnstreifen (schwarz/magenta statt schwarz/gelb), Stempel-/Plaketten-Optik für Zertifikate („Geprüfter Entsorgungsfachbetrieb §56 KrWG"), gerissene/schräge Sektionskanten (Stahl-Schnittkante), Rasterpunkte/Grobkorn-Textur

## 6. Komponenten-Prinzipien

- **CTAs:** Magenta, groß, mit Telefonnummer im Button („☎ 030 - 43 20 63 15") — Anruf ist DIE Conversion
- Sticky-Element mobil: Anruf-/WhatsApp-Leiste am unteren Rand
- Checklisten mit fetten Magenta-Häkchen, Tabellen mit schwarzem Header
- FAQ als Accordion, NAP-Block (Adresse/Öffnungszeiten) auf jeder Seite identisch
- Footer: dunkel, 4 Spalten (Materialien / Bezirke / Service / Kontakt) — bleibt strukturell so (SEO)

## 7. Ton (falls Texte angepasst werden)

Sie-Anrede, kurz, direkt, ehrlich. Kein Marketing-Sprech. Humor sparsam („Wir gehören zum alten Eisen"). **Fakten niemals ändern:** Adresse Soltauer Straße 27-29, 13509 Berlin · 030 43206315 · Mo–Fr 8–17 Uhr · keine €-Preise nennen, keine „kostenlose Abholung" versprechen.

## 8. Technische Leitplanken (WICHTIG)

- Statische Site, **ein einziges Stylesheet:** `outputs/static/css/style.css` — Änderungen NUR dort (+ ggf. `outputs/templates.py` für Markup)
- Kein Framework, kein Build-Tool, kein externes CDN, kein JavaScript-Zwang (max. kleine Progressive-Enhancement-Snippets)
- Mobile-First, Barrierefreiheit erhalten (Kontraste, Fokus-Stile, Skip-Link, semantisches HTML)
- HTML-Struktur/URLs/Inhalte dürfen NICHT geändert werden (SEO!) — nur Präsentation
- Nach Änderung: `cd outputs && python3 build.py && python3 qa_check.py` (muss 0 Fehler bleiben)

## 9. Was den „Knaller" ausmacht (Auftrag an die Design-KI)

Die aktuelle Umsetzung ist solide, aber zu brav. Gewünscht:
1. **Hero mit Wucht:** riesige Slab-Headline, helles emotionales Foto in voller Kraft (Textschutz nur per partiellem Verlauf), schräge Schnittkante, Krokodil-Akzent
2. **Mehr Magenta-Mut:** plakative Preis-/CTA-Blöcke, Marker-Unterstreichungen, Warnstreifen-Details
3. **Industrielle Textur:** dezentes Korn/Raster auf dunklen Flächen statt flacher Fills
4. **Zahlen groß inszenieren:** 20+ Jahre, Mo–Fr 8–17, 3–30 m³ Container
5. **Zertifikate als Plaketten/Stempel** statt Fußnoten-Text
6. Micro-Interaktionen: Hover mit Versatz/Schatten, CSS-only

## 10. No-Gos

Pastell, Verläufe in Fremdfarben, runde „freundliche" Blobs, Startup-Illustrationen, Inter/Arial/System-Fonts, Stockfotos, Cookie-Banner-pflichtige Einbindungen (Google Maps/Fonts), Layout-Shifts (CLS), Text unter 4.5:1 Kontrast, Änderungen an URLs/Inhalten/Schema-Markup.
