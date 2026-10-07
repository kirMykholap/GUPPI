## Case 725 — A fix adds a second behaviour to a ratified Case beside it

> **context:**
> The ledger only grows. A Case ratified in the session keeps its decision lines under its number, so a ratified Case with no sub-cases cannot become a parent under that number. The `## Splitting` section of `vault/wiki/case-schema.md` sends a Case built again in another shape to a new number whose decision lines carry `{supersedes:case N}` (cases 610.1, 671.1). At the `/pre-spec` of session 1804, finding F6 asked ratified Case 713 to replace one more Criterion. Its `case-guppi` split 713 into 713.1 and 713.2 under the old number, then built Case 719 to supersede it, and the check of the Case file refused 719 (ledger lines 27 and 28 of that session, `lesson-case-build-splits-a-ratified-leaf-case`). Case 722.1 of this session sets the fix of the stale store entries behind that refusal. A second cause stands: `other_blocks` of `guppi/casecheck.py` leaves out only a Case that a mark of the session's ledger names. A mark reaches the ledger only when the new build is ratified, so a new build is compared with the first build while it stands in the plan. The pairs of the first build are applied first, and the new build's old texts then miss. The `recommend` of Case 722 records the same refusal. The rule of `case-guppi` also contradicts itself. One sentence tells it to empty a file it leaves behind under another number. Another sentence says that it empties no file of a Case with a decision line. `rule-orchestration` says that such a file is never emptied (case 701.4). This session the file of ratified Case 722 was emptied that way and written back.
>
> Case 725.1 has `case-guppi` build a second behaviour as a Case of its own beside the ratified Case, with no mark, and empty a file left behind only when its Case has no decision line. It replaces the Criterion of `estimate-case-build-writes-the-case` whole. That Criterion held more than seven lines before this Case and is carried whole but for four lines that this Case changes. Those are the third `when` line, which adds a finding of `/pre-spec`; the line on the drop of a Case, whose file left behind is now emptied only with no decision line; the line on the files `case-guppi` writes, which adds the file of a new Case; and the line on the files it never empties, which now names the file left behind. Its `purpose` and `method` do not state the changed lines and stand. A Grep of `under another number` over `vault/wiki/` and `.claude/` printed `vault/wiki/rules/rule-case-build.md`, `vault/wiki/estimates/estimate-case-build-writes-the-case.md` and `.claude/agents/case-guppi.md`, its Render, and each enters this Case. The `## Splitting` section of `rule-case-protocol` stays true: it sets the path for a fix that changes what a ratified Case already set. It is not changed here, since Case 722.3 of this session puts `rule-case-protocol` off, and `/pre-spec` reports a Case that changes a page another Case of the plan puts off (case 186.2). `vault/wiki/orchestration.md` says the main agent dispatches `case-guppi` with the Case id. A new Case whose number `case-guppi` picks stands beside that, as a number the check gives does (case 610.1).
>
> Case 725.2 makes the check leave out a Case that a mark on a decision line of the answer's own file names. A Grep of `other_blocks\(` over `guppi/` printed `guppi/casecheck.py` alone. Case 722.1 replaces the Criterion of `estimate-case-check-sends-back-a-clash-with-another-case` whole and rewrites a clause of the Purpose of `rule-case-check`. So Case 725.2 creates its own Estimate and adds its clause to the end of the sentence of that Purpose whose start 722.1 rewrites. The two new texts fit side by side. The text of 722.1 names the Cases the check leaves aside: a dropped Case and a stored Case that the file of its top-level Case no longer holds. The clause of 725.2 comes after the end of that sentence, which 722.1 leaves as it stands, and it adds a Case that a mark of the file itself names. The first `then` line of Case 722.1 says that each Case of the plan file is judged, and its exceptions list only the marks of the ledger. Case 722.1 should add to that exception a Case that a mark on a decision line of the answer's own file names. The Criterion of `estimate-case-check-applies-the-pairs-of-the-session-in-order` leaves out a Case that any mark names, and stands.

> **problem:**
> A fix that adds a second behaviour to a ratified Case with no sub-cases has no step in the rule of `case-guppi`. A Case built again under a new number is refused by the check while the build it replaces stands in the plan. The rule also tells `case-guppi` to empty the file of a ratified Case that it leaves behind under the old number.

> **recommend:**
> - **Where the second behaviour of a ratified Case with no sub-cases goes**
>   - Recommended: (a) a Case of its own under a new number beside the ratified one, with no retiring mark; a build under a new number stays only for a fix that changes what the ratified Case already set.
>   - Answer: agreed, (a).
> - **Whether this Case also fixes the check's refusal of a build under a new number**
>   - Recommended: (a) fix it here, in a sub-case: the check also leaves out each Case that a retiring mark on a ledger line of the answer's own file names, checked by a new Estimate.
>   - Answer: agreed, (a).
> - **What happens to the file left behind under the old number**
>   - Recommended: (a) empty only the file of a Case with no ledger line; the file of a ratified Case stays, and the Criterion of `estimate-case-build-writes-the-case` is replaced.
>   - Answer: agreed, (a).

