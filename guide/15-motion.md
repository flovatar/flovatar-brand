## 15. Motion & video

### 15.1 Existing motion language (sourced)

| Asset | Specs | Look |
|---|---|---|
| **Spark** loop | 1300 × 1300, 30 fps, 4 s seamless (MP4/GIF/SVG in Media Pack) | Plasma orb pulsing, lightning crackling |
| **Booster** loops (Rare/Epic/Legendary) | 1300 × 1300, 30 fps, 4 s | Capsule glow cycling in the rarity colour |
| **Item renders** (every Flovatar, Flobot, Psyche Likee, Sportvatar) | 1000 × 1000 MP4 (x264, CRF 20) + GIF, settled final frame as PNG/JPG | The on-chain SVG animation, captured deterministically. Combo reveals included. |
| **Pack opening** (Flobit S2, TerraKit) | Inline animated SVG (SMIL) | Sequence: idle pack → **"Switch On"** pulse → bolts unscrew → pistons → latches → lid lifts → glow rings → white flash → 3 cards fade in, styled by rarity (rare / epic / legendary). |
| ***A Dust Odyssey* trailer** | 1920 × 1080, 30 fps, ~30 s and ~56 s cuts | Flat-vector illustrated stills with camera moves, parallax and simple puppet motion; dark navy/purple palette with cyan/teal light; finale lineup of the crew under a huge white condensed **A DUST ODYSSEY** title. |
| **ĐUST explainer** | 1080 × 1080, 30 fps, ~56 s | Spinning 3D-ish pink Đ coin, circular uppercase text ring, logo bottom-left, URL bottom-right on indigo. |
| **Podcast episodes** | 20 audio parts of ~12–15 min (10 script episodes × 2), 16:9 illustrated stills per scene | Narrator plus character voices recorded dry. Robot and video-feed effects added in the edit; Pixabay-style SFX (hover engines, warp, force fields, sci-fi doors). |

### 15.2 Motion principles [inferred from the assets above]

1. **Bouncy but simple.** Ease-in-out loops, float/bob, squash on landing. Characters move like puppets/cut-outs (rigged SVG parts), not full frame-by-frame anime.
2. **Glow means energy.** Sparks, portals, ĐUST and Boosters always emit a pulsing glow in their colour. Everything else stays flat.
3. **Reveals are events.** Build-up (pulse, rumble) → flash → reveal → settle. Hold the final frame ≥ 1 s.
4. **Seamless loops** for social (4–6 s), with first frame = last frame.
5. **Keep the outline.** Thick black outlines stay the same width in motion (no line boil). No motion blur on characters; use smear frames sparingly.
6. **Sound:** playful sci-fi SFX (warp, zap, boing, beep), a warm narrator; no stock "epic trailer" brass.

### 15.3 Storyboard template (per shot)

| Field | Example |
|---|---|
| Shot # / timecode | 03 / 00:00:12–00:00:16 |
| Location / time (Flovan or Earth) | Dome 93, Fasco's kitchen, morning (25.5 FT) |
| Characters (on-model refs) | Fasco, Junbee |
| Framing / camera | Medium, slow push-in |
| Action | Junbee hides Fasco's bag in the oven |
| Dialogue / VO | NARRATOR: "…" |
| SFX / music | Oven fan, comedic sting |
| Lighting / palette | Morning violet, warm oven glow |
| Notes / assets | Reuse kitchen BG from Ep1 storyboard |

### 15.4 Render and export defaults

- Social MP4: H.264 High, yuv420p, CRF 18–20, AAC 192 kbps, `+faststart`.
- GIF: ≤ 15 fps, ≤ 800 px, palette-optimised, ≤ 8 MB for X.
- Loops for the site: WebM/VP9 + MP4 fallback, muted, `playsinline`.
