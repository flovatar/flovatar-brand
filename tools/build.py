#!/usr/bin/env python3
"""Build the Flovatar brand guide into dist/ (a static site for any object-storage bucket or static host).

  guide/NN-*.md   ──►  BRAND.md (repo root, master handover, committed)
  web/            ──►  dist/ (static sources: assets, css, js, robots, 404, og image)
  dist-private/fonts/*.woff2 (licensed, gitignored) ──► dist/fonts/ + dist/static/<name>.<hash>.woff2
  generated       ──►  dist/index.html, dist/<section-slug>/index.html, dist/BRAND.md, dist/llms.txt,
                       dist/llms-full.txt, dist/sections/*.md, dist/tokens/*, dist/sitemap.xml, dist/assets/manifest.json
CSS/JS are emitted with content hashes under dist/static/ (cache 1 year immutable). Every internal link points to an
explicit file (…/index.html) so the site works on a bucket without directory-index handling.

Requirements: Python 3.9+, `pip install markdown pillow`.  Usage: python3 tools/build.py  →  scripts/publish.sh
"""
import datetime
import glob
import hashlib
import html
import json
import os
import re
import shutil

import markdown

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SITE = os.path.join(ROOT, 'dist')
WEB = os.path.join(ROOT, 'web')
FONTS = os.path.join(ROOT, 'dist-private', 'fonts')
BASE = 'https://brand.flovatar.com'
VERSION = '2.6.0'
DATE = '2026-11-24'

try:
    from PIL import Image
except ImportError:  # manifest without dimensions
    Image = None


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


def expand_includes(md):
    def inc(m):
        txt = read(os.path.join(ROOT, m.group(1)))
        lines = txt.splitlines()
        if lines and lines[0].startswith('# '):  # drop the include's own H1
            lines = lines[1:]
        txt = '\n'.join(lines).strip()
        if m.group(1).endswith('.svg'):  # keep generated sparkle coordinates out of BRAND.md (they live in the linked file)
            txt = re.sub(r'(<pattern [^>]*>)(<g [^>]*>).*?(</g></pattern>)',
                         lambda g: f'{g[1]}{g[2]}<!-- {g[0].count("M")} blue-noise sparkles: copy them from the file -->{g[3]}', txt)
        return txt
    return re.sub(r'\{\{include:([^}]+)\}\}', inc, md)


HTML_MARK = re.compile(r'<!--html:([a-z0-9-]+)-->')


def slug(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'^[0-9.]+\s*', '', s)  # drop numbering
    s = s.lower().replace('&amp;', 'and').replace('&', 'and')
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s or 'section'


def load_sections():
    secs = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'guide', '*.md'))):
        md = expand_includes(read(p)).replace('{{VERSION}}', VERSION).replace('{{DATE}}', DATE).strip() + '\n'
        title = next((l[3:].strip() for l in md.splitlines() if l.startswith('## ')), None) or \
            next((l[2:].strip() for l in md.splitlines() if l.startswith('# ')), 'Intro')
        secs.append({'file': os.path.basename(p), 'md': md, 'title': title,
                     'slug': os.path.splitext(os.path.basename(p))[0]})
    return secs


def asset_manifest():
    items = []
    for p in sorted(glob.glob(os.path.join(SITE, 'assets', '**', '*'), recursive=True)):
        if os.path.isdir(p) or p.endswith('manifest.json'):
            continue
        rel = os.path.relpath(p, SITE).replace(os.sep, '/')
        it = {'path': rel, 'url': f'{BASE}/{rel}', 'bytes': os.path.getsize(p)}
        if Image and p.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            try:
                with Image.open(p) as im:
                    it['width'], it['height'] = im.size
            except Exception:
                pass
        items.append(it)
    man = {'name': 'Flovatar brand assets', 'version': VERSION, 'generated': DATE,
           'credit': 'Art and design by the Flovatar team. Logos are trademarks of Flovatar; partner marks belong to their owners.',
           'count': len(items), 'assets': items}
    write(os.path.join(SITE, 'assets', 'manifest.json'), json.dumps(man, indent=1))
    return items


# ---------------- HTML galleries injected at <!--html:name--> markers ----------------

def A(path):
    return f'/assets/{path}'


