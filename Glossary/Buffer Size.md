---
type: glossary
confidence: low
aliases:
  - Buffer
  - Audio Buffer
tags:
  - type/glossary
created: 2026-02-17
modified: 2026-02-17
---

# Buffer Size

## Definition

The number of audio samples processed at once by the audio interface before being sent to or from the computer. Lower values reduce [[Latency]] but increase CPU strain. Common values are 64, 128, 256, 512, and 1024 samples.

## Context

Buffer size is one of the primary controls for managing the tradeoff between latency and system stability. During recording, lower buffer sizes (64-128) are preferred to minimize performer delay. During mixing, higher buffer sizes (512-1024) are used to allow more plugin processing without audio dropouts.

## Related Terms

- [[Latency]]
- [[Sample Rate]]
- [[CPU Optimization for Audio]]

## See Also

- [[DAW Comparison]]
- [[Troubleshooting DAW Issues]]

## Beginner Context (from #newbie-questions)

"Why am I getting crackles?" is one of the most common troubleshooting questions from beginners. The answer is almost always buffer size: increase to 512 or 1024 samples during mixing, use 64-128 only when tracking with software monitoring. See [[Beginner FAQ#Troubleshooting]].
