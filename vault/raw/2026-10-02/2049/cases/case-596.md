## Case 596 — The Retro onward hook sends the agent on again after a ledger refusal

> **context:**
> At the end of Retro the agent sends one reply with the readings and lessons in a `LEDGER` block. That reply must end, and the end of a reply hands the turn to the person. The hook of `rule-retro-onward`, `uv run guppi onward` on `Stop`, refuses that ending and sends the agent on to commit the session folder and call `/handoff`. To stay out of a loop, it speaks only once per stretch, from one message of the person to the next. It judges this by its own refusal in the transcript (case 577.1). This goes wrong when the ledger hook refuses a line of the same reply. In session 1834, at the ending of 20:29:52, the transcript holds two refusals. The first is the ledger hook's: the lesson slug lacked the `lesson-` prefix. The second is the onward hook's. The agent answered with a reply that wrote the lesson line again in a `LEDGER` block, so that reply also had to end. At 20:29:58 all six `Stop` hooks were silent, because the onward hook had already used its one refusal. The run then stopped with no condition of `where-to-stop.md` holding, until the person asked at 20:38:54. The `Stop` hooks run side by side at one ending, so the onward hook cannot see a ledger refusal of the same ending. It can see it at the next ending, in the transcript.
>
> The pages and code state the limit to one refusal in several places: the `Purpose` of `rule-retro-onward`, the docstring of `guppi/onward.py`, and the Criterion, `purpose` and `method` of `estimate-retro-onward-sends-the-agent-to-the-handoff`. `rule-retro` and its render `.claude/skills/retro/SKILL.md` say that no `LEDGER` block follows the reply that ends Retro. That sentence forbids the reply the ledger hook's refusal requires. The ledger hook tells each refused line once a stretch (case 577.3), in `untold` of `guppi/ledger.py`. Because of this, a hook that speaks again only after a ledger refusal cannot loop. No `create` is made, so the vault query was not run.
>
> This Case was built again on the findings of `/pre-spec`:
> - `implementation_ref` of `rule-retro-onward` gains `tests/test_ledger.py`.
> - 596.2 replaces the Criterion of `estimate-retro-runs-on-to-the-handoff`, since its line on the one reply that ends Retro speaks of the moment the rewrite reply joins. Its `purpose` and `method`, which state the old promise, are set anew.
> - 596.3 replaces the Criterion of `estimate-retro-onward-exits-2-on-an-error`. Its silence pointed to the judgment of `estimate-retro-onward-sends-the-agent-to-the-handoff`, which 596.1 rewrites to "spent". The error path keeps its own refusal in the stretch alone as its guard. That is a second condition with its own fix, so it is a sub-case of its own. It still takes the stretch and the hook's own refusal from that Estimate, whose definitions 596.1 keeps. Its `purpose` and `method` still hold and stand.
>
> The new Criterion of 596.1 changes the old one in these places only:
> - when the hook speaks: its own refusal is now "spent" rather than standing in the stretch
> - what a refusal is: a refusal of the ledger hook is defined beside the hook's own
> - refusals of other hooks: they neither silence the hook nor send it on again
> - what it judges: it judges the ledger hook's refusals as well as its own
> - the Plan Mode run: it keeps its own judgment, which `rule-prespec-onward` sets
>
> In 596.2 the new and changed lines are these:
> - the rewrite reply that answers a refusal of the ledger hook
> - the run on to `/handoff` after that reply
> - the note that this answer is no stop
>
> In 596.3 the one changed line is the silence after a later ledger refusal. Every other line of the three old Criteria is carried as it stood.
>
> Case 597 of this session takes up `rule-prespec-onward`. Its case file was not written when this Case was built, so it was not read. As the main agent reported it:
> - `uv run guppi onward --plan` drops `stop_hook_active` as its guard.
> - It takes the judgment of 596.1, through the function that 596.1 adds to `guppi/ledger.py`.
> - It leaves `estimate-retro-onward-sends-the-agent-to-the-handoff` untouched.
>
> Frame checks:
> - A Grep of `rule-retro-onward|retro-onward` over the repository outside `vault/archive/` and `vault/raw/` printed these files:
>   - `vault/wiki/where-to-stop.md`, `.claude/skills/retro/SKILL.md`, `guppi/onward.py`, `vault/wiki/brief.md`, `tests/test_onward.py`
>   - `rule-where-to-stop.md`, `rule-retro.md`, `rule-retro-onward.md`, `rule-prespec-onward.md`, `rule-hook-registry.md`, `rule-end-of-work.md`, `log.md`
>   - `estimate-end-of-work-order.md`, both Estimates of the hook, `estimate-retro-loads.md`, `estimate-ask-finds.md`
>   - `decision-case-531.9.md`, `decision-case-555.3.md`, `decision-case-555.4.md`, `decision-case-577.1.md`, `decision-case-577.2.md`
> - The hits read outside History, `log.md` and `brief.md` stay true:
>   - `where-to-stop.md` and the `Purpose` of `rule-where-to-stop` say that the hook lets a reply that opens with `STOP:` end, and that its refusal names the file.
>   - `rule-prespec-onward` says that it does what `rule-retro-onward` does after Retro.
>   - `rule-end-of-work` and `estimate-end-of-work-order` give only its place among the children.
>   - The hits in `estimate-retro-loads` and `estimate-ask-finds` are lines of a past `Result`.
>   - The decision pages only list the pages they changed.
> - A Grep of ``(write|written) (the|it|each) (line|lines) again|no `?LEDGER`? block after|refused line`` over `vault/wiki/rules/`, `.claude/` and `vault/wiki/*.md` printed `.claude/skills/retro/SKILL.md`, `vault/wiki/log.md`, `rule-ledger-write.md` (a History line only) and `rule-retro.md`. The sentence in `rule-retro` and its render is the one that 596.2 changes.
> - `orchestration.md` sets that a reply with a `LEDGER` block ends in that text. That is the reason the rewrite reply ends, so it constrains 596.2 and stands. It also says that readings and lessons from `/work` to the end of Retro go in the one reply that ends Retro. That stands as well: a line the ledger hook refused was not written, and its refusal asks for the line again.
> - `estimate-retro-loads` speaks of readings, not of the replies of Retro, and stands.
>
> Not done:
> - This Case does not change the Plan Mode run. Case 597 does.
> - `rule-ledger-write`, with its backlog line put off by case 442, is not named. Only its code in `guppi/ledger.py` is touched.

