## Case 597 — The Plan Mode onward hook goes on after a ledger refusal and after a re-ratification

> **context:**
> The Plan Mode run of the onward hook, `uv run guppi onward --plan` on `Stop`, sends the agent on where no person is needed. After the reply that acknowledges the last ratification, it sends the agent to `/pre-spec`. After the Cases rebuilt on its findings are ratified, it sends the agent to the check and the exit. A reply with a `LEDGER` block must end, so the agent cannot go on in it. To stay out of a loop, the run stays silent while `stop_hook_active` is set, and Claude Code keeps that flag set from any `Stop` hook's refusal until the person's next message (case 577.1). This goes wrong when the ledger hook refuses a line of the acknowledging reply. The agent must answer with a reply that writes the line again in a `LEDGER` block, and that reply ends. At its end the flag is set, the run stays silent, and Plan Mode stops with nobody needed. The Retro run of the same hook stopped this way in session 1834, and Case 596 fixes it there.
>
> The page also carries the decision put off by case 575. It asks whether the run should judge a Case still out by something other than the ledger's last decision line, because a re-ratification with unchanged lines adds no line. Today the run counts the decision lines of the reply that just ended as written now. The reading of session 1237 on `estimate-prespec-onward-sends-the-agent-on` saw it fire after such a re-ratification. A gap remains. When the ledger hook refuses a line of the reply that acknowledges a re-ratification, the next reply rewrites only that line. The ledger then holds only the old times of the Case's lines, so the run judges the rebuilt Case still out. Case 597.2 closes that gap and retires the defer of case 575.
>
> The `Purpose` of `rule-prespec-onward` says three things this Case changes:
> - the run judges only files and the payload, which 597.1 widens to the transcript, in the words of `rule-retro-onward`
> - it judges by the flag and fires at most once a turn, which 597.1 changes, keeping the exit 0 with the flag set and a transcript it cannot read
> - it reads the decision lines of `ledger.md` and of the reply, which 597.2 changes
>
> The page's `implementation_ref` lists only `guppi/onward.py`, `tests/test_onward.py` and `.claude/settings.json`. 597.2 sets it whole, with the modules and tests both sub-cases use. The Criterion, `purpose` and `method` of `estimate-prespec-onward-sends-the-agent-on` state the old guard, so 597.1 replaces them whole. Each old line of that Criterion is carried with new words, with these exceptions:
> - The line on the re-fire is dropped, because the flag is no longer the guard.
> - The clause on the files under `cases/` is now the judgment of 597.2, named through `rule-prespec-onward`.
>
> The `guppi/ledger.py` function that gives each refusal of a `Stop` hook in the stretch with the reply it follows comes from Case 596.1. Work Mode builds it before 597.1 uses it. The time of a transcript record is read by `moment` of `guppi/casecheck.py`, the one reading of that time. Only Estimates with a `ref` are created, so the vault query was not run. The slug `estimate-prespec-onward-reads-the-decisions-of-the-stretch` is free: a Glob of it over `vault/wiki/` and `vault/archive/` found no file. This Case was built again on the findings of `/pre-spec`. They concerned the exception for the flag, the word "transcript" in the `Purpose`, the `implementation_ref`, and the judgment of `rule-spec-write` below.
>
> Frame checks:
> - A Grep of `onward --plan|prespec-onward` over `vault/wiki/` printed these files:
>   - `orchestration.md`, `backlog.md`, `log.md`
>   - `rule-prespec.md`, `rule-prespec-onward.md`, `rule-orchestration.md`, `rule-plan-mode.md`, `rule-hook-registry.md`
>   - `estimate-orchestration-defers-in-one-reply.md`, `estimate-orchestration-acknowledging-reply.md`, `estimate-orchestration-shows-the-frontier-after-a-closed-line.md`, `estimate-prespec-onward-sends-the-agent-on.md`, `estimate-python-utf8-output-intact.md`, `estimate-retro-onward-sends-the-agent-to-the-handoff.md`
>   - `decision-case-575.md`, `decision-case-561.5.md`
> - The same Grep over the repository outside `vault/` printed `.claude/settings.json`, `.claude/skills/pre-spec/SKILL.md`, `tests/test_ledger.py`, `guppi/prespec.py`, `guppi/cli.py`, `tests/test_onward.py` and `guppi/onward.py`.
> - The hits read outside History, `log.md` and `brief.md` stay true:
>   - `orchestration.md`, `rule-orchestration` and its three Estimates say that a reply with a `LEDGER` block ends with the Frontier and the hook sends the agent on.
>   - `rule-prespec` and `.claude/skills/pre-spec/SKILL.md` say the hook sends the agent on after the acknowledging reply.
>   - `rule-plan-mode`, `rule-hook-registry`, `settings.json` and `guppi/cli.py` give only its place and its registration.
>   - `guppi/prespec.py` names the open lines the hook waits on.
>   - `tests/test_ledger.py` uses its refusal as another hook's refusal.
>   - `estimate-python-utf8-output-intact` holds a past `Result`.
> - In `estimate-retro-onward-sends-the-agent-to-the-handoff`, the line that keeps the flag as the guard of `--plan` is changed by Case 596, rebuilt by its own `case-guppi` on the person's answer. This Case does not name that Estimate.
> - A Grep of ``stop_hook_active|writes? (the|it|each) (line|lines) again|refused line`` over `.claude/`, `vault/wiki/rules/` and `vault/wiki/*.md` printed `log.md`, `rule-ledger-write.md`, `rule-case-check.md`, `rule-retro-onward.md`, `rule-prespec-onward.md` and `rule-spec-write.md`. All four other rules stay as they are:
>   - `rule-ledger-write` sets the guard of its own hook by its own refusals.
>   - `rule-case-check` sets its guard by its store.
>   - `rule-retro-onward` sets the guard of the run without `--plan`.
>   - `rule-spec-write` exits 0 on the re-fire of its own hook.
>
>   `orchestration.md` lets the agent's answer to a refusal by a hook other than the ledger hook call tools, and that stands.
>
> Estimates:
> - `estimate-retro-onward-exits-2-on-an-error` stands: `--plan` appears there only in a past `Result`.
> - The three Estimates of `rule-orchestration` named above stand: they promise only that the reply ends with the Frontier.
>
> Not done:
> - `rule-ledger-write`, with its defer by case 442, is not named. This Case only uses the `guppi/ledger.py` function set by 596.1.

