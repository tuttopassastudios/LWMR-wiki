---
type: topic
confidence: medium
aliases:
  - Session Templates
  - Track Organization
  - Session Setup
tags:
  - domain/workflow
  - type/topic
created: 2026-02-17
modified: 2026-02-17
---

# Session Templates and Organization

## Summary
> [!abstract]
> Session templates and organization are foundational to professional audio workflow. Expert engineers invest significant time building templates with pre-configured routing, color coding, naming conventions, and default processing. Automation tools like SoundFlow (Pro Tools) can dramatically accelerate mix prep. Good organization saves hours per session and reduces errors.

## Detail

### Template Philosophy
Professional engineers build comprehensive templates rather than starting from scratch:
- Pre-configured bus routing (drums, bass, vocals, instruments, FX)
- Color coding by instrument group
- Default processing on buses (bus compression, EQ)
- Monitoring routing and reference track setup
- Marker templates for common song structures

### SoundFlow Automation (Pro Tools)
Nacho Sotelo uses SoundFlow scripts to automate mix prep:
- Script searches track comments for keywords and routes tracks to appropriate template folders
- Strips silence, colors tracks, routes to corresponding folders automatically
- Smaller scripts write track comments to minimize manual typing
- Reduces what would be hours of manual mix prep to minutes

> [!quote] Source
> **Author:** Nacho Sotelo — **Date:** 2024-03-23 — **Channel:** #daw-talk
> "My mix prep script searches for specific keywords in the track comments and moves the correct tracks to the appropriate folder in my template. It strips silence, colors the tracks, routes them to the corresponding folder."

### Ableton-Specific Organization
- **Audio Effect Racks** store entire processing chains as presets (Slow Hand)
- **Instrument Racks** with chain automation for live performance (Slow Hand)
- **Dummy clips** — empty clips that send program change messages for live set management (Slow Hand)
- **Cmd+F browser search** for instant access to any saved preset, sample, or plugin (oaklandmatt)

> [!quote] Source
> **Author:** Slow Hand — **Date:** 2022-02-17 — **Channel:** #daw-talk
> "Getting familiar with all of the capabilities of the instrument racks and audio effect racks — they're immensely powerful once you understand chains. Dummy clips are empty clips that you can launch to send program change messages to your racks."

### Naming Conventions and Delivery
- Consistent naming is critical for session transfers between engineers
- Stem naming should be clear and standardized
- Slow Hand goes to "great lengths to ensure that stems are as easy as possible to plug-and-play"

> [!quote] Source
> **Author:** Slow Hand — **Date:** 2022-06-29 — **Channel:** #daw-talk
> "I'm very particular about how my stuff gets rendered and go to great lengths to ensure that when I hand someone stems that they're going to be as easy as possible to plug-and-play."

## Practical Application
- Invest time building templates — it pays off exponentially
- Use scripting tools (SoundFlow, ReaScript) to automate repetitive tasks
- Standardize naming conventions within your team/studio
- Color code by instrument group for visual navigation
- Save processing chains as presets/racks for reuse

## Common Mistakes
- Not using templates (rebuilding from scratch every session)
- Inconsistent naming that confuses collaborators
- Over-complicated templates that slow down simple sessions
- Not updating templates as workflow evolves

## See Also
- [[Pro Tools]] — template and SoundFlow integration
- [[Ableton Live]] — racks and browser workflow
- [[Bounce and Export Workflows]] — delivery naming conventions
- [[Recording and Tracking Workflows]]
- [[Mixing in the DAW]]

## Source Discussions

> [!quote] Discord Source
> **Channel:** #daw-talk — **Date Range:** 2021-02 to 2026-02
> **Key contributors:** Nacho Sotelo, Slow Hand, oaklandmatt, Adam Thein, Rob Domos
> **Message volume:** 881 categorized messages (197 directly categorized, 68 from identified experts)
