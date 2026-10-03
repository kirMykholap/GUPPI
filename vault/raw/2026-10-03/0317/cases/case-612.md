## Case 612 — What the close of a sprint moves to the archive and what it keeps

> **context:**
> A sprint is an Entity Leaf, `entity-sprint-<id>`. Its `estimates` are the sprint's done-conditions, and `guppi sprint` renders it into `vault/wiki/sprint.md`, which `/hi` loads. Nothing closes a sprint today. Under its closing milestone, the sprint page holds only an undecided note (case 478.2). It says the sprint page and its Estimates go to the archive once each has passed. A page leaves the live vault today only through an event of its own. A Decision page leaves when a later Case supersedes it. The lessons of an Insight leave once that Insight is `actioned`. An `open` Insight leaves when no live lesson is left under it. Any page leaves when a Case deletes it. The cascade of `guppi/generate.py` sets `archived`, and `guppi cleanup` (`rule-cleanup`) moves the page under `vault/archive/<sprint>/`. Everything else stays live. The main agent counted the live vault this session: 1003 Decision pages (2.7 MB), 74 lessons, 29 Insights and 195 Estimates, of which 37 are `pending` and 1 is `failed`. The person sees an endless loop of fixes, with readings that hang session after session, and wants the close of a sprint to clean the vault.
>
> In the rounds the person chose what the close does. It archives the sprint's Decision pages, but keeps those that a live page names in `deferred_by` or `addressed_by`. It archives the sprint's `actioned` Insights and its `error` lessons that joined no Insight, and keeps `knowledge` lessons and `open` Insights with their lessons. It archives the sprint page with its own Estimates, and keeps every other `passed` Estimate as the contract of its rule. Before anything moves, it puts each `pending` or `failed` Estimate to the person: read it, carry it into the next sprint, or archive it unread. The person did not decide where the close runs. They see it as a mode of work of its own, not a choice after Plan Mode, and left it for later. So this Case creates `rule-sprint-close` as a draft that holds these choices. The rule has no `enforcement` and no code. The rules schema keeps `enforcement` optional, and the Case that decides where the close runs gives the rule its guard. Not done: where the close runs, how the next sprint opens, and any code.
>
> The sprint page's own Estimates are read at the close itself. Their methods say so:
> - `estimate-sprint-migration-leftovers-gone` reads the tree by hand at the close of the sprint.
> - `estimate-sprint-migration-lint-clean` reads `make lint` at the close.
> - `estimate-sprint-migration-merges` reads `git log` of `main` at the close, and its Criterion calls the cascade's `built` on the sprint page the close of the sprint.
>
> So these Estimates cannot pass before the close runs. In this Case the close runs first and reads the sprint page's own Estimates in it. Pages move only once each of those Estimates has passed, which is when the cascade sets the sprint page `built`. This matches the merge Estimate's wording and the order of 612.4. All three Criteria therefore stand.
>
> The person chose that this sprint closes with a clean lint, so the Criterion of `estimate-sprint-migration-lint-clean` stands. At this sprint's first close, carrying an Estimate forward would leave an `unread` line that fails that Criterion.
>
> The rule's four parts can fail separately and need different fixes, so each part is a sub-case with an Estimate of its own. Each Estimate is read by hand after the first close of a sprint. The four sub-cases share the same trigger and the same shape of result, and each one names a different set of pages. The check of the answer noted that their `then` lines share words, and that is why.
>
> The closing milestone of `entity-sprint-migration` names the new rule as its item, and a plain note there says that where the close runs is not decided. A note keeps the milestone open (`rule-sprint`), and every session sees it in `sprint.md`. No put-off decision is written. That would add a `deferred` line to `make lint`, which the current sprint's clean-lint condition would have to clear.
>
> The vault query of `.claude/agents/ask-guppi.md` ran for the `create` without a `ref`. These are its findings:
> - exists: none. A Glob of `vault/wiki/**/rule-sprint-close*.md` and one of `vault/archive/**/*sprint-close*.md` printed no file, so the slug is free.
> - near: `rule-cleanup` moves a page that already stands `archived` but chooses none; `rule-sprint` renders the sprint page and does not close it; `entity-sprint` is the kind, which carries no Estimate.
> - rules: `lesson-case-build-closes-a-sprint-item-without-the-sprint-page` requires a Case that closes a sprint item to update the sprint page, which 612.1 does.
> - tags: `sprint` and `workflow`, both existing.
>
> `rule-morph` is a line under the `## Backlog` of the sprint page, about the category set, and this Case does not touch it. `applies_to: [entity-sprint]` makes the cascade add the new rule to the `rules` of `entity-sprint`. Its Purpose sentence that the page carries no Estimate stays true, because the new Estimates target the rule.
>
> Some texts say today that a lesson or an Insight leaves only through its Insight, or that an `actioned` Insight stays live for a later lesson to join. These texts become false only when a close first runs, and nothing runs one until the Case that decides where it runs. That Case changes them, and the Purpose of the new rule names them. A Grep of `archived only when|kept for the recurrence|stays live with its|never archived` over the repository outside `vault/wiki/decisions/`, `vault/archive/` and `vault/raw/` printed 5 files:
> - `.claude/agents/librarian-guppi.md`
> - `vault/wiki/insights/schema.yaml`
> - `vault/wiki/rules/rule-synthesis.md`
> - `vault/wiki/rules/rule-insights-schema.md`
> - `vault/wiki/estimates/estimate-synthesis-clusters.md`
>
> The first two are the renders of `rule-synthesis` and `rule-insights-schema`. The pre-spec check named `estimate-synthesis-keeps-actioned-by-the-mark` as well. Its Criterion has a later lesson join an existing `actioned` Insight, which keeps its status. That Insight is no longer live once a close has archived it. A Grep of `archived` over `rule-lessons-schema.md` and `rule-decisions-schema.md` printed the `status` field of each. One says a lesson is archived when its Insight is `actioned`. The other says a Decision page is archived when superseded. These stand until that Case too.
>
> A Grep of `close of (the|a) sprint|sprint clos|closes? the sprint` over `vault/wiki/rules/` and `.claude/` printed one file, `rule-prespec.md`, and the hit is a History line. A Grep of `478\.2|Slice 5` over the repository outside `vault/wiki/decisions/`, `vault/archive/` and `vault/raw/` printed 9 files:
> - `brief.md`
> - `backlog.md`
> - `sprint.md`
> - `log.md`
> - `entity-sprint-migration.md`
> - `estimate-sprint-items-move-only-by-a-case.md`
> - `estimate-hi-writes-frontier.md`
> - `tests/test_sprint.py`
> - `rule-morph.md`
>
> `brief.md` and `log.md` were not read. `sprint.md` is rendered again. The hits in `backlog.md` and `rule-morph.md` are the line of `rule-morph`. The hits in the two Estimates are Results of past readings. The hits in `tests/test_sprint.py` are test fixtures. All of these stay true. The Estimates of `rule-sprint` and `rule-cleanup` speak of the render, of moves by a Case and of the moves of `cleanup`, none of which this Case changes. Case 611 changes `rule-case-check` and an Insight, and sets nothing about a sprint.

