---
type: glossary
confidence: medium
aliases:
  - SoundFlow
tags:
  - type/glossary
created: 2026-02-17
modified: 2026-02-18
---

# SoundFlow

## Definition

Automation and scripting platform for DAWs, particularly [[Pro Tools]], that enables custom keyboard shortcuts, macros, and workflow scripts. Built on JavaScript, SoundFlow provides deep DAW integration that goes beyond simple keystroke recording to read and manipulate session data, track names, and plugin states.

## Context

SoundFlow is widely used by professional mix and mastering engineers to speed up repetitive tasks in [[Pro Tools]], such as track setup, routing, and session organization. It supports JavaScript-based scripting and has a community library of shared scripts via the SoundFlow forum.

**Key SoundFlow Tools and Workflows (from #pro-tools):**
- **[[Bounce Factory]]** — SoundFlow's built-in stem bouncing tool that automates the solo→bounce→rename cycle for stem delivery. The most popular entry point for SoundFlow automation
- **Custom stem printing scripts** — Tristan builds purpose-built scripts that go beyond Bounce Factory for session-specific delivery requirements
- **Forte** — newer third-party export tool built on SoundFlow; promising but reported as buggier than Bounce Factory
- **Nic's Logic Bouncer** — SoundFlow script for [[Logic Pro]] that automates the tedious manual solo-bounce stem export workflow (Bryan DiMaio, #logic-pro)
- **bobby k's tape saturation macro** — creative routing automation: trim → external insert → compensating trim across multiple tracks
- **Mix prep automation** — Nacho Sotelo's scripts that search track comments for keywords and auto-route tracks to template folders (from #daw-talk)

**SoundFlow vs Keyboard Maestro (Tristan, #pro-tools):**
SoundFlow is "80-90% JavaScript" with deep Pro Tools hooks — it can read session data, track properties, and plugin states. Keyboard Maestro works across all macOS apps but lacks DAW-specific depth. For Pro Tools power users, SoundFlow is the clear recommendation.

**Using AI/GPT for Script Writing:**
Tristan advocates using AI code assistants to help write SoundFlow scripts, since the platform's JavaScript foundation makes AI-generated code effective and relevant.

## Related Terms

- [[Keyboard Shortcuts and Macros]]
- [[Pro Tools]]
- [[Bounce Factory]]

## See Also

- [[Editing Techniques Across DAWs]]
- [[Session Templates and Organization]] — SoundFlow for mix prep automation
- [[Bounce and Export Workflows]] — Bounce Factory and stem export context
