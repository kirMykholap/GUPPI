## Case 670 — An Estimate is read in the session that changes it

> **context:**
> When a Case creates an Estimate or replaces its Criterion, the scripts set the page `pending`. The ledger hook of `guppi/ledger.py` then refuses a reading of that slug for the whole session (case 428.1). Retro leaves the reading to a later session, and most methods name a live moment there, "by hand in a later session". Each `/hi` takes these readings again as Work lines and reads old transcripts to judge them. Session 1616 left 13 Estimates pending, and the `/hi` of this session spent one agent of about 112k tokens on transcripts. The loop never closes, because every change makes a new pending Estimate.
> The person chose to break it. Retro reads each Estimate the session creates or updates, in the same session, on the Criterion of the Spec, and the hook lets that reading through once Retro has opened (670.1). A rule whose Render changes is read on the new text of the Spec, since its harness file follows only at the librarian's render. A reading that needs the person's word stays the one exception and is asked at the next `/hi`. Retro sets any other Estimate it cannot read `failed`, with the reason, so the next `/hi` shows it once as a Case (670.2). The handoff no longer lists these Estimates as readings that wait (670.3). A method holds only what runs in its own session, and pre-spec reports a new method that waits for another session; the check is a predicate in `guppi/lint.py` that `guppi/prespec.py` imports, and lint does not run it over the live pages, so old methods give no new finding (670.4). `/hi` reads no transcript: it takes only the readings it can run now, and turns each other open Work line into a Cases line. The 11 Estimates of the close of the sprint migration are left as they are (670.5). The list of the sources of a Cases line names that new kind (670.6). The Work readings of `/work` still leave an Estimate the session changes, and its Work line now closes at Retro (670.7). No hook checks that Retro read each Estimate. A forgotten one stays `pending`, and the next `/hi` takes it, or turns it into a Cases line.
> The librarian applies a reading of the same session in the right order. `materialize` keeps the order of the ledger. A reading folds into the `create` of its page (`fold_estimate`). An `update` that replaces a Criterion sets `pending` (`lift_criterion`), and a reading line later in the ledger becomes its own entry after it. `generate` applies the entries in order, so the reading of Retro sets the final status.
> Case 669 of this session sets fifteen Estimates `passed` by the person's decision. Each of its `update` items sets `passed` and writes the Criterion back unchanged under `sections.Criterion`. The person answered that this Case leaves such an Estimate alone, so Retro neither reads it nor sets it `failed`. The exception holds only for an `update` that sets `passed` or `failed` by the person's decision and writes its Criterion back unchanged. An ordinary replacement of a Criterion also carries a status, `set: {status: pending}`, and writes no `sections.Criterion` (`lift_criterion`), so Retro reads it. The same exception covers an `update` that names one part of the page alone, such as a `method`. That update writes no new Criterion and sets no status, so the Spec holds no new promise to read. Case 669 changes no page this Case changes. Its update of `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case` keeps a Criterion about superseded Cases, which this Case does not touch.
> In this session, the code of 670.1 and 670.4 is live once Work Mode writes it. Retro and `/hi` still follow their old rendered text until the librarian renders it. The Render of `rule-retro` says that an Estimate this session creates or updates gets no reading in this session. So the ledger hook would let a reading through at this session's Retro, after the mark `retro`, but the old Retro text takes none. This session's Retro takes no reading of this Case's Estimates, of the Estimate of Case 671.1 or of the fifteen of Case 669. The next `/hi` takes each Estimate of this Case and of Case 671.1 as a Work line it can run now: the code Estimates by pytest, and the render Estimates from the rendered file their methods name. `estimate-work-mode-takes-the-work-readings` of 670.7 gets a method of the same form as the render Estimates. `estimate-hi-writes-frontier` of 670.6 keeps its method, which waits for the close of the sprint, as 670.5 allows. The ledger hook only refuses less than before, so no line is lost between the code and the render.
> The frame. A Grep `later session` over `{.claude/**,guppi/**,vault/wiki/rules/**,vault/wiki/*.md}` printed 21 files: `vault/wiki/brief.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/retro/SKILL.md`, `vault/wiki/orchestration.md`, `.claude/agents/case-guppi.md`, `vault/wiki/case-schema.md`, `.claude/skills/carry/SKILL.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-retro.md`, `vault/wiki/rules/rule-materialize.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/rules/rule-case-build.md`, `guppi/casecheck.py`, `guppi/prespec.py`, `vault/wiki/rules/rule-case-protocol.md`, `guppi/ledger.py`, `vault/wiki/rules/rule-skill-hi.md`, `vault/wiki/rules/rule-spec-box.md`, `vault/wiki/rules/rule-carry-over.md`, `guppi/box.py` and `guppi/spec.py`. The hits in `rule-retro`, `rule-orchestration`, `rule-case-protocol` and `guppi/ledger.py` enter this Case, and their rendered files follow them. The hit in `rule-skill-hi` and its skill file says that a line of the sprint page left for a later session closes `· sprint · defer`; 670.5 does not change that, so it stands. The passages 670.5 replaces speak of an earlier session. The hits in `rule-carry-over`, `rule-spec-box`, `.claude/skills/carry/SKILL.md`, `guppi/box.py`, `guppi/spec.py` and `guppi/prespec.py` speak of a conserved Spec or a sprint item that a later session takes, so they stand. The hit in `rule-case-build`, `.claude/agents/case-guppi.md` and `guppi/casecheck.py` says that a Case of a later session removes an old form of code, so it stands. The hit in `rule-materialize` is a History line, and `brief.md` and `log.md` were not read. A Grep `creates or updates` over the same paths printed 16 files: `.claude/skills/work/SKILL.md`, `.claude/skills/retro/SKILL.md`, `vault/wiki/orchestration.md`, `.claude/skills/handoff/SKILL.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-retro.md`, `vault/wiki/rules/rule-materialize.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/rules/rule-handoff.md`, `guppi/ratified.py`, `guppi/materialize.py`, `vault/wiki/rules/rule-case-protocol.md`, `vault/wiki/rules/rule-spec-write.md`, `guppi/ledger.py`, `vault/wiki/rules/rule-work-mode.md` and `vault/wiki/rules/rule-ledger-write.md`. The hit in `rule-handoff` enters 670.3. The hit in `rule-work-mode` and its skill enters 670.7: the Work readings still leave an Estimate the session changes, and Retro now reads it and closes its line. The hits in `rule-spec-write`, `rule-materialize`, `guppi/materialize.py` and `guppi/ratified.py` speak of a schema rule that the session changes, and the hits in `rule-ledger-write` and `rule-case-protocol` are History lines; all of these stand. A Grep `^method:.*(closes (a|the) sprint|close of a sprint|closes it)` over the 11 Estimate pages of the close of the sprint migration under `vault/wiki/estimates/` printed 11 occurrences in 11 files, so the exception of 670.5 covers each of them by the words of its method.
> The Estimates. `estimate-retro-runs-on-to-the-handoff` stands. It promises that Retro takes the readings whose moment has come and leaves the person's readings to `## Ask the person`, and both stay true. `estimate-case-protocol-case-form` stands, and Case 669 writes its Criterion back. Its line says that a check after Work Mode is the reading of an Estimate or is left to `make lint`. 670.4 keeps that sentence of `case-schema.md` and only adds that Retro takes the reading. `estimate-hi-writes-frontier` stands. It says that a Work line which needs a decision closes `· case N`, and 670.5 uses that close. `estimate-lint-reports-a-method-tied-to-a-one-off-moment` stands, since its finding is not replaced. `estimate-prespec-catches-a-method-without-a-form` stands. It promises the pre-spec finding on the `method` of a `create`, or of an `update` with `set: {method: …}`, that names no form, by a predicate lifted out of `guppi/lint.py`. 670.4 reads the same input and adds a finding beside it in the same way, and its last line keeps the finding of no form. The other Stop hooks in `.claude/settings.json` (`guppi ratified`, `guppi casecheck`, `guppi context`, `guppi onward` and `guppi onward --plan`) judge no reading line. `guppi onward` reads the refusals of the ledger hook. At Retro the hook still refuses a lesson without its prefix and a line it cannot read, and `rule-retro` (case 596) and `guppi/onward.py` answer such a refusal as before. Only the refusal of a reading of a changed Estimate stops at the mark.

