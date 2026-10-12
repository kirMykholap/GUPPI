## Case 776 — A superseded entry lists every Case that retires it

> **context:**
> When a decision line carries `{supersedes:case N}`, `guppi materialize` marks each yaml entry of Case N, and of its sub-cases, with `superseded_by`. `mark_superseded` in `guppi/materialize.py` writes that field as one value, so a second line that retires the same Case overwrites the first. The `decisions` record of the Case keeps a list and appends to it. In session 2350, ledger lines 3 and 5 both carry `{supersedes:case 771}` (cases 775.1 and 775.2). The archived 1913 yaml, `vault/archive/plugin/2026-10-10/1913/raw/materialize.yaml`, therefore holds `superseded_by: '775.2'` on both `defer` entries of case 771, at ledger lines 23 and 24, while its record of 771 lists `decision-case-775.1` and `decision-case-775.2`. A `{supersedes}` mark retires the whole Case, so each of the two Cases retired both entries. With this Case the entry field becomes a list in the order the lines are lifted, as the record already is. An older yaml with one value is read as a list of one, and the next mark appends to that list. The archived 1913 yaml stays as it is, since its record of 771 already names both Cases. A Grep of `superseded_by` over `guppi/` printed five files: `guppi/materialize.py`, `guppi/render.py`, `guppi/generate.py`, `guppi/archive.py` and `guppi/pages.py`. In `render.py`, `archive.py` and `generate.py` the entry field is only tested for presence. `pages.py` names the page field of a Decision page, not the yaml field. So no reader there needs the old form. The same Grep over `.claude/` printed nothing. A Grep of `def as_list|def cases_of` over `guppi/` printed `guppi/materialize.py`, `guppi/lint.py` and `guppi/generate.py`. `cases_of` in `materialize.py` already reads one value or a list for `supersedes`, so the new mark reads the old field through it, and the task adds no second copy of that judgment (`rule-one-judgment-one-implementation`). A Grep of `superseded_by` over `tests/` printed `tests/test_casecheck.py`, `tests/test_render.py`, `tests/test_materialize.py`, `tests/test_lint.py`, `tests/test_archive.py` and `tests/test_generate.py`. Only `tests/test_materialize.py` asserts the entry field equal to one value, so those assertions change. The other files set the field as input that is only tested for presence, name the page field, or hold the word in the name of a test in `tests/test_casecheck.py`. No test reads `rule-materialize` or `estimate-materialize-marks-superseded` live: a Grep of those slugs over `tests/` printed only two comment lines in `tests/test_materialize.py`. In `rule-materialize`, one sentence states the form of the mark: a one-off migration sets `superseded_by` to the number of a Case (case 427). That sentence changes to a list of one. The other sentences that name the mark (case 299.3) state no form, so they stand. `estimate-materialize-marks-superseded` checks the mark, so its Criterion is replaced whole. Its `method` waited for a librarian's run, so it is set anew to the test run alone.

> **problem:**
> The entry-level `superseded_by` of a yaml holds one Case. When two Cases retire the same Case, the yaml names only the last one on every entry. So an entry of `rule-skill-sprint-open` names a Case other than the one that set its page anew.

> **recommend:**
> - **What should the entry's mark hold when two Cases retire the same Case?**
>   - Recommended: (a) a list of every retiring Case, in ledger order; an older yaml with one value read as a list of one; a one-off migration that retires a reading writes a list of one; the tests that compare the field to one value compare it to a list.
>   - Answer: agreed, (a).
> - **Should the archived yaml of the earlier session be corrected?**
>   - Recommended: (a) leave it as it stands; its Decision record of the earlier Case already names both sub-cases.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) replace the Criterion of `estimate-materialize-marks-superseded` whole and set its method anew to the `tests/test_materialize.py` tests of the mark, including a new test where two lines retire one Case, read at the Retro of this session.
>   - Answer: agreed, (a).

