---
type: decision
case: "420.2"
status: current
update: ["[[rule-harness]]", "[[estimate-harness-pipeline]]"]
origin: raw/2026-09-25/1228/ledger.md#case-420.2
sprint: migration
created: 2026-09-25
tags: [harness, workflow]
---

## Context

Every vault page ends with the section `## History`, the record of its changes. Agents read a page whole, its history with it. On the current pages the History is 13% of the text of the vault, 32% on rules and 25% on Estimates. The history costs tokens and also misleads: in session 0051 `frame-guppi` read the order of the `Stop` hooks from the History of `rule-hook-registry` and was wrong (`lesson-hooks-matching-hooks-of-one-event-run-in-parallel`). The person wants the History to stay on the page: in Obsidian the page shows whole. A rule in `.claude/rules/` with `paths:` was weighed. The documentation says it fires on the read of a matching file. But it is text for the model, not a mechanism, and whether it loads inside a subagent is not said. A hook on `Read` works mechanically. The documentation confirms that `PreToolUse` can change the input of a tool through `updatedInput`, that the hooks of `settings.json` fire on the tools of a subagent, and that `PostToolUse` can add `additionalContext`. No live probe has run yet, so it is the first task. On every vault page the History is the last section; no section follows it. `frame-guppi` found that `rule-harness` names in its Purpose the rules outside the pipeline and `estimate-harness-pipeline` reads that list, so the new rule enters it — that is 420.2; and that the docstrings of `guppi/pages.py` and `guppi/cli.py` list the modules and the hook commands — task lines of 420.1. `estimate-hook-registry-rendered` is left alone: it reads only that the file equals the Render.

## Problem

How agents are kept from reading the History of a vault page without an explicit request, the history kept on the page itself.

## Given

`rule-harness` — the MOC of the harness rules; its Purpose names the rules outside the pipeline
**＋** `estimate-harness-pipeline` — its Estimate, which reads that Purpose
**＋** `rule-sprint` — the check that runs between the harness files and the pages in `make lint`
**＋** `rule-page-read` — the rule added among them

## History

- 2026-09-25 created · raw/2026-09-25/1228/ledger.md#case-420.2
