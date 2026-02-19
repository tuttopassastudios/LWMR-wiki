---
type: topic
confidence: high
aliases:
  - Reverb Techniques
  - Delay Techniques
  - Spatial Effects
tags:
  - domain/mixing
  - type/topic
  - channel/mixing-talk
created: 2026-02-18
modified: 2026-02-18
---

# Reverb and Delay Techniques

## Summary

> [!abstract]
> Reverb and delay are the primary spatial tools in mixing, with 1,796 categorized messages in #mixing-talk. The community favors Valhalla plugins (VintageVerb, Room) as the go-to affordable option, with [[Lexicon]] hardware and real plates reserved for high-end work. chrissorem's real plate reverb prompted Michael Brauer to email asking about his settings. Key techniques include send/return architecture, [[Pre-delay]] management, narrowing reverb returns for better imaging, and deliberately overdriving reverb inputs for character.

## Detail

### Reverb Types and Character

**Plate reverb:** The most-discussed reverb type for vocals and instruments. Dense, smooth, and immediately recognizable. chrissorem uses a real plate as his signature sound. Plugin emulations from Soundtoys, Arturia, and UAD are common alternatives.

**Hall reverb:** Used for orchestral, ambient, and dramatic spatial effects. Longer decay times (2-5 seconds) create a sense of large space. Members use halls sparingly on pop/rock to avoid washing out the mix.

**Room reverb:** Shorter, more natural-sounding reverb for adding subtle dimension. Valhalla Room is frequently recommended. Room reverbs help sources feel "in a space" without drawing attention to the effect.

**Spring reverb:** Characterful, lo-fi reverb associated with guitar amps and vintage recordings. Used as an effect rather than a spatial tool.

### Pre-delay and Decay

[[Pre-delay]] — the gap between the dry signal and the onset of reverb — is one of the most discussed parameters. Community insights:

- Pre-delay separates the source from the reverb, maintaining clarity and intelligibility
- Longer pre-delay (50-100ms) keeps vocals upfront while still adding depth
- Shorter pre-delay (0-20ms) creates a more intimate, blended sound
- Decay time should match the tempo — shorter for fast songs, longer for ballads
- "Tune" the decay so the reverb tail fades before the next phrase begins

### Send/Return Architecture

The community strongly favors send/return (aux send) architecture over inserting reverbs directly on tracks:

- Multiple sources can share a single reverb, creating cohesive spatial context
- Send levels provide independent control of each source's reverb amount
- EQ and compression can be applied to the reverb return independently
- Multiple reverb sends (short room, medium plate, long hall) create depth layers

### Delay Techniques

**Slapback delay:** Short delay (50-120ms) with a single repeat. Used on vocals and guitars for a rockabilly or vintage pop feel. Adds presence without obvious "echo" effect.

**Timed delays:** Delays synced to tempo (quarter note, eighth note, dotted eighth) create rhythmic interest. The community discusses [[Soundtoys]] EchoBoy as the most versatile delay plugin.

**Ping-pong delay:** Alternating left/right delays for stereo movement. Used sparingly to avoid cluttering the mix.

**Throw delays:** Automated delay sends on specific words or phrases in vocals. A key mix move for adding drama and interest to vocal performances.

### Width and Imaging

Slow Hand's insight on reverb width is one of the channel's most-cited spatial mixing tips:

> [!quote] Source
> **Author:** Slow Hand — **Date:** 2023-03-04 — **Channel:** #mixing-talk
> "It's one of those paradoxical mix realizations: That the key to a wide mix is not by widening every instrument, but by using mostly mono elements and panning them dramatically in the stereo field so that they occupy distinct positions in the mix."

> [!quote] Source
> **Author:** Slow Hand — **Date:** 2023-01-17 — **Channel:** #mixing-talk
> "A recent lesson that I've had to remind myself about was the importance of narrowing my long reverbs. Recently I've had a bad habit of keeping them full-width. I've found that it really helps my sound stage to narrow them."

### Overdriving Reverb Inputs

Slow Hand discovered that deliberately overdriving Valhalla VintageVerb's input stage creates interesting saturation and character — an unconventional but effective technique for adding grit to reverb tails.

> [!quote] Source
> **Author:** chrissorem — **Date:** 2024-08-20 — **Channel:** #mixing-talk
> "I got email from michael brauer last week asking about what plugin setting I'm using for verb. I had to drop the sad news that it's a special real plate. I do love Valhalla though."

## Practical Application

- Set up 3-4 reverb sends: short room, medium plate, long hall, and an effects reverb
- Use pre-delay on vocal reverbs (40-80ms) to maintain clarity
- Narrow long reverb returns to prevent them from filling the entire stereo field
- EQ reverb returns — high-pass at 200-400Hz, low-pass at 8-12kHz to prevent muddiness and harshness
- Automate delay sends for "throw" effects on specific vocal phrases

## Common Mistakes

- Using full-width reverbs on everything, creating a washed-out stereo field
- Not EQing reverb returns — muddy low end and harsh high frequencies in the reverb tail
- Using too much reverb to mask problems that should be fixed with EQ or arrangement
- Ignoring pre-delay and losing source clarity in the reverb wash
- Inserting reverbs directly on tracks instead of using send/return architecture

## See Also

- [[Pre-delay]] — reverb pre-delay concept
- [[Lexicon]] — legendary reverb algorithms
- [[Soundtoys]] — EchoBoy delay and effects
- [[Vocal Mixing]] — vocal reverb and delay context
- [[Mix Bus Processing]] — reverb in the mix bus context

## Source Discussions

> [!quote] Discord Source
> **Channel:** #mixing-talk — **Date Range:** 2021-08 to 2026-02
> **Key contributors:** chrissorem, Slow Hand, BatMeckley, cian riordan, NoahNeedleman
> **Message volume:** 1,796 categorized messages
