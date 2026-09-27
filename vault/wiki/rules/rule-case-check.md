---
type: rule
kind: Leaf
purpose: Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them
status: draft
enforcement: hook
implementation_ref: [guppi/casecheck.py, tests/test_casecheck.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-case-check-sends-back-a-faulty-case]]", "[[estimate-case-check-shows-only-the-checked-case]]", "[[estimate-case-check-requires-a-backlog-item-decided-on-its-page]]"]
origin: raw/2026-09-25/1228/ledger.md#case-419.3
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow, session]
---

## Purpose

Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other `given`, `when`, `then`, `tasks` or `ratification` than the ones that passed them; the Case reaches the person in a file the hook writes from the answer that passed them (case 452.1). Until case 419 no script read a Case before its ratification: the hook of `rule-spec-write` checks it only after the person signed, and a fault of the form was found by the person or at pre-spec ([[insight-case-form-chat-form-read-by-no-script]]). The checks are the ones of pre-spec and of the Spec hook, imported, not copied ([[rule-one-judgment-one-implementation]]); the text of the story sections — `context`, `problem` and `recommend` — is not among them, only their presence and their order: the person judges the text (case 449).

## How it works

`uv run guppi casecheck --subagent` on `SubagentStop`. For an answer of `case-guppi` (`agent_type`), it takes as the answer the newest output of the subagent in `agent_transcript_path` that holds a Case heading — the `message` of a `SubagentHandback` call or the text of an assistant message, whichever stands later — or `last_assistant_message` when the transcript is not readable or holds none, and reads the Cases of the answer by the functions of `guppi/ratified.py` that read the chat form, builds the section of each in the Spec in memory as the `Stop` hook of `rule-spec-write` writes it, and runs `prespec.judge` over them, the decision lines of each `ratification` fence standing for the ledger, and those lines with the decision lines of the session's window naming the categories whose schema rule the session changes, whose `create` and `defer` items `judge` does not judge by their keys (case 436.4), the Frontier left to `/pre-spec` but for one check: for each open line of the session's `frontier.md` whose source is `backlog` and each page of its title that carries `deferred_by`, a Case of the answer that, itself or through a sub-case, names the page on a decision line other than a `defer` gets a finding for each Decision of that list when no Case among it and its sub-cases both names the page and carries its `{supersedes}`, by the function of `guppi/prespec.py` that `/pre-spec` runs (case 467.2). It checks besides the order of the sections and the ones the schema requires, and that `ratification` holds one untagged fence of ledger lines and nothing else. Each Case of the answer is stored, with its findings and the time of the store, in `<plan>.checked.json` beside the plan file of the session, a later answer for the same id replacing it. When no Case of the answer has findings, the hook writes the Cases of the answer, as the store holds their text, into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case — the file replaced whole, or only the section of a sub-case the answer holds alone; `case-guppi` itself writes no file (case 452.1). A finding exits 2 with the findings on stderr, and the agent answers again, whatever `stop_hook_active` says: Claude Code sets it on the second fire after a handback with no exit 2 of the hook. A finding for a Case whose text the store already holds with findings is stored and exits 0, so an unchanged answer is not sent back twice. The hooks read stdin as UTF-8 and never raise. An answer with no Case heading, where no earlier output holds one either, is neither checked nor stored; with no plan file of the session nothing is stored.

`uv run guppi casecheck` on `Stop`, beside `guppi ledger`, `guppi ratified` and `guppi context`, which run in parallel. Each Case the reply shows under its heading with at least one of its sections is compared with the Case of the same id in `<plan>.checked.json` in each of its `given`, `when`, `then`, `tasks` and `ratification` that the reply shows, line by line once line ends and trailing spaces are the same; the name of its heading, its `context`, `problem` and `recommend`, and text under the heading outside its sections are not compared (cases 441, 452.2); a parent shown with its sub-cases is compared part by part. A Case the store does not hold, one that differs, one stored with findings, or one with no `SendUserFile` call on `raw/<date>/<hi HHMM>/cases/case-<N>.md` in the turn of the reply, N the id of its top-level Case, exits 2 with the reason and the findings on stderr; the Spec hook imports the same reading of a sending (case 452.2). A heading with no section — the acknowledging reply — a fence tagged `DIFF`, and a deferred decision in the short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and no `when` — are not compared; on the re-fire (`stop_hook_active`) it exits 0.

## History

- 2026-09-25 created · [[decision-case-419.3]]
- 2026-09-25 estimate estimate-case-check-sends-back-a-faulty-case added · [[decision-case-419.3]]
- 2026-09-25 updated: the Stop hook compares the shown Case with the checked one (case 419.4) · [[decision-case-419.4]]
- 2026-09-25 estimate estimate-case-check-shows-only-the-checked-case added · [[decision-case-419.4]]
- 2026-09-26 updated: the check reads the newest output of the subagent that holds a Case, a handback or a text, else last_assistant_message; the loop guard is the store, not stop_hook_active · [[decision-case-434]]
- 2026-09-26 updated: the categories whose schema rule the session changes come from the ratification fences and the session's window (case 436.4) · [[decision-case-436.4]]
- 2026-09-26 updated: the Stop comparison reads only given, when, then, tasks and ratification (case 441.3) · [[decision-case-441.3]]
- 2026-09-27 updated: pre-spec compares the plan with no ratified copy (case 445.2) · [[decision-case-445.2]]
- 2026-09-27 updated: the Purpose says the person judges the text of the story sections, while the check requires them and their order (case 449) · [[decision-case-449]]
- 2026-09-27 updated: the check writes the file of a Case that passed, from the text it stores, and stores the time of the store (case 452.1) · [[decision-case-452.1]]
- 2026-09-27 updated: the Stop comparison covers the sections a reply shows, the prose is not translated, and a shown Case needs a sending of its file in the same turn (case 452.2) · [[decision-case-452.2]]
- 2026-09-27 updated: the answer of case-guppi is checked against the open backlog lines of the Frontier (case 467.2) · [[decision-case-467.2]]
- 2026-09-27 estimate estimate-case-check-requires-a-backlog-item-decided-on-its-page added · [[decision-case-467.2]]
