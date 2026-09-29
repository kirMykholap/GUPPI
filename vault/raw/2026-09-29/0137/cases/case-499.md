## Case 499 — Slice 3g: the Estimates of the end of a session recut to one Criterion, and the handoff names its file to the librarian

> **context:**
> Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. The page carries its promise as a `purpose` field and its way of checking as a `method` field. The older Estimates lack both fields. They carry `## Context` and `## Method`, and stack `Given:` or `### case N` blocks, and `make lint` counts them as `unmigrated`. This group holds the two Estimates of the end of a session: `estimate-end-of-work-order`, which still opens with a `Given:` about the Spec hook, the cascade and the methods of other Estimates, and `estimate-handoff-dispatches`, which has a head paragraph and block 73.7. The two parts of the second page disagree. The head says the librarian is dispatched "with the date". Block 73.7 says it is dispatched with the path of `handoff.md`. The skill `/handoff` sends only `Materialize <date>.`, but the librarian's frame takes as its first input "the `handoff.md` your dispatch names". The History of `rule-handoff` records that case 73.7 meant the path, "the librarian is dispatched with its path". The Render never got the path, so the librarian has had to find the file on its own.
> The person decided in the first round on this item. The twelve old pages go in three Cases by area: case 498 took rendering and settings, this Case takes the end of a session, and case 500 takes the librarian's and the vault's tools and replaces the Slice note. Each page gets one Criterion, no page is split, and each live half of a reading stays. In the second round the person chose to keep the path in the promise and to change the skill to match. So 499.2 changes the Render of `rule-handoff` to send `Materialize <date> from <path of handoff.md>.` and recuts `estimate-handoff-dispatches` to that behaviour. Neither page has `purpose` or `method`, so each `update` sets both, and setting `method` drops `## Context` and `## Method` (case 211). Each Criterion is replaced whole and goes back to `pending`, and its reading waits for a later session (case 428.1). `rule-end-of-work` goes from `built` to `draft` until the reading. `rule-handoff` is `draft` already. Neither page lost its Criterion to a tool fault like case 211.3. Their History shows only Criteria that cases 38, 38.3, 73.7, 190.2 and 196.2 wrote on purpose, so nothing is restored.
> What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. In 499.1 the `Given:` goes out whole. Its lines describe the Spec hook, the cascade of case 190.2, the methods of three Estimates and the order of the entries of 190.x, and all of these are history. The line on `rule-carry-over` as a child is already in `Then:`. "`make test-end-of-work` is green" moves into `method`. The `－` line "The order of the three steps of the ordinary way does not change" goes out as a bound of an edit, because the order itself stands in the line before it. In 499.2 "with the date" gives way to the path the person chose. "The first turn's context holds git status --porcelain" is kept as the skill's own check.
> The check also notes that 499.2 shares words with 499.1 on `/handoff` on a dirty tree and on the commit after the handoff. This is expected. 499.1 promises the order of the ordinary end of a session, read across its folder, the event log and `git log`: the gate of `guppi/gate.py` refuses a dirty tree, and no other commit stands between the handoff and the librarian's. 499.2 promises what the skill does when it is called: it stops on a dirty tree, writes the note, dispatches with the path, and commits nothing itself. Both old pages held these lines, as cases 38 and 38.3 signed them. `estimate-session-phases-in-order` (case 493.4) promises that the marks of all five phases rise in time, a reading across the whole session. 499.1 promises the gate and the two ends inside End of Work, so it is not touched.
> The frame. The kept lines were read against the Render of `rule-handoff`, the Purpose and `children` of `rule-end-of-work`, `guppi/gate.py`, the `Makefile` and the frame of the librarian, `.claude/agents/librarian-guppi.md`. With the new Render, the librarian's "the `handoff.md` your dispatch names" becomes true. No test and no script reads the dispatch line. The new skill text lands at the render of the librarian's run. So the `/handoff` of this session still sends the date alone, and its librarian finds the folder as it has so far. Nothing refuses in between and nothing is lost, so no old form is kept. `estimate-handoff-holds-each-fact-once` promises the content of the three sections, not the dispatch, and is left alone. The pair of 499.2 hits the one sentence of the Render that names the dispatch. The History line of 499.3 does not say the Slice note stands, because case 500.6 replaces that note in the same librarian's run. The Case creates no page, so no vault query was run. Not done: case 500 and the note of Slice 3g, and the removal of the old-layout checks.

> **problem:**
> The two Estimates of the end of a session still have the layout from before case 193, and lint counts them as `unmigrated`. One of them promises two different dispatch texts, and the skill it reads sends neither the path it promised nor the file the librarian expects.

> **recommend:**
> Replace each Criterion whole with one `When:` and `Then:`, set `purpose` and `method`, and change the dispatch line of the skill so that it names `handoff.md` by its path, as case 73.7 meant. Recutting the promise to the date alone was rejected, because it would narrow a signed promise to fit a slip in the skill and leave the librarian's frame wrong.

### Case 499.1 — A session ends one of two ways, the ordinary way in order

> **given:**
> `estimate-end-of-work-order` — the promise, its Criterion replaced whole
> **＋** `rule-end-of-work` — the MOC it promises for, its `children` and the two ends in its Purpose
> **＋** `rule-carry-over` — the second end, `/carry` straight after Plan Mode
> **＋** `rule-handoff` — the child that `rule-carry-over` follows
> **＋** `guppi/gate.py` — the gate that refuses `/handoff` on a dirty tree
> **＋** `vault/raw/<date>/<hi HHMM>/` — the session's folder, with `handoff.md`
> **＋** `vault/raw/<date>/event_log.md` — the day's event log
> **＋** `Makefile` — the target `test-end-of-work`

