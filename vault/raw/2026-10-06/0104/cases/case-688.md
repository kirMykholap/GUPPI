## Case 688 — The checks catch a showing and a ledger line copied wrong after a refusal

> **context:**
> `case-guppi` writes a Case into its file. The main agent sends the file to the person and writes in the chat a heading, a short list and the ledger lines, copied by hand from the summary of `case-guppi`. The `Stop` hook `uv run guppi casecheck` compares those lines with the Case the check of `rule-case-check` stored, and refuses a reply where they differ. It skips its whole run while `stop_hook_active` is set, and Claude Code keeps that flag set from a refusal of any `Stop` hook until the person's next message (case 644.1). So the showing written again after a refusal is not checked, and a second wrong copy reaches the person; only the Spec hook compares it again, at ratification. When the person ratifies, the agent copies the decision lines into its `LEDGER` block again, and `uv run guppi ledger` writes them as they stand: no hook compares them with the stored Case, though `generate` takes the ref and the tags of a `create` from that line. `insight-case-show-built-case-retyped-by-hand` names this. Case 452.4 put the Case into a file the agent sends, and case 662 gave the heading a name line that the check compares with the file, so a whole retyped Case and a heading of the agent's own are gone; the copied ledger lines are what is left.
> The person chose that the check of a showing stops trusting the flag (Q1), that the decision lines of the acknowledging reply come into this Case (Q2), and the recommended answer of each of Q3–Q7. The person also asked whether the agent could show the ledger lines first, in a reply of their own, so that a wrong line is caught before the rest; told that a `Stop` hook runs only at the end of a turn and that a showing is already short, the person dropped it. Case 688.1 makes the whole `Stop` run of `guppi casecheck` judge every reply, its loop guarded by its own refusals in the transcript as the Spec hook guards its own (case 644.8), with a limit of three per Case; it creates `estimate-case-check-judges-a-showing-after-a-refusal`. Cases 688.2 to 688.6 replace the Criterion of each Estimate of `rule-case-check` whose line says the run exits 0 on the re-fire; each new Criterion carries the old lines but that one, and the line of 688.4 on an error that blocks at every `Stop`, which the limit makes false. Their `then` lines share words with each other and with 688.1, since the five Estimates already shared them and each promises a part of one run; each stays its own Estimate. Case 688.7 makes the ledger hook hold a decision line that is not a line of the stored `ratification`, every time, and creates `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`. Case 688.8 sets the Insight `actioned`; `estimate-backlog-renders` checks it, since its Criterion lists an Insight under `## Deferred` only while it is `open`, and it stands.
> The frame. Case 685 changes the same ledger hook at the same `Stop`: it reminds the agent of a lesson with no mark after the hook writes fresh decision lines, and asks for a decision line written again with `{addresses:<lesson slug>}`. Case 688.7 sets that mark aside before it compares, so the line the reminder asks for lands; a held line is not written, so it brings no reminder, as the `when` of Case 685.1 reads. Case 685.1 replaces another sentence of `rule-ledger-write` than Case 688.7 does. In `rule-orchestration` it turns the sentence on where decision lines are written into a list of the acknowledging reply and the reply that answers its reminder; Case 688.7 adds the reply that answers a hold as the third item of that list, by an anchor that starts right after the text Case 685.1 replaces, so the two texts read as one list whichever applies first. At `/pre-spec` both Cases named that reply; by the person's choice the clause of Case 688.7 is the one place that names it, and Case 685.1 drops its mention, so the sentence names it once. Case 688.7 also changes the sentence of the same paragraph that says the ledger hook has written the block when another `Stop` hook refuses, since a held line is not written, and Case 688.9 replaces the Criterion of `estimate-orchestration-acknowledging-reply`, whose line says the same. Case 686 changes another sentence of `rule-orchestration`, and its hook `guppi onward --plan` sends the agent on again after a reply the ledger hook refused, which a hold is. `estimate-prespec-onward-reads-the-decisions-of-the-session` counts the decision lines of each reply in the transcript, a held line too; it stands, since a Case is out only until the person ratifies it, and the reply that carries a held line acknowledges that ratification; the held line is a wrong copy, which the ledger hook refuses at the same `Stop`, so Case 686 needs no change. The Estimates of `rule-ledger-write`, judged against Case 688.7: `estimate-ledger-write-lifts` keeps a refused line out while its refusal holds and tells each refused line once a stretch, which the hold keeps, and stands. `estimate-ledger-write-refuses-a-line-it-cannot-read` says a line `parse_line` cannot read gets no other refusal; Case 688.7 compares only a line `parse_line` reads, so it stands. `estimate-ledger-write-exits-2-on-an-error` covers an error while the hook judges the lines, the comparison included, and stands. `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` speaks of `estimate[...]` lines, `estimate-ledger-write-names-the-kind-of-a-user-record` of the records of the transcript, and `estimate-ledger-write-refuses-a-lesson-without-its-prefix`, `estimate-ledger-write-refuses-a-mark-with-no-decision-line` and `estimate-ledger-write-asks-for-the-mark-of-a-lesson` of lesson lines; none of them speaks of a decision line it would write, and they stand. The `purpose` of `estimate-case-check-shows-only-the-checked-case` and the `purpose` field of `rule-case-check` state that a wrong showing is never shown, which the limit of three makes false, so Cases 688.2 and 688.1 set them anew. `estimate-case-check-sends-back-a-faulty-case` speaks of the `--subagent` run, which keeps its guard; it stands. The store and the ledger lines keep their form, so no reader needs an old form kept.
> The searches. A Grep of `re-fire|stop_hook_active` over `vault/wiki/estimates/` with the glob `estimate-case-check-*.md` printed `estimate-case-check-refuses-a-changed-case-file.md`, `estimate-case-check-sends-back-a-faulty-case.md`, `estimate-case-check-exits-2-on-an-error.md`, `estimate-case-check-refuses-text-before-a-round.md`, `estimate-case-check-refuses-text-outside-the-list.md` and `estimate-case-check-shows-only-the-checked-case.md`; all but the second enter this Case. The same pattern over `vault/wiki/rules/` printed `rule-prespec-onward.md`, `rule-retro-onward.md`, `rule-case-check.md`, `rule-ledger-write.md` and `rule-spec-write.md`: the hits in `rule-case-check` and `rule-ledger-write` are History lines, and the others speak of their own hooks and stand. Over `.claude/` it printed nothing, so no harness file says the check of a showing is silent after a refusal. A Grep of `ledger hook (refuses|holds)|the hook refuses and says so` over `vault/wiki/rules/` printed `rule-ledger-write.md`, a History line, and `rule-orchestration.md`, `rule-ratification.md` and `rule-session.md`, whose sentences name other refusals or a refusal by another hook, and stand; two other sentences of the paragraph of `rule-orchestration` that holds the hit enter Case 688.7. A Grep of `insight-case-show-built-case-retyped-by-hand` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed 7 files: `brief.md`, `backlog.md` and `log.md`, not read; the two lessons, whose `insight` field stays true; and `estimate-synthesis-clusters.md` and `estimate-synthesis-keeps-actioned-by-the-mark.md`, whose hits stand in `## Result`, a past reading. A Glob of `vault/**/*after-a-refusal*` and of `vault/**/*off-the-stored-case*` printed nothing, so both new slugs are free.

