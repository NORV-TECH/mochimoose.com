# mochimoose.com

The Mochi Moose studio website, served by GitHub Pages from the `main` branch (custom domain in `CNAME`).

- `index.html`, `solitaire-bible-3d.html`, `dawn-of-civilizations.html`, `privacy.html`, `terms.html`, `support.html`, `404.html` are generated. Edit `tools/build.py` (layout, home page) and `tools/legal.py` (privacy, terms, support text in English, Spanish and Portuguese), then run `python3 tools/build.py`.
- Translations (Spanish, Portuguese): shared strings and the store links in `assets/js/site.js`; page strings in `assets/js/i18n-home.js`, `i18n-sb.js`, `i18n-dawn.js`.
- Dawn of Civilizations living map: `assets/js/dawn-map.js` (cities, empires, dates) over `assets/js/dawn-land.js` (Natural Earth 1:50m coastline, public domain). A store button turns into a real link as soon as its URL is filled in `STORES`.
- `app-ads.txt` is the AdMob seller file (publisher `pub-9507665972378426`).
- Fonts: Fredoka and Nunito (SIL Open Font License, see `assets/fonts/OFL-*.txt`), served from the site itself.
- Game scenes are rendered from the Solitaire Bible 3D engine.
