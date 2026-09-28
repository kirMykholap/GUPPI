---
type: decision
case: "483"
status: current
update: ["[[rule-retro]]", "[[estimate-retro-report-holds-each-fact-once]]"]
origin: raw/2026-09-28/2000/ledger.md#case-483
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness, render]
---

## Context

At `/retro`, the agent writes a report in two parts. The frontier is a numbered list of what still needs an end. The close has three blocks: Ratified, What got done and What is not done. The rule of case 468.1 puts each fact in one part: the frontier holds the text of each item, and What is not done holds each number with its end. The Retro of session 1318 wrote the whole report in one reply. It gave every frontier item its proposed end, and What is not done gave the same ends again. Item 3 read "Result: short defer, Case 481", and What is not done read "3 — defer, Case 481". So `estimate-retro-report-holds-each-fact-once` failed for the second time (L39 of `raw/2026-09-28/1318/ledger.md`). The Render of `rule-retro` never says that a frontier item carries no end. It also asks What is not done for "its ledger line number where it has one", and those lines are not yet written when the report is written. That Retro said so in its own close: "the ledger lines and Case 481 are not written yet".
This Case changes a page and does not create one, so no vault query was needed. The new Criterion keeps every line of the old one word for word except one. The line on What is not done is replaced on purpose: the end becomes the one the agent proposes, and the ledger line number is dropped. Two lines are added: a frontier item names no end, and the close stands in the same reply as the frontier. The frame holds no contradiction. `rule-handoff` and `estimate-handoff-holds-each-fact-once` rebuild What is not done in words from the items and their ends. They name no ledger line number of the Retro close, so this Case leaves them true. Of the other Estimates of `rule-retro`, `estimate-retro-loads` speaks of readings, and `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` and `estimate-retro-red-in-the-baseline-is-not-charged` speak of red checks. None of the three speaks of the layout of the report, so they are not touched. The person chose: the end only in What is not done, one reply without line numbers, a skeleton of the report in the skill, and the Criterion replaced whole.

## Problem

The Retro report writes the end of each frontier item twice: once on the item and once in What is not done. A Case that ends an item is then named in two parts. The Render allows this because it does not forbid an end on an item. It also asks What is not done for ledger line numbers that do not exist when the report is written.

## Given

`rule-retro` — its Render: the sentences on the frontier and on the close
**＋** `.claude/skills/retro/SKILL.md` — the skill rendered from `rule-retro`
**＋** `estimate-retro-report-holds-each-fact-once` — its Criterion replaced whole
**＋** `uv run guppi tail` — the decision lines and ledger lines the report counts from
**＋** `raw/<date>/<hi HHMM>/spec.md` — the unticked boxes the frontier sorts
**＋** `rule-handoff` — rebuilds What is not done from the items and their ends; unchanged

## History

- 2026-09-28 created · raw/2026-09-28/2000/ledger.md#case-483
