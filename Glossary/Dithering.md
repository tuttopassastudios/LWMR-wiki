---
type: glossary
confidence: low
aliases:
  - Dither
tags:
  - type/glossary
created: 2026-02-17
modified: 2026-02-18
---

# Dithering

## Definition

The process of adding very low-level noise when reducing [[Bit Depth]] to preserve sonic detail that would otherwise be lost to quantization distortion. Most commonly applied when converting from 24-bit to 16-bit for final distribution.

## Context

Dithering should be applied as the very last step in the signal chain, after all other processing is complete. It is only necessary when reducing bit depth — not when staying at the same bit depth or increasing it. Common dither types include TPDF (triangular probability density function) and various noise-shaped algorithms offered by plugins such as those from iZotope and Waves.

## Related Terms

- [[Bit Depth]]
- [[Gain Staging]]
- [[Offline Bounce]]

## See Also

- [[Bounce and Export Workflows]]

## Source Discussions

> [!quote] Discord Source
> Channel: #🧠nerd-talk
> Messages: ~7 (dither theory, noise shaping, noise floor, signal-to-noise ratio)
> Key contributors: Nomograph Mastering, Gerhard Westphalen
> Date range: January 2024 – February 2026
> See also: [[nerd-talk Channel Summary]]