> **when:**
> A session ends, and someone reads its folder `vault/raw/<date>/<hi HHMM>/`, the day's event log `vault/raw/<date>/event_log.md` and `git log`.

> **then:**
> The session ended one of two ways: Work Mode, Retro, the commit, the handoff and the librarian; or `/carry` straight after Plan Mode.
> **＋** In the ordinary way the order holds: `/handoff` is refused while the tree is dirty; `handoff.md` exists before the librarian is dispatched; no other commit stands between the handoff and the librarian's commit.
> **＋** On leaving Plan Mode the agent asks the person which of the two ends, and starts nothing until it is answered.
> **＋** `rule-carry-over` is a child of `rule-end-of-work`, after `rule-handoff`.

> **tasks:**
> - [ ] update `estimate-end-of-work-order`
>   - set: `{status: pending, purpose: "A session ends one of two ways, and the ordinary way keeps its order: the commit before /handoff, handoff.md before the librarian, no commit between the handoff and the librarian's", method: "make test-end-of-work, plus by hand at the close of a later session: its folder, the day's event log and git log"}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the bounds line out, the green run of make test-end-of-work into method; purpose and method set, Context and Method out (case 499.1)`
> - [ ] read `estimate-end-of-work-order` — `make test-end-of-work`, then by hand at the close of a later session

> **ratification:**
> ```
> - decision[case 499.1][update][estimate-end-of-work-order]{ref:estimate-end-of-work-order}
> ```

### Case 499.2 — `/handoff` writes the note and dispatches the librarian with its path

> **given:**
> `rule-handoff` — the rule whose Render is the skill `/handoff`; its dispatch line changes
> **＋** `estimate-handoff-dispatches` — the promise, its Criterion replaced whole
> **＋** `.claude/skills/handoff/SKILL.md` — the skill rendered from `rule-handoff`
> **＋** `.claude/agents/librarian-guppi.md` — the librarian, whose first input is the `handoff.md` its dispatch names
> **＋** `guppi/gate.py` — the gate of `/handoff` and its `handoff` mark
> **＋** `vault/raw/<date>/<hi HHMM>/` — the session's folder, where `handoff.md` is written
> **＋** `vault/raw/<date>/event_log.md` — the day's event log

> **when:**
> The person invokes `/handoff` after the Retro, the gate of `guppi/gate.py` reads the tree, and the agent runs the skill `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff`.

> **then:**
> The skill's context holds `git status --porcelain`. On a dirty tree the skill stops and says "commit first", and nothing is written.
> **＋** On a clean tree the day's event log `vault/raw/<date>/event_log.md` holds the `handoff` mark of the call.
> **＋** The agent writes `handoff.md` into the session's folder `vault/raw/<date>/<hi HHMM>/`: one document with no `---` and the three sections `## Notes from memory`, `## Direct instructions to the librarian` and `## What actually got done`, with no Read call on the artifacts.
> **＋** Then the agent dispatches `librarian-guppi` with one line, `Materialize <date> from <path of handoff.md>.`, the path being that of the file just written, and shows the librarian's report to the person unchanged.
> **－** No commit follows the handoff except the librarian's own.

> **tasks:**
> - [ ] update `rule-handoff`
>   - old: `` Then dispatch the `librarian-guppi` agent with one line: `Materialize <date>.` ``
>   - new: `` Then dispatch the `librarian-guppi` agent with one line: `Materialize <date> from vault/raw/<date>/<hi HHMM>/handoff.md.`, the path of the file you just wrote. ``
>   - change: `the dispatch names handoff.md by its path, as case 73.7 meant and the librarian's frame reads (case 499.2)`
> - [ ] update `estimate-handoff-dispatches`
>   - set: `{status: pending, purpose: "/handoff stops on a dirty tree, writes handoff.md from memory into the session's folder and dispatches the librarian with its path, with no commit after", method: "by hand at the /handoff of a later session: the event log, handoff.md, the dispatch line and git log"}`
>   - change: `the Criterion replaced whole — the head and the block 73.7 into one When and Then, the dispatch by the path; purpose and method set, Context and Method out (case 499.2)`
> - [ ] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
> - [ ] read `estimate-handoff-dispatches` — by hand at the `/handoff` of a later session

> **ratification:**
> ```
> - decision[case 499.2][update][rule-handoff]{ref:rule-handoff}
> - decision[case 499.2][update][estimate-handoff-dispatches]{ref:estimate-handoff-dispatches}
> ```

### Case 499.3 — The sprint page records the group of the end of a session

> **given:**
> `entity-sprint-migration` — the sprint page whose History records the recut
> **＋** `rule-end-of-work` — a rule whose Estimate this Case recuts
> **＋** `rule-handoff` — a rule whose Estimate this Case recuts

> **when:**
> The librarian's run applies the `update` of `entity-sprint-migration`.

> **then:**
> The History of `entity-sprint-migration` says that the Estimates of the end of a session are recut.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - change: `Slice 3g: the Estimates of rule-end-of-work and rule-handoff recut to one Criterion, the dispatch of the handoff by its path (case 499)`

> **ratification:**
> ```
> - decision[case 499.3][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
