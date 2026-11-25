#!/usr/bin/env python3
"""Prepare the web-sized brand assets in web/assets/ from the original files (re-runnable).

The original files (logo exports, published art, PDFs, site images) are NOT in this repo. Their locations come
from a local JSON config that is never committed:

  BRAND_ASSETS_CONFIG=/path/to/config.json   (default: tools/assets.local.json, gitignored)

Copy tools/assets.example.json, which documents every key. Relative paths resolve against "root". Missing
sources are skipped with a warning, so a partial config still refreshes the files it can.

Usage:  python3 tools/prepare-assets.py [--out DIR]       (default DIR: web/assets)
Output: optimised, web-sized copies only. Raw design sources (.ai/.psd/.otf) are never copied, SVG comments are
dropped, PDF metadata is scrubbed and raster images are re-encoded through Pillow (no EXIF/XMP/text chunks).
Needs Pillow, plus PyMuPDF for the PDF step (python -m pip install pillow pymupdf).
"""
import argparse
import glob
import json
import os
import re
import shutil
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
WARN = []


def kebab(name):
    name = os.path.splitext(name)[0]
    name = name.replace('Colour', 'color').replace('Vert', 'vertical')
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


def ensure(d):
    os.makedirs(d, exist_ok=True)
    return d


def png(src, dst, max_side=1024):
    im = Image.open(src)
    im = im.convert('RGBA') if im.mode in ('P', 'LA', 'RGBA') or 'transparency' in im.info else im.convert('RGB')
    im.thumbnail((max_side, max_side), Image.LANCZOS)
    im.save(dst, optimize=True)


def webp(src, dst, max_side=800, q=86):
    im = Image.open(src).convert('RGBA')
    im.thumbnail((max_side, max_side), Image.LANCZOS)
    im.save(dst, 'WEBP', quality=q, method=6)


def jpg(src, dst, max_side=1280, q=84):
    im = Image.open(src).convert('RGB')
    im.thumbnail((max_side, max_side), Image.LANCZOS)
    im.save(dst, 'JPEG', quality=q, optimize=True, progressive=True)


def svg(src, dst):
    """Copy an SVG without comments (editor/generator lines)."""
    with open(src, encoding='utf-8') as f:
        s = f.read()
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(re.sub(r'<!--.*?-->\s*', '', s, flags=re.S))


class Config:
    def __init__(self, path):
        with open(path, encoding='utf-8') as f:
            self.c = json.load(f)
        self.root = os.path.expanduser(self.c.get('root', '.'))

    def _abs(self, rel):
        rel = os.path.expanduser(rel)
        return rel if os.path.isabs(rel) else os.path.join(self.root, rel)

    def path(self, key):
        v = self.c.get(key)
        if not v:
            WARN.append(f'{key}: not configured')
            return None
        v = self._abs(v)
        if not os.path.exists(v):
            WARN.append(f'{key}: not found')
            return None
        return v

    def glob(self, key):
        v = self.c.get(key)
        if not v:
            WARN.append(f'{key}: not configured')
            return []
        return sorted(glob.glob(self._abs(v)))

    def mapping(self, key, default_max):
        """{"out-name.jpg": "src"} or {"out-name.jpg": ["src", max_side]} → [(out, src, max_side)]"""
        out = []
        for dst, v in (self.c.get(key) or {}).items():
            src, mx = (v[0], v[1]) if isinstance(v, list) else (v, default_max)
            src = self._abs(src)
            if os.path.exists(src):
                out.append((dst, src, mx))
            else:
                WARN.append(f'{key}/{dst}: source not found')
        return out


