## Case 590 — Make the turn and the stretch share one test of the person's message

> **context:**
> Three hooks read the transcript of the session, and each one needs to know where the person last spoke. The `Stop` check of `rule-case-check` reads the turn of the reply. It looks there for the sending of a Case file and for a round of `case-guppi`. `turn_of_reply` in `guppi/casecheck.py` starts that turn after the last `user` record that is not `isMeta` and holds more than tool results. The ledger hook of `rule-ledger-write`, and `guppi/onward.py` through it, read the stretch since the person's last message, to see whether they have already refused once. `own_refusals` in `guppi/ledger.py` starts the stretch after the last `user` record whose `origin.kind` is `human`. `is_prompt` in `guppi/context.py` holds a third copy: it needs a text block and no tool result. Part of the difference between the hooks is on purpose. A subagent's answer to a `SendMessage` comes back as a `user` record with `origin.kind` `task-notification`. The turn must start there, because `given_back` reads the round from that record. The stretch must not start there, because the person has not written. The weak part is the shared core, the test of the person's message, which each module writes in its own way. They already differ. In the transcript `d08a5ca5-…` of this project, the record of the local command `/clear` has string content, no `origin` and no `isMeta`. `turn_of_reply` takes it as the start of a turn, and the stretch does not. Case 586 (session 2026-10-01/1725) put this question off on the placeholder `rule-turn-start-one-judgment`. The page holds only its purpose and its defer.
> The person chose the recommendations of the first two rounds. There is one function in `guppi/ledger.py` that names the kind of a `user` record. A record is the person's message when its `origin.kind` is `human`, and a returned answer when its `origin.kind` is `task-notification`. The turn starts at either kind. The stretch starts at the person's message alone. `guppi/context.py` joins the function and counts from the start of the turn. The placeholder is deleted. One new Estimate checks the shared function, and the Criterion of `estimate-context-size-shown-after-each-reply` is replaced, since its sentence on the person's last prompt would no longer be true. Two findings of `/pre-spec` changed the Case after that. The first found that `estimate-case-check-refuses-text-before-a-round` defines the turn as the records after the person's last prompt. The person chose to replace its Criterion whole in a sub-case of its own. The second found that the Case added sentences to the `## How it works` of three Leaf pages. `vault/wiki/rules/schema.yaml` says that on a Leaf this section leaves at its next touch, and that the mechanism lives in the docstring of the code. The person chose that the section leaves now. No script removes a section, so Work Mode removes it by hand as a one-off task, as earlier sessions did, and moves what still holds into the docstring of the module. The `update` of each page then carries only its History line. This replaces the How-it-works sentences of the answer to the question on where the decision is recorded. The facts now go into the docstrings alone. Case 589.2 takes the removal of the section of `rule-case-check`, so this Case makes no change on that page. This Case takes `rule-ledger-write` and `rule-context-size`.
> The split. 590.1 is the shared function, the hooks and the new Estimate. 590.2 is the token counter and its Estimate. 590.3 is the round check of the Case check and its Estimate. These are three promises: the boundary of the turn and the stretch, the number the person sees after a reply, and the judgment of how a round is shown can each fail apart.
> What `case-guppi` found in the frame. Several searches ran over the transcripts of this project in `C:\Users\kir\.claude\projects\c--PROJECTS-GUPPI`. A Grep for a record that holds both `"isMeta":true` and `"origin":{"kind":"human"` printed no match, and neither did a Grep for a record that holds both a `tool_result` and that label. So keying on `human` alone keeps the stretch exactly as it is today. The main transcripts outside `subagents/` give different counts: 1431 records of string content not opening with `<`, against 1373 such records carrying `human`. The older transcript `71cd373f-…` holds typed messages of the person with no `origin`, and messages with `origin.kind` `peer`, which come from another Claude session. Under the chosen test, neither kind opens a turn. For a transcript with no labelled record, the Case check then reads the whole transcript as the turn, and finds an earlier sending too, so it is looser there and not stricter. The ledger hook already reads such a transcript that way. The readers judge a transcript that Claude Code writes, not a text of the vault, so no old form needs to be kept beside the new one.
> Other searches were over the vault and the code. A Grep of `turn_of_reply|own_refusals|given_back` over the repository outside `vault/raw/` and `vault/archive/` printed 9 files: `backlog.md`, `guppi/casecheck.py`, `guppi/ledger.py`, `guppi/onward.py`, `estimate-case-build-checks-the-finished-case.md`, `rule-case-check.md`, `rule-turn-start-one-judgment.md`, `decision-case-586.md` and `decision-case-584.md`. The hit in `estimate-case-build-checks-the-finished-case.md` is in its Result and stands, and the Decision pages and the backlog are not read. The hit in `rule-case-check.md` is in its `## How it works`, which Case 589.2 removes. A Grep of `person's last (prompt|message)|turn of the reply|last prompt|origin\.kind` over `vault/wiki/rules/`, `vault/wiki/entities/`, the pages at the root of `vault/wiki/`, `.claude/` and `guppi/` printed 11 files: `backlog.md`, `log.md`, `rule-turn-start-one-judgment.md`, `rule-case-check.md`, `rule-retro-onward.md`, `rule-ledger-write.md`, `rule-context-size.md`, `guppi/casecheck.py`, `guppi/ledger.py`, `guppi/onward.py` and `guppi/context.py`. `rule-retro-onward` speaks of the refusal after the person's last message, and its stretch does not change, so it stands. The hits in `rule-ledger-write.md` and `rule-context-size.md` are in the `## How it works` that leaves.
> The Estimates. The Criteria of `estimate-ledger-write-lifts` and `estimate-retro-onward-sends-the-agent-to-the-handoff` define the stretch by `human` and stand. `estimate-case-check-shows-only-the-checked-case` requires a sending in the turn of the reply without saying where the turn starts, and the new Estimate states the start, so it stands. The purpose and the method of `estimate-context-size-shown-after-each-reply` speak of the change since the last reply and of its test run. The purpose and the method of `estimate-case-check-refuses-text-before-a-round` speak of the round and of its tests. None of them states the old line, so they stand.
> Other checks. The `Stop` hooks in `.claude/settings.json` are `guppi ledger`, `guppi ratified`, `guppi casecheck`, `guppi context`, `guppi onward` and `guppi onward --plan`, and no registration changes. `guppi/ratified.py` reads a sending by time and not by the turn, so it is not touched. Case 589.2 moves what still holds of the `## How it works` of `rule-case-check` into the module docstring of `guppi/casecheck.py`. 590.1 writes the start of the turn into the same docstring, so 590.1 names the case file of 589 in its `given`, and the turn sentence of 590.1 is the one that docstring keeps. A Glob of `vault/{wiki,archive}/**/estimate-ledger-write-names-the-kind-of-a-user-record.md` printed no file, so the slug is free. A Grep of `rule-turn-start-one-judgment` over the repository outside `vault/raw/` and `vault/archive/` printed 4 files: `brief.md`, `backlog.md`, `log.md` and `decision-case-586.md`. None of them is a live page that the delete makes false.
> The notes of the check, and why each change is kept. In 590.2, the old line of the Criterion on N and D is not carried word for word. Its sentence on N is kept, and its sentence on D is replaced with the start of the turn, which is the behaviour this sub-case changes. In 590.3, the old first line is not carried word for word. Its definition of the turn is replaced, and the rest of the line is kept. The other old lines of both are carried word for word. The `－` line of 590.2 on the records that do not move the start of the count shares most of its words with the `－` line of 590.1 on the records that open no turn. The first line of 590.3 shares words with the turn line of 590.1. Each is the same boundary checked from the side of one reader, and each Estimate must read without the Estimate of the shared function, so both stand.
> Not done: a `peer` message from another Claude session opens no turn.

