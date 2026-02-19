---
type: topic
confidence: high
aliases:
  - Mastering
  - Audio Mastering
  - Mastering Chain
tags:
  - domain/mastering
  - type/topic
  - channel/mastering-talk
created: 2026-02-17
modified: 2026-02-18
---

# Mastering Workflows

## Summary
> [!abstract]
> Mastering is the final stage of audio production where a stereo mix (or stems) is processed to achieve competitive loudness, tonal balance, and format-readiness for distribution. This page covers mastering philosophy, chain signal flow, loudness standards, limiter strategies, stem mastering, the DIY-vs-professional debate, and career guidance — drawing from 22,909 messages of dedicated mastering discussion in #mastering-talk alongside mixing-adjacent perspectives from #mixing-talk and #daw-talk.

## Detail

### Mastering Philosophy

The most foundational insight from #mastering-talk is that mastering is as much a philosophical practice as a technical one. The channel's dominant contributor, Nomograph Mastering (5,730 substantive messages, mastering engineer for Lana Del Rey and Kendrick Lamar), consistently emphasizes this:

> [!quote] Nomograph Mastering (2024-11-23) — 44 reactions
> "I hope that you have a sense of the scale of Mastering's contribution to a project like this. Let's keep things in proportion and acknowledge the relative scale of invention and artistry in the songs, performances and production and what I did at the end. Not feigning humility, or diminishing my work. Just restating why this work is compelling, and it's not equilibrium."

> [!quote] Nomograph Mastering (2025-11-22) — pinned
> "I would counsel that many many engineers fall into the trap of pursuing what they think is 'correct' or 'good' without ever developing any kind of taste or artistic identity."

### Mastering Chain Basics

A typical mastering chain follows a general order: corrective EQ, compression or multiband dynamics, saturation or harmonic enhancement, stereo imaging, a final limiter, and dithering. The goal is to polish the mix without fundamentally altering it. See [[Mastering Signal Chain]] for detailed coverage of chain order, converter headroom, and processing philosophy.

The #mastering-talk community repeatedly emphasizes that real-world chains are much simpler than beginners expect — many professional masters use only EQ and a limiter, with compression playing a far smaller role than internet discourse suggests.

> [!quote] Nomograph Mastering (2023-01-15) — 5 reactions
> "If I was teaching someone modern mastering, compression would be way way down the list of priorities."

### Loudness Standards (LUFS)

See [[Loudness Standards and Streaming Delivery]] for comprehensive coverage. The key community consensus is that targeting a specific LUFS number (e.g., -14 LUFS) is largely misguided:

> [!quote] Rollmottle (2023-01-26) — 22 reactions, pinned
> "Just master the material for the material."

> [!quote] Nomograph Mastering (2023-01-26) — pinned
> "The dedication with which a Mastering Engineer advocates -14 is inversely proportional to the amount of records they've done that you've heard of."

Perceived loudness is primarily determined by the arrangement and mix, not mastering processing. If a mix needs to be loud, that loudness must be built into the mix.

### Limiter Strategies

The final limiter is the most discussed processor in #mastering-talk (1,213 messages). Popular choices include [[FabFilter]] Pro-L 2, Sonnox Oxford Limiter, and [[iZotope]] Ozone's Maximizer. Key insights:

- **Clipping before limiting** reduces limiter workload — many engineers use a clipper (Boz Big Clipper, StandardClip) to handle transient peaks first
- **Volume rides into the limiter** manage sections with wildly different energy, reducing the need for heavy limiting
- **Multiple stages of gentle limiting** achieve loudness more transparently than one heavy limiter
- True peak ceiling of **-1.0 dBTP** is standard practice for streaming delivery

> [!quote] Nomograph Mastering (2025-06-29) — 17 reactions
> "An easy and often overlooked solution is just to do a volume ride *into* the limiter. It's diving for huge gain reduction and you can make its work easier by just carefully shaving off a few dB on the choruses."

### Stem Mastering

Stem mastering involves receiving grouped submixes (typically drums, bass, vocals, instruments) rather than a single stereo mix. This gives the mastering engineer more control over balance and problem-solving without requiring a full remix.

> [!quote] hebakadry (2025-05-06) — 9 reactions
> "I did it recently on the new Trentemøller record; even though he's an insanely talented mixer/producer and has mixed most of his discography so beautifully he came to me asking for a stem approach."

Some engineers view stem mastering cautiously — it can blur the line between mastering and mixing. The community consensus is that stem mastering works best when the artist explicitly requests it and trusts the mastering engineer's judgment.

### DIY vs Professional Mastering

The community strongly favors hiring a professional mastering engineer for commercial releases, but the reasoning goes beyond "fresh ears in a calibrated room":

> [!quote] Nomograph Mastering (2022-11-29) — 26 reactions
> "The confidence this gives people is part of what we are paid for, but again nothing I'm doing tonight can sell more gear, plug ins or tutorials so we never see it focused on."

