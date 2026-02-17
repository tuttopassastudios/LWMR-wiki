#!/usr/bin/env node
/**
 * render-dataview.mjs
 *
 * Replaces ```dataview code blocks with static markdown tables.
 * Runs in CI only — vault files stay as pure Obsidian markdown.
 *
 * Usage: node render-dataview.mjs <content-dir>
 */

import { readFileSync, writeFileSync, readdirSync, statSync } from "fs";
import { join, relative, basename, extname } from "path";

const contentDir = process.argv[2];
if (!contentDir) {
  console.error("Usage: node render-dataview.mjs <content-dir>");
  process.exit(1);
}

// ---------------------------------------------------------------------------
// Collect all markdown files and parse frontmatter
// ---------------------------------------------------------------------------

function walkDir(dir) {
  const results = [];
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    const st = statSync(full);
    if (st.isDirectory()) {
      results.push(...walkDir(full));
    } else if (extname(full) === ".md") {
      results.push(full);
    }
  }
  return results;
}

function parseFrontmatter(content) {
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) return {};
  const fm = {};
  let currentKey = null;
  for (const line of match[1].split("\n")) {
    // Handle key with no value (array parent like "tags:" or "aliases:")
    const emptyKey = line.match(/^(\w[\w\s]*?):\s*$/);
    if (emptyKey) {
      currentKey = emptyKey[1].trim();
      fm[currentKey] = "";
      continue;
    }
    // Handle simple key: value pairs
    const kv = line.match(/^(\w[\w\s]*?):\s*(.+)$/);
    if (kv) {
      currentKey = kv[1].trim();
      const val = kv[2].trim();
      fm[currentKey] = val.replace(/^["']|["']$/g, "");
      continue;
    }
    // Handle array items (tags, aliases) — flatten into comma-separated
    const arr = line.match(/^\s+-\s+(.+)$/);
    if (arr && currentKey) {
      const existing = fm[currentKey];
      if (existing === "" || existing === undefined) {
        fm[currentKey] = arr[1].trim();
      } else {
        fm[currentKey] = existing + ", " + arr[1].trim();
      }
    }
  }
  return fm;
}

// Build file index
const allFiles = walkDir(contentDir);
const fileIndex = allFiles.map((fullPath) => {
  const content = readFileSync(fullPath, "utf-8");
  const fm = parseFrontmatter(content);
  const rel = relative(contentDir, fullPath);
  const name = basename(fullPath, ".md");
  // Count list items (lines starting with - )
  const listItems = content.split("\n").filter((l) => /^\s*-\s+/.test(l));
  return { fullPath, rel, name, fm, listCount: listItems.length };
});

// ---------------------------------------------------------------------------
// Dataview query evaluator
// ---------------------------------------------------------------------------

function matchesFrom(file, fromClause) {
  // FROM "path" — check if file's relative path starts with that path
  // FROM -"path" — exclude files in that path
  // FROM -"path1" AND -"path2" — exclude multiple paths
  const parts = fromClause.split(/\s+AND\s+/i);
  for (const part of parts) {
    const neg = part.trim().match(/^-"(.+)"$/);
    const pos = part.trim().match(/^"(.+)"$/);
    if (neg) {
      if (file.rel.startsWith(neg[1] + "/") || file.rel === neg[1]) return false;
    } else if (pos) {
      if (
        !file.rel.startsWith(pos[1] + "/") &&
        file.rel !== pos[1]
      )
        return false;
    }
  }
  // If all parts were negative, file passes; if positive, must have matched
  return true;
}

function matchesWhere(file, whereClause) {
  if (!whereClause) return true;

  // WHERE confidence = "low"
  const eqMatch = whereClause.match(/(\w+)\s*=\s*"([^"]+)"/);
  if (eqMatch) {
    return file.fm[eqMatch[1]] === eqMatch[2];
  }
  // WHERE length(file.inlinks) = 0 — we can't compute backlinks, skip
  if (whereClause.includes("file.inlinks")) return false;
  // WHERE type
  if (whereClause.trim() === "type") return !!file.fm.type;
  // WHERE file.name = "Processing Log"
  const nameMatch = whereClause.match(/file\.name\s*=\s*"([^"]+)"/);
  if (nameMatch) return file.name === nameMatch[1];
  // WHERE false
  if (whereClause.trim() === "false") return false;

  return true;
}

function wikilink(name) {
  return `[[${name}]]`;
}

