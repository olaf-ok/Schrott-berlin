"""HTML-Templates für den statischen Generator (Relaunch schrott-berlin.de).
Nur Python-Stdlib. Alle Funktionen geben Strings zurück."""
import html
import json


def esc(s):
    return html.escape(str(s or ""), quote=True)


# Feine Stroke-Icons (Feather-Stil, ISC-Lizenz), inline ohne CDN
_ICON_PATHS = {
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "chat": '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "arrow": '<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>',
    "mobile": '<rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/>',
    "chev-left": '<polyline points="15 18 9 12 15 6"/>',
    "chev-right": '<polyline points="9 18 15 12 9 6"/>',
}

# WhatsApp-Markenlogo (Simple Icons, CC0) – gefüllt statt Stroke
_WHATSAPP_PATH = ('M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164'
                  '-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297'
                  '-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52'
                  '-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074'
                  '-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487'
                  '.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248'
                  '-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214'
                  '-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122'
                  ' 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815'
                  ' 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654'
                  'a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z')


_BRAND_PATHS = {
    "facebook": '<path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>',
    "instagram": '<path d="M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913.306.788.717 1.459 1.384 2.126.667.666 1.336 1.079 2.126 1.384.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558.788-.306 1.459-.718 2.126-1.384.666-.667 1.079-1.335 1.384-2.126.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913-.306-.789-.718-1.459-1.384-2.126C21.319 1.347 20.651.935 19.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227-.224.562-.479.96-.899 1.382-.419.419-.824.679-1.38.896-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421-.569-.224-.96-.479-1.379-.899-.421-.419-.69-.824-.9-1.38-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06l.045.03zm0 3.678c-3.405 0-6.162 2.76-6.162 6.162 0 3.405 2.76 6.162 6.162 6.162 3.405 0 6.162-2.76 6.162-6.162 0-3.405-2.76-6.162-6.162-6.162zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405c0 .795-.646 1.44-1.44 1.44-.795 0-1.44-.646-1.44-1.44 0-.794.646-1.439 1.44-1.439.793-.001 1.44.645 1.44 1.439z"/>',
}


def icon_brand(name, cls="ic ic-brand"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="currentColor" '
            f'aria-hidden="true">{_BRAND_PATHS[name]}</svg>')


def icon_whatsapp(cls="ic"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="currentColor" '
            f'aria-hidden="true"><path d="{_WHATSAPP_PATH}"/></svg>')


def icon(name, cls="ic"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{_ICON_PATHS[name]}</svg>')


# ---------------------------------------------------------------- JSON-LD ---

def jsonld_graph(page, site, img_dims):
    """Erzeugt den @graph mit LocalBusiness, WebSite, WebPage, Breadcrumb,
    optional Service und FAQPage."""
    dom = site["domain"]
    c = site["company"]
    url = dom + page["path"]
    biz_id = dom + "/#business"
    site_id = dom + "/#website"

    business = {
        "@type": ["RecyclingCenter", "LocalBusiness"],
        "@id": biz_id,
        "name": c["legal_name"],
        "alternateName": c["brand"],
        "url": dom + "/",
        "logo": {"@type": "ImageObject", "url": dom + "/img/LOGO_neu-Out-line.png",
                 "width": 352, "height": 132},
        "image": dom + "/img/schrott-berlin-head-01.webp",
        "telephone": c["phone_intl"],
        "faxNumber": c["fax_intl"],
        "email": c["email"],
        "vatID": c["vat_id"],
        "founder": {"@type": "Person", "name": c["owner"]},
        "address": {
            "@type": "PostalAddress",
            "streetAddress": c["street"],
            "postalCode": c["zip"],
            "addressLocality": c["city"],
            "addressRegion": "Berlin",
            "addressCountry": "DE",
        },
        "geo": {"@type": "GeoCoordinates",
                "latitude": c["geo"]["lat"], "longitude": c["geo"]["lng"]},
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "08:00", "closes": "17:00",
        }],
        "areaServed": [
            {"@type": "City", "name": "Berlin"},
            {"@type": "City", "name": "Falkensee"},
            {"@type": "State", "name": "Brandenburg"},
        ],
        "priceRange": "$$",
        "currenciesAccepted": "EUR",
        "sameAs": c["sameAs"],
    }

    website = {
        "@type": "WebSite", "@id": site_id, "url": dom + "/",
        "name": site["site_name"], "publisher": {"@id": biz_id}, "inLanguage": "de",
    }

    webpage = {
        "@type": "WebPage", "@id": url + "#webpage", "url": url,
        "name": page["title"], "description": page.get("meta_description", ""),
        "isPartOf": {"@id": site_id}, "about": {"@id": biz_id}, "inLanguage": "de",
    }
    hero = page.get("hero_image")
    if hero:
        webpage["primaryImageOfPage"] = {"@type": "ImageObject", "url": f"{dom}/img/{hero}"}

    graph = [business, website, webpage]

    bc = page.get("breadcrumb") or []
    if bc:
        graph.append({
            "@type": "BreadcrumbList", "@id": url + "#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": name,
                 "item": dom + href}
                for i, (name, href) in enumerate(bc)
            ],
        })

    svc = page.get("service_schema")
    if svc:
        graph.append({
            "@type": "Service", "@id": url + "#service",
            "name": svc.get("name", page["h1"]),
            "serviceType": svc.get("serviceType", ""),
            "description": svc.get("description", ""),
            "provider": {"@id": biz_id},
            "areaServed": [{"@type": "City", "name": "Berlin"},
                           {"@type": "City", "name": "Falkensee"}],
            "url": url,
        })

    faq = page.get("faq") or []
    if faq:
        graph.append({
            "@type": "FAQPage", "@id": url + "#faq",
            "mainEntity": [
                {"@type": "Question", "name": f["q"],
                 "acceptedAnswer": {"@type": "Answer", "text": f["a"]}}
                for f in faq
            ],
        })

    data = {"@context": "https://schema.org", "@graph": graph}
    return ('<script type="application/ld+json">'
            + json.dumps(data, ensure_ascii=False, separators=(",", ":"))
            + "</script>")


