<!-- approved 22:36:36 · session b878e1fe -->

# Spec — session 2049, 2026-10-02

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

```then
update:
- slug: rule-retro-onward
  set:
    implementation_ref:
    - guppi/onward.py
    - guppi/ledger.py
    - tests/test_onward.py
    - tests/test_ledger.py
    - .claude/settings.json
  replace:
  - old: its own refusal after the person's last message in the transcript, and the first word `STOP:` of the reply — and counts nothing, so it fires at most once a stretch, from one message of the person to the next, and cannot loop.
    new: 'its own refusals and those of the ledger hook after the person''s last message in the transcript, and the first word `STOP:` of the reply — and counts nothing. It fires once a stretch, from one message of the person to the next, and once more after each reply that the ledger hook refused: the agent answers that refusal with a reply that writes the refused lines again, a reply that must end, and in session 1834 the run stopped there (case 596). The ledger hook tells each refused line once a stretch, so the hook cannot loop.'
  - old: The stretch and its own refusal are judged by one function of `guppi/ledger.py`, which the ledger hook calls too (case 577.1).
    new: The stretch and the refusals in it are judged by `guppi/ledger.py`, whose function of the stretch the ledger hook calls too (cases 577.1, 596).
  change: the hook sends the agent on again after each reply that the ledger hook refused; tests/test_ledger.py joins implementation_ref (case 596)
- slug: estimate-retro-onward-sends-the-agent-to-the-handoff
  set:
    status: pending
    purpose: Whether guppi onward refuses the end of a reply after the retro mark while handoff.md does not stand, once a stretch and once more after each reply the ledger hook refused, judged by the refusals in the transcript whatever stop_hook_active says, not on a reply that opens with STOP:, and is silent otherwise, counting nothing
    method: 'uv run pytest tests/test_onward.py tests/test_ledger.py; by hand at the first end of Retro at which the ledger hook refuses a line: the transcript, the event log and handoff.md, recorded in the estimate line'
  change: the Criterion replaced whole — the hook speaks again after each reply the ledger hook refused (case 596)
```

```tasks
- [x] update `rule-retro-onward`
- [x] update `estimate-retro-onward-sends-the-agent-to-the-handoff`
- [x] `guppi/ledger.py`: a function that gives, for the command of a `Stop` hook, its refusals in the stretch, each with the reply of the agent it follows. It is the one judgment `guppi/onward.py` uses for its own refusals and for those of the ledger hook; `own_refusals` keeps its answer.
- [x] `guppi/onward.py`: the run without `--plan` exits 0 when its own refusal is spent, judged by that function. The module docstring says so.
- [x] `tests/test_onward.py`: a ledger refusal after the same reply as its own last refusal, or after a later reply, sends it on again; a ledger refusal only before that reply, or a refusal of another hook after it, does not.
- [x] `tests/test_ledger.py`: the function over a transcript with refusals of two hooks after two replies.
- [x] `uv run pytest tests/test_onward.py tests/test_ledger.py`
- [ ] read `estimate-retro-onward-sends-the-agent-to-the-handoff`
```

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

```then
update:
- slug: rule-retro
  replace:
  - old: Write no `LEDGER` block after that reply.
    new: 'Write no `LEDGER` block after that reply, except to answer a refusal of the ledger hook: that reply holds only a `LEDGER` block with the refused lines written again, and the hook of `rule-retro-onward` then sends you on again (case 596).'
  change: the reply that answers a refusal of the ledger hook after the reply that ends Retro holds only the refused lines written again (case 596.2)
- slug: estimate-retro-runs-on-to-the-handoff
  set:
    status: pending
    purpose: Whether /retro reviews the session with no report and no approval, writes every reading and lesson of the turn in one reply and a line the ledger hook refused again in one reply that holds only it, commits on green and calls /handoff in the same turn, writes no defer, and stops only on a condition of vault/wiki/where-to-stop.md
    method: 'by hand at the first run from /work to the librarian after the render, and for the answer to a refusal of the ledger hook at the first Retro where that hook refuses a line: the replies of the turn, the ledger, git log and handoff.md read against the Criterion, recorded in the estimate line'
  change: the Criterion replaced whole — a line the ledger hook refuses at the end of Retro is written again in a reply that holds only it, and the run goes on to /handoff (case 596.2)
```

```tasks
- [x] update `rule-retro`
- [x] update `estimate-retro-runs-on-to-the-handoff`
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-runs-on-to-the-handoff`
```

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

```then
update:
- slug: estimate-retro-onward-exits-2-on-an-error
  set:
    status: pending
  change: the Criterion replaced whole — the error path is judged by its own refusal in the stretch alone, whatever the ledger hook refused after it (case 596.3)
```

```tasks
- [x] update `estimate-retro-onward-exits-2-on-an-error`
- [x] `guppi/onward.py`: the error path keeps its own refusal in the stretch as its guard, whatever the ledger hook refused after it.
- [x] `tests/test_onward.py`: the error path with its own refusal and a later ledger refusal in the stretch exits 0.
- [x] `uv run pytest tests/test_onward.py`
- [x] read `estimate-retro-onward-exits-2-on-an-error`
```

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

```then
update:
- slug: rule-prespec-onward
  replace:
  - old: It judges only the state of files and of the payload —
    new: It judges only the state of files, of the payload and of the transcript —
  - old: the flag `stop_hook_active` and the first word `STOP:` of the reply — and counts nothing, so it fires at most once a turn and cannot loop.
    new: 'its own refusals and those of the ledger hook in the stretch, from the person''s last message, and the first word `STOP:` of the reply — and counts nothing. It fires once a stretch, and once more after each reply that the ledger hook refused: the agent answers that refusal with a reply that writes the refused lines again, a reply that must end. The flag `stop_hook_active` and the refusals of other hooks neither silence it nor send it on; with the flag set and a transcript it cannot read, it exits 0 (case 597.1). The ledger hook tells each refused line once a stretch, so the hook cannot loop.'
  - old: and on the re-fire it exits 0.
    new: at most once a stretch, judged by its own refusal in the stretch alone (case 597.1).
  change: the run speaks again after each reply the ledger hook refused, judged by the refusals in the transcript, not by stop_hook_active (case 597.1)
