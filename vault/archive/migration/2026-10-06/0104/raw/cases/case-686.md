## Case 686 — The hook of Plan Mode tells the loop after the findings from its end

> **context:**
> The `Stop` hook `uv run guppi onward --plan` sends the agent on in Plan Mode where no person is needed. It acts at a reply that carries a `LEDGER` block, when no line under `## Cases` of the Frontier is open and no Case is out. Before `/pre-spec` it sends the agent to `/pre-spec`. After it, it says that the Cases built again on the findings are ratified, and sends the agent to the check and the exit. It cannot see whether the loop after the findings has started. So any reply with a `LEDGER` block after `/pre-spec` gets that message, a defer or a lesson in answer to the report too. At the `/pre-spec` of session 0109 the hook said so after the reply of the defer 643, before any Case had gone back to its `case-guppi`. Case 648 put the page `rule-prespec-onward` off on this; its `deferred_by` names `decision-case-648`, so a decision line of Case 686.1 that names the page carries `{supersedes:case 648}`.
> The person chose three things. The hook reads the files under `cases/`: after `/pre-spec`, it sends the agent to the check and the exit only when a Case file was written after the last `prespec` line and no Case is out; when no file was written after that line, it sends the agent on with the loop, to send each finding in a Case to its `case-guppi`, or, when no Case goes back, to the check and the exit. The `/pre-spec` skill, the Render of `rule-prespec`, gains a sentence on what the hook says inside the loop; Case 687, the other item of the batch, closes its Insight with no change of the skill, so the two Cases do not meet there. The new judgment gets its own Estimate, `estimate-prespec-onward-tells-the-loop-from-its-end`, in Case 686.1, and Case 686.2 replaces the Criterion of `estimate-prespec-onward-sends-the-agent-on`, whose line on the reason after `/pre-spec` the change makes false.
> The frame. The time of the `prespec` line is a second reading of the line that `window` of `guppi/prespec.py` finds, so both take it from one function there. The `purpose` of `estimate-prespec-onward-sends-the-agent-on` names only the check and the exit after `/pre-spec`, so Case 686.2 sets it anew; its `method` asks for a reading by hand at a Plan Mode that closes its last Case, which in this session reads the old hook, since the code lands in Work Mode, so it is set to the tests alone, which run in this session (case 670.4); the new Estimate is read the same way. Its exception on an error of the hook keeps its advice, which already holds only when no Case is left open. `estimate-prespec-onward-reads-the-decisions-of-the-session` judges whether a Case is out, which does not change; it stands. The other `Stop` hooks of `.claude/settings.json` stand: `guppi ledger` writes the lines before this hook judges them, and Case 685 adds its reminder at the same `Stop`, which this Case does not touch; `guppi ratified`, `guppi casecheck` and `guppi context` judge other things of the reply; `guppi onward` follows Retro.
> The ledger hook sends a reply back in three ways now: a line it refuses, the reminder of a lesson with no mark that Case 685.1 adds, and the hold of a decision line that the stored Case does not hold, which Case 688.7 adds. The page `rule-prespec-onward` and the Criterion of `estimate-prespec-onward-sends-the-agent-on` said that the agent answers each refusal by writing the refused lines again, which the reminder does not fit, since it is answered by a decision line written again with its mark or by no `LEDGER` block. So Case 686.1 rewrites those sentences of the page, and Case 686.2 does not carry the line of the Criterion on when its own refusal is spent as it stood: it writes it anew, its first sentence kept and its second fitted to the three ways, as it writes anew the line on the reason after `/pre-spec`; `spent` already counts any exit 2 of the ledger hook as its refusal, so the code does not change for it. A pre-spec finding on this Case asked for the fix; the `context` of Case 685 says that `rule-prespec-onward` stands, and that claim goes to its own builder. Case 688.7 changes another sentence of `rule-orchestration` than this Case, and the two new texts do not touch. The judgment of this Case leans on the condition that no Case is out, which `estimate-prespec-onward-reads-the-decisions-of-the-session` sets: a decision line in a `LEDGER` block of a reply counts there, a line that Case 688.7 holds too. That Estimate stands, as the `context` of Case 688 says: a Case is out only until the person ratifies it, the reply that carries a held line acknowledges that ratification, and the held line is a wrong copy that the ledger hook refuses at the same `Stop`, so this hook sends the agent on again after the line is written again. No Estimate and no `then` line of this Case changes for it.
> The searches. A Grep of `rule-prespec-onward` over `vault/wiki/` printed `brief.md`, `backlog.md` and `log.md`, not read, and `orchestration.md`, `rule-orchestration.md`, `rule-prespec.md`, `rule-plan-mode.md`, `estimate-prespec-confirms-the-findings-once.md`, `estimate-retro-onward-sends-the-agent-to-the-handoff.md`, `estimate-prespec-onward-sends-the-agent-on.md`, `estimate-orchestration-defers-in-one-reply.md`, `estimate-prespec-onward-reads-the-decisions-of-the-session.md`, `estimate-orchestration-acknowledging-reply.md` and `estimate-orchestration-shows-the-frontier-after-a-closed-line.md`. The sentence of `rule-orchestration` on the defer reply says the hook sends the agent on to `/pre-spec`, which a defer after `/pre-spec` makes false, so Case 686.1 changes it; Case 685 changes another sentence of that page, and the two new texts do not touch. `orchestration.md` follows at the render. The sentence of `rule-prespec` enters Case 686.1. `rule-plan-mode` names the page as a child. The other sentences of `rule-orchestration` and the three Estimates of orchestration say only that the hook sends the agent on, and `estimate-prespec-confirms-the-findings-once` says it sends the agent to the check and the exit after the ratification of the Cases built again; all stay true and stand. `estimate-retro-onward-sends-the-agent-to-the-handoff` says the hook keeps its own judgment; it stands. A Grep of `rule-prespec-onward` over `guppi/`, `tests/` and `.claude/` printed `.claude/skills/pre-spec/SKILL.md`, which follows at the render, `guppi/prespec.py`, whose docstring names the open lines the hook waits on and stands, and `guppi/onward.py`, whose docstring enters Case 686.1. A Glob of `vault/**/*tells-the-loop*` printed nothing, so the new slug is free.