> **problem:**
> Nothing closes a sprint, and the live vault only grows. Decision pages, finished Insights, lessons that never recurred and hanging readings stay live for good. The question was what the close of a sprint moves to the archive, what it keeps, how each part is checked, and where the close runs. The person settled everything except where it runs.

> **recommend:**
> - **What happens to the sprint's Decision pages at the close?**
>   - Recommended: (a) archive them, except the ones an open defer names.
>   - Answer: agreed, (a).
> - **What happens to lessons and Insights at the close?**
>   - Recommended: (a) archive actioned Insights and failure lessons that joined nothing; keep fact lessons and open Insights with their lessons.
>   - Answer: agreed, (a).
> - **What happens to the Estimates that passed?**
>   - Recommended: (a) keep them live; the close archives only the sprint page's own Estimates.
>   - Answer: agreed, (a).
> - **What happens to Estimates still pending or failed at the close?**
>   - Recommended: (c) the close settles each one: read it now, carry it into the next sprint, or archive it unread.
>   - Answer: agreed, (c).
> - **Who closes a sprint?**
>   - Recommended: (a) a Case you ratify.
>   - Answer: not one of the options. The close of a sprint is more than a Case: it is a separate skill or agent, more likely a separate mode of work. Where to place it is unclear, and a choice after Plan Mode seems illogical. It needs more thought. Replaced by the question where the close runs.
> - **Where does the close of a sprint run?**
>   - Recommended: (a) record what the close does now, and decide later where it runs.
>   - Answer: agreed, (a); to be thought about later.
> - **Where does the open question of where the close runs stay until you decide it?**
>   - Recommended: (a) a note on the sprint page.
>   - Answer: agreed with the recommendation, (a).
> - **How is the close checked?**
>   - Recommended: (a) four Estimates, one per part, read by hand at the first close.
>   - Answer: agreed with the recommendation, (a).
> - **What happens to the current sprint's clean-lint condition?**
>   - Recommended: (a) replace its Criterion so that Estimates carried into the next sprint may stay unread.
>   - Answer: (b), leave it as it stands; this sprint will close with a clean lint.

