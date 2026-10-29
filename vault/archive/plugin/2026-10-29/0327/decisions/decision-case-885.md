---
type: decision
case: "885"
status: archived
defer: ["[[estimate-spec-write-writes-a-defer]]", "[[estimate-close-commits]]", "[[estimate-clean-branch-writes-the-session-files]]"]
superseded_by: ["[[decision-case-900.2]]"]
origin: raw/2026-10-17/2307/ledger.md#case-885
sprint: plugin
created: 2026-10-17
tags: [hooks, harness, workflow, git, librarian, plugin, ci]
---

## Context

The person put off the items left open at the close of Plan Mode of session 2307. `estimate-spec-write-writes-a-defer` failed, because its by-hand part waits for a short-form defer the person asks for. The `method` of `estimate-close-commits` needs a transcript of an earlier session, which no `/hi` reads. The reading of `estimate-clean-branch-writes-the-session-files` needs an install by hand into an empty folder with no git, with a tag `prod-x.y.z`.

## Problem

No Case of this session sets when these three readings are taken, or changes their methods.

## Deferred

### [[estimate-spec-write-writes-a-defer]]

The Stop hook writes a deferred Case into the Spec as the reply showed it; put off at the close of Plan Mode of session 2307

### [[estimate-close-commits]]

The librarian's run ends in one separate commit of vault and each file the render writes; its method needs a transcript; put off at the close of Plan Mode of session 2307

### [[estimate-clean-branch-writes-the-session-files]]

guppi ship writes the session files of a new project so that its first /hi starts /sprint-open; put off at the close of Plan Mode of session 2307

## History

- 2026-10-26 created · raw/2026-10-17/2307/ledger.md#case-885
- 2026-10-29 superseded by decision-case-900.2 · [[decision-case-900.2]]
- 2026-10-29 archived · superseded
- 2026-10-29 archived · cleanup
