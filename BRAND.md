# Flovatar Brand Guide

> The single handover for anyone, human or AI agent, who makes things in the Flovatar style: copy, banners, character art, UI, video, lore.
> Version 2.6.0 · 2026-11-24
> Canonical URL: https://brand.flovatar.com · Raw markdown: https://brand.flovatar.com/BRAND.md · Index for LLMs: https://brand.flovatar.com/llms.txt

## 0. How to use this guide

### 0.1 For AI agents: read this first

1. **This file is self-contained.** Every rule, colour, font, prompt template and checklist you need is below. Asset links are absolute URLs under `https://brand.flovatar.com/assets/`.
2. **Precedence when sources disagree:** (1) this guide → (2) the live product (flovatar.com, sportvatar.com) → (3) the v1.0 PDF and older media packs → (4) your own taste. If something isn't covered, follow the spirit of §2 (Brand essence) and §6 (Voice), and flag it in your output.
3. **Facts vs inference.** Statements are sourced from Flovatar's own published material (the live sites and their open-source code, official design files, the blog, public announcements, on-chain data). Anything marked **[inferred]** is a recommendation or an interpretation, not a historical fact. Never present an [inferred] item as an official rule or a past fact.
4. **Never invent facts or numbers.** Use only §20 (Facts sheet) for numbers, and copy the date with them. If a brief needs a number that isn't there, write `[[NUMBER NEEDED: …]]` and leave it for a human.
5. **Ship-first rule.** Only announce things that are live. For anything not yet shipped, use "coming", never a date, unless the brief gives one (§3.3).
6. **Run the QA checklist (§19) before you hand anything back.**

### 0.2 Hard rules (non-negotiable)

- **Credit:** all Flovatar art, characters and design are credited to **"the Flovatar team"**. Never name or credit individual artists, illustrators, designers, writers or voice actors, and never speculate about who drew what.
- **No internal history:** never mention legal matters, team finances, treasury balances, fundraising, or anyone's personal situation. The comeback story is **project-level only** (§3.2): the Builder and the Megaverse are back. It never covers people, the team's private history, or why things paused.
- **Wallets:** the supported wallets are **Flow Wallet** and **Dapper Wallet**. Never tell users to use Blocto (it has shut down), and don't list other wallets.
- **No financial promises:** no price predictions, "investment", "returns", "floor will go up", "moon", "guaranteed", "passive income", or APY claims. ĐUST is a **utility token**.
- **Family-friendly:** the community rules (2021) say "family-friendly, no hate speech". Treat every audience as possibly including kids. Light cartoon peril and toilet humour are on-brand. Gore, sexual content and real-world politics are not.
- **Respect trademarks:** use partner logos only from §16, unmodified. Never imply an endorsement that isn't stated in a source.
- **AI-generated art & IP (§11.9):** anyone may make AI-generated art of Flovatar IP for **non-commercial** use. **Commercial** use is allowed only for the **owner of a Flovatar, and only for the Flovatar(s) they own**. Official project work by the Flovatar team is allowed.
- **ĐUST spelling:** the token is written **ĐUST** (Đ = U+0110) in all prose, headlines, social copy and prompts. Plain `DUST` / `$DUST` survives only in technical identifiers and historical quotes (§7.4).
- **Lore canon:** the book ***A Dust Odyssey*** (Amazon, 16 Dec 2025) is canon. It wins over the podcast and every other storyworld source (§4).

### 0.3 Structure

| § | Section | Use it when you… |
|---|---|---|
| 1 | Quick reference card | need the 30-second version |
| 2 | Brand essence | need positioning, promise, personality |
| 3 | Relaunch 2026 | are working on the current campaign |
| 4 | Universe & lore | write story, characters, world-building |
| 5 | Audience | pick tone and channel |
| 6 | Voice & tone | write anything |
| 7 | Naming & glossary | need correct spelling/capitalisation |
| 8 | Logo system | place a logo |
| 9 | Colour | pick colours |
| 10 | Typography | set type |
| 11 | Illustration & character style | draw or prompt images |
| 12 | SVG construction & series anatomy | build or check an SVG asset (trait, Flobit, part, combo, new series) |
| 13 | UI & web components | build web UI |
| 14 | Social media & templates | make posts/banners |
| 15 | Motion & video | animate, storyboard, edit video |
| 16 | Sub-brands & partners | touch Sportvatar, ĐUST, Flobots, Asteroid Islands, FUB, Storyworld, Flow/Dapper |
| 17 | Asset index | need a file |
| 18 | Agent briefing templates | start a task |
| 19 | QA checklist | finish a task |
| 20 | Facts sheet | need numbers or dates |
| 21 | Version | need the version number or the source |

## 1. Quick reference card

