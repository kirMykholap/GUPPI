## Case 696 — A replaced Case and the answer to a reminder no longer stop Plan Mode

> **context:**
> The `Stop` hook of `rule-prespec-onward` sends the agent on in Plan Mode where no person is needed: after the reply that acknowledges the last ratification, to `/pre-spec`, or after it to the check and the exit. In session 1448 it did not. The lesson `lesson-prespec-onward-a-reminder-answer-ends-the-run` blames the answer to the ledger hook's reminder of a lesson with no mark: that answer held no `LEDGER` block, and the hook speaks only at the end of a reply with one. The transcript of that session shows a cause that came first. At the `Stop` of the reply that ratified cases 695, 692 and 693, the summary record lists `uv run guppi onward --plan` among the hooks that ran, and its only error is the ledger hook's reminder: the hook ran and was silent. By `case_out` of `guppi/onward.py`, a Case is out while its file was written after its last decision line. The event log of 2026-10-07 shows the last `Edit` of `case-691.md` at 01:12:18; the ledger of session 1448 holds the lines of case 691 at 00:43:57; case 695 replaced it by `{supersedes:case 691}` and wrote lines only under its own number. So case 691 stayed out for the rest of Plan Mode. The person chose three things. A Case that a `{supersedes:case N}` mark names is not out (Case 696.1). The hook also speaks at the end of the reply after one that the ledger hook sent back, a reply with no `LEDGER` block too (Case 696.2). The lesson stays as written, and this paragraph records the first cause. Case 696.1 replaces the Criterion of `estimate-prespec-onward-reads-the-decisions-of-the-session`, which sets when a Case is out. Case 696.2 replaces the Criterion of `estimate-prespec-onward-sends-the-agent-on`, which says that an answer with no `LEDGER` block gets no second reason. After the first ratification, the person asked that a reply on a Frontier with no open line under `## Cases` ask whether to go on, because a question came up and the person had to cancel the call of an agent to ask it; the steps after `/pre-spec` stay automatic. So Case 696.2, built again under its own number with the same ledger lines, also drops the sending to `/pre-spec`: before `/pre-spec` the hook stays silent, and its advice on an error of its own no longer names `/pre-spec`. What that reply says is not set here. Case 696.2 sets the `purpose` of `estimate-prespec-onward-sends-the-agent-on` and of `rule-prespec-onward` anew, since both name the sending to `/pre-spec`. The `method` of both Estimates, and the `purpose` of `estimate-prespec-onward-reads-the-decisions-of-the-session`, state no promise that changes, so they stand. `estimate-prespec-onward-tells-the-loop-from-its-end` stands: its `When` is a reply with a `LEDGER` block, and the choice of reason it sets does not change; the answer with no block gets the same reasons through Case 696.2. The lesson is of session 1448, so no decision line carries `{addresses:...}`, as `ratification.md` sets for a lesson whose fix is ratified in another session. The hook reads the mark from the decision lines it already reads, so no reader waits for a writer and no old form is kept. The judgment of which Cases a mark retires already lives in `superseded_in_window` and `retired_by` of `guppi/prespec.py`, which the check of `/pre-spec` uses; by `rule-one-judgment-one-implementation`, Case 696.1 imports it, and the judgment that a parent is retired when each of its sub-cases with a decision line is retired is written once in the same module. `lesson-prespec-parent-of-superseded-sub-cases` names that gap for `check_ratified`; this Case closes it for the hook alone, and `check_ratified` stays as it is. `orchestration.md` sets the answer to the reminder with no block when no Case fixed the cause; that stays true. A Grep `prespec-onward` over `vault/wiki/` with the glob `!**/{log,brief}.md` printed `orchestration.md`, `rules/rule-orchestration.md`, `rules/rule-prespec.md`, `rules/rule-prespec-onward.md`, `rules/rule-plan-mode.md`, `lessons/lesson-case-build-related-cases-same-sentence-missed.md`, `lessons/lesson-prespec-onward-a-reminder-answer-ends-the-run.md`, `estimates/estimate-orchestration-defers-in-one-reply.md`, `estimates/estimate-orchestration-acknowledging-reply.md`, `estimates/estimate-orchestration-shows-the-frontier-after-a-closed-line.md`, `estimates/estimate-prespec-onward-tells-the-loop-from-its-end.md`, `estimates/estimate-retro-onward-sends-the-agent-to-the-handoff.md`, `estimates/estimate-prespec-onward-sends-the-agent-on.md`, `estimates/estimate-prespec-onward-reads-the-decisions-of-the-session.md` and `estimates/estimate-prespec-confirms-the-findings-once.md`. Outside History lines and the Result lines, which record past readings, the hits of `orchestration.md` and `rule-orchestration` say that the hook sends the agent on to `/pre-spec` when no line under `## Cases` is open, and the Criteria of `estimate-orchestration-defers-in-one-reply`, `estimate-orchestration-acknowledging-reply` and `estimate-orchestration-shows-the-frontier-after-a-closed-line` say that the hook sends the agent on after a reply that ends with the Frontier. Case 696.2 makes them false before `/pre-spec`. Case 697 of this session changes those sentences of `rule-orchestration` and the Criteria of those three Estimates, by its file `case-697.md`: before `/pre-spec` each reply on a Frontier with no open line under `## Cases` asks whether to go on, and after `/pre-spec` the hook sends the agent on. That agrees with Case 696.2, which sends no reason before `/pre-spec`. After `/pre-spec`, Case 696.2 gives no reason to a reply with no `LEDGER` block that follows a reply the ledger hook did not send back; such a reply goes on by itself, which is the moment of the replies that Case 697 sets, not of this hook. Case 699 of this session changes what `uv run guppi casecheck` refuses at the same `Stop`; this hook judges the refusals of other hooks as before, so neither Case covers the other. Case 698 changes none of the pages of this Case. The hit of `rule-prespec` sends the agent on after the Cases built again on the findings are ratified, which stays true; the hits of `rule-plan-mode` and the two lessons name the page only; the hit of `estimate-retro-onward-sends-the-agent-to-the-handoff` keeps the judgment of `--plan` apart, and that of `estimate-prespec-confirms-the-findings-once` sends the agent to the check and the exit, both still true. A Grep `case_out|last_decisions|plan_onward|onward import` over `*.py` printed `guppi/ledger.py`, `guppi/onward.py` and `tests/test_onward.py`; the hit in `guppi/ledger.py` imports only `retro_marked` and `retro_moment`, which do not change. A Grep ``to `?/pre-spec`?|call `?/pre-spec`? now|TO_PRESPEC`` over the repository with the glob `!vault/{raw,archive}/**` printed `tests/test_onward.py`, `.claude/skills/hi/SKILL.md`, `guppi/onward.py`, `vault/wiki/orchestration.md`, `vault/wiki/lessons/lesson-prespec-onward-re-ratification-out-after-its-stretch.md`, `vault/wiki/lessons/lesson-session-frontier-closer-appended-box-left-open.md`, `vault/wiki/estimates/estimate-hi-takes-a-conserved-spec.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/rules/rule-prespec-onward.md`, `vault/wiki/estimates/estimate-orchestration-defers-in-one-reply.md`, `vault/wiki/rules/rule-skill-hi.md` and `vault/wiki/estimates/estimate-prespec-onward-sends-the-agent-on.md`. The hits of `tests/test_onward.py`, `guppi/onward.py`, `rule-prespec-onward` and `estimate-prespec-onward-sends-the-agent-on` enter Case 696.2. `rule-skill-hi`, its render and `estimate-hi-takes-a-conserved-spec` have `/hi` go on to `/pre-spec` when it takes a conserved Spec; by the person's choice that stays, and it is no step of this hook. The hits of the two lessons and of the Result of `estimate-orchestration-defers-in-one-reply` record past events. On `Stop`, `.claude/settings.json` registers `uv run guppi ledger`, `uv run guppi ratified`, `uv run guppi casecheck`, `uv run guppi context` and `uv run guppi onward` before this hook; the hook judges their refusals in the transcript as before. The check of this file noted the lines of the old Criteria that the new ones do not carry, and each change is on purpose: in `estimate-prespec-onward-reads-the-decisions-of-the-session`, the line on a Case file with no decision line now excepts a Case that a mark retires, whole or sub-case by sub-case; in `estimate-prespec-onward-sends-the-agent-on`, the conditions under which the hook exits 2 add the `prespec` line and the answer to a reply sent back, the line on a spent refusal sends on that answer too, the line on the reasons drops the call of `/pre-spec`, and the line on an error of its own drops the advice to call `/pre-spec` and sends the reply back only after `/pre-spec`.