# ------------------------------------------------------------- Bausteine ---

def img_tag(fname, alt, site, img_dims, cls="", lazy=True, fetchpriority=None):
    w, h = img_dims.get(fname, (None, None))
    dim = f' width="{w}" height="{h}"' if w else ""
    lz = ' loading="lazy" decoding="async"' if lazy else ""
    fp = f' fetchpriority="{fetchpriority}"' if fetchpriority else ""
    cl = f' class="{cls}"' if cls else ""
    return f'<img src="/img/{esc(fname)}" alt="{esc(alt)}"{dim}{lz}{fp}{cl}>'


def breadcrumb_html(page):
    bc = page.get("breadcrumb") or []
    if len(bc) < 2:
        return ""
    items = []
    for i, (name, href) in enumerate(bc):
        if i == len(bc) - 1:
            items.append(f'<li aria-current="page">{esc(name)}</li>')
        else:
            items.append(f'<li><a href="{esc(href)}">{esc(name)}</a></li>')
    return f'<nav class="breadcrumb" aria-label="Brotkrümelnavigation"><ol>{"".join(items)}</ol></nav>'


def checklist_html(page):
    items = page.get("checklist") or []
    if not items:
        return ""
    lis = "".join(f"<li>{esc(i)}</li>" for i in items)
    return f'<div class="checklist-wrap"><ul class="checklist">{lis}</ul></div>'


def table_html(page):
    t = page.get("table")
    if not t or not t.get("rows"):
        return ""
    head = "".join(f"<th scope=\"col\">{esc(h)}</th>" for h in t.get("head", []))
    rows = "".join(
        "<tr>" + "".join(f"<td>{esc(c)}</td>" for c in row) + "</tr>"
        for row in t["rows"]
    )
    cap = f"<caption>{esc(t['caption'])}</caption>" if t.get("caption") else ""
    return (f'<div class="table-wrap"><table>{cap}'
            f"<thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>")


def sections_html(page, only=None, skip=None):
    out = []
    for s in page.get("sections") or []:
        if only and not s["heading"].startswith(only):
            continue
        if skip and s["heading"].startswith(skip):
            continue
        out.append(f'<section class="content-section"><h2>{esc(s["heading"])}</h2>{s["html"]}</section>')
    return "".join(out)


def faq_html(page):
    faq = page.get("faq") or []
    if not faq:
        return ""
    items = "".join(
        f"<details{' open' if i == 0 else ''}><summary>{esc(f['q'])}</summary>"
        f"<div class=\"faq-a\"><p>{esc(f['a'])}</p></div></details>"
        for i, f in enumerate(faq)
    )
    return (f'<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Häufige Fragen</h2>'
            f'<div class="faq-list">{items}</div></section>')


def related_html(page):
    rel = page.get("related") or []
    if not rel:
        return ""
    cards = "".join(
        f'<a class="rel-card" href="{esc(href)}"><span>{esc(label)}</span><span class="rel-arrow">{icon("arrow")}</span></a>'
        for label, href in rel
    )
    return (f'<section class="related" aria-labelledby="rel-h"><h2 id="rel-h">Das könnte Sie auch interessieren</h2>'
            f'<div class="rel-grid">{cards}</div></section>')


def cta_html(page, site):
    c = site["company"]
    heading = page.get("cta_heading") or "Schrott oder Metall zu verkaufen?"
    text = page.get("cta_text") or ("Rufen Sie uns an – wir nennen Ihnen sofort den "
                                    "tagesaktuellen Preis und organisieren auf Wunsch die Abholung.")
    return f'''<section class="cta-band">
  <div class="container cta-inner">
    <div>
      <h2>{esc(heading)}</h2>
      <p>{esc(text)}</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-light" href="tel:{esc(c["phone_intl"])}">{icon("phone")} {esc(c["phone_display"])}</a>
      <a class="btn btn-outline" href="/kontakt/">Nachricht schreiben</a>
    </div>
  </div>
</section>'''


def hero_h1(page, big=True):
    """H1 unverändert im Wortlaut; zweizeilig mit Magenta-Akzent (Split an – oder :)."""
    h1 = page["h1"]
    if " – " in h1:
        pre, post = h1.split(" – ", 1)
        return f'<h1>{esc(pre)}<br><span class="h1-accent">{esc(post)}</span></h1>'
    if ": " in h1:
        pre, post = h1.split(": ", 1)
        return f'<h1>{esc(pre)}:<br><span class="h1-accent">{esc(post)}</span></h1>'
    return f"<h1>{esc(page['h1'])}</h1>"