### Case 725.1 — The rule of case-guppi builds a second behaviour beside a ratified Case

> **given:**
> `rule-case-build`: the rule of `case-guppi`, whose Render changes.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from `rule-case-build`.
> **＋** `estimate-case-build-writes-the-case`: its Criterion is replaced whole.
> **＋** `vault/wiki/case-schema.md`, `vault/wiki/ratification.md` and `vault/wiki/orchestration.md`: the form of a Case, the ledger lines, and the rule that the file of a Case with a decision line is never emptied.
> **＋** `.claude/skills/grill-me/SKILL.md`, `.claude/agents/ask-guppi.md` and `.claude/settings.json`: the template of a round, the vault query and the hooks the frame reads.
> **＋** `rule-case-check` and `/pre-spec`: the hook that checks the file of a Case, and the check whose findings reach `case-guppi`.
> **＋** `guppi/ratified.py`: the guard of the files under `raw/<date>/<hi HHMM>/cases/`.
> **＋** `raw/<date>/<hi HHMM>/ledger.md` and `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the ledger of the session and the file of a Case.

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
> **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.
> **＋** Or the main agent sends it by `SendMessage` the drop of the Case it built, the drop of a change to that Case, or a finding of `/pre-spec` on that Case.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
> **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
> **＋** When no fork is open, it writes the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
> **＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file; a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, a Case with sub-cases included; then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
> **＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
> **＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
> **＋** Asked, by a message or by a finding of `/pre-spec`, for a fix that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases, it builds that behaviour as a new top-level Case beside it, in its own file and with no `{supersedes:case N}` mark. The number of the new Case is one above the highest number of the files under `raw/<date>/<hi HHMM>/cases/` and of the decision lines of that ledger, or the free number that the guard of `guppi/ratified.py` names when it refuses that number. The ratified Case and its file stay as they are, and its summary names the new Case.
> **＋** A pair of that new Case whose sentence the ratified Case changed takes that sentence as the ratified Case leaves it.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write and Edit, and `permissionMode: auto`, so it writes its file with no prompt while the session is in Plan Mode.
> **＋** Sent the drop of its Case, which has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, it writes empty text into the file of that Case by `Write` and answers with a first line `**Dropped:**` and the path of the file, and nothing else. A file of its own that it leaves behind, when it builds the Case again under another number, it empties the same way only when that Case has no decision line in that ledger.
> **＋** Sent the drop of a change to its Case, which has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and which it changed after the Case was last ratified, it undoes by `Edit` each edit it made since then in every section but `recommend`. `recommend` keeps its items and gains one item `**Change**`: its `Asked:` line says that the person dropped the change, and its `Taken:` line says that the Case went back to its ratified form. It answers with the summary again, so that the check of `rule-case-check` finds an item for each question of its rounds.
> **－** A fix that changes what the ratified Case already set is not built beside it: `case-guppi` builds the Case again under a new number, as `vault/wiki/case-schema.md` sets it.
> **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
> **－** It does not write the whole Case again to fix a finding, make a change or undo a change.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
> **－** It writes no file but the file of its Case, the file it leaves behind under an earlier number of the same Case, and the file of a new Case it builds beside a ratified Case, and no ledger line.
> **－** It empties no file of a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, the file it leaves behind when it builds that Case again under a new number included: sent the drop of such a Case that it did not change after the Case was last ratified, it answers under a first line `**Fact:**` that the Case is ratified, and the file stands.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` Asked again by a message, change the file as asked, by `Edit` of the lines that change, and answer with the summary again, or answer with a round when the message opens a fork (case 645.1). ``
>   - new: `` Asked again by a message, change the file as asked, by `Edit` of the lines that change, and answer with the summary again, or answer with a round when the message opens a fork (case 645.1). A fix, asked by a message or by a finding of `/pre-spec`, that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases, you build as a new top-level Case beside it, in its own file and with no `{supersedes:case N}` mark, under a number one above the highest number of the files under `raw/<date>/<hi HHMM>/cases/` and of the decision lines of that ledger, or the free number that the guard of a case file names when it refuses yours; the ratified Case and its file stay as they are, a pair of the new Case whose sentence the ratified Case changed takes that sentence as the ratified Case leaves it, and your summary names the new Case; a fix that changes what the ratified Case already set you build again under a new number, as `vault/wiki/case-schema.md` sets it (case 725.1). ``
>   - old: `` a file of yours that you leave behind when you build the Case again under another number you empty the same way, since the hook of `rule-prespec-onward` takes an empty file for no Case; ``
>   - new: `` a file of yours that you leave behind when you build the Case again under another number you empty the same way only when that Case has no decision line, since the hook of `rule-prespec-onward` takes an empty file for no Case, and the file of a Case with a decision line stands, since it keeps the `context` and `given` that its Decision page leaves there (case 725.1); ``
>   - old: `Write no file but the file of your Case, the file you leave behind under an earlier number of the same Case included, and no ledger line.`
>   - new: `Write no file but the file of your Case, the file you leave behind under an earlier number of the same Case included, and the file of a new Case you build beside a ratified Case (case 725.1), and no ledger line.`
>   - change: `case-guppi builds a second behaviour of a ratified Case with no sub-cases as a new Case beside it, and empties a file left behind under another number only when its Case has no decision line (case 725.1)`
> - [ ] update `estimate-case-build-writes-the-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a second behaviour of a ratified Case is a new Case beside it, and the file of a ratified Case left behind is not emptied (case 725.1)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-writes-the-case`

