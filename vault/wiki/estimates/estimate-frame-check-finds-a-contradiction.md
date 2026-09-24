---
type: estimate
kind: QA
status: pending
target: "[[rule-frame-check]]"
purpose: frame-guppi reads the frame it is given and names a contradiction of it, or none
method: "by hand: two live dispatches, one whose lines contradict a sentence of a page they name and one whose lines do not; the tokens of each dispatch from its subagent transcript in the estimate line"
origin: raw/2026-09-24/1303/ledger.md#case-391.1
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness]
---

## Criterion

When:
The main agent dispatches `frame-guppi` with the lines of a Case's `given` and a few lines on what the Case changes.

Then:
The agent reads each page and file the lines name, the part a line names where it names one, and the Criterion of each Estimate a named page lists in `estimates`.
**＋** For a Case that adds or changes a hook, it also reads the hooks registered on the same event in `.claude/settings.json` and the rule of each.
**＋** It answers with a `read:` line of the slugs and paths read, then one numbered line per contradiction — the page or file, the sentence, how the change contradicts it, the fix — or the line `none`.
**＋** An Estimate whose Criterion speaks of the thing the change touches, and which the lines do not name, is a contradiction.
**＋** It runs on `model: sonnet` with the tools Read, Grep and Glob.
**－** It does not search the vault by meaning, and does not open the decision pages or the archive.

## History

- 2026-09-24 created · [[decision-case-391.1]]
