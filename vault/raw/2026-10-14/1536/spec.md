<!-- approved 17:43:18 · session f5b00c55 -->

# Session 1536 — sprint plugin

## Case 813 — The main agent runs guppi caseid only for a new Case

> **context:**
> `uv run guppi caseid --next --session <stamp>` has one mode: each run prints the next free id and holds it in `<plan>.checked.json`, so the next run gets the id after it. In session 0232 a Case was built again under a number of its own, and the main agent ran the command to check that the number was held; that run held 813, which no Case used (`lesson-caseid-run-to-check-an-id-held-a-new-one`, handoff of session 0232). The check was never needed: the guard `guppi ratified --guard` of `guppi/ratified.py` holds the number at the first call of a `case-guppi` on its case file (docstring of `guppi/casecheck.py`, case 650.1). `rule-orchestration` says when the main agent runs the command, before the dispatch of a new top-level Case, but not that it runs it for nothing else. The person chose one sentence in that Render and no new mode of the command, so `guppi/caseid.py` and its tests do not change. The rule that governs the change is `rule-orchestration` itself; no rule forbids it. `estimate-ratification-case-id-carries-the-sprint` already promises when the main agent runs the command, so its Criterion is replaced whole: every line it holds is kept, one `－` line is added, and its `purpose` and `method` are set anew, since the `purpose` names the use of the main agent and the `method` named a new Render of `rule-ratification`, which this Case does not change. A Grep `caseid` over `vault/wiki/` (Decision pages left out) printed 13 files: `brief.md`, `log.md`, `orchestration.md`, `ratification.md`, `rules/rule-orchestration.md`, `rules/rule-ratification.md`, `lessons/lesson-caseid-run-to-check-an-id-held-a-new-one.md`, `insights/insight-caseid-printed-an-id-it-did-not-hold.md`, `estimates/estimate-ratification-case-id-carries-the-sprint.md`, `estimates/estimate-orchestration-shows-the-built-case.md`, `estimates/estimate-case-check-sends-back-a-case-number-held-by-another-agent.md`, `estimates/estimate-case-check-sends-back-a-ratified-case-in-another-shape.md` and `estimates/estimate-spec-box-refuses-a-stale-spec.md`; the same Grep over `.claude/` printed nothing. None of them is made false: `ratification.md` says what the command does, which stands; the Criterion of `estimate-orchestration-shows-the-built-case` names the command for the Work Mode dispatch of a new top-level Case, which the new sentence keeps; the two `case-check` Estimates speak of the count and of an id the command holds; `estimate-spec-box-refuses-a-stale-spec` names `guppi/caseid.py` as a reader of ids; the Insight speaks of a run with no plan file. `tests/test_orchestration.py` reads the live `orchestration.md`, but only its blocks tagged `showing` and `defer` by `example`, and the new sentence stands outside them. The decision lines carry no `{addresses}` mark: the lesson line stands in the ledger of session 0232, and a lesson whose fix is ratified in another session gets no mark (`ratification.md`).

> **problem:**
> `orchestration.md` does not tell the main agent that each run of `guppi caseid --next` holds a new id, so the agent ran it to check an id and held one that no Case uses.

> **recommend:**
> - **How do we stop a run that only checks from holding an id?**
>   - Recommended: (a) a sentence in `orchestration.md` only: the main agent runs the command only to get the id of a new top-level Case, once for each Case, and never to check an id; no code changes.
>   - Answer: agreed, (a).
> - **Which Estimate checks the fix?**
>   - Recommended: (a) replace the Criterion of `estimate-ratification-case-id-carries-the-sprint` with one more line, read at the Retro of this session against the new Render of `orchestration.md`.
>   - Answer: agreed, (a).

