## Case 493 — Slice 3g: the Estimates of the session hooks and gates recut to `When:` and `Then:`

> **context:**
> Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. Older Estimates also open with `Given:`, a set of lines that describe the code and the cases as they stood on the day the promise was written. This group holds the Estimates of the hooks and gates of a session: the recall after a compaction, the two checkpoints of Plan Mode, the gate of `/retro` and `/handoff`, the order of the five phases, and the hook that holds Plan Mode open until `/pre-spec` has run. The group has five pages and not six, because the first round left `estimate-end-of-work-order` to the old-layout item C2. Their `Given:` holds facts from the Claude Code docs, a lesson, the case numbers of old fixes, and one line on the bounds of an edit: "The `--check` pass of `rule-prespec` does not change here". Three of the pages have no `purpose`.
> The person decided in the first round on this item. The item goes in seven Cases by area, one group per Case. History and the lines on the bounds of an edit leave the Criterion. A lost ratified text is restored, and a page with no `purpose` gets one in the same change. This group is the sixth, after cases 488 to 492. None of these pages lost its Criterion to a tool fault like case 211.3. Their History shows only Criteria that cases 40, 136.2, 169.1, 180, 213.2, 261, 265.2, 265.3, 287 and 316 wrote on purpose, so nothing is restored and no commit needs to be read. `estimate-plan-mode-verified`, `estimate-retro-commit-gates` and `estimate-prespec-hook-gates` get a `purpose` from their own Criterion. Each Criterion is replaced whole and goes back to `pending`. Its reading waits for a later session (case 428.1). The note of Slice 3g stays as it is until the last group.
> What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. Each `Given:` goes out, and a `Given:` line that states lasting behaviour moves into `When:` or `Then:`. In 493.1 the facts of the Claude Code docs, the lesson that a `SessionStart` hook cannot block and the example "the glossary by C4.1" go out as history. The line on the 10,000 characters stays: no code caps the output, but a reading can check it. In 493.2 the line on the children of `rule-plan-mode` goes out, and the vault query before a `create` without a `ref` moves into `When:`. "The plan is still written" now names the hook of `rule-spec-capture`, the writer of `spec.md` at approval. In 493.3 the line "live, the first `/handoff` from Retro on a dirty tree is refused and passes after the commit" is a way of reading, and the `method` already names the live reading. "`guppi event prompt` does not change and does not fail" goes out as a bound of an edit. The old line "without `hi` — nothing to check, exit 0" is a line the code does not honour: `guppi/gate.py` checks the tree of a `/handoff` with or without a `hi`. It is dropped, and the true part stays, that without a `hi` the checks of `/retro` do not run. The check of the Spec against the ledger still names `/retro` only, as before. The code runs it on all three commands, and this Case does not widen the promise. In 493.4 the line that a Rule MOC promises its order goes out, because that is the schema's rule and not this promise. In 493.5 the `－` line on the `--check` pass goes out as a bound of an edit, and "as before" becomes a plain statement.
> Each kept line was read against `guppi/recall.py`, `guppi/gate.py`, the hook part of `guppi/prespec.py` and the `children` of `rule-session`, and none is contradicted. Some finding lines and headers hold a `/` inside a path. They stand in plain quotation marks, as the old text had them, or name the folder in words, because a code span with a `/` reads as a path that `given` must name. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. `estimate-plan-mode-names-its-estimates` and the other Estimates of these rules speak of other steps and are not touched. The Case creates no page, so no vault query was run. Not done: the last group, the five done-conditions of the sprint, and `estimate-end-of-work-order` with item C2.

> **problem:**
> The five Estimates of the session hooks and gates still open with a `Given:` of docs, lessons and old case numbers. Three of them have no `purpose`, and one line promises a pass on a `/handoff` without a `hi` that the gate does not give. So their readings check a frame that goes stale, and one line is false.