- slug: estimate-prespec-onward-sends-the-agent-on
  set:
    status: pending
    purpose: Whether guppi onward --plan refuses the end of a reply that leaves no Case open and no Case waiting in Plan Mode, sends the agent to /pre-spec or to the check and the exit, once a stretch and once more after each reply the ledger hook refused, judged by the refusals in the transcript whatever stop_hook_active says, not on a reply that opens with STOP:, and is silent otherwise
    method: 'uv run pytest tests/test_onward.py tests/test_ledger.py; by hand at the first Plan Mode at which the ledger hook refuses a line of the reply that acknowledges the last ratification: the transcript, the event log and frontier.md, recorded in the estimate line'
  change: the Criterion replaced whole — the run speaks again after each reply the ledger hook refused (case 597.1)
```

```tasks
- [x] update `rule-prespec-onward`
- [x] update `estimate-prespec-onward-sends-the-agent-on`
- [x] `guppi/onward.py`: the run with `--plan` exits 0 when its own refusal is spent, judged by the function of `guppi/ledger.py` that Case 596.1 adds, with the command `uv run guppi onward --plan`. `stop_hook_active` stays a guard only when the transcript cannot be read. The error path keeps its own refusal in the stretch as its guard. The module docstring says so.
- [x] `tests/test_onward.py`: with the flag set and a refusal of another hook in the stretch, it sends the agent on. A ledger refusal after the same reply as its own last refusal, or after a later reply, sends it on again. Its own refusal with no later ledger refusal is silent. The flag set with a transcript it cannot read is silent. The error path with its own refusal in the stretch exits 0.
- [x] `uv run pytest tests/test_onward.py tests/test_ledger.py`
- [ ] read `estimate-prespec-onward-sends-the-agent-on`
```

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

```then
create:
- slug: estimate-prespec-onward-reads-the-decisions-of-the-stretch
  type: estimate
  ref: rule-prespec-onward
  kind: QA
  purpose: Whether guppi onward --plan judges a Case out by the decision lines of ledger.md and of every reply since the person's last message, each at the time of its record, so that a re-ratification with lines the ledger already held counts at every later reply of the stretch
  method: 'uv run pytest tests/test_onward.py; by hand at the first re-ratification in Plan Mode after the change: the transcript, ledger.md and the times of the files under cases/, recorded in the estimate line'
  tags:
  - session
  - workflow
  - hooks
  - harness
update:
- slug: rule-prespec-onward
  set:
    implementation_ref:
    - guppi/onward.py
    - guppi/ledger.py
    - guppi/casecheck.py
    - tests/test_onward.py
    - tests/test_ledger.py
    - .claude/settings.json
  replace:
  - old: the files under `cases/` against the times of the decision lines in `ledger.md` and in the reply,
    new: the files under `cases/` against the times of the decision lines in `ledger.md` and in the replies since the person's last message, each at the time of its record in the transcript, the reply that ended counted as now (case 597.2),
  change: a Case is out by the decision lines of every reply of the stretch, so a re-ratification counts after a ledger refusal too; implementation_ref names the modules and tests the hook uses (case 597.2)