> **problem:**
> Every change of an Estimate leaves it `pending`. Its reading is barred in the session that made the change and waits for a live moment in another session, so each `/hi` pays to read the same Estimates again, and the list never empties.

> **recommend:**
> - **When does the ledger hook let a reading of a changed Estimate through?**
>   - Recommended: (a) from the opening of Retro, by the existing `retro` mark; before it the hook still refuses.
>   - Answer: agreed, (a).
> - **How does Retro read an Estimate of a rule whose text is rendered into a harness file?**
>   - Recommended: (a) Retro reads the new text in the Spec against the Criterion; the render and `make lint` check the file, and a problem seen later is a lesson.
>   - Answer: agreed, (a).
> - **What happens to an Estimate whose method needs your word?**
>   - Recommended: (a) the one exception: Retro leaves it under `## Ask the person`, and the next `/hi` asks it once, with no transcript.
>   - Answer: agreed, (a).
> - **What does `/hi` do with an old open reading whose method waits for a moment in another session?**
>   - Recommended: (a) remove the transcript step: `/hi` takes only the readings it can run now, and any other open Estimate becomes one Cases line; the readings of the sprint migration's close stay as they are.
>   - Answer: agreed, (a).
> - **What makes sure Retro reads, or sets `failed`, each Estimate the session changed?**
>   - Recommended: (b) Retro's text alone, with `/hi` as the net for a forgotten reading.
>   - Answer: agreed, (b).
> - **Does a check report a new method that waits for another session?**
>   - Recommended: (a) pre-spec reports it in the Spec, by a predicate in `guppi/lint.py` that `guppi/prespec.py` imports; a method whose reading is the person's answer is the exception, and lint over the live pages stays as it is.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: from the summary of Case 669, the main agent asked whether this Case should leave alone an Estimate whose `update` in this session sets its status itself and does not change its Criterion, so the fifteen of Case 669 stay `passed`; the person agreed, (a).
>   - Taken: 670.2 neither reads nor sets `failed` an Estimate whose `update` sets `passed` or `failed` by the person's decision and writes its Criterion back unchanged, nor one whose `update` names one part of the page alone.