def main():
    ap = argparse.ArgumentParser(description='Prepare the web-sized brand assets in web/assets/.')
    ap.add_argument('--out', default=os.path.join(HERE, '..', 'web', 'assets'))
    args = ap.parse_args()
    cfg = os.environ.get('BRAND_ASSETS_CONFIG', os.path.join(HERE, 'assets.local.json'))
    if not os.path.exists(cfg):
        sys.exit(f'No config at {cfg}. Copy tools/assets.example.json to tools/assets.local.json and fill it in.')
    C = Config(cfg)
    OUT = args.out

    # ---- Flovatar logos (official exported set) ----
    ds = ensure(f'{OUT}/logos/flovatar/svg'); dp = ensure(f'{OUT}/logos/flovatar/png')
    lg = C.path('flovatar_logos_dir')
    if lg:
        for f in sorted(glob.glob(f'{lg}/*.svg')):
            svg(f, f'{ds}/flovatar-{kebab(os.path.basename(f)).replace("logo-icon", "mark")}.svg')
        for f in sorted(glob.glob(f'{lg}/*.png')):
            n = kebab(os.path.basename(f)).replace('logo-icon', 'mark')
            png(f, f'{dp}/flovatar-{n}.png', 1600 if 'horizontal' in n else 1024)
    for f in C.glob('social_avatars_glob'):
        n = kebab(os.path.basename(f)).replace('social-icons-', '').replace('social-icon-', '')
        png(f, f'{dp}/flovatar-social-{n}.png', 1024)
    site = C.path('site_images_dir')  # public/images of github.com/flovatar/flovatar-web
    if site:
        svg(f'{site}/logo.svg', f'{ds}/flovatar-logo-web-header.svg')  # header logo used on flovatar.com

    # ---- Iconography (v1.0 outline icons + live product objects) ----
    di = ensure(f'{OUT}/icons')
    for f in C.glob('brand_icons_glob'):
        png(f, f'{di}/{kebab(os.path.basename(f))}.png', 512)
    if site:
        for n in ['spark.svg', 'spark-overcharged.svg', 'booster-rare.svg', 'booster-epic.svg', 'booster-legendary.svg',
                  'pack-dust.svg', 'pack-terrakit.svg', 'psyche-likee.svg', 'flobot-spark-rare.svg', 'flobot-spark-epic.svg',
                  'flobot-spark-legendary.svg', 'flobits-rarity.svg']:
            if os.path.exists(f'{site}/{n}'):
                svg(f'{site}/{n}', f'{di}/{n}')
        for n in ['token-dust.png', 'token-dust-stack.png']:
            png(f'{site}/{n}', f'{di}/{n}', 512)
    sv = C.path('sportvatar_images_dir')  # public/images of github.com/flovatar/sportvatar
    if sv:
        for n in ['rarity-flame-common.svg', 'rarity-flame-rare.svg', 'rarity-flame-epic.svg', 'rarity-flame-legendary.svg']:
            if os.path.exists(f'{sv}/{n}'):
                svg(f'{sv}/{n}', f'{di}/sportvatar-{n}')

    # ---- Sportvatar logos ----
    dss = ensure(f'{OUT}/logos/sportvatar/svg'); dsp = ensure(f'{OUT}/logos/sportvatar/png')
    sl = C.path('sportvatar_logos_dir')
    if sl:
        for f in sorted(glob.glob(f'{sl}/*.svg')):
            svg(f, f'{dss}/{kebab(os.path.basename(f))}.svg')
        for f in sorted(glob.glob(f'{sl}/*.png')):
            png(f, f'{dsp}/{kebab(os.path.basename(f))}.png', 1200)
    for f in C.glob('sportvatar_icons_glob'):
        png(f, f'{dsp}/sportvatar-mark-{kebab(os.path.basename(f)).replace("icon-", "")}.png', 512)

    # ---- Partner badges ----
    dpn = ensure(f'{OUT}/partners')
    for f in C.glob('flow_badges_glob'):
        kind = 'compact' if '/Compact/' in f else 'horizontal'
        n = kebab(os.path.basename(f)).replace('compact-builtonflow-', '').replace('builtonflow-', '')
        svg(f, f'{dpn}/built-on-flow-{kind}-{n}.svg')
    if site:
        for n in ['logo-flow.svg', 'logo-flow-black.svg', 'logo-dapper.svg']:
            svg(f'{site}/{n}', f'{dpn}/{n}')
        svg(f'{site}/logo-emerald-city.svg', f'{dpn}/logo-emerald-city-on-dark.svg')
        svg(f'{site}/logo-find.svg', f'{dpn}/logo-find-white.svg')

    # ---- Character samples: public renders, https://flovatar.com/api/image/r/<type>/<id>/full.png ----
    smp = {
        'flovatar': [3, 52, 260, 445, 475, 1763, 2073, 2324, 2860, 4135, 4200, 4908, 4983, 6313, 6570, 875, 1192, 3167],
        'flobot': [23, 153, 158, 265, 323, 72],
        'collectible': [131, 167, 614, 710, 86, 182],
        'sportvatar': [133, 195, 205, 384, 482, 1048],
        'template': [221, 572, 758, 769, 898, 873],
    }
    names = {'collectible': 'psyche-likee', 'template': 'flobit'}
    rd = C.path('renders_dir')  # files saved as <type>-<id>-full.png
    if rd:
        for t, ids in smp.items():
            d = ensure(f'{OUT}/samples/{names.get(t, t)}')
            for i in ids:
                s = f'{rd}/{t}-{i}-full.png'
                if os.path.exists(s):
                    webp(s, f'{d}/{names.get(t, t)}-{i}.webp', 800)
                    if t == 'flovatar' and i in (52, 1763, 2073, 6313, 4200, 3):
                        png(s, f'{d}/{names.get(t, t)}-{i}.png', 1000)

    # ---- Storyworld / A Dust Odyssey (published episode art) ----
    dst = ensure(f'{OUT}/story')
    for out, s, mx in C.mapping('story_images', 1280):
        jpg(s, f'{dst}/{out}', mx)
    for n in C.glob('story_title_glob'):
        jpg(n, f'{dst}/ado-{kebab(os.path.basename(n))}.jpg', 1280)

    # ---- Asteroid Islands / FUB / TerraKit ----
    da = ensure(f'{OUT}/asteroids')
    for out, s, mx in C.mapping('asteroid_images', 1100):
        jpg(s, f'{da}/{out}', mx)

    # ---- Reference layouts (published banners, covers, guides) ----
    dr = ensure(f'{OUT}/references')
    for out, s, mx in C.mapping('reference_images', 1600):
        (png if out.endswith('.png') else jpg)(s, f'{dr}/{out}', mx)
    vr = C.path('v1_page_renders_dir')  # v1-XX.png, pages of the v1.0 PDF rendered with PyMuPDF
    if vr:
        for i in (1, 5, 6, 7, 8, 9, 10, 11, 12):
            s = f'{vr}/v1-{i:02d}.png'
            if os.path.exists(s):
                jpg(s, f'{dr}/v1-guidelines-p{i:02d}.jpg', 1280)
    for out, s, _ in C.mapping('reference_pdfs', 0):
        shutil.copy(s, f'{dr}/{out}')
    # scrub PDF metadata (design-tool exports embed local file paths and user names in XMP)
    pdfs = glob.glob(f'{dr}/*.pdf')
    if pdfs:
        import pymupdf
        for f in pdfs:
            d = pymupdf.open(f)
            d.scrub(metadata=True, xml_metadata=True, thumbnails=True, javascript=True, attached_files=True,
                    embedded_files=True, clean_pages=False, hidden_text=False, redactions=False, remove_links=False,
                    reset_fields=False, reset_responses=False)
            d.save(f + '.tmp', garbage=4, deflate=True)
            d.close()
            os.replace(f + '.tmp', f)

    for w in WARN:
        print('WARNING:', w)
    print('done')


if __name__ == '__main__':
    main()
