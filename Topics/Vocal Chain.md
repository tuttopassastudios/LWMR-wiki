---
type: topic
confidence: medium
aliases:
  - Vocal Recording Chain
  - Vocal Signal Chain
  - Recording Vocals
tags:
  - type/topic
  - domain/recording
created: 2026-02-17
modified: 2026-02-18
---

# Vocal Chain

## Overview
> [!abstract]
> The vocal recording chain -- microphone, preamp, compressor, and any processing on the way in -- is one of the most discussed and debated signal paths in audio production. This guide synthesizes community recommendations on mic selection, preamp pairing, compression during tracking, and the philosophy of committing to sounds at the source.

## Community Consensus

- **The singer matters more than the chain** -- Technique, performance, and mic placement outweigh gear choices
- **Match the mic to the voice**, not to the price tag -- A $500 mic may outperform a $5,000 mic on a given vocalist
- **Commit to compression during tracking** when you know what you are doing -- it shapes the performance
- **The "default" chain** (U87 → Neve 1073 → LA-2A) is a cliche for a reason, but it is not the only path
- **Budget chains can compete** -- The community has multiple stories of inexpensive chains beating expensive ones

## The Chain That Beat a Grammy Engineer

> [!quote] SoundsLikeJoe
> "She finished production and went into vocals... AND HATED IT. They had huge mics going into a HUGE vocal chain... like $40k worth of stuff. They tried C800 and another thing or two. She hated it. Called me and said 'I gotta come back and do my vocals there.' What was I using? A Shure KSM32 into a Buzz Audio ARC1.1 strip."

This story encapsulates the community's philosophy: the right chain for the voice beats the expensive chain every time. The Grammy engineer's response -- "What the fuck are you using man? You can't use that. Those mics are terrible." -- reveals how assumptions about gear can mislead.

## Vocal Microphone Recommendations

### Budget to Mid-Range

| Mic | Type | Price | Community Notes |
|-----|------|-------|-----------------|
| [[Shure KSM32]] | LDC | ~$500 | "The star" -- handles sibilance well, works on everything |
| [[Shure SM7B]] | Dynamic | ~$400 | Pairs brilliantly with a [[Distressor]] (6:1, slow attack). Works best with loud, confident vocalists |
| [[Austrian Audio OC18]] | LDC | ~$850 | Exceptional vocal mic, designed by C12 capsule engineers |
| [[Warm Audio WA-87]] | LDC | ~$350 | Solid U87 clone |
| [[Warm Audio WA-251]] | LDC | ~$400 | Praised for vocals at its price |
| [[AT4033]] | LDC | ~$350 | "Solid workhorse" |

### High-End
| Mic | Type | Price | Community Notes |
|-----|------|-------|-----------------|
| [[Sony C800G]] | Tube LDC | $8,000+ | Hip-hop and pop standard; not universally loved |
| [[Neumann U87]] | LDC | $3,200+ | The default. Not always the best choice |
| [[Neumann U47]] | Tube LDC | Vintage | The Holy Grail for many |
| [[AKG C12]] / variants | Tube LDC | Vintage | Legendary warmth |
| [[Telefunken ELA M 251]] | Tube LDC | $10,000+ | Bright, detailed, expensive |

### Ribbon Mics for Vocals
- [[RCA 44]] -- cian riordan's pick for ribbon vocals
- Coles 4038 / KU3A -- "If it's a good one"
- Ribbons work beautifully on singers with harsh or sibilant voices

## Preamp Pairing

| Preamp | Character | Best Pairing | Community Notes |
|--------|-----------|-------------|-----------------|
| [[Neve 1073]] / clones | Warm, thick, transformer color | Thinner voices that need body | Classic pairing with any vocal mic |
| [[Buzz Audio ARC1.1]] | Channel strip with EQ/comp | All-in-one solution | SoundsLikeJoe's chain of choice |
| [[Ampex 350/351]] | Big tube sound, musical distortion | When you want TONE | "If I could have one pre to record everything for the rest of my life, this would be it" -- cian riordan |
| [[API 512]] | Punchy, midrange-forward | Vocals that need to cut | Great for aggressive performances |
| [[Focusrite ISA]] | Clean, transformer-based | Transparent with subtle warmth | Best "budget pro" option |
| Interface preamps | Clean/transparent | When the mic is doing the work | Genuinely adequate for most vocal work |

## Compression During Tracking

### The SM7B + Distressor Trick
> [!quote] Josh
> "He's literally just running the SM7 through the Distressor on the input. 6:1 ratio, slow attack. The slow attack helps prevent plosives from pumping."

This combination produces polished, controlled vocals from an affordable dynamic mic. The key insight: the slow attack lets transients through while the 6:1 ratio provides consistent level control.