### Case 612.1 — The close archives the sprint's Decision pages, except the ones a live page names

> **given:**
> `rule-sprint-close` — the new rule of what the close of a sprint archives and keeps
> **＋** `estimate-sprint-close-archives-the-decisions` — the promise on Decision pages
> **＋** `entity-sprint-<id>` — the sprint page that closes, with the Estimates it lists
> **＋** `vault/wiki/decisions/` — the Decision pages, each with its `sprint`
> **＋** `vault/archive/` — where an archived page stands, moved there by `rule-cleanup`
> **＋** `entity-sprint-migration` and `vault/wiki/sprint.md` — the current sprint page, whose closing milestone names the new rule and keeps a note, and its render by `guppi sprint`
> **＋** `rule-sprint` — the form of a milestone item and of a note

> **when:**
> The close of the sprint `entity-sprint-<id>` runs: the Estimates that `entity-sprint-<id>` lists are read in it first, and its pages move once each of them stands `passed`; someone reads `vault/wiki/decisions/` and `vault/archive/` after it.

> **then:**
> Each Decision page under `vault/wiki/decisions/` whose `sprint` is `<id>` stands under `vault/archive/`.
> **－** A Decision page that a live page names in `deferred_by` or `addressed_by` stays under `vault/wiki/decisions/`.
> **－** A Decision page whose `sprint` is another sprint does not move.

