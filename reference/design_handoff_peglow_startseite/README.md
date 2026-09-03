# Handoff: Peglow Startseite (Redesign „Soft-Industrial")

## Overview
Hi-Fi-Redesign der Startseite von schrott-berlin.de (Peglow Schrott und Metallhandel e.K.). Ziel laut CI-Briefing: bestehende Marke mutiger inszenieren — Hero mit Wucht, plakatives Magenta, große Zahlen, Plaketten-Optik. Richtung „Soft-Industrial": industriell-kontrastreich, aber mit dezentem 12px-Radius auf Karten und Fotos.

## About the Design Files
`Peglow Startseite.dc.html` ist eine **Design-Referenz in HTML** — ein Prototyp, der Look und Verhalten zeigt, **kein Produktionscode**. Aufgabe: das Design in der bestehenden Umgebung der Site nachbauen. Die Zielumgebung ist (laut `ci-vorgaben.md`, Abschnitt 8):
- Statische Site, **ein einziges Stylesheet**: `outputs/static/css/style.css` — Änderungen NUR dort (+ ggf. `outputs/templates.py` für Markup)
- Kein Framework, kein Build-Tool, kein externes CDN, kein JavaScript-Zwang
- HTML-Struktur/URLs/Inhalte dürfen NICHT geändert werden (SEO) — nur Präsentation
- Nach Änderung: `cd outputs && python3 build.py && python3 qa_check.py` (muss 0 Fehler bleiben)
- Fonts sind selbst gehostete Variable Fonts in `outputs/static/fonts/` — **keine Google-Fonts-CDN-Einbindung** (der Prototyp lädt sie nur der Einfachheit halber von Google; im Zielcode die lokalen Dateien verwenden)
- Mobile-First, Barrierefreiheit erhalten (Kontraste ≥ 4.5:1, Fokus-Stile, Skip-Link, semantisches HTML)

## Fidelity
**High-fidelity** für Desktop (~1360px). Farben, Typografie, Abstände und Hover-Zustände sind final gemeint. **Mobile Umsetzung ist NICHT im Prototyp enthalten** — mobile-first ableiten; Pflicht laut CI: Sticky-Anruf-/WhatsApp-Leiste am unteren Rand (Muster siehe Wireframes in `Peglow Wireframes.dc.html`, Option 4a mobil).

Alle Fotos/Logo sind im Prototyp Drop-Platzhalter (`<image-slot>`): im Zielcode echte Betriebsfotos aus `reference/design/assets/` einsetzen. Bildbehandlung laut CI: hell, satt, warm — Abdunkelung NUR partiell unter Text (Verlaufspanel), nie flächig.

## Screens / Views

### Startseite (Desktop, max-width 1360px zentriert)

**1. Header** — weiß, `border-bottom: 1px solid #DEDEE3`, Padding 14px 32px, Flex mit `gap: 28px`.
- Logo links: `LOGO_neu-Out-line.png` (352×132, transparent), dargestellt ~176×66, `object-fit: contain`
- Nav rechtsbündig (`margin-left: auto`): Ankauf / Container / Bezirke / Kontakt — Roboto 500, 15.5px, Farbe #131316, kein Underline
- Telefon-CTA: `background:#E2007A; color:#fff; font-weight:700; 16px; padding:12px 22px; border-radius:10px`, Text „☎ 030 - 43 20 63 15", Hover: `background:#B30061` (nur Farbwechsel, KEIN Transform/Schatten)

**2. Hero** — eingesetzte Foto-Karte: Höhe 560px, `margin: 20px 24px 0; border-radius: 12px; overflow: hidden`, `position: relative`.
- Hintergrund: Betriebsfoto (Bagger/Schrottschere), hell & satt, volle Fläche `object-fit: cover`
- Textschutz-Panel links: Breite 58%, `background: linear-gradient(90deg, rgba(19,19,22,.87) 30%, rgba(19,19,22,.55) 65%, transparent)`, Inhalt vertikal zentriert, Padding 0 56px, `gap: 18px`
  - Kicker: 13px, 700, `letter-spacing: .16em`, uppercase, weiß — „Schrottplatz · Berlin-Reinickendorf · seit über 20 Jahren"
  - H1: Roboto Slab 700, 66px, `line-height: 1; letter-spacing: -.01em`, weiß — „SCHROTT BRINGT&lt;br&gt;BARES GELD." („BARES GELD." in #E2007A)
  - Subline: 19px, lh 1.5, #F2F2F4, max-width 480px — „Metall-Ankauf, Containerdienst und Anlieferung auf die Waage — Barauszahlung direkt vor Ort."
  - Buttons (Flex, gap 14px): Primär magenta wie Header-CTA, 18px, padding 16px 28px — „☎ Jetzt Preis erfragen" (`href="tel:03043206315"`); Sekundär: `border: 2px solid #fff; color:#fff`, Hover `background: rgba(255,255,255,.14)` — „Anfahrt & Waage"
