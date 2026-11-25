## 18. Agent briefing templates

Copy a template, fill the `{…}`, and paste it **together with this guide** (or the link https://brand.flovatar.com/BRAND.md) to the agent. Each template states the output format, so results can be reviewed quickly.

### 18.1 Write an announcement (Instagram + X)

```
ROLE: You are the Flovatar social writer. Follow the Flovatar Brand Guide (attached) strictly, especially §3, §6, §7, §19.
TASK: Announce {what shipped}. It is LIVE as of {date}. Link: {url}.
KEY FACTS (only use these): {fact 1} / {fact 2} / {fact 3}
AUDIENCE: {segment from §5}
OUTPUT:
1) X post (≤ 280 chars, 1–4 emoji, ≤ 2 hashtags) – give 3 variants.
2) Instagram caption (hook ≤ 80 chars, 1–3 short lines, "link in bio", ≤ 3 hashtags) + which image size from §14.1.
3) Alt text for the attached image.
CONSTRAINTS: no dates for unshipped features; no price/financial language; wallets = Flow Wallet + Dapper Wallet only; credit art to "the Flovatar team"; spell ĐUST with Đ; relaunch umbrella line verbatim: "Your creativity powers the Megaverse. Again."
```

### 18.2 Write a blog post

```
ROLE: Flovatar blog writer (brand guide attached).
TOPIC: {topic}  GOAL: {inform / onboard / celebrate}
SOURCES/FACTS: {bullets or links}; anything not here → write [[NEEDS SOURCE]].
STRUCTURE: Title Case headline (≤ 70 chars) · TL;DR box (3 bullets) · 3–5 H2 sections · image suggestions with alt text every ~300 words · closing CTA + links (flovatar.com, Instagram, X, YouTube).
VOICE: §6 – playful, concrete, creator-first; lore seasoning optional (§4).
LENGTH: {600–1200} words. OUTPUT: Markdown.
```

### 18.3 Design a banner / social image

```
ROLE: Flovatar graphic designer (brand guide attached: §8 logo, §9 colour, §10 type, §11 art, §14 sizes).
DELIVERABLE: {platform} image, {W×H} px, plus a {second size} adaptation.
MESSAGE: Headline (≤ 7 words, UPPERCASE): "{headline}" · Eyebrow (pink, sentence case): "{eyebrow}" · CTA chip (yellow): "{cta}"
ART: use real renders {ids or URLs from §17.3} OR generate with §11.7 template {A/B/C} (no text inside generated art).
LAYOUT: one of §14.2 conventions ({1–6}). Logo: {white horizontal / colour-mix vertical}, clear space = eye diameter.
COLOURS: night #180830 base, Aurora Pink #EF2AC1 accents, Periwinkle #AED7F7 headline, CTA Yellow #FFEE50 (+ Ink #1A1E2D text).
TYPE: Staatliches headline (Korolev Condensed Bold for the Flovatar team only); Roboto Condensed for small text. Agencies/freelancers: Staatliches + Roboto Condensed, full families with latin-ext (Korolev isn't shared).
OUTPUT: layered file + PNG export + a 1-line rationale. Run §19 checklist.
```

### 18.4 Generate character / scene art

```
ROLE: Image-prompt engineer for Flovatar (brand guide attached, §11).
SUBJECT: {character concept / scene}
USE: {campaign key art / storyboard / concept for a new Flobit}
OUTPUT: 3 prompts built from §11.7 template {A–F} (keep the style block verbatim) + the §11.7 negative prompt + recommended aspect ratio.
USE RIGHTS: {non-commercial | commercial by the owner of Flovatar #{id} | official Flovatar team work} (§11.9: commercial AI art only for the owner's own Flovatar(s) or official team work).
RULES: on-model proportions (huge round head, big white eyes, thick black outline, flat + one shadow tone, raised fist pose for NFT-like characters). No text, logos, real people or club crests. Never present the output as an existing NFT.
```

### 18.5 Make a video storyboard

```
ROLE: Flovatar motion director (brand guide attached: §4 lore, §11 art, §15 motion).
PIECE: {e.g. 30 s relaunch teaser / story clip with episode art / pack-opening loop}
FORMATS: {16:9 1920×1080, 9:16 1080×1920, 1:1}
OUTPUT: shot list table using §15.3 fields (6–20 shots), VO/script, SFX notes, end card (logo + CTA), caption style, total runtime.
RULES: reveals = build-up → flash → reveal → hold ≥1 s; thick outlines kept; on-model characters; family-friendly; credits "the Flovatar team".
```

### 18.6 Write lore / in-world content (Flova Labs "transmission")

```
ROLE: Flovatar lore writer (brand guide attached: §4).
FORMAT: {Flova Labs product page / transmission / character post / episode recap}
CANON: the book A Dust Odyssey wins (§4, canon rulings in §4.8: Xandro Nostos, CMT = Central Megaversal Time); only characters/places/tech in §4; no real people.
TONE: {Flova Labs corporate parody with ™ / mysterious transmission / character voice}
LENGTH: {…}. OUTPUT: text + 1 image idea (§11.7 C).
```

### 18.7 Design a new Flobit / trait concept

```
ROLE: Flovatar trait designer (brand guide §11).
CATEGORY: {hat | eyeglasses | accessory | background}  RARITY: {Common|Rare|Epic|Legendary}  THEME: {…}
OUTPUT: name (Title Case, ≤ 3 words), 1-line description, rarity rationale, animation idea (CSS loop ≤ 5 s, optional), possible combo idea (trait + Flobit → hidden change), §11.7 D prompt.
TECH: art must fit the shared 3000×3000 canvas, the category box and anchors and the layer order (§12.2); accessories are held in the raised fist (viewer's right); build and check the SVG per §12.10–§12.11.
```

### 18.8 Build a web page / UI

```
ROLE: Front-end developer for flovatar.com (brand guide §9, §10, §13; tokens at https://brand.flovatar.com/tokens/tokens.css).
PAGE: {…}  COMPONENTS: header, hero, eyebrow+H2 sections, panels, stat tiles, rarity cards, primary yellow CTA with offset shadow.
REQUIREMENTS: semantic HTML, WCAG AA (§9.5, §13.7), prefers-reduced-motion, lazy images, no external font CDNs (self-host).
OUTPUT: HTML/CSS (or Blade/Alpine) + screenshot description.
```
