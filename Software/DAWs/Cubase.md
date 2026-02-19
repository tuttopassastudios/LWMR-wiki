---
type: topic
confidence: high
aliases:
  - Cubase Pro
  - Nuendo
  - Steinberg Cubase
tags:
  - domain/software
  - type/topic
  - daw/cubase
created: 2026-02-17
modified: 2026-02-18
---

# Cubase

## Summary
> [!abstract]
> Cubase (and its sibling Nuendo) is Steinberg's professional DAW, recognized in the community for superior export/render workflows, excellent MIDI sequencing, [[VariAudio]] pitch editing, the powerful [[Logical Editor]], and strong video/post-production capabilities (especially Nuendo). Community members who use Cubase often come from post-production backgrounds or value its detailed stem export features. The dedicated #cubase channel reveals a deeply engaged power-user community led by Joel "Roomie" Berghult, SoundsLikeJoe (24-year veteran), and LAPhill.

## Strengths (Community Consensus)
- **Export/render workflow** — considered superior to Ableton's; export features are a noted strength (austenballard)
- **Routing flexibility** — right-click to create aux/buses with naming, considered easier than other DAWs (mixedbywong_my)
- **MIDI sequencing** — detailed sequencing capabilities, custom instrument note-mappings in piano roll (Slow Hand)
- **[[Logical Editor]] & PLE** — MIDI manipulation and project-level batch operations unmatched by other DAWs (LAPhill, SoundsLikeJoe)
- **[[VariAudio]]** — built-in pitch editing comparable to Melodyne, with speed advantage of no ARA overhead
- **Video support** — Cubase Pro handles multiple videos; Nuendo is a post-production standard (mixedbywong_my)
- **Direct Offline Processing** — flexible offline effect rendering
- **Control Room** — advanced monitoring and output routing
- **Automation** — bézier curves, range tool automation, comprehensive MIDI CC lanes

> [!quote] Source
> **Author:** mixedbywong_my — **Date:** 2021-12-20 — **Channel:** #daw-talk
> "Mixing in Cubase seems easier in terms of routing and creating buses. Just right click and make new aux/buses and rename before it's created."

## Weaknesses (Community Consensus)
- **Steinberg Download Manager** — installer/manager app frustrates users (Will Melones)
- **Smaller community** — fewer users in the community compared to Pro Tools and Ableton
- **Learning curve** — dense feature set can be overwhelming
- **Perpetual license cost** — more expensive upfront than Logic
- **ARA integration reliability** — Melodyne clicks/pops at region boundaries, Auto-Tune ARA crashes persist across versions

## Logical Editor & Project Logical Editor

The [[Logical Editor]] is widely considered Cubase's killer feature — a conditional MIDI transformation engine with no equivalent in other DAWs.

### Logical Editor (MIDI-level)
Operates on MIDI data within a part. Common uses:
- Batch-edit velocity curves across multiple parts
- Filter specific MIDI CC data
- Select all notes in a pitch range
- Transform note lengths, positions, and channels
- Create custom humanization presets

### Project Logical Editor (PLE)
Operates at the project level for track and event management:
- Track visibility presets (show/hide by name, color, or type)
- Batch-select and modify events across the entire project
- Automate repetitive session organization tasks

### Community Presets and Resources
- **LAPhill** maintains an extensive MIDI preset library for velocity editing, note filtering, and CC manipulation
- **SoundsLikeJoe** uses PLE for tempo workflow and session management
- **Greg Ondo** (Steinberg) shares community presets as a starting point for new users
- **Jeff Dunne** integrates LE presets with Stream Deck for one-touch macro execution
- **"Print MIDI Modifiers"** tip — apply MIDI insert effects permanently to the part data

> [!quote] Source
> **Author:** LAPhill — **Date:** 2025-01 — **Channel:** #cubase
> LAPhill's Logical Editor MIDI presets cover velocity curves, note filtering, CC manipulation, and track organization — the most comprehensive community preset library shared in the channel.

## VariAudio

[[VariAudio]] is Cubase's built-in pitch editing tool, integrated directly into the Sample Editor.

### VariAudio vs Melodyne
Community consensus from #cubase:
- **VariAudio wins** for speed and integration — no ARA overhead, instant access in Sample Editor
- **Melodyne wins** for polyphonic editing and fine-grained control
- Both are excellent for standard vocal tuning; the choice is workflow preference, not quality
- Lee Rouse uses a multi-tool approach: VariAudio for quick passes, Auto-Tune for real-time tracking, Melodyne for detailed polyphonic editing

