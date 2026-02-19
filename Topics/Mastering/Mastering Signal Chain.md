---
type: topic
confidence: high
aliases:
  - Mastering Chain
  - Mastering Processing Chain
tags:
  - type/topic
  - domain/mastering
  - channel/mastering-talk
created: 2026-02-18
modified: 2026-02-18
---

# Mastering Signal Chain

## Summary

> [!abstract]
> The mastering signal chain is the ordered sequence of processing applied to a mix to prepare it for distribution. While conventional wisdom prescribes a rigid order (EQ → compression → saturation → stereo → limiting → dither), working mastering engineers in this community emphasize that the chain should serve the music rather than follow rules. Mastering EQ and limiting dominate real-world chains, while compression plays a much smaller role than internet discourse suggests.

## Detail

### Typical Chain Order

A standard mastering chain follows this general structure:

1. **Corrective EQ** — addressing tonal imbalances, removing problem frequencies
2. **Compression / dynamics** — gentle glue, multiband if needed (used far less than beginners expect)
3. **Saturation / harmonic enhancement** — adding warmth, density, or excitement
4. **Stereo imaging** — M/S adjustments, width control
5. **Final limiter / clipper** — loudness maximization with ceiling control
6. **Dithering** — noise shaping when converting bit depth (absolute last step)

However, the #mastering-talk community repeatedly emphasizes that real-world chains are often simpler.

> [!quote] masteredbyjack (2023-02-27) — 9 reactions
> "Just for reference, the convo was to restrict my approach to one band of EQ, Q of no sharper than .7 and maybe a low shelf. That's it. And a limiter. Since then I've done at least over 100 songs, many of which I thought were my best work."

### Mastering EQ Philosophy

EQ is the primary tool in mastering, but the approach differs fundamentally from mixing EQ.

> [!quote] Nomograph Mastering (2024-05-24) — 29 reactions
> "TLDR — if there's too much of any band between 1500 and 6000 you won't be able to perceive the rest of the frequency range correctly — it 'blinds' us."

> [!quote] Nomograph Mastering (2024-05-24) — 24 reactions
> "Even with very amateur mixes I'm often leaving sub 150 Hz relatively untouched and biasing perception using the mid range."

Key principles from working mastering engineers:

- **Broad strokes over surgical cuts** — mastering EQ should use gentle slopes and wide Qs
- **Tilt EQ and shelving** dominate over parametric moves
- **Mid-side EQ** allows treating the center and sides independently — Rollmottle described flipping the Porter Grinder into M/S to "bring the vocal closer into the center (by cutting!) and push the atmospherics to the sides (by boosting)"
- **Linear phase EQ is controversial** — Nomograph Mastering (14 reactions, tongue-in-cheek): "In this house we believe linear phase EQ is a war crime"

> [!quote] Nomograph Mastering (2025-05-18) — 20 reactions
> "As Dave Collins always says: 'the lost art of EQ in Mastering.'"

### The Role of Compression

One of the most surprising findings from #mastering-talk is how little emphasis working mastering engineers place on compression compared to online discourse.

> [!quote] Nomograph Mastering (2023-01-15) — 5 reactions
> "If I was teaching someone modern mastering, compression would be way way down the list of priorities."

When compression is used, it tends to be gentle bus-style glue (vari-mu or opto topology) rather than aggressive dynamics shaping. Multiband compression is viewed with particular skepticism:

> [!quote] Nomograph Mastering (2022-11-14) — 4 reactions
> "When I see dudes rocking multiband dynamics in MS I'm not onboard."

### Limiting and Clipping

The limiter is the most discussed processing tool in the channel (1,213 messages). Key concepts:

- **Clipping before limiting** — many engineers use a clipper (Boz Big Clipper, StandardClip) to handle transient peaks before the limiter, reducing limiter workload
- **Volume rides into the limiter** — a technique championed by Nomograph Mastering for managing sections with wildly different energy levels
- **Multi-stage limiting** — using gentle amounts across multiple stages rather than one heavy limiter
- **IRC modes** — iZotope Ozone's IRC (Intelligent Release Control) modes are widely discussed, with different modes suited to different material

> [!quote] Nomograph Mastering (2025-06-29) — 17 reactions
> "An easy and often overlooked solution is just to do a volume ride *into* the limiter. It's diving for huge gain reduction and you can make its work easier by just carefully shaving off a few dB on the choruses."

### Converter Headroom and Hardware

The channel contains deep technical discussion about converter specifications, particularly the headroom above digital full-scale:

- **AKM converter chips** — have approximately +2.5 dB of headroom above full-scale before analog clipping
- **ESS converter chips** — have significantly less headroom
- **RME converters** — documentation explains this concept in detail
- **Voltage rails** — the analog output stage determines how much level above 0 dBFS the converter can reproduce before distortion

This knowledge is relevant to understanding [[Intersample Peak|intersample peaks]] — when inter-sample reconstruction exceeds 0 dBFS, the converter's analog headroom determines whether this causes audible distortion.

### ITB vs Hardware Mastering

> [!quote] Nomograph Mastering (2023-01-16) — 8 reactions
> "If you are feeling ITB then trust that. There is no rule that outboard is better (despite what people say on Gearslutz)."

The consensus is that ITB mastering is entirely legitimate, with several engineers noting that analog hardware primarily offers speed advantages (faster to dial in certain EQ moves on hardware) rather than inherent quality advantages.

Rollmottle's detailed workflow post (16 reactions) described an analog pass through a Gyraf and Porter Grinder, noting it was chosen for speed rather than superiority: "Since time was of the essence here, that was the move."

## Practical Application

- Start with the simplest chain possible — many professional masters use only EQ and a limiter
- Use broad EQ moves; if you need surgical cuts, the mix likely needs revision
- Consider a clipper before the limiter to handle transient peaks
- Use volume rides into the limiter for songs with large dynamic variation between sections
- Test in both M/S and stereo to determine which reveals the issue more clearly
- [[Dithering|Dither]] as the absolute last step when converting bit depth

## See Also

- [[Mastering Workflows]] — complete mastering workflow and philosophy
- [[Loudness Standards and Streaming Delivery]] — loudness targets and platform behavior
- [[Compression Techniques]] — compressor topology overview
- [[Mix Bus Processing]] — mix bus chains that feed into mastering
- [[AD-DA Conversion]] — converter technology

## Source Discussions

> [!quote] Discord Source
> **Channel:** #mastering-talk — **Date Range:** 2022-04 to 2026-02
> **Key contributors:** Nomograph Mastering, Rollmottle, masteredbyjack, ALXCPH, spectrummasters
> **Message volume:** 1,213 limiting/clipping, 1,346 mastering tools, 149 mastering EQ, 178 converters/hardware