### Case 670.1 — The ledger hook writes a reading of a changed Estimate once Retro has opened

> **given:**
> `guppi/ledger.py`: the `Stop` hook that writes the ledger lines.
> **＋** `guppi/onward.py`: holds `retro_marked`, the judgment of the mark `retro`.
> **＋** `tests/test_ledger.py`: the tests of the hook.
> **＋** `rule-ledger-write`: the rule of the hook.
> **＋** `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`: its Criterion is replaced whole.
> **＋** `estimate-ledger-write-lifts`: sets how a stderr line is told once a stretch.
> **＋** `rule-orchestration`: its Render tells the main agent when a reading line is written.
> **＋** `vault/wiki/orchestration.md`: the file rendered from it.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` finds a fresh `estimate[<slug>]` line in a `LEDGER` block of the session, and a decision line `create` or `update` of `<slug>` stands in the session's ledger or among the lines the hook writes on the same `Stop`.

> **then:**
> While the event log of the session's window holds no mark `retro` of this session after its `hi`, the line is not written: the reading waits for Retro.
> **＋** Once that mark stands, the line is written as any other reading of the `Stop`.
> **＋** The mark is judged by `retro_marked` of `guppi/onward.py`, imported, the one judgment of the mark.
> **＋** A line of a reply written before the mark stays refused, and the hook skips it at every later `Stop` without a word.
> **＋** A reading of the old slug of a page that an `update` of this session renames falls under the same rule: the decision line names the old slug.
> **＋** When a refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line, which names the Case and says that the reading is taken at the Retro of this session.
> **＋** The other lines of the `Stop` are written as before.
> **－** A reading of a slug that no decision line `create` or `update` of this session names is written as before; a `defer` line of the slug does not refuse it.
> **－** Without a `hi` the hook judges no line. With `stop_hook_active` set it judges the line the same, and its stderr line is told once a stretch, as `estimate-ledger-write-lifts` sets it.

> **tasks:**
> - [ ] `guppi/ledger.py`: `refused_readings` refuses a reading of a slug the session changes only before the mark `retro` of the session, judged by `retro_marked` of `guppi/onward.py`, imported inside the function; a line of a reply written before the mark stays refused; the stderr line and the docstring say that the reading is taken at the Retro of this session.
> - [ ] `tests/test_ledger.py`: a reading of a changed slug is refused before the mark and written after it; a line of a reply before the mark stays refused after it; the stderr line names Retro.
> - [ ] update `rule-ledger-write`
>   - change: `the hook refuses a reading of an Estimate that a decision line of the session creates or updates only before the mark retro of the session (case 670.1)`
> - [ ] update `rule-orchestration`
>   - old: `— a reading of an Estimate that a decision line of this session creates or updates waits for a later session, and the ledger hook refuses it (case 428.1) —`
>   - new: `— a reading of an Estimate that a decision line of this session creates or updates stands in that reply too, and the ledger hook refuses it before Retro opens (case 670.1) —`
>   - change: `a reading of an Estimate the session changes is written in the reply that ends Retro; the ledger hook refuses it only before Retro opens (case 670.1)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] update `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether the ledger hook refuses a reading of an Estimate that a decision line of the same session creates or updates until the Retro of that session opens, writes it after, and says why only for the reply just finished"
>     ```
>   - change: `the Criterion replaced whole — the reading is refused only before the mark retro of the session (case 670.1)`
> - [ ] read `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`