> **problem:**
> A showing copied wrong a second time, after the check of a showing refused the first, reaches the person unchecked, and a decision line copied wrong into the acknowledging reply lands in the ledger, where pages are made from it.

> **recommend:**
> - **What this Case changes about the copied showing**
>   - Recommended: (b) the showing check stops trusting the flag: it runs on every reply and guards its loop by its own refusals in the transcript, as the Spec hook does.
>   - Answer: (b). The person added that the person seeing a wrong version first cannot be avoided, and asked whether the agent could show the ledger lines first, in a reply of their own; after the answer that a check runs only at the end of a turn, the person said no separate question on it is needed.
> - **Whether the ledger lines written when you ratify come into this Case**
>   - Recommended: (a) leave them out.
>   - Answer: (b) bring them in.
> - **How often the showing check refuses the same wrong showing**
>   - Recommended: (b) up to three times for the same Case since the person's last message, then let it through with a line that says it is unchecked.
>   - Answer: agreed, (b).
> - **Which parts of the end-of-reply check stop trusting the flag**
>   - Recommended: (a) all four: the comparison, the sending of the file, the layout of a showing and the opening of a round.
>   - Answer: agreed, (a).
> - **How often the ledger hook holds back a wrong decision line**
>   - Recommended: (b) every time it is still wrong.
>   - Answer: agreed, (b).
> - **What the ledger comparison sets aside**
>   - Recommended: (a) an added lesson mark and the lines that put a decision off; a line of a Case with no stored text is held.
>   - Answer: agreed, (a).
> - **How the work is split and checked**
>   - Recommended: (a) sub-cases, a new check for each hook.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec` the sentence of `rule-orchestration` on where decision lines are written named the reply that answers a hold twice, in Case 685.1 and in Case 688.7; the person chose that Case 685.1 drops its mention and Case 688.7 keeps its clause.
>   - Taken: the clause of Case 688.7 stays as written, its anchor apart from the text of Case 685.1, and the context says it is the one place that names that reply.

### Case 688.1 — The check of a showing judges every reply and stops after three refusals

> **given:**
> `rule-case-check`: the rule of the check of a Case and of its showing.
> **＋** `guppi/casecheck.py`: the `Stop` hook `uv run guppi casecheck`.
> **＋** `tests/test_casecheck.py`: the tests of the hook.
> **＋** `guppi/ledger.py`: the reading of the stretch and of the refusals of a `Stop` hook.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the new check of the loop guard.
> **＋** `<plan>.checked.json`: the store of the Cases `case-guppi` built.

> **when:**
> The `Stop` hook `uv run guppi casecheck` of `guppi/casecheck.py` fires at the end of a reply of the main agent in a session with a `hi`, and finds a reason to refuse it: a shown Case that differs from `<plan>.checked.json`, whose file was not sent or differs from the store, a text of the agent's own outside the list of a showing or before a round, or an error of its own after it read the payload.

> **then:**
> The hook judges the reply the same whether `stop_hook_active` is set or not.
> **＋** It gives a reason that names a Case, opening with `case <id>:`, while fewer than three of its own refusals in the stretch hold a reason of that Case, and any other reason while fewer than three of them hold the same reason.
> **＋** It exits 2 while a reason is left to give, with those reasons on stderr.
> **＋** When no reason is left to give, it exits 0 and prints on stderr one line per Case it let through: "casecheck: case <id> shown unchecked after three refusals; the Spec hook compares it at ratification".
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`; its own refusal is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[uv run guppi casecheck]: `, judged by the function of `guppi/ledger.py` that `guppi onward` calls.
> **－** With `stop_hook_active` set and a transcript it cannot read, it exits 0 and prints nothing.
> **－** The run `uv run guppi casecheck --subagent` keeps its own guard, the store.

> **tasks:**
> - [ ] update `rule-case-check`
>   - old: `` the person judges the text (cases 449, 537). ``
>   - new: `` the person judges the text (cases 449, 537). The `Stop` run judges every reply whether `stop_hook_active` is set or not, since Claude Code keeps the flag set from a refusal of any `Stop` hook until the person's next message, and guards its own loop by its refusals in the transcript since that message: a reason of one Case is given at most three times, and a showing still wrong after that passes with a line on stderr, the Spec hook comparing it at ratification (case 688.1). ``
>   - old: `` or with other `given`, `when`, `then`, `tasks` or `ratification` than the ones that passed them, a round ``
>   - new: `` or with other `given`, `when`, `then`, `tasks` or `ratification` than the ones that passed them, while fewer than three refusals of that Case stand since the person's last message, a round ``
>   - set:
>     ```
>     purpose: Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them, while fewer than three refusals of that Case stand since the person's last message, a round of case-guppi from reaching the main agent with a question out of the form of the grill-me template, a round of case-guppi from being shown after a text of the main agent's own, a Case from being shown with a text of the main agent's own outside the list under its heading and its ratification, and a summary of case-guppi from reaching the main agent without the id and the name of the Case it built
>     ```
>   - change: `the Stop run judges every reply whatever stop_hook_active says, a reason of one Case given at most three times a stretch; purpose set anew (case 688.1)`
> - [ ] create `estimate-case-check-judges-a-showing-after-a-refusal`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the Stop run of the Case check judges a reply after a refusal of any Stop hook as before it, gives a reason of one Case at most three times since the person's last message, and then lets the reply through with a line on stderr`
>   - method: `uv run pytest tests/test_casecheck.py — piped payloads and transcripts with refusals of the hook in a temp vault`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `guppi/casecheck.py`: `stop` no longer returns at `stop_hook_active`; it reads its own refusals in the stretch by `refusals` of `guppi/ledger.py` and keeps each reason under the count; the error path of `run` keeps the same count; the docstring says so.
> - [ ] `tests/test_casecheck.py`: tests of a showing refused after a refusal of another `Stop` hook, of the same wrong showing refused three times and let through the fourth time with its stderr line, of two Cases counted apart, of a reason with no Case, of an error repeated, and of the flag with an unreadable transcript; the tests of the re-fire changed to the count.
> - [ ] read `estimate-case-check-judges-a-showing-after-a-refusal`

