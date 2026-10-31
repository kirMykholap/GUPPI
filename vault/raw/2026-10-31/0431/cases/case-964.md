## Case 964 — The Case ratified in Work Mode names itself in the method

> **context:**
> This Case replaces Case 961.6 whole, in the Work Mode of this session (`vault/raw/2026-10-31/0431/cases/case-961.md`, read whole). Case 961.6 stages on purpose the event that `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` waits for: a Case ratified in Work Mode that replaces a sub-case of a ratified Case. Its `stop:` task asks for this Case under the id that `uv run --project .guppi guppi caseid --next --session <stamp>` prints, with one change. The bracket at the end of the `method` named the Case only as the Case that replaces Case 961.6. Here it names Case 964 by its id. Everything else of Case 961.6 stands word for word: its `given`, `when` and `then`, the `then` block but for that bracket, and its tasks. The `when` and `then` are the Criterion of the page, written back unchanged. The `method` keeps the form that Case 960 of this session sets: it names the place of the evidence and the event by its kind, and the pointer stands in a bracket of its own at its end, as `rule-clean-branch` sets for the text of an Estimate. The `stop:` task stays in the Case, since this Case holds Case 961.6 whole. Its work stands once the person ratifies this Case, so the main agent ticks it and does not run it again, as `.claude/skills/work/SKILL.md` sets it for a task done under the sub-case a Case replaces (read whole). The `update` and `read` lines stay open. The `update` of the page lands at the librarian's run, and the page still holds its old `method` (`vault/wiki/estimates/estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline.md`, read whole). A Grep of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` over `.guppi/` printed no file, so no test reads the page. The session's ledger holds no `error` lesson, so no line carries `{addresses:...}`. Case 965 is built at the same time and replaces Case 956.1 for another defect; this Case changes no page it changes and rests on nothing of it, and its file was not read.

> **problem:**
> The staged trial of Case 961 needs its Case ratified in Work Mode, and the `method` must name that Case by its id so that Retro reads the right run.

> **recommend:**
> - Recommended: replace Case 961.6 whole, with Case 964 named in the bracket at the end of the `method`.
> - Answer: ratified as built

> **given:**
> `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-work-mode`: the rule it checks, rendered into `.claude/skills/work/SKILL.md`, with `/work` and `/box`, and `vault/raw/<date>/<HHMM>/`, the folder of a conserved Spec.
> **＋** `raw/<date>/<hi HHMM>/work.md`, `raw/<date>/<hi HHMM>/spec.md` and `raw/<date>/<hi HHMM>/handoff.md`: the files of the run.
> **＋** `vault/wiki/where-to-stop.md`, `rule-prespec-onward`, `rule-spec-box` and `/retro`: the stops and the steps around the run.
> **＋** `uv run --project .guppi guppi render`, `uv run --project .guppi guppi test`, `uv run --project .guppi guppi check`, `uv run --project .guppi guppi prespec --check` and `git branch --show-current`: the commands of the run.
> **＋** `case-guppi`: the agent that builds the Case ratified in Work Mode.
> **＋** `~/.claude/projects/`: the folder of the transcript of the session.

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run --project .guppi guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.
> **＋** Or `/box` calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.
> **＋** Or, while the run of `/work` goes on, the person ratifies a Case built in Work Mode.

> **then:**
> `uv run --project .guppi guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
> **＋** When a `!` substitution of `.claude/skills/work/SKILL.md` comes back empty, the agent runs its command itself — `git branch --show-current` before the check of the branch, `uv run --project .guppi guppi test` and `uv run --project .guppi guppi check` before the first change — and uses that result.
> **＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
> **＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `uv run --project .guppi guppi test` and of `uv run --project .guppi guppi check` with each failing test and each lint finding line as printed, and an empty `## Expected red`.
> **＋** When `work.md` already stands, its `## Baseline` stays as it is.
> **＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task; a task line that opens with a code span holding `guppi sprint-close` it neither runs nor ticks, since the librarian runs it.
> **＋** The reply that acknowledges a Case ratified in Work Mode ends the turn, since the hook of `rule-prespec-onward` sends nothing on once `raw/<date>/<hi HHMM>/spec.md` stands; at the person's next message the run goes on from where it stopped.
> **＋** After the reply that acknowledges a Case ratified in Work Mode, and before the first task of that Case, the agent runs `uv run --project .guppi guppi prespec --check` on the plan file of the session, with the session id of its `hi:` line.
> **＋** When that check prints a line that does not open with `note:`, the agent stops as the first condition of `vault/wiki/where-to-stop.md` sets it and sends the finding to the `case-guppi` of that Case; the run goes on after the person ratifies the fixed Case and the check prints no such line.
> **＋** A task of that Case whose work already stands, done under the sub-case the Case replaces, is ticked in `raw/<date>/<hi HHMM>/spec.md` and not run again.
> **＋** A task that changes `uv run --project .guppi guppi check`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
> **＋** When the last task of `raw/<date>/<hi HHMM>/spec.md` is done, before the Work readings, the agent runs `uv run --project .guppi guppi test` in full and holds each failing test against `## Baseline` of `raw/<date>/<hi HHMM>/work.md`.
> **＋** A failing test that `## Baseline` holds goes on, and a new one whose fix finishes ratified work is fixed.
> **＋** With a folder from `/box`, `work.md` holds a third section, `## Conserved Spec`, naming the folder; the tasks run and ticked are those of that folder's `spec.md`; and the agent deletes that folder's `carry.md` when the last task is done, before the Work readings.
> **－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.
> **－** A new failing test whose fix needs a choice that no ratified Case makes is not fixed in that step: it is a stop of `vault/wiki/where-to-stop.md`.
> **－** Any other new failing test goes on to `/retro`, which fixes it or reverts it into a patch.
> **－** In a `/work` that `/box` calls no Case is ratified, so the check of the plan does not run there: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.

> **tasks:**
> - [ ] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
>   - set:
>     ```
>     status: pending
>     method: "by hand, at Retro: uv run --project .guppi guppi render --check; .claude/skills/work/SKILL.md read against each line of the Criterion; a Case ratified in the Work Mode of the session that replaces a sub-case of a ratified Case, the end of the turn after its acknowledging reply, the check of the plan before its first task, what followed a finding and the ticks of its tasks read in the transcript of the session under ~/.claude/projects/ and in its spec.md and work.md against the Criterion, recorded in the estimate line with the transcript named (Case 964, ratified in Work Mode, which replaces Case 961.6, staged in session 2026-10-31/0431)"
>     ```
>   - change: `the method reads Case 964, ratified in the Work Mode of session 0431 and staged on purpose, the Criterion written back unchanged`
> - [ ] stop: in Work Mode, the main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run --project .guppi guppi caseid --next --session <stamp>` prints, which replaces Case 961.6 whole with one change: the bracket at the end of the `method` names the id of that new Case as the Case ratified in Work Mode; the person ratifies it, and the run goes on as `.claude/skills/work/SKILL.md` sets it.
> - [ ] read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`

> **ratification:**
> ```
> - decision[case 964][update][estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline]{ref:rule-work-mode}{supersedes:case 961.6}
> ```
