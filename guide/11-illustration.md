## 11. Illustration & character style

This section describes how real Flovatar art is built, measured on the on-chain SVG templates (756 Series 1 templates) and the site renders. It ends with image-generation prompt templates. Visual reference: the sample gallery at https://brand.flovatar.com/illustration/index.html

### 11.1 How a Flovatar is built (technical)

- **Canvas:** square SVG, `viewBox="0 0 3000 3000"`. Every layer shares the same canvas and registration, so layers stack with no offsets.
- **Layer order (bottom → top), as on flovatar.com:**
  `background` → **core** [`body` → `clothing` → `hair` → `eyes` → `nose` → `mouth` → `facialHair`] → `accessory` → `eyeglasses` → `hat`
  (Core order from `Flovatar.cdc`; Flobit order from the site's `full_svg`. Construction rules for every series: §12.) Hats always go on top, eyeglasses over accessories. **Order matters:** hidden combos are CSS sibling selectors (`#trigger ~ #target`) that only fire in this order.
- **Core traits (7, fixed at mint):** Body, Hair, Facial Hair, Eyes, Nose, Mouth, Clothing. **Flobits (4, swappable):** Hat, Eyeglasses, Accessory, Background.
- **Character footprint** (no background): about **24–79% of the width** and **17–92% of the height**. The figure is centred, its feet sit at ~91.5% of the height, and a soft ground-shadow ellipse sits under them. Leave the top ~15% for hats and halos.
- **Animation** is native SVG: CSS `@keyframes` (85 templates) and SMIL `<animate>` (110 templates). Typical motions: floating ±100 units over 5 s ease, spinning, pulsing glows, flicker, fade-in reveals with 1 s delays. Loops are seamless. Animation is concentrated in backgrounds (38 animated), accessories (69), hats (19) and eyes (19).
- **Combos:** specific trait + Flobit sets trigger hidden changes, e.g. Axe + Lumberjack Red → a *The Shining* homage; Proton Pack + Jail → Ghostbuster (+ New York background → Slimer). They're easter eggs. Hint at them, never list them all in marketing.

### 11.2 Line, shape and shading

- **Outline:** solid black `#000`, round caps and joins. Main contour ≈ **13 px on the 3000 px canvas (≈ 0.43% of the width)**. Inner details 6–10 px, fine texture 1–4 px. Line weight is **uniform** (no tapering brush), like a clean vector cartoon.
- **Fills:** flat, saturated-but-soft colours. **One shadow tone** per shape, made as a black (or darker hue) shape at **13–32% opacity** (most common: 20%) laid over the fill along one side (light comes from the upper left). There are occasional small white highlight shapes. **No** soft airbrush gradients in characters. Gradients appear in ~15% of templates, mainly backgrounds, glass and glow effects.
- **Ground shadow:** a flat black ellipse at ~27% opacity under the feet.
- **Shapes:** rounded, chunky, bean-like. No sharp realism. Hands are **mittens**: one rounded mitt plus a small thumb lobe, no separate fingers.

### 11.3 Proportions and pose (the Flovatar silhouette)

- **Chibi:** the head is about **45% of the total figure height** and wider than the body. The cranium is a big smooth dome; ears are small half-circles on the side.
- **Three-quarter view facing the viewer's right:** the single visible ear sits on the left side of the head (viewer's left), and the face features are shifted to the right half of the head.
- **Signature pose:** standing, short stubby legs slightly apart, **one fist raised to shoulder height on the viewer's right** (a "ready/flex" gesture, often holding the accessory), the other arm relaxed down at the side. The same base pose is used for every Flovatar, so traits fit everyone.
- **Eyes:** two big round white eyeballs with black outlines and a grey inner shadow crescent, on the right half of the face. The **near eye (left of the pair) is larger**; the far eye is smaller and touches the right edge of the head. Pupils are simple black vertical ovals/dots looking forward or sideways. Variants: X-eyes, angry lids, glowing robot eyes, sleepy lids and so on.
- **Nose:** small (button, triangle, pig, clown…). **Mouth:** small and expressive (smirk, grin, open "O", tongue out, fangs).
- **Expression:** cheeky, confident, a bit goofy. Never menacing-realistic.

