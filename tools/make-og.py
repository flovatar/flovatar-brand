#!/usr/bin/env python3
"""Generate web/og.jpg (1200x630), web/favicon.png (64), web/apple-touch-icon.png (180).
Uses committed assets + the Staatliches TTF (OFL, Google Fonts) from $STAATLICHES_TTF or dist-private/fonts/Staatliches-Regular.ttf
(gitignored); falls back to Pillow's default font.
Requires Pillow."""
import os
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
S = os.path.join(ROOT, 'web')
FONT = os.environ.get('STAATLICHES_TTF', os.path.join(ROOT, 'dist-private', 'fonts', 'Staatliches-Regular.ttf'))


def main():
    W, H = 1200, 630
    bg = Image.new('RGB', (W, H), '#180830')
    d = ImageDraw.Draw(bg)
    for y in range(H):  # night → indigo vertical gradient
        t = y / H
        c = tuple(int(a + (b - a) * t) for a, b in zip((0x18, 0x08, 0x30), (0x41, 0x17, 0x93)))
        d.line([(0, y), (W, y)], fill=c)
    rnd = random.Random(7)
    for _ in range(140):
        x, y, r = rnd.randrange(W), rnd.randrange(H), rnd.choice([1, 1, 1, 2])
        d.ellipse([x, y, x + r, y + r], fill=(255, 255, 255))
    # pink planet horizon glow
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([-200, 520, W + 200, 1300], fill=(239, 42, 193, 255))
    glow = glow.filter(ImageFilter.GaussianBlur(6))
    halo = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(halo).ellipse([-260, 470, W + 260, 1360], fill=(250, 188, 235, 110))
    halo = halo.filter(ImageFilter.GaussianBlur(40))
    bg = Image.alpha_composite(bg.convert('RGBA'), halo)
    bg = Image.alpha_composite(bg, glow)
    # logo
    logo = Image.open(os.path.join(S, 'assets/logos/flovatar/png/flovatar-logo-horizontal-color-mix.png')).convert('RGBA')
    logo.thumbnail((470, 160))
    bg.alpha_composite(logo, (60, 70))
    d = ImageDraw.Draw(bg)
    try:
        f1 = ImageFont.truetype(FONT, 92)
        f2 = ImageFont.truetype(FONT, 38)
    except OSError:
        f1 = f2 = ImageFont.load_default()
    d.text((62, 250), 'BRAND GUIDE', font=f1, fill='#AED7F7')
    d.text((64, 350), 'FOR HUMANS AND AI AGENTS', font=f2, fill='#EF2AC1')
    d.text((64, 400), 'LOGO · COLOR · TYPE', font=f2, fill='#FFFFFF')
    d.text((64, 446), 'CHARACTERS · VOICE · LORE', font=f2, fill='#FFFFFF')
    # characters
    xs = [(640, 'flovatar-1763'), (790, 'flovatar-52'), (940, 'flovatar-2073')]
    for x, n in [(700, 445), (850, 875), (1000, 2324)]:
        im = Image.open(os.path.join(S, f'assets/samples/flovatar/flovatar-{n}.webp')).convert('RGBA')
        im.thumbnail((300, 300))
        bg.alpha_composite(im, (x - 150, 300))
    bg.convert('RGB').save(os.path.join(S, 'og.jpg'), 'JPEG', quality=86, optimize=True, progressive=True)
    mark = Image.open(os.path.join(S, 'assets/logos/flovatar/png/flovatar-mark-color-mix-gradient-square.png')).convert('RGBA')
    mark.resize((64, 64), Image.LANCZOS).save(os.path.join(S, 'favicon.png'), optimize=True)
    mark.resize((180, 180), Image.LANCZOS).save(os.path.join(S, 'apple-touch-icon.png'), optimize=True)
    print('og/favicons done')


if __name__ == '__main__':
    main()