> **problem:**
> Plan Mode stops where no person is needed. The hook of `rule-prespec-onward` stays silent for the rest of Plan Mode once a Case replaced under a new number counts as out. It also stays silent after the agent's answer with no `LEDGER` block to a reply that the ledger hook sent back. Before `/pre-spec`, it sends the agent on where the person may still want to speak.

> **recommend:**
> - **A replaced Case keeps the hook silent**
>   - Recommended: (a) the replacement mark settles it: a Case that a ratified line marks as replaced by `{supersedes:case N}` no longer counts as waiting, and the Criterion of `estimate-prespec-onward-reads-the-decisions-of-the-session` is replaced.
>   - Answer: agreed, (a).
> - **The answer to the ledger hook's question ends the run**
>   - Recommended: (a) the hook speaks after that answer too: when the ledger hook sent back the reply that held the block, the hook also speaks at the end of the next reply, with or without a block, at most once after each reply sent back; the Criterion of `estimate-prespec-onward-sends-the-agent-on` is replaced.
>   - Answer: agreed, (a).
> - **The lesson names only the second cause**
>   - Recommended: (a) leave the lesson as written; the `context` of this Case records the first cause.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a reply on a Frontier with no open line under `## Cases` should ask the person whether to go on, since the person had a question and had to cancel the call of an agent; the hook no longer sends the agent to `/pre-spec`, and the steps after `/pre-spec` stay automatic.
>   - Taken: Case 696.2 drops the sending to `/pre-spec` from the hook, from `rule-prespec-onward` and from the Criterion of `estimate-prespec-onward-sends-the-agent-on`; before `/pre-spec` the hook stays silent, and after it the hook sends the agent on as before. What the reply asks is left to Case 697.
> - **Change**
>   - Asked: the findings of `/pre-spec`, which the person agreed to fix as proposed: reuse the judgment of a mark in `guppi/prespec.py` rather than write a second copy; count a parent as not out when each of its sub-cases is retired; before `/pre-spec`, let an error of the hook not send the reply back; keep Case 696.2 consistent with Case 697.2 on a reply with no `LEDGER` block after `/pre-spec`.
>   - Taken: Case 696.1 imports `superseded_in_window` and `retired_by` of `guppi/prespec.py`, writes the judgment of a parent once in that module, and counts a parent whose every sub-case with a decision line is retired as not out. Case 696.2 sends the reply back on an error of its own only after `/pre-spec`, and its rule text says so. The `context` says why the reply with no `LEDGER` block after `/pre-spec` gets no reason.

