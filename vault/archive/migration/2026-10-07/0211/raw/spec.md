<!-- approved 03:46:00 · session b49412f1 -->

# Spec — session 0211, 2026-10-07

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

```then
update:
- slug: rule-prespec-onward
  replace:
  - old: the reply that ended counted as now (cases 597.2, 604)
    new: the reply that ended counted as now (cases 597.2, 604), a Case that a `{supersedes:case N}` mark of one of those lines retires, or whose every sub-case with a decision line such marks retire, never out, by the judgment of `guppi/prespec.py` (case 696.1)
  change: a Case that a supersedes mark retires, whole or sub-case by sub-case, is not out, so a Case replaced under a new number no longer keeps the hook silent (case 696.1)
- slug: estimate-prespec-onward-reads-the-decisions-of-the-session
  set:
    status: pending
  change: the Criterion replaced whole — a Case that a supersedes mark retires, whole or sub-case by sub-case, is not out
```

```tasks
- [x] update `rule-prespec-onward`
- [x] update `estimate-prespec-onward-reads-the-decisions-of-the-session`
- [x] `guppi/prespec.py`: one function beside `retired_by` tells whether a Case is retired whole — `retired_by` covers N, or it covers each sub-case of N among the decision records given — and its docstring says that `guppi onward --plan` imports it.
- [x] `guppi/onward.py`: `case_out` reads the decision records of `ledger.md`, of the replies of the transcript and of the reply that ended by `parse_line`, takes `superseded_in_window` of them, and leaves out the file of each Case that the function of `guppi/prespec.py` finds retired whole; no judgment of a mark is written in this module; the module docstring says so.
- [x] `tests/test_onward.py`: after a `prespec` line, a file of Case N written after its last decision line keeps the hook silent; with a decision line of another Case that carries `{supersedes:case N}` in `ledger.md`, in a reply of the transcript or in the reply that ended, the hook sends the agent on; marks that retire both N.1 and N.2, the only sub-cases with lines, send it on; a mark that retires only N.1 of the two keeps it silent.
- [x] `uv run pytest tests/test_onward.py`
- [x] read `estimate-prespec-onward-reads-the-decisions-of-the-session`
```

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

```then
update:
- slug: rule-prespec-onward
  replace:
  - old: the agent answers with a reply that writes a line again, a reply that must end; an answer with no `LEDGER` block gets no second reason, since the reason given at the same `Stop` as the ledger hook's already stands (case 686.1)
    new: the agent answers with a reply that writes a line again, a reply that must end, or with a reply that holds no `LEDGER` block, such as the answer that no Case fixed the cause of a lesson, and the hook sends the agent on at the end of that answer too when every other condition holds (cases 686.1, 696.2)
  - old: 'Prevents Plan Mode from stopping where no person is needed: between the reply that acknowledges the last ratification of the Frontier and `/pre-spec`, and between the ratification of the Cases built again on its findings and the exit.'
    new: 'Prevents Plan Mode from stopping where no person is needed after `/pre-spec`: in the loop after its findings, and between the ratification of the Cases built again on them and the exit. Before `/pre-spec` it stays silent, so the person may speak before `/pre-spec` runs (case 696.2).'
  - old: With no `prespec` line it sends the agent to `/pre-spec`.
    new: With no `prespec` line it stays silent and sends the agent nowhere (case 696.2).
  - old: 'An error of the hook itself after it has read the payload exits 2 with `onward: not checked: <error>` on stderr and the advice to go on,'
    new: 'An error of the hook itself after it has read the payload exits 0 before `/pre-spec`, or when the hook cannot read the `prespec` line, and does not send the reply back (case 696.2); after `/pre-spec` it exits 2 with `onward: not checked: <error>` on stderr and the advice to go on,'
  set:
    purpose: Prevents Plan Mode from stopping where no person is needed after /pre-spec, in the loop after its findings and between the ratification of the Cases built again on them and the exit
  change: the hook sends the agent on at the end of the answer to a reply the ledger hook sent back, an answer with no LEDGER block too, and no longer sends it to /pre-spec (case 696.2)
- slug: estimate-prespec-onward-sends-the-agent-on
  set:
    status: pending
    purpose: Whether guppi onward --plan, after /pre-spec, refuses the end of a reply that leaves no Case open and no Case waiting in Plan Mode and sends the agent to the check and the exit or on with the loop after its findings, once a stretch and once more after each reply the ledger hook sent back, an answer with no LEDGER block included, judged by the refusals in the transcript whatever stop_hook_active says; silent before /pre-spec, on a reply that opens with STOP:, and otherwise
  change: the Criterion replaced whole — silent before /pre-spec, and the answer with no LEDGER block to a reply the ledger hook sent back is sent on too; purpose set anew
```

```tasks
- [x] update `rule-prespec-onward`
- [x] update `estimate-prespec-onward-sends-the-agent-on`
- [x] `guppi/onward.py`: `TO_PRESPEC` goes, and `plan_onward` returns no reason with no `prespec` line; `plan_onward` goes on with a reply that holds no `LEDGER` block when a refusal of the ledger hook in the stretch follows the reply of the main agent that ended just before it, read by `refusals` of `guppi/ledger.py`; on its own error, `run` exits 0 unless `prespec_mark` reads a `prespec` line of this session, and its advice names the loop after the findings and the check and the exit, not `/pre-spec`; the module docstring says so.
- [x] `tests/test_onward.py`: the tests that expect `onward.TO_PRESPEC` expect exit 0 and no output with no `prespec` line; in `test_loop_the_reply_after_a_reminder_of_the_ledger_hook` the answer with no `LEDGER` block exits 2 too; a reply with no block after a reply the ledger hook did not send back exits 0; the reply after its own reason at that answer exits 0; an error of its own after a `prespec` line exits 2 with advice that names no `/pre-spec`, and before it exits 0.
- [x] `uv run pytest tests/test_onward.py tests/test_ledger.py`
- [x] read `estimate-prespec-onward-sends-the-agent-on`
```

## Case 697 — On an empty Frontier the agent asks before it goes on to `/pre-spec`

> **context:**
> When the last open line under `## Cases` of the Frontier closes, `orchestration.md` lets the reply end with no question. The reply that acknowledges a ratification and the reply that carries a defer end with the Frontier. A reply that closes a line with no `LEDGER` block calls `/pre-spec` itself (cases 561.6, 561.7, 561.8). Then the `Stop` hook `uv run guppi onward --plan` of `rule-prespec-onward` sends the agent to `/pre-spec` in the same turn, by the reason `TO_PRESPEC` of `guppi/onward.py`. In this session the reply that acknowledged Case 696 closed the last line. The hook sent the agent on, and the person, who had a question, had to cancel the run to ask it. The person chose four things. Before `/pre-spec`, the reply asks whether to go on, in the plain form of the question which item is next, and the agent calls `/pre-spec` only on the person's word. All three kinds of reply that can leave no line open ask the same question. After `/pre-spec` the steps stay automatic: the hook still sends the agent on with the loop after the findings, or to the check and the exit. The reply that takes a conserved Spec at `/hi` goes on to `/pre-spec` with no question, as `rule-skill-hi` sets it, since the person's choice of that Spec is the word to go on. The hook must also stop sending the agent to `/pre-spec`. That change is not in this Case. A Case that replaces a Criterion that another Case of the session replaces is a finding of `check_same_target` of `guppi/prespec.py`, and Case 696.2 replaces the Criterion of `estimate-prespec-onward-sends-the-agent-on`. So, by the person's choice, Case 696 is built again so that its new text of the hook and of that Estimate drops the reason that sends the agent to `/pre-spec`; it joins this batch. This Case changes only what the replies of the agent say, in the Render of `rule-orchestration`, by one sub-case per Estimate: 697.1 the acknowledging reply, 697.2 the reply that closes a line with no ratification and no defer, 697.3 the defer reply, 697.4 the list of questions that keep their own form. Each sub-case replaces the Criterion of its Estimate: `estimate-orchestration-acknowledging-reply`, `estimate-orchestration-shows-the-frontier-after-a-closed-line`, `estimate-orchestration-defers-in-one-reply` and `estimate-orchestration-asks-in-the-grill-me-shape`, whose `－` line lists the questions that keep their own form. Their `purpose` and `method` state no promise that changes, so they stand. The findings of `/pre-spec`, which the person agreed to, brought two changes. The list of questions in their own form became a sub-case of its own, 697.4, since one sub-case replaces one Criterion. The reply of 697.2 with no `LEDGER` block after `/pre-spec` now goes on by itself. The old words had it call `/pre-spec`, which `rule-prespec` forbids after the loop. And Case 696.2 gives no reason to a reply with no `LEDGER` block after a reply that the ledger hook did not send back, so without its own step that reply would stop Plan Mode where no person is needed. The hook runs from the working tree once Work Mode changes it under Case 696, and `orchestration.md` changes at the librarian's render after the session. In between, the hook stays silent before `/pre-spec`, while the old text has the reply end with the Frontier and no question. The turn then passes to the person, who can say to go on. No hook refuses anything there and nothing is lost, so no old form is kept. A Grep `prespec-onward` over `vault/wiki/` with the glob `!**/{log,brief}.md` printed `orchestration.md`, `rules/rule-orchestration.md`, `rules/rule-prespec.md`, `rules/rule-prespec-onward.md`, `rules/rule-plan-mode.md`, `lessons/lesson-case-build-related-cases-same-sentence-missed.md`, `lessons/lesson-prespec-onward-a-reminder-answer-ends-the-run.md`, `estimates/estimate-orchestration-defers-in-one-reply.md`, `estimates/estimate-orchestration-acknowledging-reply.md`, `estimates/estimate-orchestration-shows-the-frontier-after-a-closed-line.md`, `estimates/estimate-prespec-onward-tells-the-loop-from-its-end.md`, `estimates/estimate-retro-onward-sends-the-agent-to-the-handoff.md`, `estimates/estimate-prespec-onward-sends-the-agent-on.md`, `estimates/estimate-prespec-onward-reads-the-decisions-of-the-session.md` and `estimates/estimate-prespec-confirms-the-findings-once.md`. Outside History lines: `orchestration.md`, `rule-orchestration` and the three Estimates of the replies change here. `rule-prespec-onward` and its Estimates are the frame of Case 696. `rule-prespec` and `estimate-prespec-confirms-the-findings-once` say that the hook sends the agent on after the ratification in the loop after `/pre-spec`, which stays true. `estimate-retro-onward-sends-the-agent-to-the-handoff` keeps the judgment of `--plan` apart. `rule-plan-mode` and the two lessons only name the page. A Grep `/pre-spec` over `.claude/` printed `.claude/skills/hi/SKILL.md`, `.claude/skills/pre-spec/SKILL.md` and `.claude/agents/ask-guppi.md`. The `/hi` skill goes on to `/pre-spec` after a conserved Spec is taken, which stands by the person's choice. The `/pre-spec` skill sets the steps after `/pre-spec`, which stay. `ask-guppi.md` names the moment of its run only. A Grep `TO_PRESPEC|Call /pre-spec|call /pre-spec` over `*.py` printed `guppi/onward.py` and `tests/test_onward.py`, the code and the tests of the hook. Case 696 built again changes them, and this Case changes no code.