> **problem:**
> The person's message in a transcript is tested in three places in three ways. That breaks `rule-one-judgment-one-implementation`, and it already gives two answers on one record. The question was whether the turn and the stretch are one judgment, how they come to agree, whether the token counter joins, how the record is classified, where the decision is recorded and how it is checked.

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
>   - Asked: at `/pre-spec`, the person chose that `## How it works` leaves the Leaf pages this Case touches, as the schema of rule pages asks. What still holds moves into the docstrings of the modules, and Work Mode removes the section by hand as a one-off task. Case 589 takes the section of `rule-case-check`.
>   - Taken: the How-it-works sentences of `rule-ledger-write` and `rule-context-size` are dropped. Each `update` carries only its History line, and a one-off task removes the section and moves what holds into `guppi/ledger.py` and `guppi/context.py`. The `update` of `rule-case-check` is dropped, and 590.1 names the case file of 589.

### Case 590.1 — One function of the ledger module names the person's message and a returned answer

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
> - [ ] `guppi/ledger.py`: one function names the kind of a `user` record by its `origin.kind` (`human`, `task-notification`); `own_refusals` starts the stretch by it; the module docstring and the docstrings say that `guppi/casecheck.py` and `guppi/context.py` import it (case 590.1)
> - [ ] `guppi/casecheck.py`: `turn_of_reply` starts the turn after the last record that the function of `guppi/ledger.py` names the person's message or a returned answer; `given_back` judges the opener by the same function, and `NOTIFICATION` is imported from `guppi/ledger.py`; the paragraphs "How a round opens" and "A sending" of the module docstring and the docstrings of `turn_of_reply`, `opening_record` and `given_back` say so
> - [ ] `tests/test_casecheck.py`: `prompt` carries `origin.kind` `human`
> - [ ] `tests/test_ledger.py`: a test `test_kind_of_a_user_record_sets_the_turn_and_the_stretch` runs `casecheck.turn_of_reply`, `ledger.own_refusals` and `context.sizes` over one transcript with a person's message, a returned answer, the record of a local command with no `origin`, a `peer` message, a refusal marked `isMeta` and a tool result, and asserts where each one starts; a transcript with neither kind gives the whole of it
> - [ ] `uv run pytest tests/test_ledger.py tests/test_casecheck.py tests/test_onward.py`: green
> - [ ] one-off, by hand: the `## How it works` section of `vault/wiki/rules/rule-ledger-write.md` is removed, heading and text; what of it still holds and the module docstring of `guppi/ledger.py` does not yet say moves into that docstring first, with the shared function of case 590.1
> - [ ] update `rule-ledger-write`
>   - change: `## How it works left the Leaf, its mechanism in the docstring of guppi/ledger.py; the person's message and a returned answer are named by one function of guppi/ledger.py, which the case check and the token counter import (case 590.1)`
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
> - decision[case 590.1][create][estimate-ledger-write-names-the-kind-of-a-user-record]{ref:rule-ledger-write}{tags:session,hooks,harness,ledger}
> - decision[case 590.1][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 590.1][delete][rule-turn-start-one-judgment]{ref:rule-turn-start-one-judgment}{supersedes:case 586}
> ```

### Case 590.2 — The token counter counts the change from the start of the turn

> **given:**
> `estimate-context-size-shown-after-each-reply` — the promise of the size line, its Criterion replaced whole
> **＋** `rule-context-size` — its `## How it works` leaves, by hand
> **＋** `guppi/context.py` — `sizes`, `is_prompt` and the module docstring
> **＋** `guppi/ledger.py` — the function that names the kind of a `user` record, as 590.1 sets it
> **＋** `tests/test_context.py` — the tests of the count
> **＋** `vault/wiki/rules/schema.yaml` — a Leaf drops `## How it works` at its next touch

