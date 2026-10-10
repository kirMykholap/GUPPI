## Case 763 — A failed Estimate outside the sprint page is settled only by name

> **context:**
> At the close of a sprint, `uv run guppi sprint-close` lists each Estimate that stands `pending` or `failed`, and the close refuses to move a page until each listed Estimate is settled. `guppi/sprint_close.py` settles a `failed` Estimate without a name only when the sprint page lists it. For any other listed Estimate, `failed` or `pending`, it wants a name by `--carry` or `--archive-unread`. The function `settled` holds this rule, and `tests/test_sprint_close.py` pins it: an unnamed `failed` Estimate outside the sprint page is refused. The Criterion of `estimate-sprint-close-settles-unread-estimates`, which stands `passed`, promises otherwise: such an Estimate, read now with a `failed` result, counts as settled and is carried with no name. The code cannot keep that promise as written, because a page that failed in the closing session looks the same as one that has stood `failed` since an earlier sprint. The handoff of session 1555 reported the disagreement under Observations. The person chose to make the check follow the code, so no code and no test changes.
>
> This Case replaces Case 759, which changed only that Estimate. Pre-spec found two faults in it. First, the `－` line of `estimate-sprint-close-takes-the-readings-in-groups` allows the close line to name only an Estimate still unread after Work Mode. Under the new rule, the close line must also name an Estimate read `failed` in Work Mode that the sprint page does not list. Second, the preview over the live vault in the `method` of the first Estimate cannot run in this session. `Close.__init__` of `guppi/sprint_close.py` stops with no live `entity-sprint-<id>` page, a Glob of `vault/wiki/entities/entity-sprint-*.md` printed no file, and `entity-sprint-migration` stands only under `vault/archive/migration/2026-10-10/1555/`. So Case 763.1 replaces the Criterion of `estimate-sprint-close-settles-unread-estimates` and sets its `purpose` and its `method`. The `method` becomes the `pytest -k settle` run alone. The `When` keeps its line on the preview over the live vault for a later reading. The new Criterion keeps each old line but two. It leaves out on purpose the line that a `failed` reading counts as settled, and puts in its place one line for an Estimate of the sprint page and one for any other Estimate. It keeps the rule that no page moves before the person has chosen for each listed Estimate. Case 763.2 replaces the Criterion of `estimate-sprint-close-takes-the-readings-in-groups` and sets its `purpose`, which states the old promise in its last clause. By the person's answer it sets the `method` to a reading, in this session, of the closing Case and the ledger of the last session that closed a sprint, `vault/raw/2026-10-10/1555/`. That close named five Estimates by `--carry` and none stood `failed`, so the reading passes without testing the new case; the close of `plugin` is its first real test. The new Criterion leaves out on purpose the old `－` line and keeps the other lines. The `then` of the two sub-cases shares words, but the promises differ and can fail apart. Case 763.1 checks what the command `uv run guppi sprint-close` settles. Case 763.2 checks what the closing session writes into its closing Case and its close line.
>
> Step 4 of the Render of `rule-skill-sprint-close` has the closing Case name by `--carry` or `--archive-unread` each Estimate still unread after Work Mode. A closing Case built from that step would leave out an Estimate read `failed` in Work Mode outside the sprint page, and the close would refuse. So Case 763.2 adds that Estimate to the step by a `replace` pair and renders `.claude/skills/sprint-close/SKILL.md`. No other Estimate of that rule reads the live file. A Grep for `still unread` over `vault/wiki/`, `.claude/` and `guppi/` printed `.claude/skills/sprint-close/SKILL.md`, `vault/wiki/rules/rule-skill-sprint-close.md`, `vault/wiki/estimates/estimate-skill-sprint-close-leads-the-closing-session.md` and `vault/wiki/estimates/estimate-sprint-close-takes-the-readings-in-groups.md`. The Criterion of `estimate-skill-sprint-close-leads-the-closing-session` stands. It asks for the person's choice for each Estimate still unread and does not say that only those are named, so naming one more stays true under it. No test reads `.claude/skills/sprint-close/SKILL.md` or either Estimate page live. A Grep for `skills.{0,10}sprint-close|still unread` over `tests/` printed nothing. A Grep for either Estimate slug over `vault/wiki/`, `guppi/`, `tests/` and `.claude/` printed `vault/wiki/brief.md`, `vault/wiki/log.md` and `vault/wiki/rules/rule-sprint-close.md`. The rule page only lists them in `estimates` and stands. The docstring of `guppi/sprint_close.py` already states the code's rule and stands. Case 757 creates an Estimate under `rule-skill-sprint-close` and does not change its Render. Case 756 creates `estimate-sprint-plugin-close-steps-run-from-the-line` on the flow of the closing session as a whole and does not cover this settling.

