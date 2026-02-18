---
type: topic
confidence: medium
aliases:
  - Audio Backup
  - Session Storage
  - Archive Strategy
tags:
  - domain/workflow
  - type/topic
created: 2026-02-17
modified: 2026-02-17
---

# Backup and Storage for Audio

## Summary
> [!abstract]
> Backup and storage strategy is critical for audio professionals managing terabytes of session data. The community strongly advocates the 3-2-1 backup rule (three copies, two media types, one offsite) and warns against relying solely on cloud sync services. Hardware choices between SSD, HDD, and NAS depend on whether files are active sessions or long-term archives.

## Detail

### Backup Strategies
The **3-2-1 rule** is the foundation of professional audio backup: keep three copies of your data, on two different media types, with one stored offsite. Active sessions should live on fast local storage, with regular backups to a secondary drive and periodic offsite or cloud backup. Sync software must be configured carefully to avoid propagating accidental deletions.

> [!quote] Source
> **Author:** cian riordan — **Date:** 2021-11-03 — **Channel:** #daw-talk
> "The use case here is let's say you're working on a project and you (or the DAW) has accidentally deleted a necessary file. Now lets say you don't notice and you go to run your end of day backup -- your sync software will know that that file was deleted, and then delete it off your backup."

### Storage Hardware (SSD vs HDD vs NAS)
- **SSD** — fast read/write speeds ideal for active sessions; NVMe drives handle large track counts and virtual instruments without bottlenecks
- **HDD** — cost-effective for archival storage; slower but available in larger capacities
- **NAS (Network Attached Storage)** — centralized storage accessible across multiple machines; redundancy via RAID configurations

> [!quote] Source
> **Author:** cian riordan — **Date:** 2023-10-26 — **Channel:** #daw-talk
> "I have a 5-bay Drobo that I use as my archival storage. Once a project is done and delivered, I move it off the work drives onto the Drobo. It's got roughly 13TB of information on it — basically everything I've worked on in the past 15 years."

### Cloud Storage for Audio
Cloud services like Backblaze, Google Drive, and Dropbox can serve as offsite backups, but auto-sync features are dangerous for audio sessions. A DAW deleting a temp file can trigger cloud sync to delete the backup copy. Manual or scheduled uploads are safer than real-time sync for session folders.

### Archive Workflows
When a project is delivered, professionals typically consolidate all session files, bounce stems, and move the complete package to archival storage. This includes saving session notes, plugin recall sheets, and any relevant correspondence. Naming conventions and folder structures should be consistent across all archived projects.

### Disaster Recovery
Time Machine on macOS provides basic versioned backup but has limitations for large audio sessions — it can slow down during recording and may not handle external drives gracefully. Dedicated backup software with versioning (Carbon Copy Cloner, ChronoSync) offers more control for audio professionals.

## Practical Application
- Follow the 3-2-1 backup rule: three copies, two media types, one offsite
- Use SSDs for active sessions and HDDs or NAS for completed project archives
- Disable real-time cloud sync on session folders to prevent accidental deletion propagation
- Consolidate and collect all files before archiving a completed project
- Schedule regular backups rather than relying on remembering to do them manually

## Common Mistakes
- Relying on a single drive with no backup at all
- Trusting cloud sync as a primary backup (auto-delete propagation risk)
- Not consolidating session files before archiving, leading to missing audio references
- Using Time Machine as the sole backup for professional work
- Failing to test backup restores — a backup you cannot restore is not a backup

## See Also
- [[Computer Hardware for Audio]] — drive and system recommendations
- [[Audio File Management]] — file organization and formats
- [[Session Templates and Organization]] — project structure best practices

## Community Screenshots

![[cian-riordan_2021-11-01_cr-backup.jpg]]
***cian riordan** — 2021-11-01 — Finally listened to the backup episode from a few weeks ago. And given Matt's recent debacles, I feel like this is a pretty great system for covering ...*

![[will-melones_2022-10-04_at-pm.png]]
***Will Melones** — 2022-10-04 — Yeah no need for System Prefs tricks anymore...you can just unassign it in PT's Keyboard Shortcuts!*

![[ross-fortune_2023-01-28_realised-that-acustica-has-been-taking.png]]
***Ross Fortune** — 2023-01-28 — Realised that Acustica has been taking up a spare +20GB on my HD. Little bin icon top right of Aquarius purges this unnecessary double storage of down...*

![[will-melones_2024-01-23_at-pm.png]]
***Will Melones** — 2024-01-23 — Interesting update to this Finder thing. I had noticed that the Archive Utility settings were defaulted to "compressed archive" format and figured tha...*

## Source Discussions

> [!quote] Discord Source
> **Channel:** #daw-talk — **Date Range:** 2021-02 to 2026-02
> **Key contributors:** cian riordan, Edward Rivera, Adam Thein, Rollmottle, Will Melones
> **Message volume:** 250 categorized messages