### Case 696.1 — A replaced Case is not out

> **given:**
> `rule-prespec-onward`: the rule of the hook, whose Purpose says what counts as a Case out.
> **＋** `estimate-prespec-onward-reads-the-decisions-of-the-session`: its Criterion is replaced whole.
> **＋** `guppi/onward.py`: the hook, whose `last_decisions` and `case_out` judge a Case out.
> **＋** `guppi/materialize.py`: its `parse_line` reads the `{supersedes:case N}` marks of a decision line.
> **＋** `guppi/ledger.py`: its `transcript_records` reads the replies of the transcript.
> **＋** `guppi/casecheck.py`: its `moment` reads the time of a record.
> **＋** `tests/test_onward.py`: the tests of the hook.
> **＋** `raw/<date>/<hi HHMM>/cases/`: the folder of the Case files of the session.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of the session.
> **＋** `guppi/prespec.py`: its `superseded_in_window` and `retired_by` judge which Cases a mark retires, the one judgment the check of `/pre-spec` makes.
> **＋** `rule-one-judgment-one-implementation`: one judgment lives in one module.

> **when:**
> The `Stop` hook `uv run guppi onward --plan` judges, at the end of a reply of the main agent, whether a Case is still out.

> **then:**
> A Case N is still out when a file `case-<N>.md` under `raw/<date>/<hi HHMM>/cases/` was written after the last decision line of Case N or of a sub-case of N.
> **＋** The decision lines it reads are the timed lines of `raw/<date>/<hi HHMM>/ledger.md`, the lines inside a `LEDGER` block of each reply of the main agent in the transcript at `transcript_path`, and those of the reply that ended.
> **＋** The replies of the transcript are its `assistant` records of the main agent, read by `transcript_records` of `guppi/ledger.py`, the reading the ledger hook makes. A reply before the person's last message counts like one after it.
> **＋** A line of a reply of the transcript counts at the time of its record, read by `moment` of `guppi/casecheck.py`. A line of the reply that ended counts as written now.
> **＋** A line of `ledger.md` counts at its time on the `hi` date, rolled to the next date when the time runs backwards.
> **＋** So a Case built again and ratified by a reply whose decision lines the ledger already held is not out after that reply, and not at any later reply of the session, after a later message of the person too. This includes the reply that writes again a line the ledger hook refused.
> **＋** A Case N is not out, whenever its file was written, when a `{supersedes:case N}` mark of one of those decision lines, read by `parse_line` of `guppi/materialize.py`, retires N, or when such marks retire each sub-case of N that has a decision line. The marks are judged by `superseded_in_window` and `retired_by` of `guppi/prespec.py`, and the judgment of a parent by one function of the same module. So a Case that the person replaced by a Case under a new number, whole or sub-case by sub-case, does not keep the hook silent.
> **－** Marks that retire some sub-cases of N, but not each one that has a decision line, leave the file `case-<N>.md` judged as before.
> **－** A file of a Case with no decision line is out, unless such a mark retires the Case.
> **－** A record whose time cannot be read counts none of its lines. A transcript that cannot be read leaves `ledger.md` and the reply that ended as the only sources.
> **－** Its own refusals and those of the ledger hook are still judged in the stretch, by `refusals` of `guppi/ledger.py`.