def gallery_logos():
    rows = [
        ('logos/flovatar/svg/flovatar-logo-vertical-color-mix.svg', '#411793', 'Primary · vertical colour mix'),
        ('logos/flovatar/svg/flovatar-logo-horizontal-color-mix.svg', '#411793', 'Horizontal colour mix'),
        ('logos/flovatar/svg/flovatar-logo-vertical-pink.svg', '#411793', 'Pink on indigo'),
        ('logos/flovatar/svg/flovatar-logo-horizontal-white.svg', '#180830', 'White (dark / video)'),
        ('logos/flovatar/svg/flovatar-logo-vertical-purple.svg', '#ffffff', 'Indigo on white'),
        ('logos/flovatar/svg/flovatar-logo-vertical-black.svg', '#ffffff', 'Black on white'),
        ('logos/flovatar/svg/flovatar-logo-vertical-white.svg', '#000000', 'White on black'),
        ('logos/flovatar/svg/flovatar-mark-purple-cutout-roundel.svg', '#ffffff', 'Mark · cutout roundel'),
        ('logos/flovatar/svg/flovatar-mark-pink.svg', '#411793', 'Mark · head only'),
        ('logos/flovatar/svg/flovatar-mark-pink-purple-roundel.svg', '#ffffff', 'Mark · filled roundel'),
        ('logos/flovatar/svg/flovatar-mark-color-mix-gradient-square.svg', '#1A1E2D', 'App icon · gradient'),
        ('logos/flovatar/svg/flovatar-mark-white.svg', '#EF2AC1', 'Mark · white'),
    ]
    out = ['<div class="gallery logos">']
    for p, bg, cap in rows:
        out.append(f'<figure><a href="{A(p)}" download><div class="tile" style="background:{bg}"><img src="{A(p)}" alt="{html.escape(cap)} Flovatar logo" loading="lazy"></div></a>'
                   f'<figcaption>{html.escape(cap)} · <a href="{A(p)}" download>SVG</a> · <a href="{A(p.replace("/svg/", "/png/").replace(".svg", ".png"))}" download>PNG</a></figcaption></figure>')
    out.append('</div>')
    out.append('<div class="gallery logos">')
    for p, bg, cap in [('logos/sportvatar/svg/sportvatar-logo-color-horizontal.svg', '#283F42', 'Sportvatar · colour horizontal'),
                       ('logos/sportvatar/svg/sportvatar-logo1.svg', '#283F42', 'Sportvatar · vertical'),
                       ('logos/sportvatar/svg/sportvatar-logo-mono-neon.svg', '#152627', 'Sportvatar · mono neon mark')]:
        out.append(f'<figure><a href="{A(p)}" download><div class="tile" style="background:{bg}"><img src="{A(p)}" alt="{html.escape(cap)}" loading="lazy"></div></a><figcaption>{html.escape(cap)}</figcaption></figure>')
    out.append('</div>')
    return '\n'.join(out)


def gallery_colors():
    tok = json.load(open(os.path.join(ROOT, 'tokens', 'design-tokens.json')))
    out = []
    for brand, groups in tok['color'].items():
        for g, cols in groups.items():
            out.append(f'<h4 class="swatch-title">{html.escape(brand)} · {html.escape(g)}</h4><div class="swatches">')
            for name, v in cols.items():
                hx = v['$value']
                r, gg, b = v['$extensions']['rgb']
                light = (0.299 * r + 0.587 * gg + 0.114 * b) > 150
                out.append(f'<button class="swatch" style="background:{hx};color:{"#1A1E2D" if light else "#fff"}" data-copy="{hx}" title="Copy {hx}">'
                           f'<strong>{html.escape(name)}</strong><span>{hx}</span><small>RGB {r} {gg} {b}</small></button>')
            out.append('</div>')
    return '\n'.join(out)


