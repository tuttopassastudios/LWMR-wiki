---
type: topic
confidence: medium
aliases:
  - Audio Repair
  - iZotope RX
  - Noise Reduction
tags:
  - domain/mixing
  - type/topic
created: 2026-02-17
modified: 2026-02-17
---

# Audio Repair and Restoration

## Summary
> [!abstract]
> Audio repair and restoration covers the tools and techniques used to fix damaged, noisy, or otherwise problematic recordings. [[iZotope RX]] is the overwhelmingly dominant tool in this space, offering spectral editing, de-noise, de-hum, de-click, de-clip, and dialog isolation. ARA integration has made these workflows faster by embedding RX directly into DAW timelines.

## Detail

### iZotope RX Workflows
[[iZotope RX]] is regarded as the industry standard for audio repair across music, post-production, and podcast workflows. The software provides a standalone editor and a suite of plugins that handle everything from subtle noise floor reduction to rescuing badly damaged recordings. Most professionals configure their DAW's external sample editor to open RX directly, enabling a seamless round-trip editing workflow.

> [!quote] Source
> **Author:** Adam Thein — **Date:** 2024-01-18 — **Channel:** #daw-talk
> "One tip is setting up the Sample Editor in your settings to open up to another audio program. I have mine setup with Izotope RX, but you can also set it up to go to Melodyne Standalone if you are doing a lot of vocal work..."

### Spectral Editing
Spectral editing allows surgical removal of unwanted sounds by visualizing audio as a frequency-over-time spectrogram. Users can paint selections around specific artifacts — a chair squeak, a cough, electrical interference — and remove them without affecting surrounding audio. This approach is far more precise than traditional time-domain editing.

### Noise Reduction Techniques
Common repair modules include:
- **De-noise** — learns a noise profile and subtracts it from the signal
- **De-hum** — removes electrical hum at 50/60 Hz and harmonics
- **De-click** — eliminates pops, clicks, and digital glitches
- **De-clip** — reconstructs clipped waveform peaks
- **De-reverb** — reduces room reflections after the fact

### ARA Integration
[[ARA]] (Audio Random Access) allows RX to run directly within a DAW timeline without bouncing or round-tripping files. This is supported in [[Pro Tools]], [[Logic Pro]], [[Cubase]], and [[Studio One]], drastically speeding up repair workflows on large sessions.

### Long-Form Audio Analysis
For podcasts, meditations, and other long-form content, visualizing entire files for loudness and clipping analysis is a common need.

> [!quote] Source
> **Author:** Garth Tim — **Date:** 2023-09-25 — **Channel:** #daw-talk
> "Looking for something that can visualize an entire file and give detailed readouts on loudness/peak/clipping at various points along the waveform. For context, this is for very long files (podcasts/meditations)..."

## Practical Application
- Set up your DAW's external editor to open [[iZotope RX]] for quick round-trip repairs
- Use spectral editing for surgical removal of unwanted sounds rather than cutting entire regions
- Learn the noise profile of a room before applying De-noise to avoid artifacts
- Use [[ARA]] integration when available to avoid file export/import round-trips
- Batch process files with similar noise issues using RX's batch processor

## Common Mistakes
- Applying too aggressive noise reduction, creating hollow or "underwater" artifacts
- Not learning a proper noise profile before de-noising (using default settings blindly)
- Forgetting to set up the external editor path in DAW preferences
- Using De-reverb too heavily, which can destroy natural room tone
- Not saving a backup of the original file before destructive spectral edits

## See Also
- [[Editing Techniques Across DAWs]] — general editing workflows
- [[Vocal Editing Across DAWs]] — vocal-specific repair and processing
- [[iZotope RX]] — the industry standard repair tool
- [[ARA]] — Audio Random Access integration protocol

## Source Discussions

> [!quote] Discord Source
> **Channel:** #daw-talk — **Date Range:** 2021-02 to 2026-02
> **Key contributors:** Rollmottle, Nomograph Mastering, Adam Thein, Slow Hand, h3x
> **Message volume:** 207 categorized messages