> **problem:**
> On an empty Frontier, the hook sends the agent on to `/pre-spec` in the same turn as the reply that closed the last line. So the person has no turn to ask a question before `/pre-spec` runs.

> **recommend:**
> - **How the agent stops to ask before `/pre-spec`**
>   - Recommended: (a) the reply asks whether to go on, in the plain form of the question which item is next, and the hook no longer sends the agent to `/pre-spec`; a yes makes the agent call `/pre-spec`, and a question of the person gets an answer and the question again.
>   - Answer: agreed, (a).
> - **Which replies ask the question**
>   - Recommended: (a) all three ask: the acknowledging reply, the defer reply and the reply that closes a line with no ratification; no reply calls `/pre-spec` on its own.
>   - Answer: agreed, (a).
> - **The steps after `/pre-spec`**
>   - Recommended: (a) the steps after `/pre-spec` stay automatic.
>   - Answer: agreed, (a).
> - **How this Case and Case 696 share the hook's text**
>   - Recommended: (a) this Case builds on top of Case 696 and rewrites the hook's promise and rule text again, Case 696 untouched.
>   - Answer: agreed, (a); the check of the Case then showed that this cannot hold, and the question was asked again as "How this Case and Case 696 share the hook's text (asked again)".
> - **When you take a saved plan from an earlier session at `/hi`**
>   - Recommended: (a) the reply that takes a conserved Spec goes on to `/pre-spec` with no question, as `/hi` sets it.
>   - Answer: agreed, (a).
> - **How this Case and Case 696 share the hook's text (asked again)**
>   - Recommended: (a) Case 696 is built again with the change, and this Case changes only the replies.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a finding of `/pre-spec`, agreed to by the person: after `/pre-spec`, a reply with no `LEDGER` block that leaves no line under `## Cases` open goes on by itself, to the check and the exit or with the loop after the findings.
>   - Taken: Case 697.2 says so in its new text of `rule-orchestration` and in its `then`.
> - **Change**
>   - Asked: a finding of `/pre-spec`, agreed to by the person: the Criterion of `estimate-orchestration-asks-in-the-grill-me-shape` gains the question whether to go on to `/pre-spec` in its list of questions that keep their own form.
>   - Taken: Case 697.4 replaces that Criterion and carries the pair of `rule-orchestration` that adds the question to the list, moved from Case 697.1, since one sub-case replaces one Criterion.

### Case 697.1 — The acknowledging reply asks before `/pre-spec`

> **given:**
> `rule-orchestration`: its Render sets the acknowledging reply and the questions that keep their own form.
> **＋** `estimate-orchestration-acknowledging-reply`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `/pre-spec`: the skill that checks the plan.
> **＋** `rule-prespec-onward`: the `Stop` hook that sends the agent on.
> **＋** `vault/raw/2026-10-07/0211/cases/case-696.md`: Case 696, built again, which stops the hook sending the agent to `/pre-spec`.
> **＋** `rule-ledger-write`: the ledger hook, which writes the `LEDGER` block and holds a decision line.
> **＋** `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`: sets when the ledger hook holds a decision line.

> **when:**
> The person ratifies a Case, ratifies again a Case shown again after its ratification, or ratifies in one answer Cases shown together, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The reply has four parts, in this order. First, the `LEDGER` block. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** The open `W` lines are folded into one line that lists their ids, and each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` is open, the question which item is next ends the reply.
> **＋** When none is open before `/pre-spec`, the question whether to go on to `/pre-spec` ends the reply, in the plain form of the question which item is next. The agent calls `/pre-spec` only after the person says to go on. A reply that answers a question of the person instead ends with the same question again.
> **＋** When none is open after `/pre-spec`, the reply ends with the Frontier and asks nothing, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** One reply acknowledges every Case and sub-case ratified in one answer, a Case with its sub-cases or Cases shown together for one ratification: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names their ids, one paragraph `Changes:`, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** The headings and labels are in the language of the chat.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written, but for a decision line the ledger hook holds, as `estimate-ledger-write-holds-a-decision-line-off-the-stored-case` sets it.

```then
update:
- slug: rule-orchestration
  replace:
  - old: 'and, last, the question which item is next, or, when no line under `## Cases` is open, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on (case 561.8)'
    new: 'and, last, the question which item is next, or, when no line under `## Cases` is open, before `/pre-spec` the question whether to go on to `/pre-spec`: the agent calls `/pre-spec` only when the person says to go on, and a reply that answers a question of the person instead ends with the same question again (case 697.1); after `/pre-spec`, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on (case 561.8)'
  change: before /pre-spec the acknowledging reply on an empty Frontier asks whether to go on, and the agent calls /pre-spec only on the person's word (case 697.1)
- slug: estimate-orchestration-acknowledging-reply
  set:
    status: pending
  change: the Criterion replaced whole — on an empty Frontier before /pre-spec the reply asks whether to go on
```

```tasks
- [x] update `rule-orchestration`
- [x] update `estimate-orchestration-acknowledging-reply`
- [x] `uv run guppi render`: `vault/wiki/orchestration.md`
- [x] read `estimate-orchestration-acknowledging-reply`
```

### Case 697.2 — A reply that closes the last line with no ratification asks before `/pre-spec`

> **given:**
> `rule-orchestration`: its Render sets the reply that closes a Frontier line with no ratification and no defer.
> **＋** `estimate-orchestration-shows-the-frontier-after-a-closed-line`: its Criterion is replaced whole.
> **＋** `estimate-orchestration-acknowledging-reply`: sets the form of the Frontier checklist.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `/pre-spec`: the skill that checks the plan.
> **＋** `rule-prespec-onward`: the `Stop` hook that sends the agent on.
> **＋** `rule-skill-hi`: sets the first reply of `/hi` and the taking of a conserved Spec.
> **＋** `rule-prespec`: sets the loop after the findings of `/pre-spec`, the check and the exit.

> **when:**
> After the first reply of `/hi` and before the end of Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the agent closes a line of `raw/<date>/<hi HHMM>/frontier.md` in a reply that carries no ratification and no defer. Examples are an `A` line closed by the person's answer, a `W` line closed by a reading, a `C` line that needs no decision, or an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept`.

> **then:**
> The reply ends with the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist, in the form that `estimate-orchestration-acknowledging-reply` sets.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as they are closed.
> **＋** The open `W` lines are folded into one line that lists their ids.
> **＋** Each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
> **＋** When no line under `## Cases` is open before `/pre-spec`, the question whether to go on to `/pre-spec` follows the Frontier and ends the reply, with a `LEDGER` block or without one. The agent calls `/pre-spec` only after the person says to go on.
> **＋** When no line under `## Cases` is open after `/pre-spec`, no question follows the Frontier. A reply with a `LEDGER` block ends with the Frontier, for the hook of `rule-prespec-onward` to send the agent on. A reply with no `LEDGER` block goes on by itself after the Frontier, to the check and the exit or on with the loop after the findings, as `rule-prespec` sets it.
> **＋** A reply that closes several lines shows one Frontier, after its `LEDGER` block when it carries one.
> **－** The first reply of `/hi` keeps the form that `rule-skill-hi` sets, the lines it closes included.
> **－** The reply that takes a conserved Spec and closes the other lines goes on to `/pre-spec` with no question, as `rule-skill-hi` sets it.
> **－** A line closed in Work Mode or at Retro shows no Frontier.
> **－** The reply that acknowledges a ratification and the reply that carries a defer keep their own form, as `estimate-orchestration-acknowledging-reply` sets it.