def gallery_ultimate():
    """Specimen of the Ultimate rarity next to the other tiers."""
    tok = json.load(open(os.path.join(ROOT, 'tokens', 'design-tokens.json')))['color']['flovatar']['rarity']
    v = {k: tok[k]['$value'] for k in tok}
    tiers = [('Common', v['common'], '#1A1E2D'), ('Rare', v['rare'], '#1A1E2D'), ('Epic', v['epic'], '#1A1E2D'),
             ('Legendary', v['legendary'], '#1A1E2D')]
    chips = ''.join(f'<span class="tier-chip" style="background:{bg};color:{fg}">{n.upper()}</span>' for n, bg, fg in tiers)
    chips += '<span class="tier-chip fl-ultimate fl-ultimate-badge">ULTIMATE</span>'
    sw = ''.join(f'<button class="swatch" style="background:{v[k]};color:{fg}" data-copy="{v[k]}" title="Copy {v[k]}"><strong>{k}</strong><span>{v[k]}</span></button>'
                 for k, fg in (('ultimate', '#fff'), ('ultimate-dark', '#fff'), ('ultimate-glitter-gold', '#1A1E2D'), ('ultimate-glitter-white', '#1A1E2D')))
    return f'''<div class="ultimate-specimen" id="ultimate-specimen">
<div class="u-grid">
<div class="u-hero fl-ultimate"><span class="u-label">ULTIMATE</span><span class="u-hex">{v['ultimate']} → {v['ultimate-dark']}</span><span class="u-sub">glitter {v['ultimate-glitter-gold']} + {v['ultimate-glitter-white']} · white text 12.2 : 1</span></div>
<figure class="u-card fl-ultimate-frame"><img src="/assets/samples/flobit/flobit-221.webp" alt="Example Flobit render in an Ultimate card frame" width="160" height="160"><figcaption><span class="fl-ultimate fl-ultimate-badge">ULTIMATE</span><b>1/1 Flobit</b><small>card frame example</small></figcaption></figure>
<figure class="u-svg"><img src="/tokens/ultimate-glitter-pattern.svg?v={VERSION}" alt="ULTIMATE badge drawn with the SVG glitter pattern" width="240" height="72"><figcaption>SVG pattern version (<a href="/tokens/ultimate-glitter-pattern.svg">ultimate-glitter-pattern.svg</a>)</figcaption></figure>
</div>
<div class="tier-row" aria-label="All rarity labels side by side">{chips}</div>
<div class="swatches">{sw}</div>
</div>'''


def gallery_type():
    return '''<div class="type-specimens">
<div class="spec"><span class="lbl">Staatliches · display</span><p class="f-display">BIG HEADLINES WITHOUT MANY WORDS</p></div>
<div class="spec"><span class="lbl">Korolev Condensed Bold · headings</span><p class="f-heading">Each Flovatar is custom made by YOU</p></div>
<div class="spec"><span class="lbl">Korolev Compressed Bold · numbers / nav</span><p class="f-numeric">12,345 <small>FLOW</small> · BUILDER · MARKETPLACE</p></div>
<div class="spec"><span class="lbl">Roboto Condensed · body</span><p class="f-body">Flovatars have arrived in our universe on a rescue mission to save their planet's existence from a predicted future. Their survival will depend on StarDust — and StarDust depends on YOU!</p></div>
</div>
<div class="type-specimens dust-glyph" id="dust-glyph">
<div class="spec"><span class="lbl">Đ (U+0110) · Staatliches</span><p class="f-display">ĐUST · YOUR CREATIVITY POWERS THE MEGAVERSE. AGAIN.</p></div>
<div class="spec"><span class="lbl">Đ (U+0110) · Korolev Condensed Bold</span><p class="f-heading">Spend ĐUST on names, bios and Psyche Likees</p></div>
<div class="spec"><span class="lbl">Đ (U+0110) · Korolev Compressed Bold</span><p class="f-numeric">ĐUST · ĐUST BUILDER</p></div>
<div class="spec"><span class="lbl">Đ (U+0110) · Roboto Condensed</span><p class="f-body">ĐUST is the utility token of the Flovatar universe. <strong>ĐUST in bold.</strong></p></div>
</div>'''


def img_grid(items, cls='samples'):
    out = [f'<div class="gallery {cls}">']
    for p, cap in items:
        out.append(f'<figure><a href="{A(p)}"><img src="{A(p)}" alt="{html.escape(cap)}" loading="lazy"></a><figcaption>{html.escape(cap)}</figcaption></figure>')
    out.append('</div>')
    return '\n'.join(out)


