---
type: decision
case: "181"
status: current
update: ["[[rule-case-protocol]]"]
supersedes: ["[[decision-case-179]]"]
origin: raw/2026-09-15/2225/ledger.md#case-181
sprint: migration
created: 2026-09-15
tags: [session, workflow, ledger]
---

## Context

`rule-case-protocol` is the rule whose Render enters `CLAUDE.md`. The Render says "eight sections" (case 163); the How it works of the same page says "The six Case sections are not repeated here: they arrive through `case-schema.md`".

## Problem

The text of the page went stale after a contract change — the pattern of `insight-workflow-contract-change-leaves-its-derived-text-stale`. One `replace`; found at the pre-task of session S by `ask-guppi`, not raised as a Case there.

## Given

`rule-case-protocol` is `built`, `deferred_by: [[decision-case-179]]`; its Estimate `estimate-case-protocol-loaded` is `passed` on 167.
**＋** How it works, first sentence: "The six Case sections are not repeated here: they arrive through `@vault/wiki/case-schema.md`, imported by the same file."
**＋** How it works, second paragraph: "`parent: rule-plan-mode` names the Plan Mode MOC of Slice 2, which does not exist yet as a page; the reference dangles until then, on purpose." The page's frontmatter: `parent: "[[rule-claude-md]]"`; `rule-plan-mode` is a live page.
**＋** `{supersedes:case 179}` clears `deferred_by` on the page and archives `decision-case-179`.
**－** The Render does not change: `CLAUDE.md` after `guppi render` equals HEAD.

## History

- 2026-09-16 created · raw/2026-09-15/2225/ledger.md#case-181
