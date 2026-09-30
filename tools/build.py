#!/usr/bin/env python3
"""Builds the Mochi Moose site pages (index, privacy, terms, support, 404) from one shared header and footer.
Run from the repo root:  python3 tools/build.py
"""
import os
from legal import PRIVACY, TERMS, SUPPORT, EFFECTIVE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://mochimoose.com'
EMAIL = 'support@mochimoose.com'

ICON = {
  'phone': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="2.5" width="12" height="19" rx="3"/><path d="M10.5 18.5h3"/></svg>',
  'tablet': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3.5" y="3" width="17" height="18" rx="3"/><path d="M10.5 18h3"/></svg>',
  'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="m4 7 8 6 8-6"/></svg>',
  'bell': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20.5a2 2 0 0 0 4 0"/></svg>',
  'shield': '<svg viewBox="0 0 24 24" fill="none" stroke="#2f7a44" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 5 6v5c0 4.5 3 8.2 7 10 4-1.8 7-5.5 7-10V6z"/><path d="m9 12 2 2 4-4"/></svg>',
  'heart': '<svg viewBox="0 0 24 24" fill="none" stroke="#c23d6c" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg>',
  'cloud': '<svg viewBox="0 0 24 24" fill="none" stroke="#1f7fb3" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 18h10a4 4 0 0 0 .6-8A6 6 0 0 0 6 9.5 4.3 4.3 0 0 0 7 18z"/><path d="M4 4l16 16"/></svg>',
  'globe': '<svg viewBox="0 0 24 24" fill="none" stroke="#6b4fc4" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></svg>',
}


def head(title, desc, path, extra=''):
    url = SITE + path
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#FFF8F0">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Mochi Moose">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="/assets/fonts/fredoka-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/nunito-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css?v=1">
{extra}</head>
<body>
<a class="skip" href="#main" data-i18n="skip">Skip to content</a>
<header class="top"><div class="wrap">
  <a class="brand" href="/" aria-label="Mochi Moose, home"><img src="/assets/img/moose.svg" alt="" width="46" height="42"><span>Mochi <b>Moose</b></span></a>
  <nav class="nav" aria-label="Main"><a href="/#games" data-i18n="navGames">Games</a><a class="hide-s" href="/#about" data-i18n="navAbout">About</a><a href="/support"{' aria-current="page"' if path == '/support' else ''} data-i18n="navSupport">Support</a></nav>
  <div class="lang" role="group" aria-label="Language"><button type="button" data-lang="en" aria-pressed="true">EN</button><button type="button" data-lang="es" aria-pressed="false">ES</button><button type="button" data-lang="pt" aria-pressed="false">PT</button></div>
</div></header>
'''


def foot():
    return f'''<footer class="foot"><div class="wrap">
  <div>
    <a class="brand" href="/" aria-label="Mochi Moose, home"><img src="/assets/img/moose.svg" alt="" width="52" height="48"><span>Mochi <b>Moose</b></span></a>
    <p data-i18n="footTag">Tiny studio, big smiles. Cozy games for the whole family.</p>
  </div>
  <nav aria-label="Footer"><a href="/#games" data-i18n="navGames">Games</a><a href="/support" data-i18n="navSupport">Support</a><a href="/privacy" data-i18n="footPriv">Privacy</a><a href="/terms" data-i18n="footTerms">Terms</a><a href="mailto:{EMAIL}">{EMAIL}</a></nav>
  <div class="fine"><span>© 2026 Mochi Moose. <span data-i18n="rights">All rights reserved.</span></span><span>mochimoose.com</span></div>
