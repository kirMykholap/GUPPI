## Case 739 — A page the cascade archives is noted before it is updated

> **context:**
> After a session, `uv run guppi generate` applies the items of the Spec and then runs its cascade. The cascade archives each `clustered` lesson of an Insight set `actioned`, archives an `open` Insight left with no live child, and archives a superseded Decision page. It also moves a rule or an entity between `built` and `draft`. No check of a Case looks at that cascade. In session 1547, Case 736.1 set `insight-workflow-contract-change-leaves-its-derived-text-stale` `actioned`, and Case 737 tagged its clustered lesson `lesson-case-build-misses-the-example-a-changed-check-runs-over`. The same librarian run applied the tags and then archived the lesson. `generate` printed nothing about it, since `cascade` of `guppi/generate.py` tests only the status of the lesson. `ask-guppi` found the clash at `/pre-spec`, the person kept the target, and both Cases were ratified a second time. `lesson-case-build-misses-the-cascade-of-a-related-case` records it and joined no Insight. The person chose a check by script over a new step of `case-guppi`. The rules of the cascade move out of `cascade` into one function of `guppi/generate.py` that `cascade` calls, and `/pre-spec` and the check of the file of a Case both use it. The check runs at both moments. It covers the three steps that archive a page and only an `update` of such a page. It gives a note, not a finding, and an `update` and its archive inside one Case give the note too. Case 739.1 is the note of `/pre-spec`, and Case 739.2 is the note of the check of the file. Each creates its own Estimate, since the two can fail apart and need different fixes. The judgment of which pages, items and Cases give the note is signed once, in Case 739.1; the `then` of Case 739.2 points to that Estimate and adds only who gets the note in the file and how it is sent, so nothing is signed twice. Q5 named the second Estimate `estimate-case-check-notes-a-page-another-case-archives`. After Q7 the archive may come from the same Case, so both Estimates end in `the-cascade-archives`. `estimate-generate-cascades` stands: the function keeps every answer of `cascade`, and `tests/test_generate.py` shows it. The Render of `rule-prespec` leaves what the check compares to the module docstring of `guppi/prespec.py`, so no sentence of the page changes, and Case 739.1 changes only that docstring and the code. Case 738 of this session also changes `guppi/prespec.py`: `check_form`, which this Case does not touch, and the module docstring, which this Case changes too. Its patch adds the MOC form to the list of the form of an Estimate item, at `@@ -81,7 +81,10 @@` of `vault/raw/2026-10-08/0213/patch-prespec-moc-method-form.diff`, and Case 739.1 adds the cascade notes under the Notes paragraph of the same docstring. The patch of Case 738 lands first, and Case 739.1 adds its notes after it, on the docstring as that patch leaves it. The Purpose of `rule-case-check` lists the notes and the checks that the file of a Case gets, so Case 739.2 adds one sentence after the note of case 711.2. No other sentence of that Purpose becomes false, since the new note is a judgment of `/pre-spec`, imported. No Criterion of an Estimate of `rule-case-check` or `rule-prespec` speaks against a new note. The new Estimate of `rule-case-check` sets that page from `built` to `draft` until it is read. A Grep of `(ROOT|REPO)\s*/\s*"(vault|\.claude)"` over `tests/` printed `tests/test_case_schema.py`, `tests/test_generate.py`, `tests/test_orchestration.py` and `tests/test_schemas.py`. Only `tests/test_case_schema.py` runs a live text through the changed code: the example of `vault/wiki/case-example.md` goes through `check_answer` of `guppi/casecheck.py`, and the test fails on any note. The example sets no status of an Insight and carries no `{supersedes:case N}` mark, and the test runs over a temporary project with no lesson or Insight page, so it gives no new note. `estimate-case-example-passes-the-check` already checks this: its Criterion says that the check gives the example no finding and no note, and that a change of the check that gives one fails the test. Its Criterion stands, since this Case keeps that promise, so it is not set `pending` and gets no `read` line; the task line of `tests/test_case_schema.py` under Case 739.2 runs its test. The other three read `schema.yaml` files or `vault/wiki/orchestration.md`. The lesson line of `lesson-case-build-misses-the-cascade-of-a-related-case` stands in the ledger of session 1547, so no decision line here carries an `{addresses:...}` mark, and the lesson stays `new`. The backlog item `insight-ledger-ratified-line-never-withdrawn` is about the number of a Case built again, not about the cascade, and stays out.

> **problem:**
> A Case can update a page that the cascade of `generate` archives in the same run, after an item of another Case of the session or of its own. No script reports it, so the update is lost in the archive unless a person or `ask-guppi` sees it.

