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


def head(title, desc, path, extra='', body='', og='/og.jpg'):
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
<meta name="color-scheme" content="light">
<meta name="darkreader-lock">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Mochi Moose">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="/assets/fonts/fredoka-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/nunito-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css?v=3">
{extra}</head>
<body{' class="' + body + '"' if body else ''}>
<a class="skip" href="#main" data-i18n="skip">Skip to content</a>
<header class="top"><div class="wrap">
  <a class="brand" href="/" aria-label="Mochi Moose, home"><img src="/assets/img/moose.svg" alt="" width="46" height="42"><span>Mochi <b>Moose</b></span></a>
  <nav class="nav" aria-label="Main"><a href="/#games" data-i18n="navGames">Games</a><a class="hide-s" href="/#about" data-i18n="navAbout">About</a><a href="/support"{' aria-current="page"' if path == '/support' else ''} data-i18n="navSupport">Support</a></nav>
  <div class="lang" role="group" aria-label="Language"><button type="button" data-lang="en" aria-pressed="true">EN</button><button type="button" data-lang="es" aria-pressed="false">ES</button><button type="button" data-lang="pt" aria-pressed="false">PT</button></div>
</div></header>
'''


def foot(scripts=()):
    return f'''<footer class="foot"><div class="wrap">
  <div>
    <a class="brand" href="/" aria-label="Mochi Moose, home"><img src="/assets/img/moose.svg" alt="" width="52" height="48"><span>Mochi <b>Moose</b></span></a>
    <p data-i18n="footTag">Tiny studio, big smiles. Cozy games for the whole family.</p>
  </div>
  <nav aria-label="Footer"><a href="/solitaire-bible-3d">Solitaire Bible 3D</a><a href="/dawn-of-civilizations">Dawn of Civilizations</a><a href="/support" data-i18n="navSupport">Support</a><a href="/privacy" data-i18n="footPriv">Privacy</a><a href="/terms" data-i18n="footTerms">Terms</a><a href="mailto:{EMAIL}">{EMAIL}</a></nav>
  <div class="fine"><span>© 2026 Mochi Moose. <span data-i18n="rights">All rights reserved.</span></span><span>mochimoose.com</span></div>
</div></footer>
{''.join(f'<script src="{x}" defer></script>' for x in scripts)}<script src="/assets/js/site.js?v=2" defer></script>
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

