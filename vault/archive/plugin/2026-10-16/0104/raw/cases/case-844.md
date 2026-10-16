## Case 844 — The tests of the clean version are read after a version tag

> **context:**
> `estimate-clean-branch-ships-the-tests` checks that `guppi ship` writes the tests of GUPPI into the clean version, cleans only their comments and docstrings, and that they pass there. The first part of its `method`, `pytest .guppi/tests/test_ship.py -k tests`, ran inside `guppi test`. The brief of the librarian of session 1959 (`vault/wiki/brief.md`, Readings due) reports that `guppi test` ran `.guppi/tests/test_ship.py` with no failure, with its `live` test deselected, and that this run ran no `guppi ship`. The part by hand builds the clean version with `guppi ship --allow-draft` into an empty folder and runs `pytest .guppi/tests` there. No reading of that part was ever taken. That build cannot run today. `run` of `.guppi/guppi/ship.py` takes the version from `version`, which lists the tags `prod-*` merged into HEAD and matches them with `VERSION_TAG`. With no tag `prod-x.y.z`, it prints `ship: no tag prod-x.y.z in the history of HEAD; nothing written`. `rule-clean-branch` states the same in its Purpose. The `method` of the Estimate does not say this. It waits only for the librarian's run of its change, which has already run, so the page looked ready to read. The brief therefore proposed to defer it into `backlog.md`.
>
> The person chose to take the reading in this session instead, in one batch with the other items that wait for a version tag. Case 841 of this session owns the task that sets that tag. The rule that governs the change is the one `case-schema.md` and `rule-retro` set for a `method`: a part that opens with `by hand, after` names its event before a colon. Retro leaves the Estimate `pending` until that event comes, and reads it in the session in which the event came (case 781). So the `method` names the tag as its event. A `method` change alone would leave the page unread by the Retro of this session, since `rule-retro` does not read an Estimate whose `update` names one part alone. So the Case sets the page `pending` and its Criterion is replaced by the same text, as Case 840.2 did. The Criterion stands as it was, since the behaviour it checks does not change. The ledger hook (`refused_readings` of `.guppi/guppi/ledger.py`) refuses an `estimate` line of a slug that a decision line of this session updates until Retro opens. So the reading is taken at Retro, after the tag task of Case 841, and not in Work Mode. If no tag stands then, the page stays `pending` and is not set `failed`.
>
> The reading builds its own empty temporary folder. It does not share the folder of the plugin install of Case 842, so the `.venv` and the caches that `pytest` writes there never reach a folder that a plugin is installed from. A Grep for `estimate-clean-branch-ships-the-tests` over `vault/wiki/` printed `brief.md`, `log.md`, `rules/rule-clean-branch.md` and `estimates/estimate-clean-branch-writes-a-clean-copy.md`. Over `.claude/` it printed nothing. The rule lists the Estimate in `estimates`. The Criterion of `estimate-clean-branch-writes-a-clean-copy` points to it for what the copy writes of the tests. Both stay true, since the Criterion does not change. `test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it` of `.guppi/tests/test_guppi_package.py` reads the `method` of each live Estimate. The new `method` names `.guppi/tests` and `uv run --project .guppi` as the old one does, so the test finds no hit there. No `create` stands in the Case, so no query of the vault for a free slug was run.

> **problem:**
> The part by hand of the reading of `estimate-clean-branch-ships-the-tests` needs a tag `prod-x.y.z` in the history of HEAD, and none stands. Its `method` waits only for an event that has already come, so the page looks ready to read when it is not, and a Retro would set it `failed` again for the same reason.

> **recommend:**
> - **What does this Case change on the Estimate?**
>   - Recommended: (a) the `method` waits until a tag `prod-x.y.z` stands in the history of HEAD; the Criterion stays and is written back unchanged; the page stays `pending`, and Retro reads it in this session after the tag is set.
>   - Answer: agreed, (a).
> - **Does this reading share its build folder with the plugin-install reading of item C4?**
>   - Recommended: (a) each reading builds its own folder; this one builds into its own empty temporary folder, as its `method` says.
>   - Answer: agreed, (a).

> **given:**
> `estimate-clean-branch-ships-the-tests`: set `pending`, its Criterion kept, its `method` set anew.
> **＋** `rule-clean-branch`: the rule of `guppi ship`, which the Estimate checks.
> **＋** `rule-retro`: the rule of the reading of an Estimate whose `method` waits for an event.
> **＋** `.guppi/guppi/ship.py`: the copy, the judgment of the comments, the docstrings and the samples, and the version from the tag.
> **＋** `.guppi/tests/` and `.guppi/tests/test_ship.py`: the tests of GUPPI, and the tests of the command `ship`.
> **＋** `.guppi/.venv/`: the Python environment that the clean version does not hold.
> **＋** `uv run --project .guppi pytest .guppi/tests`: the run of the tests.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or `uv run --project .guppi guppi ship --check` judges the working tree and writes no folder.
> **＋** Then `uv run --project .guppi pytest .guppi/tests` runs in that folder.

> **then:**
> It writes each file under `.guppi/tests/` but `.guppi/tests/test_ship.py`.
> **＋** In a Python file under `.guppi/tests/`, it removes a bracket that holds a pointer only from the comments and the docstrings, and it judges only them for a pointer outside a bracket and for a bare case number.
> **＋** Each other string of such a file is a sample: a case id there, such as `[case 10]` or `(case 320)` in the data of a test, is neither removed nor judged.
> **＋** `--check` judges each file under `.guppi/tests/` in place, in the same way.
> **＋** In the clean version, `uv run --project .guppi pytest .guppi/tests` passes, and a test that needs a file or a module that the clean version does not hold is skipped.
> **－** The Python environment `.guppi/.venv/` stays out of the copy.
> **－** In a Python file outside `.guppi/tests/`, it judges the whole text as before.

> **tasks:**
> - [ ] update `estimate-clean-branch-ships-the-tests`
>   - set:
>     ```
>     status: pending
>     method: "uv run --project .guppi pytest .guppi/tests/test_ship.py -k tests; by hand, after a tag prod-x.y.z stands in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder of its own, then uv run --project .guppi pytest .guppi/tests in that folder, read against the Criterion"
>     ```
>   - change: `the method waits for a tag prod-x.y.z in the history of HEAD, which guppi ship needs; the Criterion stands`
> - [ ] read `estimate-clean-branch-ships-the-tests`

> **ratification:**
> ```
> - decision[case 844][update][estimate-clean-branch-ships-the-tests]{ref:rule-clean-branch}
> ```
