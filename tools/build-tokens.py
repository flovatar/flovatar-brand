#!/usr/bin/env python3
"""Generate tokens/design-tokens.json (W3C DTCG-style), tokens/tokens.css and tokens/contrast.md
from the single palette definition below. Stdlib only.  Usage: python3 tools/build-tokens.py
Every value cites its source: v1 = flovatar-brand-guidelines-v1.0.pdf (Mar 2022); site = github.com/flovatar/flovatar-web
resources/scss (live flovatar.com, Nov 2026); svv1 = Sportvatar-Brand-Guidelines-v1.0.pdf (Mar 2023);
svsite = sportvatar repo scss; logo = Media Pack logo SVGs; partner = partner logo SVGs.
"""
import json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

ULT_SRC = 'Brand guide §9.3.1: darker purple with subtle blue-noise gold/white glitter'
ULT_EXT = {'label': 'ULTIMATE', 'css': 'https://brand.flovatar.com/tokens/ultimate.css',
           'classes': {'.fl-ultimate': 'fill + glitter (+ twinkle, off under prefers-reduced-motion)',
                       '.fl-ultimate-badge': 'ULTIMATE pill label', '.fl-ultimate-frame': '3 px card border + gold keyline'},
           'glitter-layers': ['https://brand.flovatar.com/tokens/ultimate-glitter-509.svg', 'https://brand.flovatar.com/tokens/ultimate-glitter-613.svg',
                              'https://brand.flovatar.com/tokens/ultimate-glitter-757.svg'],
           'glitter': 'blue-noise (Poisson-disk) white + gold dots 0.75-2 px and a few 4-point stars <= 3 px, opacity 0.22-0.66; three stacked tiles of 509/613/757 px (primes, never visibly repeats); layers 2-3 twinkle 4.3 s / 6.7 s, static under prefers-reduced-motion',
           'svg-pattern': 'https://brand.flovatar.com/tokens/ultimate-glitter-pattern.svg',
           'gradient': 'linear-gradient(160deg, #5A1268 0%, #5A1268 45%, #2E0A3A 100%)'}

CMYK = {'space-indigo': [93, 99, 0, 0], 'aurora-pink': [27, 82, 0, 0], 'sky-blue': [38, 0, 4, 0],
        'nova-yellow': [5, 1, 77, 0], 'deep-space-blue': [100, 100, 39, 40], 'solar-violet': [77, 71, 0, 0]}