<!--html:samples-->

### 11.4 Palette in art

- **Skin (Common bodies):** Light Brown `#C29D84`, Dark Brown `#6D5341`, Peach/Pink `#F0D6C2`, Grey `#ADAAAF`, Red `#FF9494`, Orange `#FFBA7B`, Green `#D3FFA9`, Lilla `#FFB8FA`, Purple `#DDA9FF`, White. Rare bodies add patterns (Leopard, Scar, Tattoo, Zebra); Epic bodies are creature types (Ape, Cat, Cyborg, Devil, Frankenstein, Goblin, Robot); Legendary bodies include Alien Blue, Ghost, Golden, Radioactive, Robot Gold, Troll, Zombie.
- **Clothing and props:** bright, toy-like colours with one shadow tone. Pop-culture costume references are common (superheroes, sports kits, uniforms, movie homages), but they're stylised and never carry real logos.

### 11.5 Backgrounds (Flobit category, by rarity)

| Tier | Style | Examples |
|---|---|---|
| Rare | **Graphic patterns** filling the square, 2–3 colours | Burst (radial sunburst), Chevrons, Dots, Drips, Grid, Lines, Mesh, Waves, Squiggles, Triangles, Matrix, Gradient Diagonal Sunset |
| Epic | **Illustrated scenes** in the same outline style, eye-level perspective, often with subtle animation | Soccer Stadium, Pirate Ship, Beach, Bedroom, Shopping Mall, Garbage Dump, Haunted House, Roman Ruins, Pyramids, Underwater, Cityscape, Nostalgic Electronics, Transtator Pods |
| Legendary | **Dramatic animated scenes** | Spaceship Corridor, Magician Stage, Astro Battles, Demon Lair, Lava |

The most "on-brand" generic background is a **purple radial sunburst** (violet `#6657D3` / `#9B7BF0`-ish rays), or a night-purple sci-fi city.

### 11.6 Family styles (same line and shading rules)

- **Flobots:** small modular robots from 5 parts: **Head, Face, Body, Arms, Legs** (141 traits). White, grey and orange plastic-metal panels with cyan or orange screen accents, rivets, antennas, wheels or claw feet. One hand often raised (pointing or holding something). Friendly helper vibe. Same black outline.
- **Psyche Likees:** furry or fluffy pet companions (monster-plushie style) from 5 parts: **Face, Head, Body, Arms, Legs**. Saturated pastels (magenta, aqua, lime, lavender), big eyes, horns/ears/tufts, often a collar. Cute, never scary.
- **Sportvatars:** the same chibi body language (big head, thick outline, flat + one shadow), but in **sports kits** with numbers, sneakers, gloves and balls, and a **thumbs-up** pose instead of the raised fist. Generic kits only (no real club crests unless licensed). See §16.1.
- **Asteroid Islands:** floating rock islands in a **portrait 3:4 canvas (3025 × 4033)**, viewed from a slight top angle, with rocky underside cliffs, grassy, jungle, desert, ice or volcano tops, and castles, towers, scaffolds and a FUB building sitting on "slots". The background is a deep purple night sky. Layers: sky → island base → structures → FUB → billboard/foreground.
- **Storyworld scenes (*A Dust Odyssey*):** 16:9 cinematic panels in the same cartoon outline style with fuller lighting: interior shadows, glows from screens and portals, atmospheric colour (teal labs, warm Florentine interiors, purple Flova). Characters are Flovatars with story outfits.
- **Product objects:** **Spark** = glowing purple-blue plasma orb with white lightning cracks. **Boosters** = glass capsules with metal end caps (cyan = Rare, yellow = Epic, rainbow = Legendary). **Packs** = chunky toy-like machine boxes: Pack v2 is purple metal with bolts and a glowing cyan strip, the ĐUST pack is a lilac-and-yellow box with a camera-like lens, and the TerraKit is a steel-blue crate with latches. **ĐUST** = a pink/magenta coin with a white **Đ** glyph, shown with thickness (stacked coin edge).