```

```tasks
- [x] update `rule-prespec-onward`
- [x] create `estimate-prespec-onward-reads-the-decisions-of-the-stretch`
- [x] `guppi/onward.py`: `last_decisions` also reads the decision lines of each main-agent reply of the stretch, by the function of the stretch in `guppi/ledger.py` and `ledger_lines`, each at the time of its record by `moment` of `guppi/casecheck.py`. The module docstring says so.
- [x] `tests/test_onward.py`: a Case file newer than its ledger lines and older than a reply of the stretch that carried them is not out at a later reply with only a lesson line. The same Case with no such reply is out. A record with no readable time counts none of its lines.
- [x] `uv run pytest tests/test_onward.py`
- [ ] read `estimate-prespec-onward-reads-the-decisions-of-the-stretch`
```

## Case 598 — Cases handled side by side are signed together

> **context:**
> In Plan Mode the main agent takes Frontier items one at a time. It shows one Case per reply and does not move to the next item until that Case is ratified or deferred. The one exception is the loop after the findings of `/pre-spec`: there the Cases built again go out in one reply and are ratified once (case 561.2). The rule goes wrong when a new Case shows that a Case already ratified must change. In session 2049, the round on Case 597 found that a line of Case 596.1 would become false. Case 596 was built again and ratified again in a reply of its own, and Case 597 was then shown and ratified in the next reply. That was two sign-offs for one connected change. The person ruled that items stay one at a time and each Case is ratified after it is discussed. When Cases are handled side by side, the agent waits for the whole batch and shows them together for one ratification. This covers the pre-spec loop and the case where an earlier Case must change because of a new one.
>
> `orchestration.md` holds the rule in `## Plan Mode and the Frontier`. Case 598.1 adds the batch there and in `## Showing and signing a Case`, and names both exceptions to one Case per reply: the pre-spec loop and the batch. A batch runs the steps of the pre-spec loop, so its tools already exist:
> - The docstring of `guppi/casecheck.py` lets a reply that opens with a bold label ending in a colon pass the round check, and that is the `**Waiting:**` line.
> - The same docstring compares each Case a reply shows under its heading and asks for the sending of its file, so several top-level Cases in one reply pass when each file is sent.
> - The Result of `estimate-prespec-gathers-the-answers-after-findings` (session 1202) shows four rebuilt Cases in one reply, ratified once, with no refusal.
>
> The sentence of `## Showing and signing a Case` on sub-cases already says how one reply acknowledges sub-cases ratified together: one `LEDGER` block, one heading that names the ids, one Frontier (case 355.2). 598.2 widens that sentence to every Case ratified in one answer, so that the rule has one wording. The Criterion of `estimate-prespec-gathers-the-answers-after-findings` has a line saying that outside its loop no Case is taken up before the current one is ratified. A batch makes that line false, so 598.3 replaces it. The sentence of `rule-prespec` that lifts the one-at-a-time rule inside its loop stays true and is not changed. The `purpose` of that Estimate speaks only of the loop and stands, and so does its `method`. The `purpose` of `estimate-orchestration-acknowledging-reply` stays true. Its `method` reads only the first acknowledging reply of a session, which may hold no batch, so 598.2 adds to it the first reply that acknowledges Cases ratified together.
>
> This Case was built again on findings 4 and 5 of `/pre-spec`. Finding 4: the first replace of 598.1 named the batch as the only exception and left out the pre-spec loop. Finding 5: 598.2 added a second wording of the sub-case sentence instead of widening it. 598.1 and 598.2 now change the same paragraph of `## Showing and signing a Case` at two anchors that do not overlap. Read side by side, the paragraph says that one reply acknowledges every Case ratified in one answer, and that a Case the person questions goes back and is shown again.
>
> The new Criteria change the old ones in these places only:
> - In `estimate-orchestration-acknowledging-reply`, the `when` adds Cases ratified together in one answer.
> - In the same Estimate, the line on a Case with sub-cases now covers every Case ratified in one answer, with one paragraph `Changes:`.
> - In `estimate-prespec-gathers-the-answers-after-findings`, the line on what holds outside the loop now points to the batch of `orchestration.md`.
>
> Every other line is carried as it stood. The `then` of 598.1 repeats the steps of the loop of 598.3 on purpose: the batch takes those steps, and each Estimate checks them at its own trigger. 598.1 checks them after the person's word on a ratified Case, and 598.3 checks them after the findings of `/pre-spec`.
>
> Case 597 sets what the hook of `rule-prespec-onward` does after the acknowledging reply, and this Case leaves that unchanged. In a batch the line of the new Case under `## Cases` stays open until the batch is ratified, so that hook stays silent. Once the batch is ratified, 597.2 counts the decision lines of the reply as written. Case 596 sets the Retro run and does not touch this moment. A batch in Work Mode is not covered. The person spoke of the work on the Frontier.
>
> The one `create` has a `ref`, so the vault query was not run. A Glob of `vault/{wiki,archive}/**/estimate-orchestration-signs-a-batch-together.md` found no file, so the slug is free.
>
> Frame checks:
> - A Grep of ``[Oo]ne reply shows one Case|one Case at a time|next Case until|ratified or deferred|for one ratification|one ratification`` ran over the repository outside `vault/archive/` and `vault/raw/`. It printed these files:
>   - `.claude/skills/pre-spec/SKILL.md`, `rule-prespec.md`, `estimate-prespec-gathers-the-answers-after-findings.md`
>   - `orchestration.md`, `rule-orchestration.md`, `estimate-orchestration-shows-the-built-case.md`
>   - `glossary.md`, `entity-glossary.md`, `log.md`, `tests/test_ratified.py`
>   - `estimate-case-check-shows-only-the-checked-case.md`, `rule-case-protocol.md` and `rule-case-check.md`, each a History line only
>   - `lesson-case-showing-ratification-fence-outside-the-blockquote.md`, `decision-case-52.2.md`, `decision-case-561.md`
> - The hits read outside History and `log.md` stay true:
>   - The glossary entry Plan Mode says items are worked one by one, and that stays true.
>   - The pre-spec skill describes its own loop.
>   - The test and the lesson concern one `ratification` under one heading.
>   - `estimate-orchestration-shows-the-built-case` describes the showing that each Case of a batch keeps.
>   - The decision pages were not read.
> - A Grep of ``ratified again|re-ratification|shown again|ratifies them all|names the ids`` over `vault/wiki/rules/`, `.claude/` and `vault/wiki/*.md` printed these files:
>   - `brief.md`, `backlog.md`, `orchestration.md`, `case-schema.md`, `log.md`
>   - `rule-prespec.md` (a History line), `rule-orchestration.md`, `rule-case-protocol.md`, `rule-ledger-line-withdrawn-on-re-ratification.md`
> - The hits read outside History, `log.md` and `brief.md` stay true. The backlog lines and `rule-ledger-line-withdrawn-on-re-ratification` concern ledger lines of a re-ratification. `case-schema.md` and its rule say that `case-guppi` builds a Case at every showing again.
> - A Grep of `rule-orchestration|orchestration\.md` over the repository outside `vault/archive/` and `vault/raw/` printed 49 files. A Grep of ``one Case|next Case|item by item|one at a time|together`` then ran over the rule, estimate and skill pages among them that are not named above:
>   - `rule-case-build`, `rule-plan-mode`, `rule-ratification`, `rule-ledger-write`, `rule-internal-context`
>   - `.claude/skills/hi/SKILL.md`, the Estimates of `rule-orchestration`
>   - `insight-prespec-main-agent-question-off-the-grill-me-shape`, `estimate-skill-grill-me-asks-in-rounds`
> - That Grep printed `rule-case-build.md` and `estimate-skill-grill-me-asks-in-rounds.md`. Both speak of building one Case and of the shape of a question, and both stay true.
>
> Estimates:
> - `estimate-orchestration-shows-the-built-case` stands. Each Case of a batch keeps its showing. The number of each question keeps the number of its answer, with the Case id before it, as in the pre-spec loop.
> - `estimate-orchestration-shows-the-frontier-after-a-closed-line`, `estimate-orchestration-defers-in-one-reply` and `estimate-orchestration-names-related-cases-in-the-dispatch` stand. Their Criteria speak of a line closed with no ratification, of a defer and of the dispatch, which the batch does not change.
>
> Not done:
> - `insight-prespec-after-findings-loop-unruled`, Frontier item C5, is not taken up.
> - `rule-case-rebuild-cost` is not touched.