> **problem:**
> After the reply that ends Retro, the hook of `rule-retro-onward` speaks once per stretch. When the ledger hook refuses a line of that reply, the agent must answer with a second reply that writes the line again and ends. Nothing then sends the agent on, so the run stops before the commit and `/handoff` where no person is needed. The Retro text also forbids that second reply.

> **recommend:**
> - **Which refusals let the hook send the agent on again**
>   - Recommended: (a) after a refusal of the ledger hook. The hook stays silent only when its own refusal stands and no refusal of the ledger hook stands at the same ending or after it. It stays bounded because the ledger hook refuses each faulty line once a stretch. The change lives in `rule-retro-onward` and `guppi/onward.py`.
>   - Answer: agreed with the recommendation, (a).
> - **Retro's text on the reply that writes a refused line again**
>   - Recommended: (a) add one exception to `rule-retro`: the sentence allows the reply that writes again the lines the ledger hook refused, with nothing else in it. After it, the hook sends the agent on to the commit and `/handoff`.
>   - Answer: agreed with the recommendation, (a).
> - **How the change is checked**
>   - Recommended: (a) replace the promise of `estimate-retro-onward-sends-the-agent-to-the-handoff` whole, with its `purpose` and `method` updated to match. The hand check is read at the first end of Retro where the ledger hook refuses a line. `estimate-retro-onward-exits-2-on-an-error` stands.
>   - Answer: agreed with the recommendation, (a).
> - **The Plan Mode version of the hook**
>   - Recommended: (a) Retro only. The Plan Mode version is left as it is and named as not done.
>   - Answer: agreed with the recommendation, (a).
> - **Change**
>   - Asked: Case 597 of this session drops `stop_hook_active` as the guard of `uv run guppi onward --plan`, and the person agreed. So the line of 596.1 saying that the Plan Mode run keeps that flag as its guard becomes false. It should instead say that the Plan Mode run keeps its own judgment, set by `rule-prespec-onward`, and Case 596 is ratified again.
>   - Taken: the last `－` line of the `then` of 596.1 now says that `uv run guppi onward --plan` keeps its own judgment, set by `rule-prespec-onward`. `given` names the case file of Case 597. `context` says that Case 597 changes the Plan Mode run and leaves the Estimate of 596.1 untouched.

