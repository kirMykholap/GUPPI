---
type: decision
case: "452.2"
status: current
update: ["[[rule-case-check]]", "[[estimate-case-check-shows-only-the-checked-case]]"]
origin: raw/2026-09-27/1255/ledger.md#case-452.2
sprint: migration
created: 2026-09-27
tags: [hooks, harness, workflow, session]
---

## Context

Today `case-guppi` answers with a Case, and the `SubagentStop` hook `guppi casecheck --subagent` checks the Case and stores it in `<plan>.checked.json`. The main agent then retypes the Case whole into the chat, with its name, `context`, `problem` and `recommend` translated into Russian. The `Stop` comparison refuses a retyped showing that differs from the stored answer, but only after the person has seen it. A long Case is a heavy text for the agent to copy and for the person to read on a phone. The person tested `SendUserFile` with `display: render` and read the file on the phone. The person decided the following. The hook writes the answer into `raw/<date>/<hi HHMM>/cases/case-<N>.md` in English, and only when the answer has no findings. The agent sends that file. The chat holds a short Russian text for each Case and sub-case, plus its ledger lines. Rounds stay in the chat. The Spec hook asks for a sending made after the newest store. The `Stop` check refuses a shown Case that has no sending in the same turn. This Case closes C9.
This Case creates no page, so no vault query was run. The frame showed three consequences. The Spec hook no longer needs a showing whole. The `Stop` comparison covers only the sections a reply shows. The sentences of `rule-case-protocol`, `rule-case-check`, `rule-case-build` and `rule-language` that put the Case or its translation in the chat change. `estimate-case-protocol-case-form` is not touched here: Case 449 is built again so that its Criterion names the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` and what the chat shows, and so that it sets the page's `purpose`. `estimate-case-build-writes-the-case` stays, because `case-guppi` still writes no file. `estimate-spec-write-writes-a-defer` stays, because the short form is out of this Case.
Not done: sending the plan file or `spec.md` at pre-spec, the short form, and the acknowledging reply stay as they are. No guard stops the main agent from writing a file under `cases/`.

## Problem

The main agent retypes each built Case into the chat, so a showing can differ from the answer, and a long Case costs the agent and the person a large text. What shows a built Case to the person, and what do the checks require in its place?

## Given

`rule-case-check` — the `How it works` section on `Stop`
**＋** `estimate-case-check-shows-only-the-checked-case` — the promise of the comparison on `Stop`
**＋** `guppi/casecheck.py` — `against_store`, `mechanical_parts`, `stop`, and the new reading of a `SendUserFile` call
**＋** `guppi/ratified.py` — the Spec hook, which imports the comparison and the reading of a sending
**＋** `tests/test_casecheck.py` — the tests of `stop`
**＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file a reply must send
**＋** `rule-one-judgment-one-implementation` — the Spec hook imports the comparison and the reading of a sending

## History

- 2026-09-27 created · raw/2026-09-27/1255/ledger.md#case-452.2