> **ratification:**
> ```
> - decision[case 688.1][update][rule-case-check]{ref:rule-case-check}
> - decision[case 688.1][create][estimate-case-check-judges-a-showing-after-a-refusal]{ref:rule-case-check}{tags:hooks,harness,workflow}
> ```

### Case 688.2 — The comparison of a showing runs after a refusal

> **given:**
> `estimate-case-check-shows-only-the-checked-case`: its Criterion is replaced whole.
> **＋** `guppi/casecheck.py`: the `Stop` hook `uv run guppi casecheck`.
> **＋** `guppi/ratified.py`: the Spec hook, which imports the comparison.
> **＋** `<plan>.checked.json`: the store of the Cases `case-guppi` built.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a top-level Case of the session.
> **＋** `estimate-case-check-refuses-a-changed-case-file`: the check of the file of a shown Case.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the check of the loop guard.

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections.

> **then:**
> `uv run guppi casecheck` compares each such Case with the Case of the same id in `<plan>.checked.json` in each of its `given`, `when`, `then`, `tasks` and `ratification` that the reply shows, line by line once line ends and trailing spaces are the same.
> **＋** Under the heading of a top-level Case, one `ratification` whose fence holds the ledger lines of its sub-cases, as the list of a showing holds them, is read as the showing of each sub-case whose id a line names: the lines that name that id are compared with the `ratification` of that sub-case in the store, and a stored line that is missing or a line the store lacks is a difference.
> **＋** A section the reply does not show is not compared: a showing of the heading, a short text and `ratification` alone passes when its `ratification` equals the stored text and `raw/<date>/<hi HHMM>/cases/case-<N>.md` equals the store, as `estimate-case-check-refuses-a-changed-case-file` sets it.
> **＋** The name of its heading, its `context`, `problem` and `recommend`, and text under the heading outside its sections are not compared.
> **＋** A Case the store does not hold, a Case that differs in a compared section, a Case stored with findings, a Case whose file differs from the store, or a Case with no `SendUserFile` call on `raw/<date>/<hi HHMM>/cases/case-<N>.md` in the turn of the reply, N the id of its top-level Case, exits 2, the reason and the findings on stderr.
> **＋** A parent shown with its sub-cases is compared part by part, as the store holds each.
> **＋** The Spec hook `guppi/ratified.py` judges a showing by the same comparison, and a sending by the same reading of the transcript, both imported from `guppi/casecheck.py`.
> **－** A heading with no section, as in the acknowledging reply, a fence tagged `DIFF`, and a deferred decision in the short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and no `when` — are not compared and need no sending.
> **－** With `stop_hook_active` set the comparison runs the same, so a Case shown again after a refusal is compared again; its reasons are given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.