> **problem:**
> The Plan Mode run of the onward hook stays silent after any refusal in the stretch. When the ledger hook refuses a line of the acknowledging reply, Plan Mode stops before `/pre-spec` or the exit, although nobody is needed. After a re-ratification, the reply that rewrites a refused line carries none of the Case's decision lines, so the run would judge the Case still out. The decision of case 575 on that judgment stands open.

> **recommend:**
> - **What guards the Plan Mode run against a loop**
>   - Recommended: (a) the Retro judgment. The run speaks once per stretch and once more after each reply the ledger hook refused. The flag and refusals of other hooks neither silence it nor send it on. It reads the refusals with the function the Retro fix adds to `guppi/ledger.py`. An error of its own exits 2 at most once a stretch.
>   - Answer: agreed with the recommendation, (a).
> - **How the hook judges that a rebuilt Case is still out**
>   - Recommended: (a) read the decisions of the whole stretch. The decision lines of every reply since the person's last message count, each at the time of its record in the transcript. The defer of case 575 is closed by this change.
>   - Answer: agreed with the recommendation, (a).
> - **The line in the Retro fix that says the Plan Mode run keeps the flag**
>   - Recommended: (a) rebuild the Retro fix. Case 596 goes back to its `case-guppi`, and the line says that `--plan` keeps its own judgment, set by `rule-prespec-onward`. This Case does not touch that Estimate.
>   - Answer: agreed with the recommendation, (a).
> - **How the change is checked: one promise or two**
>   - Recommended: (a) two sub-cases. 597.1 replaces the promise of `estimate-prespec-onward-sends-the-agent-on`. 597.2 creates `estimate-prespec-onward-reads-the-decisions-of-the-stretch`. Each has its own tests and its own check by hand.
>   - Answer: agreed with the recommendation, (a).