<!--html:objects-->

### 11.7 Image-generation prompt templates

Fill the `{…}` slots. Keep the style block verbatim. For product art, prefer real renders (§17.3) over generated characters. Use generation for scenes, concepts and campaign key art. Every use of generated art follows the AI-art rule in §11.9.

**A. Single Flovatar character (key art / avatar)**
```
Flat 2D vector cartoon character in the Flovatar NFT style: chibi alien with a huge round bald head (about 45% of body height), small half-circle ear, two big round white eyes with black oval pupils on the right half of the face (near eye noticeably bigger than the far eye at the head's edge), small {nose}, cheeky {mouth} expression, stubby body in three-quarter view turned to the viewer's right (ear on the left side of the head), standing with short legs apart and one fist raised at shoulder height on the right side, other arm down. {skin colour} skin. Wearing {clothing}, {hat}, {eyeglasses}, holding {accessory}. Thick uniform black outlines with round line caps, flat fills with a single soft translucent darker shadow tone on one side, light from upper left, small flat ground shadow ellipse under the feet. Centered full body, square 1:1 canvas, generous margin, {background: plain transparent | purple radial sunburst background | illustrated {scene} background in the same outline style}. Clean, playful, toy-like, high-contrast, crisp vector edges.
```

**B. Group / campaign key art (banner)**
```
Wide 16:9 (or {ratio}) flat vector cartoon scene in the Flovatar style: a lineup of {n} chibi Flovatar characters (huge round heads, big white round eyes, thick black outlines, flat colours with one translucent shadow tone) in varied outfits ({outfits}), standing on glowing circular teleport pads, in front of a starry deep-purple night sky (#180830 to #411793) with a curved planet horizon and a faint giant condensed uppercase word "FLOVATAR" in lighter purple behind them. Accents of hot pink (#EF2AC1) and sky blue (#91E3F9) glow. Leave a clear empty area {left/center/right} for the logo and headline. Playful sci-fi, toy-like, crisp vector.
```

**C. Flova / storyworld scene (*A Dust Odyssey*)**
```
16:9 cinematic 2D cartoon illustration, Flovatar "A Dust Odyssey" style: {scene description} on planet Flova / on Earth in {era}. Characters are chibi Flovans (huge round heads, big white eyes, thick black outlines, flat colours with soft shadow tones). Richer lighting than character art: {mood lighting, e.g. teal lab glow / warm candlelight / neon portal light}, atmospheric depth, retro-futuristic props (purple slate columns, domes, holo-screens, Game Boy-like gadgets). Composition leaves the bottom-left corner clear for a logo and the bottom-right for the title. Funny, adventurous, family-friendly.
```

**D. Flobit (accessory / hat / background object)**
```
Single object icon in the Flovatar Flobit style: {object}, flat 2D vector, thick uniform black outline with round caps, flat saturated colours, one translucent darker shadow tone, small white highlight, isolated on transparent background, sized to be worn/held by a chibi character, no text, no logo.
```

**E. Asteroid Island**
```
Portrait 3:4 flat vector illustration in the Flovatar style: a floating asteroid island ({biome: rocky / jungle / desert / ice / volcano}) seen from a slight top-down angle, rocky cliff underside tapering to a point, {structures: castle, towers, scaffolding, water tank, telescope} on top, a small futuristic FUB building, tiny chibi residents. Thick black outlines, flat fills with one shadow tone, deep purple starry sky background (#180830 to #411793). Crisp vector, toy-diorama feel.
```

