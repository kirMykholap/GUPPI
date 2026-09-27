## Case 462 — One reader of the sections of a Case, in `guppi/materialize.py`

> **context:**
> Two functions read the `> **name:**` blockquotes of a Case into name → text: `case_text` in `guppi/materialize.py` and `quoted_sections` in `guppi/ratified.py`. They are the same walk, line for line. The only difference is the set of names: `case_text` fixes the seven sections, and `quoted_sections` takes the names as an argument. Both judge a fence by `fence_opening` and `closes_fence` of `materialize`. `materialize` uses its copy through `case_texts`, which `prespec` also calls. `ratified` and `casecheck` use the other copy. A fix to one walk does not reach the other, and the test in `tests/test_materialize.py` that runs both over one text catches a difference only for the input it holds. `CLAUDE.md` calls such a second copy a defect. Case 455 deferred the item onto `rule-one-judgment-one-implementation`.
> The reader cannot live in `ratified`, because `ratified` imports `materialize` and the reverse import would be a cycle. It cannot live in `guppi/pages.py`, because `materialize` imports `pages` and the fence functions live in `materialize`. The person chose that `materialize` keeps one function, `quoted_sections(lines, names)`; that `case_text` goes; and that `ratified` and `casecheck` import the function from `materialize`, with no re-export.
> The frame has one contradiction. The `When` of `estimate-materialize-judges-a-fence` lists `case_text` of `guppi/materialize.py` and `quoted_sections` of `guppi/ratified.py` among the readers of a fence, and the change makes that false. A Criterion changes only whole, so this Case replaces it whole with the list corrected. The person chose not to add a separate promise for the one reader. The guard against a second copy stays what `rule-one-judgment-one-implementation` has: its text in `CLAUDE.md` and the by-hand reading of the diff in `estimate-one-judgment-one-implementation-followed`. That Estimate is not touched, because the change makes its Criterion true and makes none of it false. The Render of the rule does not change either.
> `estimate-materialize-assembles` speaks of the `case_text` key of the yaml record, not the function. The key keeps its name, so that Estimate stands. The page of `rule-materialize` does not name either function. The fence paragraph of the `materialize.py` docstring names `quoted_sections` of `guppi/ratified.py`, and Work Mode corrects it. The `given` names `guppi/prespec.py` and `guppi/ledger.py` only because the Criterion lists their readers, so it holds eight `＋` lines.
> The decision line carries `{supersedes:case 455}`, so `generate` clears the defer from `rule-one-judgment-one-implementation`. Two things are not done here. The Case does not sweep `guppi/` for other duplicate judgments: a grep for `SECTION_START` and `QUOTE.match` found no third section reader. Case 460.3 takes the `PREFIXES` pair in `lint`.

> **problem:**
> One judgment, how the sections of a Case are read, lives in two functions in two modules. The two can drift apart while the tests still pass. The fence Estimate names both functions as separate readers, so it would be false once they merge.

> **recommend:**
> Keep one function, `quoted_sections(lines, names)`, in `guppi/materialize.py`, next to the fence judgment it uses. Remove `case_text`, and let `case_texts` call `quoted_sections` with the seven section names. `ratified` and `casecheck` import it from `materialize`. Replace the Criterion of `estimate-materialize-judges-a-fence` whole, so that its list of readers names the one function once. A thin `case_text` wrapper was rejected: it would be a second name for one judgment.

> **given:**
> `estimate-materialize-judges-a-fence` — the promise that every reader of a fence judges it by the functions of `guppi/materialize.py`.
> **＋** `guppi/materialize.py` — the fence functions, `case_text`, `case_texts` and the docstring that lists the readers of a fence.
> **＋** `guppi/ratified.py` — `quoted_sections`, the second copy of the section reader, and its callers.
> **＋** `guppi/casecheck.py` — imports `quoted_sections` from `guppi/ratified.py`; its check of `ratification` reads a fence.
> **＋** `guppi/prespec.py` — `plan_prose`, a reader of a fence the Criterion lists.
> **＋** `guppi/ledger.py` — `ledger_lines`, a reader of a fence the Criterion lists.
> **＋** `tests/test_materialize.py` — the fence test that runs `case_text` and `ratified.quoted_sections` over one text.
> **＋** `tests/test_ratified.py` — the tests that call `ratified.quoted_sections`.
> **＋** `rule-one-judgment-one-implementation` — the rule that calls a second copy of one judgment a defect.

> **when:**
> A hook or a script reads a text that holds a fence: `then_blocks`, `tagged_blocks`, `quoted_sections` and `criterion_text` of `guppi/materialize.py`, `fenced_value` of `guppi/ratified.py`, `plan_prose` of `guppi/prespec.py`, the check of `ratification` in `guppi/casecheck.py`, or `ledger_lines` of `guppi/ledger.py`.

> **then:**
> A line opens a fence when, after at most three spaces of indent inside the block it stands in (a quote, a sub-point of `tasks`), it starts with a run of three or more backticks or three or more tildes.
> **＋** The fence closes only on a line of the same character whose run is at least as long as the opening run, with nothing after the run but spaces.
> **＋** A line with a shorter run, a run of the other character, or a word after its run stays inside the fence as content.
> **＋** A fenced value under a sub-point of `tasks` that holds a shorter fence of the same character is read whole, together with the inner fence.
> **＋** Every one of these readers takes the judgment from the functions of `guppi/materialize.py`, and they all give the same answer for the same text.
> **－** No reader keeps a fence pattern of its own: the `FENCE` of `guppi/ledger.py`, the `OPEN_FENCE` of `guppi/ratified.py`, and the tests on three backticks in `guppi/ratified.py` and `guppi/casecheck.py` are removed.

> **tasks:**
> - [ ] update `estimate-materialize-judges-a-fence`: the Criterion replaced whole
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — quoted_sections of guppi/materialize.py is the one reader of the sections of a Case; case_text and the copy in guppi/ratified.py removed (case 462)`
> - [ ] `guppi/materialize.py`: move `quoted_sections(lines, names)` here from `guppi/ratified.py`; remove `case_text`; `case_texts` calls `quoted_sections(lines, CASE_SECTIONS)`; the fence paragraph of the docstring names `quoted_sections` among the readers of this module and no longer under `guppi/ratified.py`
> - [ ] `guppi/ratified.py`: remove `quoted_sections` and import it from `guppi/materialize.py`, with no re-export
> - [ ] `guppi/casecheck.py`: import `quoted_sections` from `guppi/materialize.py`
> - [ ] `tests/test_materialize.py`: the fence test asserts `materialize.quoted_sections` once; the calls of `case_text` and `ratified.quoted_sections` are removed
> - [ ] `tests/test_ratified.py`: the calls of `ratified.quoted_sections` become calls of `materialize.quoted_sections`
> - [ ] `uv run pytest`: the whole suite passes
> - [ ] read `estimate-materialize-judges-a-fence`: `uv run pytest tests/test_materialize.py -k fence` in a later session

> **ratification:**
> ```
> - decision[case 462][update][estimate-materialize-judges-a-fence]{ref:estimate-materialize-judges-a-fence}{supersedes:case 455}
> ```