> **given:**
> `rule-orchestration`: its Render, `vault/wiki/orchestration.md`, sets when the main agent runs the command.
> **＋** `guppi/caseid.py`: the command `guppi caseid --next`, which this Case does not change.
> **＋** `<plan>.checked.json`: the store of the ids the command and the guard hold.
> **＋** `guppi/ratified.py`: the guard that holds the number of a case file at the first call of its `case-guppi`.
> **＋** `estimate-ratification-case-id-carries-the-sprint`: its Criterion is replaced whole.

> **when:**
> The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, needs a Case id: for a new top-level Case, or to check the number of a Case built again.

> **then:**
> The main agent runs `uv run guppi caseid --next --session <stamp>` of `guppi/caseid.py` only to get the id of a new top-level Case, once for each Case.
> **＋** `vault/wiki/orchestration.md` says that each run of the command holds a new id.
> **－** The main agent never runs the command to check an id or what `<plan>.checked.json` holds.
> **－** A number that `case-guppi` takes for a Case built again is held by the guard of `guppi/ratified.py`, with no run of the command.

```then
update:
- slug: rule-orchestration
  replace:
  - old: since the command prints no id without that file.
    new: since the command prints no id without that file. The main agent runs the command only to get the id of a new top-level Case, once for each Case, and never to check an id or what the store holds, since each run holds a new id; a number that `case-guppi` takes for a Case built again is held by the guard of its case file (as set in case 813).
  change: the main agent runs guppi caseid --next only for the id of a new top-level Case, never to check an id
- slug: estimate-ratification-case-id-carries-the-sprint
  set:
    status: pending
    purpose: Whether every reader of a Case id takes an id that carries its sprint and a plain id from before sprint ids alike, and guppi caseid --next --session <stamp> prints and holds the next id of the open sprint, which the main agent runs only for the id of a new top-level Case and never to check an id, and prints no id without --session or without the plan file of the session
    method: 'uv run pytest tests/test_caseid.py; by hand at the Retro of this session: the new Render of rule-orchestration in raw/<date>/<hi HHMM>/spec.md, and the Render of rule-ratification, read against the Criterion'
  sections:
    Criterion: |-
      When:
      `guppi/casecheck.py`, `guppi/ratified.py`, `guppi/lint.py`, `guppi/gate.py` or `guppi/materialize.py` reads a Case id in a ledger line, a heading of a Case file, a file name `case-<id>.md` or an `origin`.
      **＋** The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, runs `uv run guppi caseid --next --session <stamp>`, `<stamp>` the stamp of the `hi:` line of its session, before it dispatches a new top-level Case.
      **＋** Or `uv run guppi caseid --next` runs without `--session`, or with a stamp whose session has no plan file.

      Then:
      A Case id of a sprint opened after case 788.2 is the sprint id, a hyphen and the number of the Case in that sprint, from 1, with a dot for each sub-case level, such as `kir-plugin-12.1`, and its Case file is `case-<id>.md` of its top-level Case.
      **＋** The readers read a Case id through `guppi/caseid.py`, which takes both forms and reads the sprint id as the text before the last hyphen ahead of the number.
      **＋** The sprints `migration` and `plugin`, opened before case 788.2, keep plain ids to their close, by a fixed list in `guppi/caseid.py`.
      **＋** The main agent creates the plan file of its session with its title line before its first run of the command.
      **＋** `uv run guppi caseid --next --session <stamp>` takes the open sprint from the `create` decision line of a sprint page in `raw/<date>/<hi HHMM>/ledger.md` of the session of that stamp, else from the first heading of `vault/wiki/sprint.md`, and prints the next id of that sprint.
      **＋** It holds the id it prints in `<plan>.checked.json` of the plan file of that session, under that id, with no `agent_id` and no text, so that the next run prints the id after it.
      **＋** The main agent dispatches each new top-level Case with the id that the command printed, but the opening Case of a sprint, whose id `/sprint-open` sets.
      **－** The main agent runs the command only to get the id of a new top-level Case, once for each Case, and never to check an id or what the store holds, since each run holds a new id.
      **－** Without `--session` the command prints no id: it prints its usage error and exits 2.
      **－** With a stamp whose session has no plan file, the command prints no id, holds nothing, prints one line on stderr and exits 1.
      **－** An id with no sprint part, such as `785.1`, stays a Case from before sprint ids, and no page, file or citation is renamed.
  change: the Criterion replaced whole — the main agent runs guppi caseid --next only for the id of a new top-level Case, never to check an id
```