<section class="sec" id="games" style="padding-top:16px">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow" data-i18n="gamesEyebrow">Our games</span><h2 data-i18n="gamesTitle">Pick a world</h2><p data-i18n="gamesSub">Classic card games you already love, with a tiny 3D world waiting behind every win.</p></div>
    <div class="tiles">
      <a class="tile sb" href="/solitaire-bible-3d">
        <img src="/assets/img/sb-redsea-1280.webp" srcset="/assets/img/sb-redsea-640.webp 640w, /assets/img/sb-redsea-1280.webp 1280w" sizes="(min-width: 900px) 540px, 100vw" alt="" width="1280" height="720">
        <div class="ttop"><img src="/assets/img/sb-icon-256.webp" alt="Solitaire Bible 3D app icon" width="64" height="64"><span class="pill" data-i18n="tileSbStatus">Launching October 2026</span></div>
        <div class="in">
          <h3><small data-i18n="tileSolitaire">Solitaire</small>Bible 3D</h3>
          <p data-i18n="tileSbTag">Win a hand of Klondike and watch a Bible story come alive, from Creation to Easter.</p>
          <div class="plats"><span data-i18n="platPT">Phones &amp; tablets</span><span>Android</span><span data-i18n="platFire">Fire tablets</span><span>iPhone &amp; iPad</span></div>
          <span class="btn go"><span data-i18n="tileSbBtn">Explore the game</span> <span aria-hidden="true">→</span></span>
        </div>
      </a>
      <a class="tile dawn" href="/dawn-of-civilizations">
        <img src="/assets/img/civ-egypt-1280.webp" srcset="/assets/img/civ-egypt-640.webp 640w, /assets/img/civ-egypt-1280.webp 1280w" sizes="(min-width: 900px) 540px, 100vw" alt="" width="1280" height="720">
        <div class="ttop"><span></span><span class="pill soon" data-i18n="badge">Coming soon</span></div>
        <div class="in">
          <h3><small data-i18n="tileSolitaire">Solitaire</small>Dawn of Civilizations</h3>
          <p data-i18n="tileDawnTag">Win hands to build the first cities of the ancient world and watch empires rise across the map.</p>
          <div class="plats"><span data-i18n="platPT">Phones &amp; tablets</span><span>Android</span><span data-i18n="platFire">Fire tablets</span><span>iPhone &amp; iPad</span></div>
          <span class="btn go"><span data-i18n="tileDawnBtn">Take a peek</span> <span aria-hidden="true">→</span></span>
        </div>
      </a>
    </div>
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
''' + foot(['/assets/js/i18n-home.js?v=2'])


STORIES = ["Creation", "The Garden of Eden", "Noah's Ark", "The Tower of Babel", "Abraham and Sarah", "Jacob and Esau", "Joseph and His Brothers",
           "Baby Moses and the Burning Bush", "The Plagues of Egypt", "Crossing the Red Sea", "The Golden Calf", "The Twelve Spies", "Balaam's Donkey",
           "The Walls of Jericho", "Gideon", "Samson", "Boy Samuel", "David and Goliath", "David Dances", "King Solomon", "Elijah", "Elisha",
           "Jonah and the Big Fish", "The Fiery Furnace", "The Writing on the Wall", "Daniel in the Lions' Den", "The Valley of Dry Bones",
           "The First Christmas", "Lost in the Temple", "John the Baptist", "Water into Wine", "Nets and Waves", "Feeding the 5,000", "Zacchaeus",
           "Lazarus", "The King: Palm Sunday to Easter"]


def sb_page():
    shots = [('sb-redsea', 'c1', 'Crossing the Red Sea'), ('sb-noah', 'c2', "Noah's Ark"), ('sb-goliath', 'c3', 'David and Goliath'),
             ('sb-jericho', 'c4', 'The walls of Jericho'), ('sb-jonah', 'c5', 'Jonah and the big fish'), ('sb-nativity', 'c6', 'The first Christmas'),
             ('sb-finale', 'c7', 'The grand finale')]
    gal = '\n'.join(f'      <li><figure>{pic(n, c)}<figcaption data-i18n="sb{k}">{c}</figcaption></figure></li>' for n, k, c in shots)
    stories = ''.join(f'<li data-i18n="st{i}">{t}</li>' for i, t in enumerate(STORIES))
    crosses = [(13, 'Legendary'), (49, 'Legendary'), (5, 'Epic'), (98, 'Legendary'), (12, 'Epic'), (44, 'Legendary'), (4, 'Rare'), (14, 'Legendary')]
    rar = {'Legendary': 'rarL', 'Epic': 'rarE', 'Rare': 'rarR'}
    xs = ''.join(f'<li style="--i:{j}"><img src="/assets/img/crosses/cross-{i}.svg" alt="" width="110" height="154" loading="lazy"><span data-i18n="{rar[r]}">{r}</span></li>' for j, (i, r) in enumerate(crosses))
    feats = [('f1', 'Verses read aloud', 'f1d', 'Real Bible verses after every win, read aloud in English, Spanish and Portuguese.'),
             ('f2', 'Classical music', 'f2d', 'Bach, Handel, Haydn, Vivaldi and Pachelbel play while you think.'),
             ('f3', 'Day and night', 'f3d', 'The sky follows your own clock, so evening games glow under the stars.'),
             ('f4', 'Spin and zoom', 'f4d', 'Push the cards aside to turn, tilt and zoom around each little world.'),
             ('f5', 'Classic Klondike', 'f5d', 'Draw 1 or Draw 3, unlimited undo, hints and deals you can always win.'),
             ('f6', 'Stuck? Skip it', 'f6d', 'Spend manna or watch a short video to move on to a fresh hand.'),
             ('f7', 'Upright or sideways', 'f7d', 'Big, clear cards for phones and tablets, held either way.'),
             ('f8', '38 languages', 'f8d', 'Play in your language, from Spanish and Portuguese to Swahili and Korean.')]
    feat = ''.join(f'<li><b data-i18n="{a}">{b}</b><span data-i18n="{c}">{d}</span></li>' for a, b, c, d in feats)
    clouds = ''.join(f'<span class="cloud" style="width:{w}px;height:{h}px;top:{t}%;animation-duration:{d}s;animation-delay:-{dl}s"></span>' for w, h, t, d, dl in [(160, 44, 8, 46, 5), (120, 34, 20, 60, 30), (200, 54, 13, 72, 50)])
    title = 'Solitaire Bible 3D · Mochi Moose'
    desc = 'Classic Klondike solitaire where every win brings a Bible story to life in a tiny 3D world. 36 stories, 221 moments, 100 hidden crosses.'
    return head(title, desc, '/solitaire-bible-3d', body='pg-sb', og='/og-sb.jpg') + f'''<main id="main">