> **recommend:**
> - **Where does the fix for a missed cascade live?**
>   - Recommended: (a) a step in the instructions of `case-guppi`, which follows the cascade of each related Case onto the pages its own Case changes.
>   - Answer: none of the options. The person wants a check by script that takes the logic of the cascade from the script that writes the pages, so that the Cases are checked at `/pre-spec`, before the pages are written. The person asked whether it should also run earlier, on one Case.
> - **Where does the script check of the cascade run?**
>   - Recommended: (a) at both moments, the check of the file of a Case and `/pre-spec`, by one shared function.
>   - Answer: agreed, (a).
> - **Does a cascade hit block the Case or only warn?**
>   - Recommended: (a) a note: the Case drops the update or its `context` says why it stands, and the person may keep the target.
>   - Answer: agreed, (a).
> - **Which steps of the cascade does the check cover?**
>   - Recommended: (a) the steps that archive a page: the lessons of an Insight set `actioned`, an `open` Insight with no live child, and a superseded Decision page.
>   - Answer: agreed, (a).
> - **How is the change split, and what checks it?**
>   - Recommended: (a) one Case with two sub-cases, the note of `/pre-spec` and the note of the check of the file, each with a new Estimate read by its unit tests; the rules of the cascade go into one shared function of `guppi/generate.py`, and `estimate-generate-cascades` stands.
>   - Answer: agreed, (a).
> - **Which changes of a Case get the note?**
>   - Recommended: (a) an `update` only; a `delete` of such a page ends where the cascade ends.
>   - Answer: agreed, (a).
> - **Does a Case that both sets the status and changes the page get the note?**
>   - Recommended: (a) no note inside one Case and its sub-cases, as in the note on a page another Case puts off.
>   - Answer: (b): a note inside one Case too, its sub-cases compared with each other as well.

### Case 739.1 — Pre-spec notes a page the cascade archives

> **given:**
> `estimate-prespec-notes-a-page-the-cascade-archives`: the new check of the note.
> **＋** `rule-prespec`: the rule of pre-spec, the target of the new Estimate; its text does not change.
> **＋** `guppi/prespec.py`: the check `--check` and its module docstring, which gain the note.
> **＋** `guppi/generate.py`: `cascade`, whose rules of the archive move into one function that the check imports.
> **＋** `tests/test_prespec.py`: the unit tests of the note.
> **＋** `tests/test_generate.py`: the tests of the cascade, which run green over the moved function.
> **＋** `rule-prespec-hook`: the hook on the exit from Plan Mode, which blocks on a finding and not on a note.
> **＋** `vault/raw/2026-10-08/2134/cases/case-738.md`: Case 738 changes `check_form` and the module docstring of `guppi/prespec.py` in the same session, and lands first.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads the `then` blocks of the plan and the decision lines of the session's window.
> **＋** Or `tests/test_prespec.py` runs it over a made-up plan.

> **then:**
> For each `update` item of the plan whose page the cascade of `guppi/generate.py` archives once the items of the plan apply, the check prints one line that opens with `note:` and names the Case of the `update`, the page and the Case whose item sets off the archive.
> **＋** The pages archived are: each lesson standing `clustered` among the `children` of an Insight that an `update` of the plan sets `status: actioned`; each Insight standing `open` whose every child stands `archived` once the items of the plan apply; and the Decision page of each Case that a `{supersedes:case N}` mark on a decision line of the session names.
> **＋** The pages are judged by one function of `guppi/generate.py`, which the cascade of `uv run guppi generate` calls too.
> **＋** An `update` and the item that sets off its archive in one Case, or in two sub-cases of one Case, give the note too.
> **＋** The note is no finding: it does not change the exit code, and the hook of `rule-prespec-hook` does not block the exit from Plan Mode on it.
> **＋** The agent answers the note in one line in the chat, and the person may change a Case or keep the `update`.
> **－** A `create`, `delete` or `defer` item of such a page gives no note.
> **－** A rule or an entity that the cascade moves between `built` and `draft` gives no note.

> **tasks:**
> - [ ] create `estimate-prespec-notes-a-page-the-cascade-archives`
>   - ref: `rule-prespec`
>   - kind: `QA`
>   - purpose: `Whether guppi prespec --check prints a note, without blocking, for an update of a page that the cascade of generate archives once the items of the plan apply, whether the item that sets off the archive stands in another Case or in the same one`
>   - method: `uv run pytest tests/test_prespec.py -k cascade`
>   - tags: `[session, workflow, harness]`
> - [ ] `guppi/generate.py`: the pages the cascade archives — the clustered lessons of an `actioned` Insight, an `open` Insight with no live child, a superseded Decision page — judged by one function, which `cascade` calls; its docstring says so; `make style` passes.
> - [ ] `guppi/prespec.py`: one function of the cascade notes, which imports the function of `guppi/generate.py` and applies the plan's items and the `{supersedes:case N}` marks of the window before it; `plan_findings` adds its notes; the module docstring, as the patch of Case 738 leaves it, names them under Notes; this task runs after the code tasks of Case 738; `make style` passes.
> - [ ] `tests/test_prespec.py`: tests with `cascade` in their names: an `actioned` Insight and an `update` of its clustered lesson under another Case give one note and exit 0; the same under one Case and under two sub-cases of one Case give the note; an `open` Insight left with no live child and a superseded Decision page give the note; a `create`, `delete` or `defer` of such a page and a move between `built` and `draft` give none.
> - [ ] `tests/test_generate.py`: runs green, every answer of `cascade` unchanged.
> - [ ] read `estimate-prespec-notes-a-page-the-cascade-archives`