```then
update:
- slug: rule-orchestration
  replace:
  - old: 'when no line under `## Cases` is open, it asks nothing: a reply with no `LEDGER` block calls `/pre-spec` after the Frontier, and a reply with a `LEDGER` block ends with the Frontier, for the hook of `rule-prespec-onward` to send the agent on (case 561.6)'
    new: 'when no line under `## Cases` is open, before `/pre-spec` it asks instead whether to go on to `/pre-spec`, with a `LEDGER` block or without one, and the agent calls `/pre-spec` only when the person says to go on, but for the reply that takes a conserved Spec, which goes on to `/pre-spec` with no question, as `rule-skill-hi` sets it, since the person''s choice of that Spec is the word to go on (case 697.2); after `/pre-spec` it asks nothing: a reply with a `LEDGER` block ends with the Frontier, for the hook of `rule-prespec-onward` to send the agent on (case 561.6), and a reply with no `LEDGER` block goes on by itself after the Frontier, to the check and the exit or on with the loop after the findings, as `rule-prespec` sets it (case 697.2)'
  change: before /pre-spec a reply that closes the last Cases line with no ratification asks whether to go on, a conserved Spec taken at /hi excepted (case 697.2)
- slug: estimate-orchestration-shows-the-frontier-after-a-closed-line
  set:
    status: pending
  change: the Criterion replaced whole — on an empty Frontier before /pre-spec the reply asks whether to go on
```

```tasks
- [x] update `rule-orchestration`
- [x] update `estimate-orchestration-shows-the-frontier-after-a-closed-line`
- [x] read `estimate-orchestration-shows-the-frontier-after-a-closed-line`
```

### Case 697.3 — The defer reply asks before `/pre-spec`

> **given:**
> `rule-orchestration`: its Render sets the reply that carries a short-form defer.
> **＋** `estimate-orchestration-defers-in-one-reply`: its Criterion is replaced whole.
> **＋** `estimate-orchestration-shows-the-frontier-after-a-closed-line`: sets the reply that closes a line with no ratification and no defer.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the handoff of the session.
> **＋** `/pre-spec`: the skill that checks the plan.
> **＋** `rule-prespec-onward`: the `Stop` hook that sends the agent on.
> **＋** `rule-spec-write`: the `Stop` hook that writes the short Case into the plan file.

> **when:**
> In Plan Mode, the person asks in the chat to put off a decision: an item of `raw/<date>/<hi HHMM>/frontier.md` whose source is neither the sprint nor the backlog, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
> **＋** The agent writes nothing of the Case into the plan file: the `Stop` hook of `rule-spec-write` writes it.
> **＋** The person's words asking for the defer are its ratification: no question asks for it.
> **＋** The reply shows the Frontier of `raw/<date>/<hi HHMM>/frontier.md` after the Case, with the line of the item closed `[-] … · defer case N`.
> **＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
> **＋** When no line under `## Cases` is open before `/pre-spec`, the question whether to go on to `/pre-spec` follows the Frontier and ends the reply. The agent calls `/pre-spec` only after the person says to go on.
> **＋** When no line under `## Cases` is open after `/pre-spec`, no question follows: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on with the loop after the findings.
> **＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.
> **－** No text follows the question, or the Frontier when no question stands.
> **－** Retro writes no short defer: what it would put off is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
> **－** An item of the sprint put off, its line of `raw/<date>/<hi HHMM>/frontier.md` closed `[-] … · sprint · defer`, and an item of the backlog left as it stands, closed `[-] … · backlog · kept`, are not this moment: they take no short Case and no ledger line, and a reply that closes only such lines is the moment of `estimate-orchestration-shows-the-frontier-after-a-closed-line`.

```then
update:
- slug: rule-orchestration
  replace:
  - old: 'or, when no line under `## Cases` is open, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on to `/pre-spec`, or, after it, on with the loop after its findings (cases 561.7, 686.1)'
    new: 'or, when no line under `## Cases` is open, before `/pre-spec` the question whether to go on to `/pre-spec`, with no text after it, and the agent calls `/pre-spec` only when the person says to go on (case 697.3); after `/pre-spec` no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on with the loop after its findings (cases 561.7, 686.1)'
  change: before /pre-spec the defer reply on an empty Frontier asks whether to go on (case 697.3)
- slug: estimate-orchestration-defers-in-one-reply
  set:
    status: pending
  change: the Criterion replaced whole — on an empty Frontier before /pre-spec the defer reply asks whether to go on
```

```tasks
- [x] update `rule-orchestration`
- [x] update `estimate-orchestration-defers-in-one-reply`
- [x] read `estimate-orchestration-defers-in-one-reply`
```

### Case 697.4 — The question whether to go on keeps its own form

> **given:**
> `rule-orchestration`: its Render lists the questions of the main agent that keep their own form.
> **＋** `estimate-orchestration-asks-in-the-grill-me-shape`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `.claude/skills/grill-me/SKILL.md`: sets the question shape.
> **＋** `/pre-spec`: the skill that checks the plan, whose report holds questions.
> **＋** `/hi`: the skill that opens the session.
> **＋** `rule-spec-capture`: sets the choice between `/work` and `/carry`.

> **when:**
> The main agent puts a question to the person itself, outside a round of `case-guppi`. The question is one of these:
> - a decision it needs in the report of `/pre-spec`;
> - a question at `/hi`;
> - a question at a stop of Work Mode;
> - the question whether another Case of the session is built again after a Case was bounded around a clash with it;
> - at `/pre-spec`, after the `ask-guppi` runs confirm their findings, the question whether each finding not closed is fixed or left.
>
> This is with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> Each such question takes the question shape of `.claude/skills/grill-me/SKILL.md`: its numbered `❓ **Qn** - **<title>**:` line, one `**Now:**` line, the label `**Options:**`, each option on a `🔹` line with one `**After:**` item, and the `➡️` line with the recommended answer.
> **＋** It stands in Russian, and its labels may stand translated.
> **－** The question which Frontier item is next, the question of an open `A` line at `/hi` — the Estimate by slug and its question —, the question that asks for the sign-off of a shown Case, the question whether to go on to `/pre-spec` when no line under `## Cases` is open, and the choice between `/work` and `/carry` of `rule-spec-capture` keep their own form.

```then
update:
- slug: rule-orchestration
  replace:
  - old: the question that asks for the sign-off of a shown Case, and the choice between `/work` and `/carry` keep their own form (case 561.13)
    new: the question that asks for the sign-off of a shown Case, the question whether to go on to `/pre-spec` when no line under `## Cases` is open (case 697.4), and the choice between `/work` and `/carry` keep their own form (case 561.13)
  change: the question whether to go on to /pre-spec on an empty Frontier keeps its own form (case 697.4)
- slug: estimate-orchestration-asks-in-the-grill-me-shape
  set:
    status: pending
  change: the Criterion replaced whole — the question whether to go on to /pre-spec keeps its own form