PALETTE = {
    'flovatar': {
        'core': {  # the official identity palette (v1)
            'space-indigo':    ('#411793', 'Primary. Logo backgrounds, covers, large brand fields.', 'v1 (Pantone Violet C, CMYK 93/99/0/0)'),
            'aurora-pink':     ('#EF2AC1', 'Primary. Logo mark, highlights, eyebrows, footer field.', 'v1 (Pantone 807 C, CMYK 27/82/0/0)'),
            'sky-blue':        ('#91E3F9', 'Secondary. Wordmark on indigo, outline icons, links on dark.', 'v1 (Pantone 0821 C); CMYK 38/0/4/0'),
            'nova-yellow':     ('#FCEB4F', 'Secondary. Attention, CTAs, epic rarity family.', 'v1 (Pantone 100 C, CMYK 5/1/77/0)'),
            'deep-space-blue': ('#1B0D49', 'Secondary. Deepest backgrounds, text on light.', 'v1 (Pantone 275 C, CMYK 100/100/39/40)'),
            'solar-violet':    ('#6657D3', 'Secondary. Panels, secondary buttons, illustrations of tech/space.', 'v1 (Pantone 2725 C, CMYK 77/71/0/0)'),
        },
        'ui': {  # the live web UI palette
            'night':           ('#180830', 'Page background of flovatar.com (body).', 'site $colors.black.2'),
            'night-violet':    ('#1A083A', 'Alternate deep background.', 'site $colors.blue.6'),
            'logo-gradient-top': ('#440099', 'Top stop of the app-icon / social gradient square.', 'logo (Logo Icon Colour Mix Gradient Square)'),
            'logo-gradient-bottom': ('#230E54', 'Bottom stop of the app-icon / social gradient square.', 'logo'),
            'royal-violet':    ('#5F37CB', 'Links / interactive violet.', 'site $colors.blue.1'),
            'indigo-2':        ('#441C8F', 'Indigo UI variant.', 'site $colors.blue.2'),
            'panel':           ('#343B5A', 'Panels, stat boxes, builder frames.', 'site $colors.gray.1'),
            'panel-deep':      ('#212741', 'Inner panels.', 'site $colors.gray.2'),
            'ink':             ('#1A1E2D', 'Outlines of UI frames, button borders, dark tiles, dark text on light.', 'site $colors.gray.3 (#1A1D2D/#1A1E2D)'),
            'periwinkle':      ('#AED7F7', 'Section headlines on dark (homepage H2).', 'site $colors.blue.7'),
            'neon-pink':       ('#EB3CF2', 'Accent pink in UI; legendary rarity.', 'site $colors.pink.1'),
            'magenta-deep':    ('#A21AA8', 'Pressed/shadow tone of neon pink.', 'site $colors.pink.2'),
            'cta-yellow':      ('#FFEE50', 'Primary UI button (Connect Wallet), nav links, epic rarity.', 'site $colors.yellow.1'),
            'cta-yellow-shade':('#CCBB1D', 'Button shadow / pressed yellow.', 'site $colors.yellow.2'),
            'cyan':            ('#23EDFC', 'Rare rarity, data highlights.', 'site (rarity rare)'),
            'buy-green':       ('#52F618', 'Buy / cart / success / selected tile.', 'site (icon-cart, selected trait)'),
            'error-red':       ('#F84F64', 'Errors, destructive.', 'site scss'),
            'muted':           ('#9DA4C7', 'Secondary text on dark.', 'site scss'),
            'white':           ('#FFFFFF', 'Body text on dark.', 'site $base-text-color'),
            'tile-light':      ('#F5F5F5', 'Trait tile background / common rarity.', 'site (rgb 245,245,245)'),
        },
        'rarity': {
            'common':          ('#F5F5F5', 'Common fill (edge #AEAEAE).', 'site _builder.scss'),
            'common-edge':     ('#AEAEAE', 'Common shadow/edge.', 'site'),
            'rare':            ('#23EDFC', 'Rare fill/border.', 'site _marketplace.scss/_builder.scss'),
            'rare-edge':       ('#19A4AE', 'Rare shadow/edge (also #0798A3 stack).', 'site'),
            'epic':            ('#FFEE50', 'Epic fill/border.', 'site'),
            'epic-edge':       ('#9F9427', 'Epic shadow/edge.', 'site $colors.yellow.4'),
            'legendary':       ('#EB3CF2', 'Legendary fill/border.', 'site $colors.pink.1'),
            'legendary-edge':  ('#A21AA8', 'Legendary shadow/edge.', 'site $colors.pink.2'),
            'spark':           ('#B196FE', 'Spark counts/labels.', 'site _marketplace.scss .sparks'),
            # Ultimate rarity (1/1 Flobits), guide §9.3.1
            'ultimate':        ('#5A1268', 'Ultimate fill (1/1 Flobits): deep grape purple, darker than Legendary and its edge. White text 12.2:1. Always with the glitter layer and the ULTIMATE label.', ULT_SRC, ULT_EXT),
            'ultimate-dark':   ('#2E0A3A', 'Ultimate edge/shadow and gradient end.', ULT_SRC),
            'ultimate-glitter-gold':  ('#FFC94D', 'Ultimate glitter: gold sparkles, plus the 1 px gold keyline that separates Ultimate from dark pages.', ULT_SRC),
            'ultimate-glitter-white': ('#FFFFFF', 'Ultimate glitter: white sparkles.', ULT_SRC),
        },
    },
    'sportvatar': {
        'core': {
            'field-green':     ('#283F42', 'Primary background.', 'svv1 (CMYK 81/53/54/55)'),
            'neon-green':      ('#D4FF36', 'Primary accent, logo on Field Green.', 'svv1 (CMYK 27/0/96/0)'),
            'slate-green':     ('#607A7C', 'Secondary.', 'svv1'),
            'aquamarine':      ('#A5F1D6', 'Secondary.', 'svv1'),
            'field-green-dark':('#152627', 'Secondary, deep backgrounds.', 'svv1'),
            'prussian-grey':   ('#353238', 'Secondary, neutral dark.', 'svv1'),
            'pitch-black':     ('#0C1617', 'Live sportvatar.com page background.', 'svsite $colors.black.2'),
        },
    },
    'partners': {
        'flow': {
            'flow-green':      ('#00EF8B', 'Flow brand green (only inside Flow badges/logos).', 'partner logo-flow.svg'),
        },
        'dapper': {
            'dapper-purple':   ('#7A2AD9', 'Dapper brand purple (only inside Dapper logo).', 'partner logo-dapper.svg'),
        },
    },
}

