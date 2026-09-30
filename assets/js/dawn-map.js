/* Dawn of Civilizations: the living map. Cities appear when they were founded, empires grow and fade,
   from c. 9600 BC to the Bronze Age collapse. Dates follow Wikipedia (middle chronology), rounded. */
(function () {
  var box = document.getElementById('dawnMap'); if (!box || !window.DAWN_LAND) return;
  var L = window.DAWN_LAND, W = L.W, H = L.H, KX = W / 31, KY = KX / Math.cos(32.5 * Math.PI / 180);
  function P(lon, lat) { return [(lon - 24) * KX, (42 - lat) * KY]; }
  var NS = 'http://www.w3.org/2000/svg';
  function el(n, a, p) { var e = document.createElementNS(NS, n); for (var k in a) e.setAttribute(k, a[k]); if (p) p.appendChild(e); return e; }
  function smooth(pts) {            // closed Catmull-Rom through lon/lat points
    var q = pts.map(function (p) { return P(p[0], p[1]); }), n = q.length, d = 'M' + q[0][0].toFixed(1) + ',' + q[0][1].toFixed(1);
    for (var i = 0; i < n; i++) {
      var p0 = q[(i - 1 + n) % n], p1 = q[i], p2 = q[(i + 1) % n], p3 = q[(i + 2) % n];
      d += 'C' + (p1[0] + (p2[0] - p0[0]) / 6).toFixed(1) + ',' + (p1[1] + (p2[1] - p0[1]) / 6).toFixed(1) + ' ' + (p2[0] - (p3[0] - p1[0]) / 6).toFixed(1) + ',' + (p2[1] - (p3[1] - p1[1]) / 6).toFixed(1) + ' ' + p2[0].toFixed(1) + ',' + p2[1].toFixed(1);
    }
    return d + 'Z';
  }
  function line(pts) { return 'M' + pts.map(function (p) { return P(p[0], p[1]).map(function (v) { return v.toFixed(1); }).join(','); }).join('L'); }

  var RIVERS = [
    [[39.6, 39.2], [38.9, 38.7], [38.3, 37.9], [38.0, 36.8], [38.1, 36.0], [39.0, 35.95], [40.15, 35.33], [40.89, 34.55], [41.98, 34.37], [42.82, 33.64], [43.78, 33.35], [44.42, 32.54], [45.23, 32.0], [45.64, 31.32], [46.1, 31.0], [47.0, 30.95], [47.43, 31.0], [47.8, 30.5], [48.5, 29.95]],
    [[39.8, 38.4], [40.23, 37.91], [41.4, 37.6], [42.18, 37.33], [43.15, 36.36], [43.33, 36.1], [43.26, 35.46], [43.68, 34.6], [43.87, 34.2], [44.4, 33.3], [45.1, 32.9], [45.8, 32.5], [46.6, 32.2], [47.15, 31.84], [47.43, 31.0]],
    [[32.9, 23.0], [32.9, 24.1], [32.64, 25.7], [32.73, 26.16], [31.92, 26.4], [31.18, 27.18], [30.87, 27.93], [31.2, 29.2], [31.25, 29.85], [31.24, 30.1], [30.9, 30.5], [30.5, 31.0], [30.4, 31.45]],
    [[31.24, 30.1], [31.5, 30.6], [31.82, 31.45]],
    [[35.6, 33.2], [35.58, 32.8], [35.55, 32.2], [35.5, 31.75]]
  ];
  var EMPIRES = [
    { id: 'sumer', name: 'Sumer', c: '#3aa0d8', from: 4000, to: 2334, lab: [45.9, 31.9], pts: [[48.3, 30.2], [47.2, 31.7], [45.8, 32.9], [44.3, 33.0], [44.2, 32.0], [45.4, 30.9], [46.8, 30.1]] },
    { id: 'akkad', name: 'Akkad', c: '#f08a3c', from: 2334, to: 2154, lab: [43.2, 34.6], pts: [[48.6, 29.8], [47.6, 31.6], [46.6, 33.6], [45.3, 35.8], [43.6, 37.0], [40.6, 37.0], [38.0, 36.4], [38.5, 35.0], [41.0, 34.0], [43.0, 32.4], [45.0, 30.7], [46.9, 29.7]] },
    { id: 'ur3', name: 'Ur', c: '#2f86c9', from: 2112, to: 2004, lab: [45.6, 32.5], pts: [[48.5, 30.0], [47.3, 31.9], [45.8, 34.2], [44.0, 35.8], [43.0, 35.2], [43.6, 33.2], [45.0, 31.0], [46.8, 29.9]] },
    { id: 'oldassyria', name: 'Assyria', c: '#d0503c', from: 2025, to: 1750, lab: [43.3, 35.8], pts: [[44.2, 36.8], [43.6, 35.1], [42.8, 35.2], [42.6, 36.4], [43.3, 36.9]] },
    { id: 'babylon', name: 'Babylon', c: '#4a6fd1', from: 1763, to: 1595, lab: [44.6, 32.4], pts: [[48.3, 30.1], [47.1, 31.8], [45.6, 33.8], [44.2, 34.7], [41.0, 34.8], [40.5, 34.2], [42.5, 33.3], [44.2, 31.6], [46.6, 30.0]] },
    { id: 'kassite', name: 'Babylon', c: '#4a6fd1', from: 1595, to: 1155, lab: [45.3, 32.1], pts: [[48.3, 30.1], [47.1, 31.8], [45.6, 33.6], [44.0, 33.9], [43.5, 33.1], [44.6, 31.4], [46.6, 30.0]] },
    { id: 'hittite', name: 'Hittites', c: '#9a6a3e', from: 1650, to: 1350, lab: [34.0, 39.2], pts: [[31.8, 40.6], [35.8, 41.0], [37.6, 39.8], [37.0, 38.2], [34.6, 37.6], [32.4, 38.0], [31.0, 39.2]] },
    { id: 'hittite2', name: 'Hittites', c: '#9a6a3e', from: 1350, to: 1185, lab: [34.4, 38.9], pts: [[29.8, 40.6], [35.8, 41.2], [38.6, 39.8], [39.0, 37.4], [38.6, 35.8], [36.8, 34.5], [35.9, 35.2], [36.0, 36.7], [34.4, 37.2], [31.6, 37.4], [29.6, 38.6]] },
    { id: 'mitanni', name: 'Mitanni', c: '#9b7bea', from: 1550, to: 1260, lab: [40.3, 36.6], pts: [[37.6, 37.4], [40.4, 37.7], [43.4, 37.2], [44.2, 35.9], [42.4, 35.3], [39.8, 35.6], [37.6, 36.0]] },
    { id: 'midassyria', name: 'Assyria', c: '#d0503c', from: 1363, to: 1150, lab: [42.6, 35.9], pts: [[39.6, 37.6], [42.2, 37.8], [44.6, 37.2], [45.2, 35.6], [44.2, 34.4], [42.6, 34.8], [40.2, 35.4], [38.8, 36.4]] },
    { id: 'egypt', name: 'Egypt', c: '#e8a51a', from: 3150, to: 1150, lab: [30.2, 27.0], pts: [[29.8, 31.5], [32.3, 31.5], [32.5, 30.0], [33.1, 28.0], [33.3, 26.0], [33.2, 24.0], [32.7, 23.1], [32.2, 24.0], [31.1, 26.5], [30.5, 28.0], [30.1, 30.3]] },
    { id: 'egyptnk', name: '', c: '#e8a51a', from: 1550, to: 1177, lab: [35.4, 32.4], pts: [[34.2, 31.3], [35.0, 33.0], [36.1, 34.8], [36.9, 34.6], [36.4, 33.0], [35.8, 31.3], [35.0, 30.5]] },
    { id: 'elam', name: 'Elam', c: '#4fb06a', from: 3200, to: 1100, lab: [50.2, 31.4], pts: [[47.8, 33.0], [49.6, 33.2], [52.6, 31.0], [53.6, 29.2], [52.2, 28.8], [49.8, 30.0], [48.3, 30.6], [47.6, 31.8]] },
    { id: 'minoan', name: 'Minoans', c: '#ff7fa8', from: 3100, to: 1450, lab: [25.3, 34.6], pts: [[23.6, 35.6], [26.4, 35.4], [26.4, 34.9], [23.6, 35.1]] }
  ];
  var CITIES = [
    ['Göbekli Tepe', 38.92, 37.22, 9500, 8000], ['Jericho', 35.44, 31.87, 9000], ['Çatalhöyük', 32.83, 37.67, 7100, 5700],
    ['Byblos', 35.65, 34.12, 5000], ['Eridu', 45.99, 30.82, 5400], ['Nippur', 45.23, 32.13, 5000], ['Susa', 48.25, 32.19, 4200],
    ['Uruk', 45.64, 31.32, 4000], ['Ur', 46.1, 30.96, 3800], ['Hamoukar', 42.08, 36.83, 4500, 3500], ['Abydos', 31.92, 26.18, 3200],
    ['Thebes', 32.64, 25.7, 3200], ['Memphis', 31.25, 29.85, 3100], ['Kish', 44.6, 32.54, 3100], ['Lagash', 46.41, 31.41, 3000],
    ['Megiddo', 35.18, 32.58, 3000], ['Nineveh', 43.15, 36.36, 3000], ['Ebla', 36.8, 35.8, 3000], ['Troy', 26.24, 39.96, 3000, 1180],
    ['Mari', 40.89, 34.55, 2900], ['Tyre', 35.2, 33.27, 2750], ['Assur', 43.26, 35.46, 2600], ['Dilmun', 50.55, 26.07, 2500],
    ['Akkad', 44.5, 33.1, 2334, 2154], ['Babylon', 44.42, 32.54, 2300], ['Knossos', 25.16, 35.3, 2000], ['Kanesh', 35.63, 38.85, 2000, 1700],
    ['Avaris', 31.83, 30.79, 1800, 1550], ['Ugarit', 35.78, 35.6, 1800, 1185], ['Kadesh', 36.52, 34.56, 1700], ['Hattusa', 34.62, 40.02, 1650, 1185],
    ['Washukanni', 40.07, 36.85, 1550, 1260], ['Amarna', 30.9, 27.65, 1346, 1332]
  ];
  var BIG = { 'Uruk': 1, 'Babylon': 1, 'Memphis': 1, 'Thebes': 1, 'Hattusa': 1, 'Nineveh': 1, 'Jericho': 1, 'Göbekli Tepe': 1, 'Ur': 1, 'Assur': 1, 'Susa': 1, 'Troy': 1, 'Ugarit': 1, 'Mari': 1, 'Kadesh': 1 };
  var NOLAB = { 'Nippur': 1, 'Lagash': 1, 'Kish': 1 };
  var EV = window.DAWN_EVENTS || [];

  var svg = el('svg', { viewBox: '0 0 ' + W + ' ' + H, role: 'img', 'aria-label': 'Animated map of the ancient Middle East' }, box);
  var defs = el('defs', {}, svg);
  var g1 = el('linearGradient', { id: 'sea', x1: 0, y1: 0, x2: 0, y2: 1 }, defs); el('stop', { offset: 0, 'stop-color': '#4cc3e6' }, g1); el('stop', { offset: 1, 'stop-color': '#2a9fcf' }, g1);
  var g2 = el('linearGradient', { id: 'sand', x1: 0, y1: 0, x2: 1, y2: 1 }, defs); el('stop', { offset: 0, 'stop-color': '#f6dfa6' }, g2); el('stop', { offset: 1, 'stop-color': '#efcf8c' }, g2);
  var bl = el('filter', { id: 'soft', x: '-20%', y: '-20%', width: '140%', height: '140%' }, defs); el('feGaussianBlur', { stdDeviation: 6 }, bl);
  el('rect', { width: W, height: H, fill: 'url(#sea)' }, svg);
  el('path', { d: L.d, fill: 'none', stroke: '#e9fbff', 'stroke-width': 9, 'stroke-opacity': .45, 'stroke-linejoin': 'round' }, svg);
  el('path', { d: L.d, fill: 'url(#sand)', stroke: '#fff', 'stroke-width': 2.5, 'stroke-linejoin': 'round' }, svg);
  // fertile river valleys, then the rivers
  RIVERS.forEach(function (r, i) { el('path', { d: line(r), fill: 'none', stroke: '#7cc86a', 'stroke-width': i === 2 ? 26 : 30, 'stroke-linecap': 'round', 'stroke-linejoin': 'round', opacity: .55, filter: 'url(#soft)' }, svg); });
  el('path', { d: smooth([[29.9, 31.4], [32.2, 31.4], [31.3, 30.1]]), fill: '#7cc86a', opacity: .55, filter: 'url(#soft)' }, svg);
  RIVERS.forEach(function (r) { el('path', { d: line(r), fill: 'none', stroke: '#3aa6d8', 'stroke-width': 3.2, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, svg); });
  [[43.0, 38.6, 18, 9], [45.4, 37.7, 10, 20]].forEach(function (k) { var p = P(k[0], k[1]); el('ellipse', { cx: p[0], cy: p[1], rx: k[2], ry: k[3], fill: '#3aa6d8', stroke: '#fff', 'stroke-width': 2 }, svg); });
  // mountains: little cartoon peaks along the Taurus and the Zagros
  var M = [[31.5, 37.2], [33, 37.1], [34.5, 37.3], [36, 37.8], [37.5, 38.2], [39.2, 38.4], [41, 38.2], [42.8, 37.6], [44.6, 36.9], [45.8, 35.6], [46.8, 34.4], [47.8, 33.4], [49, 32.4], [50.2, 31.4], [51.4, 30.3], [52.8, 29.4], [35.8, 29.2], [34.3, 28.6], [33.6, 27.6]];
  M.forEach(function (m, i) { var p = P(m[0], m[1]), s = 11 + (i % 3) * 3; el('path', { d: 'M' + (p[0] - s) + ',' + (p[1] + s * .6) + 'L' + p[0] + ',' + (p[1] - s * .8) + 'L' + (p[0] + s) + ',' + (p[1] + s * .6) + 'Z', fill: '#d9b27a', stroke: '#b98d55', 'stroke-width': 1.5, 'stroke-linejoin': 'round' }, svg); el('path', { d: 'M' + (p[0] - s * .32) + ',' + (p[1] - s * .22) + 'L' + p[0] + ',' + (p[1] - s * .8) + 'L' + (p[0] + s * .32) + ',' + (p[1] - s * .22) + 'Z', fill: '#fff' }, svg); });
  // sea names
  [['Mediterranean Sea', 29.2, 33.6], ['Persian Gulf', 50.4, 27.7], ['Red Sea', 35.6, 24.2]].forEach(function (s) { var p = P(s[1], s[2]); var t = el('text', { x: p[0], y: p[1], 'text-anchor': 'middle', fill: '#e9fbff', 'font-size': 17, 'font-family': 'Fredoka, sans-serif', 'font-weight': 600, opacity: .9, 'letter-spacing': '1' }, svg); t.textContent = s[0]; });
  // empires
  var gE = el('g', {}, svg), empires = EMPIRES.map(function (e) {
    var g = el('g', { opacity: 0 }, gE); g.style.transition = 'opacity .6s';
    el('path', { d: smooth(e.pts), fill: e.c, 'fill-opacity': .32, stroke: e.c, 'stroke-width': 3, 'stroke-dasharray': '10 7', 'stroke-linejoin': 'round' }, g);
    if (e.name) { var p = P(e.lab[0], e.lab[1]); var t = el('text', { x: p[0], y: p[1], 'text-anchor': 'middle', fill: '#fff', stroke: e.c, 'stroke-width': 5, 'paint-order': 'stroke', 'font-size': 22, 'font-family': '"Baloo 2", Fredoka, sans-serif', 'font-weight': 800, 'letter-spacing': '1.5' }, g); t.textContent = e.name.toUpperCase(); }
    return { e: e, g: g };
  });
  // cities
  var gC = el('g', {}, svg), cities = CITIES.map(function (c) {
    var p = P(c[1], c[2]), big = BIG[c[0]], g = el('g', { class: 'city', opacity: 0 }, gC); g.style.transition = 'opacity .5s';
    el('circle', { cx: p[0], cy: p[1], r: big ? 11 : 8, fill: '#fff', stroke: '#4a2a1c', 'stroke-width': 2.5 }, g);
    el('circle', { cx: p[0], cy: p[1], r: big ? 5 : 3.5, fill: '#c8683a' }, g);
    var ring = el('circle', { cx: p[0], cy: p[1], r: 10, fill: 'none', stroke: '#fff', 'stroke-width': 3, opacity: 0 }, g);
    var right = c[1] < 45.5 || c[0] === 'Ur';
    var t = el('text', { x: p[0] + (right ? 15 : -15), y: p[1] + 5, 'text-anchor': right ? 'start' : 'end', fill: '#4a2a1c', stroke: '#fff8ea', 'stroke-width': 4, 'paint-order': 'stroke', 'font-size': big ? 17 : 14, 'font-family': 'Fredoka, sans-serif', 'font-weight': 600 }, g);
    t.textContent = c[0]; if (NOLAB[c[0]]) t.setAttribute('display', 'none');
    return { c: c, g: g, ring: ring, on: false };
  });

  var yearEl = document.getElementById('mapYear'), capEl = document.getElementById('mapCap'), range = document.getElementById('mapRange'), btn = document.getElementById('mapPlay');
  var START = 9600, END = 1150, year = START, playing = true, last = 0;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function fmt(y) { var lang = document.documentElement.lang; var bc = lang === 'es' ? 'a. C.' : lang === 'pt' ? 'a.C.' : 'BC'; var n = Math.round(y); return (n >= 1000 ? n.toLocaleString(lang === 'en' ? 'en-US' : lang) : n) + ' ' + bc; }
  function draw() {
    yearEl.textContent = fmt(year);
    empires.forEach(function (o) { o.g.setAttribute('opacity', year <= o.e.from && year > o.e.to ? 1 : 0); });
    cities.forEach(function (o) {
      var on = year <= o.c[3] && (!o.c[4] || year > o.c[4]);
      o.g.setAttribute('opacity', on ? 1 : (o.c[4] && year <= o.c[4] ? .28 : 0));
      if (on && !o.on && playing && !reduce) { o.ring.setAttribute('opacity', 1); o.ring.setAttribute('r', 10); var t0 = performance.now(); (function pop(t) { var k = (t - t0) / 700; if (k > 1) { o.ring.setAttribute('opacity', 0); return; } o.ring.setAttribute('r', 10 + k * 26); o.ring.setAttribute('opacity', 1 - k); requestAnimationFrame(pop); })(t0); }
      o.on = on;
    });
    var cur = null; for (var i = 0; i < EV.length; i++) if (year <= EV[i][0]) cur = EV[i];
    var lang = document.documentElement.lang, txt = cur ? (cur[lang === 'es' ? 2 : lang === 'pt' ? 3 : 1] || cur[1]) : '';
    if (capEl.getAttribute('data-t') !== txt) { capEl.setAttribute('data-t', txt); capEl.textContent = txt; capEl.style.opacity = txt ? 1 : 0; }
    range.value = String(START - year);
  }
  // time runs faster through the long early millennia
  function speed(y) { return y > 4000 ? 520 : y > 3000 ? 190 : 120; }
  function tick(t) {
    if (playing) { var dt = last ? Math.min(.1, (t - last) / 1000) : 0; year -= speed(year) * dt; if (year <= END) { year = END; playing = false; btn.setAttribute('aria-pressed', 'false'); setTimeout(function () { if (!playing) { year = START; playing = true; btn.setAttribute('aria-pressed', 'true'); } }, 4000); } draw(); }
    last = t; requestAnimationFrame(tick);
  }
  range.min = 0; range.max = String(START - END); range.step = 10;
  range.addEventListener('input', function () { playing = false; btn.setAttribute('aria-pressed', 'false'); year = START - (+range.value); draw(); });
  btn.addEventListener('click', function () { if (year <= END) year = START; playing = !playing; btn.setAttribute('aria-pressed', playing ? 'true' : 'false'); });
  if (reduce) { playing = false; year = 1300; btn.setAttribute('aria-pressed', 'false'); }
  // start when the map scrolls into view
  if ('IntersectionObserver' in window && !reduce) {
    playing = false; var seen = false;
    new IntersectionObserver(function (es) { if (es[0].isIntersecting && !seen) { seen = true; year = START; playing = true; btn.setAttribute('aria-pressed', 'true'); } }, { threshold: .35 }).observe(box);
  }
  document.addEventListener('mm:lang', draw);
  draw(); requestAnimationFrame(tick);
})();
