---
type: topic
confidence: high
aliases:
  - Loudness Standards
  - Streaming Loudness
  - LUFS Targets
tags:
  - type/topic
  - domain/mastering
  - channel/mastering-talk
created: 2026-02-18
modified: 2026-02-18
---

# Loudness Standards and Streaming Delivery

## Summary

> [!abstract]
> Loudness standards for streaming are one of the most hotly debated topics in modern mastering. While platforms like Spotify normalize to approximately -14 LUFS, the community of working mastering engineers strongly cautions against targeting a specific LUFS number. The consensus from professional mastering engineers is to master the material for the material — letting the genre, energy, and artistic intent dictate loudness rather than platform specifications.

## Detail

### Platform Normalization Targets

Streaming platforms normalize playback levels to reduce jarring volume differences between tracks. The commonly cited targets are:

| Platform | Normalization Target | Notes |
|----------|---------------------|-------|
| Spotify | ~-14 LUFS | Only when user has normalization enabled |
| Apple Music | ~-16 LUFS | Sound Check must be enabled by user |
| YouTube | ~-14 LUFS | Applied automatically |
| Tidal | ~-14 LUFS | User-configurable |
| Bandcamp | None | No normalization applied |

However, the real-world picture is far more complex than these numbers suggest.

### The -14 LUFS Myth

Working mastering engineers in the community are nearly unanimous in their criticism of targeting -14 LUFS as a mastering goal. This is one of the strongest consensus positions across 22,909 messages of #mastering-talk discussion.

> [!quote] Nomograph Mastering (2023-01-26) — pinned
> "The dedication with which a Mastering Engineer advocates -14 is inversely proportional to the amount of records they've done that you've heard of."

> [!quote] Rollmottle (2023-01-26) — 22 reactions, pinned
> "Every streaming service has a different number at which they will do normalization. The immediate problems: 1) Every service works differently — one cannot confidently shoot at a target that doesn't really exist. 2) Not every user has normalization turned on. 3) Not everybody consumes through streaming. 4) Lots of modern music benefits sonically from being pushed into a limiter. So, just master the material for the material."

> [!quote] Nomograph Mastering (2023-01-26) — 14 reactions
> "It has become fashionable to post online about targeting -14 LUFS or so, but in my opinion, if you care about sounding approximately as loud as other artists, and until loudness normalization improves and becomes universally implemented, that is mostly well-meaning internet chatter, not good practical advice. My advice is to make one digital master that sounds good, is not overly crushed for loudness, and use it for everything."

### Where Normalization Doesn't Apply

A critical finding from #mastering-talk is the significant number of playback scenarios where loudness normalization is not applied:

- **Spotify on smart TV** — no normalization
- **Spotify web browser** — no normalization
- **External/Bluetooth speakers** — normalization behavior varies
- **Sonos and similar systems** — normalization not reliably applied
- **Bandcamp** — no normalization at all
- **Users who disable normalization** — a significant portion of listeners

> [!quote] Nomograph Mastering (2022-11-16) — 10 reactions
> "Not everyone has level norm on. Spotify on smart TV does not have level norm. Spotify on web browser does not have loudness norm. Spotify and other DSPs can and will change the targets so you CANNOT depend on them."

### The Only Real Loudness Regulation

The only context where loudness has enforceable consequences is broadcast advertising:

- **North America:** Cannot exceed -24 LUFS
- **Europe:** Cannot exceed -23 LUFS

For music streaming, normalization is a suggestion — not a hard standard.

### Loudness Is Built in the Mix

A recurring principle is that perceived loudness is primarily determined long before the mastering stage.

> [!quote] Nomograph Mastering (2025-06-11) — 11 reactions
> "Perceived loudness is almost all determined by the arrangement. Mixing can enhance it some. Mastering can enhance it less. What we typically want is maximum perceived loudness and minimum measured loudness relative to that."

> [!quote] Nomograph Mastering (2023-10-07) — 17 reactions
> "If you want a -7 LUFS master then you need to build a -7 LUFS mix, otherwise things will change too much when the level is pushed."

### Output Ceiling Debate

The true peak ceiling setting is another contested topic:

- **-1.0 dBTP:** Standard recommendation for streaming delivery; prevents [[Intersample Peak|intersample peak]] clipping during codec conversion
- **-0.3 dBTP:** Some engineers prefer this as less conservative
- **-2.0 dBTP:** Nomograph Mastering (tongue-in-cheek, 35 reactions): "I think all other mastering engineers should follow the -2dB peak standard" — partly a joke about competitive loudness, but also reflects the reality that more headroom reduces codec artifacts

> [!quote] Rollmottle (2022-05-13) — 8 reactions
> "Nah, fuck -1 or -2. Theoretically the lower the ceiling, the less risk there is of intersample peaks happening upon conversion to MP3 or some other lossless format streamers use."

### Codec Considerations

Masters are encoded into lossy formats (AAC, MP3, Ogg Vorbis) by streaming platforms. This encoding can introduce:

- **Intersample peaks** that exceed the original ceiling
- **Pre-echo artifacts** on transient-heavy material
- **Subtle changes to stereo imaging**
- **Transition artifacts** between songs on albums

> [!quote] Nomograph Mastering (2024-05-31) — 12 reactions
> "Now convert to the following and what do we see/hear happen with our beautiful transition: MP3 (Fraunhofer and Lame codecs), OGG Vorbis, AAC/M4a, ALAC (Apple Lossless), FLAC"

This is why true peak limiting (rather than sample peak limiting) is standard practice — it accounts for inter-sample reconstruction that may exceed the measured peak.

## Practical Application

- Master the material for the material — don't target a specific LUFS number
- Use genre-appropriate references to calibrate loudness expectations
- Set true peak ceiling to -1.0 dBTP minimum for streaming delivery
- Test your masters through codec conversion (AAC, MP3) to check for artifacts
- If a mix needs to be loud, build the loudness into the mix and arrangement rather than pushing the limiter harder

## See Also

- [[LUFS]] — loudness measurement standard
- [[Mastering Signal Chain]] — mastering chain order and processing
- [[Mastering Workflows]] — complete mastering workflow guidance
- [[Intersample Peak]] — inter-sample peak clipping
- [[Loudness Normalization]] — platform normalization behavior

## Source Discussions

> [!quote] Discord Source
> **Channel:** #mastering-talk — **Date Range:** 2022-04 to 2026-02
> **Key contributors:** Nomograph Mastering, Rollmottle, masteredbyjack, Nomograph Mastering, hebakadry
> **Message volume:** 419 loudness/LUFS messages, 506 streaming/delivery messages, 1,213 limiting/clipping messages