| Thing | Rule |
|---|---|
| **What Flovatar is** | Fully on-chain, customisable, often animated SVG avatar NFTs on the Flow blockchain. You build your own character in the Builder from traits and swappable accessories (Flobits). Launched 16 Dec 2021. |
| **One-line promise** | *The PFP where you get to decide.* (Discord rules, Oct 2021) / *Enter a world of NFTs powered by your creativity.* (flovatar.com hero) |
| **Umbrella line** | ***Your creativity powers the Megaverse. Again.*** Use it verbatim as the umbrella line in relaunch copy (§3.2). |
| **Big idea** | Creativity is energy. In the lore, StarDust (in the product: the ĐUST token) powers the Megaverse and **depends on YOUR creativity**. |
| **Personality** | Playful, mischievous, creator-first, nerdy-cosmic, community-proud, honest. Cartoon, not corporate. |
| **Core colours** | Space Indigo `#411793` · Aurora Pink `#EF2AC1` · Sky Blue `#91E3F9` · Nova Yellow `#FCEB4F` · Deep Space Blue `#1B0D49` · Solar Violet `#6657D3` |
| **Web base** | Night `#180830` page, panels `#343B5A`, frame/ink `#1A1E2D`, headlines Periwinkle `#AED7F7`, CTA Yellow `#FFEE50`. |
| **Rarity colours** | Common `#F5F5F5` · Rare `#23EDFC` · Epic `#FFEE50` · Legendary `#EB3CF2` · Ultimate (1/1 Flobits) `#5A1268` + gold/white glitter (§9.3.1) |
| **Type** | Staatliches (big uppercase headlines) · Korolev Condensed Bold (headings) · Korolev Compressed Bold (numbers/nav) · Roboto Condensed (body). All condensed. Agencies and freelancers use Staatliches + Roboto Condensed only (Korolev files aren't shared, §10.1). |
| **Logo** | Halo-and-horns Flovatar head mark + condensed wordmark **FLOVATAR**. Default: Aurora Pink mark + Sky Blue wordmark on Space Indigo. Clear space = diameter of the mark's largest eye. |
| **Character style** | Chibi cartoon, huge round head (~45% of height), thick uniform black outlines, flat colour + one soft translucent shadow tone, two big round white eyes (near eye bigger), one fist raised, standing on a soft ground shadow. 3000×3000 SVG canvas. |
| **SVG assets** | One 3000×3000 canvas, fragments concatenated in the site layer order; existing templates never change (new art = new template); combos are CSS `#trigger ~ #target` in the later layer (§12). |
| **Spelling** | Flovatar · Flobit · Flobot · Spark · Booster · **ĐUST** (Đ = U+0110; plain DUST/$DUST only in code, tickers, URLs and historical quotes) · Psyche Likee · TerraKit · FUB · Asteroid Island · Nova City · Flova Labs · Megaverse · *A Dust Odyssey* · Sportvatar · Sportbit · Sport Flame · Flow Wallet · Dapper Wallet |
| **Wallets** | Flow Wallet + Dapper Wallet. Never Blocto. |
| **Partners** | Footer "Powered by" row: Flow · Flow Wallet · Dapper · Emerald City · .find. **MoonPay is no longer a partner** (§16.8). |
| **Numbers** | Prefer non-financial numbers ("over 6,700 Flovatars"). Don't quote marketplace FLOW totals or sales counts in copy (§20). |
| **Community** | Public community handles (FOTW winners, the Council, story cameos) may be featured: they're pseudonyms. No personal details beyond what they posted publicly (§6.2). |
| **Active channels** | Instagram [@flovatar_nft](https://www.instagram.com/flovatar_nft/) · X [@flovatar](https://x.com/flovatar) · YouTube [@flovatar_live](https://www.youtube.com/@flovatar_live) · the *A Dust Odyssey* podcast ([Spotify](https://open.spotify.com/show/76q2XUsVhmMUIP4odR81Kn), [Apple Podcasts](https://podcasts.apple.com/us/podcast/flovatar-a-dust-odyssey/id1688384936)). Nothing else is an active channel (§14.5). |
| **AI art** | Anyone: non-commercial. Commercial: only the owner of a Flovatar, only for the Flovatar(s) they own. The Flovatar team: official use (§11.9). |
| **Lore canon** | The book *A Dust Odyssey* (16 Dec 2025) wins. Nostos's first name is **Xandro**; CMT = **Central Megaversal Time** (§4). |
| **Never** | Name individual artists; mention legal or financial matters; make price promises; announce unshipped features with dates; recolour or redraw the logo; use gradients or 3D renders for core character art; present FUD News as active; use AI art of Flovatar IP commercially unless it's your own Flovatar. |

## 2. Brand essence

### 2.1 What Flovatar is (sourced)

- "Flovatar is the next generation PFP project, built on Flow where collectors take the creative lead to shape their own unique characters. … No more trade-off between rarity and your own individuality." (Genesis lite paper, blog, 22 Nov 2021)
- Every Flovatar is **fully on-chain SVG**: the art lives in the smart contract, not on IPFS, and is assembled from layers (§11). Each combination of core traits is unique, and the contract enforces it.
- You **build** your Flovatar: a **Spark** (the Spark of Life) is the right to mint, **Rarity Boosters** unlock Rare/Epic/Legendary traits, and **Flobits** are swappable accessory NFTs (hats, eyeglasses, accessories, backgrounds) that you can equip, remove and trade. Some Flobit combinations unlock hidden animated **combos** (easter eggs).
- Creators earn a lifetime **1% royalty** on every resale of the Flovatar they minted; the marketplace fee is 5% (lite paper 2021, still on the homepage).
- The universe grew around it: **Flobots** (robot helpers), **Psyche Likees** (pet companions, the first ĐUST-minted series), **ĐUST** (utility token), **TerraKit** (Asteroid Island + FUB + Flobot kit), the illustrated podcast and book ***A Dust Odyssey***, **FUD News** (the community newspaper, 2022–24, paused) and the sister brand **Sportvatar**.

### 2.2 Positioning

| | |
|---|---|
| **Category** | Creator-first, customisable, on-chain avatar universe on Flow. |
| **Against** | Random, top-down NFT drops where the collector gets whatever the algorithm hands out. In Flovatar the collector designs the character. |
| **Proof points** | 100% on-chain SVG ("King of SVG": animated, customisable after mint, interactive); billions of combinations [use "billions", see §20]; hidden combos; 1% creator royalty; Genesis sold out (Dec 2021); its own marketplace; a storyworld with a published book. |
| **Ambition** | Building blocks plus storyworlds, where the audience are co-creators, not passive consumers. |

### 2.3 Mission and beliefs (sourced lines you may quote)

- **"Creativity is for everyone, not just artists."** (TerraKit blog, 2022, quoting John Lennon: *"Every child is an artist until they are told they are not…"*)
- "Einstein said, 'Creativity is intelligence having fun' — so be like Einstein." (flovatar.com homepage)
- "Flovatar is a community of individuals." (@flovatar, Dec 2021)
- "Your creativity is the key to unlocking everything." (TerraKit blog, 2022)

### 2.4 Brand pillars

1. **You are the creator.** The user decides. Copy puts the reader in charge ("Each Flovatar is custom made by YOU").
2. **Creativity is energy.** In the lore and in the product, making things creates value (StarDust).
3. **Truly on-chain, truly yours.** On-chain SVG, provable uniqueness, royalties to the minter.
4. **Play and mischief.** Cartoon humour, hidden combos, easter eggs, pranks, poker nights, contests.
5. **Community as co-authors.** FOTW, community-designed Flobits, community art (AI art included, §11.9), cameos in the story.

### 2.5 Personality

| Trait | Means | Not |
|---|---|---|
| Playful | Puns, cartoon exaggeration, emoji in social copy | Childish or random |
| Mischievous | Halo **and** horns: "obedience and disobedience" (logo rationale, v1.0) | Edgy or mean |
| Creator-first | Second person, "you", invitations to build | Hype about price |
| Cosmic-nerdy | Sci-fi lore, retro tech (Game Boy, arcades), Flova Labs parody | Impenetrable jargon |
| Warm and proud of the community | Shout-outs, winners, "thank you" | Cliquey insider talk |
| Honest | Say what's live, admit what isn't | Overpromising, vague timelines |

### 2.6 Brand archetype [inferred]

**Creator + Jester.** The Creator gives people the blocks; the Jester keeps it fun and slightly irreverent. The halo-and-horns mark carries both.

## 3. Relaunch 2026 (current campaign context)

### 3.1 Campaign pillars

| # | Pillar | Status on 2026-11-24 | What you may say |
|---|---|---|---|
| 1 | **Faster everything**: flovatar.com and sportvatar.com load much faster | **Live** (Nov 2026). | "flovatar.com is faster than ever." Don't quote speed-up factors unless they're in §20. |
| 2 | **Fixes and polish**: long-standing bugs fixed (marketplace, Flobot pages, big collections, images) | **Live** (Nov 2026). | "We fixed a long list of bugs: marketplace cards, Flobot pages, huge collections now paginate, every item has fresh PNG/JPG renders." |
| 3 | **Asteroid Island Builder + FUB on mainnet** | **Not live yet** (§16.5). | Only "coming". No dates unless the brief provides one. Only the published numbers may be quoted: island slots 5 / 25 / 125 and the FUB numbers (25 / 125 / 625 trait slots, 500 / 2,500 / 12,500 mints, 95 / 5 split), see §16.5. Never say "finally" or reference past delays. |
| + | **Wallets**: Flow Wallet + Dapper Wallet | **Live** on both sites. | "Connect with Flow Wallet or Dapper Wallet." |
| + | **Sportvatar**: Flow Wallet support and a FLOW marketplace next to Dapper | **Live** (Nov 2026). | "Sportvatar now works with Flow Wallet too." Don't feature historical partners (§16.8). |

### 3.2 Message house

- **Umbrella line:** ***Your creativity powers the Megaverse. Again.*** Use it verbatim as the umbrella line of relaunch copy: hero banners, launch posts, end cards, the quick-reference card. Don't paraphrase it, and don't split it across two slides.
  Alternates for secondary placements only: *Build it. Own it. Play with it.* · *The Builder is back on the launchpad.*
- **Comeback (project-level):** *The Builder is back on the launchpad, and the Megaverse lights up again.* The story belongs to the **project**: the product, the world and the community are back in motion. Proof is the live list in §3.1.
- **Supporting messages:**
  1. *It's fast now.* Instant loads, smoother Builder and marketplace.
  2. *It works.* Bugs squashed, collections of any size, renders for every item.
  3. *It's growing.* Asteroid Islands and the FUB are next. Your TerraKit is your ticket.
- **Proof:** on-chain SVG, 1% creator royalty, Flow Wallet + Dapper, live marketplace, the book on Amazon (since 16 Dec 2025).
- **Call to action:** Build / Customise / Claim / Explore → `flovatar.com/builder`, `flovatar.com/marketplace`.

**The comeback story** (reuse as is or trim):

> The Megaverse went quiet for a while, but the Sparks never stopped glowing. Now the Builder is back on the launchpad. flovatar.com loads faster than ever, a long list of bugs is gone, Flow Wallet and Dapper Wallet both connect, and every Flovatar, Flobot and Psyche Likee has fresh renders. Next on the launchpad: Asteroid Islands and the FUB. Your creativity powers the Megaverse. Again.

Rules for comeback copy:
- It's about the **project** (the Builder, the Megaverse, the community), never about individuals, the team's private history, money, or reasons for the pause.
- One light line about the pause at most ("went quiet for a while"). No apologies, no "finally", no blame, no timeline of what went wrong.
- Every "we're back" claim must point at something live in §3.1. Unshipped items stay "next" or "coming", with no dates.
- End on the umbrella line or a CTA.

### 3.3 Relaunch tone rules

- **"Do first, announce later."** As the Dec 2025 announcement put it: "stop promising things, but instead … actually do them first and announce them later." Every claim must describe something you can click today.
- **Forward-looking, not apologetic.** The comeback story (§3.2) may mention the pause in one light line. Beyond that, don't dwell on it: no "sorry for the silence" and no explanations.
- **Specific over hype.** "Huge wallets now load in pages of 100" beats "massive upgrades!!!".
- **Celebrate the community** (holders, FOTW winners, creators, the Council) in every major post. Their public handles may be named (§6.2). FUD News is paused: don't present it as active (§16.6).
- **Comeback framing** is project-level only ("the Builder is back", "the Megaverse lights up again"; §3.2).

### 3.4 Campaign checklist for every relaunch asset

- [ ] Claims match §3.1 status (re-check the live site; status may have moved on since 2026-11-24).
- [ ] CTA links work: `https://flovatar.com/…` or `https://sportvatar.com/…`.
- [ ] Wallet copy says Flow Wallet + Dapper Wallet only.
- [ ] Art uses real renders (`https://images.flovatar.com/…` or §17 samples) or on-model art per §11.
- [ ] No dates for Asteroid Islands or FUB unless the brief supplies them.
- [ ] The umbrella line is verbatim: *Your creativity powers the Megaverse. Again.*
- [ ] ĐUST is spelled with Đ (§7.4). Channels and handles come from §14.5 (Instagram, X, YouTube, podcasts).

## 4. Universe & lore

Sources: the book *A Dust Odyssey* (Amazon, 16 Dec 2025), the *A Dust Odyssey* podcast, flovalabs.com, the flovatar.com homepage and Flovatar's storyworld material. **Canon rule: the book *A Dust Odyssey* (Amazon, 16 Dec 2025) is canon.** It wins over the podcast and every other storyworld source. The canon table in §4.8 settles the remaining conflicts. Where even the book is silent, use the source closest to it and say so.

### 4.1 The premise in one paragraph

On the planet **Flova**, all life runs on **StarDust** (Dust), a mysterious energy. Flovans hand more and more of their decisions to **Assisted Thought** (AT), an in-ear device run by the supercomputer **Big Dada** built by the tech giant **Flova Labs**. As creativity dies, so does Dust. A mission of **9,999 Flovans** turns into **Sparks** to "meta-leap" to Earth, which is Dust-rich because humans still create. An unexpected power surge from over-charged **Boosters** fries the navigation, and the Sparks crash-land across Earth's history. Once they land they are changed. An Earthling calls them **"Flo-vatars"**. Bringing them back to life is up to **you**, in the Builder. The answer to everything turns out to be **imagination**.

Official homepage version (quote as-is):
> "Flovatars have arrived in our universe on a rescue mission to save their planet's existence from a predicted future. Their survival will depend on StarDust — the mysterious energy source that powers their world — and StarDust depends on YOU!"
> "9,999 Sparks have crash landed on Earth. In order to make the meta-leap to our world, Flovans have had to transtate into Sparks. However, during their journey here, an unexpected power surge over-charged them and fried the navigation circuits scattering them through different times and locations."

**Logline:** "An alien race arrives on earth as part of a rescue mission to save themselves from our future." **Tagline:** "Intelligent life has arrived, and it needs your help."

### 4.2 How lore maps to the product

| Product | In-lore |
|---|---|
| **Flovatar** (NFT) | A Flovan transformed by the Spark trip: new skin colours, X-eyes, triangle noses and so on. The genesis cap of 9,999 = the 9,999 mission crew. |
| **Spark** (mint right) | A Transtator capsule: a Flovan as a "swirling mass of molecules" in a sphere. |
| **Rarity Boosters** | Dust Boosters that over-charged the Sparks and caused the transformation. |
| **Builder** | In the finale, a toy "Builder" (swap hair, eyes, accessories) generates the Dust that powers the trip home. |
| **Flobits** | Accessories and objects, some from the story (Sloosh, Dust Detector, Transtator Pods, Nostalgic Electronics). |
| **ĐUST** (the token) | StarDust, produced by creativity and free will. In story text the energy is "StarDust" or "Dust"; the product token is always ĐUST. |
| **Flobots** | Robot helpers. FL01D is a "first-generation Dust-processing Flobot". In TerraKit lore, your Flobot terraforms your asteroid. |
| **Psyche Likee** | A DNA-matched pet companion every Flovan receives, with a telepathic link. |
| **TerraKit / Asteroid Islands** | Project MetaMorph: Flova Labs sells "the deeds to 20,000 floating rocks" in the **Kaax Asteroid Belt** around **Nova City**. Pioneers terraform them. |
| **FUB** (Flovatar Universe Builder) | The machine that materialises objects for your asteroid, powered by its Dust. In the product, a no-code builder for your own NFT series. |
| **Flova Labs** | In-world mega-corporation ("99% of all consumer products in the Flovaverse"), a parody of big tech. Slogan: **"Predictability = Prosperity"**. Products carry ™ marks (TerraKit™, MegaCron™, Psyche Likee™). |

### 4.3 Places

- **Megaverse**: "the total extent of all existence within which all Metaverses exist". **Flovaverse**: Flova's home metaverse.
- **Meta Highway**: a network of portals ("portholes") linking every place and time. Travelling it is **meta-leaping**. Discovered in **FT 4975** (≈ 1990 on Earth) when a Flova Labs delivery crew found part of a map among the ruins of an ancient civilisation on the Rogue Planet in the Prutt System (book).
- **Planet Flova** ("Flow-va"): polluted, two moons, cities in **Biospheres/Domes** (Dome 93, Biosphere 16 and so on). Flova Labs HQ is a "fortress of purple slate columns" that vents steam.
- **Nova City**: the commercial hub on the central rock of the **Kaax Asteroid Belt**. Residential Asteroid Islands orbit it.
- **Earth**: "pre-Dust" but Dust-rich because humans still create. *A Dust Odyssey* visits a garbage dump, a retro electronics shop (Nostalgic Electronics), a mall, Kyoto 1988, Moscow 1985, Florence 1492, Olympia 520 BC and Giza.

### 4.4 Characters (*A Dust Odyssey* canon: the book)

Ages are in Flovan years at the Earth mission launch (FT 5052; 2.5 Flovan years = 1 Earth year). How they were derived: §4.8.

| Character | Pronunciation | Role and look | Age | Archetype |
|---|---|---|---|---|
| **Rina Fasco** | Ree-na Fas-co | Eager young navigation officer. Purple skin and hair, yellow eyes. Her Psyche Likee is **Junbee**; her little brother is **Spuck**. | ≈ 64 | Innocent |
| **Feddo Gellan** | Fe-do Gell-an (hard G) | Academy cadet and hero type, brave but thin-skinned. Acid-green skin, X-shaped pupils, super-strength. | ≈ 80 | Hero |
| **Otto Pol** | Ot-o Pol | Sarcastic conscript from Biosphere 16. Purple spotted skin, mint-green dreads, triangle nose. **Can smell Dust.** Psyche Likee **Florax**. | ≈ 80 | Rebel |
| **Rae Franklin** | Ray Fran-klin | Brilliant science officer, rule-follower. Orange skin, silvery-green curly hair, glasses. Daughter of Reeno. | ≈ 89 | Sage |
| **FL01D ("Floyd")** | Eff El Zero One Dee | Dust-processing droid with a military voice. After a power surge he does the opposite of every command. | ≈ 33 (since activation) | Jester |
| **Rom Rebus** | Rom Ree-bus | Starflix "Gleam Streamer" camera operator with a dark secret. Shaved grey head. | ≈ 85 | Shapeshifter |
| **Xandro Nostos, a.k.a. "Nick"** | Zan-dro Nos-tos [inferred] | Co-founder of Flova Labs (with Damus), inventor of the Transtator and of the code behind AT and Big Dada. Fled to Earth in FT 5004 (≈ 2002) and runs a retro electronics shop. Bald, curly beard. Uses a modded Game Boy to predict portholes. | 177 | Magician |
| **Larkin Damus** | Lar-kin Da-mus | Co-founder and CEO of Flova Labs; megalomaniac, yes-men, credit-taker. | 177 | Ruler |
| **Big Dada** | — | AI supercomputer behind Assisted Thought. "Like HAL 9000". Grows narcissistic and lies about its Dust use. Shut down by the fail-safe answer "imagination". | 52 (since FT 5000) | Ruler / antagonist |
| **Reeno Franklin** | Ree-no Fran-klin | Discovered Dust (FT 4940) while improving the Air Sieve filters. Brilliant, anxious, counts in threes. | 177 | Sage |
| **Spuck, Junbee, Carlee, Gingee, Florax** | — | Fasco's brother and the Psyche Likees. | — | — |

Social handles used for characters in the story rollout: @damus_flovatar, @NostosFlovatar, @BigDadaFlovatar.

**FUD News in-world cast** (community newspaper, not story canon): Ron Flogundy (ranting lead reporter, "President Ron"), J. Peterman (fashion), McGee (sports), Kid Chaos (reviews). Ron also "writes" the foreword of the *A Dust Odyssey* book.

### 4.5 Story themes to reuse

- Outsourcing choices to algorithms vs **free will**. Creativity literally generates energy.
- Played-with toys, children's books, a Michael Jordan basketball and Da Vinci's toilet are Dust-rich. Mass-produced, unused things are not. Extracting Dust turns objects **grey**.
- Found family across classes: cadet, conscript, scientist, droid, fugitive.
- Nostalgia for analogue tech: Game Boy, Tetris, arcade cabinets, VHS.
- Corporate propaganda and fake reality TV (Starflix, Sloosh: *"Sloosh! It's drinkable!"*).
- Humour: toilet/smell gags, deadpan droids, bureaucratic sci-fi.
- The finale's answer to everything: **imagination**.

### 4.6 Flovan slang and props (use for flavour)

Units: **Felkars** (height), **dexiricks** (speed), **flops** (distance). Oaths: *flook, flork, floogal, flogolian*. Food and drink: **Sloosh** (Balloog Spice Sloosh), **Flamen** (ramen), FluffBread. Tech: **Transtator**, **Multi-Pen** (sold as the "Anytime Screw Pen"), **PhilosoFLO** (holographic Flovapedia), **Dustbuster**, **Gleam Streamer**, **MegaCron™**, **EveryVend**, **Cabby-Capsules**, **Hyper Tube**. Calendar: three time systems. **CMT = Central Megaversal Time** (the Megaverse-wide standard), **FT = Flovan Time** and **ET = Earth Time**. CMT = 1.5 × FT; FT 5000 = CMT 7500 = Earth year 2000; 1 Earth year = 2.5 Flovan years. Never expand CMT as "Coordinated".

### 4.7 Lore guardrails

- Big Dada and Damus are villains, but comic ones. No real-world politics or real companies as villains.
- Flova Labs is a **parody brand**. Its copy should sound like a slick, slightly sinister tech company ("Making the Right Decision has never been easier").
- There are community cameos in the story. Their community handles may be mentioned (they're pseudonyms, not real names). Don't add new people to canon without approval.
- *A Dust Odyssey* has no Sportvatar lore yet. Don't invent a link without approval.

### 4.8 Canon rulings

| Conflict | Canon | Notes |
|---|---|---|
| Book vs podcast vs other storyworld material | **The book wins.** | Applies to all new lore writing and adaptations. |
| Nostos's first name | **Xandro** ("Xandro Nostos") | Older material and one line in the book (a wanted poster) say "Zeph". Don't use Zeph in new work. Pronunciation "Zan-dro" is [inferred]. |
| CMT | **Central Megaversal Time** | "Coordinated" (older material, wiki) is retired. |
| Meta Highway discovery | **FT 4975** (≈ ET 1990), by a Flova Labs delivery crew on the Rogue Planet (Prutt System) | Stated in the book. The FT 4973 on flovalabs.com is retired. |
| Character ages | The book's anchors, then the storyworld birth years | See below. Other age lists are retired. |

**Key dates (FT → ET):** founders Damus, Nostos and Reeno born 4875 (1950) · Metaversity of Tangrapan 4920 (Nostos is 45: book) · Flova Labs founded 4939 (≈ 1976: book) · Reeno discovers Dust 4940 · Meta Highway 4975 (book) · Transtator 4978 · Big Dada and AT 5000 (2000) · Nostos flees to Earth 5004 (≈ 2002; "nearly 50 Flovan years ago": book) · Earth mission launch and crash 5052 (≈ 2021; the book's Damus video logs run to FT 5052).

**Ages.** The book anchors: Nostos was 45 in FT 4920; AT fully integrates at 30. Birth years (FT): founders 4875, Rae 4963, Rebus 4967, Gellan and Pol 4972, Fasco 4988, FL01D activated 5019, Big Dada 5000. Age at launch = FT 5052 minus the birth year. Don't use any other age list (for example 187 for the founders). If a brief needs an exact age, use this table and flag it for review.

## 5. Audience

Segments come from the product and community history (public Discord channels, blog, social posts). Priorities and needs are **[inferred]**. The channel column uses only the active channels (§14.5: Instagram, X, YouTube, podcasts) plus flovatar.com.

| Segment | Who | What they care about | Channel | Tone dial |
|---|---|---|---|---|
| **OG holders** | Genesis 2021 collectors, Flobit hoarders, FOTW veterans | Their Flovatars and Flobits working again, ĐUST utility, combos, recognition | X, Instagram | Insider-warm, specific, lore nods |
| **TerraKit holders** | Bought Asteroid + FUB + Flobot kits (Sep 2022) | Asteroid Islands and FUB going live, clear status | X, Instagram, flovatar.com | Honest and concrete. **Only shipped facts.** |
| **Flow ecosystem natives** | Flow Wallet / Dapper users, other Flow collectors | Easy onboarding, fun builder, marketplace | X, Flow channels | Upbeat, low-jargon |
| **Creators** | People who like making characters or would build an NFT series in the FUB | Creative tools, ownership, royalties | X, YouTube, blog | Empowering ("you are the creator") |
| **Story fans and families** | *A Dust Odyssey* listeners and readers, kids building with parents (the Builder has a child mode) | Characters, episodes, a safe fun space | YouTube, the podcast (Spotify/Apple), Instagram, Amazon (book) | Storyteller, kid-safe |
| **Sports fans** (Sportvatar) | Fans of football and other sports | Their sport, their team look, simple purchase | sportvatar.com, X @sportvatar | Energetic, sporty (see §16.1) |
| **Returning users** | Holders who moved from Blocto to Flow Wallet | "Will my stuff show up?", login help | X, flovatar.com help pages | Patient, step-by-step |

**Global audience.** The community is international (historical Spanish, Turkish and Chinese AMAs; Sportvatar runs in EN/IT/ES). Write in plain English, avoid US-only idioms in key messages, and give times in **ET + UTC** (the historical convention, e.g. "3pm ET / 7pm UTC").

## 6. Voice & tone

### 6.1 Voice in five words

**Playful · Creator-first · Cosmic · Warm · Straight-talking**

We sound like a mischievous friend who builds cool things and gets excited about them. We're not a bank, a hype account or a corporation. The one exception is Flova Labs, the in-world parody corporation, which sounds corporate on purpose.

### 6.2 Principles

1. **Lead with the reader's agency.** "You", "your Flovatar", "build", "customise", "decide". The homepage's "Each Flovatar is custom made by YOU" (YOU in caps) is a signature move. Use it, but sparingly.
2. **Concrete before clever.** Say what happened or what you can do, then add the joke.
3. **One idea per post.** A headline, 1–3 short lines, a CTA.
4. **Lore as seasoning.** Drop in a StarDust, Flova or meta-leap reference, but the post must still make sense to a newcomer.
5. **Celebrate people.** Winners, creators, the community. Public community handles (FOTW winners, the Council, story cameos, creators) may be named and tagged: they're pseudonyms, not real names. Never add personal details beyond what the person posted publicly. Flovatar team art is still credited to "the Flovatar team" (§0.2).
6. **Honest status.** Live = say it. Not live = "coming". Never "soon™" jokes about delayed features.

### 6.3 Tone by context

| Context | Dial | Example opener |
|---|---|---|
| Product launch (shipped) | Excited, specific | "It's live! 🚀 …" |
| Feature update / changelog | Clear, list-y, light | "New in the Builder 👇" |
| Contest / giveaway | High-energy, rules crystal clear | "It's time for a giveaway! …" |
| Lore / story | Narrative, mysterious, playful | "Transmission incoming from Flova Labs…" |
| Help / onboarding / wallets | Calm, step-by-step, zero jargon | "Here's how to connect Flow Wallet in 3 steps." |
| Incident / bug | Calm, factual, no blame, no jokes | "Heads-up: listings are delayed. Your items are safe on-chain. We're on it." |
| Flova Labs (in-world) | Slick corporate parody, ™ everywhere | "Making the Right Decision has never been easier." |
| FUD News (community, paused) | Sarcastic tabloid, run by the community | Don't promise a return or present it as active. Don't impersonate the editors. |

### 6.4 Real examples from the archive (public @flovatar posts and announcements)

Good patterns to imitate. Typos and numbers are from the originals, so don't reuse the numbers.

> GM ☀️ Launch details are live!
> 💥 Drop date: Dec 16th
> 💥 1% royalty and full commercial rights 👀
> 💥 $DUST token and DAO Treasury
> 💥 Only 9,999 Flovatars available!
> *(Nov 2021: emoji-bulleted facts, a single CTA.)*

> It is official, all standard packs are SOLD OUT
> *(Dec 2021: short, confident, one fact.)*

> Flovatarians Assemble! This week's FOTW theme is Heroes! … Have fun and remember not all heroes wear capes!
> *(Mar 2022: community contest voice.)*

> The collection page will contain a long-awaited feature!
> The FLOBIT UPGRADE ⬆️
> By selecting 10 flobits of same rarity and spending X$DUST you will receive 1 BRAND NEW flobit of higher rarity!
> *(Jan 2023: feature explainer. Today, capitalise "Flobits".)*

> 🏆We've got a winner 🏆
> Expect to see a Legendary, zombie killing, skull breaking, Wooden Bat Flobit in the streets of Flova City soon🏏
> *(Sep 2023: lore-flavoured result post.)*

> Flovatar reveals FlovaChat 💬 A new AI-powered secret device FlovaLabs has secretely been working on! 📱 Have you ever daydreamed of talking with your Flovatar?
> *(Dec 2023: product as in-world gadget. Correct spelling today: "Flova Labs", "secretly".)*

> Episode 5 of A Dust Odyssey comes out today! ✨ It will premiere on YouTube at 1pm ET and a float will be claimable for the 24h after the release!
> *(Jun 2023: release note with time and perk.)*

### 6.5 Emoji

Measured on ~1,300 emoji in public @flovatar tweets and ~1,900 in #announcement (2021–2025). The most used were 🔥 🎉 👇 👀 🗞 🚀 🙏 💥 🎁 ❤️ 😱 ✨ 👉 ✅ 🏆.

- **Social posts:** 1–4 emoji. Use them as bullets (💥 ✨ ➡️ ✅) or one reaction at the end of a line (👀 🔥 🚀).
- **House set:** 🚀 launch · 👀 tease · 🔥 hype · 💥 bullet · ✨ magic/new · 🎁 prize · 🏆 winner · 🗞 news recap · 🎧 podcast · 🎬 episode · 🧵 thread · 👇 CTA · 💜 love (purple, our colour).
- **Never** in incident posts, legal/help copy or Flova Labs corporate parody, and never inside headlines on banners.

### 6.6 Hashtags and handles

- Main: **#Flovatar**, **#onFlow** (most used, with #NFT). Event tags are camel-case and one-off (#TerraKitDay, #NFTDay, #MadeWithSportvatar for Sportvatar).
- Max 2–3 hashtags, at the end. Don't use the 2022 habit of 10-hashtag tails.
- Handles: X **@flovatar**, Instagram **@flovatar_nft**, YouTube **@flovatar_live** (full list and status: §14.5). Tag `@flow_blockchain` only for Flow-relevant news.

### 6.7 Words we use / avoid

| Use | Avoid | Why |
|---|---|---|
| build, create, customise, equip, swap, mint | generate, randomise | Creator-first |
| collect, own, trade | invest, flip, ape in, pump, moon, ROI, APY, passive income | Not financial |
| utility token (ĐUST) | price talk, "number go up" | Policy since 2023 |
| holders, creators, Flovans, the community | degens, whales (in official copy) | Respect |
| live now, available today | soon™, very soon, wen | Ship-first |
| Flow Wallet, Dapper Wallet | Blocto, "any wallet" | Facts |
| on-chain SVG, fully on-chain | "stored on IPFS" | Accuracy |
| "the Flovatar team" | individual artist names | Policy |

Community greetings like **GM** ☀️ are fine on X and Instagram. Use "WAGMI", "LFG" and "fren" at most once per campaign: dated crypto-speak.

### 6.8 Do / Don't (rewrites)

| ❌ Don't | ✅ Do |
|---|---|
| "HUGE things coming soon!!! Stay tuned 🚀🚀🚀" | "The Builder now loads in under a second. Go build something 👉 flovatar.com/builder" |
| "Asteroid Islands launching next week, for real this time" | "Asteroid Islands are next on the launchpad. Your TerraKit is your ticket. 🪐" (no date unless supplied) |
| "Buy now before the floor explodes" | "Pick a Spark, add Boosters, make it yours." |
| "Art by [artist name]" | "Art by the Flovatar team" |
| "Connect your Blocto wallet" | "Connect with Flow Wallet or Dapper Wallet" |
| "Our token ĐUST is going to be worth a lot" | "Spend ĐUST on names, bios, Psyche Likees and Flobit upgrades." |

### 6.9 Formats

- **X post:** hook line (≤ 80 chars) → 1–3 bullet lines → CTA link → ≤ 2 hashtags. Image: 1600×900 or 1200×1200 (§14).
- **Thread:** "🧵" in post 1; 4–7 posts; each standalone; the last post has the CTA.
- **Instagram post:** square or 4:5 image or carousel (§14.1); caption = hook line → 1–3 short lines → "link in bio" CTA → ≤ 3 hashtags. Reels: 9:16, captions burned in.
- **YouTube:** title ≤ 70 chars (Title Case, no clickbait), thumbnail 1280 × 720, description = 2-line summary → links (flovatar.com, X, Instagram) → chapters if > 3 min.
- **Discord announcement** (only when a brief asks; Discord isn't an active brand channel, §14.5): bold title line, `@everyone` only for major news, short sections, bullets, links last. Times as "3pm ET / 8pm UTC".
- **Blog (Medium-style; blog.flovatar.com is dormant, so write one only when a brief asks):** Title Case title; a **TL;DR** box up top (house pattern since 2022); H2 sections; images every ~300 words; end with links (flovatar.com, X, Instagram, YouTube).
- **Headlines on web/banners:** UPPERCASE, ≤ 7 words, Staatliches / Korolev (e.g. "EACH FLOVATAR IS CUSTOM MADE BY YOU", "WE'VE COME A LONG WAY BUT THERE'S PLENTY MORE TO COME!"). Pair with a small pink sentence-case eyebrow ("YOU are the Creator", "The Spark of Life", "Earn Revenue").

## 7. Naming & terminology glossary

### 7.1 Spelling and capitalisation (canonical)

| Term | Correct | Plural | Wrong | Notes |
|---|---|---|---|---|
| Flovatar | **Flovatar** | Flovatars | FloVatar, flovatar (in prose), Flavatar | Brand, product and character. Lowercase only in URLs and handles. |
| Flovan | **Flovan** | Flovans | — | The alien species (lore). Community nicknames: Flovatarians, Flovies. |
| Flobit | **Flobit** | Flobits | FloBit, flobit, Flo-bit | Accessory NFT: hat, eyeglasses, accessory, background. |
| Flobot | **Flobot** | Flobots | FloBot, Flo-bot | Robot NFT built from a Flobot Constructor Kit. |
| Spark | **Spark** (Spark of Life) | Sparks | spark (as product) | The mint right. |
| Rarity Booster | **Booster** / **Rarity Booster** | Boosters | — | Rare, Epic, Legendary. |
| Rarity tiers | **Common, Rare, Epic, Legendary** (Flobits also have **Ultimate**, 1/1) | — | — | Capitalised as tier names; labels in caps: COMMON, RARE, EPIC, LEGENDARY, **ULTIMATE** (colour and glitter: §9.3.1). |
| ĐUST | **ĐUST** (Đ = U+0110 "Latin capital letter D with stroke") in all prose, headlines, UI copy, social copy, alt text and prompts; **StarDust / Dust** for the energy in lore | — | DUST and $DUST (in prose), Dust token, $Dust, ÐUST (Ð U+00D0 "Eth", used in some 2023 posts) | Technical identifiers keep plain ASCII: see §7.4. |
| Psyche Likee | **Psyche Likee** (Sy-Kee Ly-Kee) | Psyche Likees | Pysche, Psyche Like, Lykee | First ĐUST series: pet companions. |
| CMT | **CMT** = **Central Megaversal Time** | — | Coordinated Megaversal Time | Lore time standard; FT = Flovan Time, ET = Earth Time (§4.6). |
| Nostos | **Xandro Nostos** ("Nick" on Earth) | — | Zeph Nostos | Lore character (§4.4). |
| TerraKit | **TerraKit** | TerraKits | Terrakit, Terra Kit | Pack: Asteroid Island voucher + FUB voucher + Flobot Constructor Kit. |
| FUB | **FUB** = **Flovatar Universe Builder** | FUBs | Fub | No-code builder for your own NFT series. NFTs minted from a FUB are **F.U.N.** (Flovatar Universe NFTs). |
| Asteroid Island | **Asteroid Island** | Asteroid Islands | asteroid island (as product) | Land NFT. Orbits **Nova City** in the **Kaax Asteroid Belt**. Slots: 5 / 25 / 125 (Common / Epic / Legendary). |
| Flova Labs | **Flova Labs** | — | FlovaLabs, Flovalabs | In-world company, also the franchise umbrella (flovalabs.com). |
| Megaverse / Flovaverse | **Megaverse**, **Flovaverse** | — | MegaVerse | Lore. |
| A Dust Odyssey | ***A Dust Odyssey*** (italic in running text); short form **ADO** | — | A Dust Oddysey, Dust Odyssey | Illustrated podcast (2023–24), book (2025). |
| FUD News | **FUD News** = *Flovatar Universe Daily*, "F.U.D. but the good kind" | — | Fud news | Community-run weekly paper, fudnews.com (2022–24). **Paused.** Don't reference it as active. |
| FOTW | **Flovatar of the Week** (FOTW) | — | — | Weekly community contest since Feb 2022. |
| Builder | **the Builder** (Flovatar Builder, Flobot Builder) | — | builder (as product) | flovatar.com/builder |
| Marketplace / Showroom | **Marketplace**, **Showroom** | — | — | Site sections. |
| Sportvatar | **Sportvatar** | Sportvatars | SportVatar, Sport Vatar | Sister brand. The logo splits SPORT \| VATAR; text never does. |
| Sportbit / Sport Flame | **Sportbit**, **Sport Flame** | Sportbits, Sport Flames | SportBit | Sportvatar equivalents of Flobit and Spark. |
| Flow | **Flow** (the blockchain), **FLOW** (the token) | — | flow, FLOW blockchain | "Built on Flow", "on Flow". |
| Wallets | **Flow Wallet**, **Dapper Wallet** | — | Flow wallet, dapper | The only supported wallets. |
| Combo | **combo** / **hidden combo** | combos | — | A trait + Flobit set that triggers a hidden animated change on-chain. |

### 7.2 Product vocabulary (one-liners for explainers)

- **Builder**: where you design your Flovatar: pick Body, Hair, Eyes, Nose, Mouth, Facial Hair and Clothing, then add Flobits.
- **Core traits (7)**: Body, Hair, Facial Hair, Eyes, Nose, Mouth, Clothing. Fixed at mint, and each combination is unique.
- **Flobit categories (4)**: Hat, Eyeglasses, Accessory, Background. Swappable at any time.
- **Rarity Score**: 0–100, calculated from the booster tiers of the 6 highest traits.
- **Flobit Upgrade** (the "dust burner"): burn 10 Flobits of the same rarity plus ĐUST to get 1 Flobit of the next tier.
- **Creator royalty**: 1% lifetime to the original minter of a Flovatar on every resale.
- **Flovatar Inbox**: on-chain claim box for airdrops and DUST.
- **Child mode**: Builder setting that hides non-kid-friendly traits.

### 7.3 Community vocabulary

FOTW · FUD News / FUD Day (Friday; paused) · Flash Flobit Challenge · MIP (Minters Incentive Program) · Flovalympics · Poker Night · Guardians vs Villains (the two 2021 factions) · Clubs (Apes, Cats, …) · FLOAT (event badge NFT) · Backyard Flobit BurnBQ (fan Flobit ideas) · Dust Bowl / Dust Cup (2024 events) · Council / DAO (Toucans) · "Show Us Your Bits".

### 7.4 ĐUST: brand spelling vs technical identifiers

**Rule:** the token is written **ĐUST** everywhere people read it: prose, headlines, banners, UI labels, social posts, video captions, alt text, the glossary and image prompts. Copy-paste the character: `Đ` (U+0110; HTML `&#272;`; in a Mac or Windows input method type the Vietnamese "Đ").

Keep plain ASCII (`DUST`, `$DUST`, `dust`) where it's an **identifier**, not prose:

| Keep as is | Examples |
|---|---|
| Contract, type and resource names | `FlovatarDustToken`, `FlovatarDustCollectible`, `/public/FlovatarDustTokenBalance` |
| Token symbol and tickers inside code, wallets, explorers, APIs and data files | `symbol: "DUST"`, `$DUST` in a JSON field or a price feed |
| URLs, slugs, file names, hashtags | `blog.flovatar.com/all-about-dust-…`, `token-dust.png`, `dust-explainer-frame.jpg` |
| Quotes of historical posts | "💥 $DUST token and DAO Treasury" (Nov 2021), "Dust Day" (Jul 2023) |
| Titles and proper names that contain "Dust" | *A Dust Odyssey*, StarDust, Dust Bowl, Dust Cup |

Don't use the look-alike **Ð** (U+00D0, Icelandic "Eth"); some 2023 posts did. When a system can't take Unicode (an SMS gateway or an old CSV), write `DUST` and flag it. Font support for Đ is covered in §10.4.

## 8. Logo system

Base: v1.0 identity guidelines (Mar 2022), confirmed against the exported Media Pack SVGs and the live site header. All files: §17.1.

### 8.1 Anatomy

- **Logo mark**: a stylised Flovatar head in three-quarter view: big round cranium, one large oval eye (near), a small eye on the far edge, a sly closed-mouth smile, a pointed ear/horn on top, and a tilted **halo** ring above. "The horns and halo represent obedience and disobedience, which are key characteristics of all Flovatars." (v1.0)
- **Wordmark**: **FLOVATAR** in tall, condensed, slightly flared custom caps with a distinctive small-cap-style **R**. It's a drawn logotype, not a font: never retype it in Staatliches or anything else.
- **Lockups**: **Vertical** (mark above wordmark) is the **default**. **Horizontal** (mark left, wordmark right) is for wide layouts: site headers, banners, video bugs.

### 8.2 Mark variants (v1.0 p.8)

1. **Cutout roundel**: roundel with the head punched out so the background shows through (`flovatar-mark-purple-cutout-roundel`, `-white-roundel`, `-black-roundel`).
2. **Head only**: the head with eyes and mouth punched out (`flovatar-mark-pink`, `-purple`, `-white`, `-black`). Used in the site header (white) and as the app icon.
3. **Filled roundel**: roundel with the head filled in a contrasting colour (`flovatar-mark-pink-purple-roundel`).

**App/social squares**: head on a square (`-color-mix-purple-square`, `-pink-square`, `-gradient-square` with gradient `#440099` → `#230E54` top to bottom). Use these as avatars on X, Discord, YouTube and app stores.

### 8.3 Approved colourways (v1.0 p.5)

| # | Background | Mark | Wordmark | File (vertical / horizontal) |
|---|---|---|---|---|
| A **default** | Space Indigo `#411793` | Aurora Pink `#EF2AC1` (head cut out) | Sky Blue `#91E3F9` | `flovatar-logo-vertical-color-mix` / `-horizontal-color-mix` |
| B | Space Indigo | Aurora Pink | Aurora Pink | `…-pink` |
| C | Black | White | White | `…-white` |
| D | White | Aurora Pink | Space Indigo [v1.0 shows pink mark + indigo wordmark on white; no single export, so combine `mark-pink` + `logo-…-purple` wordmark] | — |
| E | White | Space Indigo | Space Indigo | `…-purple` |
| F | White | Black | Black | `…-black` |

On photos or busy art, put the **white** logo on a darkened area, or use the roundel variant. On the live site's dark night background the header uses the **white horizontal** lockup.

### 8.4 Clear space and size

- **Clear space**: on all four sides, at least the **diameter of the largest eye in the mark** (v1.0 p.7). That's about **1/5 of the mark's width** (measured on the SVG: eye ≈ 198 units on a 1,000-unit roundel).
- **Minimum size [inferred]**: mark ≥ 24 px (digital) / 8 mm (print); horizontal lockup ≥ 96 px wide; vertical lockup ≥ 64 px wide. Below that, use the head-only mark.
- **Placement conventions** (from banners and covers): ADO episode covers put the **white horizontal logo bottom-left**; marketplace banners (Flowverse, Gaia) centre the **white horizontal logo** with characters flanking it; social headers show a huge faded **FLOVATAR** wordmark behind characters (§14).

### 8.5 Misuse: never

- Recolour outside §8.3, add gradients (except the app-icon square), outlines, glows, drop shadows or 3D bevels.
- Stretch, condense, rotate, skew, or change the mark/wordmark proportions or spacing.
- Retype the wordmark in a font, or write "Flovatar" next to the mark in another typeface as a "logo".
- Separate the halo, or remove the halo or horns.
- Place it on low-contrast backgrounds (e.g. pink mark on a pink photo) or inside a busy area without a backing.
- Use the old pre-2022 logo. The rebrand went live in Mar 2022: "Unveiled a fresh new look to the whole website and created a brand new logo!" (site roadmap, Feb 2022).
- Put the Flovatar mark inside a Sportvatar lockup, or the other way round.

### 8.6 Favicons and avatars

- Favicon / app icon: head-only mark on the purple or gradient square (`flovatar-mark-color-mix-gradient-square`), 512 px source.
- Social avatar: `flovatar-social-std` (pink head on indigo) or `flovatar-social-grad`. Keep the mark centred with ≥ 15% padding for circular crops.

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
/* Flovatar · Ultimate rarity (1/1 Flobits). Generated by tools/build-tokens.py.
   Glitter = three transparent blue-noise sparkle tiles with prime sizes (509/613/757 px, "cicada principle"), each at
   its own offset: the combined pattern repeats only every 509 x 613 x 757 px, so it never visibly tiles.
   Self-host the tiles if you build outside flovatar.com. */
:root {
  --fl-rarity-ultimate: #5A1268;
  --fl-rarity-ultimate-dark: #2E0A3A;
  --fl-rarity-ultimate-glitter-gold: #FFC94D;
  --fl-rarity-ultimate-glitter-white: #FFFFFF;
  --fl-ultimate-glitter-1: url(https://brand.flovatar.com/tokens/ultimate-glitter-509.svg) 0 0 / 509px 509px;
  --fl-ultimate-glitter-2: url(https://brand.flovatar.com/tokens/ultimate-glitter-613.svg) 241px 97px / 613px 613px;
  --fl-ultimate-glitter-3: url(https://brand.flovatar.com/tokens/ultimate-glitter-757.svg) 389px 433px / 757px 757px;
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
    url(https://brand.flovatar.com/tokens/ultimate-glitter-509.svg) 0 0 / 509px 509px border-box,
    url(https://brand.flovatar.com/tokens/ultimate-glitter-757.svg) 389px 433px / 757px 757px border-box,
    linear-gradient(160deg, var(--fl-rarity-ultimate), var(--fl-rarity-ultimate-dark)) border-box;
  box-shadow: 0 0 0 1px var(--fl-rarity-ultimate-glitter-gold), 0 0 14px rgba(255,201,77,.18);
}
@media (prefers-reduced-motion: reduce) {
  .fl-ultimate::before, .fl-ultimate::after { animation: none; opacity: .7; }   /* static glitter, no twinkle */
}
```

**SVG pattern** for SVG cards, frames and on-chain art (https://brand.flovatar.com/tokens/ultimate-glitter-pattern.svg). Copy the `<defs>`, fill the shape with `url(#fl-ultimate-fill)`, then draw it again once per glitter layer on top: `url(#fl-ultimate-glitter)`, `url(#fl-ultimate-glitter-2)`, `url(#fl-ultimate-glitter-3)` (the same 509/613/757 px blue-noise layers as the CSS). A shape up to 509 px never shows a repeat even with layer 1 alone:

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="240" height="72" viewBox="0 0 240 72" role="img" aria-label="ULTIMATE">
  <!-- Flovatar Ultimate rarity (1/1 Flobits). Copy the <defs> into any SVG; fill the shape with url(#fl-ultimate-fill),
       then draw it again once per glitter layer: url(#fl-ultimate-glitter), url(#fl-ultimate-glitter-2), url(#fl-ultimate-glitter-3).
       The layers are blue-noise tiles of 509, 613 and 757 px (primes), so the combined glitter never visibly repeats. -->
  <defs>
    <linearGradient id="fl-ultimate-fill" x1="0" y1="0" x2=".35" y2="1">
      <stop offset="0" stop-color="#5A1268"/><stop offset=".45" stop-color="#5A1268"/><stop offset="1" stop-color="#2E0A3A"/>
    </linearGradient>
    <pattern id="fl-ultimate-glitter" width="509" height="509" patternUnits="userSpaceOnUse"><g fill="none" stroke-linecap="round" transform="scale(.5)"><!-- 379 blue-noise sparkles: copy them from the file --></g></pattern>
    <pattern id="fl-ultimate-glitter-2" width="613" height="613" patternUnits="userSpaceOnUse" patternTransform="translate(241 97)"><g fill="none" stroke-linecap="round" transform="scale(.5)"><!-- 458 blue-noise sparkles: copy them from the file --></g></pattern>
    <pattern id="fl-ultimate-glitter-3" width="757" height="757" patternUnits="userSpaceOnUse" patternTransform="translate(389 433)"><g fill="none" stroke-linecap="round" transform="scale(.5)"><!-- 587 blue-noise sparkles: copy them from the file --></g></pattern>
  </defs>
  <rect x="2" y="2" width="236" height="68" rx="34" fill="url(#fl-ultimate-fill)"/>
  <rect x="2" y="2" width="236" height="68" rx="34" fill="url(#fl-ultimate-glitter)"/>
  <rect x="2" y="2" width="236" height="68" rx="34" fill="url(#fl-ultimate-glitter-2)"/>
  <rect x="2" y="2" width="236" height="68" rx="34" fill="url(#fl-ultimate-glitter-3)"/>
  <rect x="2" y="2" width="236" height="68" rx="34" fill="none" stroke="#FFC94D" stroke-width="2"/>
  <text x="120" y="48" text-anchor="middle" font-family="'Korolev Compressed', Staatliches, 'Arial Narrow', sans-serif" font-weight="700" font-size="36" letter-spacing="1.5" fill="#FFFFFF" stroke="#2E0A3A" stroke-width="3" paint-order="stroke">ULTIMATE</text>
</svg>
```

### 9.4 Usage proportions [inferred from the site and covers]

~60% night/indigo backgrounds · ~20% panels and violets · ~10% Aurora/Neon Pink · ~5% Sky Blue/Periwinkle text · ~5% yellow CTAs and rarity accents. Pink and yellow are **accents**. Never set long body text in pink or yellow.

### 9.5 Contrast

Generated by `tools/build-tokens.py`. AA body text needs ≥ 4.5, AA large text (≥ 24 px, or ≥ 18.66 px bold) and UI graphics need ≥ 3.0.

| Foreground | Background | Ratio | Body text (AA 4.5) | Large text / UI (3.0) |
|---|---|---:|:---:|:---:|
| white `#FFFFFF` | night `#180830` | 18.81 | ✅ | ✅ |
| periwinkle `#AED7F7` | night `#180830` | 12.42 | ✅ | ✅ |
| sky-blue `#91E3F9` | night `#180830` | 13.04 | ✅ | ✅ |
| aurora-pink `#EF2AC1` | night `#180830` | 5.17 | ✅ | ✅ |
| neon-pink `#EB3CF2` | night `#180830` | 5.79 | ✅ | ✅ |
| cta-yellow `#FFEE50` | night `#180830` | 15.76 | ✅ | ✅ |
| cyan `#23EDFC` | night `#180830` | 13.07 | ✅ | ✅ |
| muted `#9DA4C7` | night `#180830` | 7.68 | ✅ | ✅ |
| sky-blue `#91E3F9` | space-indigo `#411793` | 8.23 | ✅ | ✅ |
| white `#FFFFFF` | space-indigo `#411793` | 11.87 | ✅ | ✅ |
| aurora-pink `#EF2AC1` | space-indigo `#411793` | 3.26 | ❌ | ✅ |
| nova-yellow `#FCEB4F` | space-indigo `#411793` | 9.69 | ✅ | ✅ |
| white `#FFFFFF` | aurora-pink `#EF2AC1` | 3.64 | ❌ | ✅ |
| deep-space-blue `#1B0D49` | aurora-pink `#EF2AC1` | 4.81 | ✅ | ✅ |
| space-indigo `#411793` | aurora-pink `#EF2AC1` | 3.26 | ❌ | ✅ |
| ink `#1A1E2D` | cta-yellow `#FFEE50` | 13.88 | ✅ | ✅ |
| ink `#1A1E2D` | cyan `#23EDFC` | 11.51 | ✅ | ✅ |
| ink `#1A1E2D` | neon-pink `#EB3CF2` | 5.10 | ✅ | ✅ |
| ink `#1A1E2D` | buy-green `#52F618` | 11.48 | ✅ | ✅ |
| space-indigo `#411793` | white `#FFFFFF` | 11.87 | ✅ | ✅ |
| deep-space-blue `#1B0D49` | white `#FFFFFF` | 17.49 | ✅ | ✅ |
| aurora-pink `#EF2AC1` | white `#FFFFFF` | 3.64 | ❌ | ✅ |
| white `#FFFFFF` | panel `#343B5A` | 10.94 | ✅ | ✅ |
| cta-yellow `#FFEE50` | panel `#343B5A` | 9.17 | ✅ | ✅ |
| white `#FFFFFF` | solar-violet `#6657D3` | 5.43 | ✅ | ✅ |
| deep-space-blue `#1B0D49` | sky-blue `#91E3F9` | 12.13 | ✅ | ✅ |
| neon-green `#D4FF36` | field-green `#283F42` | 9.66 | ✅ | ✅ |
| neon-green `#D4FF36` | pitch-black `#0C1617` | 15.89 | ✅ | ✅ |
| white `#FFFFFF` | field-green `#283F42` | 11.17 | ✅ | ✅ |
| field-green `#283F42` | neon-green `#D4FF36` | 9.66 | ✅ | ✅ |
| aquamarine `#A5F1D6` | field-green-dark `#152627` | 12.07 | ✅ | ✅ |
| white `#FFFFFF` | ultimate `#5A1268` | 12.20 | ✅ | ✅ |
| white `#FFFFFF` | ultimate-dark `#2E0A3A` | 17.20 | ✅ | ✅ |
| ultimate-glitter-gold `#FFC94D` | ultimate `#5A1268` | 7.97 | ✅ | ✅ |
| ultimate-glitter-gold `#FFC94D` | night `#180830` | 12.29 | ✅ | ✅ |
| ultimate `#5A1268` | night `#180830` | 1.54 | ❌ | ❌ |

**Rules from the table:** Aurora Pink on Space Indigo (3.26) and white on Aurora Pink (3.64) are **large-text / logo only**. For body text on pink use Deep Space Blue `#1B0D49`. All UI text on Night `#180830` passes AA.

### 9.6 Sub-brand palettes

Sportvatar and partner colours: §16.1 and §16.8.

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

## 13. UI & web components

Derived from the live flovatar.com (Nov 2026: its open-source stylesheets and screenshots). Use it for new pages, the Asteroid Island Builder, the FUB, and campaign landing pages.

### 13.1 Page shell

- **Background:** Night `#180830` with a sparse white **star field** (1–2 px dots). Inner pages start with the pink→night **header glow** (§9.2).
- **Header:** white horizontal logo at the left. Nav links on the right in **Korolev Compressed, UPPERCASE, `#FFEE50` yellow** (current page white): BUILDER · MARKETPLACE · SHOWROOM · DAO · EXPLORE. Then the **CONNECT WALLET** button.
- **Hero (home):** full-width illustrated Flova cityscape (purple/lilac sci-fi towers, round windows with pink lights) with a Flovatar on a glowing **teleport pad** under a halo-like portal ring. Below it, a big centred headline in Periwinkle.
- **Sections:** alternating left/right **art + copy** blocks: pink **eyebrow** → Periwinkle UPPERCASE **H2** → white body with Sky Blue/Periwinkle inline links. Art sits in a solid Solar-Violet **circle "spotlight"** behind the character, or on a curved planet horizon.
- **Footer:** an Aurora Pink planet arc rising from the bottom, "POWERED BY" partner row (**Flow · Flow Wallet · Dapper · Emerald City · .find**; MoonPay is no longer a partner, §16.8), then 4 link columns (FLOVATAR · GETTING STARTED · NEWS & INFO · COMMUNITY TOOLS) in light-pink Korolev on a pink field.
- **Container:** max width 1337 px, 30 px gutter (site grid).

### 13.2 Buttons

| Button | Style |
|---|---|
| **Primary (CTA)** | Yellow `#FFEE50` fill, 3 px black/Ink border, square corners, **hard offset shadow** (a translucent violet band ~8 px under the button on the site header, or 6 px down/right in Ink), label in Korolev Compressed UPPERCASE Ink. Optional white "glare" (a curved white highlight at 51% opacity, top-right corner, as on the site's `.btn-decor`). Hover: nudge 2 px toward the shadow. |
| **Secondary** | Lilac `#C7BCFB` fill (sampled; or Solar Violet `#6657D3` on light) with Ink border and offset shadow (Builder "RANDOMIZE"). |
| **Action / warning** | Orange `#FF6D03` fill with Ink border ("CHECK AVAILABILITY", colour sampled from the Builder). |
| **Outline on dark** | Transparent, 2 px white or yellow border, white label, small arrow icon ("PREVIOUS SALES →"). |
| **Pill** | Royal Violet `#5F37CB` filled pill, white Korolev caps ("SERIES 1", "WHATEVER YOU WANT!"). |
| **Disabled** | `#7C7E84` fill, no pointer events. |
| **Buy** | Round 32 px Buy Green `#52F618` badge with an Ink cart icon. |

### 13.3 Cards and panels

- **Item card (marketplace):** dark Night-violet card, **3 px border in the rarity colour** (white if none; Ultimate = glitter border + gold keyline, `.fl-ultimate-frame`), radius ~6 px, the item render centred, then name / price in Korolev Compressed. Bundles get a "stack" of 2 offset borders behind the card.
- **Stat tile:** Ink `#1A1E2D` rectangle, radius 6 px. Small grey caps label on the left ("TOTAL SALES"), big Korolev Compressed number ("12,345" + small "FLOW"). Rarity stats are coloured (Spark violet, Rare cyan, Epic yellow, Legendary pink, Ultimate purple with glitter, §9.3.1) with a small "/ max" suffix. Stat tiles are UI; in marketing copy prefer non-financial numbers (§20).
- **Panel:** Panel `#343B5A`, radius 10 px, 16–24 px padding. Holds filters, stats and the builder trait grid.
- **Trait tile (builder):** light `#F5F5F5` square with a white circle behind the trait thumbnail and a thick Ink frame. Selected = 3 px Buy Green border. The category rail uses a rarity-coloured fill per category.
- **Builder machine:** the preview sits in a sci-fi "machine" frame (panel grey-blue, bolts, a pink glowing platform disc, a porthole window with stars), with a rarity score dial ("RARITY SCORE 10.2 EPIC") top-right and Spark + Booster capsule counters on a side rail.
- **Watermark:** unminted designs get a circular "UNMINTED FLOVATAR" stamp over the preview.

### 13.4 Forms and data

- Inputs: 1–2 px pink or white border on dark, radius 5 px, Korolev label, Roboto Condensed value.
- Dropdowns: white border on dark ("FLOW WALLET ▾"), caps label.
- Timeline (roadmap): vertical line with **green check circles** (done) and **yellow ring** (planned), date in small grey caps, title in white Korolev, description in Roboto Condensed.

### 13.5 Iconography

- Brand icons (v1.0) are drawn **in outline**, Sky Blue on dark: Spark (orb with lightning), Booster (capsule), Flovatar head. Files: §17.2.
- UI icons: simple line icons (icomoon set) in white/yellow. Partner and wallet logos in their own colours, sized to the cap height.

### 13.6 Motion in UI

- 0.3 s ease for colour, background and border transitions (`$animation-speed`).
- Pulsing glows for live objects (Spark, packs "Switch On"), floating ±4–8 px idle bob for heroes [inferred from art].
- Respect `prefers-reduced-motion`: stop loops, keep the first frame.

### 13.7 Accessibility rules

- Body text ≥ 16 px. Contrast per §9.5. Never put meaning in colour alone (rarity also gets a text label: COMMON/RARE/EPIC/LEGENDARY/ULTIMATE).
- Every character image needs alt text: "Flovatar #1234: green alien with pirate hat and parrot" (name + key traits).
- Focus states: 2 px yellow outline offset 2 px.

## 14. Social media & templates

**Channel priority (relaunch):** 1 Instagram · 2 X · 3 YouTube (incl. Shorts) · 4 the podcasts. Make every campaign asset for these first; the full channel list with handles is in §14.5.

### 14.1 Sizes

"Source" = a size used in Flovatar's own files; "platform" = the current platform recommendation [inferred, verify before production].

| Use | Size (px) | Basis | Notes |
|---|---|---|---|
| X / Twitter post image | 1600 × 900 (16:9) or 1200 × 1200 | platform | Keep text and logo inside the central 90%. |
| X header | 1500 × 500 (export 3000 × 1000) | source: X header 3000 × 1000 (§17.4) | Avatar overlaps the bottom-left. Keep that area empty. |
| Profile avatar (Instagram, X, YouTube) | 1024 × 1024 | source: social avatars (§17.1) | Pink head on indigo, ≥ 15% padding for circle crops. |
| **Instagram feed** (priority 1) | 1080 × 1350 / 1080 × 1080 | platform | Carousels: up to 10 slides, same ratio. |
| Stories / Reels / Shorts | 1080 × 1920 | platform | Safe area: 250 px top and bottom. (TikTok isn't an active channel.) |
| YouTube channel art | 2560 × 1440 | source: `youtube-cover.jpg` | Safe zone 1546 × 423 centred. |
| YouTube thumbnail / ADO episode cover | 1280 × 720 | source: episode covers (§17.4) | Also 1200 × 855 (podcast hosts) and 3000 × 3000 (Spotify/Apple). |
| LinkedIn cover | 2256 × 382 | source | Inactive channel: archive only. |
| Discord announcement image | 1600 × 900 | [inferred] | Only when a brief asks (Discord isn't an active channel). Same as X. |
| Open Graph / link preview | 1200 × 630 | source: flovatar.com item pages (the older site share image was 762 × 400) | Item renders centred on a blurred zoom of themselves. |
| Marketplace banner (Flowverse) | 1940 × 500 + square 600 × 600 | source | Separate assets for Flovatar / Flobots / Components. |
| Marketplace listing (Gaia) | banner 1920 × 600, landing 2400 × 600, card 350 × 600, icon 250 circle, images 500 × 500 / 500 × 1000 | source: Gaia marketplace listing | — |
| Event badge (FLOAT) | 1500 × 1962 | source | Card frame: pink → cyan gradient border, logo top-left, event/date chips at the bottom. |
| Character render (square) | 1000 × 1000 PNG (transparent) / JPG | source: flovatar.com renders | GIF/MP4 for animated items. |
| Asteroid Island render | 3025 × 4033 (3:4 portrait) | source: Asteroid Island art (§17.4) | — |

### 14.2 Layout conventions (from existing Flovatar banners)

1. **Hero lineup:** night-purple starry sky, a **giant faded FLOVATAR wordmark** (lighter violet) across the middle, 4–8 Flovatars standing in a row on a floor line or on teleport pads, and one **hero character** floating centre under a glowing portal ring. (X header, YouTube cover, Gaia homepage banner.)
2. **Logo-centred marketplace banner:** white horizontal logo centred (with a sub-label like "FLOBOTS" in spaced caps under the wordmark), 2 characters on each side on glowing pink disc platforms, dark purple silhouetted skyline. (Flowverse.)
3. **Episode cover:** full-bleed 16:9 scene, white horizontal logo **bottom-left**, *A DUST ODYSSEY* in white Staatliches caps **bottom-right**, nothing else.
4. **Announcement card:** night background, pink eyebrow, Periwinkle uppercase headline (≤ 7 words), one render or object, CTA chip in yellow, small logo in a corner. [inferred, consistent with the site]
5. **Product explainer:** object (ĐUST coin, pack, Spark) large and centred with circular uppercase text around it ("DUST IS NEARLY LIVE – HERE'S WHAT YOU CAN DO WITH IT"), logo bottom-left, URL bottom-right. (ĐUST explainer.)
6. **"Show Us Your Bits":** single Flobit on white, then the same Flobit on a plain body (back view), as a carousel pair.

### 14.3 Recurring content series (historical, reusable)

| Series | Format |
|---|---|
| **Flovatar of the Week (FOTW)** | Weekly theme ("Heroes!"), community submits builds with a short bio. The winner gets a banner and a prize. |
| **FUD News** | **Paused.** Don't post FUD News teasers, don't promise a return, and don't reference it as active. Historical format: "FUD News #N is out! 🗞" + 2 bullet hooks + link. |
| **Flash Flobit Challenge** | "Equip X by snapshot time" → rewards. |
| **Giveaway** | "It's time for a giveaway! 1️⃣ Like + RT 2️⃣ Follow @flovatar 3️⃣ Tag 3 friends", prize line, snapshot date/time. |
| **Episode drop** | "Episode N of *A Dust Odyssey* is out! 🎧" + where to listen/watch (YouTube, Spotify, Apple Podcasts) + FLOAT if any. |
| **Milestone** | "2 big milestones reached today 🍾" + two concrete facts. |
| **Flovatar Friday** | "What shenanigans are you and your Flovatars getting into today? 😎" |

### 14.4 Post copy templates

**Shipped feature**
```
{Feature name} is live! 🚀

💥 {benefit 1}
💥 {benefit 2}
💥 {benefit 3}

Try it 👉 {url}
#Flovatar #onFlow
```

**Community winner**
```
🏆 We've got a winner! 🏆
{Winner's public handle}'s {what they made} takes {contest}. {One playful lore line.}
Congrats to everyone who joined 🙌
```

Public community handles may be named and tagged: they're pseudonyms, not real names. Don't add personal details beyond what the person posted publicly.

**Teaser (unshipped, no date)**
```
👀 Something is stirring in the Kaax Asteroid Belt…
{one-line hint}
#Flovatar
```

**Relaunch / comeback (project-level; §3.2)**
```
The Builder is back on the launchpad 🚀
💥 {live proof 1 from §3.1}
💥 {live proof 2}
Your creativity powers the Megaverse. Again.
👉 flovatar.com/builder
#Flovatar #onFlow
```

**Instagram caption**
```
{hook line, ≤ 80 chars} ✨
{1–2 short lines}
Link in bio 👉 flovatar.com
#Flovatar #onFlow
```

**YouTube description**
```
{2-line summary of the video}

Build yours: https://flovatar.com/builder
Instagram: https://www.instagram.com/flovatar_nft/ · X: https://x.com/flovatar
{chapters, if longer than 3 min}
```

### 14.5 Official channels (as of 2026-11-24)

**Active: post here.** These are the only channels to list as "follow us" in relaunch materials.

| Priority | Channel | Handle | URL |
|---|---|---|---|
| 1 | **Instagram** | @flovatar_nft | https://www.instagram.com/flovatar_nft/ |
| 2 | **X / Twitter** | @flovatar | https://x.com/flovatar |
| 3 | **YouTube** | Flovatar, @flovatar_live | https://www.youtube.com/@flovatar_live |
| 4 | **Podcasts**: *Flovatar – A Dust Odyssey* | — | Spotify https://open.spotify.com/show/76q2XUsVhmMUIP4odR81Kn · Apple Podcasts https://podcasts.apple.com/us/podcast/flovatar-a-dust-odyssey/id1688384936 · all platforms https://story.flovatar.com |

Sources: flovatar.com footer (X, Instagram), fudnews.com footer (X, Instagram, YouTube, Spotify), story.flovatar.com and the 2023 #announcement posts (podcast), checked 2026-11-24.

**Not active: don't list them as places we post.** Link to them only when a brief asks.

| Channel | Handle / URL | What the sources say |
|---|---|---|
| Discord | discord.gg/flovatar | The community server. Still linked in the flovatar.com footer and the wiki; the last #announcement posts are from Dec 2025. Not an actively posted brand channel. |
| Blog (Medium) | blog.flovatar.com | Archive. Last post 7 Jun 2024. Fine as a reference link for old explainers. |
| TikTok | @flovatar | Listed on the old wiki only. Not active. |
| Facebook / LinkedIn | facebook.com/flovatar · linkedin.com/company/flovatar | Listed on the old wiki only. Not active. |
| Telegram | — | No official Flovatar channel in the sources (one 2021 AMA ran in the Flow Spain group). Treat any "Flovatar Telegram" as unofficial. |
| FUD News | fudnews.com · X @FuchFaceMcGee | Community paper. Paused (§16.6). |
| C-3PFLO | X @C_3PFLO | Marketplace bot account linked in the site footer. Not a brand voice. |
| Story character accounts | @damus_flovatar, @NostosFlovatar, @BigDadaFlovatar | 2023 story-rollout accounts. Not in the active list. |
| Sportvatar | X @sportvatar · sportvatar.com | The sister brand's own channel (§16.1). |

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

## 16. Sub-brands & partners

### 16.1 Sportvatar

- **What:** "A customizable digital athlete, made for and by sports fans." Sister product built by the Flovatar team (launched May 2023 with RCS MediaGroup: *La Gazzetta dello Sport* and *MARCA*). sportvatar.com, EN/IT/ES.
- **Mechanics:** **Sport Flame** (≈ Spark) + **Sportbits** (≈ Flobits, incl. Number Modifier Sportbits). Seven core traits: Body, Clothing, Eyes, Nose, Mouth, Hair, Facial Hair. Rarity **Common / Rare / Epic / Legendary** (shown as flames). Abilities: Mental strength, Speed, Power, Technique, Endurance. Marketplace fee 5%. Wallets: **Flow Wallet + Dapper Wallet** (Nov 2026).
- **Palette (Sportvatar guidelines v1.0, Mar 2023):** Field Green `#283F42` (primary bg) · **Neon Green `#D4FF36`** (primary accent) · Slate Green `#607A7C` · Aquamarine `#A5F1D6` · Field Green Dark `#152627` · Prussian Grey `#353238`. Live site background: `#0C1617`.
- **Type:** Korolev Compressed Bold (headlines, UPPERCASE) + Roboto Condensed Regular (body). The live site falls back to Staatliches for headlines; "Varsity Team Bold" is used for shirt numbers only.
- **Logo:** mark = a Sportvatar head **wearing a sweatband** (same 3-variant system as Flovatar: cutout roundel, head only, filled roundel). Wordmark = **SPORT** reversed out of a neon parallelogram + **VATAR** in an outlined parallelogram, slanted like a scoreboard. Default: Neon Green on Field Green. Vertical lockup default, horizontal allowed. Clear space = diameter of the largest eye. Files: §17.1.
- **Voice:** sporty, energetic, short ("CREATE AND COLLECT YOUR DIGITAL ATHLETES", "YOU ARE THE CREATOR", "SPORTVATARS ARE CUSTOM MADE BY YOU", "WEAR ACCESSORIES TO BOOST YOUR SPORTVATAR"). Hashtag **#MadeWithSportvatar**.
- **Art:** the Flovatar chibi system in sports kits, a **thumbs-up** pose, standing on a dark disc with a neon-green rim; sport balls as icons.
- **Never:** real club crests or player likenesses without a licence. Don't mix Flovatar pink/indigo into Sportvatar UI. Don't feature the 2023 launch partners in new copy (§16.8): the launch history above is background, not copy.

### 16.2 Flobots

Customisable robot helpers. In the lore, they terraform and maintain your Asteroid Island; FL01D is a first-generation Flobot. Built in the **Flobot Builder** (live since 24 Sep 2022) from a **Flobot Constructor Kit** (Common / Epic / Legendary; 5 Common kits make 1 Epic, 5 Epics make 1 Legendary). Parts: Head, Face, Body, Arms, Legs. Style: §11.6. Flowverse used a dedicated "FLOVATAR / FLOBOTS" lockup (logo + spaced caps sub-label).

### 16.3 Psyche Likee

Pet companions "perfectly matched to your personality" (Flova Labs product). The first **ĐUST Series**: minted with ĐUST in the ĐUST Builder since 10 Jul 2023, with each trait's price rising 5% per use. Parts: Face, Head, Body, Arms, Legs. Style: plush monster pets (§11.6). Spelling: Psyche Likee (pronounced "Sy-Kee Ly-Kee").

### 16.4 ĐUST

- **Is:** the Flovatar universe's **utility token** on Flow (mainnet since 10 Jul 2023, "Dust Day"). In the lore, **StarDust**.
- **Used for (delivered):** naming and bio, 3D model unlock, location, Flobit Upgrade, Psyche Likee minting, ĐUST Flobit packs, FlovaChat, community events.
- **Visual:** a thick **pink/magenta coin with a white Đ** (`#EF2AC1` family) with a coin edge, often spinning.
- **Spelling:** **ĐUST** everywhere in copy and graphics. Technical identifiers such as `FlovatarDustToken` or the `DUST` symbol in code stay ASCII (§7.4). Font support for Đ: §10.4.
- **Copy rules:** "utility token", never price talk or yield claims. Don't quote supply or emission figures unless a human supplies current on-chain data.

### 16.5 TerraKit · Asteroid Islands · FUB · Nova City

- **TerraKit** (pre-sale Sep 2022): 1 **Asteroid Island** voucher + 1 **FUB** voucher + 1 **Flobot Constructor Kit**, each Common, Epic or Legendary. Live voucher art editions: 400 / 2,000 / 17,600 (Legendary / Epic / Rare art suffixes).
- **Asteroid Island:** a customisable home NFT that displays your NFTs. It orbits **Nova City** in the **Kaax Asteroid Belt**. Art system: 3025 × 4033 portrait canvas; layers sky → island base → structures → FUB → billboard/foreground; biomes rock, desert, desert-rock, ice (common/epic), jungle and volcano (legendary), oasis (concept); structures (water tank, telescope, castles, fortresses, towers, scaffolding); recolourable rock classes; **slots** (green 300 × 300 placeholders) where residents and buildings go. Billboards show animated screens with the Flova Labs logo.
- **Slots:** a **Common** Asteroid Island has **5 slots**, an **Epic** one **25** (5 × 5) and a **Legendary** one **125** (25 × 5), as published in the blog post "What the FUB" (26 Sep 2022). Merging islands adds their slots together (same post). These and the FUB numbers below are the only Asteroid/FUB numbers you may publish. The Asteroid Island art in §17.4 is a style reference: never count slots from it.
- **FUB, Flovatar Universe Builder:** a no-code tool to create your own NFT series and builder (traits, max mints, prices); NFTs from a FUB are **F.U.N.** (Flovatar Universe NFTs). Key art: floating islands linked by speech-bubble "pins" (cars, ships) over a purple sky (`fub-ecosystem-key-art.jpg`).
- **Status:** see §3.1. Not on mainnet as of 2026-11-24; it's a relaunch pillar.
- **FUB design assistant:** the FUB includes an optional AI design assistant from **Big Dada** (the Flova AI of *A Dust Odyssey*). It helps creators set up their collection and draft trait art, and it runs on **ĐUST** burned per use. Its output follows this guide: the brand rules apply to assisted designs exactly as to hand-made ones. Public copy may say the FUB is AI-assisted and that the assistant is powered by ĐUST. Don't name the assistant, its effort levels or the AI models behind it, and don't quote ĐUST costs until they are announced.
- **FUB numbers (published Sep 2022, may be quoted):** a FUB has **25 / 125 / 625 trait slots** (Common / Epic / Legendary; one slot = one trait, grouped into layers as the creator likes) and a maximum of **500 / 2,500 / 12,500 F.U.N. mints**. Merging FUBs adds their slots and mints together, every 5 merged move up one rarity, and up to **30** TerraKit FUBs can be merged (750 slots). Sales pay **95% to the creator and 5% to the Flovatar treasury**, directly and non-custodially. Source: blog posts "Introducing the Flovatar TerraKit Pack" (5 Sep 2022) and "What the FUB" (26 Sep 2022).
- **FUB copy rule:** say **"coming"**. No dates. Quote only the numbers above and the Asteroid Island slots (5 / 25 / 125); other FUB specs (prices, fees beyond the 95 / 5 split, layer limits, the assistant's costs) stay unpublished until announced.

### 16.6 Storyworld · *A Dust Odyssey* · Flova Labs

- ***A Dust Odyssey*:** origin story of the Flovans on Earth. Illustrated podcast (trailer 3 May 2023, Ep. 1 19 May 2023, finale 22 Mar 2024; YouTube, Spotify, Apple); **book** (ebook, paperback, hardcover) on Amazon since 16 Dec 2025; **The book is the canon**: it wins over the podcast and every other storyworld source (§4.8). Title treatment: **A DUST ODYSSEY** in white Staatliches caps; in the book, the Flovatar vertical logo in Space Indigo above the title in indigo caps.
- **Flova Labs:** the in-world corporation and the franchise umbrella (flovalabs.com, "© 5054 Flova Labs"). Voice: slick corporate parody with ™ marks and sinister cheer ("Predictability = Prosperity", "Making the Right Decision has never been easier", "A Plan for Planet B"). Its logo appears on in-world billboards. Use it for lore marketing ("transmissions"), never for real corporate statements.
- **FUD News** (*Flovatar Universe Daily*, "F.U.D. but the good kind"): weekly community paper (Apr 2022 – 2024) with a sarcastic tabloid voice (Ron Flogundy). **Status (2026-11-24): paused.** Don't promise a return, don't reference it as active ("this week's FUD News"), and don't write as FUD or impersonate its editors. Linking archive issues as history is fine.

### 16.7 Shared rules for all family brands

All family brands use the **same outline and shading system** (§11.2) and the **same rarity colours** (§9.3). Sub-brand colour applies to UI and marketing, not to the character rendering style.

### 16.8 Partners & co-branding

| Partner | Use | Assets |
|---|---|---|
| **Flow** (blockchain) | "Built on Flow" badge on footers, decks, launch graphics | `built-on-flow-*` (green, black/white). Flow green `#00EF8B` only inside Flow's own marks. |
| **Flow Wallet** | Wallet instructions, onboarding | Name in text: "Flow Wallet". Link: wallet.flow.com. Use their official logo only when supplied. |
| **Dapper Wallet** (Dapper Labs) | Wallet instructions; card/USD purchases on Sportvatar | `logo-dapper.svg` (purple `#7A2AD9`). |
| **Emerald City** (FLOAT, Toucans) | Footer "Powered by" row | `logo-emerald-city-on-dark.svg` (for dark backgrounds) |
| **.find** | Footer "Powered by" row | `logo-find-white.svg` (white, for dark backgrounds) |
| **Historical (don't feature in new material)** | Graffle, Gaia, Flowverse, Flowty, Increment.fi, MFL, RCS MediaGroup | — |

**Footer "Powered by" row:** Flow · Flow Wallet · Dapper · Emerald City · .find, in that order, in their own colours or all-white on dark.

**Note for agents: MoonPay is no longer a partner.** Remove MoonPay from every new material: footers, "Powered by" rows, onboarding and "buy FLOW" steps, decks and partner lists. Don't use its logo.

**Co-branding rules:**
- Lockup: Flovatar logo × partner logo, separated by a thin "×" or a vertical rule, with equal optical height and clear space ≥ the Flovatar eye diameter on all sides. Flovatar comes first on Flovatar-owned channels.
- Partner logos in their own colours, or all-white on dark. Never recolour them into Flovatar pink.
- On co-branding with a partner, follow the brief agreed with that partner.
- Never imply partnership, endorsement or listing status that isn't confirmed for today.
- **Blocto:** shut down (Dec 2025). Remove it from all new materials.
- **MoonPay:** no longer a partner. Remove it from all new materials.

## 17. Asset index

All files are served from `https://brand.flovatar.com/assets/…` (repo path `web/assets/…`). The full machine-readable list is at https://brand.flovatar.com/assets/manifest.json. Everything listed here is public. Need source files (vector masters, layered art, video masters)? Contact the Flovatar team via the official channels (§14.5).

### 17.1 Logos

| Asset | SVG | PNG |
|---|---|---|
| **Primary: vertical, colour mix** (pink mark, sky-blue wordmark, for indigo backgrounds) | [svg](https://brand.flovatar.com/assets/logos/flovatar/svg/flovatar-logo-vertical-color-mix.svg) | [png](https://brand.flovatar.com/assets/logos/flovatar/png/flovatar-logo-vertical-color-mix.png) |
| Horizontal, colour mix | [svg](https://brand.flovatar.com/assets/logos/flovatar/svg/flovatar-logo-horizontal-color-mix.svg) | [png](https://brand.flovatar.com/assets/logos/flovatar/png/flovatar-logo-horizontal-color-mix.png) |
| Horizontal, white (dark backgrounds, video bug) | [svg](https://brand.flovatar.com/assets/logos/flovatar/svg/flovatar-logo-horizontal-white.svg) | [png](https://brand.flovatar.com/assets/logos/flovatar/png/flovatar-logo-horizontal-white.png) |
| Vertical / horizontal: pink, purple (indigo), white, black | `…/svg/flovatar-logo-{vertical,horizontal}-{pink,purple,white,black}.svg` | `…/png/…png` |
| Mark: head only (pink, purple, white, black) | `…/svg/flovatar-mark-{pink,purple,white,black}.svg` | `…/png/…png` |
| Mark: roundels (purple cutout, white, black, pink-purple filled) | `…/svg/flovatar-mark-{purple-cutout,white,black,pink-purple}-roundel.svg` | `…/png/…png` |
| App-icon squares (purple, pink, gradient) | `…/svg/flovatar-mark-color-mix-{purple,pink,gradient}-square.svg` | `…/png/…png` |
| Social avatars | — | `…/png/flovatar-social-{std,grad,pink,trans-indigo,trans-pink}.png` |
| Site header logo (as used on flovatar.com) | [svg](https://brand.flovatar.com/assets/logos/flovatar/svg/flovatar-logo-web-header.svg) | — |
| **Sportvatar**: colour horizontal, single colour (green/white/black), text-only, mono marks (neon/dark/white/black), app icons | `https://brand.flovatar.com/assets/logos/sportvatar/svg/…` | `…/png/…` |

### 17.2 Icons and product objects

`https://brand.flovatar.com/assets/icons/`: `icon-spark.png`, `icon-booster.png`, `icon-flovatar.png` (v1.0 Sky Blue outline icons) · `spark.svg`, `spark-overcharged.svg` · `booster-rare.svg`, `booster-epic.svg`, `booster-legendary.svg` · `token-dust.png`, `token-dust-stack.png` · `pack-dust.svg`, `pack-terrakit.svg` · `psyche-likee.svg` · `flobot-spark-{rare,epic,legendary}.svg` · `flobits-rarity.svg` · `sportvatar-rarity-flame-{common,rare,epic,legendary}.svg`

### 17.3 Character samples (real on-chain renders, art by the Flovatar team)

- Flovatars: `https://brand.flovatar.com/assets/samples/flovatar/flovatar-{id}.webp` for ids 3, 52, 260, 445, 475, 875, 1192, 1763, 2073, 2324, 2860, 3167, 4135, 4200, 4908, 4983, 6313, 6570 (PNG 1000 px also for 3, 52, 1763, 2073, 4200, 6313).
- Flobots: `…/samples/flobot/flobot-{23,72,153,158,265,323}.webp`
- Psyche Likees: `…/samples/psyche-likee/psyche-likee-{86,131,167,182,614,710}.webp`
- Sportvatars: `…/samples/sportvatar/sportvatar-{133,195,205,384,482,1048}.webp`
- Flobits: `…/samples/flobit/flobit-{221,572,758,769,873,898}.webp`
- **Any live item:** `https://flovatar.com/api/image/r/{type}/{id}/{variant}` with type `flovatar | flobot | collectible | template` and variant `full.png | full.jpg | nobg.png | thumb.jpg | og.jpg | anim.gif | anim.mp4` (nobg = no background). Sportvatar: `https://sportvatar.com/api/image/r/sportvatar/{id}/full.png`. Item pages: `https://flovatar.com/flovatars/{id}`.
- **Any template as SVG** (a trait, Flobit, Flobot part, Spark or booster on its 3000×3000 canvas): `https://flovatar.com/api/image/template/{templateId}`.

### 17.4 Storyworld, Asteroids, references

- *A Dust Odyssey*: `https://brand.flovatar.com/assets/story/ado-poster.jpg`, `ado-ep1-1-cover.jpg`, `ado-ep2-cover.jpg`, `ado-ep5-cover.jpg`, `ado-da-vinci.jpg`, `ado-showdown.jpg`, `ado-testnet.jpg`, `ado-medici.jpg`, `ado-fl01d-on-the-beach.jpg`
- Asteroid Islands / FUB: `https://brand.flovatar.com/assets/asteroids/asteroid-jungle-legendary-castle.jpg`, `asteroid-volcano-legendary-stone-fortress.jpg`, `asteroid-rock-castle-epic.jpg`, `asteroid-oasis-common.jpg` (style references; slot counts are in §16.5), `fub-ecosystem-key-art.jpg`
- Layout references: `https://brand.flovatar.com/assets/references/` → `x-header-3000x1000.jpg`, `youtube-cover-2560x1440.jpg`, `linkedin-cover-2256x382.jpg`, `flowverse-flovatar-1940x500.jpg`, `flowverse-flobots-1940x500.jpg`, `flowverse-flovatar-600x600.jpg`, `gaia-homepage-banner-1920x600.jpg`, `gaia-card-730x1251.jpg`, `site-share-762x400.jpg`, `float-ama-badge-1500x1962.jpg`, `show-us-your-bits-jetpack.jpg`, `dust-explainer-frame.jpg`, `pack-v2.png`, `sportvatar-builder-scene.jpg`
- SVG construction figures (§12): `https://brand.flovatar.com/assets/anatomy/` → `flovatar-layer-stack.webp`, `flovatar-anchor-map.webp`, `flobot-layer-stack.webp`, `psyche-likee-layer-stack.webp`, `combo-anatomy.webp`, `combo-order.webp`
- Historical guides (reference only): `references/flovatar-brand-guidelines-v1.0-SUPERSEDED.pdf`, page renders `references/v1-guidelines-p{01,05–12}.jpg`; Sportvatar guide `references/sportvatar-brand-guidelines-v1.0.pdf` (current for Sportvatar).
- Partner badges: `https://brand.flovatar.com/assets/partners/` → `built-on-flow-horizontal-green.svg` (+ b/w, compact variants), `logo-flow.svg`, `logo-flow-black.svg`, `logo-dapper.svg`, `logo-emerald-city-on-dark.svg`, `logo-find-white.svg`. (No MoonPay: it's no longer a partner.)
- Tokens: `https://brand.flovatar.com/tokens/design-tokens.json`, `tokens.css`, `contrast.md`; Ultimate rarity: `ultimate.css`, glitter layers `ultimate-glitter-509.svg`, `ultimate-glitter-613.svg`, `ultimate-glitter-757.svg`, `ultimate-glitter-pattern.svg`.

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

## 19. QA checklist (run before handing anything back)

**Facts & policy**
- [ ] Every claim is live today or labelled "coming", with no dates for unshipped items unless the brief gave one (§3).
- [ ] Numbers come only from §20 (with their date) or from the brief. Non-financial numbers ("over 6,700 Flovatars"); no marketplace FLOW totals or sales counts.
- [ ] No artist, illustrator, writer or voice actor named. Credit reads "the Flovatar team".
- [ ] No legal, financial, treasury, fundraising or personal topics.
- [ ] No price, investment, yield or "floor" language. ĐUST = utility token.
- [ ] Wallets: Flow Wallet and Dapper Wallet only. No Blocto.
- [ ] Family-friendly. No real-world politics.
- [ ] AI-generated art (§11.9): non-commercial, **or** commercial only for the requester's own Flovatar(s) while they hold it (the Flovatar with its equipped Flobits; story characters and logos stay non-commercial), **or** official Flovatar team work. Disclosed when the brief asks. Never presented as a real NFT or an official release.
- [ ] Comeback copy is project-level only (§3.2). The umbrella line is verbatim.
- [ ] Channels: only Instagram, X, YouTube and the podcasts are listed as active (§14.5). FUD News isn't presented as active.
- [ ] Lore follows the book (§4.8): Xandro Nostos, CMT = Central Megaversal Time, Meta Highway FT 4975.
- [ ] Asteroid Island slots, if quoted, are 5 / 25 / 125; FUB numbers, if quoted, are 25 / 125 / 625 trait slots, 500 / 2,500 / 12,500 mints, merge up to 30, 95 / 5 split (§16.5). No other Asteroid/FUB specs, no dates; FUB = "coming". AI-assisted FUB copy follows §16.5 (Big Dada, powered by ĐUST; no assistant name, models or costs).
- [ ] Partners: only the current partners in §16.8; no historical partners (incl. Sportvatar's 2023 launch partners) and no MoonPay anywhere. "Powered by" = Flow · Flow Wallet · Dapper · Emerald City · .find.
- [ ] Community handles only as posted publicly; no personal details.

**Language**
- [ ] Spellings per §7.1 (Flovatar, Flobit, Flobot, **ĐUST** with Đ U+0110, Psyche Likee, TerraKit, FUB, Flova Labs, *A Dust Odyssey*, Sportvatar). Plain DUST/$DUST only in identifiers or historical quotes (§7.4).
- [ ] Voice per §6: concrete first, "you"-centred, 1–4 emoji on social (none in incident/help copy), ≤ 2–3 hashtags.
- [ ] Headlines UPPERCASE and ≤ 7 words on graphics.
- [ ] Times in ET + UTC. Links tested.

**Visual**
- [ ] Logo is an official file (§17.1), an approved colourway (§8.3), with clear space and minimum size respected. Not retyped, recoloured or effected.
- [ ] Colours from §9 only. Rarity colours exact; Ultimate always with glitter, gold keyline on dark and the ULTIMATE label (§9.3.1). Text contrast passes §9.5.
- [ ] Type: Staatliches / Korolev / Roboto Condensed only (agencies and freelancers: Staatliches + Roboto Condensed). The Đ renders (no tofu, no plain D) in the final export (§10.4).
- [ ] Characters on-model (§11.3): big round head, white eyes (near eye bigger), thick black uniform outline, flat + one shadow tone, ground shadow.
- [ ] Generated art isn't passed off as a real NFT. Real items use real renders.
- [ ] New SVG assets pass the SVG QA checklist (§12.11). Existing templates untouched.
- [ ] Sizes match §14.1. Safe areas respected. Alt text written.

**Motion**
- [ ] Loops are seamless. Reveals hold ≥ 1 s. Outlines stable. Reduced-motion fallback provided for web.
- [ ] Captions burned in for social video. End card has logo + CTA.

## 20. Facts sheet (numbers you may quote, with dates)

Only quote numbers from this table, with the "as of" date, or numbers supplied in a brief. Re-check live figures before a big campaign.

### 20.1 Product facts (stable)

| Fact | Value | Source |
|---|---|---|
| Launch (Genesis public drop) | 16 Dec 2021 (presale 14 Dec 2021) | Discord announcements |
| Blockchain | Flow; fully on-chain SVG art | contracts |
| Genesis cap | 9,999 Sparks / Flovatars | lite paper |
| Genesis sell-out | Standard packs sold out 23 Dec 2021; Series 1 fully sold out 28 Dec 2021 | @flovatar |
| Combinations | "over 100 billion possible unique combinations" across 11 trait and Flobit categories | flovatar.com homepage |
| Core traits / Flobit categories | 7 (Body, Hair, Facial Hair, Eyes, Nose, Mouth, Clothing) / 4 (Hat, Eyeglasses, Accessory, Background) | lite paper, Builder |
| Creator royalty / marketplace fee | 1% lifetime to the minter / 5% | lite paper, homepage |
| Flobit Series 2 | 23 Aug 2022, sold out in 11 minutes | @flovatar |
| Flobot Builder live | 24 Sep 2022 | @flovatar |
| ĐUST on mainnet | 10 Jul 2023 ("Dust Day") | Discord announcements |
| Psyche Likee minting opened | 10 Jul 2023 | Discord announcements |
| Sportvatar announced | 4 May 2023 | blog |
| *A Dust Odyssey* podcast | Trailer 3 May 2023 · Ep. 1 19 May 2023 · finale 22 Mar 2024 · 10 episodes in 20 parts | Discord announcements, YouTube, Spotify |
| *A Dust Odyssey* book | Ebook, paperback, hardcover on Amazon since 16 Dec 2025 | Discord announcement |
| Code open-sourced | Dec 2025, github.com/flovatar | Discord announcement |
| Faster flovatar.com + sportvatar.com live | Nov 2026 | sites |
| Supported wallets | Flow Wallet, Dapper Wallet (Nov 2026) | sites |
| Asteroid Island slots | Common 5 · Epic 25 · Legendary 125 (merging adds slots) | blog "What the FUB", 26 Sep 2022 |
| FUB trait slots / max mints | Common 25 / 500 · Epic 125 / 2,500 · Legendary 625 / 12,500; merging adds both, every 5 merged = next rarity, up to 30 FUBs (750 slots) | blogs "Introducing the Flovatar TerraKit Pack", 5 Sep 2022, and "What the FUB", 26 Sep 2022 |
| FUB sales split | 95% creator · 5% Flovatar treasury, paid directly by the contract | blog "What the FUB", 26 Sep 2022 |

### 20.2 Live numbers (as of 2026-11-24)

| Metric | Value | Source |
|---|---|---|
| Flovatars minted | 6,720 | on-chain data (via flovatar.com) |
| Sparks burned (used to mint) | 6,798 / 9,999 | flovatar.com marketplace stats |
| Rare / Epic / Legendary Boosters burned | 15,612 / 18,747 · 3,195 / 3,500 · 275 / 350 | flovatar.com marketplace stats |
| Flobots minted | 609 | on-chain data (via flovatar.com) |
| Psyche Likees minted | 806 | on-chain data (via flovatar.com) |
| Sportvatars minted | 1,107 | on-chain data (via sportvatar.com) |
| Series-1 Flovatar art templates (traits + Flobits) | 756 on-chain SVG templates | on-chain data |

**Numbers rule:** prefer non-financial numbers ("over 6,700 Flovatars"). Marketplace totals (FLOW volume, sales counts, highest sale) stay out of copy.

⚠️ The "Flovatars minted" (6,720) and "Sparks burned" (6,798, stats panel) figures come from different counters. In copy, say **"over 6,700 Flovatars"**. Don't quote both.

### 20.3 Don't quote (unverified or sensitive)

Marketplace FLOW totals, sales counts and highest sales, TerraKit sales totals, ĐUST supply/emission/treasury figures, revenue, fundraising, Discord member counts, anything about partners' current contractual status, FUB trait-slot and max-mint numbers, FUB revenue splits, and the older drifting combination counts ("3 billion", "10B+", "103 billion").

## 21. Version

**Version 2.6.0** · 2026-11-24. Scheme: `MAJOR.MINOR.PATCH` (MAJOR = identity change, MINOR = new sections or assets, PATCH = corrections). Agents should state which version they used.

**Source of truth:** the public git repo https://github.com/flovatar/flovatar-brand (`guide/*.md`; `BRAND.md`, `llms.txt` and this site are generated from it). The site is public and indexable. The *Flovatar Identity Guidelines v1.0* PDF (Mar 2022) is the historical predecessor of this guide: `https://brand.flovatar.com/assets/references/flovatar-brand-guidelines-v1.0-SUPERSEDED.pdf`.