def hero_html(page, site, img_dims, big=False):
    kicker = page.get("hero_kicker") or "Schrottplatz Berlin-Reinickendorf"
    text = page.get("hero_text") or ""
    hero = page.get("hero_image")
    img = ""
    if hero:
        img = img_tag(hero, "", site, img_dims, cls="hero-img", lazy=False, fetchpriority="high")
    actions = ""
    if page.get("template") not in ("legal", "danke"):
        actions = (f'<div class="hero-actions"><a class="btn btn-primary" '
                   f'href="tel:{esc(site["company"]["phone_intl"])}">{icon("phone")} Jetzt Preis erfragen</a></div>')
    cls = "hero hero-big"
    badge = ('<div class="hero-badge" aria-hidden="true">Geprüfter<br>Entsorgungs-<br>fachbetrieb<br>'
             '<span>§56 KrWG</span></div>')
    return f'''<div class="hero-wrap"><div class="{cls}">
  {img}
  <div class="hero-panel">
    <p class="kicker">{esc(kicker)}</p>
    {hero_h1(page, big)}
    {f'<p class="hero-text">{esc(text)}</p>' if text else ''}
    {actions}
  </div>
  {badge}
</div></div>'''


def stats_html(page):
    stats = page.get("stats") or []
    if not stats:
        return ""
    chips = "".join(
        f'<div class="stat-chip"><div class="stat-num">{esc(n)}</div><div class="stat-label">{esc(l)}</div></div>'
        for n, l in stats
    )
    return f'<section class="stats" aria-label="Peglow in Zahlen">{chips}</section>'


def materials_grid_html(page, site, img_dims):
    mats = page.get("materials") or []
    if not mats:
        return ""
    h = page.get("materials_heading") or ["Das kaufen wir an.", ""]
    heading = "".join(h) if isinstance(h, list) else h
    kicker = page.get("materials_kicker") or "Metall-Ankauf · Tagespreis am Telefon"
    def card(m, dup=False):
        extra = ' aria-hidden="true" tabindex="-1"' if dup else ""
        return (f'<a class="mat-card" href="{esc(m["href"])}"{extra}>'
                f'{img_tag(m["img"], esc(m["name"]) + "-Schrott – Ankauf bei Peglow Berlin", site, img_dims)}'
                f'<span class="mat-stripe">{esc(m["name"])}</span></a>')

    # Kartensatz doppelt für nahtlose Endlos-Schleife (Duplikate sind rein dekorativ)
    cards = "".join(card(m) for m in mats) + "".join(card(m, dup=True) for m in mats)
    dots = "".join(
        f'<button type="button" class="car-dot{" is-active" if i == 0 else ""}" data-i="{i}"'
        f' aria-label="Zu {esc(m["name"])}"></button>'
        for i, m in enumerate(mats)
    )
    return f'''<section class="mat-section" aria-labelledby="mat-h">
  <p class="kicker kicker-dark">{esc(kicker)}</p>
  <h2 id="mat-h">{esc(heading)}</h2>
  <div class="mat-carousel peg-carousel" data-count="{len(mats)}" tabindex="0" aria-label="Materialien – horizontal scrollbar">{cards}</div>
  <div class="car-controls" hidden>
    <div class="car-dots" role="tablist" aria-label="Position im Karussell">{dots}</div>
    <button type="button" class="car-arrow car-prev" aria-label="Zurück">{icon("chev-left")}</button>
    <button type="button" class="car-arrow car-next" aria-label="Weiter">{icon("chev-right")}</button>
  </div>
</section>'''


def intro_owner_html(page, site, img_dims):
    """Intro-Text links, Inhaber-Foto mit Namens-Plakette rechts."""
    oi = page.get("owner_image")
    intro = f'<div class="intro intro-lg">{page.get("intro", "")}</div>'
    if not oi:
        return intro
    return f'''<div class="intro-grid">
  {intro}
  <figure class="owner-card">
    {img_tag(oi["src"], oi["alt"], site, img_dims)}
    <figcaption class="owner-plaque">
      <img src="/img/LOGO_neu-Out-line.png" alt="" width="64" height="24" loading="lazy">
      <span><span class="owner-name">{esc(oi["name"])}</span><span class="owner-role">{esc(oi["role"])}</span></span>
    </figcaption>
  </figure>
</div>'''


def steps_html(page):
    steps = page.get("steps") or []
    if not steps:
        return ""
    items = "".join(
        f'<li class="step-card"><span class="step-num" aria-hidden="true">{i + 1}</span>'
        f'<h3>{esc(s["title"])}</h3><p>{s["html"]}</p></li>'
        for i, s in enumerate(steps)
    )
    footer = f'<p class="steps-footer">{page["steps_footer"]}</p>' if page.get("steps_footer") else ""
    return f'''<section class="steps-section" aria-labelledby="steps-h">
  <h2 id="steps-h">{esc(page.get("steps_heading", "So funktioniert es"))}</h2>
  <ol class="steps">{items}</ol>
  {footer}
</section>'''