def gallery_samples():
    fl = [3, 52, 260, 445, 475, 875, 1192, 1763, 2073, 2324, 2860, 3167, 4135, 4200, 4908, 4983, 6313, 6570]
    items = [(f'samples/flovatar/flovatar-{i}.webp', f'Flovatar #{i}') for i in fl]
    out = img_grid(items)
    fam = [(f'samples/flobot/flobot-{i}.webp', f'Flobot #{i}') for i in (23, 72, 153, 158, 265, 323)]
    fam += [(f'samples/psyche-likee/psyche-likee-{i}.webp', f'Psyche Likee #{i}') for i in (86, 131, 167, 182, 614, 710)]
    fam += [(f'samples/sportvatar/sportvatar-{i}.webp', f'Sportvatar #{i}') for i in (133, 195, 205, 384, 482, 1048)]
    fam += [(f'samples/flobit/flobit-{i}.webp', f'Flobit template {i}') for i in (221, 572, 758, 769, 873, 898)]
    return out + '\n<p class="note">Family: Flobots · Psyche Likees · Sportvatars · Flobits (real on-chain renders, art by the Flovatar team)</p>\n' + img_grid(fam, 'samples small')


def gallery_objects():
    items = [('icons/spark.svg', 'Spark'), ('icons/booster-rare.svg', 'Booster · Rare'), ('icons/booster-epic.svg', 'Booster · Epic'),
             ('icons/booster-legendary.svg', 'Booster · Legendary'), ('icons/token-dust.png', 'ĐUST coin'), ('icons/pack-dust.svg', 'ĐUST pack'),
             ('icons/pack-terrakit.svg', 'TerraKit'), ('icons/icon-spark.png', 'Icon · Spark (outline)'), ('icons/icon-booster.png', 'Icon · Booster (outline)'),
             ('icons/icon-flovatar.png', 'Icon · Flovatar (outline)')]
    return img_grid(items, 'samples small objects')


def gallery_story():
    items = [('story/ado-poster.jpg', 'A Dust Odyssey · poster'), ('story/ado-ep1-1-cover.jpg', 'Episode cover · Ep 1'),
             ('story/ado-ep5-cover.jpg', 'Episode cover · Ep 5'), ('story/ado-da-vinci.jpg', 'Scene · Da Vinci'),
             ('story/ado-showdown.jpg', 'Scene · Showdown'), ('story/ado-testnet.jpg', 'Scene · TestNet')]
    return img_grid(items, 'wide')


def gallery_asteroids():
    items = [('asteroids/asteroid-jungle-legendary-castle.jpg', 'Jungle · Legendary · Castle'),
             ('asteroids/asteroid-volcano-legendary-stone-fortress.jpg', 'Volcano · Legendary · Stone Fortress'),
             ('asteroids/asteroid-rock-castle-epic.jpg', 'Rock · Epic · Castle'),
             ('asteroids/asteroid-oasis-common.jpg', 'Oasis · Common (concept)')]
    return img_grid(items, 'tall') + img_grid([('asteroids/fub-ecosystem-key-art.jpg', 'FUB ecosystem key art')], 'wide')


def gallery_references():
    items = [('references/x-header-3000x1000.jpg', 'X header 3000×1000'), ('references/youtube-cover-2560x1440.jpg', 'YouTube cover'),
             ('references/flowverse-flovatar-1940x500.jpg', 'Flowverse banner'), ('references/flowverse-flobots-1940x500.jpg', 'Flowverse · Flobots'),
             ('references/gaia-homepage-banner-1920x600.jpg', 'Gaia homepage banner'), ('references/dust-explainer-frame.jpg', 'ĐUST explainer'),
             ('references/float-ama-badge-1500x1962.jpg', 'FLOAT badge'), ('references/show-us-your-bits-jetpack.jpg', 'Show Us Your Bits')]
    return img_grid(items, 'wide')


def gallery_v1():
    items = [(f'references/v1-guidelines-p{i:02d}.jpg', f'v1.0 page {i}') for i in (1, 5, 6, 7, 8, 9, 10, 11, 12)]
    return img_grid(items, 'wide')


def gallery_anatomy():
    return (img_grid([('anatomy/flovatar-layer-stack.webp', 'Flovatar #360: the 11 layers in site order, then the composed image')], 'figure')
            + img_grid([('anatomy/flovatar-anchor-map.webp', 'Anchor map: median bounding box per category, Series 1 templates')], 'figure'))


def gallery_anatomy_family():
    return img_grid([('anatomy/flobot-layer-stack.webp', 'Flobot #72: legs → body → arms → head → face'),
                     ('anatomy/psyche-likee-layer-stack.webp', 'Psyche Likee layers and the body-mask clip join')], 'figure2')


