## Case 592 — One function of the ledger module names the person's message and a returned answer

> **context:**
> This Case re-issues Case 590.1 under a new id, with the content the person ratified last, and carries `{supersedes:case 590.1}` on each of its decision lines. The first ratification of 590.1 wrote the line `decision[case 590.1][update][rule-case-check]{ref:rule-case-check}` to the session's ledger at 13:45:27. The Case built again after the findings of `/pre-spec` no longer carries that line, since Case 589.2 takes `rule-case-check`. The ledger hook only appends, so `guppi prespec --check` reports that line with no item in the plan and refuses the exit from Plan Mode. A line is retired only by a `{supersedes:case N}`, which retires every line of Case N and takes Case N out of the plan. The person refused a hand edit of the ledger and chose this re-issue. 590.1 leaves the plan, and 590.2 and 590.3 stay as they were ratified.
> What this Case does. Three hooks read the transcript of the session, and each one needs to know where the person last spoke. The `Stop` check of `rule-case-check` reads the turn of the reply. `turn_of_reply` in `guppi/casecheck.py` starts that turn after the last `user` record that is not `isMeta` and holds more than tool results. The ledger hook of `rule-ledger-write`, and `guppi/onward.py` through it, read the stretch since the person's last message. `own_refusals` in `guppi/ledger.py` starts the stretch after the last `user` record whose `origin.kind` is `human`. `is_prompt` in `guppi/context.py` holds a third copy. A subagent's answer to a `SendMessage` comes back as a `user` record with `origin.kind` `task-notification`. The turn must start there, and the stretch must not. The three tests of the person's message already differ. In the transcript `d08a5ca5-…` of this project, the record of the local command `/clear` has string content, no `origin` and no `isMeta`. `turn_of_reply` takes it as the start of a turn, and the stretch does not. One function of `guppi/ledger.py` now names the kind of a record: the person's message by `human`, a returned answer by `task-notification`. The turn starts at either kind, and the stretch at the person's message alone. The placeholder `rule-turn-start-one-judgment` of the defer of case 586 is deleted, and the delete line keeps `{supersedes:case 586}`. The `## How it works` of `rule-ledger-write` leaves by hand as a one-off task, its mechanism moved into the docstring of `guppi/ledger.py`.
> What `case-guppi` found in the frame, as for 590.1. Over the transcripts of this project in `C:\Users\kir\.claude\projects\c--PROJECTS-GUPPI`, a Grep for a record that holds both `"isMeta":true` and `"origin":{"kind":"human"` printed no match, and neither did a Grep for one that holds both a `tool_result` and that label. So keying on `human` keeps the stretch exactly as it is. The main transcripts outside `subagents/` give different counts: 1431 records of string content not opening with `<`, against 1373 such records carrying `human`. The older transcript `71cd373f-…` holds typed messages with no `origin`, and messages with `origin.kind` `peer`. Neither kind opens a turn under this test, and a transcript with no labelled record is read whole, which makes the check looser and not stricter. A Grep of `turn_of_reply|own_refusals|given_back` over the repository outside `vault/raw/` and `vault/archive/` printed 9 files: `backlog.md`, `guppi/casecheck.py`, `guppi/ledger.py`, `guppi/onward.py`, `estimate-case-build-checks-the-finished-case.md`, `rule-case-check.md`, `rule-turn-start-one-judgment.md`, `decision-case-586.md` and `decision-case-584.md`. The Criteria of `estimate-ledger-write-lifts` and `estimate-retro-onward-sends-the-agent-to-the-handoff` define the stretch by `human` and stand. A Glob of `vault/{wiki,archive}/**/estimate-ledger-write-names-the-kind-of-a-user-record.md` printed no file, so the slug is free. A Grep of `rule-turn-start-one-judgment` over the repository outside `vault/raw/` and `vault/archive/` printed 4 files: `brief.md`, `backlog.md`, `log.md` and `decision-case-586.md`.
> Who names 590.1. The `given` of 590.2 and of 590.3 names the function of `guppi/ledger.py` "as 590.1 sets it". With 590.1 out of the plan, that pointer names a Case that is no longer in the Spec, so both need to name 592 instead. That is a change of their `given` alone. Their `when`, `then`, `tasks` and Criteria do not name 590.1. The person sees the change when the two are shown again, and it is not made by this Case. The parent context of 590 also names 590.1. Case 589.2 names 590.1 in its `given` and tasks, and it should name 592 too. The task lines and the History lines of this Case cite case 592. The content is otherwise that of 590.1 as last ratified.