> **problem:**
> Only the loop after the findings of `/pre-spec` lets Cases go out together for one ratification. When a new Case shows that a ratified Case must change, the changed Case is ratified again in a reply of its own, and the new Case in the next one. Nothing gathers the Cases handled side by side into one sign-off.

> **recommend:**
> - **Which Cases can be signed together outside the pre-spec loop?**
>   - Recommended: (a) one by one, with a batch only when Cases are handled side by side. Frontier items are taken one at a time, and each Case is ratified once discussed. After the findings of `/pre-spec`, and when a new Case shows that a ratified Case must change, the agent waits for the whole batch and shows all of it in one reply for one ratification.
>   - Answer: agreed with the recommendation, (a). In the first round the person had chosen (b), to hold every ratification for a batch, and the person's own answer in the second round replaced it.
> - **What the reply that shows a Case asks you**
>   - Recommended: (a) sign now or move on. The reply asks for the sign-off or lets the Case wait for the batch.
>   - Answer: in the person's own words: items of the Frontier are taken one after another and each Case is ratified after it is discussed. When several Cases are considered side by side, the agent always waits for the batch and shows all the Cases together. The cases are after the pre-spec check, or when it becomes clear that an earlier Case needs a change because of new edits. The person asked whether this holds.
> - **When the agent asks for the batch sign-off**
>   - Recommended: (a) when every open item under the Cases list is a waiting Case, and whenever the person asks; the person may name the Cases they sign.
>   - Answer: not answered; replaced by **How a batch runs in the middle of Plan Mode**.
> - **What the batch sign-off reply shows**
>   - Recommended: (a) a short list with no files and no ledger lines.
>   - Answer: not answered; replaced by **How a batch runs in the middle of Plan Mode**.
> - **How the Frontier shows a waiting Case**
>   - Recommended: (a) the line stays open as it is.
>   - Answer: not answered; replaced by **Which Cases can be signed together outside the pre-spec loop?**, under which no Case waits unsigned.
> - **How a batch runs in the middle of Plan Mode**
>   - Recommended: (a) the same steps as the pre-spec loop. The agent sends the ratified Case back to its `case-guppi`, writes one `**Waiting:**` line while an answer is out, gathers the rounds into one list numbered by Case, and shows all the Cases of the batch in one reply for one ratification.
>   - Answer: agreed with the recommendation, (a).
> - **If you sign only part of a batch**
>   - Recommended: (a) name the Cases you sign, as with sub-cases. A Case the person questions or changes goes back to its `case-guppi` and is shown again, alone or with any Case it changes in turn.
>   - Answer: agreed with the recommendation, (a).
> - **How the change is checked, and what else it changes**
>   - Recommended: (a) three sub-cases. The first changes `rule-orchestration` and creates an Estimate for the batch. The second replaces the Criterion of `estimate-orchestration-acknowledging-reply`. The third replaces the Criterion of `estimate-prespec-gathers-the-answers-after-findings` without its line on what holds outside the loop.
>   - Answer: agreed with the recommendation, (a).

### Case 598.1 — A ratified Case that must change goes out with the Case that changes it

> **given:**
> `rule-orchestration` — the rule of the main agent's work, its `Render` changed
> **＋** `vault/wiki/orchestration.md` — the render of `rule-orchestration`
> **＋** `estimate-orchestration-signs-a-batch-together` — the new promise
> **＋** `rule-prespec` and `/pre-spec` — the loop after the findings, whose steps the batch takes; unchanged
> **＋** `rule-case-check` — the `Stop` check, which lets a line under a bold label pass and asks for the file of each Case shown; unchanged
> **＋** `case-guppi` and `SendMessage` — the agent that builds each Case, and the call that sends a Case back to it
> **＋** `.claude/skills/grill-me/SKILL.md` — the shape of each question of the list
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier, whose items are taken one at a time