> **tasks:**
> - [ ] create `rule-sprint-close`
>   - type: `rule`
>   - kind: `Leaf`
>   - purpose: `Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow`
>   - applies_to: `[entity-sprint]`
>   - tags: `[sprint, workflow]`
>   - sections.Purpose:
>     ```
>     Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow. The close of `entity-sprint-<id>` reads the Estimates the sprint page lists first, and its pages move only once each of them has passed. Then the Decision pages of the sprint go to the archive, but a Decision page that a live page names in `deferred_by` or `addressed_by` stays (case 612.1). The `actioned` Insights of the sprint go, and its `error` lessons that joined no Insight; its `knowledge` lessons, its `open` Insights and their lessons stay (case 612.2). The sprint page and the Estimates it lists go; every other `passed` Estimate stays, the contract of its rule (case 612.3). Before anything moves, each Estimate that stands `pending` or `failed` is put to the person, who has it read, carries it into the next sprint, or archives it unread (case 612.4). Where the close runs, and how the next sprint opens, are not decided: the Case that decides them gives this rule its guard, and changes the texts that say a lesson, an Insight or a Decision page leaves only through its own event, or that an `actioned` Insight stays live for a later lesson: `rule-insights-schema`, `rule-lessons-schema`, `rule-decisions-schema`, `rule-synthesis`, `estimate-synthesis-clusters` and `estimate-synthesis-keeps-actioned-by-the-mark`.
>     ```
> - [ ] create `estimate-sprint-close-archives-the-decisions`
>   - type: `estimate`
>   - ref: `rule-sprint-close`
>   - kind: `QA`
>   - purpose: `At the close of a sprint its Decision pages go to the archive, but those a live page names in deferred_by or addressed_by`
>   - method: `by hand, vault/wiki/decisions/ and vault/archive/ read after the first close of a sprint`
>   - tags: `[sprint, workflow]`
> - [ ] update `entity-sprint-migration`
>   - old:
>     ```
>     - the close of a sprint — `entity-sprint-<id>` and the Estimates it lists go to the archive together once each has passed: a done-condition of a sprint has nothing left to guard after the close; not yet decided (case 478.2)
>     ```
>   - new:
>     ```
>     - [[rule-sprint-close]] — what the close of a sprint moves to the archive and what it keeps (case 612.1)
>     - where the close of a sprint runs — a session of its own, a command or another place: not decided (case 612.1)
>     ```
>   - change: `Slice 5: the close of a sprint is the item rule-sprint-close, and where the close runs is a note, not decided (case 612.1)`
> - [ ] `uv run guppi sprint`
> - [ ] read `estimate-sprint-close-archives-the-decisions`

> **ratification:**
> ```
> - decision[case 612.1][create][rule-sprint-close]{tags:sprint,workflow}
> - decision[case 612.1][create][estimate-sprint-close-archives-the-decisions]{ref:rule-sprint-close}{tags:sprint,workflow}
> - decision[case 612.1][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```

### Case 612.2 — The close archives actioned Insights and failure lessons that joined no Insight

> **given:**
> `rule-sprint-close` — the rule of the close
> **＋** `estimate-sprint-close-archives-done-insights-and-lone-lessons` — the promise on lessons and Insights
> **＋** `entity-sprint-<id>` — the sprint page that closes, with the Estimates it lists
> **＋** `vault/wiki/insights/` and `vault/wiki/lessons/` — the Insights and lessons, each with its `sprint`
> **＋** `vault/archive/` — where an archived page stands
> **＋** `rule-insights-schema`, `rule-lessons-schema` and `rule-synthesis` — say today when a lesson or an Insight leaves; unchanged here

> **when:**
> The close of the sprint `entity-sprint-<id>` runs: the Estimates that `entity-sprint-<id>` lists are read in it first, and its pages move once each of them stands `passed`; someone reads `vault/wiki/insights/`, `vault/wiki/lessons/` and `vault/archive/` after it.

> **then:**
> Each Insight under `vault/wiki/insights/` whose `sprint` is `<id>` and that stands `actioned` stands under `vault/archive/`.
> **＋** Each lesson under `vault/wiki/lessons/` whose `sprint` is `<id>`, whose `kind` is `error` and that stands `new` stands under `vault/archive/`.
> **－** A lesson whose `kind` is `knowledge` stays under `vault/wiki/lessons/`.
> **－** An Insight that stands `open`, and each lesson its `children` lists, stay live.

> **tasks:**
> - [ ] create `estimate-sprint-close-archives-done-insights-and-lone-lessons`
>   - type: `estimate`
>   - ref: `rule-sprint-close`
>   - kind: `QA`
>   - purpose: `At the close of a sprint its actioned Insights and its error lessons that joined no Insight go to the archive, and its knowledge lessons and open Insights stay`
>   - method: `by hand, vault/wiki/insights/, vault/wiki/lessons/ and vault/archive/ read after the first close of a sprint`
>   - tags: `[sprint, workflow]`
> - [ ] read `estimate-sprint-close-archives-done-insights-and-lone-lessons`

> **ratification:**
> ```
> - decision[case 612.2][create][estimate-sprint-close-archives-done-insights-and-lone-lessons]{ref:rule-sprint-close}{tags:sprint,workflow}
> ```