<section class="g-hero">
  <img class="bg" src="/assets/img/sb-finale-1280.webp" alt="" width="1280" height="720" fetchpriority="high">
  {clouds}
  <div class="wrap">
    <div><a class="back" href="/#games"><span aria-hidden="true">←</span> <span data-i18n="allGames">All games</span></a></div>
    <div class="sb-logo" role="img" aria-label="Solitaire Bible 3D"><span class="s">SOLITAIRE</span><span class="b">Bible<span class="d">3D</span></span></div>
    <div style="text-align:center;display:grid;gap:18px;justify-items:center">
      <span class="sb-status"><i></i><span data-i18n="sbStatus">Launching October 2026</span></span>
      <p class="lead" data-i18n="sbLead">Win a hand of classic Klondike and watch the next moment of a Bible story come alive, from the first day of Creation to Easter morning.</p>
      <div class="stores">{store('sb.play', 'phone', 'Google Play')}{store('sb.amazon', 'tablet', 'Amazon Appstore')}{store('sb.apple', 'phone', 'iPhone &amp; iPad')}</div>
      <p class="devices">{ICON['phone']}{ICON['tablet']}<span data-i18n="sbDevices">For phones and tablets: Android, Fire tablets, iPhone and iPad</span></p>
    </div>
  </div>
</section>

<section class="g-sec">
  <div class="wrap">
    <div class="g-head"><h2 data-i18n="howTitle">Play a hand. Watch the story.</h2><p data-i18n="howSub">The relaxing card game you know, with a whole world waiting behind the cards.</p></div>
    <div class="device"><img src="/assets/img/sb-play-1280.webp" srcset="/assets/img/sb-play-640.webp 640w, /assets/img/sb-play-1280.webp 1280w" sizes="(min-width: 1000px) 960px, 94vw" width="1280" height="640" loading="lazy" alt="A hand of solitaire over the parting of the Red Sea"></div>
    <ol class="steps">
      <li><b data-i18n="s1t">Play a hand</b><span data-i18n="s1">Classic Klondike with big, friendly cards.</span></li>
      <li><b data-i18n="s2t">Win it</b><span data-i18n="s2">Every win moves the story one moment forward.</span></li>
      <li><b data-i18n="s3t">Watch it come alive</b><span data-i18n="s3">The sea parts, the walls fall, the giant tumbles.</span></li>
    </ol>
  </div>
</section>

<section class="g-sec" style="padding-top:24px">
  <div class="wrap">
    <div class="g-head"><h2 data-i18n="stTitle">36 stories, 221 moments</h2><p data-i18n="stSub">Tiny living worlds built to look like the real places, full of people, animals and everyday life.</p></div>
    <ul class="gal" aria-label="Scenes from the game">
{gal}
    </ul>
    <ul class="chipcloud">{stories}</ul>
  </div>
</section>

