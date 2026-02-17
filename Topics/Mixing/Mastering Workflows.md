---
type: topic
confidence: medium
aliases:
  - Mastering
  - Audio Mastering
  - Mastering Chain
tags:
  - domain/mixing
  - type/topic
created: 2026-02-17
modified: 2026-02-17
---

# Mastering Workflows

## Summary
> [!abstract]
> Mastering is the final stage of audio production where a stereo mix (or stems) is processed to achieve competitive loudness, tonal balance, and format-readiness for distribution. This page covers mastering chain signal flow, loudness standards for streaming platforms, limiter strategies, stem mastering, and the decision between DIY mastering and hiring a professional.

## Detail

### Mastering Chain Basics
A typical mastering chain follows a general order: corrective EQ, compression or multiband dynamics, saturation or harmonic enhancement, stereo imaging, a final limiter, and dithering. The goal is to polish the mix without fundamentally altering it. Many engineers use [[Plugin Ecosystem Overview|plugin suites]] like iZotope Ozone or FabFilter's mastering bundle to handle multiple stages within a single interface. Mid-side processing is commonly applied at the EQ and compression stages to treat the center and sides of the stereo image independently, allowing engineers to tighten low-end in the center while adding width to higher frequencies.

### Loudness Standards (LUFS)
Streaming platforms normalize audio to specific [[LUFS]] targets — Spotify normalizes to approximately -14 LUFS, Apple Music to around -16 LUFS (with Sound Check enabled), and YouTube to roughly -14 LUFS. Mastering louder than the platform target results in the track being turned down, which can reduce dynamic range without any loudness benefit. Engineers increasingly target -12 to -14 LUFS integrated for modern pop and electronic genres, while more dynamic genres like jazz or classical may sit at -16 to -20 LUFS. True peak limiting (setting the ceiling to -1.0 dBTP or lower) prevents inter-sample clipping during lossy codec conversion (AAC, MP3, Ogg Vorbis).

### Limiter Strategies
The final limiter is arguably the most critical processor in the mastering chain. Popular choices include FabFilter Pro-L 2, Sonnox Oxford Limiter, and iZotope Ozone's Maximizer. Key considerations include the limiter algorithm (transparent vs. colored), attack and release behavior, and ceiling settings. Setting the true peak ceiling to -1.0 dBTP is standard practice for streaming delivery. Many engineers use multiple stages of gentle limiting rather than a single heavy limiter to achieve loudness more transparently.

### Stem Mastering
Stem mastering involves receiving grouped submixes (typically drums, bass, vocals, instruments) rather than a single stereo mix. This gives the mastering engineer more control over balance and problem-solving without requiring a full remix. Stem mastering is increasingly common for Dolby Atmos deliverables, where separate elements need to be positioned in the immersive sound field. Standard stem counts range from 4 to 8 stems, though [[Spatial Audio and Dolby Atmos]] workflows may require more granular separation.

### DIY vs Professional Mastering
The community is divided on when to master your own work versus hiring a professional. The consensus leans toward hiring a mastering engineer for commercially released material, as a fresh set of ears in a calibrated room catches issues the mixing engineer may have become deaf to. DIY mastering is considered acceptable for demos, references, and independent releases where budget is limited. Tools like LANDR and CloudBounce offer AI-driven mastering, though community sentiment generally favors human mastering engineers for critical releases.

> [!quote] Source
> **Author:** masteredbyjack — **Date:** 2025-11-03 — **Channel:** #daw-talk
> "Mixers would be better to chime in on specifics -- but I'd throw my weight behind at least being operational in all of them. But probably have one that is the go-to that you understand very deeply."

## Practical Application
- Set your limiter true peak ceiling to -1.0 dBTP for streaming delivery
- Target -14 LUFS integrated as a starting point for most modern genres
- Apply [[Dithering]] as the absolute last step when converting from higher bit depths to 16-bit for CD or distribution
- Use mid-side EQ to address stereo balance issues without affecting the center image
- When stem mastering, deliver stems at the same sample rate and bit depth as the session with no processing on the master bus

## Common Mistakes
- Mastering louder than streaming normalization targets, resulting in unnecessary dynamic range loss
- Forgetting to dither when converting bit depth (e.g., 24-bit to 16-bit)
- Applying processing to fix mix problems that should be addressed in the mix stage
- Using the same monitoring chain for mixing and mastering without recalibrating or changing rooms
- Leaving plugins on the mix bus that were intended as "mastering preview" — these should be removed or communicated to the mastering engineer

## See Also
- [[Mixing in the DAW]] — mixing techniques and strategies across DAWs
- [[LUFS]] — loudness measurement standard for streaming
- [[Dithering]] — noise shaping applied during bit depth conversion
- [[Bounce and Export Workflows]] — final delivery formats and export settings

## Source Discussions

> [!quote] Discord Source
> **Channel:** #daw-talk — **Date Range:** 2021-02 to 2026-02
> **Key contributors:** Nomograph Mastering, Iwan Morgan, cian riordan, Rollmottle, Bryan DiMaio
> **Message volume:** 344 categorized messages