> **problem:**
> The Criterion of `estimate-sprint-close-settles-unread-estimates` promises that a `failed` reading of an Estimate outside the sprint page settles that Estimate with no name. `guppi/sprint_close.py` and its tests require a name by `--carry` or `--archive-unread` for it. A signed check that the code does not keep stands `passed`, and the check of the closing session and its skill would leave such an Estimate unnamed.

> **recommend:**
> - **Which side follows the other**
>   - Recommended: (a) the check follows the code. The Criterion is replaced so that a `failed` Estimate outside the sprint page must still be named by `--carry` or `--archive-unread`, its `purpose` is reworded, and no code changes.
>   - Answer: agreed, (a).
> - **How the check of the grouped readings is read in this session**
>   - Recommended: (a) read the last close now. The line is fixed so that the close line names an Estimate still unread after Work Mode, or one read `failed` in Work Mode that the sprint page does not list, and the method becomes a reading by hand, in this session, of the closing plan and ledger of the last session that closed a sprint.
>   - Answer: agreed, (a).

### Case 763.1 — The close settles a failed Estimate outside the sprint page only by name

> **given:**
> `estimate-sprint-close-settles-unread-estimates`: the check of the settling step of the close; its Criterion is replaced whole, its `purpose` and `method` set anew.
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
>     method: pytest tests/test_sprint_close.py -k settle
>     ```
>   - change: `the Criterion replaced whole — a failed Estimate outside the sprint page is settled only when --carry or --archive-unread names it, as guppi/sprint_close.py does; the purpose set anew; the method the pytest run alone, since no sprint page is live to preview`
> - [ ] read `estimate-sprint-close-settles-unread-estimates`

> **ratification:**
> ```
> - decision[case 763.1][update][estimate-sprint-close-settles-unread-estimates]{ref:rule-sprint-close}{supersedes:case 759}
> ```

### Case 763.2 — The close line names a failed reading outside the sprint page

> **given:**
> `estimate-sprint-close-takes-the-readings-in-groups`: the check of the closing session; its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `rule-skill-sprint-close`: the skill whose step 4 has the closing Case write the close line.
> **＋** `.claude/skills/sprint-close/SKILL.md`: the rendered skill.
> **＋** `entity-sprint-<id>`: the sprint page whose `estimates` the close reads.
> **＋** `vault/wiki/estimates/`: the Estimates the closing Case sorts.
> **＋** `vault/raw/<date>/<hi HHMM>/spec.md` and `vault/raw/<date>/<hi HHMM>/ledger.md`: the closing Case and the readings of the closing session.

> **when:**
> The session that closes `entity-sprint-<id>` runs its Plan Mode and its Work Mode; someone reads its closing Case in `vault/raw/<date>/<hi HHMM>/spec.md` and its `vault/raw/<date>/<hi HHMM>/ledger.md` after its Work Mode.

> **then:**
> The `context` of the closing Case sorts each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed` into groups by the kind of moment its `method` names.
> **＋** The `tasks` of the closing Case hold one `by hand` task per moment that Work Mode sets up, and one `read` line per Estimate of each group.
> **＋** Work Mode sets up each such moment, and the ledger holds a reading of each Estimate whose moment came.
> **＋** The close line names by `--carry` or `--archive-unread` each Estimate read `failed` in Work Mode that `entity-sprint-<id>` does not list.
> **－** The close line names by `--carry` or `--archive-unread` only an Estimate still unread after Work Mode, or one read `failed` in Work Mode that `entity-sprint-<id>` does not list.

> **tasks:**
> - [ ] update `estimate-sprint-close-takes-the-readings-in-groups`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the session that closes a sprint sorts the pending and failed Estimates into groups by the kind of moment their method names, sets up each moment it can in its Work Mode, and carries or archives unread only those still unread and those read failed that the sprint page does not list
>     method: "by hand, in the session that changes this page: the closing Case in the spec.md and the ledger.md of the last session that closed a sprint, now vault/raw/2026-10-10/1555/, read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the close line also names an Estimate read failed in Work Mode that the sprint page does not list; the purpose and the method set anew`
> - [ ] update `rule-skill-sprint-close`
>   - old: `` for each Estimate still unread after Work Mode; an Estimate of the sprint page is never carried. ``
>   - new: `` for each Estimate still unread after Work Mode and each one read `failed` in Work Mode that the sprint page does not list; an Estimate of the sprint page is never carried. ``
>   - change: `step 4: the close line also names an Estimate read failed in Work Mode that the sprint page does not list`
> - [ ] `uv run guppi render`: `.claude/skills/sprint-close/SKILL.md`
> - [ ] read `estimate-sprint-close-takes-the-readings-in-groups`

> **ratification:**
> ```
> - decision[case 763.2][update][estimate-sprint-close-takes-the-readings-in-groups]{ref:rule-sprint-close}
> - decision[case 763.2][update][rule-skill-sprint-close]{ref:rule-skill-sprint-close}
> ```