def reviews_html(page, site):
    """Google-Bewertungen als Karussell (statisch eingebettet, Quelle: Google/Trustindex)."""
    reviews = page.get("reviews") or site.get("reviews") or []
    if not reviews:
        return ""
    if not page.get("reviews_link") and site.get("reviews_link"):
        page = dict(page, reviews_link=site["reviews_link"])
    star = ('<svg class="star" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
            '<path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>')

    def rcard(r, dup=False):
        extra = ' aria-hidden="true"' if dup else ""
        stars = f'<span class="rev-stars" role="img" aria-label="{r["stars"]} von 5 Sternen">{star * r["stars"]}</span>'
        return (f'<figure class="rev-card"{extra}>{stars}'
                f'<blockquote>{esc(r["text"])}</blockquote>'
                f'<figcaption>{esc(r["name"])}<span>via Google</span></figcaption></figure>')

    cards = "".join(rcard(r) for r in reviews) + "".join(rcard(r, dup=True) for r in reviews)
    dots = "".join(
        f'<button type="button" class="car-dot{" is-active" if i == 0 else ""}" data-i="{i}"'
        f' aria-label="Bewertung {i + 1}"></button>'
        for i in range(len(reviews))
    )
    link = page.get("reviews_link", "")
    more = (f'<a class="rev-more" href="{esc(link)}" rel="noopener" target="_blank">'
            f'Alle Bewertungen auf Google {icon("arrow", "ic ic-sm")}</a>') if link else ""
    return f'''<section class="rev-section" aria-labelledby="rev-h">
  <p class="kicker kicker-dark">Google-Bewertungen</p>
  <h2 id="rev-h">{esc(page.get("reviews_heading", "Das sagen unsere Kunden"))}</h2>
  <div class="rev-carousel peg-carousel" data-count="{len(reviews)}" tabindex="0" aria-label="Kundenbewertungen – horizontal scrollbar">{cards}</div>
  <div class="car-controls" hidden>
    {more}
    <div class="car-dots" role="tablist" aria-label="Position im Karussell">{dots}</div>
    <button type="button" class="car-arrow car-prev" aria-label="Zurück">{icon("chev-left")}</button>
    <button type="button" class="car-arrow car-next" aria-label="Weiter">{icon("chev-right")}</button>
  </div>
</section>'''


def container_feature_html(page, site, img_dims):
    cf = page.get("container_feature")
    if not cf:
        return ""
    checks = "".join(f'<li>{esc(c)}</li>' for c in cf.get("checklist", []))
    return f'''<section class="feature" aria-labelledby="feat-h">
  <div class="feature-img">{img_tag(cf["image"], "Peglow-LKW mit Absetzcontainer", site, img_dims)}</div>
  <div class="feature-body">
    <p class="kicker kicker-dark">{esc(cf.get("kicker", ""))}</p>
    <h2 id="feat-h">{esc(cf["heading_pre"])}<span class="accent">{esc(cf["heading_accent"])}</span>{esc(cf["heading_post"])}</h2>
    <ul class="feature-checks">{checks}</ul>
    <p class="feature-actions">
      <a class="btn btn-primary" href="tel:{esc(site["company"]["phone_intl"])}">{icon("phone")} Container anfragen</a>
      <a class="feature-more" href="{esc(cf["more_href"])}">{esc(cf["more_label"])} {icon("arrow", "ic ic-sm")}</a>
    </p>
  </div>
</section>'''


def nap_box(site, img_dims=None, contact_btn=True):
    c = site["company"]
    wa_url = f'https://wa.me/{esc(c["whatsapp_intl"].lstrip("+"))}'
    buttons = ""
    if contact_btn:
        buttons = f'<a class="btn btn-primary" href="/kontakt/">Kontaktformular</a>'
    return f'''<aside class="nap-box" aria-label="Kontakt und Öffnungszeiten">
  <p class="kicker kicker-dark">Anfahrt &amp; Öffnungszeiten</p>
  <h2>{esc(c["legal_name"])}</h2>
  <address>
    {esc(c["street"])}<br>{esc(c["zip"])} {esc(c["city"])} ({esc(c["district"])})
  </address>
  <p class="nap-line">{icon("phone")} <a href="tel:{esc(c["phone_intl"])}"><strong>{esc(c["phone_display"])}</strong></a></p>
  <p class="nap-line">{icon("mobile")} <a href="tel:{esc(c["whatsapp_intl"])}">{esc(c["whatsapp"])}</a></p>
  <p class="nap-line">{icon("mail")} <a href="mailto:{esc(c["email"])}">{esc(c["email"])}</a></p>
  <p class="nap-line">{icon("clock")} Mo–Fr <strong>8–17 Uhr</strong></p>
  <div class="nap-actions">
    {buttons}
    <a class="btn btn-wa" href="{wa_url}">{icon_whatsapp()} WhatsApp</a>
  </div>
</aside>'''


# ---------------------------------------------------------------- Layout ---

HEADER_NAV = [
    ["Ankauf", "/schrott-ankauf/"],
    ["Schrottpreise", "/schrottpreise/"],
    ["Container", "/container/"],
    ["Bezirke", "/einzugsgebiete/"],
    ["Anfahrt", "/anfahrt/"],
    ["Kontakt", "/kontakt/"],
]


def header_html(site, active_path):
    c = site["company"]
    aria_current = ' aria-current="page"'
    nav_items = "".join(
        f'<li><a href="{esc(href)}"{aria_current if href == active_path else ""}>{esc(label)}</a></li>'
        for label, href in HEADER_NAV
    )
    return f'''<a class="skip-link" href="#main">Zum Inhalt springen</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="/" aria-label="Peglow Schrott und Metall – Startseite">
      <img src="/img/LOGO_neu-Out-line.png" alt="Logo Peglow Schrott &amp; Metall" width="176" height="66">
    </a>
    <input type="checkbox" id="nav-toggle" class="nav-toggle" aria-hidden="true">
    <label for="nav-toggle" class="nav-burger" aria-hidden="true"><span></span><span></span><span></span><span class="sr-only">Menü</span></label>
    <nav class="main-nav" aria-label="Hauptnavigation"><ul>{nav_items}</ul></nav>
    <a class="btn btn-primary header-cta" href="tel:{esc(c["phone_intl"])}">{icon("phone")} {esc(c["phone_display"])}</a>
  </div>
</header>'''


