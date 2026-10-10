## Case 770 — Cleanup files a page under the sprint of the session of its run

> **context:**
> At the librarian's run `guppi cleanup` moves each live page with `status: archived` to `vault/archive/<sprint>/<date>/<HHMM>/<category>/`, and takes `<sprint>` from the first `## <id>` heading of `vault/wiki/sprint.md` by `sprint_id` of `guppi/materialize.py`. The librarian runs cleanup at step 3 and `guppi sprint`, which rewrites `sprint.md`, only at step 5. So in the session that opens a sprint, `sprint.md` still names the closed sprint when cleanup runs. In session 1713, which opened `plugin`, cleanup moved `decision-case-757` and `decision-case-759` to `vault/archive/migration/2026-10-10/1713/decisions/`, while the `materialize.yaml` of 1713 holds `sprint: plugin`, which `guppi materialize` sets in a unit whose ledger creates `entity-sprint-<id>` (case 628.3). `guppi archive` had the same fault for the folders of `raw/` and takes the `sprint` field of the unit's own yaml since case 743.2, by `unit_sprint` of `guppi/archive.py`. The person chose the same source for cleanup, one shared function for the judgment, the move of the two pages in Work Mode, and a new Estimate. A Grep `` sprint_id|unit_sprint|\.sprint\b|"sprint" `` over `guppi/` printed `cli.py`, `cleanup.py`, `backlog.py`, `archive.py`, `generate.py`, `materialize.py`, `sprint_close.py`, `sprint.py` and `prespec.py`; the same judgment, the `sprint` field of a unit's yaml and else `sprint_id`, stands in `unit_sprint` of `archive.py` and inline in `generate_date` of `generate.py`, so the task moves it into one function of `materialize.py` that all three import, and adds no second copy. A Grep `` first `## <id>` heading|first heading of `?(vault/wiki/)?sprint\.md|sprint_id|heading of sprint\.md `` over `vault/wiki/`, `log.md` and `brief.md` left out, printed `rules/rule-sprint.md`, `rules/rule-skill-sprint-open.md`, `rules/rule-raw-archive.md`, `rules/rule-materialize.md`, `estimates/estimate-sprint-marks-a-closed-sprint.md` and `estimates/estimate-raw-archive-files-a-session-by-its-sprint.md`. The sentence of `rule-sprint` that the heading is the id that `cleanup` and `archive` read stays true, since both still read it when the yaml holds no sprint; the other hits speak of `sprint.md` itself, of `materialize` or of `archive`, whose behaviour does not change, and stand. The docstring of `guppi/cleanup.py` says the sprint is the first heading of `sprint.md`; the code task rewrites it. `rule-cleanup` keeps its mechanism in that docstring (case 632.1), and its `## Purpose` names no sprint, so the page needs no `update`; the new Estimate joins its `estimates` by its `ref`. The Criterion of `estimate-cleanup-moves` writes the folder as `<sprint>` and does not say where the name comes from, so it stays true and stands; `estimate-raw-archive-files-a-session-by-its-sprint` checks the move of `guppi archive`, whose behaviour the shared function keeps, and stands, its test run again in `tasks`. The Criterion of `estimate-generate-writes` says a created page's `sprint` is the `sprint` of the yaml, which `guppi materialize` takes from the first heading of `sprint.md` or from the `<id>` of `entity-sprint-<id>`; the shared function strips the field, as `unit_sprint` does and `generate_date` does not today, but `sprint_id` returns its id stripped and `opened_sprint` cuts it from a slug, which holds no space, so for each yaml `guppi materialize` writes the stripped field is the field itself, and that Criterion stays true and stands; `test_a_created_page_takes_the_sprint_of_its_yaml_over_the_heading` of `tests/test_generate.py`, run again in `tasks`, checks that generate still takes the yaml's sprint over the heading. A Grep `guppi cleanup` over `vault/wiki/rules/` and `.claude/` printed `.claude/agents/librarian-guppi.md` and `rules/rule-documentation.md`; both set the order of the steps of the librarian's run, which this Case keeps. Case 769 changes neither the librarian's run nor `guppi cleanup`. A Grep `` parents\[1\]|parent\.parent|ROOT\s*=|REPO\s*=|project_root\(\) `` over `tests/` printed `test_schemas.py`, `test_orchestration.py`, `test_lint.py`, `test_materialize.py`, `test_generate.py` and `test_case_schema.py`; they read live the schemas, the `Makefile`, `orchestration.md`, `case-schema.md` and `case-example.md`, none of which the sprint of a unit reaches, so no live test changes.

> **problem:**
> In the session that opens a sprint, `guppi cleanup` files archived pages under the closed sprint, since it reads `sprint.md` before `guppi sprint` rewrites it.

