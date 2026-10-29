---
type: decision
case: "862"
status: archived
defer: ["[[estimate-git-context-offers-git-init]]", "[[estimate-plugin-install-offers-to-install-uv]]", "[[estimate-plugin-install-undoes-the-copy-when-uv-sync-fails]]", "[[estimate-guppi-package-is-ready-after-the-install]]"]
superseded_by: ["[[decision-case-900.1]]", "[[decision-case-900.3]]", "[[decision-case-900.4]]", "[[decision-case-900.5]]"]
origin: raw/2026-10-16/1712/ledger.md#case-862
sprint: plugin
created: 2026-10-16
tags: [session, harness, git, plugin]
---

## Context

At /hi of session 1712 the person put off the four hand readings that the brief of session 0342 groups for one install session: `estimate-git-context-offers-git-init` (an empty folder with no git), `estimate-plugin-install-offers-to-install-uv` (a terminal with no `uv`), `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` (an offline install with an empty cache of `uv`) and `estimate-guppi-package-is-ready-after-the-install` (an install with `uv`). Each needs a copy written by `guppi ship --allow-draft` after a librarian's render and an install by hand into an empty project. No step of this session runs such an install.

## Problem

No reading of the four install Estimates runs in this session, since each needs an install by hand into an empty project from a copy built after the librarian's render.

## Deferred

### [[estimate-git-context-offers-git-init]]

Whether /hi outside a git repository offers git init -b main and ends; its hand reading waits for one install session into an empty folder with no git; put off at /hi of session 1712

### [[estimate-plugin-install-offers-to-install-uv]]

Whether /guppi:install offers to install uv where it is missing; its hand reading waits for one install session from a terminal with no uv; put off at /hi of session 1712

### [[estimate-plugin-install-undoes-the-copy-when-uv-sync-fails]]

Whether /guppi:install undoes the copy when uv sync fails; its hand reading waits for one install session offline with an empty cache of uv; put off at /hi of session 1712

### [[estimate-guppi-package-is-ready-after-the-install]]

Whether .guppi is ready after /guppi:install on a machine with uv; its hand reading waits for one install session; put off at /hi of session 1712

## History

- 2026-10-16 created · raw/2026-10-16/1712/ledger.md#case-862
- 2026-10-29 superseded by decision-case-900.1 · [[decision-case-900.1]]
- 2026-10-29 superseded by decision-case-900.3 · [[decision-case-900.3]]
- 2026-10-29 superseded by decision-case-900.4 · [[decision-case-900.4]]
- 2026-10-29 superseded by decision-case-900.5 · [[decision-case-900.5]]
- 2026-10-29 archived · superseded
- 2026-10-29 archived · cleanup
