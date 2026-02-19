---
type: topic
confidence: high
aliases:
  - Vocal Processing
  - Vocal Chain Mixing
  - Vocal Mix Techniques
tags:
  - domain/mixing
  - type/topic
  - channel/mixing-talk
created: 2026-02-18
modified: 2026-02-18
---

# Vocal Mixing

## Summary

> [!abstract]
> Vocal mixing is the single largest topic category in #mixing-talk with 2,741 categorized messages. The channel covers every aspect of vocal processing — EQ, compression, de-essing, reverb/delay, pitch correction, doubles/ad-libs, vocal bus processing, and genre-specific approaches. A defining thread is oaklandmatt's observation that modern vocals are becoming "heavily processed in the same way," sparking debate about dynamics, character, and the over-use of processing chains. The community emphasizes that great vocal mixing starts with great tracking and performance.

## Detail

### Vocal EQ

Community EQ approaches for vocals:

- **High-pass filter at 80-120Hz** to remove rumble without thinning the vocal
- **Cut around 200-400Hz** to reduce mud and boxiness — but not so much that the vocal loses body
- **Boost around 2-5kHz** for presence and intelligibility
- **Air boost at 10-12kHz** with a shelf for sheen and openness
- **Use [[FabFilter]] Pro-Q3 spectrum analyzer** to compare vocal EQ against a reference

> [!quote] Source
> **Author:** cian riordan — **Date:** 2023-08-29 — **Channel:** #mixing-talk
> "Prefacing this unsolicited tip with 'always use your ears, not your eyes, yadda yadda' -- but a few months ago I set my Pro-Q3 default to have the Lead Vocal bus in my template as the external spectrum analyzer sidechain source."

### Vocal Compression

The community's vocal compression approach varies by genre and desired sound:

- **Opto compression ([[Teletronix LA-2A]]):** The go-to for smooth, transparent vocal compression. 3-5 dB of gain reduction in Limit mode
- **FET compression ([[UREI 1176]]):** 4:1 ratio for more aggressive, present vocals. Fast attack catches consonants
- **Serial compression:** Multiple compressors doing 2-3 dB each is preferred over one compressor doing 6+ dB
- **Clip gain first:** Felix Byrne's pinned advice — use clip gain to even out dramatic volume jumps before any compression

> [!quote] Source
> **Author:** oaklandmatt — **Date:** 2023-12-17 — **Channel:** #mixing-talk
> "imho, a lot of the vocals I'm hearing from younger record makers are sounding heavily processed in the same way. 'Lack of dynamics' doesn't really explain it because people think of dynamics as dynamics in the compressor sense."

### De-essing

[[De-esser]] placement and technique is extensively discussed:

- Place the de-esser **after compression** — compression can exaggerate sibilance
- Multiple gentle de-essers are preferred over one aggressive instance
- Split-band mode is generally preferred for transparency
- Manual de-essing (clip gain on individual sibilants) produces the most natural results but takes the most time
- FabFilter Pro-DS, Waves DeEsser, and stock DAW de-essers all get recommendations

### Vocal Effects Chain

A typical community-recommended vocal chain order:

1. **Clip gain** for level consistency
2. **EQ** (subtractive — remove problems)
3. **Compression** (1-2 stages, gentle)
4. **De-esser**
5. **EQ** (additive — add character)
6. **Saturation** (subtle warmth)
7. **Sends:** reverb, delay, effects

### Doubles and Ad-libs

- Doubles should be **tucked under** the lead vocal, not competing for attention
- Pan doubles hard left/right for width, or slightly off-center for subtlety
- Compress doubles harder than the lead — they should be consistent and "pad-like"
- Ad-libs often get more aggressive effects processing (more delay, distortion, filtering)
- Background vocals (BGVs) benefit from bus processing — shared reverb and compression for cohesion

### Vocal Bus Processing

Many members route all vocals (lead, doubles, BGVs, ad-libs) to a vocal bus for group processing:

- Light bus compression (2-3 dB) for cohesion
- Bus EQ for overall tonal shaping
- Shared reverb sends from the bus
- cian riordan advocates for getting the vocal bus right before fine-tuning individual tracks

### Pitch Correction