### General Tracking Compression Approach
- **Light compression** (2-4 dB of gain reduction) is safe and recommended during tracking
- **Slow attack** preserves vocal transients and natural dynamics
- **Fast release** keeps the compressor from holding down the signal between phrases
- **Commit to the sound** -- If you are using hardware compression during tracking, print it. Do not try to undo it later

### When to Skip Tracking Compression
- When the vocalist has excellent dynamic control
- When you are unsure of the arrangement and want maximum flexibility
- When the compressor is adding artifacts you do not want

## The "Right" Vocal Chain

There is no universal answer. The community's approach:

1. **Listen to the vocalist** -- Record a test with 2-3 microphones if possible
2. **Choose the mic that flatters the voice**, not the most expensive one
3. **Add preamp character if needed** -- Some voices need warmth, others need clarity
4. **Compress only if you know what you are doing** -- Light gain reduction is usually safe
5. **Focus on mic placement** -- Distance, angle, and pop filter placement matter enormously

> [!quote] Eric Martin
> "The singer's talent and technique are even more important than mic placement, or mixing."

> [!quote] oaklandmatt
> "Good singer, singing a good part for their voice, not too close to the mic. That would drastically improve the majority of bad vocals for sure."

## Tips from the Community

- Record vocal tests with different mics before committing to a session's vocal chain
- The [[Shure KSM32]] handles sibilance better than most mics in its price range -- consider it before buying de-esser plugins
- If a vocalist sounds harsh through a condenser, try a ribbon or dynamic mic instead of reaching for EQ
- Mic distance matters more than mic choice in many cases -- a vocalist eating the mic sounds fundamentally different from one at 8-12 inches
- Do not be afraid to use "cheap" mics -- kidcutler did half of rapper Lucki's first project on a KSM32 and it matched seamlessly with the other half recorded through a vintage 87/Avalon/LA-2A chain

## Common Mistakes

- **Defaulting to the "industry standard" chain** without testing alternatives on the actual vocalist
- **Over-compressing during tracking** -- You cannot undo this
- **Ignoring room acoustics** -- The best vocal chain in an untreated room sounds worse than a budget chain in a treated one
- **Placing the mic too close** for vocalists who are not experienced with mic technique
- **Not recording a DI/clean take** for safety alongside the processed version
- **Spending $5,000 on a microphone** before investing in room treatment and monitoring

## Recording Vocal Technique (from #recording-talk)

### Mic Distance and Proximity Effect
> [!quote] cian riordan (2023-12-28)
> "Proximity effect on the mic is useful, so get right up on there. Aggressive HPF into heavy compression (1176 style FET is tough to beat). Heavy handed RXing to get out mouth noise and breaths that you've brought into the center of your brain with all the compression."

### Historical Perspective on Distance
> [!quote] BatMeckley (2023-01-25)
> "Those mics were meant to be used at a greater distance than we use them at today. Engineers were actual lab coat wearing electrical engineers with exacting standards of doing things and it was Geoff Emerick who kinda started when no one was looking pushing the mics closer to the sources to get a particular vibe, and it caught on."

### Omni Pattern for Vocalists
BatMeckley: "The biggest bonus of Omni to me is its basic total lack of proximity effect. So if you're in a well treated booth, the singer can really be feeling themselves dancing around (which can really help a take) and the recording will be way more consistent. It's also great for doing BVs."

### Voice Care and Remedies
See [[Session Mindset and Engineering Philosophy]] for Ross Fortune's pinned voice remedy guide (peppermint tea, salt gargle, steam, ginger) and BatMeckley's unconventional tips (Lays chips, Altoids, ibuprofen).

### Mic Shootouts
BatMeckley recommends regular mic shootouts on vocalists: "It's a good idea every once in a while to shoot out your mics on things and recalibrate your life. I just had a singer over to sing into the 251, the Josephson 705, the Soyuz 17FET, and the M930."

## Microphone Physics — How Mics Actually Work (from #nerd-talk)

David Fuller's cardioid microphone primer (14 reactions — the 2nd highest in #nerd-talk) explained the physics behind polar patterns in a way that helps engineers make better mic choices:

### How Cardioid Patterns Work
A cardioid microphone is not a single element that "listens forward." It achieves directionality through **phase cancellation**:

- The capsule has openings on both the front and rear
- Sound arriving from the front reaches the diaphragm directly
- Sound arriving from the rear enters through both the front and rear ports, arriving at the diaphragm at nearly the same time from both sides — the resulting pressure difference is near zero, producing cancellation
- The rear port's acoustic resistance (a carefully tuned damping material) controls the timing and degree of cancellation, shaping the polar pattern

