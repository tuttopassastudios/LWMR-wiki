---
type: glossary
confidence: medium
aliases:
  - Word Length
tags:
  - type/glossary
created: 2026-02-17
modified: 2026-02-17
---

# Bit Depth

## Definition

The number of bits used to represent each audio sample in a digital audio system. 16-bit is the CD standard, 24-bit is the professional recording and mixing standard, and 32-bit float is used for internal DAW processing. Bit depth determines the theoretical dynamic range of the audio signal.

## Context

Each additional bit of depth adds approximately 6dB of dynamic range. 16-bit audio provides ~96dB of dynamic range, while 24-bit provides ~144dB. Recording at 24-bit is standard practice as it provides ample headroom and low noise floor. When delivering final masters at 16-bit (for CD or certain streaming formats), [[Dithering]] should be applied to preserve detail.

## Community Perspective

> [!quote] cian riordan (2022-06-30)
> "You shouldn't [record at 32-bit float from a 24-bit interface]. 24 bits is an insane amount of head room to begin with."

Adam Thein clarified: "If you are tracking 32-bit float from an interface that only captures 24 bit you are basically wasting hard drive space. Unless you have specifically purchased a 32-bit depth recording device or interface then use 24."

The community consensus is clear: **24-bit is the professional standard for recording**. 32-bit float is valuable for internal DAW processing but provides no benefit at the capture stage with standard converters.

## Related Terms

- [[Sample Rate]]
- [[Dithering]]
- [[Gain Staging]]

## See Also

- [[Bounce and Export Workflows]]

## Source Discussions

> [!quote] Discord Source
> Channel: #recording-talk
> Matches: 53 (shared with Sample Rate discussions)
> Key contributors: cian riordan, Adam Thein