> **when:**
> In Plan Mode before `/pre-spec`, the person's answer to a round of a `case-guppi`, or the person's word on a shown Case, asks that a Case already ratified in the session change, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent sends the ratified Case back to its `case-guppi` by `SendMessage`, and shows neither that Case nor the Case being built alone: the two are one batch.
> **＋** A Case that a Case of the batch asks to change in the same way joins the batch.
> **＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line that opens with the bold label `**Waiting:**`, translated, and names the Cases that have answered and those still out. It writes nothing else in the chat, and `rule-case-check` refuses no such reply.
> **＋** It shows one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>`. It sends each answer to the `case-guppi` of its Case, all in one message, until every `case-guppi` of the batch has answered with its Case.
> **＋** It shows every Case of the batch in one reply, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
> **＋** The person ratifies the batch at once or names the ids. A Case the person questions or changes goes back to its `case-guppi` and is shown again, alone or in a new batch with each Case it asks to change.
> **－** Outside a batch and the loop after the findings of `/pre-spec`, the main agent does not take up the next item of `raw/<date>/<hi HHMM>/frontier.md` before the shown Case is ratified or deferred.
> **－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.

```then
create:
- slug: estimate-orchestration-signs-a-batch-together
  type: estimate
  ref: rule-orchestration
  kind: QA
  purpose: Whether, when the person's word asks that a ratified Case change while another Case is built, the main agent sends it back and shows the two Cases together for one ratification, with the rounds gathered and the waits marked as after the findings of pre-spec
  method: 'by hand at the first Plan Mode of a later session after the render in which the person''s word asks that a ratified Case change: the SendMessage calls and the replies from that word to the acknowledging reply, read in the transcript'
  tags:
  - session
  - workflow
update:
- slug: rule-orchestration
  replace:
  - old: One reply shows one Case, in the form of `case-schema.md` as `case-guppi` built it.
    new: 'One reply shows one Case, in the form of `case-schema.md` as `case-guppi` built it, except Cases handled side by side and shown together for one ratification: in the loop after the findings of `/pre-spec` and in a batch, as below (case 598.1).'
  - old: Never move to the next Case until this one is ratified or deferred — but in the loop after the findings of `/pre-spec`, where the Cases built again go out together and come back for one ratification, as `rule-prespec` sets it (case 561.2).
    new: 'Never move to the next Case until this one is ratified or deferred — but where Cases are handled side by side they go out together and come back for one ratification: in the loop after the findings of `/pre-spec`, as `rule-prespec` sets it (case 561.2), and in a batch, when the person''s word asks that a Case already ratified change while another Case is built, as `## Showing and signing a Case` sets it (case 598.1).'
  - old: a sub-case the person questions or changes is shown again alone (case 355.2).
    new: 'a sub-case the person questions or changes is shown again alone (case 355.2). When, before `/pre-spec`, the person''s answer to a round or the person''s word on a shown Case asks that a Case already ratified in the session change, the agent sends that Case back to its `case-guppi` by `SendMessage` and shows neither it nor the Case being built alone: the two are a batch, and a Case that a Case of the batch asks to change in the same way joins it. The batch takes the steps of the loop of `rule-prespec`: while an answer is out, each turn ends with one line under the bold label `**Waiting:**`, translated, naming the Cases that have answered and those still out, and nothing else; one list shows every round that came back, each question numbered `<Case id>.Q<n>`; each answer goes to the `case-guppi` of its Case, all in one message; and every Case of the batch is shown in one reply, each in the showing `## Who builds a Case` sets, for one ratification. The person ratifies the batch at once or names the ids; a Case the person questions or changes goes back to its `case-guppi` and is shown again, alone or in a new batch with each Case it asks to change (case 598.1).'
  change: 'Cases handled side by side go out together: a ratified Case that must change is shown with the Case that changes it, for one ratification (case 598.1)'
```

```tasks
- [x] update `rule-orchestration`
- [x] create `estimate-orchestration-signs-a-batch-together`
- [x] `uv run guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-orchestration-signs-a-batch-together`
```

### Case 598.2 — One reply acknowledges every Case ratified in one answer

> **given:**
> `rule-orchestration` — the sentence on sub-cases in `## Showing and signing a Case`, widened
> **＋** `vault/wiki/orchestration.md` — the render of `rule-orchestration`
> **＋** `estimate-orchestration-acknowledging-reply` — the promise of the reply, its Criterion and `method` replaced
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier the reply shows
> **＋** `rule-ledger-write` — the ledger hook, which writes the `LEDGER` block and does not append a line it already holds; unchanged
> **＋** `rule-prespec-onward` — the hook that sends the agent on when no line under `## Cases` is open; unchanged
> **＋** `raw/2026-10-02/2049/cases/case-597.md` — Case 597, which sets what that hook does after this reply

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
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written.

```then
update:
- slug: rule-orchestration
  replace:
  - old: the person ratifies them all at once or names the ids, and the acknowledging reply carries one `LEDGER` block with the lines of every sub-case ratified, one heading `## Case N — ratified` naming those ids, and one Frontier;
    new: the person ratifies them all at once or names the ids; one reply acknowledges every Case the person ratified in one answer — a Case with its sub-cases, or the Cases of a batch or of the loop after the findings of `/pre-spec` — with one `LEDGER` block holding the decision lines of each, one heading `## Case N — ratified` naming their ids, one **Changes:** paragraph and one Frontier (case 598.2);
  change: one reply acknowledges every Case ratified in one answer, under one heading that names their ids (case 598.2)
- slug: estimate-orchestration-acknowledging-reply
  set:
    status: pending
    method: one reading by hand of the first acknowledging reply of a session, and of the first reply that acknowledges Cases ratified together in one answer
  change: the Criterion replaced whole — one reply acknowledges every Case ratified in one answer (case 598.2)
