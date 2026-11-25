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