- Plakette rechts unten (34px/30px vom Rand): Kreis 118px, `border: 3px solid #fff; border-radius: 50%`, `background: rgba(19,19,22,.42)`, Roboto Slab 600 13px uppercase zentriert, „Geprüfter Entsorgungsfachbetrieb §56 KrWG" (§56 KrWG in #E2007A, 15px). Einblendanimation: von `rotate(-14deg) scale(1.15)` auf `rotate(-7deg)`, .5s ease-out (CSS-only, optional)

**3. Stats-Chips** — 3 gleiche Flex-Kacheln, `gap: 16px; padding: 56px 24px 0`.
- Kachel: `background:#F2F2F4; border-radius:12px; padding:22px 12px`, zentriert, Hover `background:#E8E8EC`
- Zahl: Roboto Slab 700, 46px, #E2007A, lh 1 — „20+" / „3–30 m³" / „Mo–Fr 8–17"
- Label darunter: 15px — „Jahre Familienbetrieb" / „Containergrößen" / „Uhr — Waage geöffnet"

**4. Metall-Ankauf** — `padding: 92px 24px 0`.
- Kicker: 12.5px, 700, `letter-spacing:.16em`, uppercase, #E2007A — „Metall-Ankauf · Tagespreis am Telefon"
- H2: Roboto Slab 700, 38px, #131316 — „Das kaufen wir an." — „an." mit Marker-Effekt: `background: linear-gradient(transparent 62%, rgba(226,0,122,.45) 62%)`
- Grid `repeat(6, 1fr); gap: 14px`, Karten (als Links): `border: 1px solid #DEDEE3; border-radius: 12px; padding: 10px`, zentriert. Hover: `border-color:#E2007A; background:#FDF2F8` (nur Farbe)
  - Foto 110px hoch, radius 8 (Material-Nahaufnahmen: Kupfer, Messing, Zink, Aluminium, Kabel, Edelstahl)
  - Name: Roboto Slab 600, 18px
  - „☎ Tagespreis": 13px, 700, #B30061

**5. Warnstreifen-Trenner** (optional, im Prototyp als Tweak schaltbar) — `height: 10px; margin: 84px 24px 0; border-radius: 5px; background: repeating-linear-gradient(-45deg, #131316 0 14px, #E2007A 14px 28px)`