> **ratification:**
> ```
> - decision[case 670.1][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 670.1][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 670.1][update][estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session]{ref:rule-ledger-write}
> ```

### Case 670.2 — Retro reads each Estimate the session changes, or sets it failed

> **given:**
> `rule-retro`: the Render of the Retro skill, whose paragraph on readings changes.
> **＋** `.claude/skills/retro/SKILL.md`: the skill file rendered from it.
> **＋** `estimate-retro-loads`: its Criterion is replaced whole.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec whose Criteria Retro reads.
> **＋** `raw/<date>/<hi HHMM>/work.md`: names a conserved Spec that `/box` runs.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: names a reading that needs the person.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: holds the `W` line of an Estimate Retro reads.

> **when:**
> The agent calls `/retro` of `.claude/skills/retro/SKILL.md` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, and the agent takes the readings of the session's Estimates.

> **then:**
> A reading measures the Criterion the page carries at the moment of the reading — the one ratified last; its line is written only when the work that Criterion names is built.
> **＋** Each Estimate this session creates or updates — by a decision line of its slug, or by an `update` that renames a page to it — is read in the reply that ends Retro, on the Criterion of `raw/<date>/<hi HHMM>/spec.md`: the `when` and `then` of its Case, or the Criterion its item writes.
> **＋** For an Estimate of a rule whose Render a Case of the Spec changes, the reading reads the new text of the Render in `raw/<date>/<hi HHMM>/spec.md` against that Criterion.
> **＋** Each such Estimate that Retro cannot read gets a `failed` line in the same `LEDGER` block, whose result opens with the date and says that Retro did not read it and why.
> **＋** When `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec`, the Spec is the `spec.md` of the folder that section names, and the decision lines of that folder's `ledger.md` count as this session's for its boxes, for the scope of an edit and for the readings above.
> **＋** Retro closes the open `W` line of each Estimate it reads or sets `failed` `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`.
> **－** An Estimate whose `update` sets `passed` or `failed` by the person's decision and writes its Criterion back unchanged, and one whose `update` names one part of the page alone, is neither read nor set `failed`.
> **－** A reading whose `method` names the person's word is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question, and its `read` line is neither debt nor the librarian's.
> **－** A reading of an Estimate this session neither creates nor updates is taken as before, once its work is built.

> **tasks:**
> - [ ] update `rule-retro`
>   - old: `and for the readings this session does not take; the ledger hook sees only this session's own lines, so this text is the guard (case 591)`
>   - new: `and for the readings of the Estimates this session creates or updates; the ledger hook sees only this session's own lines (cases 591, 670.2)`
>   - old: `` A `read` line whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it, waits for a later session; it is neither debt nor the librarian's (case 428.4). ``
>   - new: `` A `read` line whose `failed` line you write in this turn waits for the librarian as a reading does. A `read` line of an Estimate whose reading only the person can take, named under `## Ask the person` of `handoff.md`, waits for the person; it is neither debt nor the librarian's (case 670.2). ``
>   - old:
>     ```
>     What a session changes, it does not measure: an Estimate this session creates or updates has no reading in this session, built or not, and the ledger hook refuses one (case 428.1); the `read` line of its old Criterion in an earlier Spec is not debt and is not read, and the reading of the new Criterion closes it in a later session, at the moment its `method` names (cases 283, 428.3). A reading whose `method` names the person's word is not yours to take: it is a line of `## Ask the person` of `handoff.md`, with the question the person answers (case 531.1). `handoff.md` names every Estimate whose reading cannot be taken yet, and every Estimate this session creates or updates.
>     ```
>   - new:
>     ```
>     Read each Estimate this session creates or updates — by a decision line of its slug, or by an `update` that renames a page to it — in this turn, on the Criterion of the Spec: the `when` and `then` of its Case, or the Criterion its item writes; the ledger hook writes such a reading only after Retro opens (cases 670.1, 670.2). For an Estimate of a rule whose Render a Case of the Spec changes, read the new text of the Render in the Spec against that Criterion: the harness file follows at the librarian's render, and its `make lint` checks the file. An Estimate whose `update` sets `passed` or `failed` by the person's decision and writes its Criterion back unchanged, and one whose `update` names one part of the page alone, is neither read nor set `failed`. The `read` line of an old Criterion in an earlier Spec is not debt and is not read (case 283). A reading whose `method` names the person's word is not yours to take: it is a line of `## Ask the person` of `handoff.md`, with the question the person answers (case 531.1). Each other Estimate this session creates or updates that you cannot read gets a `failed` line in the same `LEDGER` block, its result opening with the date, the words `Retro, not read` and the reason; the next session shows it as a Case. Close the open `W` line of each Estimate you read or set `failed` `[x] … · work` in `frontier.md` (case 670.7). A problem seen live in a later session is a lesson of that session, not a reading. `handoff.md` names every Estimate whose reading cannot be taken yet.
>     ```
>   - change: `Retro reads each Estimate the session creates or updates on the Criterion of the Spec, or sets it failed; a reading that needs the person waits for the person (case 670.2)`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] update `estimate-retro-loads`
>   - set:
>     ```
>     status: pending
>     method: "by hand, the text of .claude/skills/retro/SKILL.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-retro in the Spec, read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — Retro reads each Estimate the session creates or updates on the Criterion of the Spec, or sets it failed (case 670.2)`
> - [ ] read `estimate-retro-loads`