**F. Product objects**
```
Flat vector icon, Flovatar style, thick black outline: {a glowing purple-blue plasma orb with white lightning cracks (Spark) | a glass capsule booster with metal end caps glowing {cyan|yellow|rainbow} | a chunky purple metal pack box with bolts and a glowing cyan light strip (pack) | a thick magenta coin with a white Đ symbol (the ĐUST token)}, centered, transparent background.
```

**Negative prompt (use with every template):**
```
photorealistic, 3D render, CGI, clay, plastic shine, anime, manga, chibi anime eyes with highlights, realistic proportions, long legs, small head, sketchy lines, painterly, watercolor, gradient-heavy shading, airbrush, lens flare on characters, thin hairline outlines, colored outlines on characters, noisy texture, text, letters, watermark, signature, logos, brand marks, real sports club crests, celebrities, gore, blood, weapons pointed at viewer, sexualized, scary horror realism, extra fingers, deformed hands, cropped head, multiple views
```

### 11.8 Art do / don't

| ✅ Do | ❌ Don't |
|---|---|
| Use real renders from `images.flovatar.com` / §17 for product posts | Generate "fake" Flovatars and present them as real NFTs |
| Keep thick black outlines and flat fills | Use 3D, glossy or anime styles (the 3D models are a separate, licensed asset) |
| Keep the raised-fist base pose for characters shown "as NFTs" | Change body proportions (long legs, small heads) |
| Use rarity colours exactly when showing tiers | Invent new tier colours |
| Credit "art by the Flovatar team" | Credit or name individual artists |
| Disclose AI-generated campaign art when the brief asks | Generate art of real people or other projects' characters |
| Check the use before generating: non-commercial, owner of that Flovatar, or official team work (§11.9) | Make commercial AI art of a Flovatar the requester doesn't own |

### 11.9 AI-generated art & IP

In short: everything is allowed for non-commercial use; commercial use only for the Flovatar(s) you own.

| Who | Non-commercial use | Commercial use |
|---|---|---|
| **Everyone** (fans, creators, agents working for anyone) | ✅ AI-generated art of any Flovatar IP: Flovatars, Flobits, Flobots, Psyche Likees, the story cast, the Megaverse. Fan art, memes, avatars, posts, stories, experiments. | ❌ |
| **The owner of a Flovatar** | ✅ | ✅ only for **the Flovatar(s) they own**, e.g. merch, prints, a comic or a paid product featuring their own Flovatar #1234 |
| **The Flovatar team** (official project work) | ✅ | ✅ campaigns, key art, merch, video and any other official use |

**Scope:**
- An owner's commercial right lasts **only while they hold that Flovatar**. It ends when they sell or transfer it.
- It covers **only the Flovatar itself**, with its equipped Flobits. It doesn't extend to other NFTs they own (Flobits on their own, Flobots, Psyche Likees).
- **Story characters and logos stay non-commercial** for everyone except the Flovatar team.
- **Disclosure:** label AI-generated art as AI-generated when a brief asks for it.

**For the community (plain words):** Make all the AI art of Flovatar you like, for fun. If you want to sell it or use it in something paid, you can, but only with the Flovatar(s) you own. Everything else stays non-commercial.

**For agents (decision steps):**
1. Ask or infer the **use**. If it's non-commercial (fan art, personal post, concept, storyboard), go ahead.
2. If it's **commercial** (sold, licensed, used in ads, merch or a paid product), continue only when one of these holds:
   - The brief says this is official Flovatar team work.
   - The brief names the requester's own Flovatar ID(s), held today. Then depict only those Flovatars (with their equipped Flobits), no story characters or logos.
3. Otherwise, decline the commercial part and offer a non-commercial version. Never decide ownership yourself: a human confirms it, for example by checking the wallet on flovatar.com.
4. The other rules still apply: on-model style (§11.3), family-friendly (§0.2), no artist names, and never present generated art as an existing NFT or an official release.
