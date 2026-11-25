## 12. SVG construction & series anatomy

Every Flovatar-family image is a stack of **on-chain SVG fragments** ("templates") joined into one `<svg>` document. This section explains how the fragments are built for each series, how they join visually and in code, how combos and rarity work, and how to add new assets without breaking anything that already exists. All numbers are measured on the live on-chain templates (Series 1: 756 Flovatar templates; Flobots: 144; Psyche Likee: 154) and on the images the site renders. The drawing style itself (outline, shading, pose) is §11. Look at any template as a standalone SVG at `https://flovatar.com/api/image/template/{templateId}`.

### 12.1 The shared model (all series)

- **One canvas, one registration.** Every fragment is drawn on the full `viewBox="0 0 3000 3000"` square at its final position. Parts are never moved, scaled or offset when they're composed: a hat is drawn where a hat sits on the head.
- **Fragments, not documents.** A template has no `<?xml>`, no DOCTYPE and no `<svg>` element. It is `<defs>`/`<style>` plus drawing elements, ideally inside one root `<g id="…">`. The wrapper is added at composition time (code below).
- **Plain concatenation.** Fragments are appended as direct children of the root `<svg>`, in a fixed order per series. Later fragments paint over earlier ones. No per-layer `<g>` wrapper, transform or nested `<svg>` is added.
- **One shared document.** Because the fragments end up in one document: a `<style>` in any fragment applies to the **whole** image; every `id` must be unique across everything that can be composed together (`url(#id)` resolves to the first match in the document); and CSS sibling selectors (`#A ~ #B`) can react to fragments that come **earlier**. That's how the hidden combos (§12.8) and cross-layer joins (§12.3) work.
- **Templates are immutable.** Optional slots (Flobits, Flobot parts, Psyche Likee layers) are read live from their template, and combos refer to other templates' exact ids and classes. Changing one byte of an existing template can change or break every NFT that uses it. New art = a **new** template (§12.10).

The composed document:

```xml
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 3000 3000" width="100%" height="100%">
  <!-- fragment 1 (bottom) --><!-- fragment 2 --> … <!-- fragment n (top) -->
</svg>
```

| Series | Canvas | Wrapper | Layer order, bottom → top (as on flovatar.com / sportvatar.com) | Uniqueness key |
|---|---|---|---|---|
| **Flovatar** (Series 1) | 3000 × 3000 | plain wrapper above | background → body → clothing → hair → eyes → nose → mouth → facialHair → accessory → eyeglasses → hat | `B{body}H{hair}F{facialHair or x}E{eyes}N{nose}M{mouth}C{clothing}` (core traits only) |
| **Flobot** | 3000 × 3000 | wrapper + `fill="#000"` | background → legs → body → arms → head → face | `B{body}H{head}A{arms}L{legs}F{face}` |
| **Psyche Likee** (ĐUST collectible series 1) | 3000 × 3000 | the series' own prefix/suffix (same as above) | layer 1 Background → 2 Legs → 3 Body → 4 Arms → 5 Head → 6 Face → 7 Accessory Left → 8 Accessory Right | `S1-L2_{id}-L3_{id}-L4_{id}-L5_{id}-L6_{id}` (layers 2–6) |
| **Sportvatar** | 3000 × 3000 | series prefix that already holds the floor shadow ellipse | 1 background → 2 body → 3 clothing → 4 nose → 5 mouth → 6 facialHair → 7 hair → 8 eyes → 9 eyeglasses → 10 hat → 11 shoes → 12 accessory → 13 numbers → 14 modifiers | `S{series}-L2_{id}…-L8_{id}` (layers 2–8) |
| **Asteroid Island** | 3025 × 4033 portrait | — | see §11.6 and §16.5 | — |

**Images always use the site order above.** The Flovatar contract's own `getSvg()` appends the Flobits as eyeglasses → hat → accessory, and the Flobot contract's as arms → legs → body → head → face. Those orders break combos that the site order shows (§12.8), so every render, preview and export uses the site order.

### 12.2 Flovatar anatomy (Series 1)

<!--html:anatomy-->

**Where things live** (median bounding box of all Series 1 templates per category, 3000-unit canvas; sizes = median / 90th percentile / max of the fragment in KB):