> **tasks:**
> - [ ] update `rule-prespec-onward`
>   - old: `the reply that ended counted as now (cases 597.2, 604)`
>   - new: `` the reply that ended counted as now (cases 597.2, 604), a Case that a `{supersedes:case N}` mark of one of those lines retires, or whose every sub-case with a decision line such marks retire, never out, by the judgment of `guppi/prespec.py` (case 696.1) ``
>   - change: `a Case that a supersedes mark retires, whole or sub-case by sub-case, is not out, so a Case replaced under a new number no longer keeps the hook silent (case 696.1)`
> - [ ] update `estimate-prespec-onward-reads-the-decisions-of-the-session`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a Case that a supersedes mark retires, whole or sub-case by sub-case, is not out`
> - [ ] `guppi/prespec.py`: one function beside `retired_by` tells whether a Case is retired whole — `retired_by` covers N, or it covers each sub-case of N among the decision records given — and its docstring says that `guppi onward --plan` imports it.
> - [ ] `guppi/onward.py`: `case_out` reads the decision records of `ledger.md`, of the replies of the transcript and of the reply that ended by `parse_line`, takes `superseded_in_window` of them, and leaves out the file of each Case that the function of `guppi/prespec.py` finds retired whole; no judgment of a mark is written in this module; the module docstring says so.
> - [ ] `tests/test_onward.py`: after a `prespec` line, a file of Case N written after its last decision line keeps the hook silent; with a decision line of another Case that carries `{supersedes:case N}` in `ledger.md`, in a reply of the transcript or in the reply that ended, the hook sends the agent on; marks that retire both N.1 and N.2, the only sub-cases with lines, send it on; a mark that retires only N.1 of the two keeps it silent.
> - [ ] `uv run pytest tests/test_onward.py`
> - [ ] read `estimate-prespec-onward-reads-the-decisions-of-the-session`

> **ratification:**
> ```
> - decision[case 696.1][update][rule-prespec-onward]{ref:rule-prespec-onward}
> - decision[case 696.1][update][estimate-prespec-onward-reads-the-decisions-of-the-session]{ref:rule-prespec-onward}
> ```

### Case 696.2 — The hook speaks after `/pre-spec` only, and after the answer to a reply sent back

> **given:**
> `rule-prespec-onward`: the rule of the hook, whose `purpose` and Purpose say which replies get its reason.
> **＋** `estimate-prespec-onward-sends-the-agent-on`: its Criterion is replaced whole.
> **＋** `guppi/onward.py`: the hook, whose `plan_onward` and `spent` judge when it speaks.
> **＋** `guppi/ledger.py`: its `refusals` reads the refusals of the ledger hook in the transcript.
> **＋** `tests/test_onward.py`: the tests of the hook.
> **＋** `.claude/settings.json`: registers the hook on `Stop`.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec of the session, whose presence silences the hook.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session, whose open lines under `## Cases` silence the hook.
> **＋** `/pre-spec`: the skill before whose run the hook stays silent.
> **＋** `estimate-prespec-onward-tells-the-loop-from-its-end`: sets the reasons after `/pre-spec`; its Criterion stands.

