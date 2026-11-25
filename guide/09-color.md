## 9. Colour

Machine-readable: https://brand.flovatar.com/tokens/design-tokens.json · CSS variables: https://brand.flovatar.com/tokens/tokens.css

### 9.1 Core identity palette

**Print:** use the Pantone or CMYK values below; for digital use HEX/RGB. Sky Blue is **CMYK 38/0/4/0**; the 0/43/6/0 printed in the v1.0 PDF is a typo that would print orange, so never use it.

"The main colors of the Flovatar palette are Space Indigo and Aurora Pink, although they are supported by four secondary colors. … Tints should only be used when the main color has already been used." (v1.0 p.9)

| Name | HEX | RGB | Pantone | CMYK | Role |
|---|---|---|---|---|---|
| **Space Indigo** (primary) | `#411793` | 65 23 147 | Violet C | 93 99 0 0 | Brand fields, logo backgrounds, covers |
| **Aurora Pink** (primary) | `#EF2AC1` | 239 42 193 | 807 C | 27 82 0 0 | Logo mark, highlights, eyebrows, footer field |
| **Sky Blue** | `#91E3F9` | 145 227 249 | 0821 C | **38 0 4 0** | Wordmark on indigo, outline icons |
| **Nova Yellow** | `#FCEB4F` | 252 235 79 | 100 C | 5 1 77 0 | Attention, highlights |
| **Deep Space Blue** | `#1B0D49` | 27 13 73 | 275 C | 100 100 39 40 | Deepest backgrounds, dark text on light |
| **Solar Violet** | `#6657D3` | 102 87 211 | 2725 C | 77 71 0 0 | Secondary panels, illustrations |

### 9.2 Web UI palette (live flovatar.com, Nov 2026)

| Token | HEX | Where it's used |
|---|---|---|
| `night` | `#180830` | Page background |
| `night-violet` | `#1A083A` | Alternate section background |
| `royal-violet` | `#5F37CB` | Interactive violet, pills (roadmap "SERIES 1" chip) |
| `panel` | `#343B5A` | Stat panels, builder frame, filter bars (radius 10 px) |
| `panel-deep` | `#212741` | Inner panels |
| `ink` | `#1A1E2D` | Stat tiles, chunky button borders, frame outlines |
| `periwinkle` | `#AED7F7` | Big section headlines on dark |
| `neon-pink` | `#EB3CF2` | UI pink accent (top of page gradient, legendary) |
| `magenta-deep` | `#A21AA8` | Shade of neon pink |
| `cta-yellow` | `#FFEE50` | "Connect Wallet" button, nav links, epic |
| `cyan` | `#23EDFC` | Rare, data highlights |
| `buy-green` | `#52F618` | Buy/cart, selected-trait border, success ticks |
| `error-red` | `#F84F64` | Errors |
| `muted` | `#9DA4C7` | Secondary text |
| `tile-light` | `#F5F5F5` | Trait thumbnails / common |

**Signature gradients**
- Inner-page header glow: `linear-gradient(180deg, #ED2BEB 0%, #B822BD 25%, #7F198B 50%, #460F59 75%, #180830 100%)` over ~240 px (sampled from the live marketplace page).
- App-icon square: `linear-gradient(180deg, #440099, #230E54)`.
- Footer: a big **Aurora Pink** planet-horizon arc rising from the bottom of a starry night page, with a soft pink glow (`#FABCEB`) at the rim.

### 9.3 Rarity colours (product-wide; Flobits, traits, cards, filters)

| Tier | Fill | Edge / shadow | On-colour text |
|---|---|---|---|
| Common | `#F5F5F5` | `#AEAEAE` | `#1A1E2D` |
| Rare | `#23EDFC` | `#19A4AE` | `#1A1E2D` |
| Epic | `#FFEE50` | `#9F9427` | `#1A1E2D` |
| Legendary | `#EB3CF2` | `#A21AA8` | `#1A1E2D` |
| **Ultimate** (1/1 Flobits) | `#5A1268` + glitter (§9.3.1) | `#2E0A3A` · gold keyline `#FFC94D` | `#FFFFFF` |
| Spark (counter) | `#B196FE` | — | — |

Booster objects follow the same code: **Rare = cyan capsule, Epic = yellow capsule, Legendary = rainbow capsule** (Builder UI). Cards for listed items get a 3 px rarity-colour border; uncoloured (white) border = not boosted.

#### 9.3.1 Ultimate rarity (1/1 Flobits): darker purple with glitter

Use it for every Ultimate badge, card, frame and filter chip. Take the values from the tokens (`rarity.ultimate*`, `ultimate.css`) rather than hard-coding them.