### Case 597.1 — The Plan Mode run speaks again after each reply the ledger hook refused

> **given:**
> `rule-prespec-onward` — the rule of the hook, its `Purpose` changed
> **＋** `estimate-prespec-onward-sends-the-agent-on` — the promise of the hook, its Criterion, `purpose` and `method` replaced
> **＋** `guppi/onward.py` and `tests/test_onward.py` — the hook, its run with `--plan` changed, and its tests
> **＋** `guppi/ledger.py` — the function of the refusals of a `Stop` hook in the stretch, each with the reply it follows; the ledger hook tells each refused line once a stretch
> **＋** `raw/2026-10-02/2049/cases/case-596.md` — the Retro fix, which adds that function and sets the same judgment for the run without `--plan`
> **＋** `.claude/settings.json` — registers the hook on `Stop` after `uv run guppi onward`; unchanged
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec of the session, whose presence silences the hook
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier, whose open lines under `## Cases` silence the hook
> **＋** `/pre-spec`, `uv run guppi prespec --check` and `ExitPlanMode` — the steps the reasons of the hook name

> **when:**
> The `Stop` hook `uv run guppi onward --plan` receives the payload of the end of a reply of the main agent.

> **then:**
> It exits 2 when all of these hold: the event log of the session's window holds a `hi` of this session; `raw/<date>/<hi HHMM>/spec.md` does not stand; `raw/<date>/<hi HHMM>/frontier.md` holds no open line under `## Cases`; the reply carries a `LEDGER` block; no Case is still out, as `rule-prespec-onward` judges it; its own refusal is not spent; and the reply does not open with `STOP:`.
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. A refusal of a `Stop` hook is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[<command>]: `. Its own command is `uv run guppi onward --plan`, and the command of the ledger hook is `uv run guppi ledger`.
> **＋** Its own refusal is spent when its last refusal stands in the stretch and no refusal of the ledger hook follows the same reply of the agent or a later one, judged by `guppi/ledger.py`. So after a reply that the ledger hook refused, it sends the agent on again at the end of the next reply, the one that writes the refused lines again.
> **＋** A refusal of another `Stop` hook in the stretch neither silences it nor sends it on again, and neither does `stop_hook_active`.
> **＋** With no `prespec` line of this session after its `hi` in the event log, its reason on stderr tells the agent to call `/pre-spec` now. With that line, its reason tells the agent to run `uv run guppi prespec --check` on the plan file with `--session <id>`, to fix what it prints, and to call `ExitPlanMode` when it prints no finding.
> **＋** Each reason adds that, when only the person can go on — a Case still out with its `case-guppi`, or a question the person must answer — the agent opens its reply with `STOP:` and asks the person instead.
> **＋** In every other case with no error of its own, it exits 0 and prints nothing. This holds once its own refusal is spent, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript.
> **＋** `.claude/settings.json` registers it on `Stop`, after `uv run guppi onward`.
> **－** An error of its own after it has read the payload exits 2 with `onward: not checked: <error>` on stderr and the advice to call `/pre-spec`, or to run the check and exit Plan Mode, when no Case is left open. It does so at most once a stretch, judged by its own refusal in the stretch alone. An empty payload exits 0.
> **－** It counts nothing, calls no model and writes no file and no mark. Its judgment is the marks, the files and their times, the refusals in the transcript and the first word of the reply.
> **－** `uv run guppi onward` without `--plan` keeps its own judgment.

> **tasks:**
> - [ ] update `rule-prespec-onward`
>   - old: `It judges only the state of files and of the payload —`
>   - new: `It judges only the state of files, of the payload and of the transcript —`
>   - old: `` the flag `stop_hook_active` and the first word `STOP:` of the reply — and counts nothing, so it fires at most once a turn and cannot loop. ``
>   - new: `` its own refusals and those of the ledger hook in the stretch, from the person's last message, and the first word `STOP:` of the reply — and counts nothing. It fires once a stretch, and once more after each reply that the ledger hook refused: the agent answers that refusal with a reply that writes the refused lines again, a reply that must end. The flag `stop_hook_active` and the refusals of other hooks neither silence it nor send it on; with the flag set and a transcript it cannot read, it exits 0 (case 597.1). The ledger hook tells each refused line once a stretch, so the hook cannot loop. ``
>   - old: `and on the re-fire it exits 0.`
>   - new: `at most once a stretch, judged by its own refusal in the stretch alone (case 597.1).`
>   - change: `the run speaks again after each reply the ledger hook refused, judged by the refusals in the transcript, not by stop_hook_active (case 597.1)`
> - [ ] update `estimate-prespec-onward-sends-the-agent-on`
>   - set: `{status: pending, purpose: "Whether guppi onward --plan refuses the end of a reply that leaves no Case open and no Case waiting in Plan Mode, sends the agent to /pre-spec or to the check and the exit, once a stretch and once more after each reply the ledger hook refused, judged by the refusals in the transcript whatever stop_hook_active says, not on a reply that opens with STOP:, and is silent otherwise", method: "uv run pytest tests/test_onward.py tests/test_ledger.py; by hand at the first Plan Mode at which the ledger hook refuses a line of the reply that acknowledges the last ratification: the transcript, the event log and frontier.md, recorded in the estimate line"}`
>   - change: `the Criterion replaced whole — the run speaks again after each reply the ledger hook refused (case 597.1)`
> - [ ] `guppi/onward.py`: the run with `--plan` exits 0 when its own refusal is spent, judged by the function of `guppi/ledger.py` that Case 596.1 adds, with the command `uv run guppi onward --plan`. `stop_hook_active` stays a guard only when the transcript cannot be read. The error path keeps its own refusal in the stretch as its guard. The module docstring says so.
> - [ ] `tests/test_onward.py`: with the flag set and a refusal of another hook in the stretch, it sends the agent on. A ledger refusal after the same reply as its own last refusal, or after a later reply, sends it on again. Its own refusal with no later ledger refusal is silent. The flag set with a transcript it cannot read is silent. The error path with its own refusal in the stretch exits 0.
> - [ ] `uv run pytest tests/test_onward.py tests/test_ledger.py`
> - [ ] read `estimate-prespec-onward-sends-the-agent-on`

> **ratification:**
> ```
> - decision[case 597.1][update][rule-prespec-onward]{ref:rule-prespec-onward}
> - decision[case 597.1][update][estimate-prespec-onward-sends-the-agent-on]{ref:rule-prespec-onward}
> ```

### Case 597.2 — The Plan Mode run reads the decision lines of every reply of the stretch

> **given:**
> `rule-prespec-onward` — the rule of the hook, its `Purpose` and `implementation_ref` changed; the defer of case 575 retired
> **＋** `estimate-prespec-onward-reads-the-decisions-of-the-stretch` — the new promise
> **＋** `guppi/onward.py` and `tests/test_onward.py` — the judgment of a Case still out, and its tests
> **＋** `guppi/ledger.py` and `tests/test_ledger.py` — the stretch and the reading of the transcript records, and their tests; unchanged by this sub-case
> **＋** `raw/2026-10-02/2049/cases/case-596.md` — the Retro fix, which sets the function of the stretch in `guppi/ledger.py`
> **＋** `guppi/casecheck.py` — `moment`, the one reading of the time of a transcript record
> **＋** `.claude/settings.json` — registers the hook; unchanged, named in `implementation_ref`
> **＋** `raw/<date>/<hi HHMM>/cases/` — the case files, whose times the hook reads
> **＋** `raw/<date>/<hi HHMM>/ledger.md` — the session's ledger, whose timed decision lines the hook reads
> **＋** `estimate-prespec-onward-sends-the-agent-on` — the promise of 597.1, which leaves this judgment to `rule-prespec-onward`

> **when:**
> The `Stop` hook `uv run guppi onward --plan` judges, at the end of a reply of the main agent, whether a Case is still out.

> **then:**
> A Case N is still out when a file `case-<N>.md` under `raw/<date>/<hi HHMM>/cases/` was written after the last decision line of Case N or of a sub-case of N.
> **＋** The decision lines it reads are the timed lines of `raw/<date>/<hi HHMM>/ledger.md`, the lines inside a `LEDGER` block of each reply of the main agent in the stretch, and those of the reply that ended.
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`.
> **＋** A line of a reply in the stretch counts at the time of its record in the transcript, read by `moment` of `guppi/casecheck.py`. A line of the reply that ended counts as written now.
> **＋** A line of `ledger.md` counts at its time on the `hi` date, rolled to the next date when the time runs backwards.
> **＋** So a Case built again and ratified by a reply whose decision lines the ledger already held is not out after that reply, and not at any later reply of the stretch either. This includes the reply that writes again a line the ledger hook refused.
> **－** A file of a Case with no decision line is out.
> **－** A record whose time cannot be read counts none of its lines. A transcript that cannot be read leaves `ledger.md` and the reply that ended as the only sources.

