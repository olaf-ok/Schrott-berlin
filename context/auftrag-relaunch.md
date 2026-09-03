# Auftrag: Relaunch schrott-berlin.de

**Kunde:** Peglow Schrott und Metallhandel e.K. (Schrotthandel/Metallankauf, Berlin-Reinickendorf)
**Erteilt:** 2026-08-12
**Modus:** Autonom, keine Rückfragen, Entscheidungen selbst treffen + im Abschlussbericht dokumentieren. Bis zu 3 Self-Review-Runden vor Präsentation.

## Kontext
- Aktuelle Seite: WordPress/Elementor, Hosting Mittwald (mStudio)
- Struktur: Startseite, 16 Bezirks-/Einzugsgebiets-Seiten (Berlin + Umland + Falkensee), Material-Seiten (Kupfer, Messing, Zink, Blei, Kabel, Eisen, Altmetall), Service-Seiten (Schrott-Ankauf, Metall-Ankauf, Schrottpreise, Container, Schrott verkaufen, Einzugsgebiete), Stellenanzeigen
- SEO: ~1.000 organische Keywords, ~1.900 Sichtbarkeits-Traffic/Monat, steigend
- **Kritisch — Redirect-Ziel-URLs, MÜSSEN 1:1 erhalten bleiben:** /altmetall-berlin/, /altmetall-ankauf/, /altmetall-ankauf-berlin/, /schrotthandel/, /metall-ankauf-berlin/
- Content-Lücken → neue SEO-Seiten: **Edelstahl-Ankauf** (SV ~2.900), **Aluminium-Ankauf** (~2.400), **Mischschrott** (~1.900)
- Top-Rankings erhalten/verbessern: schrott ankauf berlin, berlin schrotthandel, schrottplatz berlin, altmetall verkaufen, messing ankauf berlin (Platz 1), schrottpreise, schrotthändler in der nähe, kupfer preis pro kg

## Auftrag (Kurzfassung)
1. **Original NICHT anfassen.** Kein Deployment, keine Änderung an Produktion/Hosting/DNS. Nur in diesem Projektordner arbeiten.
2. **Bestandsaufnahme zuerst:** Komplette Seite crawlen (Sitemap + interne Links): Texte, Bilder, Meta-Title/Description, Überschriften, Schema-Markup, interne Verlinkung, Formulare, Öffnungszeiten, NAP → vollständiges Content-/URL-Inventar VOR dem Neubau.
3. **Technischer Neuaufbau:** moderner Stack (freie Wahl, nicht an WP/Elementor gebunden), schnelle CWV, semantisches HTML, Mobile-First, Barrierefreiheit. Stack-Wahl im Bericht begründen.
4. **Jede URL exakt erhalten** (gleiche Pfade/Slugs). Falls Wegfall zwingend: 301-Mapping dokumentieren.
5. **SEO erhalten + verbessern:** Titles, Descriptions, H1-Struktur, interne Verlinkung, sitemap.xml, robots.txt, Canonicals, Alt-Texte, CWV. + 3 neue Material-Seiten.
6. **GEO-Schwerpunkt:**
   - Schema.org komplett: LocalBusiness/Organization (NAP, Öffnungszeiten, Geo, Logo, Social), Service/Product auf Material-Seiten, FAQPage überall relevant, BreadcrumbList
   - KI-zitierbare Inhalte: abgeschlossene Absätze, Preis-/Ablauf-Infos in Listen/Tabellen/FAQ
   - FAQ-Block (3-5 Fragen) auf jeder Material-/Service-Seite
   - robots.txt: KI-Crawler explizit erlauben (GPTBot, PerplexityBot, ClaudeBot, Google-Extended, CCBot)
   - llms.txt im Root (Angebot, Standort, Einzugsgebiet, Preise/Ablauf, wichtigste Unterseiten)
   - Konsistente NAP/Fakten auf jeder Seite (Entity-Vertrauen)
7. **Design/Content:** Ton, Kernaussagen, Bildsprache übernehmen. Sprachlich verbessern erlaubt, Fakten erhalten, keine Fakten erfinden, Annahmen kennzeichnen.

## Arbeitsweise
- Mehrere spezialisierte Subagenten parallel: (a) Crawl/Inventar, (b) SEO-Struktur, (c) GEO/Structured Data, (d) Frontend-Build je Seitentyp, (e) QA/Test (Links, Ladezeit, mobil, Schema-Validierung)
- Review-Agent prüft gegen Checkliste (URL-Erhalt, SEO, GEO, Technik, Content-Treue, Design) → Mängel beheben → bis zu 3 Zyklen oder mängelfrei
- Automatisierte Checks am Ende: Linkcheck, Lighthouse/CWV, Schema-Validator, Screenshot-Vergleich alt/neu je Seitentyp

## Erwartetes Ergebnis
- Lokale, lauffähige, vollständige neue Version (nicht live)
- Abschlussbericht (Markdown): URL-Mapping alt→neu, Stack-Entscheidung + Begründung, SEO-Checkliste, GEO-Checkliste, neue Seiten, Annahmen, offene Punkte vor Livegang, Ergebnis der Review-Runden
- Kein Deployment, keine DNS-/Hosting-Änderung, keine Löschung der alten Seite