> **recommend:**
> Replace each Criterion whole with only `When:` and `Then:`, set the three missing `purpose` fields, and drop the one line the gate does not honour, keeping its true part. Widening the check of the Spec to all three commands was rejected, because this Case recuts promises and does not add them.

### Case 493.1 — The recall after a compaction

> **given:**
> `estimate-compact-recall-reloads` — the promise, its Criterion replaced whole
> **＋** `rule-compact-recall` — the rule it promises for
> **＋** `guppi/recall.py` — the hook that prints the recall
> **＋** `guppi/ledger.py` — `session_dir` and `plan_path`, the session's folder and plan file
> **＋** `.claude/skills/hi/SKILL.md` — the skill whose `@` lines are the list of paths
> **＋** `.claude/settings.json` — the matcher `compact` on `SessionStart`
> **＋** `vault/raw/<date>/<hi HHMM>/` — the session's folder, with `frontier.md` and `spec.md`
> **＋** `tests/test_recall.py` — the tests the reading runs

> **when:**
> The client compacts the context of a session, on the person's command or on its own, and `SessionStart` fires with `source: compact` and runs `guppi/recall.py`.

> **then:**
> With a `hi` in the session's window, stdout holds a header line, "recall: the context was compacted at HH:MM:SS; the session is" followed by the session folder under the vault, such as raw/2026-09-28/2229/, and "Read before the next reply:". Then comes one path per line: the `@` files of `.claude/skills/hi/SKILL.md` in their order, the session's `frontier.md` when it exists, and the Spec when one exists. Last come the line `Frontier:` and the text of `frontier.md` as it stands.
> **＋** The Spec is the `spec.md` of the folder, or before the approval the plan file the event log names last.
> **＋** The list of paths is the `@` lines of the skill file at the moment the hook fires, with no copy in the code: a file added to those lines is in the list without a change to the hook.
> **＋** The texts of the files, the Frontier apart, are not printed, only the paths; the output stays under 10,000 characters.
> **－** Without a `hi` in the window, nothing is printed on stdout, and the exit is 0.
> **－** Another `source` gives nothing: the matcher keeps the hook from firing, and the code checks `source` itself.
> **－** Exit 0 always; an error prints nothing and blocks nothing; the hook writes no file and no event line — `session-start compact` is written by `guppi event`.