```

```tasks
- [x] update `rule-orchestration`
- [x] update `estimate-orchestration-acknowledging-reply`
- [x] `uv run guppi render`: `vault/wiki/orchestration.md`
- [x] read `estimate-orchestration-acknowledging-reply`
```

### Case 598.3 — The pre-spec loop no longer owns signing together

> **given:**
> `estimate-prespec-gathers-the-answers-after-findings` — the promise of the loop after the findings, its Criterion replaced
> **＋** `rule-prespec` and `.claude/skills/pre-spec/SKILL.md` — the loop after the findings; unchanged
> **＋** `vault/wiki/orchestration.md` — sets the batch outside the loop
> **＋** `case-guppi` and `SendMessage` — the agent of each Case, and the call that sends it its findings
> **＋** `.claude/skills/grill-me/SKILL.md` — the shape of each question
> **＋** `uv run guppi casecheck` — the `Stop` check of `rule-case-check`

> **when:**
> `/pre-spec` has reported findings in Cases of the plan, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

> **then:**
> The main agent sends each finding in a Case, with each answer of the report that bears on that Case, to the `case-guppi` of that Case by `SendMessage`, one message to each `case-guppi`, as soon as the report asks the person no question or the person has answered every question of the report.
> **＋** While a question of the report is unanswered, the main agent sends nothing to any `case-guppi`.
> **＋** A question of the report that the person leaves unanswered is asked again in the shape of `.claude/skills/grill-me/SKILL.md` under its number.
> **＋** The main agent ends each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer it sent is still out, with one line that opens with a bold label ending in a colon and names the Cases that have answered and the Cases still out.
> **＋** That line holds nothing of what an answer says and no question, and the main agent writes nothing else in the chat while an answer is out and passes on no answer of one `case-guppi` alone.
> **＋** It then shows the person one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>` by the Case it belongs to, sends each answer to the `case-guppi` of its Case in one message, and repeats the wait and the list until every `case-guppi` it sent has answered with its Case.
> **＋** It then shows every Case built again in one reply, in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
> **－** When an answer brings back a round while another answer is still out, the round is not shown in that turn, and `uv run guppi casecheck` does not refuse the reply that opens with the labelled line.
> **－** Outside this loop, Cases go out together for one ratification only in a batch, as `vault/wiki/orchestration.md` sets it.
> **－** A question that no answer settles stays in the next list under its number.

```then
update:
- slug: estimate-prespec-gathers-the-answers-after-findings
  set:
    status: pending
  change: the Criterion replaced whole — outside the loop, Cases go out together only in a batch that orchestration.md sets (case 598.3)
```

```tasks
- [x] update `estimate-prespec-gathers-the-answers-after-findings`
- [x] read `estimate-prespec-gathers-the-answers-after-findings`
```

## Case 599 — The Insight on the main agent's own questions is closed by the rule that gave them the grill-me shape

> **context:**
> At `/pre-spec`, the main agent sometimes needs a decision from the person. In sessions 0248 and 1306 it asked for those decisions in a layout of its own. The questions had no numbered title line, no `**Now:**` line and no recommended answer. At that time only the rounds of `case-guppi` had to use the grill-me shape. The librarian put the two lessons together in `insight-prespec-main-agent-question-off-the-grill-me-shape`, and that Insight is still `open` in `backlog.md`.
>
> Case 561.13 closed the cause in two places. `## Who builds a Case` of `orchestration.md` gives the question shape of `.claude/skills/grill-me/SKILL.md` to each question the main agent puts to the person itself: at `/pre-spec`, at `/hi` and at a stop of Work Mode. `.claude/skills/pre-spec/SKILL.md` asks for each decision of its report in that same shape. Case 595 moved the sentence into `rule-orchestration` and did not change its meaning. The second half of the Insight's Proposal was that the first lesson must stand where the next `/pre-spec` reads it. That half is covered too: the shape is now a rule in the files that the main agent loads at `/hi` and at `/pre-spec`.
>
> No decision marked the Insight `actioned`, so it stayed in the backlog. This Case does that. Its `addressed_by` names `decision-case-561.13`, because the schema of `rule-insights-schema` sets that field to the decision that fixed the pattern. The cascade of `generate` then archives the two `clustered` lessons. The Insight stays live, so that a new lesson with the same cause reopens it.
>
> Searches of the frame:
> - A Grep of the Insight's slug over `vault/wiki/` printed these files:
>   - `backlog.md`, where the line comes from the `open` status
>   - `log.md`, not read
>   - `lesson-prespec-report-decisions-off-the-question-shape.md` and `lesson-prespec-report-questions-still-off-the-shape.md`, its children
> - A Grep of `^(root_cause|pattern):.*(shape|grill)` over `vault/wiki/` printed 5 files: the Insight, its two lessons, `insight-harness-yaml-entry-shape-assumed.md` and `lesson-hooks-posttooluse-stdout-not-in-context.md`. The last two concern other causes, so no new lesson of this cause was recorded after case 561.13.
> - A Grep of `grill-me` over `.claude/` printed `agents/case-guppi.md`, `skills/grill-me/SKILL.md`, `skills/wait-what/SKILL.md` and `skills/pre-spec/SKILL.md`. Over `vault/wiki/rules/` it printed 7 files: `rule-skill-grill-me`, `rule-prespec`, `rule-orchestration`, `rule-case-build`, `rule-case-protocol`, `rule-plan-mode` and `rule-skill-wait-what`. None of them is made false by closing the Insight, and this Case changes none of them.
>
> The Insight has no `deferred_by`, so no `{supersedes:case N}` block is needed. The Case makes no `create`, so the vault query was not run.
>
> Case 598 of this session changes `rule-orchestration` to add a batch, and each question of the batch also takes the grill-me shape. It does not touch the sentence of case 561.13. This Case changes no text of that page.
>
> `estimate-orchestration-asks-in-the-grill-me-shape` already checks the fix. Its Criterion covers each question the main agent asks itself at `/pre-spec`, at `/hi` and at a stop of Work Mode. It passed by hand at the close of session 1441. Case 595.13 moved it and set it `pending`. Its Criterion stands, because this Case changes no behaviour. `estimate-insights-schema-checked` speaks of the schema file, which is not changed.

