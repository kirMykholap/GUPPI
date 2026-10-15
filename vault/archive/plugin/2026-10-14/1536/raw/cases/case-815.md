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

> **tasks:**
> - [ ] update `rule-clean-branch`
>   - old:
>     ```
>     A case id in a code span or a fenced block, of a Markdown file or of the text of a `schema.yaml`, in `case-example.md` or the Render of `rule-case-example`, or in the form of a line after `[case `, `#case-` or `:case `, is no pointer.
>     ```
>   - new:
>     ```
>     A case id in a code span or a fenced block, of a Markdown file or of the text of a `schema.yaml`, or in the form of a line after `[case `, `#case-` or `:case `, is no pointer; the example Case of `case-example.md` and of the Render of `rule-case-example` stands in a fenced block, and the text around it is judged and cleaned like the text of any other page.
>     ```
>   - change: `guppi ship judges and cleans the text around the example Case; only its fenced blocks are set aside`
> - [ ] update `estimate-clean-branch-writes-a-clean-copy`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — case-example.md and the Render of rule-case-example are cleaned outside their fenced blocks`
> - [ ] update `entity-sprint-plugin`
>   - old:
>     ```
>     what remains: once the librarian's run applies the rewording of the pages (case 809), the owner pushes a tag `prod-*` on a commit of `plugin`, and the CI run it starts is read by its Estimate
>     ```
>   - new:
>     ```
>     what remains: once Work Mode commits the fix of `guppi ship` that cleans the text around the example Case (case 815), the owner pushes `plugin` and a tag `prod-2` on its last commit, and the CI run it starts is read by its Estimate
>     ```
>   - change: `the milestone The clean branch says what remains after the fix of guppi ship for the example Case`
> - [ ] `uv run guppi sprint`
> - [ ] `guppi/ship.py`: remove `EXAMPLE` and `EXAMPLE_FILE`, the branch of `masked` that sets aside the lines of the Render of `EXAMPLE`, and the exception of `judged` for `EXAMPLE_FILE`; reword the module docstring and the docstrings of `masked` and `judged` so that they name no exception for the example.
> - [ ] `tests/test_ship.py`: `test_a_sample_is_no_pointer` puts the example Case of its `case-example.md` and of the Render of its `rule-case-example` in a fenced block, and asserts that the case id in the fence stays and that the bracket `(case 717.1)` in the prose is removed in both; a new test asserts that a pointer outside a bracket in the prose of `case-example.md` exits 1 and prints its file and line.
> - [ ] `uv run pytest tests/test_ship.py`
> - [ ] read `estimate-clean-branch-writes-a-clean-copy`
> - [ ] stop: after the commit of Work Mode, the owner pushes `plugin` and a tag `prod-2` on its last commit; the main agent reads the CI run that the tag starts, its push and the branch `prod` against the Criterion of `estimate-sprint-plugin-ci-writes-a-clean-branch` and writes its `estimate` line.

> **ratification:**
> ```
> - decision[case 815][update][rule-clean-branch]{ref:rule-clean-branch}{addresses:lesson-ship-example-file-exempt-whole-left-case-pointers}
> - decision[case 815][update][estimate-clean-branch-writes-a-clean-copy]{ref:rule-clean-branch}
> - decision[case 815][update][entity-sprint-plugin]{ref:entity-sprint-plugin}
> ```