### Case 596.1 — The onward hook speaks again after each reply the ledger hook refused

> **given:**
> `rule-retro-onward` — the rule of the hook, its `Purpose` and `implementation_ref` changed
> **＋** `estimate-retro-onward-sends-the-agent-to-the-handoff` — the promise of the hook, its Criterion, `purpose` and `method` replaced
> **＋** `guppi/onward.py` — the hook, the run without `--plan` changed
> **＋** `guppi/ledger.py` — the one judgment of the stretch and of the refusals in it; the ledger hook tells each refused line once a stretch
> **＋** `tests/test_onward.py` and `tests/test_ledger.py` — the tests of the hook and of the judgment
> **＋** `.claude/settings.json` — registers the hook on `Stop` after the ledger hook; unchanged
> **＋** `raw/<date>/<hi HHMM>/handoff.md` and `/handoff` — the report whose presence silences the hook, and the skill that the reason names
> **＋** `vault/wiki/where-to-stop.md` — the conditions that the reason of the hook names
> **＋** `raw/2026-10-02/2049/cases/case-597.md` — Case 597, which sets the judgment of `uv run guppi onward --plan` in `rule-prespec-onward`

> **when:**
> The `Stop` hook `uv run guppi onward` receives the payload of the end of a reply of the main agent.