<section class="g-sec">
  <div class="wrap split">
    <img class="scroll-img" src="/assets/img/sb-saying-900.webp" width="900" height="563" loading="lazy" alt="A saying of Jesus on a parchment scroll, with a painting by James Tissot">
    <div>
      <h2 data-i18n="vTitle">Words that stay with you</h2>
      <p data-i18n="vSub">After every win, a real Bible verse appears on a parchment scroll and is read aloud.</p>
      <ul>
        <li data-i18n="v1">Tap Jesus and the Bible heroes to collect their sayings</li>
        <li data-i18n="v2">Each saying comes with a painting by James Tissot</li>
        <li data-i18n="v3">Share any verse or saying with someone you love</li>
      </ul>
    </div>
  </div>
</section>

<section class="heaven g-sec">
  <div class="wrap">
    <div class="g-head"><h2 data-i18n="xTitle">100 hidden crosses</h2><p data-i18n="xSub">Beautiful necklace crosses are hidden all over the stories: on trees, on houses, carried by birds. Some are easy to spot. Some you'll have to turn the world to find.</p></div>
    <ul class="crosses">{xs}</ul>
    <div class="split" style="margin-top:56px">
      <img class="gift" src="/assets/img/sb-gift-540.webp" width="540" height="675" loading="lazy" alt="A gift card with a golden cross and the note: I love you, Mom!">
      <div>
        <h2 data-i18n="gTitle">Gift one to someone special</h2>
        <p data-i18n="gSub">Unlock a cross with manna, then gift it once, ever, with your own handwritten note.</p>
        <ul>
          <li data-i18n="g1">Common, rare, epic and legendary crosses</li>
          <li data-i18n="g2">See every cross and saying in My Collection</li>
          <li data-i18n="g3">A golden share button, good for one special share</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="g-sec">
  <div class="wrap">
    <div class="g-head"><h2 data-i18n="fTitle">Made to relax</h2></div>
    <ul class="feat">{feat}</ul>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <h2 data-i18n="ctaTitle">Coming this October</h2>
    <p class="devices dark">{ICON['phone']}{ICON['tablet']}<span data-i18n="sbDevices">For phones and tablets: Android, Fire tablets, iPhone and iPad</span></p>
    <div class="stores">{store('sb.play', 'phone', 'Google Play')}{store('sb.amazon', 'tablet', 'Amazon Appstore')}{store('sb.apple', 'phone', 'iPhone &amp; iPad')}</div>
    <div class="legal-links"><a href="/privacy" data-i18n="legalPriv">Privacy policy</a> · <a href="/terms" data-i18n="legalTerms">Terms of use</a> · <a href="/support" data-i18n="navSupport">Support</a></div>
  </div>
</section>
</main>
''' + foot(['/assets/js/i18n-sb.js?v=2'])


def dawn_page():
    civs = [('civ-sumer', 'cv1', 'Sumer', 'cv1s', 'The first cities'), ('civ-egypt', 'cv2', 'Egypt', 'cv2s', 'Pyramids on the Nile'),
            ('civ-assyria', 'cv3', 'Assyria', 'cv3s', 'Mighty Nineveh'), ('civ-babylon', 'cv4', 'Babylon', 'cv4s', 'The great city on the Euphrates')]
    civ = '\n'.join(f'        <li><figure>{pic(n, t)}<figcaption><b data-i18n="{k}">{t}</b> · <span data-i18n="{ks}">{s}</span></figcaption></figure></li>' for n, k, t, ks, s in civs)
    minds = [('Imhotep', 'fl. c. 2650 BC', 'm1', 'Architect of the first pyramid, later honored as a great healer.', '#e8a51a', 'I'),
             ('Sargon of Akkad', 'c. 2334–2279 BC', 'm2', 'Built one of the first empires in history.', '#f08a3c', 'S'),
             ('Enheduanna', 'fl. c. 2300 BC', 'm3', 'Priestess of Ur and the earliest author we know by name.', '#3aa0d8', 'E'),
             ('Hammurabi', 'c. 1792–1750 BC', 'm4', 'Carved his famous laws in stone “so that the strong should not harm the weak.”', '#4a6fd1', 'H'),
             ('Hatshepsut', 'c. 1479–1458 BC', 'm5', 'A woman pharaoh who sent great trading ships to the land of Punt.', '#e8a51a', 'H'),
             ('Thutmose III', '1479–1425 BC', 'm6', 'A general-pharaoh who won the Battle of Megiddo.', '#c8683a', 'T'),
             ('Ramesses II', '1279–1213 BC', 'm7', 'Fought at Kadesh, then made one of the oldest known peace treaties.', '#9a6a3e', 'R'),
             ('Puduhepa', 'c. 1275–1245 BC', 'm8', 'A Hittite queen and diplomat who helped keep that peace.', '#9b7bea', 'P')]
    mind = ''.join(f'<li><div class="who"><span class="ini" style="--c:{c}">{i}</span><div><b>{n}</b><small data-i18n="{k}d">{d}</small></div></div><span data-i18n="{k}">{t}</span></li>' for n, d, k, t, c, i in minds)
    treasures = ['Royal Game of Ur', 'Standard of Ur', 'Narmer Palette', 'Code of Hammurabi', 'Cylinder seals', 'Clay tablets', 'Queen Puabi’s crown',
                 'Warka Vase', 'Bust of Nefertiti', 'Mask of Tutankhamun', 'Lion Gate of Hattusa', 'Copper ingots of Uluburun']
    tre = ''.join(f'<li data-i18n="tr{i}">{t}</li>' for i, t in enumerate(treasures))
    title = 'Solitaire Dawn of Civilizations · Mochi Moose'
    desc = 'Coming soon from Mochi Moose: win hands of solitaire to build the first cities of the ancient Middle East and watch empires rise and fall.'
    return head(title, desc, '/dawn-of-civilizations', body='pg-dawn', og='/og-dawn.jpg') + f'''<main id="main">