> **given:**
> `guppi/materialize.py`: `mark_superseded` writes the mark and `cases_of` reads one value or a list.
> **＋** `tests/test_materialize.py`: the tests of the `{supersedes}` mark.
> **＋** `rule-materialize`: the rule of the yaml, which names the mark of a one-off migration.
> **＋** `estimate-materialize-marks-superseded`: its Criterion is replaced whole and its method set anew.
> **＋** `rule-one-judgment-one-implementation`: the old field is read through `cases_of`, never a second copy.
> **＋** `guppi/ratified.py`: `remove_case` imports `in_family`.
> **＋** `guppi/prespec.py`: imports `in_family`.
> **＋** `guppi/casecheck.py`: its clash check imports `in_family`.

> **when:**
> `uv run guppi materialize` lifts a decision line that carries one `{supersedes:case N}` block or several, and the entries of each Case N, or of its sub-cases, stand in this unit's `materialize.yaml` or in the `materialize.yaml` of another unit.
> **＋** A later decision line lifted in the same run, or in a later run, carries a `{supersedes:case N}` block for the same Case N.

> **then:**
> For each Case N that a block of the line names, every entry with `case: N` gets `superseded_by`, whatever its kind, and the `decisions` record of that Case gets it too.
> **＋** The `superseded_by` of an entry is a list that holds each Case whose line retires the entry, in the order the lines are lifted, with no Case twice.
> **＋** So does every entry and every `decisions` record of a sub-case of Case N at any depth. A block that names Case N.M marks N.M and its own sub-cases, and leaves its parent and its other sub-cases.
> **＋** The entry of the line carries `supersedes` as a list with one Case per block, in the order of the blocks. The `decisions` record of its Case lists under `supersedes` every Case that its lines name.
> **＋** The `materialize.yaml` of another unit is written with that mark only.
> **＋** An entry marked while no heading of its own Case stands in the unit's `spec.md` carries no `incomplete: [then]`, and its `decisions` record no `case_text` and no `incomplete` for a section.
> **＋** Whether a block covers a Case is judged by `in_family` of `guppi/materialize.py`; `remove_case` of `guppi/ratified.py`, `guppi/prespec.py` and `guppi/casecheck.py` import it.
> **－** An entry without `case` — an `estimate` or a `lesson` entry — gets no mark.
> **－** An entry of an existing `materialize.yaml` whose `supersedes` is one value, not a list, is read as a list of one.
> **－** An entry of an existing `materialize.yaml` whose `superseded_by` is one value, not a list, is read as a list of one, and a new mark is appended to that list.

> **tasks:**
> - [ ] `guppi/materialize.py`: `mark_superseded` reads the entry's `superseded_by` through `cases_of` and appends the superseding Case when the list does not hold it; the docstring of `cases_of` names both fields; the module docstring names `superseded_by` of an entry as a list, one value in a yaml written before case 776, and the one-off migration of case 427 as writing a list of one.
> - [ ] `tests/test_materialize.py`: each assertion that compares an entry's `superseded_by` to one value compares it to a list; one new test where two decision lines each carry `{supersedes:case N}` for the same Case, and every entry of that Case lists both Cases in ledger order; one new test where an entry holds one value and a new mark appends to it, and a mark of a Case already listed adds nothing.
> - [ ] update `rule-materialize`
>   - old: `` whose one-off migration sets `superseded_by` to the number of that Case on the entry ``
>   - new: `` whose one-off migration sets `superseded_by` on the entry to a list that holds the number of that Case ``
>   - change: `the superseded_by of an entry is a list, one Case per line that retires it (case 776)`
> - [ ] update `estimate-materialize-marks-superseded`
>   - set:
>     ```
>     status: pending
>     method: pytest in tests/test_materialize.py, the tests of the supersedes mark, a test where two decision lines retire one Case among them
>     ```
>   - change: `the Criterion replaced whole — the superseded_by of an entry lists every Case that retires it; the method is the test run alone (case 776)`
> - [ ] read `estimate-materialize-marks-superseded`

> **ratification:**
> ```
> - decision[case 776][update][rule-materialize]{ref:rule-materialize}
> - decision[case 776][update][estimate-materialize-marks-superseded]{ref:rule-materialize}
> ```