function renderQuery(queryBlock) {
  const lines = queryBlock.trim().split("\n");
  const firstLine = lines[0].trim().toUpperCase();

  // Detect LIST vs TABLE vs TABLE WITHOUT ID
  const isList = firstLine.startsWith("LIST");
  const isTableNoId = lines[0].trim().match(/^TABLE\s+WITHOUT\s+ID/i);

  // Parse FROM clause
  const fromLine = lines.find((l) => /^\s*FROM\s+/i.test(l));
  const fromClause = fromLine
    ? fromLine.replace(/^\s*FROM\s+/i, "").trim()
    : null;

  // Parse WHERE clause
  const whereLine = lines.find((l) => /^\s*WHERE\s+/i.test(l));
  const whereClause = whereLine
    ? whereLine.replace(/^\s*WHERE\s+/i, "").trim()
    : null;

  // Parse SORT clause
  const sortLine = lines.find((l) => /^\s*SORT\s+/i.test(l));
  let sortField = "file.name";
  let sortDir = "ASC";
  if (sortLine) {
    const sp = sortLine.replace(/^\s*SORT\s+/i, "").trim().split(/\s+/);
    sortField = sp[0];
    if (sp[1]) sortDir = sp[1].toUpperCase();
  }

  // Parse LIMIT
  const limitLine = lines.find((l) => /^\s*LIMIT\s+/i.test(l));
  const limit = limitLine
    ? parseInt(limitLine.replace(/^\s*LIMIT\s+/i, "").trim())
    : Infinity;

  // Parse GROUP BY
  const groupLine = lines.find((l) => /^\s*GROUP\s+BY\s+/i.test(l));
  const groupByField = groupLine
    ? groupLine.replace(/^\s*GROUP\s+BY\s+/i, "").trim()
    : null;

  // Parse column fields (TABLE field1, field2, ... or TABLE WITHOUT ID field1 AS "Alias", ...)
  let columns = [];
  if (!isList) {
    let fieldLine;
    if (isTableNoId) {
      fieldLine = lines[0]
        .replace(/^TABLE\s+WITHOUT\s+ID\s*/i, "")
        .trim();
      // Collect continuation lines (before FROM/WHERE/SORT/LIMIT/GROUP)
      for (let i = 1; i < lines.length; i++) {
        if (/^\s*(FROM|WHERE|SORT|LIMIT|GROUP)/i.test(lines[i])) break;
        fieldLine += " " + lines[i].trim();
      }
    } else {
      fieldLine = lines[0].replace(/^TABLE\s*/i, "").trim();
      for (let i = 1; i < lines.length; i++) {
        if (/^\s*(FROM|WHERE|SORT|LIMIT|GROUP)/i.test(lines[i])) break;
        fieldLine += " " + lines[i].trim();
      }
    }
    // Split on commas, respecting AS aliases
    if (fieldLine) {
      columns = fieldLine.split(",").map((c) => {
        c = c.trim();
        const asMatch = c.match(/(.+?)\s+AS\s+"([^"]+)"/i);
        if (asMatch) {
          return { field: asMatch[1].trim(), alias: asMatch[2] };
        }
        return { field: c, alias: c };
      });
    }
  }

  // Filter files
  let results = fileIndex.filter((f) => {
    if (fromClause && !matchesFrom(f, fromClause)) return false;
    if (!matchesWhere(f, whereClause)) return false;
    return true;
  });

  // Sort
  results.sort((a, b) => {
    let aVal, bVal;
    if (sortField === "file.name") {
      aVal = a.name;
      bVal = b.name;
    } else if (sortField === "file.mtime") {
      // We don't have real mtime in CI — sort by name as fallback
      aVal = a.name;
      bVal = b.name;
    } else {
      aVal = a.fm[sortField] || "";
      bVal = b.fm[sortField] || "";
    }
    const cmp =
      typeof aVal === "string"
        ? aVal.localeCompare(bVal)
        : aVal - bVal;
    return sortDir === "DESC" ? -cmp : cmp;
  });

  // Limit
  if (limit !== Infinity) results = results.slice(0, limit);

  // GROUP BY
  if (groupByField) {
    const groups = {};
    for (const f of results) {
      const key = f.fm[groupByField] || "(none)";
      if (!groups[key]) groups[key] = [];
      groups[key].push(f);
    }
    // Render grouped table
    const colHeaders = columns.map((c) => c.alias);
    let md = `| ${colHeaders.join(" | ")} |\n| ${colHeaders.map(() => "---").join(" | ")} |\n`;
    const sortedKeys = Object.keys(groups).sort();
    for (const key of sortedKeys) {
      // For "type AS Type, length(rows) AS Count" pattern
      md += `| ${key} | ${groups[key].length} |\n`;
    }
    return md.trim();
  }

  // Render LIST
  if (isList) {
    if (results.length === 0)
      return "*No results.*";
    return results.map((f) => `- ${wikilink(f.name)}`).join("\n");
  }

  // Render TABLE
  const showId = !isTableNoId;
  const headers = [];
  if (showId) headers.push("File");
  for (const col of columns) headers.push(col.alias);

  if (results.length === 0) return "*No results.*";

  let md = `| ${headers.join(" | ")} |\n| ${headers.map(() => "---").join(" | ")} |\n`;

  for (const f of results) {
    const row = [];
    if (showId) row.push(wikilink(f.name));
    for (const col of columns) {
      const field = col.field;
      if (field === "file.mtime") {
        row.push("—");
      } else if (field === "file.link") {
        row.push(wikilink(f.name));
      } else if (field.includes("length(file.lists)")) {
        row.push(String(f.listCount));
      } else if (field.includes("length(filter(")) {
        row.push("—");
      } else {
        row.push(f.fm[field] || "—");
      }
    }
    md += `| ${row.join(" | ")} |\n`;
  }

  return md.trim();
}

// ---------------------------------------------------------------------------
// Process all markdown files — replace ```dataview blocks
// ---------------------------------------------------------------------------

const dataviewRegex = /```dataview\r?\n([\s\S]*?)```/g;
let filesChanged = 0;
let blocksReplaced = 0;

for (const file of allFiles) {
  const content = readFileSync(file, "utf-8");
  if (!content.includes("```dataview")) continue;

  const newContent = content.replace(dataviewRegex, (_match, query) => {
    blocksReplaced++;
    return renderQuery(query);
  });

  if (newContent !== content) {
    writeFileSync(file, newContent, "utf-8");
    filesChanged++;
    console.log(`  Rendered: ${relative(contentDir, file)}`);
  }
}

console.log(
  `\nDataview pre-render complete: ${blocksReplaced} blocks in ${filesChanged} files.`
);