def sticky_bar_html(site):
    c = site["company"]
    return f'''<div class="sticky-bar" role="complementary" aria-label="Schnellkontakt">
  <a class="sticky-call" href="tel:{esc(c["phone_intl"])}">{icon("phone")} Anrufen</a>
  <a class="sticky-wa" href="https://wa.me/{esc(c["whatsapp_intl"].lstrip('+'))}">{icon("chat")} WhatsApp</a>
</div>'''


def footer_html(site):
    c = site["company"]
    cols = ""
    for col in site["footer_cols"]:
        links = "".join(f'<li><a href="{esc(h)}">{esc(l)}</a></li>' for l, h in col["links"])
        cols += f'<div class="f-col"><h2>{esc(col["title"])}</h2><ul>{links}</ul></div>'
    certs = "".join(f"<li>{esc(x)}</li>" for x in c["certificates"])
    return f'''<footer class="site-footer">
  <div class="container footer-grid">
    {cols}
    <div class="f-col f-contact">
      <h2>Kontakt</h2>
      <address>
        <strong>{esc(c["legal_name"])}</strong><br>
        {esc(c["street"])}<br>{esc(c["zip"])} {esc(c["city"])}-{esc(c["district"])}
      </address>
      <ul class="f-nap">
        <li><a href="tel:{esc(c["phone_intl"])}">{icon("phone")} {esc(c["phone_display"])}</a></li>
        <li>Fax: {esc(c["fax"])}</li>
        <li><a href="https://wa.me/{esc(c["whatsapp_intl"].lstrip('+'))}">{icon("chat")} WhatsApp {esc(c["whatsapp"])}</a></li>
        <li><a href="mailto:{esc(c["email"])}">{icon("mail")} {esc(c["email"])}</a></li>
        <li>{icon("clock")} {esc(c["opening"])}</li>
      </ul>
      <div class="f-social">
        <a href="{esc(c["sameAs"][0])}" rel="noopener" target="_blank" aria-label="Peglow auf Facebook">{icon_brand("facebook")}</a>
        <a href="{esc(c["sameAs"][1])}" rel="noopener" target="_blank" aria-label="Peglow auf Instagram">{icon_brand("instagram")}</a>
      </div>
    </div>
  </div>
  <div class="container f-certs">
    <p>Zertifizierter Entsorgungsfachbetrieb (oecontrol Technische Überwachungsorganisation GmbH):</p>
    <ul>{certs}</ul>
  </div>
  <div class="f-bottom">
    <div class="container f-bottom-inner">
      <p>© 2026 {esc(c["legal_name"])} – Wir gehören zum alten Eisen.</p>
      <ul>
        <li><a href="/impressum/">Impressum</a></li>
        <li><a href="/datenschutz/">Datenschutz</a></li>
        <li><a href="/kontakt/">Kontakt</a></li>
      </ul>
    </div>
  </div>
</footer>'''


CAROUSEL_JS = """<script>
document.querySelectorAll('.peg-carousel').forEach(function (c) {
  var ctr = c.nextElementSibling;
  if (!ctr || !ctr.classList.contains('car-controls')) ctr = null;
  if (ctr) ctr.hidden = false;
  var n = parseInt(c.dataset.count, 10);
  var cards = c.children;
  if (!n || !cards.length) return;
  function step() {
    var gap = parseFloat(getComputedStyle(c).columnGap) || 16;
    return cards[0].offsetWidth + gap;
  }
  function loopWidth() { return step() * n; }
  function idx() { return Math.round(c.scrollLeft / step()) % n; }
  var last = 0, pos = null;
  function touched() { last = Date.now(); pos = null; }
  function go(i) {
    touched();
    c.scrollTo({ left: i * step(), behavior: 'smooth' });
  }
  ['pointerdown', 'wheel', 'touchstart', 'keydown'].forEach(function (ev) {
    c.addEventListener(ev, touched, { passive: true });
  });
  if (ctr) {
    var dots = ctr.querySelectorAll('.car-dot');
    ctr.querySelector('.car-prev').addEventListener('click', function () { go((idx() - 1 + n) % n); });
    ctr.querySelector('.car-next').addEventListener('click', function () { go(idx() + 1); });
    dots.forEach(function (d) {
      d.addEventListener('click', function () { go(parseInt(d.dataset.i, 10)); });
    });
    c.addEventListener('scroll', function () {
      var i = idx();
      dots.forEach(function (d, j) { d.classList.toggle('is-active', j === i); });
    }, { passive: true });
  }
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var prev = null;
    function frame(ts) {
      if (prev !== null && !document.hidden && Date.now() - last > 2500) {
        if (pos === null) pos = c.scrollLeft;
        pos += Math.min(ts - prev, 100) * 0.032;
        if (pos >= loopWidth()) pos -= loopWidth();
        c.scrollLeft = pos;
      }
      prev = ts;
      requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  } else {
    c.addEventListener('scroll', function () {
      if (c.scrollLeft >= loopWidth()) c.scrollLeft -= loopWidth();
    }, { passive: true });
  }
});
</script>"""