### Key VariAudio Techniques
- **Split notes** — divide detected segments for more precise pitch control (SoundsLikeJoe)
- **Vibrato control** — adjust vibrato depth on individual notes
- **Free mode** — drag notes to non-chromatic positions for blue notes and microtonal work
- **Delete block technique** (Lee Rouse) — deleting an analyzed segment disables tuning for that region without affecting surrounding corrections; useful for preserving natural phrasing

> [!quote] Source
> **Author:** Lee Rouse — **Date:** 2024–2025 — **Channel:** #cubase
> Lee Rouse's multi-tool pitch workflow — VariAudio for quick tuning, Auto-Tune for real-time tracking correction, Melodyne for detailed polyphonic editing — represents the power-user approach to vocal production in Cubase.

## Cubase 14 Features

Cubase 14 (released ~2025) was well received by the community. Key additions:

- **Modulators** — Joel "Roomie" Berghult extensively tested the new modulator system for creative sound design
- **Mixer reordering** — long-requested ability to reorder mixer channels independently of the arrange window
- **Blob editing** — new audio editing mode (arrived in a 14.x maintenance update)
- **PT-style clip gain** — direct clip gain adjustment similar to Pro Tools' implementation
- **Dorico integration** — improved interoperability with Steinberg's notation software
- **Bitwig compatibility** — improved project exchange capabilities
- **M4 efficiency core support** — better performance on Apple Silicon, particularly M4 chips

## Cubase 15 Preview

Early reception of Cubase 15 in the community:
- **Expression maps revision** — significant overhaul of the expression map system, welcomed by orchestral users
- **Pattern engine melodic mode** — new creative tool for melodic pattern generation
- **Known bugs** — nudge bar bug reported by multiple users
- **Community consensus:** wait for the first maintenance update before upgrading — consistent with the community's general approach to DAW updates

## ARA Integration Issues

ARA plugin integration in Cubase remains a persistent pain point:

- **Melodyne clicks/pops** — audible artifacts at region boundaries when using Melodyne via ARA; the most commonly reported ARA issue
- **Auto-Tune ARA crashes** — Antares Auto-Tune in ARA mode causes session instability and occasional crashes
- **Workarounds:**
  - Commit early — render ARA-processed audio before further editing
  - Bounce in place before applying ARA plugins
  - Use [[VariAudio]] instead of Melodyne for simple tuning tasks to avoid ARA entirely
  - Avoid editing region boundaries after ARA processing

## Automation Workflow

Cubase's automation system offers capabilities valued by the community:
- **Bézier curves** — smooth automation curves beyond simple linear ramps
- **Write mode** — real-time automation recording with touch, latch, and write modes
- **Range tool** — select time ranges and apply automation operations to specific sections
- **MIDI CC automation lanes** — dedicated lanes for MIDI CC data alongside audio automation
- **Quick Controls** — map any parameter to a set of quick-access knobs
- **MIDI Remote** — Cubase's MIDI controller mapping system for custom hardware integration

## Click/Metronome Management

Two community approaches to click/metronome control:
- **Time signature track trick** — insert a time signature change to effectively mute the click for specific sections without automation
- **Fader automation approach** (LAPhill) — automate the click channel fader in the Control Room for gradual click fade-outs during recording

## Tempo Mapping

- **Warp grid manual workflow** — manually align the project grid to a free-tempo recording by adjusting warp points
- **"Set Definition From Tempo"** — transfers the project tempo map into an audio file's definition, useful for working with recorded audio that wasn't tracked to a click
- **Tempo detection limitations** — Cubase's automatic tempo detection works best with clear transient material; community recommends manual warp for complex or rubato recordings

## Nuendo/Cubase Distinction

- **ADM import** — Nuendo only. Cubase cannot import ADM files (Dolby Atmos Audio Definition Model), confirmed by Jemody's investigation. This is a hard limitation requiring a Nuendo license for immersive audio post-production
- **Feature comparison** — Nuendo includes all Cubase features plus post-production tools (ADM authoring, dialogue editing, game audio middleware integration)
- **Upgrade path** — Steinberg offers a Cubase Pro → Nuendo crossgrade at reduced cost

> [!quote] Source
> **Author:** Jemody — **Date:** 2024–2025 — **Channel:** #cubase
> Jemody's investigation confirmed that ADM import is exclusive to Nuendo — Cubase users working with Dolby Atmos must upgrade to Nuendo for full immersive audio authoring.

## Mixing Workflow
- Traditional mixer with flexible bus/aux creation
- Control Room feature for advanced monitoring setups
- Direct Offline Processing for non-destructive offline rendering
- Comprehensive automation system with bézier curves
- Mixer reordering (Cubase 14+)

## Recording Workflow
- Lane-based comping system
- Multiple video track support (Cubase Pro and Nuendo)
- Strong for post-production workflows where video sync is critical
- VST Connect for remote recording sessions

