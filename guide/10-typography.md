## 10. Typography

"The Flovatar typefaces are all condensed so as to complement each other." (v1.0 p.10) Every brand typeface is condensed. Never use a wide geometric sans (Poppins, Montserrat and so on) for brand headlines. (flovatar.com still loads Poppins for a few legacy widgets. Don't copy that.)

### 10.1 Typefaces

| Role | Typeface | Source / licence | Use |
|---|---|---|---|
| **Display** | **Staatliches** Regular | Google Fonts (OFL) | Big headlines and page titles. "Short titles being set in uppercase throughout." Covers, banners, video titles (*A DUST ODYSSEY*). |
| **Headings** | **Korolev Condensed Bold** | Adobe Fonts (licensed by Flovatar) | "Carries a lot of the personality of Staatliches yet also possesses a lowercase set." Smaller headlines, section titles, all h1–h6 on flovatar.com. |
| **Numbers / nav / UI caps** | **Korolev Compressed Bold** | Adobe (licensed; self-hosted on flovatar.com) | Stats ("12,345 FLOW"), nav links, buttons, rarity labels. |
| **Body** | **Roboto Condensed** Regular/Bold | Google Fonts (OFL) | "Carries good legibility across multiple devices and at different sizes." Section headers (caps) and body copy. |

Webfonts for this guide's own pages (licensed, self-hosted) under `https://brand.flovatar.com/fonts/`: (`staatliches-latin.woff2` + `staatliches-latin-ext.woff2`, `korolev-condensed-bold.woff2`, `korolev-compressed-bold.woff2`, `roboto-condensed-latin.woff2` + `roboto-condensed-latin-ext.woff2`). Raw font files are **not** distributed. If a tool can't use Korolev, fall back to Staatliches (display) / Roboto Condensed Bold (headings).

**Agencies and freelancers:** third parties use the **fallback fonts**: **Staatliches** (display and headings) + **Roboto Condensed** (headings in Bold, body), the full Google Fonts families including the **latin-ext** subset so the Đ of ĐUST renders (§10.4). The Korolev files are licensed to Flovatar and are **not shared** with agencies or freelancers. Work that needs Korolev is finished by the Flovatar team.

**Not brand fonts** (legacy, avoid in new work): "name_smile" and "Bradley Hand" (site handwriting accents), Poppins, and the trading-card template fonts (Antenna, Ironmonger, United Sans).

<!--html:type-->

### 10.2 Hierarchy (v1.0 p.11 + live site)

| Level | Font | Case | Size desktop / mobile (px) | Line height | Colour on dark |
|---|---|---|---|---|---|
| Hero / Big headline | Staatliches or Korolev Condensed Bold | UPPERCASE | 55–72 / 40 | 0.9–1.0 | Periwinkle `#AED7F7` or white |
| H2 section | Korolev Condensed Bold | UPPERCASE | 50 / 40 | 0.9 | Periwinkle `#AED7F7` |
| Eyebrow | Korolev Condensed Bold | Sentence case | 17–20 | 1.1 | Aurora/Neon Pink |
| H3 | Korolev Condensed Bold | UPPERCASE or Title | 32 / 28 | 1.0 | White |
| H4–H6 | Korolev Condensed Bold | Title | 26 / 17 / 15 | 1.1 | White |
| Section header (in copy) | Roboto Condensed Bold | UPPERCASE | 16–18 | 1.25 | White |
| Body | Roboto Condensed Regular | Sentence | 16 | 1.25 (site) / 1.5 (long reads) | White; secondary `#9DA4C7` |
| Stats / numbers | Korolev Compressed Bold | — | 32–48 | 1 | White, or the rarity colour |
| Buttons / nav | Korolev Compressed Bold | UPPERCASE | 18–24 | 1 | Ink on yellow / yellow on night |

Rules: titles are "bold and punchy". **"BIG HEADLINES WITHOUT MANY WORDS"** (v1.0 specimen). Keep headline letter-spacing at 0 (the faces are already tight). Inline links in body copy are Periwinkle/Sky Blue; key phrases may be Aurora Pink ("StarDust depends on YOU!").

### 10.3 CSS starter

```css
@font-face { font-family: "Staatliches"; src: url(https://brand.flovatar.com/fonts/staatliches-latin.woff2) format("woff2"); font-display: swap; }
/* latin-ext subsets carry Đ (U+0110) for ĐUST; the browser only downloads them when the page uses such a character */
@font-face { font-family: "Staatliches"; src: url(https://brand.flovatar.com/fonts/staatliches-latin-ext.woff2) format("woff2"); font-display: swap; unicode-range: U+0100-02BA, U+1E00-1EFF, U+2C60-2C7F, U+A720-A7FF; }
@font-face { font-family: "Korolev Condensed"; font-weight: 700; src: url(https://brand.flovatar.com/fonts/korolev-condensed-bold.woff2) format("woff2"); font-display: swap; }
@font-face { font-family: "Korolev Compressed"; font-weight: 700; src: url(https://brand.flovatar.com/fonts/korolev-compressed-bold.woff2) format("woff2"); font-display: swap; }
@font-face { font-family: "Roboto Condensed"; font-weight: 100 900; src: url(https://brand.flovatar.com/fonts/roboto-condensed-latin.woff2) format("woff2"); font-display: swap; }
@font-face { font-family: "Roboto Condensed"; font-weight: 100 900; src: url(https://brand.flovatar.com/fonts/roboto-condensed-latin-ext.woff2) format("woff2"); font-display: swap; unicode-range: U+0100-02BA, U+1E00-1EFF, U+2C60-2C7F, U+A720-A7FF; }
body { font: 16px/1.25 "Roboto Condensed", "Arial Narrow", sans-serif; color: #fff; background: #180830; }
h1, h2, h3, h4 { font-family: "Korolev Condensed", "Roboto Condensed", sans-serif; font-weight: 700; }
.display { font-family: "Staatliches", sans-serif; text-transform: uppercase; line-height: .9; }
.eyebrow { font-family: "Korolev Condensed", sans-serif; font-weight: 700; color: #EF2AC1; }
```

(These font URLs are for Flovatar-owned properties. Agencies, freelancers and third-party agents use Staatliches / Roboto Condensed from Google Fonts, full families with latin-ext; Korolev isn't shared, §10.1.)

### 10.4 The Đ in ĐUST: glyph coverage and fallback

The brand spelling ĐUST (§7.4) needs **Đ, U+0110**. Checked in the font files on 2026-11-24:

| Font | Đ (U+0110) | Notes |
|---|:---:|---|
| Korolev Condensed Bold | ✅ | Licensed file. Also has đ (U+0111). |
| Korolev Compressed Bold | ✅ | Licensed file. |
| Staatliches, full family (Google Fonts) | ✅ | Đ is in the **latin-ext** subset. The latin-only subset (`staatliches-latin.woff2`) lacks it. |
| Roboto Condensed, full family (Google Fonts) | ✅ | Đ is in the **latin-ext** subset. The latin-only subset (`roboto-condensed-latin.woff2`) lacks it. |

**Fallback rule.**
1. **Web:** load the latin-ext subset next to the latin one, with `unicode-range` (CSS in §10.3; this site does it). The browser fetches it only for pages that use Đ.
2. **Design tools and image generators:** install the full Staatliches / Roboto Condensed families, not web subsets. If a tool still shows a box (tofu) or a plain D, set only the Đ in **Korolev Compressed Bold** (display) or **Korolev Condensed Bold** (text), matched to cap height (Flovatar team only). Agencies and freelancers don't have Korolev: they use **Arial Narrow Bold** or Arial for that one glyph.
3. **CSS stacks** already fall back per glyph: display `'Staatliches', 'Korolev Compressed', …`, body `'Roboto Condensed', 'Arial Narrow', Arial, …` (tokens §9).
4. Never fake the Đ by drawing a line over a D, and never swap in Ð (U+00D0).
5. Check every ĐUST headline in the final export (PNG or video frame) before shipping.
