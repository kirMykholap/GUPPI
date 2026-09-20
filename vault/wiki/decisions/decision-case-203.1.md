---
type: decision
case: "203.1"
status: current
create: ["[[estimate-prespec-checks-the-plan]]"]
origin: raw/2026-09-16/1955/ledger.md#case-203.1
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness, tests]
---

## Context

`rule-prespec` is a Leaf, `enforcement: render`, it governs `.claude/skills/pre-task/SKILL.md`; the code of the check is `guppi/pretask.py` (`--check`), its tests `tests/test_pretask.py`. The page carries `## Purpose` and `## Render`, no `## How it works`; one Estimate — `estimate-prespec-reconciles`: a head plus six blocks (73.4, 74, 75.2, 90.2, 103.4, 128), `passed`, its `## Method` "one reading by hand" although half of the blocks are checked by pytest. The Render still names the findings of the old shape: a Leaf `create` without `method`, an `update` without `contract`, two contracts in one Case, a derived slug without `estimate_slug`; `check_form` in the code prints them — five times on the plan of 1651, as the brief knows. Decision 191 deferred the page with the text: pre-task checks the Estimates of the rule named in `context` and asks `ask-guppi` whether an unnamed one speaks of the same thing; the checks of the old model are removed; the changes of 186.2 (the body of a defer is not read) and 198 stand. The vault was asked: `estimate-prespec-checks-the-plan` is free in the vault and in the archive. The Case touches the one Estimate of the rule and creates one.

## Problem

The model of 182 closes the hole with one question: a Case that changes a rule names the Estimate it touches, and pre-task asks whether an unnamed one was left. Today pre-task asks about `contract: changed`, which no longer exists, and prints findings on keys materialize ignores. The one Estimate mixes two promises with different ways to check — the `--check` command (pytest) and the live run of the skill (a reading by hand) — and its Method speaks of one only. The question: which findings `--check` prints by the new model, what the skill asks `ask-guppi`, and how to cut the Estimate along the axis of the promise.

## History

- 2026-09-16 created · raw/2026-09-16/1955/ledger.md#case-203.1
