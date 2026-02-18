---
type: topic
confidence: high
aliases:
  - Gear Repair
  - Studio Maintenance
  - Equipment Maintenance
  - Troubleshooting Gear
tags:
  - type/topic
  - domain/hardware
created: 2026-02-17
modified: 2026-02-17
---

# Gear Maintenance and Repair

## Overview
> [!abstract]
> Owning professional audio equipment means maintaining it. This guide covers preventive maintenance, common repair scenarios, backup and storage strategies, finding qualified technicians, and the community's practical advice for keeping a studio running reliably.

## Community Consensus

- **Learn basic soldering and cable repair** -- This is the minimum DIY maintenance skill every engineer should have
- **Preventive maintenance is cheaper than emergency repairs** -- Regular cleaning and inspection prevents failures
- **Find a trusted local technician** before you need one urgently
- **Backup your sessions religiously** -- Hardware fails; data should survive
- **Vintage gear requires budgeting for maintenance** -- Factor ongoing costs into purchase decisions
- **Climate control matters** -- Humidity and temperature affect tube gear, capacitors, and mechanical components

## Preventive Maintenance

### Regular Cleaning Schedule
| Task | Frequency | Details |
|------|-----------|---------|
| Dust equipment exteriors | Weekly | Compressed air or soft cloth |
| Clean faders and pots | Monthly-Quarterly | DeoxIT or contact cleaner |
| Inspect cable connections | Monthly | Check for loose or corroded connectors |
| Test all cables | Quarterly | Use a cable tester to catch intermittent failures |
| Clean patch bay jacks | Quarterly | Contact cleaner and dummy plugs |
| Inspect tube gear | Annually | Check for microphonic or failing tubes |
| Recap electrolytic capacitors | Every 10-20 years | Critical for vintage gear |

### Environment
- **Temperature**: Keep studio between 65-75F / 18-24C
- **Humidity**: 40-60% relative humidity is ideal
- **Ventilation**: Tube gear and power amplifiers need airflow
- **Power**: Use surge protection at minimum; see [[Power Conditioning]]

## Common Repairs

### Cable Repair
The most common and most accessible repair:
- Learn to re-solder XLR, TRS, and TS connectors
- Keep spare Neutrik connectors on hand
- A cable tester pays for itself after the first repair
- See [[DIY and Clone Gear]] for soldering equipment recommendations

### Tube Replacement
- Tubes degrade over time and eventually need replacement
- Keep spare matched sets for critical equipment
- **JJ tubes** are a commonly recommended replacement brand
- Biasing may be required after tube replacement (consult your manual or tech)

> [!quote] cian riordan
> "No more expensive than any other modern tube pre, maybe even cheaper given how available tubes are and how much knowledge is out there about them." (on maintaining Ampex 350 tube preamps)

### Capacitor Replacement (Recapping)
- Electrolytic capacitors have a finite lifespan (10-30 years depending on quality and conditions)
- Vintage gear almost certainly needs recapping
- Symptoms of failing caps: hum, reduced output, intermittent operation, audio distortion
- This is generally a job for a qualified technician

### Fader Cleaning/Replacement
- Console faders get noisy and scratchy over time
- Contact cleaner (DeoxIT) resolves most issues
- Motorized faders may need motor replacement
- Moving fader calibration is a specialist task

## Vintage Gear Maintenance

### Budgeting for Vintage
When purchasing vintage equipment, add 20-30% to the purchase price as a maintenance buffer:
- Initial servicing (recap, tube check, alignment)
- Replacement parts
- Technician labor

### Finding Vintage Mic Repair
> [!quote] Adam Thein
> "Cole [Picks Vintage] is also a great resource for dynamic and ribbon mic repairs. He's fixed up quite a few for me and always is a great communicator and friendly. 10/10."

Specialized vintage microphone technicians:
- Cole Picks Vintage (Nashville) -- Dynamic and ribbon mic repairs
- Vintage microphone specialists can restore RCA 44s, U47s, and other classic mics
- Always get a quote before shipping expensive vintage gear