> **problem:**
> After `/pre-spec`, the hook of `rule-prespec-onward` tells the agent that the Cases built again on the findings are ratified at any reply with a `LEDGER` block, before any Case has gone back to be built again, and sends it to the exit of Plan Mode.

> **recommend:**
> - **How the hook tells the start of the loop after the findings from its end**
>   - Recommended: (a) look for files of rebuilt Cases: the check and the exit only when a Case file was written after the `/pre-spec` run and every such Case is ratified; otherwise on with the loop.
>   - Answer: agreed, (a).
> - **Where this Case stops beside the item on the loop after the findings**
>   - Recommended: (a) only the hook, its rule page and its checks; the text of the `/pre-spec` skill left to the other item.
>   - Answer: (b) the hook and one sentence of the `/pre-spec` skill on what the hook says inside the loop.
> - **What checks the new judgment of the hook**
>   - Recommended: (b) a new check for the new judgment, and the line of `estimate-prespec-onward-sends-the-agent-on` on the message after `/pre-spec` rewritten to point to it; two sub-cases.
>   - Answer: agreed, (b).
> - **Change**
>   - Asked: bring the `context` in line with Case 688 on `estimate-prespec-onward-reads-the-decisions-of-the-session`: the Estimate stands, for the reason Case 688 gives; no Estimate and no `then` line changes.
>   - Taken: the `context` says that the Estimate stands and gives that reason; nothing else changed.

### Case 686.1 — The hook sends the agent on with the loop until a Case is built again

