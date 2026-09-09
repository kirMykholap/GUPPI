---
type: rule
kind: Leaf
purpose: Prevents deferred bugs, tracked outside the vault, from being forgotten at session start
status: draft
enforcement: render
governs: .claude/skills/hi/SKILL.md
render_mode: partial
parent: rule-skill-hi
estimates: [estimate-github-issues-listed]
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness, github]
---

## Purpose

Prevents deferred bugs, tracked outside the vault, from being forgotten at session start.
Issues never become vault pages — GitHub is already their source of truth — so this is the
only way they return.

## How it works

`gh issue list --limit 5`. When `gh` is not authenticated or the repository has no GitHub
remote, `gh`'s own message lands in the context instead of a list, and the skill still
completes: the rule is "the list, or the named reason there is none". As of 2026-09-09
there is no GitHub remote and `gh` is not logged in; the owner chose to leave it so until a
remote exists.

## Render

<!-- rule-github-issues -->
Open issues: !`gh issue list --limit 5 2>&1 || true`
<!-- /rule-github-issues -->

## Estimates

- [[estimate-github-issues-listed]]

## Parent

- [[rule-skill-hi]]

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
