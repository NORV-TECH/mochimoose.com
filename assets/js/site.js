/* Mochi Moose site: language (EN / ES / PT) and store buttons. No cookies, no analytics. */
(function () {
  document.documentElement.classList.add('js');

  // A store button becomes a real link once its URL is filled in here.
  var STORES = {
    sb: { play: '', amazon: '', apple: '' },
    dawn: { play: '', amazon: '', apple: '' }
  };

  var T = {
    es: {
      skip: 'Saltar al contenido', navGames: 'Juegos', navAbout: 'Nosotros', navSupport: 'Ayuda',
      kicker: '¡Hola, somos Mochi Moose!',
      h1: 'Juegos acogedores que dan vida a pequeños <em>mundos</em>',
      lead: 'Somos un pequeño y alegre estudio de juegos. Hacemos juegos relajantes para toda la familia, donde cada victoria hace que pase algo maravilloso.',
      ctaGames: 'Conoce nuestros juegos', ctaHello: 'Escríbenos',
      gamesEyebrow: 'Nuestros juegos', gamesTitle: 'Juega una mano, mira una historia',
      gamesSub: 'Los juegos de cartas clásicos que ya te encantan, con un pequeño mundo en 3D esperándote detrás de cada victoria.',
      sbStatus: 'Llega en octubre de 2026', sbBy: 'Solitario Klondike · 36 historias bíblicas',
      sbDesc: 'Gana una mano de Klondike clásico y mira cómo cobra vida el siguiente momento de una historia bíblica, desde el primer día de la Creación hasta la mañana de Pascua. El mar Rojo se abre, caen los muros de Jericó y David enfrenta a Goliat, todo en pequeños mundos 3D que puedes girar y explorar.',
      chip1: '221 momentos animados', chip2: '100 cruces escondidas', chip3: 'Versículos narrados', chip4: '38 idiomas', chip5: 'Música clásica',
      soon: 'Muy pronto', getIt: 'Disponible en', legalPriv: 'Política de privacidad', legalTerms: 'Términos de uso',
      cap1: 'Cruzando el mar Rojo', cap2: 'El arca de Noé', cap3: 'David y Goliat', cap4: 'Los muros de Jericó', cap5: 'Jonás y el gran pez', cap6: 'El gran final',
      badge: 'Muy pronto',
      dawnDesc: 'Nuestros personajitos viajan al comienzo mismo de la historia. Gana manos de solitario para construir las primeras grandes ciudades, mira cómo cambia el mapa del mundo antiguo mientras los imperios surgen y caen, y colecciona tesoros del amanecer de la civilización.',
      dawnWhere: 'Llegará a Android, tabletas Fire, iPhone y iPad.',
      civ1: 'Sumeria', civ1s: 'Las primeras ciudades', civ2: 'Egipto', civ2s: 'Pirámides junto al Nilo', civ3: 'Asiria', civ3s: 'La poderosa Nínive', civ4: 'Babilonia', civ4s: 'La Puerta de Ishtar',
      dawnNote: '¿Quieres enterarte en cuanto salga?', dawnBtn: 'Avísame cuando esté listo',
      famEyebrow: 'Hecho para familias', famTitle: 'Seguro, tranquilo y amigable', famSub: 'El tipo de juego que le puedes pasar a cualquiera de la familia.',
      perk1t: 'Sin cuentas ni chats', perk1: 'No hay que registrarse ni hablar con desconocidos. Tu progreso se queda en tu dispositivo.',
      perk2t: 'Anuncios aptos para la familia', perk2: 'Los anuncios se limitan a contenido familiar, y una pequeña compra los quita para siempre.',
      perk3t: 'Funciona sin internet', perk3: '¿Sin internet? No pasa nada. Los juegos funcionan donde sea, en teléfonos y tabletas.',
      perk4t: 'En tu idioma', perk4: 'Solitaire Bible 3D habla 38 idiomas, con versículos narrados en inglés, español y portugués.',
      aboutEyebrow: 'Nosotros', aboutTitle: '¡Hola desde el alce!',
      about1: 'Mochi Moose es un pequeño estudio independiente. Hacemos juegos que se sienten como un abrazo: colores suaves, música tranquila, personajitos con un gran corazón e historias para compartir con quienes amas.',
      about2: '¿Tienes una idea, encontraste un error o solo quieres saludar? Leemos todos los mensajes.', aboutBtn: 'Escríbenos',
      footTag: 'Estudio pequeño, sonrisas grandes. Juegos acogedores para toda la familia.',
      footPriv: 'Privacidad', footTerms: 'Términos', rights: 'Todos los derechos reservados.',
      privTitle: 'Política de privacidad', termsTitle: 'Términos de uso', supTitle: 'Ayuda', supSub: 'Estamos aquí para ayudarte.',
      nfTitle: '¡Uy! Esta página se escondió', nfBody: 'Buscamos por todas partes, hasta debajo de las cartas, y no la encontramos.', nfBtn: 'Volver al inicio'
    },
    pt: {
      skip: 'Pular para o conteúdo', navGames: 'Jogos', navAbout: 'Sobre', navSupport: 'Ajuda',
      kicker: 'Oi, nós somos a Mochi Moose!',
      h1: 'Jogos aconchegantes que dão vida a pequenos <em>mundos</em>',
      lead: 'Somos um estúdio de jogos pequeno e feliz. Fazemos jogos relaxantes para toda a família, em que cada vitória faz algo maravilhoso acontecer.',
      ctaGames: 'Conheça nossos jogos', ctaHello: 'Fale com a gente',
      gamesEyebrow: 'Nossos jogos', gamesTitle: 'Jogue uma mão, veja uma história',
      gamesSub: 'Os jogos de cartas clássicos que você já ama, com um pequeno mundo em 3D esperando por trás de cada vitória.',
      sbStatus: 'Chega em outubro de 2026', sbBy: 'Paciência Klondike · 36 histórias bíblicas',
      sbDesc: 'Vença uma mão de Klondike clássico e veja o próximo momento de uma história bíblica ganhar vida, do primeiro dia da Criação até a manhã da Páscoa. O mar Vermelho se abre, as muralhas de Jericó caem e Davi enfrenta Golias, tudo em pequenos mundos 3D que você pode girar e explorar.',
      chip1: '221 momentos animados', chip2: '100 cruzes escondidas', chip3: 'Versículos narrados', chip4: '38 idiomas', chip5: 'Música clássica',
      soon: 'Em breve', getIt: 'Disponível no', legalPriv: 'Política de privacidade', legalTerms: 'Termos de uso',
      cap1: 'Atravessando o mar Vermelho', cap2: 'A arca de Noé', cap3: 'Davi e Golias', cap4: 'As muralhas de Jericó', cap5: 'Jonas e o grande peixe', cap6: 'O grande final',
      badge: 'Em breve',
      dawnDesc: 'Nossos personagens estão voltando ao comecinho da história. Vença mãos de paciência para construir as primeiras grandes cidades, veja o mapa do mundo antigo mudar enquanto impérios surgem e caem, e colecione tesouros do amanhecer da civilização.',
      dawnWhere: 'Chegando ao Android, tablets Fire, iPhone e iPad.',
      civ1: 'Suméria', civ1s: 'As primeiras cidades', civ2: 'Egito', civ2s: 'Pirâmides à beira do Nilo', civ3: 'Assíria', civ3s: 'A poderosa Nínive', civ4: 'Babilônia', civ4s: 'A Porta de Ishtar',
      dawnNote: 'Quer saber assim que sair?', dawnBtn: 'Me avise quando estiver pronto',
      famEyebrow: 'Feito para famílias', famTitle: 'Seguro, tranquilo e amigável', famSub: 'O tipo de jogo que você pode entregar para qualquer pessoa da família.',
      perk1t: 'Sem contas, sem chat', perk1: 'Nada de cadastro e nenhum desconhecido para conversar. Seu progresso fica no seu aparelho.',
      perk2t: 'Anúncios para a família', perk2: 'Os anúncios são limitados a conteúdo familiar, e uma pequena compra remove todos de vez.',
      perk3t: 'Funciona offline', perk3: 'Sem internet? Sem problema. Os jogos funcionam em qualquer lugar, em celulares e tablets.',
      perk4t: 'No seu idioma', perk4: 'Solitaire Bible 3D fala 38 idiomas, com versículos narrados em inglês, espanhol e português.',
      aboutEyebrow: 'Sobre nós', aboutTitle: 'Um oi do alce!',
      about1: 'A Mochi Moose é um pequeno estúdio independente. Fazemos jogos que parecem um abraço quentinho: cores suaves, música tranquila, personagens pequenos de coração grande e histórias para compartilhar com quem você ama.',
      about2: 'Tem uma ideia, achou um bug ou só quer dar um oi? Lemos todas as mensagens.', aboutBtn: 'Mande um e-mail',
      footTag: 'Estúdio pequeno, sorrisos grandes. Jogos aconchegantes para toda a família.',
      footPriv: 'Privacidade', footTerms: 'Termos', rights: 'Todos os direitos reservados.',
      privTitle: 'Política de privacidade', termsTitle: 'Termos de uso', supTitle: 'Ajuda', supSub: 'Estamos aqui para ajudar.',
      nfTitle: 'Ops! Esta página se escondeu', nfBody: 'Procuramos em todo lugar, até embaixo das cartas, e não encontramos.', nfBtn: 'Voltar ao início'
    }
  };

  // page-specific strings (game pages) add to the dictionaries
  var X = window.MM_EXTRA || {};
  ['es', 'pt'].forEach(function (l) { if (X[l]) for (var k in X[l]) T[l][k] = X[l][k]; });

  var EN = {};
  var nodes = document.querySelectorAll('[data-i18n]');
  for (var i = 0; i < nodes.length; i++) EN[nodes[i].getAttribute('data-i18n')] = nodes[i].innerHTML;

  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function put(k, v) { try { localStorage.setItem(k, v); } catch (e) { } }

  function pick() {
    var q = (location.search.match(/[?&]lang=(en|es|pt)\b/) || [])[1];
    if (q) return q;
    var s = get('mm.lang'); if (s === 'en' || s === 'es' || s === 'pt') return s;
    var n = (navigator.languages && navigator.languages[0]) || navigator.language || 'en';
    n = n.slice(0, 2).toLowerCase();
    return n === 'es' || n === 'pt' ? n : 'en';
  }

  function apply(lang) {
    var d = T[lang] || {};
    document.documentElement.lang = lang;
    for (var i = 0; i < nodes.length; i++) {
      var k = nodes[i].getAttribute('data-i18n');
      var v = lang === 'en' ? EN[k] : d[k];
      if (v != null) nodes[i].innerHTML = v;
    }
    var bs = document.querySelectorAll('.lang button');
    for (var j = 0; j < bs.length; j++) bs[j].setAttribute('aria-pressed', bs[j].getAttribute('data-lang') === lang ? 'true' : 'false');
    // documents keep all three languages in the page; show the chosen one
    var arts = document.querySelectorAll('.doc > [lang]');
    if (arts.length) {
      var has = false;
      for (var a = 0; a < arts.length; a++) if (arts[a].getAttribute('lang') === lang) has = true;
      for (var b = 0; b < arts.length; b++) arts[b].hidden = has && arts[b].getAttribute('lang') !== lang;
      var ls = document.querySelectorAll('.langbar a');
      for (var c = 0; c < ls.length; c++) ls[c].setAttribute('aria-current', ls[c].getAttribute('data-lang') === lang ? 'true' : 'false');
    }
    try { document.dispatchEvent(new CustomEvent('mm:lang', { detail: lang })); } catch (e) { }
    var t = document.querySelector('[data-title]');
    if (t) { var tk = t.getAttribute('data-title'); var tv = lang === 'en' ? EN[tk] : d[tk]; if (tv) document.title = tv.replace(/<[^>]+>/g, '') + ' · Mochi Moose'; }
  }

  function stores() {
    var bs = document.querySelectorAll('[data-store]');
    for (var i = 0; i < bs.length; i++) {
      var p = bs[i].getAttribute('data-store').split('.'), url = STORES[p[0]] && STORES[p[0]][p[1]];
      if (!url) continue;
      bs[i].href = url; bs[i].removeAttribute('aria-disabled'); bs[i].removeAttribute('role'); bs[i].className = 'btn';
      var s = bs[i].querySelector('small'); if (s) s.setAttribute('data-i18n', 'getIt'), s.innerHTML = EN.getIt || 'Get it on';
    }
  }

  var lang = pick();
  if (!EN.getIt) EN.getIt = 'Get it on';
  stores();
  nodes = document.querySelectorAll('[data-i18n]');
  apply(lang);

  document.addEventListener('click', function (e) {
    var b = e.target.closest ? e.target.closest('[data-lang]') : null;
    if (b) {
      e.preventDefault();
      lang = b.getAttribute('data-lang'); put('mm.lang', lang); apply(lang);
      return;
    }
    var off = e.target.closest ? e.target.closest('[aria-disabled="true"]') : null;
    if (off) e.preventDefault();
  });
})();