> **problem:**
> The cause of the Insight is closed by a ratified rule, and the check of that rule passed once. The Insight still stands `open` in the backlog only because no decision marked it `actioned`. The question was whether to close it now, and which decision to name as the fix.

> **recommend:**
> - **Should the Insight be marked closed now, and which decision should it name as the fix?**
>   - Recommended: (a) close it now and name the decision that wrote the rule, `decision-case-561.13`. The cause is closed in `orchestration.md` and in the pre-spec skill, the check passed once on real questions at `/pre-spec`, and the schema says `addressed_by` names the decision that fixed the pattern.
>   - Answer: (a).

> **given:**
> `insight-prespec-main-agent-question-off-the-grill-me-shape` — the Insight, set `actioned`
> **＋** `decision-case-561.13` — the decision that gave the main agent's own questions the grill-me shape, named by `addressed_by`; unchanged
> **＋** `lesson-prespec-report-decisions-off-the-question-shape` and `lesson-prespec-report-questions-still-off-the-shape` — its `clustered` children
> **＋** `rule-insights-schema` — the shape of an Insight, `addressed_by` and the cascade; unchanged
> **＋** `guppi/generate.py` — applies the `update` and runs the cascade; unchanged
> **＋** `vault/wiki/backlog.md` — lists the `open` Insights
> **＋** `rule-orchestration` and `.claude/skills/pre-spec/SKILL.md` — give the grill-me shape to the main agent's own questions; unchanged
> **＋** `estimate-orchestration-asks-in-the-grill-me-shape` — the check of that rule; unchanged

> **when:**
> `uv run guppi generate` applies the `update` of `insight-prespec-main-agent-question-off-the-grill-me-shape`, and someone then reads `vault/wiki/backlog.md`.

> **then:**
> `insight-prespec-main-agent-question-off-the-grill-me-shape` has `status: actioned` and `addressed_by` naming `decision-case-561.13`.
> **＋** The cascade of `guppi/generate.py` archives `lesson-prespec-report-decisions-off-the-question-shape` and `lesson-prespec-report-questions-still-off-the-shape`.
> **＋** `vault/wiki/backlog.md` holds no line for the Insight.
> **－** The Insight is not archived: it stays live, and a new lesson with its cause reopens it.
> **－** `rule-orchestration`, `.claude/skills/pre-spec/SKILL.md` and `estimate-orchestration-asks-in-the-grill-me-shape` do not change.

```then
update:
- slug: insight-prespec-main-agent-question-off-the-grill-me-shape
  set:
    status: actioned
    addressed_by: '[[decision-case-561.13]]'
  change: 'actioned: orchestration.md and the pre-spec skill give the grill-me shape to each question the main agent puts to the person itself (case 561.13); no lesson of the cause since (case 599)'
```

```tasks
- [x] update `insight-prespec-main-agent-question-off-the-grill-me-shape`
```

## Case 600 — The Insight on the loop after the pre-spec findings is closed by the rules that set the loop

> **context:**
> After `/pre-spec` reports findings, the Cases they touch go back to their `case-guppi` agents. The rebuilt Cases, the rounds those agents raise and the main agent's own questions must then reach the person. In session 2042 none of this had a rule, and two failures came of it. The main agent passed on the answers of four `case-guppi` agents one at a time, and the person could not tell what to answer (`lesson-prespec-findings-relayed-piecemeal-lose-the-person`). A second run of the skill sent `ask-guppi` over the whole plan again for eight minutes, and nobody told the person first (`lesson-prespec-second-run-dispatches-ask-guppi-again`). The librarian joined the two lessons in `insight-prespec-after-findings-loop-unruled`, which is still `open` in `backlog.md`.
>
> Each part of the Insight's pattern and Proposal was checked against the rules of today:
> - How the rebuilt Cases, the rounds and the main agent's own questions reach the person. The Render of `rule-prespec`, written whole by case 561.1, sets the loop of case 561.2. Case 581.1 added the waiting line, and case 595.1 holds everything until the person answers every question of the report. The questions of the report take the grill-me shape (case 561.13). `estimate-prespec-gathers-the-answers-after-findings` passed by hand at the `/pre-spec` of session 1202, with one list numbered by Case and the four rebuilt Cases shown in one reply.
> - What a second run checks. The same Render sends `ask-guppi` at the first run of the session only. After the rebuilt Cases are ratified, the agent does not call `/pre-spec` again: it runs the script check alone, and the hook on the exit runs it too (cases 561.1, 561.3). `estimate-prespec-reconciles` passed by hand in session 1237: the check ran once more, and `ExitPlanMode` followed with no second `/pre-spec`.
> - What a run costs. The Proposal asked a second run to state its cost before it starts. No costly later run remains. Case 561 recorded that this question falls away, and the person confirmed it in this Case.
>
> Cases 580 and 581 left the Insight open because no rule covered waits on a `case-guppi` outside the loop. Case 598.1 of this session now sets those waits for a batch. This Case marks the Insight `actioned`. Its `addressed_by` names `decision-case-561.1`, the decision that wrote the loop and the first-run-only dispatch and so closed both lessons. `rule-insights-schema` sets that field to one decision, the one that fixed the pattern. Case 595.1 later changed one step of the loop and said nothing of a later run. The cascade of `generate` then archives the two `clustered` lessons. The Insight stays live, so a new lesson with the same cause reopens it. The Insight has no `deferred_by`, so no `{supersedes:case N}` block is needed. The Case makes no `create`, so the vault query was not run.
>
> Searches of the frame:
> - A Grep of `insight-prespec-after-findings-loop-unruled` over the repository, run again after the finding of `/pre-spec`, printed 21 files:
>   - under `vault/wiki/`: `backlog.md`, where the line comes from the `open` status; `log.md`, which was not read; and the two children
>   - under `vault/raw/2026-10-02/2049/`: `ledger.md`, `frontier.md`, `cases/case-598.md` and `cases/case-600.md`
>   - under `vault/raw/2026-10-02/1834/`: `spec.md`, `materialize.yaml` and `cases/case-595.md`
>   - under `vault/archive/migration/`: `2026-10-01/1441/raw/spec.md`, `materialize.yaml`, `cases/case-581.md` and `cases/case-580.md`; `2026-09-30/2356/raw/spec.md`, `materialize.yaml`, `frontier.md` and `cases/case-561.md`; `2026-10-01/1237/raw/frontier.md`; and `2026-09-30/2042/raw/materialize.yaml`
> - The Grep does not search `vault/raw/2026-10-02/event_log.md`, so that file is not among its hits.
> - A Grep of `^(root_cause|pattern):.*(pre-spec|prespec|findings|built again|rebuilt)` over `vault/wiki/` printed 13 files. Besides the Insight and its two lessons, the lessons it printed were these: `lesson-spec-write-keeps-the-body-of-a-case-that-gains-sub-cases`, `lesson-case-build-closes-a-sprint-item-without-the-sprint-page`, `lesson-prespec-judged-a-pair-by-its-anchor-alone`, `lesson-ledger-ratification-with-a-new-item-lost-its-block` and `lesson-lint-schema-body-table-one-section-per-row`. Their root causes concern other mechanisms, so no lesson of this cause was recorded after case 561. The other hits were Insights of other patterns.
>
> Case 598 of this session replaces the Criterion of `estimate-prespec-gathers-the-answers-after-findings`, and case 595.1 left it `pending`. This Case changes no text of that page or of `rule-prespec`. Case 599 actions a sibling Insight in the same way, by the same `generate` run, on another page. Case 597 does not touch this moment.
>
> Two Estimates already check the fix, `estimate-prespec-gathers-the-answers-after-findings` and `estimate-prespec-reconciles`. Their Criteria stand, because this Case changes no behaviour. `estimate-insights-schema-checked` speaks of the schema file, which this Case does not change.

