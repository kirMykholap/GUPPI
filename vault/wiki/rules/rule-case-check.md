---
type: rule
kind: Leaf
purpose: Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or in other words than the ones that passed them
status: draft
enforcement: hook
implementation_ref: [guppi/casecheck.py, tests/test_casecheck.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-case-check-sends-back-a-faulty-case]]", "[[estimate-case-check-shows-only-the-checked-case]]"]
origin: raw/2026-09-25/1228/ledger.md#case-419.3
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow, session]
---

## Purpose

Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or in other words than the ones that passed them. Until case 419 no script read a Case before its ratification: the hook of `rule-spec-write` checks it only after the person signed, and a fault of the form was found by the person or at pre-spec ([[insight-case-form-chat-form-read-by-no-script]]). The checks are the ones of pre-spec and of the Spec hook, imported, not copied ([[rule-one-judgment-one-implementation]]); a count in a story section is not among them — no script tells a count from other words.

## How it works

`uv run guppi casecheck --subagent` on `SubagentStop`. For an answer of `case-guppi` (`agent_type`), it takes as the answer the newest output of the subagent in `agent_transcript_path` that holds a Case heading — the `message` of a `SubagentHandback` call or the text of an assistant message, whichever stands later — or `last_assistant_message` when the transcript is not readable or holds none, and reads the Cases of the answer by the functions of `guppi/ratified.py` that read the chat form, builds the section of each in the Spec in memory as the `Stop` hook of `rule-spec-write` writes it, and runs `prespec.judge` over them, the decision lines of each `ratification` fence standing for the ledger, and those lines with the decision lines of the session's window naming the categories whose schema rule the session changes, whose `create` and `defer` items `judge` does not judge by their keys (case 436.4), the Frontier and the ratified copy left to `/pre-spec`. It checks besides the order of the sections and the ones the schema requires, and that `ratification` holds one untagged fence of ledger lines and nothing else. Each Case of the answer is stored, with its findings, in `<plan>.checked.json` beside the plan file of the session, a later answer for the same id replacing it. A finding exits 2 with the findings on stderr, and the agent answers again, whatever `stop_hook_active` says: Claude Code sets it on the second fire after a handback with no exit 2 of the hook. A finding for a Case whose text the store already holds with findings is stored and exits 0, so an unchanged answer is not sent back twice. The hooks read stdin as UTF-8 and never raise. An answer with no Case heading, where no earlier output holds one either, is neither checked nor stored; with no plan file of the session nothing is stored.

`uv run guppi casecheck` on `Stop`, beside `guppi ledger`, `guppi ratified` and `guppi context`, which run in parallel. Each Case the reply shows under its heading with at least one of its sections is compared with the Case of the same id in `<plan>.checked.json`, line by line once line ends and trailing spaces are the same; a parent shown with its sub-cases is compared part by part. A Case the store does not hold, one that differs, or one stored with findings exits 2 with the reason and the findings on stderr. A heading with no section — the acknowledging reply — a fence tagged `DIFF`, and a deferred decision in the short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and no `when` — are not compared; on the re-fire (`stop_hook_active`) it exits 0.

## History

- 2026-09-25 created · [[decision-case-419.3]]
- 2026-09-25 estimate estimate-case-check-sends-back-a-faulty-case added · [[decision-case-419.3]]
- 2026-09-25 updated: the Stop hook compares the shown Case with the checked one (case 419.4) · [[decision-case-419.4]]
- 2026-09-25 estimate estimate-case-check-shows-only-the-checked-case added · [[decision-case-419.4]]
- 2026-09-26 updated: the check reads the newest output of the subagent that holds a Case, a handback or a text, else last_assistant_message; the loop guard is the store, not stop_hook_active · [[decision-case-434]]
- 2026-09-26 updated: the categories whose schema rule the session changes come from the ratification fences and the session's window (case 436.4) · [[decision-case-436.4]]