### Tape Machine Maintenance
- Head alignment, demagnetization, and cleaning are regular maintenance tasks
- See [[Tape Machines in Modern Production]] for specific tape maintenance advice
- Qualified tape machine technicians are increasingly rare -- find one and maintain the relationship

## Backup and Storage

### The 3-2-1 Rule
The community follows a variation of the standard backup rule:
- **3 copies** of important data
- **2 different media types** (SSD + cloud, or NAS + external drive)
- **1 offsite** (cloud backup)

### Recommended Backup Solutions

| Solution | Type | Community Notes |
|----------|------|-----------------|
| [[Backblaze]] | Cloud backup | Backs up everything continuously. Multiple members use this |
| Local NAS (Synology, QNAS) | Network storage | Long-term archival, can run as local "cloud" |
| External SSDs | Portable | For working drives; more reliable than spinning drives |
| TrueNAS / FreeNAS | DIY NAS | "Roll your own local Dropbox" -- Rollmottle |

> [!quote] Rollmottle
> "Backblaze backs up everything. I am in the process of standing up a local NAS to long-term store everything. Then I am moving to exclusively solid state drives for all working drives going forward."

### Drive Strategy
- **Working drives**: SSD only (reliability, speed)
- **Archive drives**: NAS with RAID redundancy
- **Cloud**: Backblaze or similar for offsite disaster recovery
- **Never trust a single drive** with irreplaceable data

## Finding a Technician

### What to Look For
- Experience with your specific type of gear (console techs, tube amp techs, and digital repair techs are different specialties)
- Willingness to communicate clearly about what they find and what it will cost
- Reasonable turnaround times
- References from other studio owners

### When to DIY vs Hire a Pro
| Task | DIY | Professional |
|------|-----|-------------|
| Cable repair | Yes | -- |
| Tube replacement (simple) | Yes, if manual covers it | If biasing is needed |
| Capacitor replacement | Only if experienced | Usually |
| Console fader cleaning | Yes | If motorized/complex |
| Tape machine alignment | Only if trained | Usually |
| Power supply repair | No | Always |
| Vintage mic restoration | No | Always |

## Industry Concerns

The community has discussed broader concerns about gear maintenance and the industry:
- Market consolidation ("enshittification") affects parts availability and support
- Small manufacturers being acquired by larger companies can lead to reduced support for older products
- The importance of companies maintaining long-term product support
- Right-to-repair considerations for professional audio equipment

## Tips from the Community

- **Label everything** -- When you open a piece of gear for maintenance, photograph the internals before touching anything
- **Keep a maintenance log** -- Track when tubes were replaced, when gear was last serviced, etc.
- **Budget for maintenance annually** -- Set aside 5-10% of your gear value per year
- **Do not defer known issues** -- A scratchy pot today becomes a dead channel next month
- **Build relationships with technicians** before emergencies -- Being a regular customer gets you faster turnaround
- **Stock spare cables, tubes, and fuses** -- The most common failures should have instant replacements available

## Common Mistakes

- **Ignoring preventive maintenance** until something fails catastrophically
- **Attempting repairs beyond your skill level** -- A botched repair is more expensive than a professional one
- **Not backing up sessions** -- Hardware failure is when, not if
- **Buying vintage gear without a maintenance budget**
- **Using compressed air on tube gear without proper technique** -- You can damage delicate components
- **Storing gear in humid or temperature-extreme environments**
- **Not testing gear after purchase** -- Always verify functionality before the return window closes

## See Also
- [[DIY and Clone Gear]]
- [[Power Conditioning]]
- [[Cables and Connectivity Guide]]
- [[Tape Machines in Modern Production]]
- [[Backup and Storage for Audio]]

## Source Discussions
> [!quote] Discord Source
> Channel: #gear-talk
> Matches: 174
> Key contributors: Nomograph Mastering, cian riordan, Eric Martin, David Fuller, SoundsLikeJoe, Zack Hames, peterlabberton, Adam Thein, Rollmottle, Will Melones