- [[Melodyne]] is the community standard for transparent pitch correction
- Jeremy Klein's pinned trick: record-enable to transfer vocals into Melodyne without waiting for playback
- Auto-Tune is used deliberately as an effect rather than corrective tool
- The community emphasizes that pitch correction cannot fix a bad performance — it's polish, not repair

## Practical Application

- Start with clip gain to even out the performance before touching any plugins
- Use serial compression (2 compressors doing light work) rather than one compressor working hard
- Place de-esser after compression, or use multiple gentle instances
- Set up a vocal bus and get the group sound right before individual vocal processing
- Automate vocal levels through the mix — this is where "mix moves" matter most

## Common Mistakes

- Over-processing vocals with too many plugins, creating a lifeless, hyper-compressed sound
- Not using clip gain before compression, forcing compressors to handle extreme dynamics
- De-essing before compression, then getting sibilance exaggerated by the compressor
- Treating doubles/BGVs the same as the lead vocal — they need different processing
- Using pitch correction as a crutch for poor tracking rather than re-recording

### Vocal Production Perspective (from #production-talk)

#production-talk adds 812 messages of vocal production discussion focused on the **creative/production side** rather than mixing:

> [!quote] Source
> **Author:** BatMeckley — **Date:** 2023-02-19 — **Channel:** #production-talk — 17 reactions (pinned)
> "I would say it's not one or the other. I might do some big timing moves first, just to have the vocal 80% of the way there. Then I'll consolidate and drop into Melodyne. At this stage it's a lot more stretching and/or compressing notes, or more importantly PARTS of words."

> [!quote] Source
> **Author:** popaganda. — **Date:** 2025-01-02 — **Channel:** #production-talk — 14 reactions
> "No matter what I'd be trying to build off a live performance. Vocals and guitar at the same time if possible, make sure the artist is comfortable enough to really deliver the way they did on their videos. Sometimes when artists get in the studio they get way in their heads."

Key production-talk vocal insights:
- **Vocal tuning is both pitch AND timing** — BatMeckley separates consonants from vowels in Melodyne for more natural results
- **Auto-Tune Classic mode** was created after producers complained about Antares changing the sound between versions 5 and 7
- **The vocal producer's job** is as much about artist management (making them feel "safe enough to be dangerous") as it is about technical skill
- **Monitoring matters for production** — NoahNeedleman: "I want my artists to feel expensive when they're recording, so getting the mic and cue mix right is everything"

## See Also

- [[Vocal Chain]] — signal chain for vocal recording and processing
- [[Vocal Editing Across DAWs]] — vocal editing workflows per DAW
- [[De-esser]] — sibilance control glossary
- [[Compression Techniques]] — compressor topology and applications
- [[Automation and Mix Moves]] — vocal automation techniques
- [[Songwriting and Arrangement]] — vocal arrangement decisions

## Source Discussions

> [!quote] Discord Source
> **Channel:** #mixing-talk — **Date Range:** 2021-08 to 2026-02
> **Key contributors:** NoahNeedleman, ehutton21, Jeremy Klein, chrissorem, cian riordan, Ross Fortune, BatMeckley, oaklandmatt
> **Message volume:** 2,741 categorized messages

> [!quote] Discord Source — #newbie-questions
> **Channel:** #newbie-questions — **Date Range:** 2021-02 to 2026-02
> **Beginner vocal mixing context:** chrissorem (6 reactions): "Most people hear tuning/intonation better with a bass element in the mix. If I'm tuning multiple vocals, I tune the lead and mute other melodic instruments that might be distracting." BatMeckley (4 reactions): "Bounce all your vocals from beat 1. Make a stereo instrumental bounce. Tune and de-ess and re-consonant and time to your hearts content."
> See also: [[Beginner FAQ#Vocal Production]]

> [!quote] Discord Source
> **Channel:** #production-talk — **Date Range:** 2022-01 to 2026-02
> **Key contributors:** BatMeckley (47 vocal production msgs), austenballard (56 msgs), oaklandmatt (28 msgs), NoahNeedleman (42 msgs), popaganda. (vocal performance philosophy)
> **Message volume:** 812 vocal production categorized messages
> See also: [[production-talk Channel Summary]]