> **problem:**
> A ledger line of the first ratification of 590.1 has no item in the plan, so the exit from Plan Mode is refused, and only a supersede retires it. The question answered is how 590.1 stays in force without that line: re-issued whole under a new id that supersedes it.

> **recommend:**
> - **How should the two hooks agree on the person's message?**
>   - Recommended: (a) one shared function in `guppi/ledger.py` that names the kind of a user record. The Case check starts its turn at the person's message or a returned answer, and the ledger hook and `guppi/onward.py` start at the person's message only.
>   - Answer: Agreed with the recommendations: (a).
> - **Does the token counter join the shared function?**
>   - Recommended: (a) yes. `guppi/context.py` uses the shared function with the turn boundary, and `is_prompt` is removed.
>   - Answer: Agreed with the recommendations: (a).
> - **Where is the decision recorded?**
>   - Recommended: (a) delete the placeholder, which retires its defer, and record the decision in the docstrings and the How it works of the existing rule pages.
>   - Answer: Agreed with the recommendations: (a).
> - **Which test says that a line is the person's message?**
>   - Recommended: (a) the source label: `origin.kind` `human` is the person's message, and `task-notification` is a returned answer.
>   - Answer: Agreed with the recommendations: (a).
> - **How is it checked that the fix is done?**
>   - Recommended: (a) a new Estimate for the shared test under `rule-ledger-write`, and the Criterion of `estimate-context-size-shown-after-each-reply` rewritten, in two sub-cases.
>   - Answer: Agreed with the recommendations: (a).
> - **Is the Criterion of the round check rewritten too?**
>   - Recommended: (a) a third sub-case replaces the Criterion of `estimate-case-check-refuses-text-before-a-round` whole. Its first line names the turn by the shared function, and every other line is carried word for word.
>   - Answer: (a).
> - **Change**
>   - Asked: at `/pre-spec`, the person chose that `## How it works` leaves the Leaf pages this Case touches. What still holds moves into the docstrings of the modules, and Work Mode removes the section by hand as a one-off task. Case 589 takes the section of `rule-case-check`.
>   - Taken: the update of `rule-ledger-write` carries only its History line, a one-off task removes the section, and the update of `rule-case-check` is dropped.
> - **Change**
>   - Asked: the person refused a hand edit of the ledger, and chose to re-issue 590.1 as Case 592 with `{supersedes:case 590.1}`, with the same content.
>   - Taken: this Case holds the `given`, `when`, `then` and `tasks` of 590.1 as last ratified, each decision line carries `{supersedes:case 590.1}`, and the delete line keeps `{supersedes:case 586}`.

> **given:**
> `estimate-ledger-write-names-the-kind-of-a-user-record` — the new promise of the shared function
> **＋** `rule-ledger-write` — its `## How it works` leaves, by hand
> **＋** `rule-turn-start-one-judgment` — the placeholder of the defer of case 586, deleted
> **＋** `guppi/ledger.py` — the shared function, `own_refusals` and the module docstring
> **＋** `guppi/casecheck.py` — `turn_of_reply`, `given_back` and the module docstring
> **＋** `guppi/onward.py` — reads the stretch by `own_refusals`, unchanged
> **＋** `guppi/context.py` — the token counter, which imports the function as 590.2 sets it
> **＋** `tests/test_ledger.py` — the test over one transcript for every reader
> **＋** `tests/test_casecheck.py` — its `prompt` record
> **＋** `raw/2026-10-02/1202/cases/case-589.md` — removes the `## How it works` of `rule-case-check` into the docstring of `guppi/casecheck.py`
> **＋** `vault/wiki/rules/schema.yaml` — a Leaf drops `## How it works` at its next touch
> **＋** `rule-one-judgment-one-implementation` — the rule the change serves

> **when:**
> The `Stop` hooks `uv run guppi casecheck`, `uv run guppi ledger`, `uv run guppi onward` and `uv run guppi context` run after a reply and read the transcript at `transcript_path`.