> **tasks:**
> - [ ] update `estimate-compact-recall-reloads`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given, the docs and the lesson out (case 493.1)`
> - [ ] read `estimate-compact-recall-reloads` — `pytest tests/test_recall.py`, then by hand at the first compaction of a later working session

> **ratification:**
> ```
> - decision[case 493.1][update][estimate-compact-recall-reloads]{ref:estimate-compact-recall-reloads}
> ```

### Case 493.2 — The two checkpoints of Plan Mode

> **given:**
> `estimate-plan-mode-verified` — the promise, its Criterion replaced whole
> **＋** `rule-plan-mode` — the MOC it promises for
> **＋** `rule-ask` — the vault query and its index lines
> **＋** `rule-case-build` — `case-guppi`, which runs the query and writes the `context`
> **＋** `rule-prespec-hook` — the hook on `ExitPlanMode`
> **＋** `rule-spec-capture` — the hook that writes the plan into the session's `spec.md`
> **＋** `Makefile` — the target `test-plan-mode`

> **when:**
> `case-guppi` builds a Case that proposes a `create` without a `ref` and runs the vault query first, and later the person approves the plan at `ExitPlanMode`.

> **then:**
> A `create` for a page whose `purpose` an index line already carries is named in the `context` of the Case before ratification.
> **＋** At `ExitPlanMode` the hook of `rule-prespec-hook` runs before the plan is written, and once it lets the call through, the hook of `rule-spec-capture` still writes the plan into the session's `spec.md`.

> **tasks:**
> - [ ] update `estimate-plan-mode-verified`
>   - set: `{status: pending, purpose: "Across Plan Mode a create whose purpose the vault already carries is named in the Case before ratification, and the pre-spec hook runs before the plan is written, which is still written"}`
>   - change: `the Criterion replaced whole — When and Then only, Given out, the writer of the plan named; purpose set (case 493.2)`
> - [ ] read `estimate-plan-mode-verified` — `make test-plan-mode`, then by hand at a later approval of a plan

> **ratification:**
> ```
> - decision[case 493.2][update][estimate-plan-mode-verified]{ref:estimate-plan-mode-verified}
> ```

### Case 493.3 — The gate of `/retro` and `/handoff`

> **given:**
> `estimate-retro-commit-gates` — the promise, its Criterion replaced whole
> **＋** `rule-retro-commit` — the rule it promises for
> **＋** `guppi/gate.py` — the hook `guppi gate`
> **＋** `/retro` — the skill gated on an empty session and on a Spec ahead of the ledger
> **＋** `/handoff` — the skill gated on a dirty tree
> **＋** `/hi` — the skill whose `hi` line opens the session's window, and which the gate lets pass
> **＋** `tests/test_gate.py` — the tests the reading runs

> **when:**
> `guppi gate` receives a `PreToolUse` payload of a `Skill` call, or a `UserPromptSubmit` payload whose prompt, trimmed, opens with one of the three commands the gate marks, with or without arguments.

> **then:**
> A `/handoff` on a dirty tree, where `git status --porcelain` is not empty, exits 2 with the reason "commit first" on stderr, and the client blocks the call; on a clean tree it exits 0.
> **＋** A `/retro` in a session with a `hi` but no `spec.md` in its folder, no plan file named by the event log and no `- decision[`, `- estimate[` or `- lesson[` line in its window exits 2 with "gate: /retro refused — nothing to review: no Spec and no ledger line in raw/<date>/<HHMM>/. Ratify a Case or write a reading or a lesson first, then type /retro again."; on the `Skill` path the end reads "…then call /retro in the next reply."
> **＋** Otherwise a `/retro` whose Spec holds an item with no decision line of its Case exits 2 with "gate: /retro refused — N item(s) of the Spec have no ledger line (case A). Ask the agent to end its reply with the LEDGER block, then type /retro again".
> **＋** A call it lets through, on either path, writes the same mark `prespec`, `retro` or `handoff` into the day's event log; a refusal writes no mark.
> **＋** Any other prompt or skill, `/hi` included, exits 0 with no output and no mark.
> **－** Without a `hi` in the session, the checks of `/retro` do not run.

> **tasks:**
> - [ ] update `estimate-retro-commit-gates`
>   - set: `{status: pending, purpose: "guppi gate refuses /handoff on a dirty tree and /retro with nothing to review or a Spec ahead of the ledger, and marks each call it lets through"}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the bounds line out, the pass without hi narrowed to what the gate does; purpose set (case 493.3)`
> - [ ] read `estimate-retro-commit-gates` — `pytest tests/test_gate.py`, then by hand at a later `/retro` and `/handoff`

> **ratification:**
> ```
> - decision[case 493.3][update][estimate-retro-commit-gates]{ref:estimate-retro-commit-gates}
> ```

### Case 493.4 — The five phases of a session, in order

> **given:**
> `estimate-session-phases-in-order` — the promise, its Criterion replaced whole
> **＋** `rule-session` — the MOC it promises for, its children in order
> **＋** `vault/raw/<date>/event_log.md` — the day's event log with the `hi` line
> **＋** `vault/raw/<date>/<hi HHMM>/` — the session's folder: `frontier.md`, `spec.md`, `handoff.md` or `carry.md`
> **＋** `/carry` — the skill that conserves a session after Plan Mode

> **when:**
> A session has ended, and someone reads its folder, the day's event log and `git log`.

> **then:**
> All five phases left a mark, and the marks ascend in time: the `hi` line of the day's event log → `frontier.md` → `spec.md` with its approved stamp → the Retro commit → `handoff.md` → the librarian's commit.
> **＋** `rule-session` is the parent of the five phases, its children in that order.
> **－** A session conserved by `/carry` ends at `carry.md`: the marks of Work Mode, End of Work and Documentation are absent, and that is not a failure.

> **tasks:**
> - [ ] update `estimate-session-phases-in-order`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given out (case 493.4)`
> - [ ] read `estimate-session-phases-in-order` — by hand at the close of a later session

> **ratification:**
> ```
> - decision[case 493.4][update][estimate-session-phases-in-order]{ref:estimate-session-phases-in-order}
> ```

### Case 493.5 — Plan Mode stays open until `/pre-spec` has run

> **given:**
> `estimate-prespec-hook-gates` — the promise, its Criterion replaced whole
> **＋** `rule-prespec-hook` — the rule it promises for
> **＋** `guppi/prespec.py` — the hook part, `run` without arguments
> **＋** `guppi/ledger.py` — `session_event_logs`, the logs the ledger hook reads
> **＋** `vault/raw/<date>/event_log.md` — the event logs with the `hi` and `prespec` lines
> **＋** `/pre-spec` — the skill whose call writes the `prespec` line
> **＋** `tests/test_prespec.py` — the tests the reading runs

> **when:**
> The hook `guppi prespec` receives a `PreToolUse` payload naming `ExitPlanMode` with the session's stamp, and asks whether `/pre-spec` ran in this session.

> **then:**
> With no `prespec` line of this session's stamp after its `hi`, the hook exits 2 with a reason that names `/pre-spec` and the session; with the line, it exits 0; any other tool exits 0.
> **＋** The window is open when the logs hold a `hi` of the session's stamp and a `prespec` of the same stamp after it; a mark of another stamp or `--------` does not count; a foreign `session-start` resets nothing.
> **＋** The logs it reads are the ledger hook's, from today back to the date of this session's `session-start`, so the `hi` and the `prespec` of yesterday's session are found after midnight.
> **－** Without a `hi` of this session the call passes.

> **tasks:**
> - [ ] update `estimate-prespec-hook-gates`
>   - set: `{status: pending, purpose: "The ExitPlanMode hook holds a working session in Plan Mode until /pre-spec has run in it, across midnight too"}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the bounds line out; purpose set (case 493.5)`
> - [ ] read `estimate-prespec-hook-gates` — `pytest tests/test_prespec.py`, then by hand at a later approval of a plan

> **ratification:**
> ```
> - decision[case 493.5][update][estimate-prespec-hook-gates]{ref:estimate-prespec-hook-gates}
> ```

### Case 493.6 — The sprint page records the group of the session hooks and gates

> **given:**
> `entity-sprint-migration` — the sprint page; its Slice 3g holds the note on every other Estimate
> **＋** `vault/wiki/sprint.md` — the render of the sprint page
> **＋** `/hi` — builds the Frontier from `vault/wiki/sprint.md`
> **＋** `rule-compact-recall` — a rule whose Estimate this Case recuts
> **＋** `rule-plan-mode` — a rule whose Estimate this Case recuts
> **＋** `rule-retro-commit` — a rule whose Estimate this Case recuts
> **＋** `rule-session` — a rule whose Estimate this Case recuts
> **＋** `rule-prespec-hook` — a rule whose Estimate this Case recuts

> **when:**
> The librarian's run applies the `update` of `entity-sprint-migration`.

> **then:**
> The History of `entity-sprint-migration` says that the Estimates of the session hooks and gates are recut.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - change: `Slice 3g: the Estimates of rule-compact-recall, rule-plan-mode, rule-retro-commit, rule-session and rule-prespec-hook recut to When and Then; the note on every other Estimate stands (case 493)`

> **ratification:**
> ```
> - decision[case 493.6][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