TYPE = {
    'family': {
        'display':   ("'Staatliches', 'Korolev Compressed', 'Arial Narrow', sans-serif", 'Big headlines, page titles, short uppercase titles. v1.'),
        'heading':   ("'Korolev Condensed', 'Roboto Condensed', 'Arial Narrow', sans-serif", 'Smaller headlines; all headings h1–h6 on flovatar.com (bold). v1 + site.'),
        'numeric':   ("'Korolev Compressed', 'Staatliches', 'Arial Narrow', sans-serif", 'Big numbers / stats / nav on flovatar.com. site.'),
        'body':      ("'Roboto Condensed', 'Arial Narrow', Arial, sans-serif", 'Section headers and body copy. v1 + site.'),
    },
    'size-px': {  # flovatar.com scale (desktop / <tablet)
        'h1': (55, None), 'h2': (50, 40), 'h3': (32, 28), 'h4': (26, None), 'h5': (17, None), 'h6': (15, None), 'body': (16, None),
    },
    'line-height': {'body': 1.25, 'h2': 0.9, 'h3': 1.0},
}

# brand strings: the token's brand spelling. Identifiers in code stay ASCII (guide §7.4).
TEXT = {
    'dust': ('ĐUST', 'Brand spelling of the Flovatar utility token in all prose, headlines, UI, social copy, alt text and prompts.',
             {'codepoint': 'U+0110', 'html': '&#272;', 'not': ['DUST (in prose)', '$DUST (in prose)', 'ÐUST (U+00D0 Eth)'],
              'identifiers-keep-ascii': ['FlovatarDustToken', 'DUST (token symbol in code/wallets)', 'URLs, file names, hashtags', 'quotes of historical posts'],
              'glyph-coverage': {'Korolev Condensed Bold': True, 'Korolev Compressed Bold': True,
                                 'Staatliches': 'latin-ext subset only (the latin subset lacks U+0110)',
                                 'Roboto Condensed': 'latin-ext subset only (the latin subset lacks U+0110)'},
              'fallback': 'Load the latin-ext subset with unicode-range; otherwise set the Đ in Korolev Compressed/Condensed Bold, then Arial Narrow/Arial (guide §10.4).'}),
    'umbrella-line': ('Your creativity powers the Megaverse. Again.', 'Relaunch umbrella line. Use verbatim.', {}),
}