> **when:**
> The `Stop` hook `uv run guppi context` runs after a reply of the main agent and reads the transcript at `transcript_path`.

> **then:**
> With no error of its own, the hook prints JSON with a `systemMessage` of one line that opens with `context: <N> tokens (<+D> since the last reply)`.
> **＋** N is the sum of the input, cache read, cache creation and output tokens of the last main-agent API call the transcript holds; D is N less the same sum at the last main-agent call before the start of the turn, the last `user` record that the function of `guppi/ledger.py` names the person's message or a returned answer.
> **＋** The records of a subagent (`isSidechain`) are not counted.
> **＋** On the re-fire (`stop_hook_active`), with a transcript it cannot read, or with no call that carries `usage`, the hook prints nothing.
> **－** A record with no `origin.kind`, a record marked `isMeta` and a tool result do not move the call that D is counted from.
> **－** The hook never blocks: it exits 0 in every case.

> **tasks:**
> - [ ] `guppi/context.py`: `is_prompt` is removed; `sizes` takes the start of the turn by the function of `guppi/ledger.py`; the module docstring says that D counts from the last call before the start of the turn (case 590.2)
> - [ ] `tests/test_context.py`: the prompt records carry `origin.kind` `human`; a test `test_d_counts_from_the_start_of_the_turn`: a returned answer starts the count, and a record with no `origin` does not
> - [ ] `uv run pytest tests/test_context.py`: green
> - [ ] one-off, by hand: the `## How it works` section of `vault/wiki/rules/rule-context-size.md` is removed, heading and text; what of it still holds and the module docstring of `guppi/context.py` does not yet say moves into that docstring first, D counted from the start of the turn
> - [ ] update `rule-context-size`
>   - change: `## How it works left the Leaf, its mechanism in the docstring of guppi/context.py; D counts from the start of the turn, named by the function of guppi/ledger.py (case 590.2)`
> - [ ] update `estimate-context-size-shown-after-each-reply`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — D counts from the last call before the start of the turn, the person's message or a returned answer (case 590.2)`
> - [ ] read `estimate-context-size-shown-after-each-reply` — in a later session: `uv run pytest tests/test_context.py`