> **ratification:**
> ```
> - decision[case 670.2][update][rule-retro]{ref:rule-retro}
> - decision[case 670.2][update][estimate-retro-loads]{ref:rule-retro}
> ```

### Case 670.3 — The handoff lists no Estimate the session changed as a reading that waits

> **given:**
> `rule-handoff`: the Render of the handoff skill, whose line on `## Debt` changes.
> **＋** `.claude/skills/handoff/SKILL.md`: the skill file rendered from it.
> **＋** `estimate-handoff-holds-each-fact-once`: its Criterion is replaced whole.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the report of Retro the skill writes.
> **＋** `rule-retro`: reads or sets `failed` each Estimate the session changes.
> **＋** `rule-brief`: reads `## What actually got done`.

> **when:**
> The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, on a clean tree, and the agent runs `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff` and writes `raw/<date>/<hi HHMM>/handoff.md`.

> **then:**
> `raw/<date>/<hi HHMM>/handoff.md` is the report of Retro: under `# Handoff — <date>, <slice or topic>` it holds, in order, `## Notes from memory`, `## Direct instructions to the librarian`, `## What actually got done`, `## Debt`, `## Observations`, `## For the next session` and `## Ask the person`.
> **＋** `## Notes from memory` holds only where the person hesitated, what stayed unclear and which decisions carried caveats. `## Direct instructions to the librarian` holds only what to check first and what may duplicate what, and lists no reading that waits.
> **＋** `## What actually got done` holds the ids of the Cases ratified, the code files and tests changed, the result of `make test` and `make style`, and the readings and lessons written, by their ledger line numbers.
> **＋** `## Debt` holds each box of the Spec that is debt and each red test reverted into a patch, with the path of the patch. Under them stands a line with the count of the boxes that wait for the librarian. Then comes one line per Estimate whose reading cannot be taken yet, except one that `## Ask the person` holds: its slug and the moment its reading waits for. These lines stand in the section and are not debt.
> **＋** An Estimate this session creates or updates has no such line in `## Debt`: the Retro of `rule-retro` read it or set it `failed`, unless the person's answer is its reading.
> **＋** `## Observations` holds what was noticed in Work Mode and Retro, a red before the work and an expected red among them; `## For the next session` holds what needs a decision.
> **＋** `## Ask the person` holds one line per reading that only the person can take: the Estimate by slug, the mark `needs the person` and the question the person answers.
> **－** No statement stands twice: a Case, box, reading, lesson or observation that one section names stands in another section only with what that section's kind adds about it, such as a caveat or what to check first, and no section says again what another section says of it. The file holds no commit, no number of an item and no end of an item.
> **－** The section names `## Notes from memory`, `## Direct instructions to the librarian` and `## What actually got done` stay, so `rule-brief` reads `## What actually got done` as before.

> **tasks:**
> - [ ] update `rule-handoff`
>   - old: `` then one line per Estimate whose reading cannot be taken yet, each one this session creates or updates among them, except one that `## Ask the person` holds: its slug and the moment its reading waits for; these lines stand in the section and are not debt (case 624). ``
>   - new: `` then one line per Estimate whose reading cannot be taken yet, except one that `## Ask the person` holds: its slug and the moment its reading waits for; an Estimate this session creates or updates has no such line, since Retro read it or set it `failed`; these lines stand in the section and are not debt (cases 624, 670.3). ``
>   - change: `the Debt section lists no Estimate the session creates or updates as a reading that waits: Retro reads it or sets it failed (case 670.3)`
> - [ ] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
> - [ ] update `estimate-handoff-holds-each-fact-once`
>   - set:
>     ```
>     status: pending
>     method: "one reading by hand of .claude/skills/handoff/SKILL.md as rendered, or, at the Retro of the session that changes it, of the new Render of rule-handoff in the Spec, against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — Debt lists no Estimate the session creates or updates as a reading that waits (case 670.3)`
> - [ ] read `estimate-handoff-holds-each-fact-once`