def gallery_combos():
    return img_grid([('anatomy/combo-anatomy.webp', 'Combo: Proton Pack reveals its suit only when Jail is worn'),
                     ('anatomy/combo-order.webp', 'Same Flobits, two layer orders: only the site order fires the combo')], 'figure2')


GALLERIES = {'logos': gallery_logos, 'colors': gallery_colors, 'ultimate': gallery_ultimate, 'type': gallery_type, 'samples': gallery_samples,
             'objects': gallery_objects, 'story': gallery_story, 'asteroids': gallery_asteroids,
             'references': gallery_references, 'v1': gallery_v1,
             'anatomy': gallery_anatomy, 'anatomy-family': gallery_anatomy_family, 'combos': gallery_combos}


def autolink(md):
    """Wrap bare URLs in <...> so they render as links (HTML only), skipping code."""
    out, fence = [], False
    for line in md.split('\n'):
        if line.strip().startswith('```'):
            fence = not fence
            out.append(line)
            continue
        if fence:
            out.append(line)
            continue
        parts = re.split(r'(`[^`]*`)', line)
        for i, p in enumerate(parts):
            if i % 2 == 0:
                parts[i] = re.sub(r'(?<![(<\["\'/=\w])(https?://[^\s)<>`|]+[^\s)<>`|.,;:])', r'<\1>', p)
        out.append(''.join(parts))
    return '\n'.join(out)


def md_to_html(md):
    md = autolink(md)
    conv = markdown.Markdown(extensions=['tables', 'fenced_code', 'sane_lists', 'toc', 'attr_list'],
                             extension_configs={'toc': {'slugify': lambda v, sep: slug(v), 'toc_depth': '2-3'}})
    h = conv.convert(md)
    # colour chips next to inline hex codes
    h = re.sub(r'<code>(#[0-9A-Fa-f]{6})</code>',
               lambda m: f'<code class="hex" data-copy="{m.group(1)}"><span class="chip" style="background:{m.group(1)}"></span>{m.group(1)}</code>', h)
    # external links open in new tab
    h = re.sub(r'<a href="(https?://(?!brand\.flovatar\.com)[^"]+)"', r'<a href="\1" rel="noopener" target="_blank"', h)
    # markdown task lists
    h = h.replace('<li>[ ] ', '<li class="task"><input type="checkbox" disabled> ')
    # site-relative asset links
    h = h.replace(f'{BASE}/assets/', '/assets/').replace(f'href="{BASE}/"', 'href="/index.html"')
    h = HTML_MARK.sub(lambda m: GALLERIES[m.group(1)]() if m.group(1) in GALLERIES else '', h)
    return h


def hashed(src_bytes, name):
    h = hashlib.sha256(src_bytes).hexdigest()[:10]
    base, ext = os.path.splitext(name)
    return f'{base}.{h}{ext}'