| Layer | Category | Templates (C/R/E/L) | Box (x, y) | Size KB | Animated | Carries combos |
|---|---|---|---|---|---|---|
| 1 | background (Flobit) | 68 (1/26/36/5) | full canvas 0–3000 | 75 / 219 / 518 | 38 | 1 |
| 2 | body (core) | 39 (10/11/11/7) | x 720–2360, y 700–2740 | 18 / 54 / 91 | 16 | 0 |
| 3 | clothing (core) | 136 (49/56/20/11) | x 800–2330, y 1670–2740 | 11 / 19 / 77 | 0 | 0 |
| 4 | hair (core) | 99 (50/27/16/6) | x 800–2150, y 630–1620 | 5.5 / 9 / 27 | 0 | 0 |
| 5 | eyes (core) | 29 (6/4/14/5) | x 1200–2170, y 1080–1450 | 10 / 21 / 39 | 19 | 0 |
| 6 | nose (core) | 10 (3/3/2/2) | x 1640–1880, y 1210–1420 | 0.7 / 1.5 / 2 | 0 | 0 |
| 7 | mouth (core) | 25 (7/6/8/4) | x 1530–1940, y 1460–1650 | 4 / 8 / 12 | 12 | 0 |
| 8 | facialHair (core, optional) | 21 (0/12/8/1) | x 1320–2120, y 1330–1900 | 3.3 / 5.4 / 6 | 0 | 0 |
| 9 | accessory (Flobit) | 196 (12/104/64/16) | x 1610–2420, y 1610–2360 | 11 / 47 / 235 | 69 | 43 |
| 10 | eyeglasses (Flobit) | 41 (10/15/12/4) | x 1110–2240, y 980–1510 | 4.7 / 11 / 17 | 3 | 5 |
| 11 | hat (Flobit) | 88 (11/31/26/20) | x 720–2210, y 400–1140 | 7 / 34 / 96 | 19 | 25 |
| — | spark, rarity boosters | 1 + 3 | x 920–2080, y 920–2080 (centred icon) | 44 / 15 | all | 0 |

**Anchors of the base pose** (identical in every body template, so every trait fits every body):

