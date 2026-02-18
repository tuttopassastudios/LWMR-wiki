---
type: topic
confidence: medium
aliases:
  - Power Conditioner
  - Rack Power
  - Clean Power
  - Surge Protection
tags:
  - type/topic
  - domain/hardware
created: 2026-02-17
modified: 2026-02-17
---

# Power Conditioning

## Overview
> [!abstract]
> Power conditioning in the studio ranges from basic surge protection to elaborate isolation transformers and voltage regulation. The community's take is refreshingly pragmatic: you do not need to spend a fortune, but you do need organized, switched, surge-protected power distribution. This guide covers what actually matters and what is marketing.

## Community Consensus

- **Basic Furman rack power strips are all most studios need**
- **A front-panel switch** is the most important feature -- lets you sequence power on/off
- **Surge protection is essential**; exotic "power conditioning" is optional
- **Organize your studio power** through rack-mounted strips for clean switching
- **Ground loops are the real enemy** -- proper grounding practices matter more than expensive power conditioners
- **Do not spend a fortune** on power conditioning until everything else in your signal chain is sorted

## Recommended Power Solutions

| Product | Price Range | Features | Community Notes |
|---------|------------|----------|-----------------|
| [[Furman]] basic rack power conditioner | $50-100 | Surge protection, front switch, rear outlets | "The classic Furman power conditioner, it's worked great and has been helpful" -- Zack Hames |
| [[Furman D10-PFP]] | ~$100 | No front switch, daisy-chainable | Eric Martin uses 4 daisy-chained under the desk for sequenced power |
| [[Furman Power Factor Pro]] | ~$300 | Balanced power, voltage regulation | Rollmottle uses one to aggregate 3 rack Furmans |
| Pyle rack power strip | ~$30 | Basic switched rack strip | "Nothing fancy. Have a few of these and they work great" -- cian riordan |

## Power Distribution Strategy

### The Rollmottle Approach
> [!quote] Rollmottle
> "Buy one with a switch on the front and an outlet or two on the front face. Everything else is gravy. Everything in my studio is routed through 3 rackmount Furmans, which then go to 1 Furman Power Factor Pro on the ground, which aggregates the 3 rack Furmans and plugs into the wall."

### The Eric Martin Approach
> [!quote] Eric Martin
> "I have 2 on my desk that have switches and a plug on the front and then I have 4 of the Furman D10's on racks and under the desk daisy chained together without switches. This lets me sequence the power on and off with only 2 switches for the studio."

### Key Principles
1. **Centralize power switching** -- 1-3 switches should control your entire studio
2. **Use rack-mounted strips** for clean installation
3. **Front-panel switches and outlets** are genuinely useful features
4. **Sequence power-on order**: Monitors and amplifiers should power on LAST and off FIRST
5. **Separate digital and analog power** where practical to reduce noise

## What Actually Matters vs Marketing

### What Matters
- **Surge protection** -- Protects equipment from power spikes
- **Switched outlets** -- Organized power-on/off sequencing
- **Adequate outlet count** -- Enough plugs for all your gear
- **Proper grounding** -- Star ground or isolated ground circuits
- **Dedicated circuits** -- Having your studio on its own electrical circuit(s)

### What Is Mostly Marketing
- "Audiophile" power cables ($500+ power cords)
- Ultra-expensive power conditioners promising "blacker backgrounds"
- Exotic voltage regulation for studios with stable municipal power
- Power cable "directionality"

> [!note]
> The community firmly distinguishes between practical power management and audiophile snake oil. No one in #gear-talk recommends expensive power cables.

## Grounding and Noise

### Ground Loops
The most common power-related audio problem:
- Caused by multiple ground paths between equipment
- Manifests as 60Hz (US) or 50Hz (EU) hum in audio signals
- **Solutions**: Ground lift on DI boxes, balanced connections, star grounding, isolation transformers

### Dedicated Circuits
- Ideally, your studio should have its own dedicated electrical circuit(s)
- Avoid sharing circuits with refrigerators, HVAC, or other high-draw appliances
- An electrician can add dedicated circuits relatively affordably

### Power Sequencing
Proper power-on sequence prevents pops and speaker damage:
1. Power on source equipment (interface, outboard) first
2. Power on monitor controller
3. Power on amplifiers/powered monitors LAST
4. Reverse order for power-off

## Tips from the Community

- A front-panel outlet on your rack power strip is surprisingly useful for charging phones, powering test equipment, etc.
- If you are building out a studio, have an electrician install dedicated circuits before buying exotic power conditioners
- The Furman Power Factor Pro is useful if you have particularly dirty power or play live shows -- otherwise the basic Furmans are sufficient
- Use a UPS (uninterruptible power supply) on your computer to prevent data loss during power outages, separate from your audio power

## Common Mistakes

- **Spending hundreds on power conditioning before treating the room or upgrading monitors**
- **Daisy-chaining consumer power strips** instead of using proper rack-mounted distribution
- **Ignoring power-on sequencing** and sending pops through monitors
- **Not using surge protection at all** -- Equipment damage from power surges is preventable
- **Believing expensive power cables improve audio quality**
- **Sharing circuits with non-studio appliances**

## See Also
- [[Gear Maintenance and Repair]]
- [[Cables and Connectivity Guide]]
- [[Budget Gear Guide]]
- [[Acoustic Treatment Guide]]

## Source Discussions
> [!quote] Discord Source
> Channel: #gear-talk
> Matches: 36
> Key contributors: Bryan DiMaio, Eric Martin, Nomograph Mastering, Zack Hames, Rollmottle, Gerhard Westphalen, jonmatteson, SoundsLikeJoe