> **ratification:**
> ```
> - decision[case 670.3][update][rule-handoff]{ref:rule-handoff}
> - decision[case 670.3][update][estimate-handoff-holds-each-fact-once]{ref:rule-handoff}
> ```

### Case 670.4 — Pre-spec reports a method that waits for another session

> **given:**
> `rule-case-protocol`: the Render of the Case form, which sets what a `method` holds.
> **＋** `vault/wiki/case-schema.md`: the file rendered from it.
> **＋** `rule-prespec-hook`: the rule of the pre-spec check.
> **＋** `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`: the new check of this promise.
> **＋** `guppi/lint.py`: holds the predicate.
> **＋** `guppi/prespec.py`: the pre-spec check that calls it.
> **＋** `tests/test_prespec.py`: the tests of the finding.
> **＋** `tests/test_lint.py`: the tests of the predicate.
> **＋** `/hi`: the command that opens a session, which a method may name.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` of `guppi/prespec.py` reads the `method` of a `create` of an Estimate, or of an `update` that carries `set: {method: …}`, in the `then` blocks of the plan file.

> **then:**
> A `method` with a part between two `;` that names a later session, the next session, a session after another, the librarian or `/hi` gives one line `case N: <create|update> <slug>: method waits for another session — a method holds only what runs in its own session`.
> **＋** The judgment is one predicate in `guppi/lint.py`, which `guppi/prespec.py` imports.
> **－** A part that names the person, such as the person's answer at `/hi`, gives no such line.
> **－** `uv run guppi lint` of `guppi/lint.py` over the live Estimate pages gives no finding by this predicate.
> **－** The line does not replace the finding of a `method` that names no form or that ties its reading to a one-off moment.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `` or the text the item writes under `sections: Criterion` (cases 188, 194.1). A rule with several promises ``
>   - new: `` or the text the item writes under `sections: Criterion` (cases 188, 194.1). Its `method` holds only what runs in the Case's own session — a test, a command, a probe, or the reading of the Spec at Retro — or the person's answer; a problem seen live in a later session is a lesson, and pre-spec reports a `method` that waits for a later session, the librarian or a `/hi` (case 670.4). A rule with several promises ``
>   - old: `` through the `read` line of one the Case creates or sets `pending` or through one its `context` names, ``
>   - new: `` through the `read` line of one the Case creates or sets `pending`, which the Retro of the Case's own session takes on the Criterion of the Spec (case 670.4), or through one its `context` names, ``
>   - change: `a method holds only what runs in the Case's own session, or the person's answer; Retro takes the read line of the Case's own Estimate (case 670.4)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] `guppi/lint.py`: a predicate `waits_for_another_session` over the parts of a `method` between `;`, with its docstring; `check_moment` and the lint run do not call it.
> - [ ] `guppi/prespec.py`: the check of the form of an Estimate item calls `waits_for_another_session` on the `method` of a `create` and of an `update` that sets one, and the module docstring names the finding.
> - [ ] `tests/test_lint.py`: the predicate is true for a later session, the next session, a session after another, the librarian and `/hi`, and false for a part that names the person and for a method of the session itself.
> - [ ] `tests/test_prespec.py`: the finding on a `create` and on an `update` with `set: {method: …}`, none on a method that names the person, and the other method findings unchanged.
> - [ ] create `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`
>   - ref: `rule-prespec-hook`
>   - kind: `QA`
>   - purpose: `Whether pre-spec reports a method in the plan that waits for a later session, the librarian or a /hi, by one predicate of guppi/lint.py, and leaves a method that names the person and the live pages alone`
>   - method: `uv run pytest tests/test_prespec.py tests/test_lint.py -k waits`
>   - tags: `[harness, workflow]`
> - [ ] read `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`

> **ratification:**
> ```
> - decision[case 670.4][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 670.4][create][estimate-prespec-hook-reports-a-method-that-waits-for-another-session]{ref:rule-prespec-hook}{tags:harness,workflow}
> ```

### Case 670.5 — /hi reads no transcript and turns an unreadable Work line into a Case

> **given:**
> `rule-skill-hi`: the Render of the `/hi` skill, whose reading step changes.
> **＋** `.claude/skills/hi/SKILL.md`: the skill file rendered from it.
> **＋** `estimate-hi-takes-its-readings`: its Criterion is replaced whole.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier `/hi` writes.
> **＋** `vault/wiki/brief.md`: holds the `pending` readings and the Ask list.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