| Anchor | Position on the 3000 canvas |
|---|---|
| Head dome | x ≈ 730–2160 at its widest (y ≈ 1275), top at y ≈ 720, centre line x ≈ 1450–1475. The head is ≈ 44% of the figure height. |
| Ear | one half-circle ear on the viewer's left, x ≈ 730 |
| Eye zone | x 1200–2170, y 1080–1450: near eye (left of the pair) larger, far eye touching the head's right edge |
| Chin / collar line | y ≈ 1620–1670. There's **no neck**: the head sits on the torso. |
| Raised fist (viewer's right) | x ≈ 1990–2360, y ≈ 1640–2160, the default hold point for accessories |
| Lowered hand (viewer's left) | x ≈ 820–1200, y ≈ 1980–2560 |
| Feet / ground | soles at y ≈ 2745; ground-shadow ellipse `cx 1335 cy 2682 rx 612 ry 59`, black at 27% (drawn by the body) |
| Hands | **mittens**: one rounded mitt plus a small thumb lobe, no separate fingers |

**How the layers join visually:**

- **Body** carries the whole figure: head, ear, torso, arms with mitten hands, legs, feet and the ground shadow. Every other layer is drawn on top of this pose.
- **Clothing** covers torso, legs and feet (trousers, shoes) and the upper arms (sleeves). Its top edge follows the head's lower outline exactly, so the head reads in front of the collar. Mittens stay visible below the cuffs.
- **Hair** sits above clothing (long hair may fall on the shoulders) and below the eyes, so bangs stop above y ≈ 1080 or go around the eyes. Hair never covers the face zone.
- **Eyes, nose, mouth** sit in fixed zones on the right half of the face and don't overlap each other.
- **Facial hair** sits above the mouth and nose (moustaches overlap the top lip) and meets the hair at the sideburns. The Builder preview draws hair above facial hair, while the minted image draws facial hair above hair, so the seam has to look right in both stackings.
- **Eyeglasses** sit on the eye zone, above the accessory and below the hat.
- **Hats** cover the dome (median y 400–1140). A hat that must hide big hair ships a **hair mask**: a `<clipPath>` plus a CSS rule that targets the hair templates' root ids and namespaced classes, for example `#Hair_Dreads, path[class$="-351"] { clip-path: url(#sombrero_hair_mask); }`.
- **Accessories** are held in the raised fist or worn (capes, jetpacks, wings). Parts that must appear **behind** the body use a canvas-sized inverted `<clipPath>` (the canvas minus the body silhouette). 52 Series 1 accessories do this.
- **Backgrounds** fill the full square edge to edge (paths or rects from 0 to 3000) and keep the centre readable behind the character (footprint ≈ 24–79% of the width, §11.1).

### 12.3 How fragments join in code

Rules for every series:

| Do | Don't |
|---|---|
| Ship a fragment: `<defs>`/`<style>` + one root `<g id="…">` with a unique, descriptive id (`id="spartan_helmet"`, `id="Bear-Blue" class="legs"`) | Ship `<?xml>`, DOCTYPE, `<svg>` or a nested `<svg>` with its own viewBox |
| Namespace **every** id, class, gradient, clipPath, mask, filter and keyframe name with a per-template token (Series 1 uses a numeric suffix: `.cls-2-51`, `Scene-1-33`) | Reuse generic names (`clip-path`, `shadow`, `linear-gradient`): the legacy set already has 207 duplicate ids, and a duplicate makes `url(#…)` point at another layer's element |
| Start every selector with your root id or a namespaced class (`#spartan_helmet .plume {…}`) | Write global selectors (`path {…}`, `.st0 {…}`, `g {…}`): they restyle every other layer |
| Write cross-layer rules on purpose only: combos (§12.8), hair masks, behind-the-body clips, stack motion (Flobot/Psyche legs) | Restyle or hide another template by accident |
| Give the root `<g>` a `class` equal to the layer name in part-based series (`legs`, `body`, `arms`, `head`, `face`) | Change or drop those classes: other layers animate the stack through them |
| Fill and stroke with hex colours (CSS classes, `style` or presentation attributes) | Rely on `currentColor`, inherited fills or external CSS |
| Outline text: convert lettering to paths | Use `<text>`, fonts, `<image>` rasters (a few legacy flags embed JPEGs; don't add more), `<foreignObject>`, `<script>`, external `href`s |
| Make the **first frame** (t = 0) and the **default state** a complete, good-looking image | Rely on an animation having run: static renderers freeze SMIL at t = 0 and CSS animations at their start or end state, and many viewers don't run combos |
| Animate with CSS `@keyframes` (`transform-box: fill-box`, `transform-origin` in px) or SMIL `<animate>`/`<animateTransform>`, seamless loops ≤ 5 s | Put filters (`feGaussianBlur`) on large areas or animate filters: they're slow in every renderer |
| Keep coordinates at ≤ 2 decimals and the whole fragment on one line (newlines are collapsed at import) | Put tabs or meaningful whitespace in the SVG string |

**Part-based series share a class API.** Flobot and Psyche Likee part roots are `<g id="Name-Part" class="legs|body|arms|head|face">`. Because the class names are stable, one layer can drive the others:

- **Stack motion:** hovering or stomping legs animate the upper parts with `.face, .head, .body, .arms { animation: float 3s infinite; }` (`@keyframes float` moves them `translate(0, -50px)` and back).
- **Behind-the-body clip (Psyche Likee):** each body ships `<clipPath id="body-mask">` (the canvas minus the body silhouette) and `.arm-back { clip-path: url(#body-mask); }`. Each arms template splits into `.arm-back` and `.arm-front` groups, so the far arm disappears behind the body although the arms layer is drawn above it.
- **Shared colour and expression hooks (Psyche Likee):** `.leg-color`, `.body-color`, `.arm-color`, `.head-color`, `.eye-pupil`, `.eye-blink` (every face blinks).

### 12.4 Flobits, Sparks and rarity

- A **template** stores: name, category, colour, description, `svg` (the fragment), series, rarity and the maximum mintable count. A **Flobit** is an NFT that points at a template; its art is always read from that template.
- **Edition size defines rarity** (Series 1 and Flobot parts): Common 1,000 · Rare 250 · Epic 50 · Legendary 10 per template.
- **Core traits** (body, hair, facial hair, eyes, nose, mouth, clothing) aren't NFTs: a **Spark** unlocks every Common core trait, and each Rare, Epic or Legendary core trait needs **one Rarity Booster of the same tier**. The contract requires the exact count per tier and checks that every trait, Flobit and booster has the Spark's series. The Spark and boosters are burned at mint.
- The core fragments are **baked into the Flovatar at mint** (concatenated body → clothing → hair → eyes → nose → mouth → facialHair). The four **Flobit slots** (background, accessory, eyeglasses, hat) are swappable and read live from their templates.
- **Rarity score:** each core trait counts 1 (Common), 5 (Rare), 25 (Epic) or 125 (Legendary), normalised to 0–100 over six slots.
- **"Flobit Series 2"** (the Aug 2022 pack) is a product name. On chain those Flobits are Series 1 templates, because a Flobit must share the series of the Flovatar's Spark.

### 12.5 Flobots

<!--html:anatomy-family-->

| Part (site order) | Templates (C/E/L) | Box (x, y) | Size KB (median / p90) | Joins |
|---|---|---|---|---|
| background | Flovatar Series 1 background Flobits | full canvas | — | Flobots wear Flovatar backgrounds |
| legs | 28 (20/5/3) | x 940–2040, y 1980–2710 | 9.9 / 18.5 | also ships `<g id="legs-shadow">`, a ground ellipse at 20% black; hover legs move the upper stack |
| body | 26 (20/4/2) | x 980–2020, y 1260–2140 | 6.6 / 14.7 | the hub: arms, head and legs attach to its fixed sockets |
| arms | 27 (20/4/3) | x 650–2350, y 1540–2380 | 11.8 / 31.9 | one arm often raised (pointing, holding a tool) |
| head | 29 (22/6/1) | x 1070–1930, y 610–1410 | 3.4 / 10.2 | sits on the body's neck socket |
| face | 31 (24/5/2) | x 1250–1750, y 920–1270 | 3.1 / 4.5 | screen or eyes on the head's front plate |

- Construction kit: 1 **Flobot Constructor Kit** (or 5 of one tier to step up). The Flobot's rarity is its highest part rarity, and the kit's tier must be at least that.
- Look: white/grey panels `#D1D1D1`, dark metal `#303030` / `#59534D` / `#4B4F56`, orange `#FF7C10` and cyan `#27EBFF` accents, 13-unit black outline, shadow tone = black at 10–20%.

### 12.6 Psyche Likee (ĐUST collectible series)

| Layer | Name | Templates (C/R/E/L) | Box (x, y) | Size KB (median / p90) | Notes |
|---|---|---|---|---|---|
| 1 | Background | accessory slot | full canvas | — | optional, not part of the uniqueness key |
| 2 | Legs | 34 (17/7/8/2) | x 940–1920, y 2070–2750 | 8.2 / 13.4 | `.leg-color`; some move the stack (stomp, bounce, dance) |
| 3 | Body | 34 (15/11/6/2) | x 800–2120, y 1550–2480 | 4.3 / 10.1 | every body ships the `body-mask` clip (§12.3) and a `neck-shadow` |
| 4 | Arms | 23 (8/8/4/3) | x 510–2220, y 1700–2460 | 5.6 / 10.5 | `.arm-back` (clipped behind the body) + `.arm-front` |
| 5 | Head | 33 (16/8/7/2) | x 690–2190, y 840–1970 | 7.6 / 29.4 | ears, horns, tufts; matching sets can chain combos (`#Unicorn-Legs ~ #Unicorn-Body ~ #Unicorn-Head …`) |
| 6 | Face | 30 (15/7/6/2) | x 900–1580, y 1240–1740 | 5.9 / 9.9 | all faces blink (`.eye-blink`) |
| 7, 8 | Accessory Left / Right | accessory slots | — | — | optional, not part of the uniqueness key |

- A series is defined on chain by an SVG prefix and suffix, its numbered layers (each flagged core or accessory) and a price curve. The image is prefix + each layer's fragment in layer-number order + suffix, so layer numbers must run from 1 without gaps.
- Each mint of a trait raises that trait's ĐUST price for the next minter.

### 12.7 Line, colour and shading in SVG terms

| Property | Measured value | Rule for new art |
|---|---|---|
| Outline colour | `#000` (99% of strokes) | Black outlines only. White/colour strokes for glows and highlights only. |
| Main contour | **13** units (Series 1 core: 514 of 900 stroke rules; Flobits 4,269; Flobots 2,735; Psyche 1,139) | 13 on contours; 11–12 inner lines; 6–10 details; 1–4 texture |
| Line caps | `round` (≥ 96%) | `stroke-linecap: round` |
| Line joins | `round` on Flobits, Flobots and Psyche; `miter` (limit 10) in older core art | `stroke-linejoin: round` for new art |
| Shadow tone | one black shape over the fill at 13–32% opacity (Series 1 core 18–32%, Flobits and Flobots 20%) | [inferred] One shadow shape per form on the side away from the upper-left light, black at **20%** (core traits 20–32%) |
| Highlight | white shape at 20–40% opacity | Optional, small, upper left |
| Ground shadow | Flovatar 27% black (in the body); Flobot 20% (in the legs); Sportvatar 20% (in the prefix) | Ground shadows belong to the bottom-most character layer |
| Gradients | ~15% of templates, mostly backgrounds, glass and glows | No gradients on skin or cloth |
| Skin (Common bodies) | `#C29D84` `#6D5341` `#F0D6C2` `#ADAAAF` `#FF9494` `#FFBA7B` `#D3FFA9` `#FFB8FA` `#DDA9FF` `#FFFFFF` | One flat fill per body; rarer bodies add pattern or creature detail (§11.4) |

### 12.8 Hidden combos: how they work

<!--html:combos-->

A combo is CSS inside one template that changes that template when another specific template is present **earlier** in the document. About 75 Series 1 templates carry combo rules (≈ 10%), plus a few Flobot and Psyche Likee parts.

```css
/* inside the Lasso accessory template (root <g id="lasso">) */
#lasso-spin { display: none; }                          /* default: static rope, spinning rope hidden */
#COWBOY ~ #lasso #lasso-static { display: none; }       /* trigger: root id of the Cowboy clothing */
#COWBOY ~ #lasso #lasso-spin { display: inline; }       /* swap in the spinning rope */
```

- **Anatomy:** `TRIGGER ~ #OWN_ROOT #OWN_PART { … }`. The trigger is an element of another template that comes earlier among the root's children: its root id (`#COWBOY`, `#circus`, `#Hair_Fluf`), or its first element's namespaced class when it has no root group (`.cls-1-117`, `path[class$="-117"]`). The target always sits inside the combo template's own root.
- **Effects in use:** reveal hidden parts (`display:none` or `opacity:0` → shown), swap a default part for an alternate (`#lasso-static` → `#lasso-spin`), recolour, clip the revealed outfit around the beard or moustache in place (`clip-path` per facial hair), move the whole stack (legs), and reveal with staggered fade-ins (`animation-delay` 0.5–2 s, `animation-fill-mode: forwards`).
- **Chains:** `#A ~ #B ~ #TARGET` needs two triggers in order, for example a matching background and outfit.
- **Direction:** a target can only react to fragments **before** it. In the site order that means:

| Combo lives in… | can react to… |
|---|---|
| hat | background, any core trait, accessory, eyeglasses |
| eyeglasses | background, any core trait, accessory |
| accessory | background, any core trait |
| a core trait | background only (avoid: core order differs between Builder preview and minted image) |
| background | nothing (it's first): backgrounds can only be triggers |

- **Marketing rule:** combos are easter eggs. Hint at them, never publish the full list (§11.1).

### 12.9 Uniqueness ("combinations" in the contract)

- Each series keeps a registry of minted **combination keys** (table in §12.1). Minting panics if the key already exists. The Builder checks availability before minting and shows "Combination unavailable" when it's taken.
- Only **core** parts are in the key: Flovatar core traits (facial hair `x` when absent), the five Flobot parts, Psyche Likee layers 2–6, Sportvatar layers 2–8. Backgrounds, Flobits and accessory layers never make a Flovatar unique.
- Keys are built from **template ids**. Adding a template creates new free combinations and can never collide with minted keys. Re-using or editing an id would change the meaning of keys that are already minted.
- Names are unique too (Flovatar: 3–31 characters).

### 12.10 Making new assets safely

**Golden rules:**
1. **Never modify an existing template.** Not its art, ids, classes, whitespace or order. Existing Flovatars, Flobits and combos depend on it byte for byte. A fix or a variant is a **new** template.
2. **New combos go in the new template.** Reference existing templates' ids and classes exactly as they are, and only triggers that come earlier in the site order (§12.8).
3. **Compose in the site order** for every preview, render and export (§12.1).
4. **Test on Flow testnet first:** create the template, mint with it, compose, render, compare, then repeat on mainnet. Creating templates is an admin-only action.

**Recipe for a new trait, Flobit or part:**
1. Draw on the 3000 canvas over a reference composite (a Common body for Flovatar traits). Stay inside the category's box (§12.2, §12.5, §12.6) and hit the anchors: fist hold point, eye zone, dome, chin line, feet.
2. Style per §11.2 and §12.7: 13-unit black round outlines, flat fill, one 20% black shadow shape, optional white highlight.
3. Structure per §12.3: one root `<g id>` (plus `class` = layer for part-based series), namespaced ids/classes, scoped CSS, no rasters or text.
4. Animate only if it adds something. The first frame and default state must stand alone.
5. **Budget [inferred]:** keep a new fragment near the category median and under the 90th percentile (§12.2 tables). Hard ceilings: core traits ≤ 20 KB (body ≤ 30 KB), eyeglasses ≤ 15 KB, hats and accessories ≤ 40 KB, Flobot/Psyche parts ≤ 20 KB, backgrounds ≤ 150 KB. The mint transaction concatenates the core fragments on chain, so its cost grows with their total size: mint the heaviest combination that includes the new trait on testnet.
6. Optimise **only the new file, before its first upload** [inferred: safe settings]. With SVGO, use the config below, which keeps the structure intact. These are switched off because they rename ids (combos break), drop `display:none` parts (combo reveals vanish), delete clipPaths used only from CSS, or merge and regroup shapes (stacking and selectors change). Never run an optimiser over existing templates.
7. **Name** in Title Case, ≤ 3 words, variant last (`Racing Helmet`, `Beard Black`). Root id = the name in kebab or snake case.

SVGO config for step 6 [inferred]:

```js
// svgo.config.js: safe for Flovatar fragments (wrap in <svg> to run, strip the wrapper after)
module.exports = { multipass: true, js2svg: { pretty: false }, plugins: [{ name: 'preset-default', params: { overrides: {
  cleanupIds: false, inlineStyles: false, minifyStyles: false, mergeStyles: false,
  removeHiddenElems: false, removeUselessDefs: false, removeEmptyContainers: false,
  collapseGroups: false, moveElemsAttrsToGroup: false, moveGroupAttrsToElems: false, mergePaths: false,
  cleanupNumericValues: { floatPrecision: 2 }, convertPathData: { floatPrecision: 2 } } } }] };
```

### 12.11 SVG QA checklist (new assets)

- [ ] Fragment only (no `<svg>`, `<?xml>`, DOCTYPE), one root `<g id>` and, for part-based series, `class` = layer name.
- [ ] Every id, class, gradient, clip, mask, filter and keyframe name is namespaced. No id collides with any existing template of the series.
- [ ] Every CSS selector starts with the template's root id or a namespaced class, except intended cross-layer rules.
- [ ] No `<text>`, `<image>`, `<foreignObject>`, `<script>`, external `href`, or fonts.
- [ ] Outline `#000`, 13 units on contours, round caps and joins, one shadow tone, no gradients on skin or cloth.
- [ ] Inside the category's box, aligned to the anchors, fits all body shapes of its series (render it on at least the Common body, one creature body and the widest body).
- [ ] Hats rendered over the biggest hairstyles (hair mask if hair pokes through); eyeglasses over every eye type; facial hair over every mouth and with the hair seams; clothing under long hair; accessories with and without capes, wings and jetpacks.
- [ ] Composed in the **site order**, rendered in a browser **and** in a static renderer (first frame). Default state looks complete with no trigger present.
- [ ] Each combo fires with its trigger(s) and does nothing without them, and the trigger comes earlier in the site order.
- [ ] Size within budget; heaviest core combination minted on testnet.
- [ ] Existing templates untouched: their SVG strings are byte-identical before and after the release.
