# Content-Spezifikation für Seiten-JSON (Relaunch schrott-berlin.de)

Jede Seite = eine Datei `outputs/content/<slug>.json` (slug = URL-Pfad ohne Slashes, Homepage = `_home`).
Die Datei MUSS valides JSON (UTF-8) sein und exakt diesem Schema folgen.

## Verbindliche Quellen (IMMER zuerst lesen)
1. `reference/inventar/texte/<slug>.txt` — Originaltext der Seite (Fakten-Quelle!)
2. `reference/inventar/inventar.json` — Eintrag der Seite: alter Title, Meta-Description, Überschriften
3. `context/fakten.md` — verbindliche NAP-/Unternehmensfakten
4. `reference/design/page_backgrounds.json` — verfügbare Hero-Bilder je Seite (Dateinamen aus `reference/design/assets/`)

## Schema

```json
{
  "path": "/kupfer/",
  "template": "material",
  "title": "Kupfer Ankauf in Berlin | Peglow Schrott und Metall",
  "meta_description": "Max. 155 Zeichen, mit Kern-Keyword + USP + Call-to-Action.",
  "h1": "Kupfer-Ankauf in Berlin",
  "hero_kicker": "Schrottplatz Berlin-Reinickendorf",
  "hero_text": "1-2 Sätze Claim unter der H1.",
  "hero_image": "kupfer_milberry.webp",
  "breadcrumb": [["Startseite", "/"], ["Metall-Ankauf", "/metall-ankauf/"], ["Kupfer", "/kupfer/"]],
  "intro": "<p>Ein in sich abgeschlossener Absatz (3-5 Sätze), der die Kernfrage der Seite DIREKT beantwortet — KI-zitierbar. Muss Ort (Berlin/Reinickendorf) + Leistung + Entität (Peglow) enthalten.</p>",
  "sections": [
    {"heading": "Welche Kupfersorten kaufen wir an?", "html": "<p>…</p><ul><li>…</li></ul>"},
    {"heading": "So läuft der Kupfer-Ankauf ab", "html": "<ol><li>…</li></ol>"}
  ],
  "checklist": ["Barzahlung nach tagesaktuellen Preisen", "Ankauf ab 1 kg", "…"],
  "table": {
    "caption": "Kupfersorten im Überblick",
    "head": ["Sorte", "Beschreibung", "Beispiele"],
    "rows": [["Kupfer Millberry", "blanker Draht …", "Kabelader"], ["…", "…", "…"]]
  },
  "faq": [
    {"q": "Was zahlt Peglow aktuell für Kupfer in Berlin?", "a": "Klare, in sich geschlossene Antwort in 2-4 Sätzen. Keine konkreten €-Preise erfinden! Auf tagesaktuelle Preise + Telefon 030 43206315 verweisen."},
    {"q": "…", "a": "…"}
  ],
  "service_schema": {
    "name": "Kupfer-Ankauf Berlin",
    "serviceType": "Ankauf von Kupferschrott",
    "description": "1 Satz."
  },
  "related": [["Messing-Ankauf", "/messing/"], ["Kabel-Ankauf", "/kabel/"], ["Aktuelle Schrottpreise", "/schrottpreise/"]],
  "cta_heading": "Kupfer verkaufen? Jetzt Preis anfragen!",
  "cta_text": "1-2 Sätze."
}
```

