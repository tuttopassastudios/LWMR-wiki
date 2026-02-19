---
type: glossary
confidence: medium
aliases:
  - ISP
  - Inter-Sample Peak
  - True Peak
tags:
  - type/glossary
  - domain/mastering
  - channel/mastering-talk
created: 2026-02-18
modified: 2026-02-18
---

# Intersample Peak

## Definition

An intersample peak (ISP) occurs when the reconstructed analog waveform between two digital samples exceeds the level of either individual sample, potentially surpassing 0 dBFS. This happens because digital-to-analog conversion reconstructs a continuous waveform from discrete samples, and the peak of that continuous waveform may be higher than any measured sample value.

## Context

Intersample peaks are a critical concern in mastering because they can cause audible distortion during:

- **Lossy codec conversion** (AAC, MP3, Ogg Vorbis) — streaming platforms re-encode masters, and ISPs can clip during this process
- **D/A conversion** — the converter's analog headroom determines whether ISPs cause audible distortion; AKM converter chips have approximately +2.5 dB of headroom above full-scale, while ESS chips have significantly less

The standard mitigation is **true peak limiting** — setting the limiter ceiling to -1.0 dBTP (decibels True Peak) or lower. True peak metering oversamples the signal to detect peaks between samples, unlike standard sample peak metering which only measures the actual sample values.

> [!quote] Rollmottle (2022-05-13) — #mastering-talk — 8 reactions
> "Theoretically the lower the ceiling, the less risk there is of intersample peaks happening upon conversion to MP3 or some other format streamers use."

## Related Terms

- [[LUFS]]
- [[Mastering Signal Chain]]
- [[Loudness Standards and Streaming Delivery]]
- [[AD-DA Conversion]]