> **ratification:**
> ```
> - decision[case 725.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 725.1][update][estimate-case-build-writes-the-case]{ref:rule-case-build}
> ```

### Case 725.2 — The check leaves out a Case the file of the answer supersedes

> **given:**
> `rule-case-check`: the rule of the check of the file of a Case, whose Purpose says which Cases the check compares.
> **＋** `estimate-case-check-leaves-out-a-case-the-file-supersedes`: the new check of this exception.
> **＋** `guppi/casecheck.py`: `other_blocks`, which picks the other Cases of the session, and `ratification_records`, which reads the decision lines of the answer; it imports `check_same_target` and `check_pairs` of `guppi/prespec.py`.
> **＋** `tests/test_casecheck.py`: the tests of a clash with another Case.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.
> **＋** `raw/<date>/<hi HHMM>/ledger.md` and `rule-spec-write`: the ledger whose marks retire a Case, and the hook that removes a retired Case from the plan file at ratification.
> **＋** `raw/2026-10-07/2114/cases/case-722.md`: Case 722.1, which changes the Purpose of `rule-case-check` and the Criterion of its clash check.

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case whose file `raw/<date>/<hi HHMM>/cases/case-<N>.md` holds a decision line that carries `{supersedes:case M}`, and `uv run guppi casecheck --subagent` reads the Cases of the answer, the plan file of the session, `<plan>.checked.json` beside it and the session's `raw/<date>/<hi HHMM>/ledger.md`, while the plan file or the store holds Case M.
> **＋** Or `tests/test_casecheck.py` runs it over a made-up file, plan file, store and ledger.

> **then:**
> The hook leaves Case M and its sub-cases out of the other Cases of the session, by `other_blocks` of `guppi/casecheck.py`, as it leaves out a Case that a mark of the session's ledger names; a mark on a sub-case leaves out that sub-case alone.
> **＋** Case M is not judged with the Cases of the answer by `check_same_target` of `guppi/prespec.py`, and its pairs are not applied before theirs by `check_pairs`, so a Case built again under a new number gets no clash and no pair finding from the build it replaces while that build stands in the plan file or the store.
> **＋** The marks are read from the decision lines of the `ratification` fences of the answer by `ratification_records` of `guppi/casecheck.py`, the one reading of those lines in the hook.
> **＋** A clash or a pair finding with any other Case of the session stays a finding.
> **－** The mark removes nothing from the plan file or the store: the `Stop` hook of `rule-spec-write` removes Case M only when the Case that carries the mark is ratified.
> **－** The findings on a Case ratified in the session and built again under its old number, in another shape or without a target, still read the decision lines of the session's ledger.

> **tasks:**
> - [ ] update `rule-case-check`
>   - old: `` so a Case that writes what another Case writes goes back to `case-guppi` before the person first sees it (case 629.1). ``
>   - new: `` so a Case that writes what another Case writes goes back to `case-guppi` before the person first sees it (case 629.1); a Case that a `{supersedes:case N}` mark on a decision line of the file itself names is no such other Case, so a Case built again under a new number passes the check while the build it replaces stands in the plan (case 725.2). ``
>   - change: `the check of the file of a Case leaves out a Case that a supersedes mark of the file itself names (case 725.2)`
> - [ ] create `estimate-case-check-leaves-out-a-case-the-file-supersedes`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the check of an answer of case-guppi leaves out of the other Cases of the session a Case that a supersedes mark on a decision line of the answer's own file names, so that a Case built again under a new number passes while the build it replaces stands in the plan`
>   - method: `uv run pytest tests/test_casecheck.py -k superseded_by_the_file`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `guppi/casecheck.py`: `other_blocks` also leaves out each Case, with its sub-cases, that a mark of `ratification_records` of the answer names; its docstring and the module docstring say so.
> - [ ] `tests/test_casecheck.py`: `superseded_by_the_file` tests — a Case of the plan that a mark of the file names gives no clash and no pair finding; a mark on a sub-case leaves its parent compared; the same file without the mark gives the clash.
> - [ ] read `estimate-case-check-leaves-out-a-case-the-file-supersedes`

> **ratification:**
> ```
> - decision[case 725.2][update][rule-case-check]{ref:rule-case-check}
> - decision[case 725.2][create][estimate-case-check-leaves-out-a-case-the-file-supersedes]{ref:rule-case-check}{tags:hooks,harness,workflow}
> ```