> **tasks:**
> - [ ] update `estimate-case-check-shows-only-the-checked-case`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the Stop check refuses a showing of a Case that differs from the answer of case-guppi or that the checks did not pass, after a refusal of any Stop hook too, while fewer than three refusals of that Case stand since the person's last message
>     ```
>   - change: `the Criterion replaced whole — the comparison runs whatever stop_hook_active says, its reasons given as the loop guard sets it; purpose set anew (case 688.2)`
> - [ ] read `estimate-case-check-shows-only-the-checked-case`

> **ratification:**
> ```
> - decision[case 688.2][update][estimate-case-check-shows-only-the-checked-case]{ref:rule-case-check}
> ```

### Case 688.3 — The check of the file of a shown Case runs after a refusal

> **given:**
> `estimate-case-check-refuses-a-changed-case-file`: its Criterion is replaced whole.
> **＋** `guppi/casecheck.py`: the `Stop` hook `uv run guppi casecheck` and its one comparison of a file with the store.
> **＋** `guppi/ratified.py`: the Spec hook, which imports that comparison.
> **＋** `guppi/materialize.py`: the reading of the Cases of a file.
> **＋** `<plan>.checked.json`: the store of the Cases `case-guppi` built.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a top-level Case of the session.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the check of the loop guard.

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, and `uv run guppi casecheck` reads `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and `<plan>.checked.json`.

