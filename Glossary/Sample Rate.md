---
type: glossary
confidence: medium
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

## Community Debate: Which Sample Rate?

The #recording-talk channel reveals a pragmatic consensus with some entertaining outliers:

> [!quote] cian riordan (2022-02-09) — 20 reactions
> "I think everyone should come to their own conclusions but in my research, I found that 96 is in fact a higher number than *both* 44 and 48. I'm sure there's more to dig into there, but that's what I've come up with thus far."

> [!quote] cian riordan (2022-07-18)
> "Most sane, reasonable people would say no -- there's no audible difference. But then you have very successful record makers who have un-challenged opinions rooted in magic and mystique who swear that a difference exists. I find it best to make these decisions on program material. If you're doing anything exclusively for CD, there's merit in sticking at 44.1 kHz to save a conversion step -- but 48kHz makes more sense in the modern record making era because streaming services accept it and it's the standard for TV/film."

- **44.1kHz** -- CD standard, avoids sample rate conversion for CD delivery
- **48kHz** -- Video/broadcast standard, Calvin Lauber: "I record at 48 cause it's a little more than 44 and I've never heard a difference between any of it"
- **96kHz** -- Some engineers prefer for headroom during pitch/time manipulation
- **Higher sample rates help with cleaner time and pitch shifting** -- This is the most practical argument for recording above 44.1/48

> [!quote] chadwahlbrink (2022-04-12)
> "'Gang vocals only sound right at 44.1kHz' -- JJP"

Slow Hand noted that despite the humorous sample rate takes, "JJP is a goldmine of insights into production and engineering."

## Related Terms

- [[Bit Depth]]
- [[Buffer Size]]
- [[Latency]]

## See Also

- [[DAW Comparison]]
- [[Bounce and Export Workflows]]

## Source Discussions

> [!quote] Discord Source
> Channel: #recording-talk
> Matches: 53
> Key contributors: cian riordan, Calvin Lauber, chadwahlbrink, Slow Hand, Adam Thein, Nomograph Mastering