> **then:**
> In its first reply, before the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
> **＋** It opens the page of each Estimate it reads and judges the reading against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply, which ends in text.
> **＋** For each other open `W` line, whose reading cannot run now, it writes one line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` that names the Estimate by slug and asks to fix its method, replace its Criterion or archive it; the `W` line closes `· case N` when that Case is ratified.
> **＋** In the same reply, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
> **＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result, in a `LEDGER` block of the reply, which ends in text.
> **－** It reads no transcript of an earlier session.
> **－** A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and is no Cases line.
> **－** The Frontier is still assembled with no page opened. Only the reading step opens the pages of the Estimates it reads.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

> **tasks:**
> - [ ] update `rule-skill-hi`
>   - old:
>     ```
>     Before the question on the order, in the same reply, take each reading of an open `W` line whose whole method can be done now: each moment its `method` names is this `/hi` or has come in an earlier session (case 613.2). Read what the method names from the brief, `git log`, `git status` and the commands the method names, and each moment of an earlier session — the librarian's run, `/retro`, `/handoff` or any other — from the transcript of the latest session that held it: the event logs `vault/raw/<date>/event_log.md` name each session by the first characters of its id, and its transcript is the file of Claude Code whose name opens with that id; read each part of the method from the session where its moment came.
>     ```
>   - new:
>     ```
>     Before the question on the order, in the same reply, take each reading of an open `W` line whose whole method runs now, from files and commands alone: the brief, `git log`, `git status`, and the files and the commands the method names; read no transcript of an earlier session (case 670.5).
>     ```
>   - old:
>     ```
>     A reading with a moment that has come in no session yet, or whose transcript Claude Code no longer holds, waits for its next moment, and its line stays open; a reading whose `method` asks for a `/hi` run of its own is not taken here (cases 508.1, 613.2).
>     ```
>   - new:
>     ```
>     An open `W` line whose reading cannot run now — its method waits for a moment of an earlier session, for a moment not come, or for a `/hi` run of its own — needs a decision: write one line for it under `## Cases` of `frontier.md`, the Estimate by slug in a code span and the words that its method, its Criterion or the page itself is fixed, replaced or archived, with the source `brief`; its `W` line closes `· case N` when that Case is ratified. A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and waits for that session (case 670.5).
>     ```
>   - old: `` a `failed` reading or a lesson of the Tail; an item the person adds. ``
>   - new: `` a `failed` reading or a lesson of the Tail; an open `W` line whose reading cannot run now, written by the reading step below (case 670.6); an item the person adds. ``
>   - change: `/hi reads no transcript: it takes the readings it can run now, and an open Work line it cannot read becomes a Cases line, but those of the close of a sprint (cases 670.5, 670.6)`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] update `estimate-hi-takes-its-readings`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether /hi takes, in its first reply, each open W reading whose whole method runs now from files and commands, reads no transcript, writes a Cases line for each other open W line but those of the close of a sprint, puts each open Ask line to the person and writes the answer as its reading line, and opens no page but the Estimates it reads"
>     method: "by hand, the text of the skill file rendered from rule-skill-hi, or, at the Retro of the session that changes it, the new Render of rule-skill-hi in the Spec, read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — /hi reads no transcript, and an open Work line it cannot read becomes a Cases line (case 670.5)`
> - [ ] read `estimate-hi-takes-its-readings`

> **ratification:**
> ```
> - decision[case 670.5][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 670.5][update][estimate-hi-takes-its-readings]{ref:rule-skill-hi}
> ```

### Case 670.6 — The Frontier names an unreadable Work line among the sources of a Cases line

> **given:**
> `estimate-hi-writes-frontier`: its Criterion is replaced whole.
> **＋** `rule-skill-hi`: its Render lists the sources of a Cases line, changed by 670.5.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier `/hi` writes.
> **＋** `vault/wiki/sprint.md`: the sprint, whose current milestone gives items.
> **＋** `vault/wiki/brief.md`: the brief, whose Next session gives items.
> **＋** `vault/wiki/backlog.md`: the backlog, whose items the Frontier counts.

> **when:**
> The person invokes `/hi` of `rule-skill-hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md` and the output of the skill's commands, and closes its lines in Plan Mode.