| Token | HEX | Use |
|---|---|---|
| `rarity.ultimate` | `#5A1268` | Fill: deep grape purple (hue ≈ 290°). Darker than Legendary `#EB3CF2` and its edge `#A21AA8`, and clearly different from Space Indigo `#411793` and Royal Violet `#5F37CB`. |
| `rarity.ultimate-dark` | `#2E0A3A` | Edge, shadow, gradient end, text outline. |
| `rarity.ultimate-glitter-gold` | `#FFC94D` | Gold sparkles and the 1 px **gold keyline** around Ultimate shapes on dark pages. Warmer and deeper than Epic yellow `#FFEE50`, so it never reads as Epic. |
| `rarity.ultimate-glitter-white` | `#FFFFFF` | White sparkles and the label text. |

**Why these values:** white text on `#5A1268` is **12.2 : 1** (AAA), on `#2E0A3A` 17.2 : 1, and gold on the purple 8.0 : 1. The colour difference (CIELAB ΔE) is ≈ 59 from Legendary, ≈ 31 from the Legendary edge and ≥ 23 from every brand violet, so it reads as its own tier. Purple alone is too dark on Night `#180830` (1.5 : 1), so an Ultimate shape on a dark page always gets the gold keyline (12.3 : 1) and the glitter.

**Rules**
- **Never without glitter.** The fill is a 160° gradient `#5A1268` → `#2E0A3A` plus the glitter: fine, subtle sparkle dust, and the purple always dominates. **Size:** mostly dots of 0.75–2 px at 1×, plus a few tiny 4-point stars (≤ 3 px across); nothing bigger. **Colour:** about 60% white, 40% gold `#FFC94D`, at varied opacity (white 28–68%, gold 36–80%). **Distribution:** even, never a visible pattern. Points come from Poisson-disk (blue-noise) sampling with fixed seeds, so there are no clumps or gaps, and the glitter is three stacked transparent tiles of **509, 613 and 757 px** (prime sizes, each at its own offset: the "cicada principle"). The combined pattern only repeats every 509 × 613 × 757 px, so no screen or card ever shows a repeat. Keep the glitter behind the text.
- **Twinkle (optional):** layer 1 is static; layers 2 and 3 fade gently between 35% and 100% opacity, out of step (4.3 s and 6.7 s, alternating, different start offsets), opacity only, no movement. With `prefers-reduced-motion: reduce` they stop at 70% (static glitter). In video and GIFs, a slow, desynchronised twinkle of 3–7 s is fine; on print and static images use the static glitter.
- **Label:** always write **ULTIMATE** (Korolev Compressed Bold caps, white, like the other rarity labels). Colour is never the only signal (§13.7). The label stays in English, like COMMON / RARE / EPIC / LEGENDARY.
- **Cards:** the 3 px rarity border of marketplace cards becomes the glittering Ultimate gradient with a 1 px gold keyline outside (`.fl-ultimate-frame`).
- **Boosters:** there's no Ultimate Booster. Ultimate exists only for 1/1 Flobits.
- Don't use the Ultimate colours or glitter for anything that isn't an Ultimate item (no decorative sparkle on Legendary items, no purple-glitter campaign backgrounds).

**CSS** (https://brand.flovatar.com/tokens/ultimate.css; the glitter layers are https://brand.flovatar.com/tokens/ultimate-glitter-509.svg, https://brand.flovatar.com/tokens/ultimate-glitter-613.svg and https://brand.flovatar.com/tokens/ultimate-glitter-757.svg, transparent and seamless; keep their sizes and offsets as in the CSS). Usage: `<span class="fl-ultimate fl-ultimate-badge">ULTIMATE</span>`, `<div class="fl-ultimate-frame">…card…</div>`.

```css
{{include:tokens/ultimate.css}}
```

**SVG pattern** for SVG cards, frames and on-chain art (https://brand.flovatar.com/tokens/ultimate-glitter-pattern.svg). Copy the `<defs>`, fill the shape with `url(#fl-ultimate-fill)`, then draw it again once per glitter layer on top: `url(#fl-ultimate-glitter)`, `url(#fl-ultimate-glitter-2)`, `url(#fl-ultimate-glitter-3)` (the same 509/613/757 px blue-noise layers as the CSS). A shape up to 509 px never shows a repeat even with layer 1 alone:

```svg
{{include:tokens/ultimate-glitter-pattern.svg}}
```

<!--html:ultimate-->

<!--html:colors-->

### 9.4 Usage proportions [inferred from the site and covers]

~60% night/indigo backgrounds · ~20% panels and violets · ~10% Aurora/Neon Pink · ~5% Sky Blue/Periwinkle text · ~5% yellow CTAs and rarity accents. Pink and yellow are **accents**. Never set long body text in pink or yellow.

### 9.5 Contrast

{{include:tokens/contrast.md}}

**Rules from the table:** Aurora Pink on Space Indigo (3.26) and white on Aurora Pink (3.64) are **large-text / logo only**. For body text on pink use Deep Space Blue `#1B0D49`. All UI text on Night `#180830` passes AA.

### 9.6 Sub-brand palettes

Sportvatar and partner colours: §16.1 and §16.8.