> **then:**
> The hook reads the Cases of that file by `split_cases` of `guppi/materialize.py` and compares each with the entry of the store under its id alone, line ends and trailing spaces aside.
> **＋** A Case of the file whose text differs from its entry, or that the store does not hold, exits 2 with a reason that names the Case and the file, joined with the other reasons of the hook.
> **＋** The comparison is one function of `guppi/casecheck.py`, which the Spec hook `guppi/ratified.py` imports.
> **－** A heading with no section, a fence tagged `DIFF` and a deferred decision in the short form are not compared, and no file is read for them.
> **－** With `stop_hook_active` set the file is compared the same, as by the other checks of the same run, and its reason is given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.

> **tasks:**
> - [ ] update `estimate-case-check-refuses-a-changed-case-file`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the file is compared whatever stop_hook_active says, its reason given as the loop guard sets it (case 688.3)`
> - [ ] read `estimate-case-check-refuses-a-changed-case-file`

> **ratification:**
> ```
> - decision[case 688.3][update][estimate-case-check-refuses-a-changed-case-file]{ref:rule-case-check}
> ```

### Case 688.4 — An error of the check of a showing blocks at most three times

> **given:**
> `estimate-case-check-exits-2-on-an-error`: its Criterion is replaced whole, its `purpose` set anew.
> **＋** `guppi/casecheck.py`: the `Stop` hook `uv run guppi casecheck` and its `--subagent` run.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the check of the loop guard.

> **when:**
> The `Stop` hook `uv run guppi casecheck` fires, and an exception rises in `guppi/casecheck.py` after the hook has read the payload: while it reads the transcript, the event log or the store, or while it compares a shown Case or reads a sending.

> **then:**
> `guppi casecheck` exits 2. Its stderr holds `casecheck: not checked: <error>` and the advice to show the Case again once the cause is fixed, so the agent sees the error at the end of that reply.
> **＋** While the cause stands, `guppi casecheck` blocks with the same error at each `Stop`, whether `stop_hook_active` is set or not, until three of its own refusals since the person's last message hold that error; then it exits 0, as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.
> **－** An empty or unreadable payload of `guppi casecheck` exits 0 with its line on stderr.
> **－** With `stop_hook_active` set and a transcript it cannot read, `guppi casecheck` exits 0 and prints nothing, so it cannot loop.
> **－** The run `uv run guppi casecheck --subagent` on `SubagentStop` keeps exit 0 with its error on stderr, since a send-back to `case-guppi` is not ended by `stop_hook_active` and would loop.
> **－** A refusal of `guppi casecheck` with no error keeps its own reason on stderr and its exit 2.

> **tasks:**
> - [ ] update `estimate-case-check-exits-2-on-an-error`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the Stop run of the Case check exits 2 with the error on stderr when it raises after reading the payload, at most three times for one error since the person's last message, and exits 0 on an empty payload and in the --subagent run
>     ```
>   - change: `the Criterion replaced whole — an error blocks whatever stop_hook_active says, at most three times a stretch; purpose set anew (case 688.4)`
> - [ ] read `estimate-case-check-exits-2-on-an-error`

> **ratification:**
> ```
> - decision[case 688.4][update][estimate-case-check-exits-2-on-an-error]{ref:rule-case-check}
> ```

### Case 688.5 — The check of how a round opens runs after a refusal

> **given:**
> `estimate-case-check-refuses-text-before-a-round`: its Criterion is replaced whole, its `method` set anew.
> **＋** `guppi/casecheck.py`: the `Stop` hook `uv run guppi casecheck` and its one test of a round.
> **＋** `guppi/ledger.py`: the reading of the person's message and of a returned answer.
> **＋** `/pre-spec`: the skill whose `prespec` line ends the judgment of text before the last tool call.
> **＋** `/hi`: the skill whose `hi` line opens the session's window.
> **＋** `rule-prespec`: the text the main agent writes in the loop after the findings.
> **＋** `.claude/skills/wait-what/SKILL.md`: the re-pitch, which is not judged.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the check of the loop guard.

> **when:**
> `Stop` fires after a reply of the main agent, and `uv run guppi casecheck` runs on it.

