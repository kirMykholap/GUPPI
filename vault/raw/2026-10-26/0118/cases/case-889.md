## Case 889 — After /pre-spec the hook sends the agent on while a Case is still out

> **context:**
> After `/pre-spec`, the `Stop` hook `uv run --project .guppi guppi onward --plan` sends the agent on where no person is needed, since a reply that carries a `LEDGER` block ends in that text and can call no tool. `plan_onward` of `.guppi/guppi/onward.py` returns no reason when `case_out` finds a Case still out: a file `case-<N>.md` under `cases/` written after the last decision line of Case N. So a batch that the person ratifies in part leaves the Cases still out to no turn. At `/pre-spec` of session 2307 the person ratified Cases 882, 883, 884 and 886, Case 881 had to go back to its `case-guppi`, the hook said nothing, and the session stood until the person asked what came next (`lesson-prespec-loop-stalls-when-one-case-waits-after-a-partial-ratification`, from L55 of `raw/2026-10-17/2307/ledger.md`). The person chose that the hook sends the agent on in that state too, at every reply it sends on today, with a third reason that names each Case still out; the agent sends each one that must change to its `case-guppi`, ends the turn as `orchestration.md` sets it for a Case out while a `case-guppi` has not answered, or opens its reply with `STOP:` when each Case waits only for the person's word. `rule-prespec-onward` is the rule this touches: its Purpose is to keep Plan Mode from stopping where no person is needed, and the chosen option serves it. Two sentences of its Purpose change: the one that sends the agent to the check and the exit gains the condition that no Case is still out, and the third reason is added after the reason of the loop. The Criterion of `estimate-prespec-onward-sends-the-agent-on` lists "no Case is still out" among the conditions of exit 2, and the Criterion of `estimate-prespec-onward-tells-the-loop-from-its-end` says that a Case built again and not yet ratified keeps the hook silent; the change makes both false, so Case 889.1 and Case 889.2 replace each whole, and set anew each `purpose` that states the old promise. Each reason carries the text of `ONLY_THE_PERSON` of `.guppi/guppi/onward.py`, which today asks for `STOP:` for "a Case still out with its case-guppi"; beside the third reason that would tell the agent both `STOP:` and `**Waiting:**` for the same Case (finding F1 of `/pre-spec`), so by the person's choice of the third message that text, and the line of the Criterion of Case 889.1 that states it, keep `STOP:` for a question the person must answer and a Case that waits only for the person's word, and, while a `case-guppi` has not answered, send the agent to the end of the turn that `orchestration.md` sets for a Case out. The reason does not name the `**Waiting:**` line itself, since Case 890.3 sets that a Case sent back after the check refused a showing of a batch is out of the batch and takes no `**Waiting:**` line while its `case-guppi` has not answered; after the person ratifies the other Cases, that Case is still out and this hook names it, and the agent waits for it as `orchestration.md` then sets it. The Criterion of `estimate-prespec-onward-reads-the-decisions-of-the-session` sets when a Case is still out, and that judgment does not change; its line that a Case replaced under a new number does not keep the hook silent stays true, since after the change no Case keeps it silent, so its Criterion stands and the person's choice of two rewritten checks holds. But its tests told a Case out by the silence of the hook and a Case not out by exit 2 alone, which would pass whether the Case is out or not once a Case still out exits 2 too (finding F4 of `/pre-spec`); so the tests of a Case out assert the third reason, and the tests of a Case not out assert the reason of the exit or of the loop, never the third, so that its `method` still tells the two apart. Before `/pre-spec` the hook stays silent on purpose, and this Case does not change that. The Case does not change `rule-orchestration`: the sentences of `orchestration.md` and of `.claude/skills/pre-spec/SKILL.md` that say the hook of `rule-prespec-onward` sends the agent on after the reply that acknowledges the ratification stay true. The item put off on that page by Case 884 stays in `backlog.md`; the item put off by Case 887 is retired by Case 890, whose file carries `{supersedes:case 887}` on the decision lines of Case 890.1 on `rule-case-check` and of Case 890.3 on `rule-orchestration` (finding F2 of `/pre-spec`). A Grep of `rule-prespec-onward|onward --plan` over `vault/wiki/`, `log.md` and `brief.md` left out, printed 21 files; besides the rule page and its three Estimates, the hits of `estimate-orchestration-acknowledging-reply`, `estimate-orchestration-defers-in-one-reply`, `estimate-orchestration-shows-the-frontier-after-a-closed-line` and `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` say only that the hook sends the agent on after `/pre-spec` or nothing once `spec.md` stands, which stays true; `estimate-prespec-confirms-the-findings-once` says the hook sends the agent to the check and the exit after the one ratification of every Case built again, which stays true; the other hits name the hook as a child, in the registry of hooks, in a Result or a History, or for what it counts as no Case or as ratified (`rule-case-build`, `estimate-case-check-sends-back-a-clash-with-another-case`, `estimate-orchestration-shows-the-built-case`), or as a judgment apart (`estimate-retro-onward-sends-the-agent-to-the-handoff`), which the change leaves true. The same Grep over `.claude/` printed `.claude/settings.json`, `.claude/skills/pre-spec/SKILL.md` and `.claude/agents/case-guppi.md`, none of which the change makes false. A Grep of `case_out|cases_out` over `.guppi/` printed only `.guppi/guppi/onward.py` and `.guppi/tests/test_onward.py`, so the judgment of a Case still out lives in one function, and the ids of the third reason come from that same judgment, with no second copy, as `rule-one-judgment-one-implementation` sets it. The lesson stands in the ledger of session 2307, so no decision line carries `{addresses:...}`.