## Feld-Regeln
- **path**: EXAKT der Original-Pfad mit führendem und schließendem Slash. NIEMALS ändern.
- **template**: `home` | `material` | `landing` | `district` | `service` | `company` | `contact` | `legal` | `jobs` | `danke`
- **title**: 50–60 Zeichen. Muster „<Keyword> | Peglow Schrott und Metall Berlin" o. ä. Haupt-Keyword der Seite aus altem Title übernehmen/schärfen. Jeder Title einzigartig.
- **meta_description**: 140–155 Zeichen, einzigartig, mit Handlungsaufforderung (z. B. „☎ 030 43206315").
- **h1**: genau eine, keyword-tragend, natürlich formuliert (besser als die alten Ein-Wort-H1s wie „Kupfer").
- **intro**: Der wichtigste GEO-Absatz. Direktantwort auf die implizite Suchfrage, eigenständig zitierbar, Entität + Ort nennen.
- **sections**: 3–6 Sektionen, H2-Überschriften als FRAGEN oder klare Themen. Erlaubtes HTML: p, ul, ol, li, strong, em, a, br. Interne Links (relative Pfade) einbauen — mind. 3 pro Seite, thematisch sinnvoll.
- **checklist**: 4–6 kurze USP-Punkte (wird als Häkchen-Liste gerendert).
- **table**: optional, aber PFLICHT auf Material-Seiten (Sorten/Qualitäten) und auf /schrottpreise/ (Materialübersicht OHNE erfundene Preise — Spalte „Preis" = „tagesaktuell auf Anfrage").
- **faq**: 3–5 Fragen. PFLICHT auf material/landing/district/service. Fragen so formulieren, wie Nutzer sie in Google/ChatGPT stellen. Antworten 2–4 Sätze, in sich geschlossen, NAP-konsistent.
- **service_schema**: nur bei template material/landing/service — Basis für Service-Schema-JSON-LD.
- **related**: 3–5 interne Links (Label + Pfad).
- **Bilder**: hero_image = Dateiname aus reference/design/assets/ (siehe page_backgrounds.json der Seite; wenn leer → passendes Material-/Betriebsbild wählen).

## Inhaltliche Regeln (KRITISCH)
1. **Keine Fakten erfinden.** Keine konkreten Ankaufspreise in €, keine erfundenen Mengen, Mitarbeiterzahlen, Gründungsjahre. Was nicht im Originaltext/fakten.md steht, wird nicht behauptet.
2. **NAP überall identisch** (aus context/fakten.md): Peglow Schrott und Metallhandel e.K., Soltauer Straße 27-29, 13509 Berlin, 030 43206315, info@schrott-berlin.de, Mo–Fr 8–17 Uhr.
3. **Ton**: bodenständig, direkt, vertrauenswürdig, „wir"-Perspektive, Sie-Anrede. Berliner Schnauze dezent ok, kein Marketing-Blabla.
4. **Sprachlich verbessern erlaubt**: alte Texte sind teils dünn/redundant — aufräumen, präzisieren, erweitern. Kernaussagen und Fakten erhalten.
5. **Keyword-Fokus je Seite beibehalten** (alter Title zeigt das Ziel-Keyword). Keine Kannibalisierung: jede Seite behält ihren eigenen Fokus, ähnliche Seiten (z. B. /kupfer/ vs. /kupfer-ankauf-berlin/) differenzieren (eine = Material-Ratgeber, andere = lokale Ankauf-Landingpage).
6. **Länge**: material/landing/district: 500–800 Wörter Fließtext gesamt; die 3 Schwerpunkt-Seiten /edelstahl/, /aluminium/, /mischschrott/: 800–1100 Wörter (Suchvolumen-Chance). legal: Originaltext 1:1 übernehmen (nur HTML-Struktur, KEINE Umformulierung).
7. **Einzugsgebiet**: Abholung in ganz Berlin + Umland + Falkensee; Schrottplatz/Selbstanlieferung in Reinickendorf (Soltauer Straße 27-29).
8. **Zertifikate** (Entsorgungsfachbetrieb §56 KrWG) als Vertrauenssignal erwähnen, exakt wie in fakten.md.
9. Auf Bezirksseiten (schrottplatz-X): klarstellen, dass der Schrottplatz in Reinickendorf liegt und Peglow im Bezirk X ABHOLT — so macht es die alte Seite auch (kein fiktiver Standort im Bezirk!). Lokalbezug über Abholung, Anfahrtsnähe, Bezirks-Eigenheiten.
