## Case 464 — The file-route Estimate says what generate does with an unknown category

> **context:**
> `materialize` gives `category: unknown` to the entry of a ledger line whose slug has no category prefix (case 320). `generate` then treats that entry in one of four ways, by its kind. A `create` fails with `category 'unknown' is not a vault folder`. A `defer` with no page fails the same way. An `update` applies to the page of that slug, in whatever folder it is in. A `delete` prints `outside the vault, nothing to archive`, applies and ticks its line (case 48). Case 460.1 relied on the `update` road: it renamed `harness-senduserfile-renders-a-markdown-file-on-the-phone`, and that entry was `category: unknown`.
> The Criterion of `estimate-sprint-migration-file-route-gone` (status `passed`, from case 320) says the entry "lands `category: unknown`, and `generate` reports an error instead of 'applied by hand'". That is true for a `create` and a page-less `defer`. It is false for an `update` and a `delete`. The docstring of `guppi/generate.py` already describes both roads that apply (cases 460.1, 463). In session 1819 the person left the Estimate as it stood (Q7), and the brief flagged the contradiction again.
> The Criterion also keeps the old shape: a `Given:` block, and a `－` line that only bounds the edit ("`rule-morph` is untouched"). Its `method` still reads "at the close of theme 5", and theme 5 is closed. `tests/test_generate.py` covers the unknown-category `delete` (`test_a_delete_outside_the_vault_applies_and_a_delete_of_a_missing_page_fails`, `test_a_delete_of_an_unknown_category_is_outside_the_vault`). No test covers the `update`, the `create` or the page-less `defer` of that category.
> The item is an `update` of an existing page, so no vault query ran. In the frame: the `purpose` of the Estimate and the Purpose of `entity-sprint-migration` stay true. No sentence of `rule-page-generation` speaks of an unknown category outside its History. Of the Estimates of `rule-page-generation`, `estimate-generate-fails-alone` names only failures in general, and the unknown `create` failing agrees with it. `estimate-generate-renames` speaks of the page's own category prefix, which a page found in its folder has. Neither speaks of the unknown category, so both stand. The code does not change.
> In the rounds, the person chose these answers: replace the Criterion so that it describes the code; write it in the current model, with no `Given:`, the input in `When:` and the `rule-morph` line dropped; state all four roads; add tests for the untested roads and set a `method` without theme 5.

> **problem:**
> A `passed` Estimate promises that `generate` reports an error for every entry of unknown category. The code applies the `update` and the `delete` of such an entry, and a ratified Case depends on the `update` applying. The promise and the behaviour disagree, and no test holds three of the four roads.

> **recommend:**
> Replace the Criterion whole with the four roads as the code runs them, in the current model, and set the Estimate `pending` so that a later session reads it again. Add tests to `tests/test_generate.py` for the untested roads, and give the `method` commands that run them. The other way, making `generate` fail every unknown entry, would undo case 48 and close the rename road that 460.1 used.

> **given:**
> `estimate-sprint-migration-file-route-gone` — the promise that the file route is gone
> **＋** `guppi/` — the scripts the file route left
> **＋** `guppi/generate.py` — applies or fails the entry of each kind, and ticks the line of an applied entry
> **＋** `guppi/materialize.py` — `category_of` gives the entry of a slug with no prefix `category: unknown`
> **＋** `guppi/prespec.py` — `check_governed` refuses an `update` item that carries `file`
> **＋** `tests/test_generate.py` — the tests of the unknown-category roads
> **＋** `vault/wiki/sprint.md` — shows the status of the Estimate

> **when:**
> `generate` applies a `materialize.yaml` that holds an entry lifted from a ledger line whose slug has no category prefix.
> **＋** `make test` and `make lint` run on the tree.

> **then:**
> No file under `guppi/` holds `RULE_CLASS`, `rule_class`, `applied by hand` or `prose_names`.
> **＋** An `update` item that carries `file` is a `pre-spec` finding: `check_governed` refuses any such item, not only one on a governed path.
> **＋** The entry of a ledger line whose slug has no category prefix lands `category: unknown`.
> **＋** `generate` fails a `create` of that entry, and a `defer` of it with no page, with `category 'unknown' is not a vault folder`.
> **＋** `generate` applies an `update` of that entry to the page of that slug in any folder, and ticks its line.
> **＋** `generate` applies a `delete` of that entry with the stdout line `outside the vault, nothing to archive`, and ticks its line.
> **＋** `make test` is green, and `make lint` has no finding on a schema.
> **－** `generate` prints "applied by hand" for no entry.

> **tasks:**
> - [ ] update `estimate-sprint-migration-file-route-gone`
>   - set: `{status: pending, method: "rg 'RULE_CLASS|rule_class|applied by hand|prose_names' guppi/ empty; uv run pytest tests/test_generate.py -k unknown — the update applied in any folder, the create and the page-less defer failed, the delete outside the vault; make test; make lint"}`
>   - change: `the Criterion replaced whole — an update of category unknown applies, a delete applies outside the vault, a create and a page-less defer fail; Given out; the method without theme 5 (case 464)`
> - [ ] `tests/test_generate.py`: an `update` of `category: unknown` applies to its page in a category folder and ticks its Spec line; a `create` and a page-less `defer` of `category: unknown` fail with `not a vault folder`; each test name holds `unknown`
> - [ ] `uv run guppi sprint`
> - [ ] read `estimate-sprint-migration-file-route-gone`

> **ratification:**
> ```
> - decision[case 464][update][estimate-sprint-migration-file-route-gone]{ref:estimate-sprint-migration-file-route-gone}
> ```
