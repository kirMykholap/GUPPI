## Case 759 — A failed Estimate outside the sprint page is settled only by name

> **context:**
> At the close of a sprint, `uv run guppi sprint-close` lists each Estimate that stands `pending` or `failed`, and the close refuses to move a page until each listed Estimate is settled. `guppi/sprint_close.py` settles a `failed` Estimate without a name only when the sprint page lists it; for any other listed Estimate, `failed` or `pending`, it wants a name by `--carry` or `--archive-unread`. The function `settled` holds this rule, and `tests/test_sprint_close.py` pins it: an unnamed `failed` Estimate outside the sprint page is refused. The Criterion of `estimate-sprint-close-settles-unread-estimates`, which stands `passed`, promises something else. It says that such an Estimate, read now with a `failed` result, counts as settled and is carried with no name. The code cannot keep that promise as written, because a page that failed in the closing session looks the same as one that has stood `failed` since an earlier sprint. The handoff of session 1555 reported the disagreement under Observations. The person chose to make the check follow the code, so no code and no test changes. This Case replaces the Criterion whole and sets the page `pending`. The new Criterion keeps each old line but one. It leaves out on purpose the line that says an Estimate read now whose reading comes out `failed` counts as settled, and puts two lines in its place: one for an Estimate of the sprint page and one for any other Estimate. It also sets anew the `purpose` of the page, which states the old promise in its last clause. The `method` stands: the `pytest -k settle` run and the preview over the live vault run in this session and check the new Criterion. The docstring of `guppi/sprint_close.py` already states the code's rule and stands. Step 4 of the render of `rule-skill-sprint-close` asks for `--carry` or `--archive-unread` for each Estimate still unread after Work Mode. That sentence stands, because the code and its preview lines use unread for an Estimate that stands `pending` or `failed`, so a reading that came out `failed` is still unread there. A Grep for `estimate-sprint-close-settles-unread-estimates` over `vault/wiki/`, `guppi/`, `tests/` and `.claude/` printed `vault/wiki/brief.md`, `vault/wiki/log.md` and `vault/wiki/rules/rule-sprint-close.md`. The rule page only lists the Estimate in `estimates` and stands. No test reads the page live. Case 756 creates `estimate-sprint-plugin-close-steps-run-from-the-line` on the flow of the closing session as a whole; it does not cover this settling, and this Case does not change it.

> **problem:**
> The Criterion of `estimate-sprint-close-settles-unread-estimates` promises that a `failed` reading of an Estimate outside the sprint page settles that Estimate with no name. `guppi/sprint_close.py` and its tests require a name by `--carry` or `--archive-unread` for it. A signed check that the code does not keep stands `passed`.

> **recommend:**
> - **Which side follows the other**
>   - Recommended: (a) the check follows the code. The Criterion is replaced so that a `failed` Estimate outside the sprint page must still be named by `--carry` or `--archive-unread`, its `purpose` is reworded, and no code changes.
>   - Answer: agreed, (a).

> **given:**
> `estimate-sprint-close-settles-unread-estimates`: the check of the settling step of the close; its Criterion is replaced whole and its `purpose` set anew.
> **＋** `rule-sprint-close`: the rule the Estimate checks.
> **＋** `guppi/sprint_close.py`: the command `uv run guppi sprint-close` that the Criterion reads.
> **＋** `tests/test_sprint_close.py`: the made-up vault and the `settle` tests the Criterion runs.
> **＋** `entity-sprint-<id>`: the sprint page whose `estimates` the close reads.
> **＋** `vault/wiki/estimates/`: the live Estimates the close lists.
> **＋** `vault/archive/`: where the moved pages stand.

> **when:**
> `uv run guppi sprint-close --sprint <id>` closes the sprint `entity-sprint-<id>` of the made-up vault of `tests/test_sprint_close.py`, its preview first and then its run with `--apply`, after each Estimate that `entity-sprint-<id>` lists and that does not stand `passed` is read or archived unread, as the person chooses; someone reads the record of the close, `vault/wiki/estimates/` and `vault/archive/` after it.
> **＋** Or the preview `uv run guppi sprint-close --sprint <id>` runs over the live vault, and someone reads its output against `vault/wiki/estimates/`.

> **then:**
> Before any page of the close moves, the close lists to the person each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed`.
> **＋** For each listed Estimate the person chooses one way: read it now, carry it into the next sprint, or archive it unread.
> **＋** An Estimate read now has its reading in the ledger.
> **＋** A listed Estimate that `entity-sprint-<id>` lists and that stands `failed` counts as settled: it stands under `vault/archive/` with the sprint page, and the record of the close keeps its status.
> **＋** A listed Estimate that `entity-sprint-<id>` does not list counts as settled only when the close names it by `--carry` or `--archive-unread`, also when a reading read now came out `failed`.
> **＋** An Estimate carried into the next sprint stays under `vault/wiki/estimates/` with its status.
> **＋** An Estimate archived unread stands under `vault/archive/`, and the page that listed it no longer lists it in `estimates`.
> **－** No page of the close moves before the person has chosen for each listed Estimate.
> **－** An Estimate that `entity-sprint-<id>` lists is not carried into the next sprint: the person reads it now or archives it unread.

> **tasks:**
> - [ ] update `estimate-sprint-close-settles-unread-estimates`
>   - set:
>     ```
>     status: pending
>     purpose: At the close of a sprint each pending or failed Estimate is put to the person, who has it read, carries it into the next sprint or archives it unread, before any page moves; an Estimate of the sprint page is read or archived with the sprint page and never carried, and one that stands failed goes with the sprint page; any other Estimate, one whose reading came out failed included, is settled only when the close names it to be carried or archived
>     ```
>   - change: `the Criterion replaced whole — a failed Estimate outside the sprint page is settled only when --carry or --archive-unread names it, as guppi/sprint_close.py does; the purpose set anew`
> - [ ] read `estimate-sprint-close-settles-unread-estimates`

> **ratification:**
> ```
> - decision[case 759][update][estimate-sprint-close-settles-unread-estimates]{ref:rule-sprint-close}
> ```