### Case 612.3 — The close archives the sprint page with its own Estimates and keeps every other passed Estimate

> **given:**
> `rule-sprint-close` — the rule of the close
> **＋** `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` — the promise on the sprint page and the passed Estimates
> **＋** `entity-sprint-<id>` — the sprint page that closes, with the Estimates it lists
> **＋** `entity-sprint` — the kind, whose Leaf the sprint page is
> **＋** `vault/wiki/entities/` and `vault/wiki/estimates/` — the Entity pages, and the Estimates, each with its `target`
> **＋** `vault/archive/` — where an archived page stands

> **when:**
> The close of the sprint `entity-sprint-<id>` runs: the Estimates that `entity-sprint-<id>` lists are read in it first, and its pages move once each of them stands `passed`; someone reads `vault/wiki/entities/`, `vault/wiki/estimates/` and `vault/archive/` after it.

> **then:**
> `entity-sprint-<id>` and each Estimate its `estimates` lists stand under `vault/archive/`.
> **－** Every other Estimate that stands `passed` stays under `vault/wiki/estimates/`, and the rule or Entity that lists it keeps it in `estimates`.
> **－** The close does not archive the MOC `entity-sprint`.

> **tasks:**
> - [ ] create `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`
>   - type: `estimate`
>   - ref: `rule-sprint-close`
>   - kind: `QA`
>   - purpose: `At the close of a sprint the sprint page and its own Estimates go to the archive, and every other passed Estimate stays live`
>   - method: `by hand, vault/wiki/entities/, vault/wiki/estimates/ and vault/archive/ read after the first close of a sprint`
>   - tags: `[sprint, workflow]`
> - [ ] read `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`

> **ratification:**
> ```
> - decision[case 612.3][create][estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest]{ref:rule-sprint-close}{tags:sprint,workflow}
> ```

### Case 612.4 — The close puts each Estimate not passed to the person before anything moves

> **given:**
> `rule-sprint-close` — the rule of the close
> **＋** `estimate-sprint-close-settles-unread-estimates` — the promise on the Estimates not passed
> **＋** `entity-sprint-<id>` — the sprint page that closes, with the Estimates it lists
> **＋** `vault/wiki/estimates/` — the Estimates, each with its status
> **＋** `vault/archive/` — where an archived page stands
> **＋** `estimate-sprint-migration-lint-clean` — the current sprint's clean-lint condition; unchanged

> **when:**
> The close of the sprint `entity-sprint-<id>` runs: the Estimates that `entity-sprint-<id>` lists are read in it first, and its pages move once each of them stands `passed`; someone reads the record of the close, `vault/wiki/estimates/` and `vault/archive/` after it.

> **then:**
> Before any page of the close moves, the close lists to the person each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed`.
> **＋** For each listed Estimate the person chooses one way: read it now, carry it into the next sprint, or archive it unread.
> **＋** An Estimate read now has its reading in the ledger.
> **＋** An Estimate carried into the next sprint stays under `vault/wiki/estimates/` with its status.
> **＋** An Estimate archived unread stands under `vault/archive/`, and the page that listed it no longer lists it in `estimates`.
> **－** No page of the close moves before the person has chosen for each listed Estimate.

> **tasks:**
> - [ ] create `estimate-sprint-close-settles-unread-estimates`
>   - type: `estimate`
>   - ref: `rule-sprint-close`
>   - kind: `QA`
>   - purpose: `At the close of a sprint each pending or failed Estimate is put to the person, who has it read, carries it into the next sprint or archives it unread, before any page moves`
>   - method: `by hand, the record of the first close of a sprint, vault/wiki/estimates/ and vault/archive/ read after it`
>   - tags: `[sprint, workflow]`
> - [ ] read `estimate-sprint-close-settles-unread-estimates`

> **ratification:**
> ```
> - decision[case 612.4][create][estimate-sprint-close-settles-unread-estimates]{ref:rule-sprint-close}{tags:sprint,workflow}
> ```
