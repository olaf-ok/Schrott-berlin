# Design-Brief Relaunch (aus Bestandsanalyse 2026-08-12)

## Markenidentität (Ist-Zustand, zu übernehmen)
- **Logo:** `reference/design/assets/LOGO_neu-Out-line.png` — „PEGLOW" schwarz, Krokodil-Maskottchen in Magenta, Subline „SCHROTT·METALL"
- **Primärfarbe:** Magenta **#E2007A** (Elementor Global Primary; Verlauf-Variante #ea3495)
- **Sekundär:** Schwarz #000000 / Dunkelgrau #262a2b (Header/Hero-Overlays)
- **Text:** #7A7A7A auf Weiß; Flächen: #EBEBEB / #eaeaea hellgrau
- **Fonts:** Roboto (Text/Primary/Accent), Roboto Slab (Secondary/Überschriften) — via Google Fonts, beim Relaunch **selbst hosten** (DSGVO + Performance)
- Akzent-Grün #04B428 nur vereinzelt im Header-Template (Telefon-Icon o. ä.) — untergeordnet

## Bildsprache
- Authentische Betriebsfotos: LKW mit Container, Gabelstapler, Gebäude, Bagger, Schere
- Material-Nahaufnahmen je Materialseite (kupfer_milberry, messing_raff, zink, …)
- Karte des Einzugsgebiets: karte_peglow_01-2.webp
- Haupt-Hero: schrott-berlin-head-01.webp
- Mapping Seite→Hintergrundbilder: `reference/design/page_backgrounds.json`
- Alle Originale liegen in `reference/design/assets/`

## Seitenaufbau (Ist, als Grundmuster übernehmen)
- Topbar: Telefon, E-Mail, Öffnungszeiten, WhatsApp
- Header: Logo + Hauptnavigation (Schrotthandel, Schrott Ankauf, Metall Ankauf, Einzugsgebiete, Schrottpreise, Container, Anfahrt, Über uns, Jobs, Kontakt)
- Hero mit BG-Bild + H1 + Claim
- Content-Sektionen, Checkmark-Listen (haekchen-Icon)
- Sektion „Das sagen unsere Kunden" (Bewertungen)
- Footer: großes Linkverzeichnis aller Bezirks-/Material-Seiten + NAP + Zertifikat + Social + Impressum/Datenschutz

## Relaunch-Verbesserungen (Soll)
- Gleiche Markenanmutung, aber: moderneres Spacing, klarere Typo-Hierarchie, bessere Kontraste (A11y: Textgrau #7A7A7A ist zu schwach → dunkler, z. B. #4a4a4a auf Weiß)
- Mobile-First, semantisches HTML5 (header/nav/main/section/article/footer)
- FAQ-Blöcke als <details> o. ä. + FAQPage-Schema
- Sticky-CTA „Jetzt Schrottpreis anfragen" / Telefon
- Bilder: WebP behalten, width/height-Attribute, lazy loading, responsive srcset wo sinnvoll