> **then:**
> When the turn of the reply, the records after the last `user` record that the function of `guppi/ledger.py` names the person's message or a returned answer, holds a round of `case-guppi`, `uv run guppi casecheck` judges how the reply opens. A round is a text that `case-guppi` gives back to an `Agent` or `SendMessage` call and that `is_round` of `guppi/casecheck.py`, the one test of a round, finds one.
> **＋** While the session's event log holds no `prespec` line of this session after its `hi`, it exits 2 when the main agent wrote text in the turn before its last tool call.
> **＋** It exits 2 when the first line of the reply that is not blank opens neither with `❓ ` nor with a bold label that ends in a colon, the label of the Context paragraph as it stands translated.
> **＋** Its reason on stderr quotes the text that stands before the round and tells the agent to show the round again, opening with its Context paragraph or its first question, with nothing before it.
> **＋** Text after the last question and one horizontal rule is not judged.
> **＋** The check runs in the same `Stop` run as the comparison of shown Cases, and a reply that both refuse gives both reasons.
> **－** Once the session's event log holds a `prespec` line of this session after its `hi`, text before the last tool call of the turn is not judged, and a reply of the loop after the findings of `/pre-spec` is judged only by its first line; in that loop each answer of a `case-guppi` comes back in a turn of its own, and the text the main agent writes there is set by `rule-prespec`.
> **－** A turn with no round of `case-guppi` is not judged: the main agent's own questions in the report of `/pre-spec`, at `/hi` or at a stop of Work Mode, a `**Fact:**` answer shown with the question that stood open, and a re-pitch by `.claude/skills/wait-what/SKILL.md`.
> **－** With `stop_hook_active` set a round shown again after a refusal is judged again, and the reason is given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.
> **－** It stores nothing and writes no file.

> **tasks:**
> - [ ] update `estimate-case-check-refuses-text-before-a-round`
>   - set:
>     ```
>     status: pending
>     method: uv run pytest tests/test_casecheck.py -k round
>     ```
>   - change: `the Criterion replaced whole — a round shown again after a refusal is judged again, its reason given as the loop guard sets it; method set to the tests, which run in the session (case 688.5)`
> - [ ] read `estimate-case-check-refuses-text-before-a-round`

> **ratification:**
> ```
> - decision[case 688.5][update][estimate-case-check-refuses-text-before-a-round]{ref:rule-case-check}
> ```

### Case 688.6 — The check of the layout of a showing runs after a refusal

> **given:**
> `estimate-case-check-refuses-text-outside-the-list`: its Criterion is replaced whole, its `method` set anew.
> **＋** `guppi/casecheck.py`: the `Stop` hook `uv run guppi casecheck` and its judgment of the text before the last tool call.
> **＋** `.claude/settings.json`: the registration of the hook on `Stop`.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the check of the loop guard.

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, not a deferred decision in the short form, and `uv run guppi casecheck` runs on it, as `.claude/settings.json` registers it.

> **then:**
> `uv run guppi casecheck` exits 2 when a line that is not blank stands in the reply before its first Case heading.
> **＋** It exits 2 when a line stands between a Case heading and the next Case heading or the horizontal rule `---` that is not blank, not a list item — a line that opens with `- `, `* ` or a number and `. ` — not a line indented under a list item, and not a line of the `ratification` blockquote, its `> **ratification:**` line and the `>` lines after it.
> **＋** It exits 2 when the main agent wrote text in the turn of the reply before its last tool call, judged by `texts_before_last_call` of `guppi/casecheck.py`, the judgment the check of a round uses.
> **＋** Its reason on stderr quotes the first such text and tells the agent to show the Case again with that text moved after the horizontal rule.
> **＋** The check runs in the same `Stop` run as the comparison of shown Cases with the stored answer and the check of how a round opens, and a reply that more than one of them refuse gives each reason.
> **－** Text after the horizontal rule is not judged.
> **－** A reply with no Case heading that holds a section, the acknowledging reply among them, a fence tagged `DIFF`, and a deferred decision in the short form are not judged.
> **－** With `stop_hook_active` set a Case shown again after a refusal is judged again, and the reason is given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.
> **－** It stores nothing and writes no file.

> **tasks:**
> - [ ] update `estimate-case-check-refuses-text-outside-the-list`
>   - set:
>     ```
>     status: pending
>     method: uv run pytest tests/test_casecheck.py
>     ```
>   - change: `the Criterion replaced whole — a Case shown again after a refusal is judged again, its reason given as the loop guard sets it; method set to the tests, which run in the session (case 688.6)`
> - [ ] read `estimate-case-check-refuses-text-outside-the-list`