def base(page, site, img_dims, body, noindex=False, extra_head=""):
    dom = site["domain"]
    url = dom + page["path"]
    robots = '<meta name="robots" content="noindex, follow">' if noindex else ""
    hero = page.get("hero_image")
    og_img = f"{dom}/img/{hero}" if hero else f"{dom}/img/schrott-berlin-head-01.webp"
    preload = (f'<link rel="preload" as="image" href="/img/{esc(hero)}" fetchpriority="high">'
               if hero else "")
    um = site.get("umami") or {}
    umami = (f'<script defer src="{esc(um["src"])}" data-website-id="{esc(um["website_id"])}"></script>'
             if um.get("src") and um.get("website_id") else "")
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(page["title"])}</title>
<meta name="description" content="{esc(page.get("meta_description", ""))}">
{robots}<link rel="canonical" href="{esc(url)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(site["site_name"])}">
<meta property="og:locale" content="de_DE">
<meta property="og:title" content="{esc(page["title"])}">
<meta property="og:description" content="{esc(page.get("meta_description", ""))}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:image" content="{esc(og_img)}">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/img/LOGO_neu-Out-line.png" type="image/png">
<link rel="stylesheet" href="/css/style.css">
{preload}{umami}{extra_head}
{jsonld_graph(page, site, img_dims)}
</head>
<body>
{header_html(site, page["path"])}
<main id="main">
{body}
</main>
{footer_html(site)}
{sticky_bar_html(site)}
{CAROUSEL_JS}
</body>
</html>'''


# --------------------------------------------------------------- Seiten ----

def map_card_html(site, img_dims):
    """Statische Einzugsgebiets-Karte + Google-Maps-Routenlink (kein Embed, kein Cookie)."""
    route = ("https://www.google.com/maps/dir/?api=1&destination="
             "Soltauer+Stra%C3%9Fe+27-29%2C+13509+Berlin")
    return f'''<figure class="map-card">
  <img src="/img/karte-einzugsgebiet.webp" alt="Stadtkarte von Berlin und Umgebung mit dem Standort von Peglow Schrott und Metall in Reinickendorf" width="1238" height="957" loading="lazy" decoding="async">
  <a class="btn btn-primary map-btn" href="{route}" rel="noopener" target="_blank">{icon("pin")} Route in Google Maps öffnen</a>
</figure>'''


def wo_peglow_html(page, site, img_dims):
    """'Wo ist Peglow'-Sektion: Text links, Einzugsgebiets-Karte rechts (50/50)."""
    sec = next((s for s in page.get("sections", []) if s["heading"].startswith("Wo ist Peglow")), None)
    if not sec:
        return ""
    return f'''<section class="wo-grid" aria-labelledby="wo-h">
  <div><h2 id="wo-h">{esc(sec["heading"])}</h2>{sec["html"]}</div>
  {map_card_html(site, img_dims)}
</section>'''


def faq_nap_html(page, site, img_dims):
    """FAQ + NAP-Karte/Karte zweispaltig 50/50."""
    return f'''<div class="faq-nap">
  <div>{faq_html(page)}</div>
  <div class="nap-col">
    {nap_box(site, img_dims)}
  </div>