</div></footer>
<script src="/assets/js/site.js?v=1" defer></script>
</body>
</html>
'''


def store(key, icon, name):
    return (f'<a class="btn soft" data-store="{key}" aria-disabled="true" role="link">{ICON[icon]}'
            f'<span class="two"><small data-i18n="soon">Coming soon</small>{name}</span></a>')


def pic(name, alt, sizes='(min-width: 900px) 360px, 78vw', cls=''):
    return (f'<img{cls} src="/assets/img/{name}-640.webp" srcset="/assets/img/{name}-640.webp 640w, /assets/img/{name}-1280.webp 1280w" '
            f'sizes="{sizes}" width="640" height="360" loading="lazy" decoding="async" alt="{alt}">')


def index():
    shots = [('sb-redsea', 'cap1', 'Crossing the Red Sea', 'Little people in robes walk between two walls of water on the sea floor'),
             ('sb-noah', 'cap2', "Noah's Ark", 'Families line up in front of the big wooden ark on a grassy hill'),
             ('sb-goliath', 'cap3', 'David and Goliath', 'Giant Goliath in bronze armor faces the armies across a stream'),
             ('sb-jericho', 'cap4', 'The walls of Jericho', 'The people march around the walled city of Jericho with priests and soldiers'),
             ('sb-jonah', 'cap5', 'Jonah and the big fish', 'Jonah sits inside the belly of the big blue fish'),
             ('sb-finale', 'cap6', 'The grand finale', 'Everyone from the stories gathers together under a rainbow')]
    shot_html = '\n'.join(f'      <li><figure>{pic(n, alt)}<figcaption data-i18n="{k}">{c}</figcaption></figure></li>' for n, k, c, alt in shots)
    civs = [('civ-sumer', 'civ1', 'Sumer', 'civ1s', 'The first cities', 'A tall stepped tower rising over a sandy plain with builders around it'),
            ('civ-egypt', 'civ2', 'Egypt', 'civ2s', 'Pyramids on the Nile', 'Pyramids and the Sphinx beside the Nile, with the royal court across the river'),
            ('civ-assyria', 'civ3', 'Assyria', 'civ3s', 'Mighty Nineveh', 'The walled city of Nineveh with its towers and palace'),
            ('civ-babylon', 'civ4', 'Babylon', 'civ4s', 'The Ishtar Gate', 'The blue Ishtar Gate and the walls of Babylon with the ziggurat behind')]
    civ_html = '\n'.join(f'        <li><figure>{pic(n, alt, "(min-width: 900px) 250px, 45vw")}<figcaption><b data-i18n="{k}">{t}</b><span data-i18n="{ks}">{s}</span></figcaption></figure></li>' for n, k, t, ks, s, alt in civs)
    bubbles = ''.join(f'<span style="--c:{c};width:{s}px;height:{s}px;left:{x}%;top:{y}%;--d:{d}s;--dl:{dl}s;--x:{dx}px;--y:{dy}px"></span>'
                      for c, s, x, y, d, dl, dx, dy in [('#FFC2D4', 64, 4, 10, 9, 0, 10, -26), ('#BDE6FA', 38, 88, 8, 7, -2, -8, -20), ('#FFE59A', 28, 80, 70, 8, -4, 6, -18),
                                                        ('#CDEFD2', 46, 2, 72, 10, -1, 12, -22), ('#E2D6FF', 22, 50, 4, 6.5, -3, -6, -16), ('#FFD2B8', 18, 94, 44, 7.5, -5, -4, -14)])
    title = 'Mochi Moose · Cozy family games'
    desc = 'Mochi Moose is a tiny, happy game studio making cozy, family-friendly games. Meet Solitaire Bible 3D and the upcoming Solitaire Dawn of Civilizations.'
    ld = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"Mochi Moose","url":"{SITE}","logo":"{SITE}/apple-touch-icon.png","email":"{EMAIL}"}}</script>
'''
    return head(title, desc, '/', ld) + f'''<main id="main">
<section class="hero">
  <div class="blob" style="width:420px;height:420px;background:#FFD1DE;left:-160px;top:-120px"></div>
  <div class="blob" style="width:360px;height:360px;background:#CBEBFB;right:-140px;top:40px"></div>
  <div class="blob" style="width:300px;height:300px;background:#FFF0B8;left:40%;bottom:-180px"></div>
  <div class="wrap">
    <div>
      <span class="kicker"><i></i><span data-i18n="kicker">Hi, we're Mochi Moose!</span></span>
      <h1 data-i18n="h1">Cozy games that bring little <em>worlds</em> to life</h1>
      <p class="lead" data-i18n="lead">We're a tiny, happy game studio. We make relaxing, family-friendly games where every win makes something wonderful happen.</p>
      <div class="cta"><a class="btn" href="#games" data-i18n="ctaGames">Meet our games</a><a class="btn soft" href="mailto:{EMAIL}"><span data-i18n="ctaHello">Say hello</span></a></div>
    </div>
    <div class="mascot" aria-hidden="true"><div class="halo"></div><div class="bubbles">{bubbles}</div><img src="/assets/img/moose.svg" alt="" width="240" height="220"></div>
  </div>
</section>

<section class="sec" id="games" style="padding-top:24px">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow" data-i18n="gamesEyebrow">Our games</span><h2 data-i18n="gamesTitle">Play a hand, watch a story</h2><p data-i18n="gamesSub">Classic card games you already love, with a tiny 3D world waiting behind every win.</p></div>

    <article class="game" aria-labelledby="sb-title">
      <div class="media">{pic('sb-nativity', 'Angels over the shepherds in a tiny 3D Bethlehem from Solitaire Bible 3D', '(min-width: 900px) 600px, 100vw').replace(' loading="lazy"', ' fetchpriority="high"')}</div>
      <div class="info">
        <span class="status"><i></i><span data-i18n="sbStatus">Launching October 2026</span></span>
        <div class="title"><img class="icon" src="/assets/img/sb-icon-256.webp" width="76" height="76" alt="Solitaire Bible 3D app icon"><div><h3 id="sb-title">Solitaire Bible 3D</h3><div class="by" data-i18n="sbBy">Klondike solitaire · 36 Bible stories</div></div></div>
        <p class="desc" data-i18n="sbDesc">Win a hand of classic Klondike and watch the next moment of a Bible story come alive, from the first day of Creation to Easter morning. The Red Sea parts, the walls of Jericho fall and David faces Goliath, all in cozy little 3D worlds you can spin and explore.</p>
        <ul class="chips">
          <li style="--c:var(--butter-soft)" data-i18n="chip1">221 animated moments</li>
          <li style="--c:var(--pink-soft)" data-i18n="chip2">100 hidden crosses to find</li>
          <li style="--c:var(--sky-soft)" data-i18n="chip3">Verses read aloud</li>
          <li style="--c:var(--matcha-soft)" data-i18n="chip4">38 languages</li>
          <li style="--c:var(--lilac-soft)" data-i18n="chip5">Classical music</li>
        </ul>
        <div class="stores">{store('sb.play', 'phone', 'Google Play')}{store('sb.amazon', 'tablet', 'Amazon Appstore')}{store('sb.apple', 'phone', 'iPhone &amp; iPad')}</div>
        <div class="legal-links"><a href="/privacy" data-i18n="legalPriv">Privacy policy</a> · <a href="/terms" data-i18n="legalTerms">Terms of use</a></div>
      </div>
    </article>
    <ul class="shots" aria-label="Scenes from Solitaire Bible 3D">
{shot_html}
    </ul>

    <article class="soon" aria-labelledby="dawn-title" style="margin-top:56px">
      <div class="sun" aria-hidden="true"></div>
      <div class="inner">
        <span class="badge" data-i18n="badge">Coming soon</span>
        <div class="lockup"><small>Solitaire</small><h3 id="dawn-title">Dawn of Civilizations</h3></div>
        <p class="desc" data-i18n="dawnDesc">Our cozy little people are heading back to the very beginning of history. Win hands of solitaire to build the first great cities, watch the map of the ancient world change as empires rise and fall, and collect treasures from the dawn of civilization.</p>
        <p class="desc" style="font-weight:700;font-size:17px" data-i18n="dawnWhere">Coming to Android, Fire tablets, iPhone and iPad.</p>
      </div>
      <ul class="civs">
{civ_html}
      </ul>
      <div class="note"><p data-i18n="dawnNote">Want to know the moment it's out?</p><a class="btn pink" href="mailto:{EMAIL}?subject=Dawn%20of%20Civilizations">{ICON['bell']}<span data-i18n="dawnBtn">Tell me when it's ready</span></a></div>
    </article>
  </div>
</section>

<svg class="wave" viewBox="0 0 1440 48" preserveAspectRatio="none" aria-hidden="true"><path fill="currentColor" d="M0 48V26c120-18 240-26 360-14s240 30 360 26 240-26 360-30 240 8 360 18v22z"/></svg>
<section class="sec band" style="padding-top:28px">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow" data-i18n="famEyebrow">Made for families</span><h2 data-i18n="famTitle">Safe, calm and friendly</h2><p data-i18n="famSub">The kind of game you can hand to anyone in the family.</p></div>
    <ul class="perks">
      <li><span class="ico" style="--c:var(--matcha-soft)">{ICON['shield']}</span><h3 data-i18n="perk1t">No accounts, no chat</h3><p data-i18n="perk1">Nothing to sign up for and no strangers to talk to. Your progress stays on your device.</p></li>
      <li><span class="ico" style="--c:var(--pink-soft)">{ICON['heart']}</span><h3 data-i18n="perk2t">Family-safe ads</h3><p data-i18n="perk2">Ads are limited to family-friendly content, and one small purchase turns them off for good.</p></li>
      <li><span class="ico" style="--c:var(--sky-soft)">{ICON['cloud']}</span><h3 data-i18n="perk3t">Plays offline</h3><p data-i18n="perk3">No internet? No problem. The games work anywhere, on phones and tablets.</p></li>
      <li><span class="ico" style="--c:var(--lilac-soft)">{ICON['globe']}</span><h3 data-i18n="perk4t">In your language</h3><p data-i18n="perk4">Solitaire Bible 3D speaks 38 languages, with Bible verses read aloud in English, Spanish and Portuguese.</p></li>
    </ul>
  </div>
</section>
<svg class="wave" viewBox="0 0 1440 48" preserveAspectRatio="none" aria-hidden="true" style="transform:scaleY(-1)"><path fill="currentColor" d="M0 48V26c120-18 240-26 360-14s240 30 360 26 240-26 360-30 240 8 360 18v22z"/></svg>

<section class="sec" id="about">
  <div class="wrap about">
    <div class="pic" aria-hidden="true"><img src="/assets/img/moose.svg" alt="" width="240" height="220"></div>
    <div>
      <span class="eyebrow" data-i18n="aboutEyebrow">About us</span>
      <h2 data-i18n="aboutTitle">Hi from the moose!</h2>
      <p data-i18n="about1">Mochi Moose is a tiny independent studio. We make games that feel like a warm hug: soft colors, gentle music, little characters with big hearts, and stories worth sharing with the people you love.</p>
      <p data-i18n="about2">Got an idea, found a bug, or just want to say hi? We read every message.</p>
      <div class="cta"><a class="btn pink" href="mailto:{EMAIL}">{ICON['mail']}<span data-i18n="aboutBtn">Email us</span></a></div>
    </div>
  </div>
</section>
</main>
''' + foot()