<section class="g-hero">
  <img class="bg" src="/assets/img/civ-egypt-1280.webp" alt="" width="1280" height="720" fetchpriority="high">
  <div class="wrap">
    <div><a class="back" href="/#games"><span aria-hidden="true">←</span> <span data-i18n="allGames">All games</span></a></div>
    <div class="dawn-logo" role="img" aria-label="Solitaire Dawn of Civilizations"><small>Solitaire</small><b>Dawn of Civilizations</b></div>
    <div style="text-align:center;display:grid;gap:18px;justify-items:center">
      <span class="badge" data-i18n="badge">Coming soon</span>
      <p class="lead" data-i18n="dLead">Our cozy little people travel back to the very beginning of history. Win hands of solitaire to build the first cities, and watch empires rise and fall across the ancient Middle East.</p>
      <a class="btn" href="mailto:{EMAIL}?subject=Dawn%20of%20Civilizations">{ICON['bell']}<span data-i18n="dawnBtn">Tell me when it's ready</span></a>
      <p class="devices">{ICON['phone']}{ICON['tablet']}<span data-i18n="dawnDevices">Coming to phones and tablets: Android, Fire tablets, iPhone and iPad</span></p>
    </div>
  </div>
</section>
<div class="frieze" aria-hidden="true"></div>

<section class="g-sec">
  <div class="wrap">
    <div class="g-head"><h2 data-i18n="mTitle">Watch the ancient world come alive</h2><p data-i18n="mSub">Start with an empty map. Villages appear, then cities, then kingdoms and empires, over more than 8,000 years.</p></div>
    <div class="mapbox" id="dawnMap"><div class="hud"><span class="year" id="mapYear">9,600 BC</span><span class="cap" id="mapCap"></span></div></div>
    <div class="mapctl"><button type="button" id="mapPlay" aria-pressed="true" aria-label="Play or pause"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 4v16l13-8z"/></svg></button><input type="range" id="mapRange" aria-label="Year"><span data-i18n="mDrag">Drag through time</span></div>
    <ul class="maplegend"><li style="--c:#3aa0d8"><i></i>Sumer</li><li style="--c:#f08a3c"><i></i>Akkad</li><li style="--c:#e8a51a"><i></i><span data-i18n="cv2">Egypt</span></li><li style="--c:#4a6fd1"><i></i><span data-i18n="cv4">Babylon</span></li><li style="--c:#d0503c"><i></i><span data-i18n="cv3">Assyria</span></li><li style="--c:#9a6a3e"><i></i><span data-i18n="lHit">Hittites</span></li><li style="--c:#9b7bea"><i></i>Mitanni</li><li style="--c:#4fb06a"><i></i>Elam</li></ul>
  </div>