> [!quote] Source
> **Author:** mixedbywong_my — **Date:** 2022-11-17 — **Channel:** #daw-talk
> "If you're working with videos, you need a DAW that'll handle multiple videos. Logic can't do it. Only PT Ultimate lets you do more than 1 video track. Cubase Pro/Nuendo handles multiple videos."

## Key Features
- **[[VariAudio]]** — integrated pitch correction and editing
- **[[Logical Editor]]** — MIDI and project-level manipulation engine
- **Direct Offline Processing** — apply and manage offline effects non-destructively
- **Control Room** — sophisticated monitoring section with multiple outputs
- **Expression Maps** — custom instrument articulation mapping for the piano roll (Slow Hand)
- **[[Render in Place]]** — flexible rendering with or without inserts/sends
- **Nuendo** — extended version with additional post-production features

> [!quote] Source
> **Author:** Slow Hand — **Date:** 2021-02-06 — **Channel:** #daw-talk
> "I like the way you can make custom instrument note-mappings for the piano roll in Cubase. It's so helpful when using sampler instruments that use key-switching to change instrument articulations."

## Stock Plugins

Community assessment of Cubase's bundled plugins:

- **Magneto II** — tape saturation plugin with a direct connection to SPL Machine Head hardware; community rates it as an underappreciated stock plugin
- **Frequency** — parametric EQ comparable to FabFilter Pro-Q3 for basic tasks; dynamic EQ mode available
- **Retrologue** — virtual analog synthesizer; SoundsLikeJoe's blind test demonstrated it competing favorably with uHe Diva
- **DeEsser** — functional stock de-esser suitable for basic vocal work

## Known Issues
- Download manager and licensing system considered cumbersome (Will Melones)
- Smaller user base means fewer community resources and tutorials
- **Cubase 13 bounce fatal error** — LAPhill reported a fatal error during bounce operations in specific session configurations
- **Group editing confusion** — group editing behavior can produce unexpected results when tracks have different edit histories
- **VSTi multi-out visibility sync bug** — multi-output instrument track visibility doesn't always sync correctly between the arrange window and mixer
- **Melodyne ARA clicks** — audible artifacts at region boundaries (see ARA Integration Issues above)
- **OpenGL plugin issues** — plugins using OpenGL rendering (Soothe 2, Altiverb) can conflict with Steinberg's window management system
- **NVIDIA vs Radeon GPU issues** — some users report GUI glitches with specific GPU drivers; Radeon generally reported as more stable with Cubase

## Community Tips
- Nuendo is the better choice for audio post-production and sound design
- Cubase Pro required for multiple video tracks
- Consider Cubase if coming from a post-production background or if export workflow is a priority
- **Hazel rules** for automatic file management — Dean Tuza shared Hazel (macOS automation) rules that auto-organize Cubase project folders, backups, and exports
- **Parallel version installs** — Cubase supports running multiple major versions side-by-side; recommended for safe version migration
- **Pro Tools key command preset caveats** — Cubase ships with a Pro Tools key command preset, but community warns it has gaps and inconsistencies; building custom commands recommended over using the PT preset
- **"Bad plugin" diagnosis workflow** (SoundsLikeJoe) — when a session crashes on load, rename the VST plugin folders to isolate the offending plugin, then re-enable one at a time to identify the culprit
- Steinberg created the VST format — Cubase has the deepest VST/VST3 integration by design

## See Also
- [[Pro Tools]] — alternative for mixing and post-production
- [[Bounce and Export Workflows]] — Cubase export considered superior
- [[DAW Comparison]]
- [[Plugin Formats and Compatibility]] — VST/VST3 native (Steinberg created VST format)
- [[DAW Routing and Signal Flow]]
- [[Logical Editor]] — Cubase's MIDI and project manipulation engine
- [[VariAudio]] — built-in pitch editing
- [[Render in Place]] — Cubase's rendering workflow
- [[Vocal Editing Across DAWs]] — VariAudio in the vocal workflow
- [[Keyboard Shortcuts and Macros]] — Logical Editor as macro system

## Source Discussions

> [!quote] Discord Source
> **Channel:** #daw-talk — **Date Range:** 2021-02 to 2026-02
> **Key contributors:** mixedbywong_my, Slow Hand, austenballard, Will Melones
> **Message volume:** 280 categorized messages (40 from identified experts)

> [!quote] Discord Source
> **Channel:** #cubase — **Date Range:** 2024-09 to 2026-01
> **Key contributors:** Joel "Roomie" Berghult (141), Jemody (63), SoundsLikeJoe (59), LAPhill (52), Lee Rouse (49), chrissorem (41), Jeff Dunne (19)
> **Message volume:** ~421 substantive messages from 26 authors
> See also: [[cubase Channel Summary]]