> **ratification:**
> ```
> - decision[case 590.2][update][estimate-context-size-shown-after-each-reply]{ref:rule-context-size}
> - decision[case 590.2][update][rule-context-size]{ref:rule-context-size}
> ```

### Case 590.3 — The round check reads the turn by the shared function

> **given:**
> `estimate-case-check-refuses-text-before-a-round` — the promise of the round check, its Criterion replaced whole
> **＋** `guppi/casecheck.py` — `round_opening` and `turn_of_reply`
> **＋** `guppi/ledger.py` — the function that names the kind of a `user` record, as 590.1 sets it
> **＋** `tests/test_casecheck.py` — the tests of the round check
> **＋** `.claude/skills/grill-me/SKILL.md` — the question line of a round
> **＋** `.claude/skills/wait-what/SKILL.md` — a re-pitch, not judged
> **＋** `/pre-spec` — the skill after which only the first line is judged
> **＋** `/hi` — the skill whose own questions are not judged
> **＋** `rule-prespec` — sets the text of the loop after the findings of `/pre-spec`

> **when:**
> `Stop` fires after a reply of the main agent, and `uv run guppi casecheck` runs on it.

> **then:**
> When the turn of the reply, the records after the last `user` record that the function of `guppi/ledger.py` names the person's message or a returned answer, holds a round of `case-guppi`, `uv run guppi casecheck` judges how the reply opens. A round is a text that `case-guppi` gives back to an `Agent` or `SendMessage` call and that holds a question line `❓ **Q<n>** - **<title>**:` of `.claude/skills/grill-me/SKILL.md`, no Case heading and no first line `**Fact:**`.
> **＋** While the session's event log holds no `prespec` line of this session after its `hi`, it exits 2 when the main agent wrote text in the turn before its last tool call.
> **＋** It exits 2 when the first line of the reply that is not blank opens neither with `❓ ` nor with a bold label that ends in a colon, the label of the Context paragraph as it stands translated.
> **＋** Its reason on stderr quotes the text that stands before the round and tells the agent to show the round again, opening with its Context paragraph or its first question, with nothing before it.
> **＋** Text after the last question and one horizontal rule is not judged.
> **＋** The check runs in the same `Stop` run as the comparison of shown Cases, and a reply that both refuse gives both reasons.
> **－** Once the session's event log holds a `prespec` line of this session after its `hi`, text before the last tool call of the turn is not judged, and a reply of the loop after the findings of `/pre-spec` is judged only by its first line; in that loop each answer of a `case-guppi` comes back in a turn of its own, and the text the main agent writes there is set by `rule-prespec`.
> **－** A turn with no round of `case-guppi` is not judged: the main agent's own questions in the report of `/pre-spec`, at `/hi` or at a stop of Work Mode, a `**Fact:**` answer shown with the question that stood open, and a re-pitch by `.claude/skills/wait-what/SKILL.md`.
> **－** On the re-fire (`stop_hook_active`) it exits 0, so the round shown again after a refusal is not judged again.
> **－** It stores nothing and writes no file.

> **tasks:**
> - [ ] `tests/test_casecheck.py`: a test `test_round_a_record_with_no_origin_opens_no_turn`: a round given back to an `Agent` call before the record of a local command with no `origin` is still judged in the turn of the reply (case 590.3)
> - [ ] `uv run pytest tests/test_casecheck.py -k round`: green
> - [ ] update `estimate-case-check-refuses-text-before-a-round`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the turn of the reply starts at the person's message or a returned answer, by the function of guppi/ledger.py (case 590.3)`
> - [ ] read `estimate-case-check-refuses-text-before-a-round` — in a later session: `uv run pytest tests/test_casecheck.py -k round`

> **ratification:**
> ```
> - decision[case 590.3][update][estimate-case-check-refuses-text-before-a-round]{ref:rule-case-check}
> ```