> **given:**
> `rule-prespec-onward`: the rule of the hook.
> **＋** `guppi/onward.py`: the `Stop` hook `uv run guppi onward --plan`.
> **＋** `guppi/prespec.py`: the judgment of the `prespec` line of the event log.
> **＋** `tests/test_onward.py`: the tests of the hook.
> **＋** `estimate-prespec-onward-tells-the-loop-from-its-end`: the new check of the judgment.
> **＋** `rule-prespec`: the `/pre-spec` skill, which names the hook after the loop.
> **＋** `rule-orchestration`: the defer reply, which names the hook.
> **＋** `vault/raw/2026-10-06/0104/cases/case-685.md`: Case 685, which changes another sentence of `rule-orchestration` and adds a reminder at the same `Stop`.
> **＋** `raw/<date>/<hi HHMM>/cases/`: the files of the Cases of the session, whose times the hook reads.
> **＋** `vault/raw/2026-10-06/0104/cases/case-688.md`: Case 688, whose Case 688.7 makes the ledger hook hold a decision line and changes another sentence of `rule-orchestration`.

> **when:**
> The `Stop` hook `uv run guppi onward --plan` of `guppi/onward.py` receives the end of a reply of the main agent that carries a `LEDGER` block, the event log holds a `prespec` line of this session after its `hi`, and every other condition holds under which the hook sends the agent on.

> **then:**
> When a file under `raw/<date>/<hi HHMM>/cases/` was written after the last `prespec` line of the session, the hook exits 2 and tells the agent that the Cases built again on the findings of `/pre-spec` are ratified, to run `uv run guppi prespec --check` on the plan file with `--session <id>`, to fix what it prints, and to call `ExitPlanMode` when it prints no finding.
> **＋** When no file under `cases/` was written after that line, the hook exits 2 and tells the agent to go on with the loop after the findings of `/pre-spec`: to send each finding in a Case to its `case-guppi`, or, when no Case goes back, to run the check and exit as above.
> **＋** The hook reads the time of the `prespec` line, on the date of the event log that holds it, through the one function of `guppi/prespec.py` that `window` uses to find the line.
> **－** A reply that writes a defer or a lesson after `/pre-spec` and before any Case is built again never gets the message that the Cases built again are ratified.
> **－** A Case built again and not yet ratified keeps the hook silent, as before.