def doc_page(path, key, title_en, desc, sections, sub_en='', sub_key=''):
    """sections: {'en': html, 'es': html, 'pt': html}"""
    names = {'en': 'English', 'es': 'Español', 'pt': 'Português'}
    bar = ''.join(f'<a href="#{l}" data-lang="{l}" aria-current="{"true" if l == "en" else "false"}">{names[l]}</a>' for l in ('en', 'es', 'pt'))
    body = '\n'.join(f'<article lang="{l}" id="{l}">\n{sections[l]}\n</article>' for l in ('en', 'es', 'pt'))
    sub = f'<p data-i18n="{sub_key}">{sub_en}</p>' if sub_en else ''
    return head(f'{title_en} · Mochi Moose', desc, path) + f'''<main id="main">
<div class="wrap">
  <div class="doc-hero"><h1 data-i18n="{key}" data-title="{key}">{title_en}</h1>{sub}<nav class="langbar" aria-label="Language">{bar}</nav></div>
  <div class="doc">
{body}
  </div>
</div>
</main>
''' + foot()


def notfound():
    return head('Page not found · Mochi Moose', 'This page is hiding.', '/404') + f'''<main id="main">
<div class="wrap nf">
  <img src="/assets/img/moose.svg" alt="" width="240" height="220">
  <h1 data-i18n="nfTitle">Oops! This page is hiding</h1>
  <p data-i18n="nfBody">We looked everywhere, even under the cards, and couldn't find it.</p>
  <a class="btn" href="/" data-i18n="nfBtn">Back to the start</a>
</div>
</main>
''' + foot()


def write(name, html):
    with open(os.path.join(ROOT, name), 'w', encoding='utf-8') as f:
        f.write(html)
    print('wrote', name, len(html) // 1024, 'KB')


if __name__ == '__main__':
    write('index.html', index())
    write('privacy.html', doc_page('/privacy', 'privTitle', 'Privacy Policy',
          'How Mochi Moose games and this website handle information: no accounts, progress stays on your device, family-safe ads by Google AdMob.', PRIVACY))
    write('terms.html', doc_page('/terms', 'termsTitle', 'Terms of Use', 'The terms for playing Mochi Moose games, including Solitaire Bible 3D.', TERMS))
    write('support.html', doc_page('/support', 'supTitle', 'Support', 'Get help with Mochi Moose games: contact us, restore purchases, delete your data and more.', SUPPORT,
          "We're here to help.", 'supSub'))
    write('404.html', notfound())