</div>'''


# Bild-Pools für 50/50-Sektionen (Startseiten-Rhythmus auf Unterseiten)
SECTION_ALT_TEXTS = {
    "Fahrerseite_mit_Container_schraeg_2.webp": "Peglow-LKW mit Absetzcontainer bei der Schrottabholung in Berlin",
    "bagger2.webp": "Bagger verlädt Metallschrott auf dem Schrottplatz von Peglow in Reinickendorf",
    "Gabelstapler-fahren.webp": "Gabelstapler im Einsatz auf dem Peglow-Schrottplatz",
    "Gabelstapler-Heizung.webp": "Gabelstapler transportiert alte Heizkörper zum Wiegen",
    "Schere.webp": "Schrottschere zerkleinert Metallschrott bei Peglow",
    "Container.webp": "Absetzcontainer für Schrott und Metall von Peglow",
    "absetzcontainer-540x200.webp": "Absetzcontainer in verschiedenen Größen",
    "gebaeude311-z.webp": "Betriebsgebäude von Peglow Schrott und Metall mit Graffiti-Logo",
    "geldschein.webp": "Barauszahlung beim Schrott-Ankauf nach tagesaktuellen Preisen",
    "kupfer_milberry.webp": "Blanker Kupferdraht (Millberry) beim Ankauf",
    "kupfer_raff.webp": "Kupfer-Raff: gebrauchte Kupferrohre und -bleche",
    "messing.webp": "Messing-Schrott: Armaturen und Fittings",
    "messing_raff.webp": "Messing-Raff beim Metall-Ankauf",
    "zink.webp": "Zink-Schrott: Dachrinnen und Bleche",
    "blei-header.webp": "Blei-Schrott beim Ankauf",
    "blei-teaser.webp": "Bleiplatten und Altblei",
    "kabel-1.webp": "Kabelschrott mit Kupferadern",
    "kabel-e1556089444211.webp": "Alte Kabel und Leitungen beim Ankauf",
    "Alu_Guss.webp": "Aluminium-Guss-Teile beim Ankauf",
    "Alu_Guss_01.webp": "Aluminium-Guss: Felgen und Motorenteile",
    "schrott_guss.webp": "Gusseisen-Schrott auf dem Schrottplatz",
    "schrott_guss-1.webp": "Guss-Schrott beim Ankauf",
    "metalle_edelstahl_01.webp": "Edelstahl-Schrott: V2A- und V4A-Teile",
    "aluminum-scrap-e1557150174466.webp": "Aluminium-Schrott vor der Verwertung",
    "aluminum-scrap-1024x683.jpg.webp": "Sortierter Metallschrott",
    "construction-material-grid-metal-35543.webp": "Eisen- und Stahlschrott",
    "moniereisen_01.webp": "Moniereisen und Bewehrungsstahl",
    "bremsscheiben.webp": "Alte Bremsscheiben beim Ankauf",
    "brennerschrott.webp": "Brennerschrott und Heizkessel",
    "schienen.webp": "Eisenbahnschienen als Schwerschrott",
    "philip-peglow-schrottplatz.webp": "Inhaber Philip Peglow auf dem Schrottplatz in Berlin-Reinickendorf",
    "aktuelle-schrottpreise-berlin.webp": "Aktuelle Schrottpreise: Vergütung nach Tageskurs",
}

# Zweites Materialbild je Seite (Hero nicht wiederholen)
MATERIAL_ALT_IMG = {
    "kupfer": "kupfer_raff.webp", "kupfer-raff": "kupfer_milberry.webp",
    "kupfer-ankauf-berlin": "kupfer_milberry.webp",
    "messing": "messing_raff.webp", "messing-raff": "messing.webp", "messing-schrott": "messing_raff.webp",
    "zink": "alloy-aluminum-close-up-1427292.webp", "zink-ankauf-berlin": "zink.webp",
    "blei": "blei-teaser.webp", "blei-ankauf": "blei-header.webp",
    "kabel": "kabel-1.webp", "kabel-schrott": "kabel-e1556089444211.webp",
    "aluminium": "Alu_Guss_01.webp", "aluminium-guss": "Alu_Guss.webp",
    "guss": "schrott_guss-1.webp", "eisen-schrott": "moniereisen_01.webp",
    "edelstahl": "abstract-honeycomb-metal-5294.webp", "mischschrott": "schrott_guss.webp",
    "bremsscheiben": "bremsscheiben.webp", "moniereisen": "moniereisen_01.webp",
    "brennerschrott": "brennerschrott.webp", "schienen": "schienen.webp",
    "schrottpreise": "geldschein.webp", "container": "absetzcontainer-540x200.webp",
    "uber-uns": "philip-peglow-schrottplatz.webp", "peglow-schrott": "gebaeude311-z.webp",
}

OPS_POOL = ["Fahrerseite_mit_Container_schraeg_2.webp", "bagger2.webp", "Gabelstapler-fahren.webp",
            "Schere.webp", "geldschein.webp", "Container.webp", "gebaeude311-z.webp",
            "Gabelstapler-Heizung.webp"]


def pick_section_images(page):
    slug = page.get("_slug") or (page["path"].strip("/").replace("/", "-") or "home")
    hero = page.get("hero_image")
    cands = []
    if slug in MATERIAL_ALT_IMG:
        cands.append(MATERIAL_ALT_IMG[slug])
    h = sum(ord(c) for c in slug)
    rot = h % len(OPS_POOL)
    cands += OPS_POOL[rot:] + OPS_POOL[:rot]
    out = []
    for c in cands:
        if c != hero and c not in out:
            out.append(c)
    return out


def sections_features_html(page, site, img_dims):
    """Sektionen im Startseiten-Rhythmus: jede zweite als 50/50-Block mit Bild."""
    secs = page.get("sections") or []
    imgs = pick_section_images(page)
    parts = []
    img_i = 0
    for i, s in enumerate(secs):
        html_body = s["html"]
        # Lange Linklisten zweispaltig
        if html_body.count("<li>") > 8:
            html_body = html_body.replace("<ul>", '<ul class="list-cols">', 1)
        if i % 2 == 1 and img_i < len(imgs):
            img = imgs[img_i]
            img_i += 1
            flip = " feature-flip" if img_i % 2 == 0 else ""
            alt = SECTION_ALT_TEXTS.get(img, "Peglow Schrott und Metall Berlin")
            parts.append(
                f'<section class="feature feature-sec{flip}">'
                f'<div class="feature-img">{img_tag(img, alt, site, img_dims)}</div>'
                f'<div class="feature-body"><h2>{esc(s["heading"])}</h2>{html_body}</div>'
                f"</section>")
        else:
            parts.append(f'<section class="content-section"><h2>{esc(s["heading"])}</h2>{html_body}</section>')
    return "".join(parts)


def render_standard(page, site, img_dims):
    """material / landing / district / service / company – gemeinsames Muster."""
    if page.get("show_map"):
        intro_block = (f'<div class="wo-grid intro-map"><div><div class="intro">{page.get("intro", "")}</div></div>'
                       f'{map_card_html(site, img_dims)}</div>')
    else:
        intro_block = f'<div class="intro">{page.get("intro", "")}</div>'
    reviews = reviews_html(page, site) if page.get("show_reviews") else ""
    body = f'''{hero_html(page, site, img_dims)}
<div class="container page-body">
  {breadcrumb_html(page)}
  {intro_block}
  {checklist_html(page)}
  {sections_features_html(page, site, img_dims)}
  {table_html(page)}
  {reviews}
</div>
{cta_html(page, site)}
<div class="container page-body">
  {faq_nap_html(page, site, img_dims)}
  {related_html(page)}
</div>'''
    return base(page, site, img_dims, body)


def render_home(page, site, img_dims):
    body = f'''{hero_html(page, site, img_dims, big=True)}
