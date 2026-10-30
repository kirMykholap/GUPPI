---
type: decision
case: "949"
status: current
defer: ["[[estimate-plugin-install-sets-aside-the-files-of-the-project]]"]
origin: raw/2026-10-30/2345/ledger.md#case-949
sprint: plugin
created: 2026-10-30
tags: [plugin, harness]
---

## Context

At the /hi of session 2345 the person put off the reading of `estimate-plugin-install-sets-aside-the-files-of-the-project`. Its event, the librarian's run of session 1713, came, and at the stop of Work Mode of session 2005 three projects ran; the project started with `UV_OFFLINE=1` and an empty `UV_CACHE_DIR` installed online (L56), so the putting back of the set-aside files after a failed `uv sync` was not seen.

## Problem

No session has yet seen the install of a project with files of its own fail at `uv sync` offline, so no Case of this session can take the reading.

## Deferred

### [[estimate-plugin-install-sets-aside-the-files-of-the-project]]

Whether the install sets aside the files of the project and puts them back after a failed uv sync; its offline reading waits for an install started with UV_OFFLINE=1 and an empty UV_CACHE_DIR, which no session has run offline yet

## History

- 2026-10-31 created · raw/2026-10-30/2345/ledger.md#case-949