> **tasks:**
> - [ ] update `rule-prespec-onward`
>   - old: `` the files under `cases/` against the times of the decision lines ``
>   - new: `` the files under `cases/` against the time of the last `prespec` mark (case 686.1) and the times of the decision lines ``
>   - old: `` With no `prespec` line it sends the agent to `/pre-spec`; with the line it sends the agent to run the check and exit Plan Mode, where the hook of `rule-prespec-hook` refuses the exit while the check prints a finding. ``
>   - new: `` With no `prespec` line it sends the agent to `/pre-spec`. With the line, when a file under `cases/` was written after the last `prespec` mark, it sends the agent to run the check and exit Plan Mode, where the hook of `rule-prespec-hook` refuses the exit while the check prints a finding. When no file under `cases/` was written after that mark, no Case has been built again on the findings yet — the reply wrote a defer or a lesson in answer to the report — and it sends the agent on with the loop after the findings: to send each finding in a Case to its `case-guppi`, or, when no Case goes back, to run the check and exit (case 686.1). ``
>   - old: `It fires once a stretch, and once more after each reply that the ledger hook refused: the agent answers that refusal with a reply that writes the refused lines again, a reply that must end.`
>   - new: `` It fires once a stretch, and once more after each reply that the ledger hook sent back — a line it refused or held, or its reminder of a lesson with no mark (cases 685.1, 688.7): the agent answers with a reply that writes a line again, a reply that must end; an answer with no `LEDGER` block gets no second reason, since the reason given at the same `Stop` as the ledger hook's already stands (case 686.1). ``
>   - old: `The ledger hook tells each refused line once a stretch, so the hook cannot loop.`
>   - new: `The ledger hook tells each refused or held line and each reminder once a stretch, so the hook cannot loop.`
>   - set:
>     ```
>     implementation_ref: [guppi/onward.py, guppi/prespec.py, guppi/ledger.py, guppi/casecheck.py, tests/test_onward.py, tests/test_ledger.py, .claude/settings.json]
>     ```
>   - change: `after /pre-spec the hook sends the agent to the check and the exit only when a Case file was written after the prespec mark, and on with the loop after the findings otherwise; it sends the agent on again after a line the ledger hook held and after its reminder of a lesson with no mark, as after a refused line; the defer of case 648 retired (case 686.1)`
> - [ ] create `estimate-prespec-onward-tells-the-loop-from-its-end`
>   - ref: `rule-prespec-onward`
>   - kind: `QA`
>   - purpose: `Whether guppi onward --plan, after /pre-spec, sends the agent to the check and the exit only when a file under cases/ was written after the last prespec line of the session, and on with the loop after the findings when none was`
>   - method: `uv run pytest tests/test_onward.py — piped payloads, an event log with a prespec line and files under cases/ in a temp vault`
>   - tags: `[session, workflow, hooks, harness]`
> - [ ] update `rule-prespec`
>   - old: `` The hook of `rule-prespec-onward` sends you on after the reply that acknowledges the ratification, and the hook of `rule-prespec-hook` refuses the exit while the check prints a finding (cases 561.3, 561.5). ``
>   - new: `` The hook of `rule-prespec-onward` sends you on after the reply that acknowledges the ratification, and the hook of `rule-prespec-hook` refuses the exit while the check prints a finding (cases 561.3, 561.5). A reply with a `LEDGER` block inside the loop before any Case is built again — a defer or a lesson in answer to the report — is sent on by the same hook too: on with the loop, or, when no Case goes back, to the check and the exit (case 686.1). ``
>   - change: `the hook of rule-prespec-onward sends the agent on with the loop after a reply with a LEDGER block before any Case is built again (case 686.1)`
> - [ ] update `rule-orchestration`
>   - old: `` the hook of `rule-prespec-onward` sends the agent on to `/pre-spec` (case 561.7) ``
>   - new: `` the hook of `rule-prespec-onward` sends the agent on to `/pre-spec`, or, after it, on with the loop after its findings (cases 561.7, 686.1) ``
>   - change: `a defer after /pre-spec is sent on with the loop after its findings (case 686.1)`
> - [ ] `guppi/prespec.py`: one function gives the date and time of the last `prespec` line of the session after its `hi`; `window` finds the line through it.
> - [ ] `guppi/onward.py`: `plan_onward` sends `TO_EXIT` when a file under `cases/` is newer than that moment, and a new reason that sends the agent on with the loop otherwise; the docstring says so.
> - [ ] `tests/test_onward.py`: tests of a reply with a `LEDGER` block after `/pre-spec` with no file under `cases/` written after the `prespec` line, with one written after it and ratified, with one written after it and not ratified, with only files older than the line, of a session across midnight, and of the reply after a reminder of the ledger hook with a `LEDGER` block and with none.
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-prespec-onward-tells-the-loop-from-its-end`

> **ratification:**
> ```
> - decision[case 686.1][update][rule-prespec-onward]{ref:rule-prespec-onward}{supersedes:case 648}
> - decision[case 686.1][create][estimate-prespec-onward-tells-the-loop-from-its-end]{ref:rule-prespec-onward}{tags:session,workflow,hooks,harness}
> - decision[case 686.1][update][rule-prespec]{ref:rule-prespec}
> - decision[case 686.1][update][rule-orchestration]{ref:rule-orchestration}
> ```

### Case 686.2 — The check of the hook points to the new judgment after /pre-spec

> **given:**
> `estimate-prespec-onward-sends-the-agent-on`: its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `guppi/onward.py`: the `Stop` hook `uv run guppi onward --plan`.
> **＋** `estimate-prespec-onward-tells-the-loop-from-its-end`: the check of the reason after `/pre-spec`.
> **＋** `rule-prespec-onward`: the rule of the hook, which judges whether a Case is out.
> **＋** `guppi/ledger.py`: the judgment of the refusals in the transcript.
> **＋** `.claude/settings.json`: the registration of the hook on `Stop`.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec, whose presence silences the hook.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier, whose open lines silence the hook.

> **when:**
> The `Stop` hook `uv run guppi onward --plan` receives the payload of the end of a reply of the main agent.

> **then:**
> It exits 2 when all of these hold: the event log of the session's window holds a `hi` of this session; `raw/<date>/<hi HHMM>/spec.md` does not stand; `raw/<date>/<hi HHMM>/frontier.md` holds no open line under `## Cases`; the reply carries a `LEDGER` block; no Case is still out, as `rule-prespec-onward` judges it; its own refusal is not spent; and the reply does not open with `STOP:`.
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. A refusal of a `Stop` hook is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[<command>]: `. Its own command is `uv run guppi onward --plan`, and the command of the ledger hook is `uv run guppi ledger`.
> **＋** Its own refusal is spent when its last refusal stands in the stretch and no refusal of the ledger hook follows the same reply of the agent or a later one, judged by `guppi/ledger.py`. So after a reply that the ledger hook sent back — a line it refused or held, or its reminder of a lesson with no mark — it sends the agent on again at the end of the next reply that carries a `LEDGER` block, the one that writes a line again; an answer with no `LEDGER` block gets no second reason, since its reason at the same `Stop` as the ledger hook's already stands.
> **＋** A refusal of another `Stop` hook in the stretch neither silences it nor sends it on again, and neither does `stop_hook_active`.
> **＋** With no `prespec` line of this session after its `hi` in the event log, its reason on stderr tells the agent to call `/pre-spec` now. With that line, its reason sends the agent to the check and the exit, or on with the loop after the findings of `/pre-spec`, as `estimate-prespec-onward-tells-the-loop-from-its-end` sets it.
> **＋** Each reason adds that, when only the person can go on — a Case still out with its `case-guppi`, or a question the person must answer — the agent opens its reply with `STOP:` and asks the person instead.
> **＋** In every other case with no error of its own, it exits 0 and prints nothing. This holds once its own refusal is spent, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript.
> **＋** `.claude/settings.json` registers it on `Stop`, after `uv run guppi onward`.
> **－** An error of its own after it has read the payload exits 2 with `onward: not checked: <error>` on stderr and the advice to call `/pre-spec`, or to run the check and exit Plan Mode, when no Case is left open. It does so at most once a stretch, judged by its own refusal in the stretch alone. An empty payload exits 0.
> **－** It counts nothing, calls no model and writes no file and no mark. Its judgment is the marks, the files and their times, the refusals in the transcript and the first word of the reply.
> **－** `uv run guppi onward` without `--plan` keeps its own judgment.

> **tasks:**
> - [ ] update `estimate-prespec-onward-sends-the-agent-on`
>   - set:
>     ```
>     status: pending
>     purpose: Whether guppi onward --plan refuses the end of a reply that leaves no Case open and no Case waiting in Plan Mode, sends the agent to /pre-spec, or after it to the check and the exit or on with the loop after its findings, once a stretch and once more after each reply the ledger hook refused, judged by the refusals in the transcript whatever stop_hook_active says, not on a reply that opens with STOP:, and is silent otherwise
>     method: uv run pytest tests/test_onward.py tests/test_ledger.py, which cover a refusal of the ledger hook
>     ```
>   - change: `the Criterion replaced whole — after /pre-spec the reason sends the agent to the check and the exit, or on with the loop, as estimate-prespec-onward-tells-the-loop-from-its-end sets it; purpose and method set anew (case 686.2)`
> - [ ] read `estimate-prespec-onward-sends-the-agent-on`

> **ratification:**
> ```
> - decision[case 686.2][update][estimate-prespec-onward-sends-the-agent-on]{ref:rule-prespec-onward}
> ```