> [!quote] Nomograph Mastering (2025-07-03) — 9 reactions
> "They think we sell processing, or our fancy speakers. But we sell the feeling that it's done, or could not be better."

The critique of DIY mastering centers on "Ozone preset jockeys" — engineers using AI mastering assistants without developing critical listening skills. Tools like LANDR and CloudBounce are considered acceptable for demos but not commercial releases.

### Career Guidance for Mastering Engineers

Nomograph Mastering's career advice (40 reactions, pinned) is the channel's most comprehensive guide for aspiring mastering engineers:

> [!quote] Nomograph Mastering (2025-02-03) — 40 reactions, pinned
> "If I was in charge of newcomer's career in Mastering: 1) Focus 100% of early efforts on getting the best speaker/room combo you can muster in place (forget all other gear). 2) Spend as much time as possible listening with the best listeners you can get access to. 3) Ignore almost everything you read and watch on the internet about the topic of Mastering. 4) Ringfence your time developing techniques away from when you are working on music. 5) Maximize your availability to the music. 6) Listen as widely as you can, to every genre. 7) Love everything you touch. You don't have to like it, but you've gotta love it. Love is a quality of attention."

> [!quote] Nomograph Mastering (2025-06-20) — 17 reactions
> "Your clients will be your greatest teachers. I learn more every year than the last, and I'm 31 years into record life and 23 in mastering."

## Practical Application

- Master the material for the material — don't target a specific LUFS number
- Start with the simplest chain possible (EQ + limiter); add processing only when the music demands it
- Set your limiter true peak ceiling to -1.0 dBTP for streaming delivery
- Use volume rides into the limiter for songs with large section-to-section dynamics
- Apply [[Dithering]] as the absolute last step when converting bit depth
- Use mid-side EQ to address stereo balance issues without affecting the center image
- When stem mastering, deliver stems at the same sample rate and bit depth as the session with no processing on the master bus
- Invest in monitoring above all other gear — the room and speakers are more important than any plugin or outboard

## Common Mistakes

- Targeting -14 LUFS rather than mastering appropriately for the genre and material
- Over-compressing at the mastering stage — compression is far less important than beginners expect
- Applying processing to fix mix problems that should be addressed in the mix stage
- Using the same monitoring chain for mixing and mastering without recalibrating
- Sending multiple master versions unprompted — send one confident master
- Asking young artists for technical notes instead of asking how it feels
- Leaving plugins on the mix bus that were intended as "mastering preview"

### Mastering-Adjacent Discussion (from #mixing-talk)

The #mixing-talk channel (706 gain staging/levels messages, 800 mix bus messages) includes significant mastering-adjacent discussion:

- **Loudness targets for mixing:** The debate over how loud to mix before mastering — Nomograph Mastering advocates leaving headroom (-3 to -6 dBTP) for the mastering engineer, while some members mix into a limiter
- **Print chains:** Mix bus processing that serves a mastering-like function — compression, EQ, saturation, and limiting on the mix bus effectively "pre-masters" the mix
- **Metering awareness:** Iwan Morgan's discovery (36 reactions) that changing Pro Tools metering settings fundamentally improved his mixing approach
- **Streaming loudness normalization:** Ongoing debate about targeting -14 LUFS vs mixing louder for platforms that don't normalize

## See Also

- [[Mastering Signal Chain]] — detailed processing chain and converter technology
- [[Loudness Standards and Streaming Delivery]] — platform LUFS targets and normalization behavior
- [[Client Communication in Mastering]] — managing client relationships and revisions
- [[Album Mastering and Sequencing]] — album-specific mastering workflows
- [[LUFS]] — loudness measurement standard
- [[Dithering]] — noise shaping applied during bit depth conversion
- [[Bounce and Export Workflows]] — final delivery formats and export settings
- [[Mixing in the DAW]] — mixing techniques that feed into mastering

## Source Discussions

> [!quote] Discord Source
> **Channel:** #mastering-talk — **Date Range:** 2022-04 to 2026-02
> **Key contributors:** Nomograph Mastering (5,730 msgs), Rollmottle (1,307), masteredbyjack (1,288), Berlin (1,288), cian riordan (470), hebakadry (104)
> **Message volume:** 22,909 raw → 19,806 substantive → 6,466 categorized across 15 categories

> [!quote] Discord Source
> **Channel:** #daw-talk — **Date Range:** 2021-02 to 2026-02
> **Key contributors:** Nomograph Mastering, Iwan Morgan, cian riordan, Rollmottle, Bryan DiMaio
> **Message volume:** 344 categorized messages

> [!quote] Discord Source
> **Channel:** #mixing-talk — **Date Range:** 2021-02 to 2026-02
> **Key contributors:** Nomograph Mastering, Iwan Morgan
> **Message volume:** 706 gain staging/levels messages, 800 mix bus messages