> **problem:**
> After `/pre-spec`, a batch ratified in part leaves the Cases still out with no turn: the hook that sends the agent on stays silent while any Case is out, so the run stops where no person is needed.

> **recommend:**
> - **How the run goes on after a partial ratification**
>   - Recommended: (a) the hook sends the agent on with a third message.
>   - Answer: agreed, (a).
> - **Which replies get the new message**
>   - Recommended: (a) the same replies as today.
>   - Answer: agreed, (a).
> - **What the new message names**
>   - Recommended: (a) the message names each Case left without a ratification.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) rewrite the two existing checks, in two sub-cases.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the findings of `/pre-spec`: the text that each reason adds asks for `STOP:` for a Case still with its `case-guppi` while the third reason asks for the `**Waiting:**` line; the `context` claimed that the item of Case 887 stays in `backlog.md`; the tests of `estimate-prespec-onward-reads-the-decisions-of-the-session` tell a Case not out by exit 2 alone.
>   - Taken: `ONLY_THE_PERSON` and the line of Case 889.1 keep `STOP:` for a question or a Case that waits only for the person's word and send a `case-guppi` that has not answered to the end of the turn that `orchestration.md` sets for a Case out, which Case 890.3 sets for a Case sent back after a refusal; the `context` says that Case 890 retires the item of Case 887; the tests of a Case not out assert the reason of the exit or of the loop, and that Estimate's Criterion stands, as the `context` says.

### Case 889.1 — A Case still out does not silence the hook

> **given:**
> `estimate-prespec-onward-sends-the-agent-on`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/onward.py`: the hook `guppi onward --plan`.
> **＋** `.guppi/tests/test_onward.py`: the tests of the hook.
> **＋** `rule-prespec-onward`: the rule of the hook.
> **＋** `estimate-prespec-onward-tells-the-loop-from-its-end`: the check of which reason the hook gives.
> **＋** `.guppi/guppi/ledger.py`: the reading of the refusals in the transcript.
> **＋** `.claude/settings.json`: the registry of the `Stop` hooks.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec of the session, whose presence silences the hook.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier, whose open lines silence the hook.
> **＋** `/pre-spec`: the skill whose `prespec` line the hook waits for.
> **＋** `vault/wiki/orchestration.md`: how the main agent ends a turn while a Case is out.
> **＋** `raw/2026-10-26/0118/cases/case-890.md`: the Case of this session that sets the turn of a Case sent back after a refusal of a showing.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi onward --plan` receives the payload of the end of a reply of the main agent.