> **recommend:**
> - **Where does cleanup take the sprint name from?**
>   - Recommended: (a) the session's own record, as `guppi archive` does: the `sprint` field of the `materialize.yaml` of the session of the run, else `sprint.md`, in one function that `guppi archive`, `guppi cleanup` and `guppi generate` import.
>   - Answer: agreed, (a).
> - **What happens to the two pages already filed under `migration`?**
>   - Recommended: (a) move them in Work Mode to `vault/archive/plugin/2026-10-10/1713/decisions/`.
>   - Answer: agreed, (a).
> - **How is the fix checked?**
>   - Recommended: (a) a new check of its own, `estimate-cleanup-files-a-session-by-its-sprint`, by `uv run pytest tests/test_cleanup.py -k sprint`; `estimate-cleanup-moves` stays as it is.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed to the fix of a finding of `/pre-spec`: name `estimate-generate-writes`, whose Criterion says a created page takes the `sprint` of the yaml, and keep it true.
>   - Taken: `given` names it, and `context` says why its Criterion stays true under the shared function.

> **given:**
> `estimate-cleanup-files-a-session-by-its-sprint`: the new check of the sprint folder that cleanup picks.
> **＋** `rule-cleanup`: the rule of `guppi cleanup`, whose mechanism lives in the docstring of `guppi/cleanup.py`.
> **＋** `guppi/cleanup.py`: the move of archived pages.
> **＋** `guppi/materialize.py`: `sprint_id`, and the one function of the sprint of a unit.
> **＋** `guppi/archive.py` and `guppi/generate.py`: the other readers of the sprint of a unit.
> **＋** `estimate-generate-writes`: the check that a created page takes the `sprint` of its yaml, which stands.
> **＋** `tests/test_cleanup.py`, `tests/test_archive.py`, `tests/test_generate.py` and `tests/test_sprint_close.py`: the tests of cleanup and of the other readers.
> **＋** `vault/raw/<date>/<HHMM>/materialize.yaml`: the yaml of the session, with its `sprint` field.
> **＋** `vault/wiki/sprint.md`: the rendered sprint, whose first heading is the fallback.
> **＋** `vault/archive/` and its folder `vault/archive/<sprint>/`: where cleanup files an archived page.

> **when:**
> `uv run guppi cleanup` of `guppi/cleanup.py` moves a live page with `status: archived` under `vault/archive/`, or `tests/test_cleanup.py` runs that move over a made-up vault.

> **then:**
> The page goes under `vault/archive/<sprint>/`, `<sprint>` being the value of the `sprint` field of the `vault/raw/<date>/<HHMM>/materialize.yaml` of the session of the run.
> **＋** A run whose session has no `materialize.yaml`, or whose yaml holds no `sprint` field, or a run with no session folder, takes the first `## <id>` heading of `vault/wiki/sprint.md`, as before.
> **－** The date and session folders under the sprint folder, the History and `log.md` lines and the rest of the move do not change.

> **tasks:**
> - [ ] create `estimate-cleanup-files-a-session-by-its-sprint`
>   - ref: `rule-cleanup`
>   - kind: `QA`
>   - purpose: `Whether guppi cleanup moves an archived page under the sprint that the materialize.yaml of the session of its run records, and under the sprint of sprint.md only when that yaml or its field is missing`
>   - method: `uv run pytest tests/test_cleanup.py -k sprint`
>   - tags: `[harness, librarian, sprint]`
> - [ ] `guppi/materialize.py`: one function gives the sprint of a unit, the `sprint` field of its yaml stripped, else `sprint_id`; `unit_sprint` of `guppi/archive.py` and the inline judgment in `generate_date` of `guppi/generate.py` are replaced by imports of it.
> - [ ] `guppi/cleanup.py`: `run` takes the sprint of the unit `<date>/<HHMM>` that `session_of_run` names, by that function, and `sprint_id` when no session folder exists; the docstring says so.
> - [ ] `tests/test_cleanup.py`: a test whose session yaml holds `sprint: a` while `sprint.md` names `b`, and the page lands under `vault/archive/a/`; a test whose session has no yaml, and the page lands under `b`; both names hold `sprint`.
> - [ ] `uv run pytest tests/test_cleanup.py tests/test_archive.py tests/test_generate.py tests/test_sprint_close.py`
> - [ ] one-off migration: `git mv` `vault/archive/migration/2026-10-10/1713/decisions/decision-case-757.md` and `decision-case-759.md` to `vault/archive/plugin/2026-10-10/1713/decisions/`, and remove the folders left empty.
> - [ ] read `estimate-cleanup-files-a-session-by-its-sprint`

> **ratification:**
> ```
> - decision[case 770][create][estimate-cleanup-files-a-session-by-its-sprint]{ref:rule-cleanup}{tags:harness,librarian,sprint}
> ```