> **ratification:**
> ```
> - decision[case 688.6][update][estimate-case-check-refuses-text-outside-the-list]{ref:rule-case-check}
> ```

### Case 688.7 — The ledger hook holds a decision line that the stored Case does not hold

> **given:**
> `rule-ledger-write`: the rule of the ledger hook.
> **＋** `guppi/ledger.py`: the `Stop` hook `uv run guppi ledger`.
> **＋** `tests/test_ledger.py`: the tests of the hook.
> **＋** `guppi/casecheck.py`: the store and its reading of the ledger lines of a `ratification`.
> **＋** `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`: the new check of the hold.
> **＋** `rule-orchestration`: what the agent does when the ledger hook refuses.
> **＋** `vault/raw/2026-10-06/0104/cases/case-685.md`: Case 685, which adds a reminder to the same hook at the same `Stop` and the reply that answers it to `rule-orchestration`.
> **＋** `guppi/materialize.py`: the grammar of a ledger line, whose refusal comes first.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` finds, in a `LEDGER` block of a session with a `hi`, a decision line of a kind other than `defer` that no ledger holds yet.

> **then:**
> The hook compares the line, a `{addresses:<slug>}` block and trailing spaces set aside, with the ledger lines of the `ratification` of the entry stored under its Case id alone in `<plan>.checked.json`, read by the function of `guppi/casecheck.py` by which the `Stop` check of a showing reads them.
> **＋** A line equal to one of them lands as before.
> **＋** A line equal to none of them, a line of a Case the store holds no text for, and a line of a session with no plan file is not written; the other lines of the `Stop` land.
> **＋** For such a line of the reply just finished, the hook exits 2 and prints: "ledger: decision[case <N>] not written — it is not a line of the ratification case-guppi stored for case <N>: copy it again as the summary of case-guppi holds it, alone in a LEDGER block, or send the Case back to its case-guppi when the stored line is wrong."
> **＋** The stderr line is printed only when it does not already stand in a refusal of the hook since the person's last message.
> **＋** A held line is judged again at every `Stop` while it stands in a text of the transcript, and never lands while it differs; a line written again that equals a stored line lands.
> **＋** A line written again with `{addresses:<slug>}` added, as Case 685 asks, lands when the line without the mark equals a stored line.
> **－** A `defer` line, an `estimate` line and a `lesson` line are not compared.
> **－** A line that `parse_line` of `guppi/materialize.py` cannot read, and a line the hook refuses while no live sprint page stands, get that refusal alone and are not compared.
> **－** With `stop_hook_active` set the hook judges the line the same; with the flag set and a transcript it cannot read, the line does not land and the hook prints nothing.

> **tasks:**
> - [ ] update `rule-ledger-write`
>   - old: `` so that the session after the close of a sprint opens the next sprint first (`rule-sprint-close`, case 628.3). ``
>   - new: `` so that the session after the close of a sprint opens the next sprint first (`rule-sprint-close`, case 628.3). It holds a decision line other than a `defer` that is not a line of the `ratification` of the Case `case-guppi` stored for it, a `{addresses:<slug>}` mark set aside, and tells the agent once a stretch to copy it again from the summary of `case-guppi`; the line never lands while it differs, since `generate` takes the ref and the tags of a page from it (case 688.7). ``
>   - set:
>     ```
>     implementation_ref: [guppi/ledger.py, guppi/materialize.py, guppi/gate.py, guppi/casecheck.py, tests/test_ledger.py, tests/test_gate.py, .claude/settings.json]
>     ```
>   - change: `the hook holds a decision line that is not a line of the stored ratification of its Case, every time it differs (case 688.7)`
> - [ ] create `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`
>   - ref: `rule-ledger-write`
>   - kind: `QA`
>   - purpose: `Whether the ledger hook holds a decision line other than a defer that is not a line of the stored ratification of its Case, an addresses mark set aside, tells the agent once a stretch, and writes it once a copy equal to a stored line stands`
>   - method: `uv run pytest tests/test_ledger.py — piped payloads, a session ledger and a store beside a plan file in a temp vault`
>   - tags: `[session, hooks, harness, ledger]`
> - [ ] update `rule-orchestration`
>   - old: `` `- estimate[...]` and `- lesson[...]` lines the moment ``
>   - new: `` and in the reply that answers the ledger hook's hold of a decision line that is not a line of the `ratification` of the Case `case-guppi` stored: that reply holds only a `LEDGER` block with the line written again as the summary of `case-guppi` holds it, or, when the stored line itself is wrong, no block, and the Case goes back to its `case-guppi` to be shown and ratified again (case 688.7); `- estimate[...]` and `- lesson[...]` lines the moment ``
>   - old: `` the ledger hook has written the block at that same `Stop` ``
>   - new: `` the ledger hook has written the block at that same `Stop`, but for a decision line it holds (case 688.7) ``
>   - change: `the reply that answers a held decision line copies it again from the summary of case-guppi, and a held line is not written at the Stop that another hook refuses (case 688.7)`
> - [ ] `guppi/ledger.py`: a function judges each fresh decision line other than a `defer` against the stored `ratification` of its Case, read through `guppi/casecheck.py` inside the function; `run` keeps a held line out and prints its reason by `untold`; the docstring says so.
> - [ ] `tests/test_ledger.py`: tests of a line equal to the store, of a line that differs, of a Case with no stored text, of no plan file, of a line written again equal, of a line with `{addresses:<slug>}` added, of a `defer` line, of a held line from an earlier text, of the reason told once, and of the flag with an unreadable transcript.
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`

