---
title: "Playwright MCP drives Edge, and its argument change takes effect only in the next process"
type: entity
status: current
authority: browser-harness
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [testing, web]
---

# Playwright MCP

As installed it defaulted to the `chrome` channel and failed with
`Chromium distribution 'chrome' is not found`: **this machine has no Chrome, and Edge is what the
owner actually uses.** The user-scope entry was rewritten to
`npx -y @playwright/mcp@latest --browser msedge` on 2026-08-05.

**A server already running keeps its old arguments** — that was confirmed rather than assumed, and
it means a configuration change lands only in the next Claude Code process.

The fallback that needs no MCP at all is a direct Playwright script: `npm i playwright` in a
scratch directory, browsers from the cache.

**Read [[a-browser-walk-watches-the-network-not-the-screen]] before writing another browser check.**
Those traps have cost three slices between them.

One cosmetic quirk of the browser itself: `/favicon.ico` returns 404 and **Edge writes it to the
console** while chromium stays quiet. No route serves an icon, so "no errors in the console" has to
be read as "none except favicon" in Edge.