> **ratification:**
> ```
> - decision[case 739.1][create][estimate-prespec-notes-a-page-the-cascade-archives]{ref:rule-prespec}{tags:session,workflow,harness}
> ```

### Case 739.2 — The check of a Case file notes a page the cascade archives

> **given:**
> `estimate-case-check-notes-a-page-the-cascade-archives`: the new check of the note.
> **＋** `rule-case-check`: the rule of the check of the file of a Case; its Purpose gains one sentence.
> **＋** `guppi/casecheck.py`: `check_answer` and its module docstring, which gain the note.
> **＋** `guppi/prespec.py`: the function of the cascade notes, imported.
> **＋** `tests/test_casecheck.py`: the unit tests of the note.
> **＋** `tests/test_case_schema.py`: runs the check over the example of `vault/wiki/case-example.md` and fails on any note.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the session's ledger, whose `{supersedes:case N}` marks the check reads.
> **＋** `estimate-prespec-notes-a-page-the-cascade-archives`: the promise of the judgment that this check imports.

> **when:**
> `SubagentStop` fires when `case-guppi` writes a file of Cases, and `uv run guppi casecheck --subagent` reads the Cases of the file, the plan file of the session, `<plan>.checked.json` beside it and the session's `raw/<date>/<hi HHMM>/ledger.md`.
> **＋** Or `tests/test_casecheck.py` runs it over a made-up file, plan file, store and ledger.

> **then:**
> The hook judges the Cases of the file with the other Cases of the session, as `other_blocks` of `guppi/casecheck.py` gives them, by the function of `guppi/prespec.py` that prints the cascade notes of pre-spec, imported, not copied.
> **＋** Which pages, items and Cases give a note is what `estimate-prespec-notes-a-page-the-cascade-archives` sets for that function; this check adds only who gets the note and how.
> **＋** The note goes to `case-guppi` under the Case of the file it names, and asks it to drop the change or to give the reason in `context`.
> **＋** The note is sent back once by exit 2 beside any findings, stored under `notes` in `<plan>.checked.json`, and not sent again for the same Case id.
> **－** The note is no finding: the Case is stored with no finding for it, and the `Stop` check of `guppi casecheck` refuses no showing for it.
> **－** Two other Cases of the session give the file no note.

> **tasks:**
> - [ ] create `estimate-case-check-notes-a-page-the-cascade-archives`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the check of the file of a Case sends case-guppi a note once for an update of a page that the cascade of generate archives after an item of the file or of another Case of the session, by the judgment pre-spec prints`
>   - method: `uv run pytest tests/test_casecheck.py -k cascade`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `rule-case-check`
>   - old: `so the two new texts are read side by side before the person sees the Case (case 711.2).`
>   - new: `` so the two new texts are read side by side before the person sees the Case (case 711.2). It sends `case-guppi` a note once, too, for each `update` of a page that the cascade of `guppi/generate.py` archives after an item of the same file or of another Case of the session — a lesson of an Insight set `actioned`, an `open` Insight left with no live child, the Decision page of a superseded Case — by the judgment that `/pre-spec` prints as a `note:` line, so that the Case drops the update or its `context` says why it stands (case 739.2). ``
>   - change: `the check of the file of a Case notes an update of a page that the cascade archives (case 739.2)`
> - [ ] `guppi/casecheck.py`: `check_answer` adds the cascade notes of `guppi/prespec.py` for the Cases of the file, the other Cases of the session first; the module docstring names them beside the notes of `promise_notes`; `make style` passes.
> - [ ] `tests/test_casecheck.py`: tests with `cascade` in their names: an update in the file of a lesson that another stored Case archives, an item of the file that archives a page another Case updates, and both inside the file give one note sent once; two other Cases give the file none; a `create`, `delete` or `defer` gives none.
> - [ ] `tests/test_case_schema.py`: runs green over the example of `vault/wiki/case-example.md`.
> - [ ] read `estimate-case-check-notes-a-page-the-cascade-archives`

> **ratification:**
> ```
> - decision[case 739.2][create][estimate-case-check-notes-a-page-the-cascade-archives]{ref:rule-case-check}{tags:hooks,harness,workflow}
> - decision[case 739.2][update][rule-case-check]{ref:rule-case-check}
> ```