> **when:**
> The `Stop` hook `uv run guppi onward --plan` receives the payload of the end of a reply of the main agent.

> **then:**
> It exits 2 when all of these hold: the event log of the session's window holds a `hi` of this session and, after it, a `prespec` line of this session; `raw/<date>/<hi HHMM>/spec.md` does not stand; `raw/<date>/<hi HHMM>/frontier.md` holds no open line under `## Cases`; the reply carries a `LEDGER` block, or a refusal of the ledger hook in the stretch follows the reply of the main agent that ended just before it; no Case is still out, as `rule-prespec-onward` judges it; its own refusal is not spent; and the reply does not open with `STOP:`.
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. A refusal of a `Stop` hook is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[<command>]: `. Its own command is `uv run guppi onward --plan`, and the command of the ledger hook is `uv run guppi ledger`.
> **＋** Its own refusal is spent when its last refusal stands in the stretch and no refusal of the ledger hook follows the same reply of the agent or a later one, judged by `refusals` of `guppi/ledger.py`. So after a reply that the ledger hook sent back — a line it refused or held, or its reminder of a lesson with no mark — it sends the agent on again at the end of the next reply: the one that writes a line again, or an answer with no `LEDGER` block, such as the answer that no Case fixed the cause of the lesson.
> **＋** A refusal of another `Stop` hook in the stretch neither silences it nor sends it on again, and neither does `stop_hook_active`.
> **＋** Its reason on stderr sends the agent to the check and the exit, or on with the loop after the findings of `/pre-spec`, as `estimate-prespec-onward-tells-the-loop-from-its-end` sets it.
> **＋** Each reason adds that, when only the person can go on — a Case still out with its `case-guppi`, or a question the person must answer — the agent opens its reply with `STOP:` and asks the person instead.
> **＋** In every other case with no error of its own, it exits 0 and prints nothing. This holds once its own refusal is spent, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript.
> **＋** `.claude/settings.json` registers it on `Stop`, after `uv run guppi onward`.
> **－** With no `prespec` line of this session after its `hi` in the event log, it exits 0 and prints nothing, and its reason never tells the agent to call `/pre-spec`.
> **－** A reply with no `LEDGER` block after a reply that the ledger hook did not send back gets no reason.
> **－** An error of its own after it has read the payload, when a `prespec` line of this session stands after its `hi`, exits 2 with `onward: not checked: <error>` on stderr and the advice, when no Case is left out, to go on with the loop after the findings of `/pre-spec` or to run the check and exit Plan Mode; the advice does not name a call of `/pre-spec`. It does so at most once a stretch, judged by its own refusal in the stretch alone. Before `/pre-spec`, or when it cannot read the `prespec` line, an error of its own exits 0 and does not send the reply back. An empty payload exits 0.
> **－** It counts nothing, calls no model and writes no file and no mark. Its judgment is the marks, the files and their times, the refusals in the transcript and the first word of the reply.
> **－** `uv run guppi onward` without `--plan` keeps its own judgment.

> **tasks:**
> - [ ] update `rule-prespec-onward`
>   - old: `` the agent answers with a reply that writes a line again, a reply that must end; an answer with no `LEDGER` block gets no second reason, since the reason given at the same `Stop` as the ledger hook's already stands (case 686.1) ``
>   - new: `` the agent answers with a reply that writes a line again, a reply that must end, or with a reply that holds no `LEDGER` block, such as the answer that no Case fixed the cause of a lesson, and the hook sends the agent on at the end of that answer too when every other condition holds (cases 686.1, 696.2) ``
>   - old: `` Prevents Plan Mode from stopping where no person is needed: between the reply that acknowledges the last ratification of the Frontier and `/pre-spec`, and between the ratification of the Cases built again on its findings and the exit. ``
>   - new: `` Prevents Plan Mode from stopping where no person is needed after `/pre-spec`: in the loop after its findings, and between the ratification of the Cases built again on them and the exit. Before `/pre-spec` it stays silent, so the person may speak before `/pre-spec` runs (case 696.2). ``
>   - old: `` With no `prespec` line it sends the agent to `/pre-spec`. ``
>   - new: `` With no `prespec` line it stays silent and sends the agent nowhere (case 696.2). ``
>   - old: `` An error of the hook itself after it has read the payload exits 2 with `onward: not checked: <error>` on stderr and the advice to go on, ``
>   - new: `` An error of the hook itself after it has read the payload exits 0 before `/pre-spec`, or when the hook cannot read the `prespec` line, and does not send the reply back (case 696.2); after `/pre-spec` it exits 2 with `onward: not checked: <error>` on stderr and the advice to go on, ``
>   - set: `{purpose: "Prevents Plan Mode from stopping where no person is needed after /pre-spec, in the loop after its findings and between the ratification of the Cases built again on them and the exit"}`
>   - change: `the hook sends the agent on at the end of the answer to a reply the ledger hook sent back, an answer with no LEDGER block too, and no longer sends it to /pre-spec (case 696.2)`
> - [ ] update `estimate-prespec-onward-sends-the-agent-on`
>   - set:
>     ```
>     status: pending
>     purpose: Whether guppi onward --plan, after /pre-spec, refuses the end of a reply that leaves no Case open and no Case waiting in Plan Mode and sends the agent to the check and the exit or on with the loop after its findings, once a stretch and once more after each reply the ledger hook sent back, an answer with no LEDGER block included, judged by the refusals in the transcript whatever stop_hook_active says; silent before /pre-spec, on a reply that opens with STOP:, and otherwise
>     ```
>   - change: `the Criterion replaced whole — silent before /pre-spec, and the answer with no LEDGER block to a reply the ledger hook sent back is sent on too; purpose set anew`
> - [ ] `guppi/onward.py`: `TO_PRESPEC` goes, and `plan_onward` returns no reason with no `prespec` line; `plan_onward` goes on with a reply that holds no `LEDGER` block when a refusal of the ledger hook in the stretch follows the reply of the main agent that ended just before it, read by `refusals` of `guppi/ledger.py`; on its own error, `run` exits 0 unless `prespec_mark` reads a `prespec` line of this session, and its advice names the loop after the findings and the check and the exit, not `/pre-spec`; the module docstring says so.
> - [ ] `tests/test_onward.py`: the tests that expect `onward.TO_PRESPEC` expect exit 0 and no output with no `prespec` line; in `test_loop_the_reply_after_a_reminder_of_the_ledger_hook` the answer with no `LEDGER` block exits 2 too; a reply with no block after a reply the ledger hook did not send back exits 0; the reply after its own reason at that answer exits 0; an error of its own after a `prespec` line exits 2 with advice that names no `/pre-spec`, and before it exits 0.
> - [ ] `uv run pytest tests/test_onward.py tests/test_ledger.py`
> - [ ] read `estimate-prespec-onward-sends-the-agent-on`

> **ratification:**
> ```
> - decision[case 696.2][update][rule-prespec-onward]{ref:rule-prespec-onward}
> - decision[case 696.2][update][estimate-prespec-onward-sends-the-agent-on]{ref:rule-prespec-onward}
> ```