> **tasks:**
> - [ ] update `rule-prespec-onward`
>   - set: `{implementation_ref: [guppi/onward.py, guppi/ledger.py, guppi/casecheck.py, tests/test_onward.py, tests/test_ledger.py, .claude/settings.json]}`
>   - old: `` the files under `cases/` against the times of the decision lines in `ledger.md` and in the reply, ``
>   - new: `` the files under `cases/` against the times of the decision lines in `ledger.md` and in the replies since the person's last message, each at the time of its record in the transcript, the reply that ended counted as now (case 597.2), ``
>   - change: `a Case is out by the decision lines of every reply of the stretch, so a re-ratification counts after a ledger refusal too; implementation_ref names the modules and tests the hook uses (case 597.2)`
> - [ ] create `estimate-prespec-onward-reads-the-decisions-of-the-stretch`
>   - type: `estimate`
>   - ref: `rule-prespec-onward`
>   - kind: `QA`
>   - purpose: `Whether guppi onward --plan judges a Case out by the decision lines of ledger.md and of every reply since the person's last message, each at the time of its record, so that a re-ratification with lines the ledger already held counts at every later reply of the stretch`
>   - method: `uv run pytest tests/test_onward.py; by hand at the first re-ratification in Plan Mode after the change: the transcript, ledger.md and the times of the files under cases/, recorded in the estimate line`
>   - tags: `[session, workflow, hooks, harness]`
> - [ ] `guppi/onward.py`: `last_decisions` also reads the decision lines of each main-agent reply of the stretch, by the function of the stretch in `guppi/ledger.py` and `ledger_lines`, each at the time of its record by `moment` of `guppi/casecheck.py`. The module docstring says so.
> - [ ] `tests/test_onward.py`: a Case file newer than its ledger lines and older than a reply of the stretch that carried them is not out at a later reply with only a lesson line. The same Case with no such reply is out. A record with no readable time counts none of its lines.
> - [ ] `uv run pytest tests/test_onward.py`
> - [ ] read `estimate-prespec-onward-reads-the-decisions-of-the-stretch`

> **ratification:**
> ```
> - decision[case 597.2][update][rule-prespec-onward]{ref:rule-prespec-onward}{supersedes:case 575}
> - decision[case 597.2][create][estimate-prespec-onward-reads-the-decisions-of-the-stretch]{ref:rule-prespec-onward}{tags:session,workflow,hooks,harness}
> ```