def build():
    if os.path.isdir(SITE):
        shutil.rmtree(SITE)
    shutil.copytree(WEB, SITE)
    os.makedirs(os.path.join(SITE, 'static'), exist_ok=True)
    # ---------- fonts (licensed: never in git; only in the bucket) ----------
    font_map = {}
    if os.path.isdir(FONTS):
        os.makedirs(os.path.join(SITE, 'fonts'), exist_ok=True)
        for f in sorted(os.listdir(FONTS)):
            if f.endswith('.woff2'):
                b = open(os.path.join(FONTS, f), 'rb').read()
                shutil.copy(os.path.join(FONTS, f), os.path.join(SITE, 'fonts', f))
                hn = hashed(b, f)
                open(os.path.join(SITE, 'static', hn), 'wb').write(b)
                font_map[f] = hn
    else:
        print('WARNING: dist-private/fonts missing: site will use fallback fonts')
    css = read(os.path.join(WEB, 'style.css'))
    # Ultimate rarity classes (tokens/ultimate.css, generated) served same-origin on this site
    css += '\n' + read(os.path.join(ROOT, 'tokens', 'ultimate.css')).replace(f'{BASE}/tokens/', '/tokens/')
    for f, hn in font_map.items():
        css = css.replace(f'url(/fonts/{f})', f'url(/static/{hn})')
    css_name = hashed(css.encode(), 'style.css')
    write(os.path.join(SITE, 'static', css_name), css)
    js = read(os.path.join(WEB, 'app.js'))
    js_name = hashed(js.encode(), 'app.js')
    write(os.path.join(SITE, 'static', js_name), js)
    os.remove(os.path.join(SITE, 'style.css'))
    os.remove(os.path.join(SITE, 'app.js'))

    secs = load_sections()
    # ---------- BRAND.md ----------
    brand_md = '\n\n'.join(HTML_MARK.sub('', s['md']).strip() for s in secs) + '\n'
    brand_md = re.sub(r'\n{3,}', '\n\n', brand_md)
    write(os.path.join(ROOT, 'BRAND.md'), brand_md)
    write(os.path.join(SITE, 'BRAND.md'), brand_md)
    for s in secs:
        write(os.path.join(SITE, 'sections', s['file']), HTML_MARK.sub('', s['md']))

    # ---------- tokens ----------
    shutil.copytree(os.path.join(ROOT, 'tokens'), os.path.join(SITE, 'tokens'), dirs_exist_ok=True)

    # ---------- llms.txt ----------
    lines = ['# Flovatar Brand Guide', '',
             f'> The complete brand style guide and AI-agent handover for Flovatar (customisable, fully on-chain SVG avatar NFTs on Flow, launched 16 Dec 2021) and its family: Flobits, Flobots, Psyche Likees, ĐUST, TerraKit / Asteroid Islands / FUB, the storyworld *A Dust Odyssey*, and the sister brand Sportvatar. Version {VERSION} ({DATE}).', '',
             'Paste `BRAND.md` (or `llms-full.txt`) into an agent\'s context to produce on-brand copy, images, UI and video. Hard rules: credit art to "the Flovatar team" (never individual artists); no financial promises; wallets = Flow Wallet + Dapper Wallet; only announce shipped features; spell the token ĐUST (Đ U+0110) in all copy; AI-generated art of Flovatar IP is non-commercial for everyone, commercial only for the owner of that Flovatar or official team work; the book *A Dust Odyssey* is lore canon. Relaunch umbrella line: "Your creativity powers the Megaverse. Again." Active channels: Instagram @flovatar_nft, X @flovatar, YouTube @flovatar_live, the *A Dust Odyssey* podcast. Agencies and freelancers use Staatliches + Roboto Condensed (Korolev files are not shared). MoonPay is no longer a partner. Ultimate rarity (1/1 Flobits): deep purple #5A1268 with gold/white glitter. SVG assets (§12): one 3000×3000 canvas, fragments joined in the site layer order, existing templates never modified.', '',
             '## Full guide', '',
             f'- [BRAND.md]({BASE}/BRAND.md): the master handover, all sections in one file',
             f'- [llms-full.txt]({BASE}/llms-full.txt): BRAND.md + design tokens (CSS) + asset manifest', '',
             '## Sections (raw markdown)', '']
    for s in secs:
        lines.append(f'- [{s["title"]}]({BASE}/sections/{s["file"]})')
    lines += ['', '## Machine-readable', '',
              f'- [Design tokens (JSON)]({BASE}/tokens/design-tokens.json): colours (hex/RGB, roles, sources), type, radii, shadows',
              f'- [CSS variables]({BASE}/tokens/tokens.css)',
              f'- [Contrast pairs]({BASE}/tokens/contrast.md)',
              f'- [Asset manifest]({BASE}/assets/manifest.json): every logo, icon, sample render and reference with URL and size', '',
              '## Optional', '',
              f'- [Flovatar Identity Guidelines v1.0 (historical predecessor, PDF)]({BASE}/assets/references/flovatar-brand-guidelines-v1.0-SUPERSEDED.pdf)',
              f'- [Sportvatar Identity Guidelines v1.0 (PDF)]({BASE}/assets/references/sportvatar-brand-guidelines-v1.0.pdf)',
              '- [Source repository](https://github.com/flovatar/flovatar-brand)',
              '- [flovatar.com](https://flovatar.com): live product (Builder, Marketplace)',
              '- [sportvatar.com](https://sportvatar.com): sister product', '']
    write(os.path.join(SITE, 'llms.txt'), '\n'.join(lines))

    items = asset_manifest()
    full = [brand_md, '\n---\n\n# Appendix A: CSS design tokens\n\n```css\n' + read(os.path.join(ROOT, 'tokens', 'tokens.css')) + '```\n',
            '\n# Appendix B: asset manifest\n\n' + '\n'.join(f'- {i["url"]}' + (f' ({i["width"]}×{i["height"]})' if 'width' in i else '') for i in items) + '\n']
    write(os.path.join(SITE, 'llms-full.txt'), ''.join(full))

    # ---------- HTML ----------
    tpl = read(os.path.join(ROOT, 'tools', 'template.html'))
    rendered = []
    for s in secs:
        s['anchor'] = slug(s['title'])
        s['dir'] = s['slug'].split('-', 1)[1]
        s['page'] = f'/{s["dir"]}/index.html'
        h = md_to_html(s['md'])
        tools = (f'<div class="sec-tools"><button class="btn-mini" data-fetch="/sections/{s["file"]}">Copy section</button>'
                 f'<a class="btn-mini" href="/sections/{s["file"]}">Raw .md</a>'
                 f'<a class="btn-mini" href="{s["page"]}">Page</a></div>')
        h = re.sub(r'(</h[12]>)', lambda m: m.group(1) + tools, h, count=1)
        rendered.append((s, h))

    def page(title, desc, canonical, toc_items, body, hero):
        return (tpl.replace('{{TITLE}}', html.escape(title)).replace('{{DESC}}', html.escape(desc))
                .replace('{{CANONICAL}}', canonical).replace('{{TOC}}', '\n'.join(toc_items))
                .replace('{{BODY}}', body).replace('{{HERO}}', hero)
                .replace('{{VERSION}}', VERSION).replace('{{DATE}}', DATE).replace('{{BASE}}', BASE)
                .replace('{{CSS}}', f'/static/{css_name}').replace('{{JS}}', f'/static/{js_name}')
                .replace('{{FONT_HEAD}}', f'/static/{font_map.get("korolev-condensed-bold.woff2", "")}')
                .replace('{{FONT_BODY}}', f'/static/{font_map.get("roboto-condensed-latin.woff2", "")}'))

    hero = read(os.path.join(ROOT, 'tools', 'hero.html'))
    toc_main = [f'<li><a href="#{s["anchor"]}">{html.escape(s["title"])}</a></li>' for s, _ in rendered]
    body = '\n'.join(f'<section class="sec" id="sec-{s["slug"]}">{h}</section>' for s, h in rendered)
    write(os.path.join(SITE, 'index.html'),
          page(f'Flovatar Brand Guide v{VERSION}: style guide & AI-agent handover',
               'The official Flovatar brand guide: logo, colours, typography, character illustration style, voice & tone, lore, UI, social, motion, sub-brands, prompts and briefing templates. Optimised for LLM agents.',
               f'{BASE}/', toc_main, body, hero))
    for s, h in rendered:
        toc = [f'<li><a href="{x["page"]}"{" class=\"active\"" if x is s else ""}>{html.escape(x["title"])}</a></li>' for x, _ in rendered]
        # in-page anchors of other sections → their own pages
        hh = re.sub(r'href="#([a-z0-9-]+)"', lambda m: f'href="/index.html#{m.group(1)}"', h)
        write(os.path.join(SITE, s['dir'], 'index.html'),
              page(f'{s["title"]} · Flovatar Brand Guide v{VERSION}', f'Flovatar brand guide section: {s["title"]}.',
                   f'{BASE}{s["page"]}', toc, f'<section class="sec" id="sec-{s["slug"]}">{hh}</section>', ''))
    # 404 with hashed css
    p404 = os.path.join(SITE, '404.html')
    write(p404, read(p404).replace('{{CSS}}', f'/static/{css_name}'))

    # ---------- sitemap ----------
    urls = ['/', '/BRAND.md', '/llms.txt', '/llms-full.txt'] + [s['page'] for s, _ in rendered] + [f'/sections/{s["file"]}' for s in secs]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f'  <url><loc>{BASE}{u}</loc><lastmod>{DATE}</lastmod></url>' for u in urls]
    sm.append('</urlset>')
    write(os.path.join(SITE, 'sitemap.xml'), '\n'.join(sm) + '\n')
    words = len(re.findall(r'\w+', brand_md))
    n = sum(len(fs) for _, _, fs in os.walk(SITE))
    print(f'built dist/: {len(secs)} sections, BRAND.md {len(brand_md)//1024} KB / {words} words, {len(items)} assets, {n} files, fonts={len(font_map)}')


if __name__ == '__main__':
    build()