> **ratification:**
> ```
> - decision[case 688.7][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 688.7][create][estimate-ledger-write-holds-a-decision-line-off-the-stored-case]{ref:rule-ledger-write}{tags:session,hooks,harness,ledger}
> - decision[case 688.7][update][rule-orchestration]{ref:rule-orchestration}
> ```

### Case 688.8 — The Insight on the retyped showing closes

> **given:**
> `insight-case-show-built-case-retyped-by-hand`: the Insight this Case closes.
> **＋** `rule-insights-schema`: the form of an Insight and of its `actioned` status.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which applies the update and archives the lessons of an `actioned` Insight.
> **＋** `vault/wiki/backlog.md`: the backlog, which lists each `open` Insight.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decision of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `insight-case-show-built-case-retyped-by-hand` stands `actioned`, and its `addressed_by` names the Decision of this Case.
> **＋** Its `clustered` lessons become `archived` by the cascade.
> **＋** `vault/wiki/backlog.md` no longer lists it under `## Deferred`.

> **tasks:**
> - [ ] update `insight-case-show-built-case-retyped-by-hand`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-688.8
>     ```
>   - change: `actioned: the check of a showing judges every reply and stops after three refusals of one Case (case 688.1), and the ledger hook holds a decision line that is not a line of the stored ratification (case 688.7); the heading of a showing comes from the checked Case line (case 662) (case 688.8)`

> **ratification:**
> ```
> - decision[case 688.8][update][insight-case-show-built-case-retyped-by-hand]{ref:insight-case-show-built-case-retyped-by-hand}
> ```

### Case 688.9 — The acknowledging reply keeps a held decision line out of the ledger

> **given:**
> `estimate-orchestration-acknowledging-reply`: its Criterion is replaced whole.
> **＋** `rule-orchestration`: the reply that acknowledges a ratification.
> **＋** `vault/wiki/orchestration.md`: the Render the agent follows.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier the reply shows.
> **＋** `rule-ledger-write`: the ledger hook, which writes the `LEDGER` block.
> **＋** `rule-prespec-onward`: the hook that sends the agent on.
> **＋** `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`: the check of a held decision line.

> **when:**
> The person ratifies a Case, ratifies again a Case shown again after its ratification, or ratifies in one answer Cases shown together, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The reply has four parts, in this order. First, the `LEDGER` block. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** The open `W` lines are folded into one line that lists their ids, and each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` is open, the question which item is next ends the reply; when none is open, the reply ends with the Frontier and asks nothing, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** One reply acknowledges every Case and sub-case ratified in one answer, a Case with its sub-cases or Cases shown together for one ratification: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names their ids, one paragraph `Changes:`, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** The headings and labels are in the language of the chat.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written, but for a decision line the ledger hook holds, as `estimate-ledger-write-holds-a-decision-line-off-the-stored-case` sets it.

> **tasks:**
> - [ ] update `estimate-orchestration-acknowledging-reply`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the LEDGER block stands written after a refusal of another hook, but for a decision line the ledger hook holds (case 688.9)`
> - [ ] read `estimate-orchestration-acknowledging-reply`

> **ratification:**
> ```
> - decision[case 688.9][update][estimate-orchestration-acknowledging-reply]{ref:rule-orchestration}
> ```