</section>

<section class="g-sec" style="padding-top:12px">
  <div class="wrap">
    <div class="g-head"><h2 data-i18n="hTitle">How it plays</h2></div>
    <ol class="steps">
      <li><b data-i18n="h1t">See the whole map</b><span data-i18n="h1">Time moves forward and the map fills with towns, roads, trade and kingdoms.</span></li>
      <li><b data-i18n="h2t">Fly down into history</b><span data-i18n="h2">The birth of a city, a new invention, a famous battle, a great trade fair.</span></li>
      <li><b data-i18n="h3t">Win hands to play it forward</b><span data-i18n="h3">Each win moves the moment on, from the first villages to the great collapse.</span></li>
    </ol>
  </div>
</section>

<section class="g-sec">
  <div class="wrap split">
    <img class="scroll-img" src="/assets/img/dawn-battle-1280.webp" srcset="/assets/img/dawn-battle-640.webp 640w, /assets/img/dawn-battle-1280.webp 1280w" sizes="(min-width: 900px) 540px, 94vw" width="1280" height="720" loading="lazy" alt="Two armies of little soldiers clash on a green hill, seen from high above">
    <div>
      <h2 data-i18n="bTitle">A bird’s-eye view of history</h2>
      <p data-i18n="bSub">High above the world, you see it all: markets and caravans, builders and farmers, and armies of tiny soldiers charging across the hills.</p>
      <ul>
        <li data-i18n="b1">The first cities, temples and pyramids</li>
        <li data-i18n="b2">Trade by donkey caravan, river boat and ship</li>
        <li data-i18n="b3">Great battles like Megiddo and Kadesh</li>
      </ul>
    </div>
  </div>
</section>

<section class="g-sec" style="padding-top:12px">
  <div class="wrap">
    <div class="g-head"><h2 data-i18n="cTitle">Four great civilizations, and many more</h2></div>
    <ul class="gal" aria-label="Civilizations">
{civ}
    </ul>
  </div>
</section>

<section class="g-sec">
  <div class="wrap">
    <div class="g-head"><h2 data-i18n="kTitle">Meet the great minds</h2><p data-i18n="kSub">Kings and queens, builders, writers and lawgivers. Tap them in the game to collect words from real ancient texts.</p></div>
    <ul class="minds">{mind}</ul>
  </div>
</section>

<section class="g-sec" style="padding-top:12px">
  <div class="wrap">
    <div class="g-head"><h2 data-i18n="tTitle">Treasures to find</h2><p data-i18n="tSub">Hidden in every age: real wonders from the museums of the world. (No coins yet: people paid in silver, weighed in shekels. Coins came much later!)</p></div>
    <ul class="chipcloud treasures">{tre}</ul>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <h2 data-i18n="dCta">Be the first to play</h2>
    <div class="stores" style="margin-top:18px"><a class="btn pink" href="mailto:{EMAIL}?subject=Dawn%20of%20Civilizations">{ICON['bell']}<span data-i18n="dawnBtn">Tell me when it's ready</span></a></div>
  </div>
</section>
</main>
''' + foot(['/assets/js/i18n-dawn.js?v=2', '/assets/js/dawn-land.js?v=2', '/assets/js/dawn-map.js?v=2'])


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
    write('solitaire-bible-3d.html', sb_page())
    write('dawn-of-civilizations.html', dawn_page())
    write('privacy.html', doc_page('/privacy', 'privTitle', 'Privacy Policy',
          'How Mochi Moose games and this website handle information: no accounts, progress stays on your device, family-safe ads by Google AdMob.', PRIVACY))
    write('terms.html', doc_page('/terms', 'termsTitle', 'Terms of Use', 'The terms for playing Mochi Moose games, including Solitaire Bible 3D.', TERMS))
    write('support.html', doc_page('/support', 'supTitle', 'Support', 'Get help with Mochi Moose games: contact us, restore purchases, delete your data and more.', SUPPORT,
          "We're here to help.", 'supSub'))
    write('404.html', notfound())