> **problem:**
> The rules of `/pre-spec` now set the loop after its findings and rule out a costly second run, and the checks of both passed once. The Insight still stands `open` in the backlog only because no decision marked it `actioned`. The questions were whether every part of its cause is closed, which decision to name as the fix, and whether to close it now.

> **recommend:**
> - **Is the cost part closed by removing the costly run?**
>   - Recommended: (a) closed. No costly later run remains, since a later step is only the script check. Neither lesson concerned the first run.
>   - Answer: agreed with the recommendation, (a).
> - **Which decision should the note name as its fix?**
>   - Recommended: (a) `decision-case-561.1`, the decision that wrote the loop and the later-run rule and so closed both failures.
>   - Answer: agreed with the recommendation, (a).
> - **Close the note now, or after the loop's check passes again?**
>   - Recommended: (a) close now. The rule stands, its check passed once on real questions, and a recurrence reopens the note.
>   - Answer: agreed with the recommendation, (a).

> **given:**
> `insight-prespec-after-findings-loop-unruled` — the Insight, set `actioned`
> **＋** `decision-case-561.1` — the decision that wrote the loop after the findings and the first-run-only dispatch, named by `addressed_by`; unchanged
> **＋** `lesson-prespec-findings-relayed-piecemeal-lose-the-person` and `lesson-prespec-second-run-dispatches-ask-guppi-again` — its `clustered` children
> **＋** `rule-insights-schema` — the shape of an Insight, `addressed_by` and the cascade; unchanged
> **＋** `guppi/generate.py` — applies the `update` and runs the cascade; unchanged
> **＋** `vault/wiki/backlog.md` — lists the `open` Insights
> **＋** `rule-prespec` and `.claude/skills/pre-spec/SKILL.md` — set the loop after the findings and the later run; unchanged
> **＋** `estimate-prespec-gathers-the-answers-after-findings` and `estimate-prespec-reconciles` — the checks of that rule; unchanged

> **when:**
> `uv run guppi generate` applies the `update` of `insight-prespec-after-findings-loop-unruled`, and someone then reads `vault/wiki/backlog.md`.

> **then:**
> `insight-prespec-after-findings-loop-unruled` has `status: actioned` and `addressed_by` naming `decision-case-561.1`.
> **＋** The cascade of `guppi/generate.py` archives `lesson-prespec-findings-relayed-piecemeal-lose-the-person` and `lesson-prespec-second-run-dispatches-ask-guppi-again`.
> **＋** `vault/wiki/backlog.md` holds no line for the Insight.
> **－** The Insight is not archived: it stays live, and a new lesson with its cause reopens it.
> **－** `rule-prespec`, `.claude/skills/pre-spec/SKILL.md`, `estimate-prespec-gathers-the-answers-after-findings` and `estimate-prespec-reconciles` do not change.

```then
update:
- slug: insight-prespec-after-findings-loop-unruled
  set:
    status: actioned
    addressed_by: '[[decision-case-561.1]]'
  change: 'actioned: the pre-spec skill gathers the rounds and the rebuilt Cases after the findings into one list and one showing, and sends ask-guppi at the first run only, with no second call (cases 561.1, 561.2); the cost of a second run falls away with it; no lesson of the cause since (case 600)'
```

```tasks
- [x] update `insight-prespec-after-findings-loop-unruled`
```