```

```tasks
- [x] update `rule-orchestration`
- [x] update `estimate-orchestration-asks-in-the-grill-me-shape`
- [x] read `estimate-orchestration-asks-in-the-grill-me-shape`
```

## Case 698 — `case-guppi` reads the saved transcripts in its own permission mode

> **context:**
> Claude Code asks the person before an agent reads a file outside the project folder, unless a rule of the allow list or the permission mode of the agent lets the call run. Today `case-guppi` runs in `permissionMode: acceptEdits`, set by the Render of `rule-case-build`, so it writes its Case file with no prompt. Its reads of this project's saved transcripts, under `~/.claude/projects/c--PROJECTS-GUPPI`, rest on two read rules of the allow list of `rule-permissions`, added by cases 656 and 693. The person was still asked for read permission while `case-guppi` built Case 696 of this session, and said the prompt came after the builder started, so the call that asked was the builder's. The person chose that `case-guppi` runs in the mode `auto`. The modes Claude Code reports are listed in `guppi/event.py`: `default`, `acceptEdits`, `auto`, `dontAsk` and `bypassPermissions`. The archived file of case 645 quotes the subagents page of the Claude Code documentation: in Plan Mode a subagent "runs in the permission mode you set, except `bypassPermissions`". I could not read that documentation, so this Case does not say what `auto` does for a subagent beyond what the vault records.
>
> This Case is built again under its own number, as Case 696 was. As first ratified it removed both read rules; pre-spec found that this puts every read of `case-guppi` there, and the write of its Case file, under the verdict of the classifier of Claude Code. Three pages record that verdict. `insight-hi-skill-substitution-checked-by-a-model-call`, `actioned`, says that when the server of the classifier gives no verdict the call is refused, and that a call a permission rule allows needs no verdict. `lesson-permissions-auto-mode-refuses-a-remote-change-despite-the-chat`, `new`, says that the classifier judges the action against the permission rules of the settings. `rule-skill-hi` says that a `!` command of `/hi` that no rule allows is refused, and that a matching rule needs no classifier. At pre-spec the person chose to keep both read rules beside `auto`: a read they match passes with no verdict, and a call they do not match is judged by `auto` with no prompt to the person. So 698.2 keeps the allow list as it stands and changes only the sentences of `rule-permissions` that name the mode, and the Criterion of `estimate-permissions` checks both paths. The `purpose` and Purpose of `rule-morph`, which say its initiation at install sets the folder name in those rules, stay true. Its update in 698.2 therefore changes no text and carries only a `change` line for its History, which records that the rules it names stay; that keeps the ledger line of 698.2 on `rule-morph` matched by an item of this text. The Frontier line A1 of this session, which asks whether a search of a subagent under the read rules runs with no prompt, stands, and the new `method` of `estimate-permissions` keeps its question. The write of the Case file has no allow rule, so in `auto` it is judged by the classifier; whether it still runs with no prompt is the person's word.
>
> Whether a call asks is the person's word, since only the person can see a prompt (`lesson-permissions-reading-taken-by-the-agent-who-cannot-see-the-prompt`). A rendered file changes at the librarian's render after the session, so the new mode holds from the next session. The person chose that the promise sits in `estimate-permissions`, which stays `pending` until the person's word in that session; its `method` is set anew, and like the method case 693 set, it waits for a later session, which pre-spec reports (case 670.4). Case 698.1 replaces the Criterion of `estimate-case-build-writes-the-case`, whose line on the mode names `acceptEdits`. It is written whole under `sections`, with that line alone changed, and the page goes back to `pending`. Its `purpose` and `method` do not name the mode and stand. The check of the file notes lines of the old Criteria that the new ones do not carry; each is the line on the mode, changed on purpose, and in `estimate-permissions` the line of the Case-file write, which leaves the mode and the guard to 698.1 and adds that a read no rule matches runs with no prompt.
>
> What the frame showed, by these searches:
> - A Grep `acceptEdits` over the repository, with the glob `!vault/{raw,archive}/**`, printed `guppi/event.py`, `tests/test_event.py`, `vault/wiki/estimates/estimate-case-protocol-case-form.md`, `vault/wiki/estimates/estimate-case-build-writes-the-case.md`, `vault/wiki/estimates/estimate-event-log-records.md`, `vault/wiki/rules/rule-case-build.md`, `vault/wiki/log.md`, `.claude/agents/case-guppi.md`, `vault/wiki/rules/rule-permissions.md` and `vault/wiki/estimates/estimate-permissions.md`. `guppi/event.py`, `tests/test_event.py` and `estimate-event-log-records` list the modes in which `/hi` is refused, and they stand. The hit in `estimate-case-protocol-case-form` is in its Result, a record of a past reading, and it stands. I did not read `log.md`. The rest enter the Case.
> - A Grep `permissionDecision|allow list|without asking|permission prompt|permissionMode` over `vault/wiki/rules/` printed `rule-permissions.md`, `rule-morph.md` and `rule-case-build.md`, and over `.claude/` printed `.claude/agents/case-guppi.md`. The pattern does not match `rule-skill-hi`, which sets, through `allowed-tools`, whether the `!` commands of `/hi` ask; this Case does not touch those commands, and no other rule that the search printed sets whether a call of `case-guppi` asks.
> - A Grep `PROJECTS-GUPPI|projects|permissionMode|Read\(` over `tests/` printed nothing. The JSON cases of `tests/test_render.py` use an allow list of their own, so no test changes.
>
> Cases 696, 697 and 699 of this session change none of the pages of this Case.

> **problem:**
> `case-guppi` still makes the client ask the person for permission when it reads this project's saved transcripts, though two read rules of the allow list were meant to stop that.

> **recommend:**
> - **Whose prompt the Case removes**
>   - Recommended: (a) the builder only, and say whether the prompt came before or after the builder started.
>   - Answer: (a); the prompt came after the builder started.
> - **Which mode the builder runs in**
>   - Recommended: (a) `auto`.
>   - Answer: (a).
> - **Whether the two read rules stay in the allow list**
>   - Recommended: (a) keep both rules.
>   - Answer: (b), remove both rules.
> - **Which check says the change is done**
>   - Recommended: (a) the promise sits in `estimate-permissions`; `estimate-case-build-writes-the-case` names the new mode and goes back to pending.
>   - Answer: (a).
> - **Change**
>   - Asked: at pre-spec, a call that no permission rule allows is judged by the classifier, which refuses it when its server gives no verdict; the person chose to keep both read rules beside `auto`.
>   - Taken: both read rules stay in the allow list; a read they match passes with no verdict, and a call they do not match is judged by `auto` with no prompt; the update of `rule-morph` changes no text and keeps only a `change` line, and the Case is built again under its own number.

### Case 698.1 — `case-guppi` runs in the mode `auto`

> **given:**
> `rule-case-build`: the rule whose Render is the agent file of `case-guppi`.
> **＋** `.claude/agents/case-guppi.md`: the agent file, which sets the permission mode of `case-guppi`.
> **＋** `estimate-case-build-writes-the-case`: the check of the agent file, whose Criterion is replaced whole.
> **＋** `rule-spec-reconcile`: its guard keeps the writes of `case-guppi` inside `cases/`.

> **when:**
> The main agent dispatches `case-guppi` from `.claude/agents/case-guppi.md`, in a session after the render of `rule-case-build`.

> **then:**
> `.claude/agents/case-guppi.md` sets `permissionMode: auto`.
> **＋** Its model, effort, tools and skills stay as they are.
> **＋** The guard of `rule-spec-reconcile` refuses a write of `case-guppi` outside `cases/` in that mode too.
> **－** The mode of `.claude/agents/case-guppi.md` sets no mode of the main agent.

```then
update:
- slug: rule-case-build
  replace:
  - old: 'permissionMode: acceptEdits'
    new: 'permissionMode: auto'
  change: case-guppi runs in permissionMode auto instead of acceptEdits, so that a call no rule of the allow list matches is judged by that mode with no prompt (case 698)
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
      **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.

      Then:
      `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
      **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
      **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
      **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
      **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
      **＋** When no fork is open, it writes the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
      **＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file; a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, a Case with sub-cases included; then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
      **＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
      **＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
      **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
      **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write and Edit, and `permissionMode: auto`, so it writes its file with no prompt while the session is in Plan Mode.
      **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
      **－** It does not write the whole Case again to fix a finding or make a change.
      **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
      **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
      **－** It writes no file but the file of its Case, and no ledger line.
  change: the Criterion replaced whole — case-guppi runs in permissionMode auto; the other lines stand (case 698)
```

```tasks
- [x] update `rule-case-build`
- [x] update `estimate-case-build-writes-the-case`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] read `estimate-case-build-writes-the-case`
```

### Case 698.2 — The read rules stay beside the mode `auto`

> **given:**
> `rule-permissions`: the rule of the allow list, whose Render is the allow list of `.claude/settings.json`.
> **＋** `estimate-permissions`: the check of the allow list and of the prompts of `case-guppi`, whose Criterion is replaced whole.
> **＋** `.claude/settings.json`: the rendered settings that hold the allow list.
> **＋** `tests/test_render.py`: its JSON case fixes the shape of the rendered block.
> **＋** `.claude/agents/case-guppi.md`: the agent file of `case-guppi`, which sets its permission mode.
> **＋** `rule-spec-reconcile`: its guard keeps the writes of `case-guppi` inside `cases/`.
> **＋** `rule-morph`: the draft rule of the initiation at install, whose History records that the read rules it names stay.
> **＋** `~/.claude/projects/c--PROJECTS-GUPPI`: the folder of this project's saved transcripts, outside the repository.
> **＋** `Read(~/.claude/projects/c--PROJECTS-GUPPI)` and `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`: the read rules for that folder and for what lies inside it.
> **＋** `vault/raw/**`: the folders of the sessions, which hold their working files.
> **＋** `cases/`: the folder of a session that holds the files of its Cases.
> **＋** `vault/wiki/brief.md`: the brief, which `/carry` rewrites.
> **＋** `vault/wiki/`: the live pages of the vault.

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`; or `case-guppi` writes the file of its Case.
> **＋** Or an agent of the session, `case-guppi` among them, calls Read, Grep or Glob with the folder `~/.claude/projects/c--PROJECTS-GUPPI` itself as its path, or a path under it.
> **＋** Or `case-guppi` calls Read, Grep or Glob on a path outside the project that no rule of the allow list names.

> **then:**
> The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, Edit and Write for `vault/wiki/brief.md`, `Read(~/.claude/projects/c--PROJECTS-GUPPI)` and `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`.
> **＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the shape of the block.
> **＋** Whether the client asked is seen by the person only; the agent's reply does not tell an approved call from one not asked.
> **＋** The client's prompt is the person's word: the reading line records whether the client asked, from the person, never from the agent.
> **＋** In Plan Mode the client asks before every edit of the main agent outside the plan file, allow list or not.
> **＋** A Read, Grep or Glob whose path is `~/.claude/projects/c--PROJECTS-GUPPI` itself or a path under it runs with no prompt, in Plan Mode too.
> **＋** `case-guppi` writes the file of its Case with no prompt in Plan Mode, and its Read, Grep or Glob on a path outside the project that no rule of the allow list names runs with no prompt to the person.
> **－** A prompt in Plan Mode on an edit of the main agent, approved by the person, is not a finding and not a `failed`.
> **－** `deny` and `ask` are empty; nothing else under `vault/wiki/` is allowed, no path under `cases/` is on the allow list, no other path outside the project is on it, and no Edit or Write rule names `~/.claude/projects/c--PROJECTS-GUPPI`.

```then
update:
- slug: rule-permissions
  replace:
  - old: '`case-guppi` writes it in the mode `permissionMode: acceptEdits` of its agent file,'
    new: '`case-guppi` writes it in the mode `permissionMode: auto` of its agent file (case 698),'
  - old: and whether a search there still asks is the person's word (case 656).
    new: 'and whether a search there still asks is the person''s word (case 656). A call of `case-guppi` that these rules do not match is judged by its mode `permissionMode: auto`, with no prompt to the person, and a call they match needs no verdict of the classifier of Claude Code, which refuses a call when its server gives none (case 698).'
  change: case-guppi runs in permissionMode auto; the read rules of the saved transcripts stay, and a call they do not match is judged by that mode (case 698)
- slug: estimate-permissions
  set:
    status: pending
    method: the allow list of the rendered .claude/settings.json against the Criterion, and the JSON case of tests/test_render.py; the live probe is the person's word on the client's prompt at a Write of work.md in Work Mode, recorded in the estimate line; the live probe of the transcripts and of the mode of case-guppi is the person's word on the client's prompt, in a session after the librarian's render, at a Grep of a subagent whose path is the folder ~/.claude/projects/c--PROJECTS-GUPPI itself and at one whose path is a file under it, at the Write of the Case file of case-guppi, and at a Read of case-guppi on a path outside the project that no rule names, recorded in the estimate line — never the agent's, which cannot see the prompt; the Estimate stays pending until the person gives that word
  change: the Criterion replaced whole — case-guppi runs in permissionMode auto beside the read rules of the saved transcripts, and a call they do not match is judged by that mode with no prompt (case 698)
- slug: rule-morph
  change: the read rules of rule-permissions that its initiation at install names stay, beside the mode auto of case-guppi; no text changes (case 698)
```

```tasks
- [x] update `rule-permissions`
- [x] update `estimate-permissions`
- [x] update `rule-morph`
- [x] `uv run guppi render`: `.claude/settings.json`
- [x] read `estimate-permissions`
```

## Case 699 — A layout fault of a shown round or Case is told at the next message, not shown again

> **context:**
> The `Stop` run `uv run guppi casecheck` of `rule-case-check` judges each reply of the main agent when the reply ends. By then the person has already read the reply. When the reply shows a round of `case-guppi` and its first line opens neither with `❓ ` nor with a bold label that ends in a colon, or when the agent wrote a text of its own after the round came back, the run exits 2 (`round_opening` of `guppi/casecheck.py`). `orchestration.md` then requires a reply that shows the whole round again (case 561.9). A Case shown with a text of the agent's own before its heading or outside its list is refused the same way (`showing_layout`, case 611), and it is shown again (case 452.4). In this session the agent showed the rounds of Cases 697 and 698 in one list under a heading of its own, `### Case 697 — C4`. The run refused the reply, and the person read seven questions twice, though the questions were right. The lesson `lesson-orchestration-batch-rounds-headed-by-their-case` finds the cause: `rule-orchestration` numbers the questions of a batch `<Case id>.Q<n>`, but sets no mark where the round of each Case begins. The person chose four things. A layout fault of a round is let through at `Stop`. The agent is told of it when the person sends the next message, so the round is not shown twice (Case 699.1). A layout fault of a shown Case is handled the same way. A Case whose file was not sent, or whose lines differ from the checked text, is still refused (Case 699.2). In a batch, the Context label of each first round names its Case, so no heading of the agent's own is needed (Case 699.5). The person sees no extra line. The route to the agent is the one `guppi context --prompt` already uses: its code says that stdout of `UserPromptSubmit` reaches the context. The new run `uv run guppi casecheck --prompt` uses the judgments that the `Stop` run uses today, so no second copy exists. It exits 0 always, since a block on `UserPromptSubmit` would block the person's message. `.claude/settings.json` registers `uv run guppi event prompt`, `uv run guppi context --prompt` and `uv run guppi gate` on that event. Their rules, `rule-event-log`, `rule-context-size` and `rule-retro-commit`, write the `hi` and gate marks, print the size note and refuse a typed command. None of them reads a reply, so the new run sits beside them. Case 699.3 replaces the Criterion of `estimate-case-check-judges-a-showing-after-a-refusal`, whose `When` lists the layout faults among the reasons of the `Stop` run; its `purpose` and `method` state no promise that changes. Case 699.4 replaces the Criterion of `estimate-orchestration-shows-the-built-case`, which has a refused round shown again. Case 699.6 replaces the Criterion of `estimate-orchestration-showing-example-passes-the-check`, which says that the example passes the functions of the `Stop` run; its `purpose` is set anew, and the test stays as it is. `estimate-case-check-shows-only-the-checked-case` stands: it sets the comparison with the store and the sending, which the `Stop` run still refuses. `estimate-case-check-exits-2-on-an-error` stands: it sets an error of the `Stop` run. `estimate-hook-registry-rendered` stands: it promises only that the file equals the Render. `estimate-orchestration-signs-a-batch-together` and `estimate-orchestration-signs-items-taken-together` stand: they set the one list numbered `<Case id>.Q<n>`, which stays true, and the new Estimate of Case 699.5 checks the mark. The two Estimates of `rule-case-check` that Cases 699.1 and 699.2 change keep their slugs; their Criterion and `purpose` say the new behaviour. The `purpose` of `rule-case-check` is set once, in Case 699.2, for both runs. A Glob `vault/**/*marks-each-round*` printed nothing, so the new slug is free. The code runs from the working tree once Work Mode changes it. The registration in `.claude/settings.json` and the text of `orchestration.md` land at the librarian's render. In between, the `Stop` run refuses no layout fault and no note comes. The old text of `orchestration.md` has a refused round shown again, but no refusal comes. Nothing is refused and nothing is lost, so no old form is kept. Case 696 of this session sets what `uv run guppi onward --plan` does at the same `Stop`. It judges the refusals of the other `Stop` hooks in the transcript, and a refusal of another hook neither silences it nor sends it on again. Fewer refusals of `uv run guppi casecheck` change nothing there, so this Case does not cover that hook. Case 697 changes other sentences of `rule-orchestration`. Its `old` anchors and the anchors of this Case do not overlap, and its new text says nothing of a showing again or of a batch. A Grep ``shows? the round again|round shown again|refuses is followed|text before a round|text-before-a-round|text-outside-the-list`` over the repository with the glob `!vault/{raw,archive}/**` printed `vault/wiki/brief.md`, `vault/wiki/orchestration.md`, `vault/wiki/log.md`, `vault/wiki/estimates/estimate-case-check-refuses-text-before-a-round.md`, `vault/wiki/rules/rule-case-check.md`, `vault/wiki/lessons/lesson-case-check-round-refused-for-an-own-text-no-showing-clears.md`, `tests/test_casecheck.py`, `guppi/casecheck.py`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/estimates/estimate-orchestration-shows-the-built-case.md`, `vault/wiki/rules/rule-case-protocol.md` and `vault/wiki/insights/insight-case-form-chat-form-read-by-no-script.md`. The hits of the code, the tests, the two Estimates and the two rules enter the Case. `orchestration.md` is the Render of `rule-orchestration`. The hits of `rule-case-protocol`, of the Insight and of `rule-case-check` outside its `estimates` list are History lines. The lesson records a past event. A Grep ``own text before|text of (its|the main agent's|the agent's) own (before|outside)|before a round|before the round`` over `vault/wiki/` with the glob `!{log,brief}.md` printed `estimates/estimate-case-check-refuses-text-outside-the-list.md`, `estimates/estimate-case-check-refuses-text-before-a-round.md`, `rules/rule-case-check.md`, `estimates/estimate-case-check-judges-a-showing-after-a-refusal.md`, `estimates/estimate-orchestration-shows-the-built-case.md`, `insights/insight-case-form-chat-form-read-by-no-script.md` and `lessons/lesson-sendmessage-answers-open-a-turn-of-their-own.md`. All of them but the last two enter the Case. In `estimate-orchestration-shows-the-built-case` the hit says that the agent writes no context of its own before the first question of a round, which stays true. The hit of the Insight is a History line, and the lesson records a past measurement. The same Grep over `.claude/` printed nothing. A Grep ``round_opening|showing_layout|outside_the_list|texts_after`` over `*.py` printed `tests/test_schemas.py`, `tests/test_orchestration.py`, `tests/test_lint.py` and `guppi/casecheck.py`. The hits of `tests/test_schemas.py` and `tests/test_lint.py` are names of tests of their own. `tests/test_orchestration.py` runs `outside_the_list` over the showing example, which Case 699.6 keeps. `/pre-spec` found four faults, and the person agreed to each fix. In a batch the main agent writes the label of its own, so Case 699.4 has the showing of a round in `rule-orchestration` and in the Criterion of `estimate-orchestration-shows-the-built-case` let that label stand. Case 699.6 also replaces the sentence that a refusal of the check names the limit a showing broke, since a layout fault now gets a note instead. The list of the rounds after the findings of `/pre-spec`, which `rule-prespec` sets and `estimate-prespec-gathers-the-answers-after-findings` checks, shows rounds of several Cases too. So Case 699.7 sets the same label there. It is a sub-case of its own, since it replaces the Criterion of another Estimate. The `method` of that Estimate waits for the `/pre-spec` of a later session, so it is set to the reading of the Spec at the Retro of this session. Its `purpose` states no promise that changes. The vault already held `lesson-orchestration-batch-rounds-headed-by-own-text`, of session 0104, with the same root cause, a child of `insight-orchestration-items-taken-together-unruled`. By the person's answer, Case 699.5 sets that Insight `actioned`, so it leaves the backlog and its lessons go to the archive. The lesson is of another session, so no line of this Case carries a mark for it. The check of this file noted the lines of the old Criteria that the new ones do not carry, and each change is on purpose. In 699.1 and 699.2 a layout fault no longer exits 2 at `Stop`, and the judgment moves to the run at the next message. In 699.3 the layout faults leave the list of reasons. In 699.4 the refusal that is followed by a showing again names its faults, and the lines on the showing of a round and on the agent's own context let the batch label stand. In 699.7 the list of the rounds gains the label. In 699.6 the example passes both runs. The check also noted lines that 699.1 and 699.2 share, and lines that other sub-cases share with a sibling. The run at the next message acts the same way for a round and for a Case, so its exit and its silence are said in each sub-case. Each other shared line states the frame of its own sub-case, which the Criterion of its Estimate needs in order to read without the Case.

> **problem:**
> A layout fault of a shown round or Case makes the `Stop` check send the reply back after the person has read it, and the agent shows the whole round or Case a second time. In a batch, the agent marks where each Case's round begins with a heading of its own, because the rules set no mark, and the check reads that heading as such a fault.

> **recommend:**
> - **What the check does when only the layout of a round is wrong**
>   - Recommended: (b) let it through, and tell the agent at the next message: the check lets the reply through, and a hook at the person's next message tells the agent what was wrong.
>   - Answer: agreed, (b).
> - **How a joint showing marks where each Case's round begins**
>   - Recommended: (a) the Context label names the Case, such as `**Context — Case 697 (C4):**`, translated; a later round is marked by its question numbers alone.
>   - Answer: agreed, (a).
> - **Whether a layout fault in a shown Case is handled the same way**
>   - Recommended: (a) layout faults of a Case get the note too; a file not sent or ledger lines that differ from the checked ones are still sent back.
>   - Answer: agreed, (a).
> - **Whether the person sees anything when a layout fault is let through**
>   - Recommended: (a) the agent alone is told, at the person's next message.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: by a finding of `/pre-spec` the person agreed to, let the batch label stand in the showing of a round in `rule-orchestration` and in the Criterion of `estimate-orchestration-shows-the-built-case`.
>   - Taken: Case 699.4 adds a pair on the Render and two lines of its Criterion.
> - **Change**
>   - Asked: by a finding of `/pre-spec` the person agreed to, replace the sentence that a refusal of the check names the limit a showing broke.
>   - Taken: Case 699.6 adds a pair that names the note at the next message too, and a line of its Criterion.
> - **Change**
>   - Asked: by a finding of `/pre-spec` the person agreed to, the label holds in the list of the rounds after the findings too, through `rule-prespec` and `estimate-prespec-gathers-the-answers-after-findings`.
>   - Taken: the new Case 699.7 does it, since it replaces the Criterion of another Estimate.
> - **Change**
>   - Asked: by the person's answer (a) to the question of `/pre-spec`, name the old lesson `lesson-orchestration-batch-rounds-headed-by-own-text` and its Insight, and set `insight-orchestration-items-taken-together-unruled` `actioned`.
>   - Taken: `context` names both, and Case 699.5 sets the Insight `actioned`.

### Case 699.1 — A layout fault of a shown round is told at the next message

> **given:**
> `rule-case-check`: the rule of the check, whose Purpose says what it prevents.
> **＋** `estimate-case-check-refuses-text-before-a-round`: its Criterion is replaced whole.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the count of the refusals of the `Stop` run.
> **＋** `guppi/casecheck.py`: the check, whose `round_opening` judges how a round opens.
> **＋** `guppi/ledger.py`: its `refusals` reads the refusals of the check in the transcript.
> **＋** `tests/test_casecheck.py`: the tests of the check.
> **＋** `rule-hook-registry`: renders the hooks of `.claude/settings.json`.
> **＋** `.claude/settings.json`: registers the hooks.

> **when:**
> A reply of the main agent shows a round of `case-guppi`, `Stop` fires and `uv run guppi casecheck` of `guppi/casecheck.py` runs on it. Then the person sends a message, and `uv run guppi casecheck --prompt` runs on `UserPromptSubmit`, as `.claude/settings.json` registers it.

> **then:**
> At `Stop`, `uv run guppi casecheck` refuses no reply for the way it opens a round of `case-guppi`, or for a text of the main agent's own before the round. Its other reasons stand.
> **＋** On `UserPromptSubmit`, `uv run guppi casecheck --prompt` judges the last reply of the main agent before the person's message, and the turn that reply ends. The turn holds a round when a text that `case-guppi` gave back in it is a round by `is_round` of `guppi/casecheck.py`.
> **＋** It finds a fault when the first line of the reply that is not blank opens neither with `❓ ` nor with a bold label that ends in a colon. While the session's event log holds no `prespec` line of this session after its `hi`, it also finds a fault when the main agent wrote text in the turn after the first round came back and before its last tool call. It judges only the texts after the reply that the last refusal of `uv run guppi casecheck` in the turn follows, judged by `refusals` of `guppi/ledger.py`.
> **＋** On a fault it prints one line to stdout, which reaches the agent's context. The line quotes the text before the round, says that the round stands as shown and is not shown again, and tells the agent to open the next round with its Context paragraph or its first question, with nothing before it.
> **＋** `.claude/settings.json` registers `uv run guppi casecheck --prompt` on `UserPromptSubmit`, as `rule-hook-registry` renders it.
> **－** With no fault, in a turn with no round, and for text after the last question, it prints nothing.
> **－** It exits 0 always and never blocks the person's message. An error of its own goes to stderr.
> **－** The person sees nothing of the note. It stores nothing and writes no file.
> **－** The refusals of the `Stop` run are counted as `estimate-case-check-judges-a-showing-after-a-refusal` sets it, and a layout fault of a round is not one of them.

```then
update:
- slug: rule-case-check
  replace:
  - old: a round of `case-guppi` from being shown after a text of the main agent's own written after the round came back (case 562)
    new: 'a round of `case-guppi` from being shown after a text of the main agent''s own written after the round came back with no word to the agent: the `Stop` run lets the showing through, and the run on `UserPromptSubmit` tells the agent of it at the person''s next message, so that the round is not shown twice (cases 562, 699.1)'
  change: a layout fault of a shown round passes the Stop run and is told to the agent at the person's next message by casecheck --prompt (case 699.1)
- slug: estimate-case-check-refuses-text-before-a-round
  set:
    status: pending
    purpose: Whether the Stop run of the Case check lets through a reply that shows a round of case-guppi after a text of the main agent's own, and the run on UserPromptSubmit tells the agent of it at the person's next message, judging only what follows the last refusal in the turn, only the first line after pre-spec, and no turn with no round
  change: the Criterion replaced whole — the Stop run lets a layout fault of a round through, and casecheck --prompt tells the agent at the next message; purpose set anew
- slug: rule-hook-registry
  replace:
  - old: '"uv run guppi context --prompt", "timeout": 30 },'
    new: '"uv run guppi context --prompt", "timeout": 30 }, { "type": "command", "command": "uv run guppi casecheck --prompt", "timeout": 30 },'
  change: uv run guppi casecheck --prompt registered on UserPromptSubmit (case 699.1)
```

```tasks
- [x] update `rule-case-check`
- [x] update `estimate-case-check-refuses-text-before-a-round`
- [x] update `rule-hook-registry`
- [x] `guppi/casecheck.py`: `stop` no longer adds the reason of `round_opening`; `run` takes `--prompt`, which reads the transcript of the `UserPromptSubmit` payload, leaves out the person's message when the transcript holds it, judges the last reply of the main agent and its turn by `round_opening`, prints the note on stdout and exits 0 always, its own error on stderr; the module docstring says so.
- [x] `tests/test_casecheck.py`: the tests of a round expect the `Stop` run to exit 0 on a layout fault; new tests whose names hold `round` run `--prompt` over a transcript whose last reply opens with a line of its own, or with text written after the round came back, and find the note on stdout and exit 0; a round with nothing before it, a turn with no round and an unreadable payload print nothing and exit 0.
- [x] `uv run pytest tests/test_casecheck.py`
- [x] `uv run guppi render`: `.claude/settings.json`
- [x] read `estimate-case-check-refuses-text-before-a-round`
```

### Case 699.2 — A layout fault of a shown Case is told at the next message

> **given:**
> `rule-case-check`: the rule of the check, whose `purpose` and Purpose say what it prevents.
> **＋** `estimate-case-check-refuses-text-outside-the-list`: its Criterion is replaced whole.
> **＋** `estimate-case-check-shows-only-the-checked-case`: sets the comparison and the sending that the `Stop` run still refuses; its Criterion stands.
> **＋** `guppi/casecheck.py`: the check, whose `showing_layout` judges the layout of a showing.
> **＋** `guppi/ledger.py`: its `refusals` reads the refusals of the check in the transcript.
> **＋** `tests/test_casecheck.py`: the tests of the check.
> **＋** `.claude/settings.json`: registers the run on `UserPromptSubmit`.

> **when:**
> A reply of the main agent shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, not a deferred decision in the short form. `Stop` fires and `uv run guppi casecheck` of `guppi/casecheck.py` runs on it. Then the person sends a message, and `uv run guppi casecheck --prompt` runs on `UserPromptSubmit`, as `.claude/settings.json` registers it.

> **then:**
> At `Stop`, `uv run guppi casecheck` refuses no showing for a text of the main agent's own before its first Case heading, outside its list and its `ratification`, or written after the summary of `case-guppi` came back.
> **＋** It still refuses a shown Case that differs from the checked text, or whose file was not sent or differs from the store, as `estimate-case-check-shows-only-the-checked-case` sets it.
> **＋** On `UserPromptSubmit`, `uv run guppi casecheck --prompt` judges the last reply of the main agent before the person's message, and the turn that reply ends, when that reply shows a Case.
> **＋** It finds a fault when a line that is not blank stands before the first Case heading. It finds a fault when a line between a Case heading and the next Case heading or the horizontal rule `---` is not blank, not a list item — a line that opens with `- `, `* ` or a number and `. ` — not a line indented under a list item, and not a line of the `ratification` blockquote. It finds a fault when the main agent wrote text in the turn after the first summary of `case-guppi` came back — a text given back whose first line that is not blank opens with `**Built:**` — and before its last tool call. It judges only the texts after the reply that the last refusal of `uv run guppi casecheck` in the turn follows, judged by `refusals` of `guppi/ledger.py`.
> **＋** On a fault it prints one line to stdout, which reaches the agent's context. The line quotes the first such text, says that the Case stands as shown and is not shown again, and tells the agent to write nothing of its own before the Case and to keep its own text after the horizontal rule at the next showing.
> **－** A text written before the first summary came back, text after the horizontal rule, a reply with no Case heading that holds a section, a fence tagged `DIFF` and a deferred decision in the short form are not judged, and it prints nothing for them.
> **－** It exits 0 always and never blocks the person's message. An error of its own goes to stderr.
> **－** The person sees nothing of the note. It stores nothing and writes no file.

```then
update:
- slug: rule-case-check
  replace:
  - old: and a Case from being shown with a text of the main agent's own outside the list under its heading and its `ratification` or written after the summary of `case-guppi` came back (case 611), each judged only by what follows the last refusal of the check in the turn, so that one showing again clears a refusal (case 692)
    new: and a Case from being shown with a text of the main agent's own outside the list under its heading and its `ratification` or written after the summary of `case-guppi` came back with no word to the agent, told in the same way at the person's next message, so that the Case is not shown twice, while a Case whose file was not sent or whose showing differs from the stored text is still refused (cases 611, 699.2), each judged only by what follows the last refusal of the check in the turn (case 692)
  set:
    purpose: Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them, while fewer than three refusals of that Case stand since the person's last message, a round of case-guppi from reaching the main agent with a question out of the form of the grill-me template, a round of case-guppi or a Case from being shown after a text of the main agent's own with no word to the agent at the person's next message, and a summary of case-guppi from reaching the main agent without the id and the name of the Case it built
  change: a layout fault of a shown Case passes the Stop run and is told to the agent at the person's next message; a file not sent or a showing that differs from the store is still refused (case 699.2)
- slug: estimate-case-check-refuses-text-outside-the-list
  set:
    status: pending
    purpose: Whether the Stop run of the Case check lets through a reply that shows a Case with a text of the main agent's own before its first Case heading, outside its list and its ratification, or written after the summary of case-guppi came back, and the run on UserPromptSubmit tells the agent of it at the person's next message, judging only what follows the last refusal in the turn
  change: the Criterion replaced whole — the Stop run lets a layout fault of a Case through, and casecheck --prompt tells the agent at the next message; purpose set anew
```

```tasks
- [x] update `rule-case-check`
- [x] update `estimate-case-check-refuses-text-outside-the-list`
- [x] `guppi/casecheck.py`: `stop` no longer adds the reason of `showing_layout`; `--prompt` judges the last reply of the main agent and its turn by `showing_layout` when that reply shows a Case, and prints the note on stdout; the module docstring says so.
- [x] `tests/test_casecheck.py`: the layout tests expect the `Stop` run to exit 0 on a text before the heading, outside the list or after the summary came back; new tests run `--prompt` over a transcript whose last reply shows such a Case and find the note on stdout and exit 0; a showing with no file sent is still refused at `Stop`.
- [x] `uv run pytest tests/test_casecheck.py`
- [x] read `estimate-case-check-refuses-text-outside-the-list`
```

### Case 699.3 — The count of the refusals holds only the reasons left to the `Stop` run

> **given:**
> `estimate-case-check-judges-a-showing-after-a-refusal`: its Criterion is replaced whole.
> **＋** `rule-case-check`: the rule of the check.
> **＋** `guppi/casecheck.py`: the check, whose `give` counts its reasons.
> **＋** `guppi/ledger.py`: its `refusals` reads the refusals in the transcript.
> **＋** `tests/test_casecheck.py`: the tests of the check.

> **when:**
> The `Stop` hook `uv run guppi casecheck` of `guppi/casecheck.py` fires at the end of a reply of the main agent in a session with a `hi`, and finds a reason to refuse it: a shown Case that differs from `<plan>.checked.json`, a shown Case whose file was not sent or differs from the store, or an error of its own after it read the payload.

> **then:**
> The hook judges the reply the same whether `stop_hook_active` is set or not.
> **＋** It gives a reason that names a Case, opening with `case <id>:`, while fewer than three of its own refusals in the stretch hold a reason of that Case, and any other reason while fewer than three of them hold the same reason.
> **＋** It exits 2 while a reason is left to give, with those reasons on stderr.
> **＋** When no reason is left to give, it exits 0 and prints on stderr one line per Case it let through: "casecheck: case <id> shown unchecked after three refusals; the Spec hook compares it at ratification".
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`; its own refusal is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[uv run guppi casecheck]: `, judged by `refusals` of `guppi/ledger.py`, the function that `guppi onward` calls.
> **－** A text of the main agent's own before a round of `case-guppi` or outside the list of a showing is no reason of the `Stop` run. `uv run guppi casecheck --prompt` refuses nothing, so it counts nothing.
> **－** With `stop_hook_active` set and a transcript it cannot read, it exits 0 and prints nothing.
> **－** The run `uv run guppi casecheck --subagent` keeps its own guard, the store.

```then
update:
- slug: estimate-case-check-judges-a-showing-after-a-refusal
  set:
    status: pending
  change: the Criterion replaced whole — a text of the agent's own before a round or outside the list is no reason of the Stop run
```

```tasks
- [x] update `estimate-case-check-judges-a-showing-after-a-refusal`
- [x] `tests/test_casecheck.py`: a test of the count whose reason is a text before a round or outside the list gives a reason of a shown Case instead, such as a file not sent.
- [x] `uv run pytest tests/test_casecheck.py`
- [x] read `estimate-case-check-judges-a-showing-after-a-refusal`
```

### Case 699.4 — A round or a Case with a layout fault is not shown again

> **given:**
> `rule-orchestration`: its Render sets the showing of a round and of a Case after a refusal.
> **＋** `estimate-orchestration-shows-the-built-case`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `rule-case-check`: the check of a showing.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.
> **＋** `.claude/skills/wait-what/SKILL.md`: the skill of a plain explanation.
> **＋** `.claude/skills/grill-me/SKILL.md`: the form of a question.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session, whose items the label of a batch names.

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no first line `**Built:**` and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, its label naming its Case and its item of `raw/<date>/<hi HHMM>/frontier.md` when the round is one of a batch, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in Russian translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands, and the main agent asks the person whether that other Case is built again.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses — its file not sent, or a showing that differs from the checked text — is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it.
> **＋** A round or a Case shown with a text of the main agent's own before it or outside its list is not refused and is not shown again: `rule-case-check` tells the agent of it at the person's next message, and the agent keeps the form from the next showing on.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, never to build a Case, and asks that run again only to confirm its own findings.
> **－** The main agent writes the heading, the list, the `ratification` and the question on another Case from the summary, and does not read the file of the Case.
> **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
> **－** The main agent writes no context of its own before the first question of a round. The label that names the Case of a round in a batch is no such context.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

```then
update:
- slug: rule-orchestration
  replace:
  - old: a reply that shows a Case and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it (case 452.4); a reply that shows a round and that the `Stop` check refuses is followed, before the person answers, by a reply that shows the round again with nothing before its `**Context:**` paragraph or its first question (case 561.9)
    new: 'a reply that shows a Case and that the `Stop` check of `rule-case-check` refuses — its file not sent, or a showing that differs from the checked text — is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it (case 452.4); a round or a Case shown with a text of the agent''s own before it or outside its list is not refused and is not shown again: the check tells the agent of it at the person''s next message, and the agent keeps the form from the next showing on (case 699.4)'
  - old: the `**Context:**` paragraph that opens the first round on an item translated in place before the first question,
    new: the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, its label in a batch naming its Case and its Frontier item as `## Showing and signing a Case` sets it (case 699.4),
  change: a round or a Case shown with a layout fault is not shown again; the check tells the agent at the person's next message; the Context label of a round in a batch names its Case (case 699.4)
- slug: estimate-orchestration-shows-the-built-case
  set:
    status: pending
  change: the Criterion replaced whole — a round or a Case with a layout fault is not shown again, and the Context label of a round in a batch names its Case
```

```tasks
- [x] update `rule-orchestration`
- [x] update `estimate-orchestration-shows-the-built-case`
- [x] `uv run guppi render`: `vault/wiki/orchestration.md`
- [x] read `estimate-orchestration-shows-the-built-case`
```

### Case 699.5 — The Context label marks the round of each Case of a batch

> **given:**
> `rule-orchestration`: its Render sets the list of the rounds of a batch.
> **＋** `estimate-orchestration-marks-each-round-of-a-batch`: the new check of the mark.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `/pre-spec`: the skill before which a batch is shown.
> **＋** `rule-case-check`: the check of how a round opens.
> **＋** `estimate-orchestration-signs-a-batch-together`: sets the batch and its list; its Criterion stands.
> **＋** `insight-orchestration-items-taken-together-unruled`: the Insight whose lesson of the batch headings this Case closes; set `actioned`.

> **when:**
> In Plan Mode before `/pre-spec`, the main agent shows in one list the rounds of `case-guppi` that came back for a batch of Cases, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The `**Context:**` paragraph of each first round on an item opens with a label that names its Case id and its item of `raw/<date>/<hi HHMM>/frontier.md`, translated, such as `**Context — Case 7 (C2):**`.
> **＋** A later round, which has no Context paragraph, is marked by its question numbers `<Case id>.Q<n>` alone.
> **＋** No heading or other line of the main agent's own stands before a round to mark where it begins, so the reply opens with a Context label or a question line, which the check of `rule-case-check` accepts.
> **－** A round shown alone, outside a batch, keeps its `**Context:**` label as `case-guppi` gave it, translated.

```then
create:
- slug: estimate-orchestration-marks-each-round-of-a-batch
  ref: rule-orchestration
  kind: QA
  purpose: Whether the list of the rounds of a batch marks where each Case's round begins by its Context label, which names the Case and its item, and by its question numbers, with no heading of the main agent's own
  method: 'by hand at the Retro of this session: the new Render of rule-orchestration in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
update:
- slug: rule-orchestration
  replace:
  - old: one list shows every round that came back, each question numbered `<Case id>.Q<n>`;
    new: one list shows every round that came back, each question numbered `<Case id>.Q<n>` and the `**Context:**` label of each first round naming its Case and its Frontier item, translated, such as `**Context — Case 7 (C2):**`, with no heading or other line of the agent's own to mark where a round begins (case 699.5);
  change: the Context label of each first round of a batch names its Case and its item, and no heading of the agent's own marks a round (case 699.5)
- slug: insight-orchestration-items-taken-together-unruled
  set:
    status: actioned
  change: 'actioned: the Context label of each first round of a batch names its Case, so no heading of the agent''s own marks a round (case 699.5)'
```

```tasks
- [x] update `rule-orchestration`
- [x] create `estimate-orchestration-marks-each-round-of-a-batch`
- [x] update `insight-orchestration-items-taken-together-unruled`
- [x] read `estimate-orchestration-marks-each-round-of-a-batch`
```

### Case 699.6 — The showing example passes both runs of the check

> **given:**
> `rule-orchestration`: its Render holds the showing example and the sentence on its test.
> **＋** `estimate-orchestration-showing-example-passes-the-check`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `tests/test_orchestration.py`: the test of the example.
> **＋** `guppi/casecheck.py`: the check whose functions the test runs.
> **＋** `rule-case-check`: the check of a showing.

> **when:**
> `tests/test_orchestration.py` runs under `uv run pytest`. It reads the block tagged `showing` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it the functions of `guppi/casecheck.py` that the check of `rule-case-check` runs over a reply that shows a Case — the comparison of its `Stop` run and the judgment of the layout of its run on `UserPromptSubmit` — with a store whose sub-cases hold the ledger lines the example's `ratification` gives them.

> **then:**
> `vault/wiki/orchestration.md` holds, under its own heading at the end of `## Showing and signing a Case`, one block tagged `showing`: a reply that shows a Case with two sub-cases, its heading, one list with an item per sub-case, one `ratification` and the agent's own text after one horizontal rule.
> **＋** The `ratification` of the example is a quote block: the line `> **ratification:**`, then the fence and the ledger lines of both sub-cases, each line opening with `> `.
> **＋** The example is in English; the paragraph before the block says that in the chat the heading, the names and the short texts stand in the language of the chat, that the file goes by `SendUserFile` in the same reply, and that the example passes the check of `rule-case-check` at the `Stop` of the reply and at the person's next message, which is the source of the limits, and that a refusal of the check, or its note at the person's next message, names the limit a showing broke; it lists no other limit.
> **＋** The check finds no text outside the list and the `ratification`, reads the `ratification` as the showing of each sub-case it names, and finds no difference from the store, and the test passes.
> **＋** The example with the lines of its fence not quoted gives the finding of a text outside the list, and the test asserts it.
> **＋** The test reads the example from `vault/wiki/orchestration.md` and the checks from `guppi/casecheck.py`, and holds no copy of either.
> **－** While `vault/wiki/orchestration.md` holds no block tagged `showing`, both tests of `tests/test_orchestration.py` that read it fail with a message that names the file; no test of the file is skipped.

```then
update:
- slug: rule-orchestration
  replace:
  - old: A test runs over the example the functions that the `Stop` check of `rule-case-check` runs over a reply that shows a Case, and fails on any refusal, so the example keeps to that check as the check stands (case 651.2).
    new: A test runs over the example the functions that the check of `rule-case-check` runs over a reply that shows a Case, at the `Stop` of the reply and at the person's next message, and fails on any refusal or note, so the example keeps to that check as the check stands (cases 651.2, 699.6).
  - old: Copy its form; a refusal of the check names the limit a showing broke.
    new: Copy its form; a refusal of the check, or its note at the person's next message, names the limit a showing broke (case 699.6).
  change: the showing example is tested by the functions of both runs of the check (case 699.6)
- slug: estimate-orchestration-showing-example-passes-the-check
  set:
    status: pending
    purpose: Whether the example of a showing in orchestration.md passes the check of rule-case-check of a reply that shows a Case, at its Stop and at the person's next message, so the form the main agent copies stays a form the check accepts
  change: the Criterion replaced whole — the example passes the comparison of the Stop run and the layout judgment of the run at the next message; purpose set anew
```

```tasks
- [x] update `rule-orchestration`
- [x] update `estimate-orchestration-showing-example-passes-the-check`
- [x] `uv run pytest tests/test_orchestration.py`
- [x] read `estimate-orchestration-showing-example-passes-the-check`
```

### Case 699.7 — The Context label marks the round of each Case after the findings of `/pre-spec`

> **given:**
> `rule-prespec`: its Render sets the list of the rounds in the loop after the findings.
> **＋** `estimate-prespec-gathers-the-answers-after-findings`: its Criterion is replaced whole.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the skill rendered from `rule-prespec`.
> **＋** `.claude/skills/grill-me/SKILL.md`: the form of a question.
> **＋** `vault/wiki/orchestration.md`: sets the showing of a Case and of a batch.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session, whose items the label names.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec of the session, read at Retro.

> **when:**
> `/pre-spec` has reported findings in Cases of the plan, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

> **then:**
> The main agent sends each finding in a Case, with each answer of the report that bears on that Case, to the `case-guppi` of that Case by `SendMessage`, one message to each `case-guppi`, as soon as the report asks the person no question or the person has answered every question of the report.
> **＋** While a question of the report is unanswered, the main agent sends nothing to any `case-guppi`.
> **＋** A question of the report that the person leaves unanswered is asked again in the shape of `.claude/skills/grill-me/SKILL.md` under its number.
> **＋** The main agent ends each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer it sent is still out, with one line that opens with a bold label ending in a colon and names the Cases that have answered and the Cases still out.
> **＋** That line holds nothing of what an answer says and no question, and the main agent writes nothing else in the chat while an answer is out and passes on no answer of one `case-guppi` alone.
> **＋** It then shows the person one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>` by the Case it belongs to, sends each answer to the `case-guppi` of its Case in one message, and repeats the wait and the list until every `case-guppi` it sent has answered with its Case.
> **＋** In that list the `**Context:**` label of each first round on an item names its Case id and its item of `raw/<date>/<hi HHMM>/frontier.md`, translated, such as `**Context — Case 7 (C2):**`, and no heading or other line of the main agent's own marks where a round begins.
> **＋** It then shows every Case built again in one reply, in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
> **－** When an answer brings back a round while another answer is still out, the round is not shown in that turn, and `uv run guppi casecheck` does not refuse the reply that opens with the labelled line.
> **－** Outside this loop, Cases go out together for one ratification only in a batch, as `vault/wiki/orchestration.md` sets it.
> **－** A question that no answer settles stays in the next list under its number.

```then
update:
- slug: rule-prespec
  replace:
  - old: numbered `<Case id>.Q<n>` — the id of its Case and its number in the round — so that each answer goes back to its `case-guppi`.
    new: numbered `<Case id>.Q<n>` — the id of its Case and its number in the round — so that each answer goes back to its `case-guppi`; the `**Context:**` label of each first round names its Case and its Frontier item, translated, such as `**Context — Case 7 (C2):**`, and no heading or other line of your own marks where a round begins (case 699.7).
  change: in the list of the rounds after the findings, the Context label of each first round names its Case (case 699.7)
- slug: estimate-prespec-gathers-the-answers-after-findings
  set:
    status: pending
    method: 'by hand at the Retro of this session: the new Render of rule-prespec in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line'
  change: the Criterion replaced whole — the Context label of each first round in the list names its Case; method set to the reading of the Spec at Retro
```

```tasks
- [x] update `rule-prespec`
- [x] update `estimate-prespec-gathers-the-answers-after-findings`
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] read `estimate-prespec-gathers-the-answers-after-findings`
```