### Why This Matters for Recording
- **Cupping a mic** (wrapping your hand around the grille) blocks the rear ports, destroying the cardioid pattern and turning it closer to omnidirectional — this is why vocalists who cup the mic sound muddy and feedback-prone in live settings
- **Proximity effect** is a consequence of the pressure-gradient design — the bass boost at close distances is physics, not a feature. It is more pronounced in cardioid patterns than in omni (which uses a different operating principle)
- **Off-axis coloration** varies dramatically between mic designs — some mics reject off-axis sound cleanly, while others color it heavily. This matters for room bleed and for how the mic handles a moving singer

### Choosing Patterns for the Source
| Pattern | Best For | Why |
|---------|----------|-----|
| **Cardioid** | Most vocal recording | Rejects rear sound, proximity effect available |
| **Omni** | Singers who move, well-treated rooms | No proximity effect, most natural sound, no off-axis coloration |
| **Figure-8** | Ribbon mics, MS technique, duets | Rejects sides, captures front and rear equally |
| **Hypercardioid** | Loud stages, high-bleed environments | Tighter pickup, but has a rear lobe — point the null at the loudest bleed source |

> [!note]
> See [[Impedance and Audio Electronics]] for how mic output impedance interacts with preamp input impedance to affect tone — this is another physical factor in "why mics sound different through different preamps."

## VariAudio vs Melodyne — Pitch Correction Workflow (from #cubase)

The #cubase channel produced extensive discussion on pitch correction tool selection and multi-tool workflows:

### Community Consensus
- **[[VariAudio]] wins for speed** — built into Cubase's Sample Editor, no ARA overhead, instant access
- **[[Melodyne]] wins for polyphonic editing** — superior fine-grained control on complex material
- Both tools are excellent for standard vocal tuning; the choice is workflow preference, not quality

### Multi-Tool Pitch Workflow
Lee Rouse's power-user approach chains multiple tools:
1. **[[VariAudio]]** — first pass for quick macro-tuning and timing correction
2. **Auto-Tune** — real-time tracking correction during recording for vocalists who want to hear correction in their headphones
3. **[[Melodyne]]** — detailed polyphonic editing for complex passages, harmonies, or fine corrections that VariAudio can't handle

### Lee Rouse's "Delete Block" Technique
In VariAudio, deleting an analyzed segment disables pitch correction for that specific region without affecting surrounding corrections. This is useful for preserving natural phrasing, slides, or intentional bends on specific notes while the rest of the vocal remains tuned.

> [!quote] Source
> **Author:** Lee Rouse — **Date:** 2024–2025 — **Channel:** #cubase
> Lee Rouse's multi-tool pitch workflow and delete-block technique represent the community's most refined approach to vocal pitch correction in Cubase.

## See Also
- [[Budget Gear Guide]]
- [[Acoustic Treatment Guide]]
- [[Outboard vs In-The-Box]]
- [[Recording and Tracking Workflows]]
- [[Session Mindset and Engineering Philosophy]]
- [[Headphone Mixes and Cue Systems]]
- [[Impedance and Audio Electronics]]

## Source Discussions

> [!quote] Discord Source
> **Channel:** #cubase — **Date Range:** 2024-09 to 2026-01
> **Key contributors:** Lee Rouse, SoundsLikeJoe, Joel "Roomie" Berghult
> **Message volume:** ~60 messages on VariAudio, Melodyne, and pitch correction workflows
> See also: [[cubase Channel Summary]]

> [!quote] Discord Source
> Channel: #gear-talk
> Matches: 62
> Key contributors: NoahNeedleman, Josh, ehutton21, BatMeckley, Jodonny, cian riordan, chris_donlin, SoundsLikeJoe, oaklandmatt

> [!quote] Discord Source
> Channel: #recording-talk
> Matches: 933
> Key contributors: BatMeckley, cian riordan, Zakhiggins, NoahNeedleman, Ross Fortune, peterlabberton, LAPhill

> [!quote] Discord Source
> Channel: #🧠nerd-talk
> Messages: ~126 (microphone physics, polar pattern theory, capsule design, preamp impedance interaction)
> Key contributors: David Fuller (polar pattern primer — 14 reactions), Nomograph Mastering, Bryan DiMaio, Gerhard Westphalen
> Date range: January 2024 – February 2026
> See also: [[nerd-talk Channel Summary]]

> [!quote] Discord Source — #newbie-questions
> **Channel:** #newbie-questions — **Date Range:** 2021-02 to 2026-02
> **Beginner vocal chain context:** oaklandmatt (6 reactions): "1. Sing a lot every day. If you don't, no other advice matters. 2. Hire a decent vocal coach." chrissorem (6 reactions): "Most people hear tuning/intonation better with a bass element in the mix." BatMeckley (4 reactions): "Bounce all your vocals from beat 1. Make a stereo instrumental bounce. Tune and de-ess to your hearts content." 47 vocal production messages categorized from beginners.
> See also: [[Beginner FAQ#Vocal Production]]