**6. Containerdienst** — 2 Spalten (Foto 1fr / Text 1.15fr), `gap: 32px; padding: 84px 24px`.
- Foto: min-height 300px, radius 12 (LKW setzt Absetzcontainer ab)
- Kicker magenta wie oben — „Containerdienst"; H2 38px — „Container von 3 bis 30 m³ — Stellung & Abholung." („3 bis 30 m³" in #E2007A)
- Checkliste: 17px, lh 2.1, fette Magenta-Häkchen „✔" (#E2007A, 20px): Bauschutt/Mischschrott/Metall · kurzfristige Stellung in ganz Berlin · faire Abrechnung nach Gewicht
- CTA magenta „☎ Container anfragen", Hover nur `background:#B30061`

**7. FAQ + NAP** — 2 Spalten (FAQ 1.2fr / NAP 1fr), `gap: 32px; padding: 16px 24px 100px`, id `kontakt`.
- FAQ: H2 30px „Häufige Fragen"; native `<details>/<summary>`, `border-bottom: 1px solid #DEDEE3`, Frage 17px/500 mit magenta „+" rechts (22px), Hover Frage #B30061, Antwort 15.5px lh 1.6. 4 Fragen (Wortlaut siehe Prototyp; Fakten-Regeln der CI beachten: keine €-Preise, keine „kostenlose Abholung")
- NAP-Karte (auf jeder Seite identisch!): `background:#F2F2F4; border:1px solid #DEDEE3; border-radius:12px; padding:26px` — Kicker „Anfahrt & Öffnungszeiten", Titel Roboto Slab 700 24px „Peglow Schrott und Metallhandel e.K.", darunter 16.5px lh 1.9: Soltauer Straße 27-29 · 13509 Berlin (Reinickendorf) · ☎ 030 43206315 (tel-Link, fett) · Mo–Fr **8–17 Uhr**. Darunter Foto 150px radius 8 (Gebäude mit Peglow-Graffiti; KEIN Google Maps — DSGVO)

**8. Footer** — `background:#131316; color:#fff; border-radius: 16px 16px 0 0; padding: 40px 40px 22px`.
- Optionale Korn-Textur als Overlay: `background-image: radial-gradient(rgba(255,255,255,.055) 1px, transparent 1px); background-size: 6px 6px` (im Prototyp als Tweak; Kunde hat sie aktuell abgeschaltet — im Zweifel weglassen)
- 4 Spalten Grid, gap 28px, 14.5px lh 2: Materialien / Bezirke / Service / Kontakt (Struktur beibehalten — SEO). Spaltentitel Roboto Slab 600 17px, Links #C8C8CE, Hover #fff
- Bottom-Bar: `border-top: 1px solid #38383F`, 13px #9a9aa2 — „© 2026 … — Wir gehören zum alten Eisen." + Impressum/Datenschutz rechts

## Interactions & Behavior
- Alle Hover-Zustände sind **reine Farbwechsel** (Kundenentscheidung — keine Transforms, keine Offset-Schatten):
  - Magenta-Buttons: #E2007A → #B30061
  - Material-Karten: Rand #DEDEE3 → #E2007A, Fond #fff → #FDF2F8
  - Stats-Chips: #F2F2F4 → #E8E8EC
  - Footer-Links: #C8C8CE → #fff
- Telefon-CTAs als `tel:03043206315`-Links — Anruf ist DIE Conversion
- FAQ: natives `<details>`-Accordion, kein JS
- Plaketten-Einblendung: CSS-Keyframe, `prefers-reduced-motion` respektieren
- Fokus-Stile erhalten/ergänzen (sichtbarer Outline, nicht Browser-Default-blau auf Magenta prüfen)
- Mobil (zu ergänzen): Sticky-Leiste unten „☎ Anrufen | WhatsApp", magenta; Hero-Panel dann volle Breite mit Verlauf; Grids auf 2–3 Spalten/Stack reduzieren

## State Management
Keins nötig — statische Seite. Tweaks des Prototyps (Warnstreifen an/aus, Korn an/aus) sind Design-Entscheidungen, kein Runtime-State. Aktueller Kundenstand: Warnstreifen AN (Default), Korn AUS.

## Design Tokens
Farben (aus `ci-vorgaben.md`):
- Peglow-Magenta `#E2007A` (CTAs, Zahlen, Highlights) · Magenta dunkel `#B30061` (Hover)
- Schwarz/Ink `#131316` · Stahl-Anthrazit `#26262B` / `#38383F`
- Zink-Hellgrau `#F2F2F4`, Linien `#DEDEE3`, Hover-Grau `#E8E8EC`, Rosé-Hover `#FDF2F8`
- Text `#3A3A40` (nie heller als `#5C5C64` für Fließtext), Weiß `#FFFFFF`

Typografie: Roboto Slab 600/700 (Headlines, Zahlen, Kartennamen) · Roboto 400/500/700 (Text/UI) — selbst gehostet. Skala im Prototyp: H1 66px, H2 38/30px, Zahlen 46px, Body 15.5–19px, Kicker 12.5–13px uppercase +.16em.

Radius: 12px (Karten, Fotos, Chips), 10px (Buttons), 8px (kleine Fotos), 16px oben am Footer, 50% Plakette. Sektionsabstände: 56–100px vertikal, 24px Seitenrand.

## Assets
- Logo: `reference/design/assets/LOGO_neu-Out-line.png` (weiße Variante für dunklen Grund existiert noch nicht → erstellen oder Logo auf weißer Plakette)
- Betriebsfotos aus `reference/design/assets/` (LKW/Container, Bagger, Schrottschere, Gebäude-Graffiti, Material-Nahaufnahmen). Keine Stockfotos, keine KI-Menschen.
- Im Prototyp sind alle Bilder leere `<image-slot>`-Platzhalter (Hilfskomponente `image-slot.js`, nur fürs Preview — nicht übernehmen)

## Files
- `Peglow Startseite.dc.html` — der Hi-Fi-Prototyp (Design-Referenz; `<helmet>`/`<x-dc>`-Wrapper und `image-slot.js` sind Prototyp-Infrastruktur, nicht übernehmen)
- `image-slot.js` — Platzhalter-Komponente, nur damit der Prototyp lokal rendert
- `ci-vorgaben.md` — das verbindliche CI-Briefing (Fakten, No-Gos, technische Leitplanken)
- `Peglow Wireframes.dc.html` (im Hauptprojekt, nicht im Bundle) — Wireframe-Erkundung inkl. Mobil-Layouts (Option 4a)