RADII = {'none': '0', 'tile': '6px', 'panel': '10px', 'input': '5px', 'pill': '999px', 'round': '50%'}
SHADOWS = {
    'button-offset': ('6px 6px 0 0 #1A1E2D', 'Hard offset shadow under chunky buttons (builder / Connect Wallet).'),
    'card-stack': ('-9px 0 0 -3px currentColor, -15px 0 0 -3px currentColor', 'Stacked-card hint for bundles (approximation of site .stack).'),
    'glow-pink': ('0 0 24px rgba(239,42,193,.55)', 'Portal / spark glow (inferred from art).'),
}


def lum(hexc):
    h = hexc.lstrip('#')
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def rgb(hexc):
    h = hexc.lstrip('#')
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]


def main():
    tok = {'$description': 'Flovatar brand tokens — generated by tools/build-tokens.py. Values are sourced; see $extensions.source.',
           'color': {}, 'font': {}, 'radius': {}, 'shadow': {}, 'text': {}}
    css = [':root {', '  /* Generated by tools/build-tokens.py — do not edit by hand. */']
    for k, (v, d, ext) in TEXT.items():
        tok['text'].setdefault('brand', {})[k] = {'$type': 'string', '$value': v, '$description': d, '$extensions': ext}
        css.append(f'  --brand-{k}: "{v}";')
    for brand, groups in PALETTE.items():
        tok['color'][brand] = {}
        for g, cols in groups.items():
            tok['color'][brand][g] = {}
            for name, (hexc, role, src, *more) in cols.items():
                ext = {'rgb': rgb(hexc), 'source': src}
                if brand == 'flovatar' and g == 'core' and name in CMYK:
                    ext['cmyk'] = CMYK[name]
                if more:
                    ext.update(more[0])
                tok['color'][brand][g][name] = {'$type': 'color', '$value': hexc, '$description': role, '$extensions': ext}
                prefix = {'flovatar': 'fl', 'sportvatar': 'sv', 'partners': 'partner'}[brand]
                gp = '' if g in ('core', 'ui', 'flow', 'dapper') else g + '-'
                css.append(f'  --{prefix}-{gp}{name}: {hexc};')
    for k, (v, d) in TYPE['family'].items():
        tok['font'].setdefault('family', {})[k] = {'$type': 'fontFamily', '$value': v, '$description': d}
        css.append(f'  --font-{k}: {v};')
    for k, (d, m) in TYPE['size-px'].items():
        tok['font'].setdefault('size', {})[k] = {'$type': 'dimension', '$value': f'{d}px', '$extensions': {'below-tablet': f'{m}px' if m else None}}
        css.append(f'  --size-{k}: {d}px;')
    tok['font']['lineHeight'] = {k: {'$type': 'number', '$value': v} for k, v in TYPE['line-height'].items()}
    for k, v in RADII.items():
        tok['radius'][k] = {'$type': 'dimension', '$value': v}
        css.append(f'  --radius-{k}: {v};')
    for k, (v, d) in SHADOWS.items():
        tok['shadow'][k] = {'$type': 'shadow', '$value': v, '$description': d}
        css.append(f'  --shadow-{k}: {v};')
    css.append('}')
    os.makedirs(f'{ROOT}/tokens', exist_ok=True)
    json.dump(tok, open(f'{ROOT}/tokens/design-tokens.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
    open(f'{ROOT}/tokens/tokens.css', 'w', encoding='utf-8').write('\n'.join(css) + '\n')

    # contrast table for the pairs agents actually use
    F = {k: v[0] for g in PALETTE['flovatar'].values() for k, v in g.items()}
    S = {k: v[0] for k, v in PALETTE['sportvatar']['core'].items()}
    S['white'] = '#FFFFFF'
    pairs = [
        ('white', 'night', F), ('periwinkle', 'night', F), ('sky-blue', 'night', F), ('aurora-pink', 'night', F),
        ('neon-pink', 'night', F), ('cta-yellow', 'night', F), ('cyan', 'night', F), ('muted', 'night', F),
        ('sky-blue', 'space-indigo', F), ('white', 'space-indigo', F), ('aurora-pink', 'space-indigo', F),
        ('nova-yellow', 'space-indigo', F), ('white', 'aurora-pink', F), ('deep-space-blue', 'aurora-pink', F),
        ('space-indigo', 'aurora-pink', F), ('ink', 'cta-yellow', F), ('ink', 'cyan', F), ('ink', 'neon-pink', F),
        ('ink', 'buy-green', F), ('space-indigo', 'white', F), ('deep-space-blue', 'white', F), ('aurora-pink', 'white', F),
        ('white', 'panel', F), ('cta-yellow', 'panel', F), ('white', 'solar-violet', F), ('deep-space-blue', 'sky-blue', F),
        ('neon-green', 'field-green', S), ('neon-green', 'pitch-black', S), ('white', 'field-green', S),
        ('field-green', 'neon-green', S), ('aquamarine', 'field-green-dark', S),
        ('white', 'ultimate', F), ('white', 'ultimate-dark', F), ('ultimate-glitter-gold', 'ultimate', F),
        ('ultimate-glitter-gold', 'night', F), ('ultimate', 'night', F),
    ]
    rows = ['# Contrast-checked colour pairs (WCAG 2.x)', '',
            'Generated by `tools/build-tokens.py`. AA body text needs ≥ 4.5, AA large text (≥ 24 px, or ≥ 18.66 px bold) and UI graphics need ≥ 3.0.', '',
            '| Foreground | Background | Ratio | Body text (AA 4.5) | Large text / UI (3.0) |', '|---|---|---:|:---:|:---:|']
    for fg, bg, P in pairs:
        r = contrast(P[fg], P[bg])
        rows.append(f'| {fg} `{P[fg]}` | {bg} `{P[bg]}` | {r:.2f} | {"✅" if r >= 4.5 else "❌"} | {"✅" if r >= 3 else "❌"} |')
    open(f'{ROOT}/tokens/contrast.md', 'w').write('\n'.join(rows) + '\n')
    write_ultimate(F)
    print('\n'.join(rows))


# ---------------- Ultimate rarity glitter ----------------
# Subtle, small, evenly distributed, never a visible repeat:
# tiny dots (0.75-2 px at 1x) plus a few 4-point stars (<= 3 px), placed by Poisson-disk (blue-noise) sampling
# on a torus so each tile wraps seamlessly, in three layers with prime tile sizes (cicada principle): the
# combined pattern only repeats every 509 x 613 x 757 px. Fixed seeds: the output is reproducible.
import math, random

GLITTER_LAYERS = [  # (id, tile px, min distance px, seed, background offset px)
    ('509', 509, 21, 9301, (0, 0)),
    ('613', 613, 23, 7717, (241, 97)),
    ('757', 757, 25, 5323, (389, 433)),
]
DOT_SIZES = [(0.75, 34), (1.0, 30), (1.25, 18), (1.5, 11), (2.0, 7)]   # diameter px, weight
STAR_SIZES = [1.2, 1.5]                                                # arm length px (<= 3 px across)
OPACITY = {'w': [.28, .4, .52, .68], 'g': [.36, .5, .64, .8]}          # white / gold opacity buckets
GOLD_SHARE, STAR_SHARE = .42, .045
U = 2   # SVG units per px: integer coordinates in half-pixel steps keep the files small


def poisson_torus(size, r, rng, k=30):
    """Bridson Poisson-disk sampling on a size x size torus (distances wrap), so tiles join without seams."""
    cell = r / math.sqrt(2)
    n = int(math.ceil(size / cell))
    grid = [[None] * n for _ in range(n)]

    def ok(x, y):
        gx, gy = int(x / cell), int(y / cell)
        for i in range(-2, 3):
            for j in range(-2, 3):
                q = grid[(gx + i) % n][(gy + j) % n]
                if q:
                    dx, dy = abs(q[0] - x), abs(q[1] - y)
                    dx, dy = min(dx, size - dx), min(dy, size - dy)
                    if dx * dx + dy * dy < r * r:
                        return False
        return True

    p0 = (rng.uniform(0, size), rng.uniform(0, size))
    pts, active = [p0], [p0]
    grid[int(p0[0] / cell)][int(p0[1] / cell)] = p0
    while active:
        i = rng.randrange(len(active))
        ax, ay = active[i]
        for _ in range(k):
            a, d = rng.uniform(0, 2 * math.pi), rng.uniform(r, 2 * r)
            x, y = (ax + d * math.cos(a)) % size, (ay + d * math.sin(a)) % size
            if ok(x, y):
                pts.append((x, y)); active.append((x, y)); grid[int(x / cell)][int(y / cell)] = (x, y)
                break
        else:
            active.pop(i)
    return pts


def fnum(v):
    s = f'{v:.2f}'.rstrip('0').rstrip('.')
    if s.startswith('0.'):
        s = s[1:]
    elif s.startswith('-0.'):
        s = '-' + s[2:]
    return s or '0'


def star(x, y, s):
    k, f = s * 0.22, lambda v: str(round(v * U))
    return (f'M{f(x)} {f(y - s)}Q{f(x + k)} {f(y - k)} {f(x + s)} {f(y)}Q{f(x + k)} {f(y + k)} {f(x)} {f(y + s)}'
            f'Q{f(x - k)} {f(y + k)} {f(x - s)} {f(y)}Q{f(x - k)} {f(y - k)} {f(x)} {f(y - s)}Z')


def glitter_layer(size, r, seed, gold, white='#FFFFFF'):
    """SVG markup (no wrapper) for one seamless glitter tile. Dots are zero-length round-capped strokes
    (needs stroke-linecap="round" on an ancestor); stars are filled 4-point sparkles."""
    rng = random.Random(seed)
    pts = poisson_torus(size, r, rng)
    dots, stars = {}, {}
    for x, y in pts:
        col = 'g' if rng.random() < GOLD_SHARE else 'w'
        op = rng.choice(OPACITY[col])
        is_star = rng.random() < STAR_SHARE
        sz = rng.choice(STAR_SIZES) if is_star else rng.choices([d for d, _ in DOT_SIZES], [w for _, w in DOT_SIZES])[0]
        copies, m = [(x, y)], 2.5   # wrap copies for sparkles touching an edge, so the tile stays seamless
        for dx in ([-size] if x > size - m else [size] if x < m else []) + [0]:
            for dy in ([-size] if y > size - m else [size] if y < m else []) + [0]:
                if dx or dy:
                    copies.append((x + dx, y + dy))
        for cx, cy in copies:
            if is_star:
                stars.setdefault((col, min(.9, round(op + .15, 2))), []).append(star(cx, cy, sz))
            else:
                dots.setdefault((col, op, sz), []).append(f'M{round(cx * U)} {round(cy * U)}h0')
    paint = {'w': white, 'g': gold}
    out = [f'<path stroke="{paint[c]}" stroke-opacity="{fnum(o)}" stroke-width="{fnum(w * U)}" d="{"".join(d)}"/>'
           for (c, o, w), d in sorted(dots.items())]
    out += [f'<path fill="{paint[c]}" fill-opacity="{fnum(o)}" d="{"".join(d)}"/>' for (c, o), d in sorted(stars.items())]
    return ''.join(out), len(pts)


ULT_CSS = '''/* Flovatar · Ultimate rarity (1/1 Flobits). Generated by tools/build-tokens.py.
   Glitter = three transparent blue-noise sparkle tiles with prime sizes (@SA@/@SB@/@SC@ px, "cicada principle"), each at
   its own offset: the combined pattern repeats only every @SA@ x @SB@ x @SC@ px, so it never visibly tiles.
   Self-host the tiles if you build outside flovatar.com. */
:root {
  --fl-rarity-ultimate: @BASE@;
  --fl-rarity-ultimate-dark: @DARK@;
  --fl-rarity-ultimate-glitter-gold: @GOLD@;
  --fl-rarity-ultimate-glitter-white: #FFFFFF;
  --fl-ultimate-glitter-1: url(https://brand.flovatar.com/tokens/ultimate-glitter-@A@.svg) @OA@ / @SA@px @SA@px;
  --fl-ultimate-glitter-2: url(https://brand.flovatar.com/tokens/ultimate-glitter-@B@.svg) @OB@ / @SB@px @SB@px;
  --fl-ultimate-glitter-3: url(https://brand.flovatar.com/tokens/ultimate-glitter-@C@.svg) @OC@ / @SC@px @SC@px;
  --fl-ultimate-fill:
    radial-gradient(120% 90% at 25% 0%, rgba(255,255,255,.12), transparent 55%),
    linear-gradient(160deg, var(--fl-rarity-ultimate) 0%, var(--fl-rarity-ultimate) 45%, var(--fl-rarity-ultimate-dark) 100%);
}
/* Fill with glitter: badges, rarity chips, card backgrounds. White text on it: 12.2:1.
   Layer 1 is static; layers 2 and 3 sit behind the content and twinkle out of step (opacity only). */
.fl-ultimate {
  position: relative; isolation: isolate; color: #fff;
  background: var(--fl-ultimate-glitter-1), var(--fl-ultimate-fill);
}
.fl-ultimate::before, .fl-ultimate::after {
  content: ""; position: absolute; inset: 0; z-index: -1; border-radius: inherit; pointer-events: none;
}
.fl-ultimate::before { background: var(--fl-ultimate-glitter-2); animation: fl-ultimate-twinkle 4.3s ease-in-out -1.1s infinite alternate; }
.fl-ultimate::after { background: var(--fl-ultimate-glitter-3); animation: fl-ultimate-twinkle 6.7s ease-in-out -3.9s infinite alternate-reverse; }
@keyframes fl-ultimate-twinkle { from { opacity: .35; } to { opacity: 1; } }
/* ULTIMATE label (pill), Korolev Compressed caps like the other rarity labels. Use together with .fl-ultimate. */
.fl-ultimate-badge {
  display: inline-block; padding: .28em .8em .22em; border-radius: 999px;
  font: 700 1em/1 "Korolev Compressed", "Staatliches", "Arial Narrow", sans-serif; letter-spacing: .05em; text-transform: uppercase;
  text-shadow: 0 1px 0 var(--fl-rarity-ultimate-dark);
  box-shadow: 0 0 0 1.5px var(--fl-rarity-ultimate-glitter-gold), 0 0 8px rgba(255,201,77,.28);
}
/* Card frame: the 3 px rarity border of marketplace cards, in glittering Ultimate purple, with a 1 px gold keyline
   so it reads on Night backgrounds (purple alone is too dark there). */
.fl-ultimate-frame {
  border: 3px solid transparent; border-radius: 6px;
  background:
    linear-gradient(var(--fl-card-bg, #1A083A), var(--fl-card-bg, #1A083A)) padding-box,
    url(https://brand.flovatar.com/tokens/ultimate-glitter-@A@.svg) @OA@ / @SA@px @SA@px border-box,
    url(https://brand.flovatar.com/tokens/ultimate-glitter-@C@.svg) @OC@ / @SC@px @SC@px border-box,
    linear-gradient(160deg, var(--fl-rarity-ultimate), var(--fl-rarity-ultimate-dark)) border-box;
  box-shadow: 0 0 0 1px var(--fl-rarity-ultimate-glitter-gold), 0 0 14px rgba(255,201,77,.18);
}
@media (prefers-reduced-motion: reduce) {
  .fl-ultimate::before, .fl-ultimate::after { animation: none; opacity: .7; }   /* static glitter, no twinkle */
}
'''

ULT_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="240" height="72" viewBox="0 0 240 72" role="img" aria-label="ULTIMATE">
  <!-- Flovatar Ultimate rarity (1/1 Flobits). Copy the <defs> into any SVG; fill the shape with url(#fl-ultimate-fill),
       then draw it again once per glitter layer: url(#fl-ultimate-glitter), url(#fl-ultimate-glitter-2), url(#fl-ultimate-glitter-3).
       The layers are blue-noise tiles of @SA@, @SB@ and @SC@ px (primes), so the combined glitter never visibly repeats. -->
  <defs>
    <linearGradient id="fl-ultimate-fill" x1="0" y1="0" x2=".35" y2="1">
      <stop offset="0" stop-color="@BASE@"/><stop offset=".45" stop-color="@BASE@"/><stop offset="1" stop-color="@DARK@"/>
    </linearGradient>@PATTERNS@
  </defs>
  <rect x="2" y="2" width="236" height="68" rx="34" fill="url(#fl-ultimate-fill)"/>@GLITTER@
  <rect x="2" y="2" width="236" height="68" rx="34" fill="none" stroke="@GOLD@" stroke-width="2"/>
  <text x="120" y="48" text-anchor="middle" font-family="'Korolev Compressed', Staatliches, 'Arial Narrow', sans-serif" font-weight="700" font-size="36" letter-spacing="1.5" fill="#FFFFFF" stroke="@DARK@" stroke-width="3" paint-order="stroke">ULTIMATE</text>
</svg>
'''


def fill_tpl(tpl, rep):
    for k, v in rep.items():
        tpl = tpl.replace(f'@{k}@', str(v))
    return tpl


def write_ultimate(F):
    base, dark, gold = F['ultimate'], F['ultimate-dark'], F['ultimate-glitter-gold']
    for old in ('a', 'b'):  # remove obsolete 64 px tiles
        if os.path.exists(f'{ROOT}/tokens/ultimate-glitter-{old}.svg'):
            os.remove(f'{ROOT}/tokens/ultimate-glitter-{old}.svg')
    pats, rects, rep = [], [], {'BASE': base, 'DARK': dark, 'GOLD': gold}
    for i, (lid, size, r, seed, (ox, oy)) in enumerate(GLITTER_LAYERS):
        body, n = glitter_layer(size, r, seed, gold)
        open(f'{ROOT}/tokens/ultimate-glitter-{lid}.svg', 'w').write(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 {size * U} {size * U}" fill="none" stroke-linecap="round">'
            f'<!-- Flovatar Ultimate glitter layer {lid} px: {n} blue-noise sparkles, transparent, wraps seamlessly. '
            f'Stack it with the other prime-sized layers (509/613/757) so the glitter never visibly repeats. -->{body}</svg>\n')
        pid = 'fl-ultimate-glitter' + ('' if i == 0 else f'-{i + 1}')
        tr = f' patternTransform="translate({ox} {oy})"' if ox or oy else ''
        pats.append(f'\n    <pattern id="{pid}" width="{size}" height="{size}" patternUnits="userSpaceOnUse"{tr}>'
                    f'<g fill="none" stroke-linecap="round" transform="scale({fnum(1 / U)})">{body}</g></pattern>')
        rects.append(f'\n  <rect x="2" y="2" width="236" height="68" rx="34" fill="url(#{pid})"/>')
        L = 'ABC'[i]
        rep.update({L: lid, 'S' + L: size, 'O' + L: f'{ox}px {oy}px' if ox or oy else '0 0'})
    rep.update({'PATTERNS': ''.join(pats), 'GLITTER': ''.join(rects)})
    open(f'{ROOT}/tokens/ultimate-glitter-pattern.svg', 'w').write(fill_tpl(ULT_SVG, rep))
    open(f'{ROOT}/tokens/ultimate.css', 'w').write(fill_tpl(ULT_CSS, rep))


if __name__ == '__main__':
    main()