```tasks
- [ ] update `rule-orchestration`
- [ ] update `estimate-ratification-case-id-carries-the-sprint`
- [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-ratification-case-id-carries-the-sprint`
```

## Case 815 — guppi ship cleans the prose around the example Case

> **context:**
> `guppi ship` builds the clean version of the project and removes from it each bracket that holds a pointer to a case. It makes two exceptions for the example Case: `judged` in `guppi/ship.py` returns the file `EXAMPLE_FILE`, `vault/wiki/case-example.md`, as it stands, and `masked` sets aside every line between the markers of the Render of `EXAMPLE`, `rule-case-example`. Both exist so that the case ids of the example Case are not read as pointers. The example Case stands in a fenced block tagged `case`, though, and `masked` sets aside each line of a fenced block in any Markdown file; the example `then` block is fenced too. So the exceptions only keep the prose around the examples from being judged. The run of the tag `prod-1` showed it: in this session the main agent read `vault/wiki/case-example.md` lines 3 and 7 and `vault/wiki/rules/rule-case-example.md` lines 27 and 31 on `origin/prod`, which still hold `(case 717.1)` and `(case 646)`, and wrote the reading of `estimate-sprint-plugin-ci-writes-a-clean-branch` `failed` in this session's ledger. The lesson `lesson-ship-example-file-exempt-whole-left-case-pointers` names that cause, and the decision line on `rule-clean-branch` carries its `addresses` mark. The person chose to drop both exceptions, so that only the fenced blocks are set aside as in any other page, and to read the CI again in this session, after the owner pushes `plugin` and a tag `prod-2`. The case-guppi read the prose of both texts outside their fences: each pointer there stands in a bracket of its own at the end of its sentence, and no other text there matches a pointer, so `guppi ship` will remove those brackets and exit 0 on them. The two sentences that state the exemption are the docstrings of `guppi/ship.py` and the sentence of the Purpose of `rule-clean-branch` that lists what is no pointer; the Case rewords both. The fourth `－` line of the Criterion of `estimate-clean-branch-writes-a-clean-copy`, on a case id inside a fenced block, names the two exempt texts, so the Case replaces that Criterion whole: that line alone changes, and every other line is carried as it stands, so `then` keeps the nine `＋` lines of the Criterion it replaces. Its `purpose` and `method` do not state the exemption and stand. The other two Estimates of `rule-clean-branch` speak of the pointers in the source texts, which this Case does not change, and stand. The Criterion of `estimate-sprint-plugin-ci-writes-a-clean-branch` already promises that no text of the clean version holds a reference to a case, so it stands, and the main agent reads it again after the new run. A Grep `EXAMPLE|masked\(|case-example|rule-case-example` over `guppi/` printed only `guppi/ship.py`; `guppi/prespec.py` judges a pointer by `outside` of `guppi/ship.py`, which calls `masked`, so `/pre-spec` will judge the prose of a new Render of `rule-case-example` the same way, and the sentence of `rule-clean-branch` on `/pre-spec` stays true. A Grep `rule-clean-branch|estimate-clean-branch-writes-a-clean-copy|estimate-sprint-plugin-ci` over `tests/` printed only `tests/test_ship.py`, which builds its tree in a temporary folder; no test reads a page this Case changes live. A Grep `import .*\bship\b|guppi\.ship|prespec\.(outside|pointer)` over `tests/` printed `tests/test_ship.py` and `tests/test_prespec.py`; `tests/test_prespec.py` holds no read of the live tree, and of `tests/test_ship.py` only `test_a_sample_is_no_pointer` expects the old copy of `case-example.md`. The Case closes the item of the milestone The clean branch on `entity-sprint-plugin`, so it rewrites what remains there, as `uv run guppi prespec --check` asked: the fix of this Case, then the push of `plugin` and a tag `prod-2`, and the reading of the run by its Estimate. The brief reports `make test`: 1619 passed, 6 skipped, and `make lint`: 0 lines, exit 0, at the last close.

> **problem:**
> `guppi ship` never judges or cleans the prose around the example Case, so the pointers there reach the branch `prod`.

> **recommend:**
> - **How the prose around the example Case gets cleaned**
>   - Recommended: (a) drop both exceptions; the example Case and the example `then` block stay aside as fenced blocks, and the brackets in the prose are removed from the copy.
>   - Answer: agreed, (a).
> - **When the CI run is read again**
>   - Recommended: (a) in this session, after Work Mode commits the fix: the owner pushes `plugin` and a tag `prod-2`, and the main agent reads the run against the unchanged Criterion.
>   - Answer: agreed, (a).

> **given:**
> `guppi/ship.py`: the command that builds the clean version, and its exceptions for the example Case.
> **＋** `tests/test_ship.py`: the tests of `guppi ship` over a sample tree.
> **＋** `rule-clean-branch`: the rule of the clean version, whose Purpose lists what is no pointer.
> **＋** `estimate-clean-branch-writes-a-clean-copy`: its Criterion is replaced whole.
> **＋** `vault/wiki/case-example.md`: the file of the examples, rendered from `rule-case-example`.
> **＋** `rule-case-example`: the rule whose Render is the examples.
> **＋** `estimate-sprint-plugin-ci-writes-a-clean-branch`: the reading of the CI run that the new tag starts.
> **＋** `.claude/`, `vault/wiki/tags.md`, `vault/raw/`, `vault/archive/` and `.github/`: the folders and files the clean version takes or leaves out.
> **＋** `decision-case-N`: the form of the id of a Decision page, one form of a pointer.
> **＋** `entity-sprint-plugin`: the sprint page, whose milestone The clean branch says what remains.

> **when:**
> `uv run guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or `uv run guppi ship --review <folder>` does the same.
> **＋** Or `uv run guppi ship --check` judges the working tree and writes no folder.

> **then:**
> It writes `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page under `vault/wiki/` with `core: true`, and each file rendered from such a page.
> **＋** In each file it writes, it removes whole each bracket that holds a pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — with every word in it and the space before it, and each `[[decision-case-N]]` link; a bracket that holds no pointer stays as it is.
> **＋** It writes each other `[[…]]` link of a Markdown file to a page or a file it does not write as the slug in a code span.
> **＋** Each page it writes carries `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line that says the page shipped with GUPPI, and its link fields keep only the pages it writes.
> **＋** It exits 1, and prints the file and the line, for each pointer that stands outside such a bracket, each id of a list of sessions included.
> **＋** In a comment or a docstring of a Python file it writes, it exits 1, and prints the file and the line, for each bracket that holds only case numbers, joined by a comma, a semicolon, `and` or a dash, such as `(274.1)` or `(513, 544.7)`.
> **＋** It does the same for each comment or docstring that opens with one or more case numbers joined the same way, followed by a colon, such as `# 169.1:`, `"""75.2:` or `# 387.4, 445.4:`, and for each comment whose whole text is one or more case numbers joined the same way, such as `# 786` or `# 387.4, 445.4`.
> **＋** It exits 1 when a file it writes holds a section between the markers of a page without `core: true`.
> **＋** With `--review` it also prints the file, the line and the bracket for each bracket it removes that holds words beside its pointers, and those lines set no exit code.
> **＋** With `--check` it judges each file it would write outside `vault/` — `guppi/`, `.claude/` and the files at the root of the project — but `uv.lock`, which it does not clean, as it would write it, prints the same lines for it, exits 1 on any, and writes nothing.
> **－** It writes no page without `core: true`, nothing of `vault/raw/`, `vault/archive/` or `.github/`, and no `sprint.md`, `backlog.md`, `brief.md`, `log.md` or `guppi.toml`.
> **－** It writes no file that a page without `core: true` renders in full.
> **－** A case id inside a code span of a Markdown file, or after `[case ` or `#case-`, is the form of a line, not a reference.
> **－** A case id inside a fenced block of a Markdown file, inside a code span of the text of a `schema.yaml`, or after `:case `, is the form of a sample or of a line: it is neither removed nor printed; in `vault/wiki/case-example.md` and the Render of `rule-case-example` only the fenced blocks, the example Case among them, are set aside so, and the text around them is judged and cleaned like the text of any other page.
> **－** It removes no bare case number: the copy holds it as written.
> **－** It judges no code of a Python file outside its comments and docstrings for a bare case number, such as `match.group(1)`, and a number or a list of numbers that opens a comment with words and no colon after it, such as `# 3, 4 tries`, is no finding.

```then
update:
- slug: rule-clean-branch
  replace:
  - old: A case id in a code span or a fenced block, of a Markdown file or of the text of a `schema.yaml`, in `case-example.md` or the Render of `rule-case-example`, or in the form of a line after `[case `, `#case-` or `:case `, is no pointer.
    new: A case id in a code span or a fenced block, of a Markdown file or of the text of a `schema.yaml`, or in the form of a line after `[case `, `#case-` or `:case `, is no pointer; the example Case of `case-example.md` and of the Render of `rule-case-example` stands in a fenced block, and the text around it is judged and cleaned like the text of any other page.
  change: guppi ship judges and cleans the text around the example Case; only its fenced blocks are set aside
- slug: estimate-clean-branch-writes-a-clean-copy
  set:
    status: pending
  change: the Criterion replaced whole — case-example.md and the Render of rule-case-example are cleaned outside their fenced blocks
- slug: entity-sprint-plugin
  replace:
  - old: 'what remains: once the librarian''s run applies the rewording of the pages (case 809), the owner pushes a tag `prod-*` on a commit of `plugin`, and the CI run it starts is read by its Estimate'
    new: 'what remains: once Work Mode commits the fix of `guppi ship` that cleans the text around the example Case (case 815), the owner pushes `plugin` and a tag `prod-2` on its last commit, and the CI run it starts is read by its Estimate'
  change: the milestone The clean branch says what remains after the fix of guppi ship for the example Case
```

```tasks
- [ ] update `rule-clean-branch`
- [ ] update `estimate-clean-branch-writes-a-clean-copy`
- [ ] update `entity-sprint-plugin`
- [ ] `uv run guppi sprint`
- [x] `guppi/ship.py`: remove `EXAMPLE` and `EXAMPLE_FILE`, the branch of `masked` that sets aside the lines of the Render of `EXAMPLE`, and the exception of `judged` for `EXAMPLE_FILE`; reword the module docstring and the docstrings of `masked` and `judged` so that they name no exception for the example.
- [x] `tests/test_ship.py`: `test_a_sample_is_no_pointer` puts the example Case of its `case-example.md` and of the Render of its `rule-case-example` in a fenced block, and asserts that the case id in the fence stays and that the bracket `(case 717.1)` in the prose is removed in both; a new test asserts that a pointer outside a bracket in the prose of `case-example.md` exits 1 and prints its file and line.
- [x] `uv run pytest tests/test_ship.py`
- [ ] read `estimate-clean-branch-writes-a-clean-copy`
- [x] stop: after the commit of Work Mode, the owner pushes `plugin` and a tag `prod-2` on its last commit; the main agent reads the CI run that the tag starts, its push and the branch `prod` against the Criterion of `estimate-sprint-plugin-ci-writes-a-clean-branch` and writes its `estimate` line.
```
