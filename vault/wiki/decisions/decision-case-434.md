---
type: decision
case: "434"
status: current
update: ["[[rule-case-check]]", "[[estimate-case-check-sends-back-a-faulty-case]]"]
origin: raw/2026-09-26/1337/ledger.md#case-434
sprint: migration
created: 2026-09-26
tags: [hooks, harness, workflow, session]
---

## Context

The hook `guppi casecheck --subagent` fires on `SubagentStop`. It checks the answer of `case-guppi` and stores each Case in `<plan>.checked.json` beside the plan file. Then the `Stop` comparison compares the shown Case with the stored one. Today the hook reads only `last_assistant_message`. But the main agent gets the Case now as the `message` of a `SubagentHandback` call, now as a text. At the first dispatch for Case 433, `case-guppi` gave the Case through the handback and ended with a short summary. The hook found no Case, stored nothing, and the `Stop` comparison refused a Case that was built (lesson `lesson-hooks-subagentstop-reads-the-last-text-not-the-handback`).

Probe W28 showed the order of events in Claude Code 2.1.282 (lesson `lesson-hooks-subagentstop-fires-before-and-after-the-handback`). The payload carries `agent_transcript_path` and `stop_hook_active`. When a subagent ends with a text and no handback, `SubagentStop` fires with `stop_hook_active: false`. Then the harness requires a handback, the subagent calls it, may get a reminder about empty output, and writes a text. After that `SubagentStop` fires a second time with `stop_hook_active: true`, though no hook exited 2. In this same session Claude Code once told `case-guppi` that `SubagentHandback` was not available in that run and the report had to be plain text. So a Case comes both ways.

The previous rebuild used rounds and recognised the harness notices by their text. The owner chose a simpler rule. The answer is the newest output of the subagent in the transcript that holds a Case heading: the `message` of a handback call or an assistant text, whichever stands later. A search of handbacks only does not work. If version 1 came by handback, version 2 as text, and a question by handback again, a search of handbacks finds version 1 and overwrites version 2 in the store. A summary with no heading is skipped. If the newest output is a question, the check finds the earlier Case and stores it again. That text is already in the store, so this does no harm. The harness sets `stop_hook_active` without our exit 2, so the store is the guard against a loop: the same text with the same findings is not sent back a second time. Whether an exit 2 with `stop_hook_active: true` reaches the subagent in 2.1.282 is not measured. The reading by hand of the Estimate shows it.

The frame. How it works in `rule-case-check` says three things: the hook reads `last_assistant_message`; an answer with no Case heading is not checked; on the re-fire the hook stores and exits 0. All three become false, and the Case changes all three. The Criterion of `estimate-case-check-sends-back-a-faulty-case` is replaced whole by the `when` and `then` of this Case. Case 436.4, ratified in this session, replaces the same Criterion after 434 and carries the earlier `then` lines of Case 434 word for word. Those lines are now out of date, and 436.4 must be shown again. It is not rebuilt here. `estimate-case-check-shows-only-the-checked-case` is not touched: the comparison reads the reply of the main agent and the store, as before. The Render of `rule-case-build` and `estimate-case-build-writes-the-case` stay true: the agent still answers with a Case alone or a question alone. This is the only hook registered on `SubagentStop` in `.claude/settings.json`. There is one parsing of a JSONL transcript, in `guppi/ledger.py`: the check imports it and does not apply the filter `is_main` to the records of the subagent. The ratification lines stay as they were, so the ledger hook does not write them a second time.

## Problem

The check on `SubagentStop` must store the Case the main agent gets. It comes now through `SubagentHandback`, now as a text, sometimes followed by a summary or a question, and the hook fires twice with `stop_hook_active: true` without our exit 2. The ratified rule reads the wrong output and lets through a faulty Case that came at the second fire.

## Given

`rule-case-check` — the rule of the check and the comparison; its How it works changes
**＋** `estimate-case-check-sends-back-a-faulty-case` — the promise of the check on `SubagentStop`
**＋** `guppi/casecheck.py` — the hook module; `subagent` reads the answer and guards the loop
**＋** `guppi/ledger.py` — the reading of a JSONL transcript, shared with the check
**＋** `guppi/ratified.py` — the reading of the chat form, used as it stands
**＋** `guppi/prespec.py` — `judge`, the checks of pre-spec, used as they stand
**＋** `tests/test_casecheck.py` — the tests of the hook
**＋** `rule-one-judgment-one-implementation` — one reader of a transcript, imported, not copied

## History

- 2026-09-26 created · raw/2026-09-26/1337/ledger.md#case-434