> **then:**
> It exits 2 when all of these hold: the event log of the session's window holds a `hi` of this session and, after it, a `prespec` line of this session; `raw/<date>/<hi HHMM>/spec.md` does not stand; `raw/<date>/<hi HHMM>/frontier.md` holds no open line under `## Cases`; the reply carries a `LEDGER` block, or a refusal of the ledger hook in the stretch follows the reply of the main agent that ended just before it; its own refusal is not spent; and the reply does not open with `STOP:`.
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. A refusal of a `Stop` hook is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[<command>]: `. Its own command is `uv run --project .guppi guppi onward --plan`, and the command of the ledger hook is `uv run --project .guppi guppi ledger`.
> **＋** Its own refusal is spent when its last refusal stands in the stretch and no refusal of the ledger hook follows the same reply of the agent or a later one, judged by `refusals` of `.guppi/guppi/ledger.py`. So after a reply that the ledger hook sent back — a line it refused or held, or its reminder of a lesson with no mark — it sends the agent on again at the end of the next reply: the one that writes a line again, or an answer with no `LEDGER` block, such as the answer that no Case fixed the cause of the lesson.
> **＋** A refusal of another `Stop` hook in the stretch neither silences it nor sends it on again, and neither does `stop_hook_active`.
> **＋** Its reason on stderr sends the agent on with the Cases still out, to the check and the exit, or on with the loop after the findings of `/pre-spec`, as `estimate-prespec-onward-tells-the-loop-from-its-end` sets it.
> **＋** Each reason adds that, when only the person can go on — a question the person must answer, or a Case that waits only for the person's word — the agent opens its reply with `STOP:` and asks the person instead, and that while a `case-guppi` has not answered the agent ends the turn as `vault/wiki/orchestration.md` sets it for a Case out and goes on in the turn that the answer opens.
> **＋** In every other case with no error of its own, it exits 0 and prints nothing. This holds once its own refusal is spent, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript. `.claude/settings.json` registers it on `Stop`, after `uv run --project .guppi guppi onward`.
> **－** A Case still out, as `rule-prespec-onward` judges it, does not keep it silent: it changes only its reason.
> **－** With no `prespec` line of this session after its `hi` in the event log, it exits 0 and prints nothing, and its reason never tells the agent to call `/pre-spec`.
> **－** A reply with no `LEDGER` block after a reply that the ledger hook did not send back gets no reason.
> **－** An error of its own after it has read the payload, when a `prespec` line of this session stands after its `hi`, exits 2 with `onward: not checked: <error>` on stderr and the advice, when no Case is left out, to go on with the loop after the findings of `/pre-spec` or to run the check and exit Plan Mode; the advice does not name a call of `/pre-spec`. It does so at most once a stretch, judged by its own refusal in the stretch alone. Before `/pre-spec`, or when it cannot read the `prespec` line, an error of its own exits 0 and does not send the reply back. An empty payload exits 0.
> **－** It counts nothing, calls no model and writes no file and no mark. Its judgment is the marks, the files and their times, the refusals in the transcript and the first word of the reply.
> **－** `uv run --project .guppi guppi onward` without `--plan` keeps its own judgment.

> **tasks:**
> - [ ] update `estimate-prespec-onward-sends-the-agent-on`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether guppi onward --plan, after /pre-spec, refuses the end of a reply that leaves no Case open in the Frontier and sends the agent on with the Cases still out, to the check and the exit or on with the loop after its findings, once a stretch and once more after each reply the ledger hook sent back, an answer with no LEDGER block included, judged by the refusals in the transcript whatever stop_hook_active says; silent before /pre-spec, on a reply that opens with STOP:, and otherwise"
>     ```
>   - change: `the Criterion replaced whole — a Case still out no longer keeps the hook silent; it changes only its reason`
> - [ ] `.guppi/guppi/onward.py`: `plan_onward` no longer returns None when a Case is still out; the module docstring of `guppi onward --plan` drops "no file under cases/ was written after the last decision line" from the conditions of exit 2 and says that a Case still out changes only the reason; the text of `ONLY_THE_PERSON`, which each reason carries, asks for `STOP:` only for a question the person must answer or a Case that waits only for the person's word, and, while a `case-guppi` has not answered, for the end of the turn that `vault/wiki/orchestration.md` sets for a Case out, and the docstring says the same.
> - [ ] `.guppi/tests/test_onward.py`: the tests that asserted exit 0 because a Case was still out — `test_loop_a_case_built_again_and_not_ratified_keeps_it_silent`, `test_supersede_a_case_file_after_its_last_line_keeps_it_silent`, the case `{supersedes:case 5.1}` of `test_supersede_marks_on_each_sub_case_with_lines_retire_the_parent`, `test_plan_a_case_file_newer_than_its_last_decision_line_is_silent`, `test_plan_a_case_with_no_reply_that_ratified_it_is_out` and `test_plan_a_record_with_no_readable_time_counts_none_of_its_lines` — assert exit 2 with the reason of the Cases still out, and are renamed to say so; a new test has a reply that ratifies one Case of two built again after the `prespec` line and asserts exit 2, and one more asserts exit 2 at the answer with no `LEDGER` block to a reminder of the ledger hook while a Case is still out; the tests that tell a Case not out by the exit code alone — `test_supersede_a_mark_in_ledger_md_sends_it_on`, `test_supersede_a_mark_in_a_reply_of_the_transcript_sends_it_on`, `test_supersede_a_mark_in_the_reply_that_ended_sends_it_on`, the case `{supersedes:case 5.1}{supersedes:case 5.2}` of `test_supersede_marks_on_each_sub_case_with_lines_retire_the_parent`, `test_plan_a_case_file_older_than_its_last_decision_line_is_no_case_out`, `test_plan_a_case_ratified_by_an_earlier_reply_of_the_stretch_is_not_out` and `test_plan_a_case_ratified_before_the_persons_last_message_is_not_out` — assert the reason of the exit or of the loop, never the reason of the Cases still out; a test asserts that `ONLY_THE_PERSON` names `orchestration.md` for a `case-guppi` that has not answered and no longer names a Case still out with its `case-guppi` for `STOP:`.
> - [ ] read `estimate-prespec-onward-sends-the-agent-on`

