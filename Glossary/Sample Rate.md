---
type: glossary
confidence: low
aliases:
  - Sampling Rate
  - Sample Frequency
tags:
  - type/glossary
created: 2026-02-17
modified: 2026-02-17
---

# Sample Rate

## Definition

The number of audio samples captured per second in a digital audio system. Common rates include 44.1kHz (CD standard), 48kHz (video/broadcast standard), and 96kHz (high-resolution audio). Higher sample rates increase file size and CPU usage proportionally.

## Context

The choice of sample rate affects file size, CPU overhead, and [[Latency]]. The Nyquist theorem dictates that a sample rate captures frequencies up to half its value (e.g., 44.1kHz captures up to ~22kHz). Recording at higher sample rates is debated in the community — some engineers prefer 48kHz or 96kHz for headroom during processing, while others maintain that 44.1kHz is sufficient for most purposes.

## Related Terms

- [[Bit Depth]]
- [[Buffer Size]]
- [[Latency]]

## See Also

- [[DAW Comparison]]
- [[Bounce and Export Workflows]]