<div class="container page-body">
  {stats_html(page)}
  {intro_owner_html(page, site, img_dims)}
  {materials_grid_html(page, site, img_dims)}
  {steps_html(page)}
  {sections_html(page, only="Unsere Leistungen")}
  {container_feature_html(page, site, img_dims)}
  {checklist_html(page)}
  {sections_html(page, only="Warum Peglow")}
  {reviews_html(page, site)}
  {wo_peglow_html(page, site, img_dims)}
  {table_html(page)}
  {faq_nap_html(page, site, img_dims)}
  {related_html(page)}
</div>'''
    return base(page, site, img_dims, body)


def render_contact(page, site, img_dims):
    c = site["company"]
    body = f'''{hero_html(page, site, img_dims)}
<div class="container page-body">
  {breadcrumb_html(page)}
  <div class="intro">{page.get("intro", "")}</div>
  <div class="contact-grid">
    <div class="nap-col">{nap_box(site, contact_btn=False)}{map_card_html(site, img_dims) if page.get("show_map") else ""}</div>
    <form class="contact-form" action="/contact.php" method="post">
      <h2>Kontaktformular</h2>
      <p class="form-hint">Felder mit * sind Pflichtfelder.</p>
      <div class="field"><label for="cf-name">Name *</label>
        <input id="cf-name" name="name" type="text" required autocomplete="name"></div>
      <div class="field"><label for="cf-email">E-Mail *</label>
        <input id="cf-email" name="email" type="email" required autocomplete="email"></div>
      <div class="field"><label for="cf-subject">Betreff / Material</label>
        <input id="cf-subject" name="subject" type="text"></div>
      <div class="field"><label for="cf-message">Ihre Nachricht *</label>
        <textarea id="cf-message" name="message" rows="6" required></textarea></div>
      <div class="field field-hp"><label for="cf-website">Website</label>
        <input id="cf-website" name="website" type="text" tabindex="-1" autocomplete="off"></div>
      <div class="field field-check">
        <input id="cf-privacy" name="privacy" type="checkbox" required>
        <label for="cf-privacy">Ich akzeptiere die <a href="/datenschutz/">Datenschutzerklärung</a>. *</label>
      </div>
      <button class="btn btn-primary" type="submit">Nachricht senden</button>
    </form>
  </div>
  {sections_html(page)}
  {faq_html(page)}
  {related_html(page)}
</div>'''
    return base(page, site, img_dims, body)


def render_legal(page, site, img_dims):
    intro = page.get("intro", "")
    intro_block = f'<div class="intro">{intro}</div>' if intro else ""
    body = f'''{hero_html(page, site, img_dims)}
<div class="container page-body page-narrow">
  {breadcrumb_html(page)}
  {intro_block}
  {sections_html(page)}
</div>'''
    return base(page, site, img_dims, body)


def render_danke(page, site, img_dims):
    body = f'''<div class="container page-body page-narrow danke">
  <h1>{esc(page["h1"])}</h1>
  <div class="intro">{page.get("intro", "")}</div>
  {sections_html(page)}
  <p><a class="btn btn-primary" href="/">Zur Startseite</a>
     <a class="btn btn-outline" href="/schrottpreise/">Aktuelle Schrottpreise</a></p>
</div>'''
    return base(page, site, img_dims, body, noindex=True)


def render_jobs(page, site, img_dims):
    body = f'''{hero_html(page, site, img_dims)}
<div class="container page-body">
  {breadcrumb_html(page)}
  <div class="intro">{page.get("intro", "")}</div>
  {sections_features_html(page, site, img_dims)}
  {checklist_html(page)}
</div>
{cta_html(page, site)}
<div class="container page-body">
  {faq_nap_html(page, site, img_dims)}
  {related_html(page)}
</div>'''
    return base(page, site, img_dims, body)


RENDERERS = {
    "home": render_home,
    "material": render_standard,
    "landing": render_standard,
    "district": render_standard,
    "service": render_standard,
    "company": render_standard,
    "contact": render_contact,
    "legal": render_legal,
    "danke": render_danke,
    "jobs": render_jobs,
}


def render_page(page, site, img_dims):
    fn = RENDERERS.get(page.get("template", "landing"), render_standard)
    return fn(page, site, img_dims)


def render_404(site, img_dims):
    page = {
        "path": "/404.html", "template": "danke",
        "title": "Seite nicht gefunden | Peglow Schrott und Metall Berlin",
        "meta_description": "Diese Seite existiert nicht (mehr). Hier finden Sie unsere wichtigsten Seiten rund um Schrott- und Metall-Ankauf in Berlin.",
        "h1": "Seite nicht gefunden (404)",
    }
    body = f'''<div class="container page-body page-narrow danke">
  <h1>Seite nicht gefunden</h1>
  <div class="intro"><p>Die aufgerufene Seite gibt es leider nicht (mehr). Vielleicht hilft Ihnen einer dieser Wege weiter:</p></div>
  <ul>
    <li><a href="/">Startseite</a></li>
    <li><a href="/schrott-ankauf/">Schrott-Ankauf Berlin</a></li>
    <li><a href="/schrottpreise/">Aktuelle Schrottpreise</a></li>
    <li><a href="/metall-ankauf/">Metall-Ankauf: alle Materialien</a></li>
    <li><a href="/kontakt/">Kontakt</a></li>
  </ul>
</div>'''
    return base(page, site, img_dims, body, noindex=True)