> **then:**
> The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, `## Work`, with lines `- [ ] W<n> — <title> · <source>`, and `## Ask`, with lines `` - [ ] A<n> — `<slug>` — <question> · brief ``. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
> **＋** The kind comes from the source. Cases: first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line; then, on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an open `W` line whose reading cannot run now, written by the reading step of `/hi`; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`. Ask: the `Ask the person` list of the brief's Next session.
> **＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
> **＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when decided, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`.
> **＋** An item closed `defer` or `kept` has no short Case and no ledger line. A sprint item never closes `· defer case N`.
> **＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
> **＋** In the chat the Cases are shown as a checklist. Each line stands as `raw/<date>/<hi HHMM>/frontier.md` holds it, `- [ ] C<n> — <title> · <source>`, with its detail on an indented line under it and the `- near` line under that, and the line `Backlog: N items` comes last. The Work is shown as one block. Only Cases are cut into sub-cases. A `W` that turns out to need a decision closes `· case N`. A `C` that needs none closes `· work`.
> **－** While the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, no conserved Spec and no item of the current milestone is a Cases line, and each conserved Spec stays in `vault/wiki/backlog.md`.
> **－** At `/hi` no Case stands in the chat as a bold line, and no Case has its detail as a paragraph.
> **－** Pre-spec finds an open line under `## Cases`. A `W` or an `A` line stands open until its work is done and closes `· work` where that work is done: at `/hi`, in Work Mode or at Retro. Claude Code's plan mode does not stop the agent from writing `frontier.md`.

> **tasks:**
> - [ ] update `estimate-hi-writes-frontier`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — an open W line whose reading cannot run now is a source of a Cases line (case 670.6)`
> - [ ] read `estimate-hi-writes-frontier`

> **ratification:**
> ```
> - decision[case 670.6][update][estimate-hi-writes-frontier]{ref:rule-skill-hi}
> ```

### Case 670.7 — The Work line of an Estimate the session changes closes at Retro

> **given:**
> `rule-work-mode`: the Render of the `/work` skill, whose step of the Work readings changes.
> **＋** `.claude/skills/work/SKILL.md`: the skill file rendered from it.
> **＋** `estimate-work-mode-takes-the-work-readings`: its Criterion is replaced whole.
> **＋** `/retro`: the Retro that reads each Estimate the session changes and closes its line, by 670.2.
> **＋** `/box`: runs a conserved Spec and calls `/work` with its folder.
> **＋** `vault/raw/<date>/<HHMM>/`: the folder of a conserved Spec.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec Work Mode runs.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: holds the `W` lines.
> **＋** `vault/wiki/where-to-stop.md`: the conditions of a stop.

> **when:**
> The agent calls `/work` of `rule-work-mode` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the last task of `raw/<date>/<hi HHMM>/spec.md` is done.
> **＋** Or `/box` called `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec, and the last task of that folder's `spec.md` is done.

> **then:**
> Before `/retro`, the agent takes, in the order of `raw/<date>/<hi HHMM>/frontier.md`, each reading of an open `W` line whose work is built and whose moment, as its `method` names it, has come.
> **＋** A moment of an earlier session, such as the librarian's run, has come.
> **＋** Every reading taken is first marked done in `raw/<date>/<hi HHMM>/frontier.md`, and its `estimate[...]` line stands in the `LEDGER` block of the one reply that ends Retro.
> **＋** The tasks, the readings and `/retro` run in one turn, and no reply ends before the reply that ends Retro, except at a stop of `vault/wiki/where-to-stop.md`.
> **－** A reading of an Estimate this session creates or updates is not taken in this step: its `W` line stays open until `/retro` reads that Estimate or sets it `failed`, and closes the line.
> **－** With a folder from `/box`, a reading of an Estimate that a decision line of that folder's `ledger.md` creates or updates is not taken in this step either, and Retro closes its `W` line the same way.
> **－** A reading whose moment has not come is not taken, and its `W` line stays open.
> **－** The step ticks no `read` box of `raw/<date>/<hi HHMM>/spec.md`.

> **tasks:**
> - [ ] update `rule-work-mode`
>   - old: `` and one whose moment has not come: its line stays open. ``
>   - new: `` and one whose moment has not come: its line stays open; Retro reads an Estimate this session or that folder creates or updates, or sets it `failed`, and closes its line (case 670.7). ``
>   - change: `the Work line of an Estimate the session changes stays open until Retro reads it and closes it (case 670.7)`
> - [ ] `uv run guppi render`: `.claude/skills/work/SKILL.md`
> - [ ] update `estimate-work-mode-takes-the-work-readings`
>   - set:
>     ```
>     status: pending
>     method: "by hand, the text of the skill file rendered from rule-work-mode, or, at the Retro of the session that changes it, the new Render of rule-work-mode in the Spec, read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the Work line of an Estimate the session changes closes at Retro (case 670.7)`
> - [ ] read `estimate-work-mode-takes-the-work-readings`

> **ratification:**
> ```
> - decision[case 670.7][update][rule-work-mode]{ref:rule-work-mode}
> - decision[case 670.7][update][estimate-work-mode-takes-the-work-readings]{ref:rule-work-mode}
> ```