> **then:**
> It exits 2 when the event log of the session's window holds the mark `retro` of this session, `raw/<date>/<hi HHMM>/handoff.md` does not stand, the reply that ended does not open with `STOP:`, and its own refusal is not spent.
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. A refusal of a `Stop` hook is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[<command>]: `. Its own command is `uv run guppi onward`, and the command of the ledger hook is `uv run guppi ledger`.
> **＋** Its own refusal is spent when its last refusal stands in the stretch and no refusal of the ledger hook follows the same reply of the agent or a later one. So after a reply that the ledger hook refused, it sends the agent on again at the end of the next reply, the one that writes the refused lines again.
> **＋** A refusal of another `Stop` hook in the stretch neither silences it nor sends it on again, and neither does `stop_hook_active`.
> **＋** Its reason on stderr tells the agent to commit the session folder and call `/handoff`, and, when a condition of `vault/wiki/where-to-stop.md` holds, to open its reply with `STOP:` and ask the person instead.
> **＋** In every other case with no error of its own, it exits 0 and prints nothing. This holds before the mark `retro`, once `handoff.md` stands, once its own refusal is spent, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript.
> **＋** It judges the stretch and the refusals in it by `guppi/ledger.py`, whose function of the stretch the ledger hook calls too.
> **＋** `.claude/settings.json` registers it on `Stop`, after `uv run guppi ledger`, `uv run guppi ratified`, `uv run guppi casecheck` and `uv run guppi context`.
> **－** It counts nothing, reads no test result and calls no model. Its judgment is the mark, the file, the refusals in the transcript and the first word of the reply.
> **－** Without a `hi` of the session in the event log, and with no error of its own, it exits 0.
> **－** It writes no file and no mark.
> **－** `uv run guppi onward --plan` keeps its own judgment, set by `rule-prespec-onward`.

> **tasks:**
> - [ ] update `rule-retro-onward`
>   - set: `{implementation_ref: [guppi/onward.py, guppi/ledger.py, tests/test_onward.py, tests/test_ledger.py, .claude/settings.json]}`
>   - old: `` its own refusal after the person's last message in the transcript, and the first word `STOP:` of the reply — and counts nothing, so it fires at most once a stretch, from one message of the person to the next, and cannot loop. ``
>   - new: `` its own refusals and those of the ledger hook after the person's last message in the transcript, and the first word `STOP:` of the reply — and counts nothing. It fires once a stretch, from one message of the person to the next, and once more after each reply that the ledger hook refused: the agent answers that refusal with a reply that writes the refused lines again, a reply that must end, and in session 1834 the run stopped there (case 596). The ledger hook tells each refused line once a stretch, so the hook cannot loop. ``
>   - old: `` The stretch and its own refusal are judged by one function of `guppi/ledger.py`, which the ledger hook calls too (case 577.1). ``
>   - new: `` The stretch and the refusals in it are judged by `guppi/ledger.py`, whose function of the stretch the ledger hook calls too (cases 577.1, 596). ``
>   - change: `the hook sends the agent on again after each reply that the ledger hook refused; tests/test_ledger.py joins implementation_ref (case 596)`
> - [ ] update `estimate-retro-onward-sends-the-agent-to-the-handoff`
>   - set: `{status: pending, purpose: "Whether guppi onward refuses the end of a reply after the retro mark while handoff.md does not stand, once a stretch and once more after each reply the ledger hook refused, judged by the refusals in the transcript whatever stop_hook_active says, not on a reply that opens with STOP:, and is silent otherwise, counting nothing", method: "uv run pytest tests/test_onward.py tests/test_ledger.py; by hand at the first end of Retro at which the ledger hook refuses a line: the transcript, the event log and handoff.md, recorded in the estimate line"}`
>   - change: `the Criterion replaced whole — the hook speaks again after each reply the ledger hook refused (case 596)`
> - [ ] `guppi/ledger.py`: a function that gives, for the command of a `Stop` hook, its refusals in the stretch, each with the reply of the agent it follows. It is the one judgment `guppi/onward.py` uses for its own refusals and for those of the ledger hook; `own_refusals` keeps its answer.
> - [ ] `guppi/onward.py`: the run without `--plan` exits 0 when its own refusal is spent, judged by that function. The module docstring says so.
> - [ ] `tests/test_onward.py`: a ledger refusal after the same reply as its own last refusal, or after a later reply, sends it on again; a ledger refusal only before that reply, or a refusal of another hook after it, does not.
> - [ ] `tests/test_ledger.py`: the function over a transcript with refusals of two hooks after two replies.
> - [ ] `uv run pytest tests/test_onward.py tests/test_ledger.py`
> - [ ] read `estimate-retro-onward-sends-the-agent-to-the-handoff`

> **ratification:**
> ```
> - decision[case 596.1][update][rule-retro-onward]{ref:rule-retro-onward}
> - decision[case 596.1][update][estimate-retro-onward-sends-the-agent-to-the-handoff]{ref:rule-retro-onward}
> ```

### Case 596.2 — Retro allows the reply that writes refused lines again

> **given:**
> `rule-retro` — the Retro rule, one sentence of its `Render` changed
> **＋** `.claude/skills/retro/SKILL.md` — the render of `rule-retro`
> **＋** `estimate-retro-runs-on-to-the-handoff` — the promise of Retro's run to `/handoff`, its Criterion, `purpose` and `method` replaced
> **＋** `/retro`, `/work` and `/handoff` — the skills before, of and after Retro
> **＋** `raw/<date>/<hi HHMM>/spec.md`, `raw/<date>/<hi HHMM>/work.md` and `raw/<date>/<hi HHMM>/handoff.md` — the Spec, the work record and the report of the session
> **＋** `vault/wiki/where-to-stop.md` — the conditions of a stop
> **＋** `rule-retro-onward` — the hook that sends the agent on after the reply that answers the refusal
> **＋** `rule-orchestration` — a reply with a `LEDGER` block ends in that text

> **when:**
> The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose `raw/<date>/<hi HHMM>/spec.md` holds the tasks of the run.

> **then:**
> Retro asks for no approval: it sorts the boxes of `raw/<date>/<hi HHMM>/spec.md`, reads `raw/<date>/<hi HHMM>/work.md` if it stands — with the Read tool, unless the agent wrote or changed the file itself in the same turn, whose text then counts as read —, takes the readings whose moment has come, and decides which lessons to write.
> **＋** A red test that the agent cannot fix within the ratified work is saved as a patch in the session folder and reverted, with a `lesson[error]` line and a line in `## Debt` of `raw/<date>/<hi HHMM>/handoff.md` that names the patch.
> **＋** The agent commits the work when `make style` is clean and `make test` is green, except for the tests that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` holds.
> **＋** One reply ends Retro: one sentence in the language of the chat that names the commit of the work, then one `LEDGER` block with every reading and lesson of `/work` and Retro; it asks the person nothing.
> **－** That reply shows the person no report: no heading, no list and no other paragraph stands before or after the block, since `raw/<date>/<hi HHMM>/handoff.md` is the report of Retro.
> **＋** When the ledger hook refuses a line of that reply, the agent answers with a reply that holds only a `LEDGER` block with the refused lines written again. No other `LEDGER` block follows the reply that ends Retro.
> **＋** After that reply, or after the reply that answers a refusal of the ledger hook, in the same turn, the agent commits the session folder and calls `/handoff`.
> **－** Retro writes no short defer and ratifies no decision: what needs a decision is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
> **－** Retro stops for the person only on a condition of `vault/wiki/where-to-stop.md`, with a reply that opens with `STOP:` and asks the person instead. The answer to a refusal of the ledger hook is no stop.
> **－** A reading that only the person can take is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question.

> **tasks:**
> - [ ] update `rule-retro`
>   - old: `` Write no `LEDGER` block after that reply. ``
>   - new: `` Write no `LEDGER` block after that reply, except to answer a refusal of the ledger hook: that reply holds only a `LEDGER` block with the refused lines written again, and the hook of `rule-retro-onward` then sends you on again (case 596). ``
>   - change: `the reply that answers a refusal of the ledger hook after the reply that ends Retro holds only the refused lines written again (case 596.2)`
> - [ ] update `estimate-retro-runs-on-to-the-handoff`
>   - set: `{status: pending, purpose: "Whether /retro reviews the session with no report and no approval, writes every reading and lesson of the turn in one reply and a line the ledger hook refused again in one reply that holds only it, commits on green and calls /handoff in the same turn, writes no defer, and stops only on a condition of vault/wiki/where-to-stop.md", method: "by hand at the first run from /work to the librarian after the render, and for the answer to a refusal of the ledger hook at the first Retro where that hook refuses a line: the replies of the turn, the ledger, git log and handoff.md read against the Criterion, recorded in the estimate line"}`
>   - change: `the Criterion replaced whole — a line the ledger hook refuses at the end of Retro is written again in a reply that holds only it, and the run goes on to /handoff (case 596.2)`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] read `estimate-retro-runs-on-to-the-handoff`

> **ratification:**
> ```
> - decision[case 596.2][update][rule-retro]{ref:rule-retro}
> - decision[case 596.2][update][estimate-retro-runs-on-to-the-handoff]{ref:rule-retro}
> ```

### Case 596.3 — The error path of the onward hook stays once a stretch

> **given:**
> `estimate-retro-onward-exits-2-on-an-error` — the promise of the error path of the hook, its Criterion replaced
> **＋** `estimate-retro-onward-sends-the-agent-to-the-handoff` — defines the stretch and the hook's own refusal
> **＋** `rule-retro-onward` — the rule of the hook
> **＋** `guppi/onward.py` — the hook, its error path
> **＋** `tests/test_onward.py` — the tests of the hook
> **＋** `/handoff` — the skill that the advice of the error names

> **when:**
> The `Stop` hook `uv run guppi onward` fires, and an exception rises in `guppi/onward.py` after the hook has read the payload: while it reads the reply, the session folder, the event log or the transcript.

> **then:**
> `guppi onward` exits 2. Its stderr holds `onward: not checked: <error>` and the advice: if Retro has ended and `handoff.md` does not stand, commit the session folder and call `/handoff`.
> **＋** While the cause stands, `guppi onward` blocks with the same error at the first `Stop` of each stretch of the session, before Retro too.
> **－** An empty payload of `guppi onward` exits 0 with nothing on stderr.
> **－** It exits 0 and prints nothing when its own refusal stands in the stretch, as `estimate-retro-onward-sends-the-agent-to-the-handoff` defines the stretch and its own refusal, whatever the ledger hook refused after it. It also exits 0 when `stop_hook_active` is set and it cannot tell whether one stands, so it fires at most once a stretch.
> **－** With no error, `guppi onward` exits 2 or 0 by its own judgment, as before.

> **tasks:**
> - [ ] update `estimate-retro-onward-exits-2-on-an-error`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the error path is judged by its own refusal in the stretch alone, whatever the ledger hook refused after it (case 596.3)`
> - [ ] `guppi/onward.py`: the error path keeps its own refusal in the stretch as its guard, whatever the ledger hook refused after it.
> - [ ] `tests/test_onward.py`: the error path with its own refusal and a later ledger refusal in the stretch exits 0.
> - [ ] `uv run pytest tests/test_onward.py`
> - [ ] read `estimate-retro-onward-exits-2-on-an-error`

> **ratification:**
> ```
> - decision[case 596.3][update][estimate-retro-onward-exits-2-on-an-error]{ref:rule-retro-onward}
> ```