> **then:**
> One function of `guppi/ledger.py` names the kind of a `user` record of the transcript: the person's message when its `origin.kind` is `human`, a returned answer when its `origin.kind` is `task-notification`, and neither for any other record.
> **＋** The turn of the reply, which `guppi/casecheck.py` reads for a sending and for a round, is the records after the last record that is the person's message or a returned answer.
> **＋** The stretch, which `guppi/ledger.py` and `guppi/onward.py` read for their own refusals, is the records after the last person's message, and a returned answer does not end it.
> **＋** `guppi/casecheck.py` and `guppi/context.py` import that function, `guppi/onward.py` reaches it through `own_refusals`, and no other module of `guppi/` judges `origin.kind` of a `user` record.
> **＋** One test runs `turn_of_reply`, `own_refusals` and the count of `guppi/context.py` over one transcript that holds a person's message, a returned answer, a local command with no `origin`, a `peer` message, a refusal marked `isMeta` and a tool result, and asserts where each one starts.
> **－** A record with no `origin.kind`, such as that of the local command that clears the session, a record of another kind, a record marked `isMeta` and a tool result open no turn and end no stretch.
> **－** A transcript that holds neither kind of record gives the whole transcript as the turn and as the stretch.

> **tasks:**
> - [ ] `guppi/ledger.py`: one function names the kind of a `user` record by its `origin.kind` (`human`, `task-notification`); `own_refusals` starts the stretch by it; the module docstring and the docstrings say that `guppi/casecheck.py` and `guppi/context.py` import it (case 592)
> - [ ] `guppi/casecheck.py`: `turn_of_reply` starts the turn after the last record that the function of `guppi/ledger.py` names the person's message or a returned answer; `given_back` judges the opener by the same function, and `NOTIFICATION` is imported from `guppi/ledger.py`; the paragraphs "How a round opens" and "A sending" of the module docstring and the docstrings of `turn_of_reply`, `opening_record` and `given_back` say so
> - [ ] `tests/test_casecheck.py`: `prompt` carries `origin.kind` `human`
> - [ ] `tests/test_ledger.py`: a test `test_kind_of_a_user_record_sets_the_turn_and_the_stretch` runs `casecheck.turn_of_reply`, `ledger.own_refusals` and `context.sizes` over one transcript with a person's message, a returned answer, the record of a local command with no `origin`, a `peer` message, a refusal marked `isMeta` and a tool result, and asserts where each one starts; a transcript with neither kind gives the whole of it
> - [ ] `uv run pytest tests/test_ledger.py tests/test_casecheck.py tests/test_onward.py`: green
> - [ ] one-off, by hand: the `## How it works` section of `vault/wiki/rules/rule-ledger-write.md` is removed, heading and text; what of it still holds and the module docstring of `guppi/ledger.py` does not yet say moves into that docstring first, with the shared function of case 592
> - [ ] update `rule-ledger-write`
>   - change: `## How it works left the Leaf, its mechanism in the docstring of guppi/ledger.py; the person's message and a returned answer are named by one function of guppi/ledger.py, which the case check and the token counter import (case 592)`
> - [ ] create `estimate-ledger-write-names-the-kind-of-a-user-record`
>   - type: `estimate`
>   - ref: `rule-ledger-write`
>   - kind: `QA`
>   - purpose: `One function of guppi/ledger.py says whether a user record of a transcript is the person's message or a returned answer, and the case check, the ledger hook, the onward hook and the token counter judge by it, so the turn and the stretch cannot drift apart`
>   - method: `uv run pytest tests/test_ledger.py -k kind; by hand, a Grep of task-notification|"human" over guppi/ that prints guppi/ledger.py alone`
>   - tags: `[session, hooks, harness, ledger]`
> - [ ] delete `rule-turn-start-one-judgment`
>   - impact: `its question is answered by the function of guppi/ledger.py, its docstring and estimate-ledger-write-names-the-kind-of-a-user-record; in vault/wiki/ only brief.md, backlog.md, log.md and decision-case-586 name it, and the supersede of case 586 retires that defer`
> - [ ] read `estimate-ledger-write-names-the-kind-of-a-user-record` — in a later session: `uv run pytest tests/test_ledger.py -k kind`

> **ratification:**
> ```
> - decision[case 592][create][estimate-ledger-write-names-the-kind-of-a-user-record]{ref:rule-ledger-write}{tags:session,hooks,harness,ledger}{supersedes:case 590.1}
> - decision[case 592][update][rule-ledger-write]{ref:rule-ledger-write}{supersedes:case 590.1}
> - decision[case 592][delete][rule-turn-start-one-judgment]{ref:rule-turn-start-one-judgment}{supersedes:case 586}{supersedes:case 590.1}
> ```