> **ratification:**
> ```
> - decision[case 889.1][update][estimate-prespec-onward-sends-the-agent-on]{ref:rule-prespec-onward}
> ```

### Case 889.2 — The hook names the Cases still out and says what to do

> **given:**
> `estimate-prespec-onward-tells-the-loop-from-its-end`: its Criterion is replaced whole.
> **＋** `rule-prespec-onward`: the rule of the hook, whose Purpose gains the third reason.
> **＋** `.guppi/guppi/onward.py`: the hook `guppi onward --plan` and its judgment of a Case still out.
> **＋** `.guppi/tests/test_onward.py`: the tests of the hook.
> **＋** `rule-one-judgment-one-implementation`: one judgment of a Case still out.
> **＋** `estimate-prespec-onward-sends-the-agent-on`: the check of the text that each reason adds.
> **＋** `/pre-spec`: the skill whose loop after the findings the reasons name.
> **＋** `raw/<date>/<hi HHMM>/cases/`: the folder of the case files, also written `cases/`.
> **＋** `cases/`: the same folder, as the lines of `then` name it short.
> **＋** `.guppi/guppi/prespec.py`: the reading of the `prespec` line.
> **＋** `.guppi/guppi/casecheck.py`: the judgment of an empty case file.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi onward --plan` of `.guppi/guppi/onward.py` receives the end of a reply of the main agent that carries a `LEDGER` block, the event log holds a `prespec` line of this session after its `hi`, and every other condition holds under which the hook sends the agent on.

> **then:**
> When a Case is still out, as `rule-prespec-onward` judges it, the hook exits 2 and tells the agent that the Cases it names by id were built again and are not ratified yet: to send each one that must change to its `case-guppi`, as the loop after the findings of `/pre-spec` sets it. What the agent does when only the person can go on, or while a `case-guppi` has not answered, is the text that each reason adds, as `estimate-prespec-onward-sends-the-agent-on` sets it.
> **＋** It names each Case still out by the N of its file `case-<N>.md` under `raw/<date>/<hi HHMM>/cases/`, found by the one function of `.guppi/guppi/onward.py` that judges whether a Case is still out.
> **＋** When no Case is still out and a file under `raw/<date>/<hi HHMM>/cases/` was written after the last `prespec` line of the session, the hook exits 2 and tells the agent that the Cases built again on the findings of `/pre-spec` are ratified, to run `uv run --project .guppi guppi prespec --check` on the plan file with `--session <id>`, to fix what it prints, and to call `ExitPlanMode` when it prints no finding.
> **＋** When no Case is still out and no file under `cases/` was written after that line, the hook exits 2 and tells the agent to go on with the loop after the findings of `/pre-spec`: to send each finding in a Case to its `case-guppi`, or, when no Case goes back, to run the check and exit as above.
> **＋** The hook reads the time of the `prespec` line, on the date of the event log that holds it, through the one function of `.guppi/guppi/prespec.py` that `window` uses to find the line.
> **＋** One function of `.guppi/guppi/casecheck.py` tells whether a file under `raw/<date>/<hi HHMM>/cases/` holds nothing but blank space, both for this judgment and for the judgment whether a Case is still out.
> **－** While a Case is still out, the hook never tells the agent that the Cases built again are ratified, and never sends it on with the loop alone.
> **－** A reply that writes a defer or a lesson after `/pre-spec` and before any Case is built again never gets the message that the Cases built again are ratified.
> **－** An emptied file under `cases/`, the file of a dropped Case, is never taken for a Case built again after the `prespec` line, nor for a Case still out, whatever its time: with no other file written after that line, the agent is sent on with the loop after the findings.

> **tasks:**
> - [ ] update `rule-prespec-onward`
>   - old: `With the line, when a file under`
>   - new: `With the line and no Case still out, when a file under`
>   - old: `` or, when no Case goes back, to run the check and exit (case 686.1). ``
>   - new: `` or, when no Case goes back, to run the check and exit (case 686.1). When a Case is still out at a reply it would send on, such as a reply that ratifies only some Cases of a batch, it sends the agent on instead with a reason that names each such Case: to send each one that must change to its `case-guppi`, to end the turn as `orchestration.md` sets it for a Case out while a `case-guppi` has not answered, and to open the reply with `STOP:` and ask the person when each waits only for the person's word (as set in case 889.2). ``
>   - change: `a Case still out no longer keeps the hook silent after /pre-spec: a third reason names each such Case and says what to do`
> - [ ] update `estimate-prespec-onward-tells-the-loop-from-its-end`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether guppi onward --plan, after /pre-spec, names each Case still out and sends the agent on with it while one is out, sends the agent to the check and the exit only when no Case is out and a file under cases/ that holds more than blank space was written after the last prespec line of the session, and on with the loop after the findings when none was; the emptied file of a dropped Case counts as none"
>     ```
>   - change: `the Criterion replaced whole — a third reason names each Case still out in place of the silence`
> - [ ] `.guppi/guppi/onward.py`: one function returns the ids of the Cases still out, by the judgment `case_out` makes today, and `case_out` returns whether that list holds any; `plan_onward` returns a third reason, with the ids of that function and the text of `ONLY_THE_PERSON`, when the list holds any, before it chooses between the reason of the exit and the reason of the loop.
> - [ ] `.guppi/tests/test_onward.py`: a test asserts that the third reason names each Case still out by id and none that is not out, that it holds `case-guppi`, `orchestration.md` and `STOP:`, and that it holds neither the reason of the exit nor the reason of the loop; a test asserts that the ids come from the function that `case_out` uses.
> - [ ] read `estimate-prespec-onward-tells-the-loop-from-its-end`

> **ratification:**
> ```
> - decision[case 889.2][update][rule-prespec-onward]{ref:rule-prespec-onward}
> - decision[case 889.2][update][estimate-prespec-onward-tells-the-loop-from-its-end]{ref:rule-prespec-onward}
> ```
