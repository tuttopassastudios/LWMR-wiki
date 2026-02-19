# LWMR Wiki — Audio Production Knowledge Base

Community-built wiki from the **Live with Matt Rad** Discord server, covering mixing, mastering, production, songwriting, gear, and more.

## Live Site

Browse the wiki online: https://tuttopassastudios.github.io/LWMR-wiki/

## Project Structure

```
Topics/       Wiki articles organized by subject (mixing, mastering, production, etc.)
Gear/         Hardware and equipment pages
Glossary/     Audio terminology definitions
MOC/          Maps of Content — high-level index pages linking related topics
Software/     DAWs, plugins, and tool pages
Sources/      Channel message vaults (raw Obsidian-formatted Discord exports)
Assets/       Images and attachments referenced by wiki pages
_Meta/        Home page, templates, contributor info, and site config

scripts/      Python processing scripts (extraction, image handling, link conversion)
Extracts/     JSON data output from extraction scripts (one folder per channel)
.github/      Deploy workflow and Quartz rendering script
```

## How to Use

1. Clone this repo: `git clone https://github.com/tuttopassastudios/LWMR-wiki.git`
2. Open the folder in [Obsidian](https://obsidian.md)
3. Install the community plugins when prompted (Dataview, Templater, etc.)
4. Start browsing from **Home** (`_Meta/Home.md`) → explore via the Maps of Content in `MOC/`

> `scripts/`, `Extracts/`, and `.github/` are hidden from Obsidian's sidebar by default. You'll only see wiki content when browsing.

## How to Contribute

1. Fork this repo
2. Open your fork in Obsidian
3. Make edits or add new pages following existing templates in `_Meta/Templates/`
4. Submit a Pull Request

## Processing Pipeline

The wiki is built from Discord channel exports. The pipeline works as follows:

1. **Extract** — `scripts/extract_*.py` scripts parse raw Discord JSON exports, categorize messages by topic, and output structured JSON to `Extracts/`
2. **Build vault** — Extracted data is transformed into Obsidian markdown pages in `Sources/` and `Topics/`
3. **Process media** — `scripts/extract_images.py`, `scripts/embed_media.py`, and `scripts/convert_to_cdn_links.py` handle image extraction and CDN linking
4. **Deploy** — GitHub Actions builds the vault with [Quartz](https://quartz.jzhao.xyz/) and publishes to GitHub Pages
