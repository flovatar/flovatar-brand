// brand.flovatar.com: copy-to-clipboard helpers and TOC highlighting (no dependencies)
(function () {
  const toast = document.getElementById('toast');
  let t;
  function say(msg) {
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(t);
    t = setTimeout(() => toast.classList.remove('show'), 2200);
  }
  async function copyText(text) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch (e) {
      const ta = document.createElement('textarea');
      ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      const ok = document.execCommand('copy');
      ta.remove();
      return ok;
    }
  }
  document.addEventListener('click', async (e) => {
    const f = e.target.closest('[data-fetch]');
    if (f) {
      e.preventDefault();
      try {
        const r = await fetch(f.dataset.fetch, { cache: 'no-cache' });
        const txt = await r.text();
        const ok = await copyText(txt);
        say(ok ? `Copied ${Math.round(txt.length / 1024)} KB: paste it into your agent` : 'Copy failed: open the raw file');
      } catch (err) { say('Copy failed: open the raw file'); }
      return;
    }
    const c = e.target.closest('[data-copy]');
    if (c) {
      if (await copyText(c.dataset.copy)) say(`Copied ${c.dataset.copy}`);
      return;
    }
    const cc = e.target.closest('.copy-code');
    if (cc) {
      const code = cc.parentElement.querySelector('code');
      if (code && await copyText(code.innerText)) say('Copied');
    }
  });
  // copy buttons on code blocks (prompts, templates)
  document.querySelectorAll('pre').forEach((pre) => {
    const b = document.createElement('button');
    b.className = 'btn-mini copy-code'; b.type = 'button'; b.textContent = 'Copy';
    pre.appendChild(b);
  });
  // mobile TOC
  const toc = document.getElementById('toc');
  const mt = document.querySelector('.menu-toggle');
  if (mt) mt.addEventListener('click', () => {
    const open = toc.classList.toggle('open');
    mt.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  toc.addEventListener('click', (e) => { if (e.target.closest('a')) { toc.classList.remove('open'); mt && mt.setAttribute('aria-expanded', 'false'); } });
  // active section highlight
  const links = new Map();
  toc.querySelectorAll('a').forEach((a) => links.set(a.getAttribute('href').slice(1), a));
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (en.isIntersecting) {
        const h = en.target.querySelector('h1[id], h2[id]');
        const a = h && links.get(h.id);
        if (a) { toc.querySelectorAll('a.active').forEach((x) => x.classList.remove('active')); a.classList.add('active'); }
      }
    });
  }, { rootMargin: '-40% 0px -55% 0px' });
  document.querySelectorAll('section.sec').forEach((s) => io.observe(s));
})();
