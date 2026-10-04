## Case 619 — The test page reworded, then deleted

> **context:**
> The last session created the test page `entity-reading-probe` to bring on readings that wait for their moment (case 614). Its `## Purpose` holds the made-up word `quillwort` and the word `bramblewort`. A reword is an `update` item that carries `{old, new}` pairs. At the librarian's run, `guppi generate` replaces each pair as a whole word on every live rule, entity and estimate. The page of the item is the owner, and its text must hold each `new`. The reword has never run live. `estimate-generate-rewords` stands `pending`, and its live leg waits for a librarian's run that applies a reword. While the test page is live, `make lint` reports two findings on it, `schema` and `orphan`. `estimate-sprint-migration-lint-clean` needs `make lint` to exit 0 at the close of the sprint. Case 614 could not do the reword in its own session, because the pair check of `guppi/prespec.py` loads only the pages on disk. That gap still stands, and this Case does not fix it.
>
> This Case does the reword and then deletes the page. The two steps are two sub-cases, and both run at the librarian's run after this session. The docstring of `guppi/generate.py` says it applies the entries of a yaml in order. The decision line of 619.1 comes before the line of 619.2, so the reword runs on the live page and then the delete sets it `archived`. `guppi cleanup` (`rule-cleanup`) then moves the page under `vault/archive/` with its History. Its `reworded` History line therefore stays readable. So do the `log.md` line and the stdout line of the run. If the reword fails and the delete applies, a later `update` still reaches the archived page, because `generate` finds a slug that is not under `vault/wiki/` in the archive. `check_items` of `guppi/prespec.py` keys each item by its kind and slug, so an `update` and a `delete` of one page in one Spec are no finding.
>
> Searches. The Grep `quillwort|bramblewort` (case-insensitive) over `vault/wiki/` printed two files: `brief.md` and `entities/entity-reading-probe.md`. A reword never touches `brief.md`, so the pair hits the test page alone. The owner's `## Purpose` holds `bramblewort`, so the check of the owner's text passes, and the pair check of `guppi/prespec.py` finds the pair on a live page. The Grep `quillwort|bramblewort|reading-probe` (case-insensitive) over `vault/wiki/` printed five files: `brief.md`, `log.md`, `entities/entity-reading-probe.md`, `estimates/estimate-plan-mode-verified.md` and `decisions/decision-case-614.md`. The hit on `estimate-plan-mode-verified` stands in its `## Result`, a record that a reword skips and a delete leaves true. The hit on `decision-case-614` is its `create` list, a record. Its `ref` check in `guppi/lint.py` accepts a slug that an archived page carries. The hits in `brief.md` and `log.md` were not read. The Grep `reword` over `vault/wiki/rules/` printed `rule-case-protocol`, `rule-materialize` and `rule-page-generation`. Each describes how a reword pair is written, carried or applied, and this Case follows each as it stands. The same Grep over `.claude/` printed nothing. `rule-page-generation` carries `deferred_by` `decision-case-469`. Its Problem is whether a supersede of an archived Decision keeps `archived`, and that does not touch this Case.
>
> Done means the following. `estimate-generate-rewords` reads the librarian's run that applies the pair. Its Criterion describes exactly that run, so it stands. Its reading comes at the next `/hi` through the Work list of the brief, since this Case does not set it `pending`. The delete is checked by `estimate-generate-writes` (a `delete` sets `archived` with History `deleted`) and `estimate-cleanup-moves`. Both Criteria stand, because the delete is the kind of entry each describes. At the close of the sprint, `estimate-sprint-migration-lint-clean` reads `make lint`, and its Criterion stands. The Criteria of `estimate-entities-schema-checked` and `estimate-lint-finds-a-broken-link` speak of the findings a page like this one draws while it is live. They stand, because they check `guppi lint` and not this page. The page has an empty `estimates` list. This Case creates no Estimate and replaces no Criterion. No other Case of this session is related.

> **problem:**
> The test page has served its purpose except for one moment: a live reword. It keeps `make lint` red and must be gone before any close of the sprint. The question is how to bring on the reword and remove the page in one session, with each step checked on its own.

> **recommend:**
> - **One decision or two?**
>   - Recommended: (b) two sub-cases under one Case, the reword first and the delete second, since the reword can fail on its own and its fix differs from the fix of a delete.
>   - Answer: Agreed with the recommendation.
> - **Does the delete wait for the word change to be read?**
>   - Recommended: (a) both in this session. The reading loses nothing with the delete, and the lint findings clear soonest.
>   - Answer: Agreed with the recommendation.

### Case 619.1 — The made-up word replaced across the vault

> **given:**
> `entity-reading-probe` — the test page that owns the pair and holds the old word
> **＋** `rule-page-generation` — `guppi generate` applies a `reword` at the librarian's run
> **＋** `estimate-generate-rewords` — the check whose live leg this run is

> **when:**
> The librarian's run after this session runs `guppi generate` over the `update` of `entity-reading-probe` that carries the reword pair `quillwort` → `bramblewort`.

> **then:**
> `quillwort` becomes `bramblewort` as a whole word in the `## Purpose` of `entity-reading-probe`.
> **＋** `entity-reading-probe` gets one History line `reworded: quillwort → bramblewort` that names the Decision page of this sub-case.
> **＋** The stdout of `guppi generate` has one line for `entity-reading-probe` with its count of replacements.
> **－** No live page other than `entity-reading-probe` changes by the pair, and the status of no Estimate changes.

> **tasks:**
> - [ ] update `entity-reading-probe`
>   - reword old: `quillwort`
>   - reword new: `bramblewort`
>   - change: `quillwort replaced by bramblewort across the vault, the live leg of estimate-generate-rewords`

> **ratification:**
> ```
> - decision[case 619.1][update][entity-reading-probe]{ref:entity-reading-probe}
> ```

### Case 619.2 — The test page deleted

> **given:**
> `entity-reading-probe` — the test page this sub-case deletes
> **＋** `decision-case-614` — the Decision page whose `create` list keeps the slug
> **＋** `rule-page-generation` — `guppi generate` applies a `delete` at the librarian's run
> **＋** `rule-cleanup` — `guppi cleanup` moves an archived page under `vault/archive/`
> **＋** `rule-lint` — `guppi lint` reports a live page off its schema or named by no page

> **when:**
> The librarian's run after this session runs `guppi generate` over the `delete` of `entity-reading-probe`, after the `update` of Case 619.1, and then runs `guppi cleanup` and `guppi lint`.

> **then:**
> `entity-reading-probe` stands `archived`, with History `deleted` after its `reworded` line.
> **＋** `guppi cleanup` moves `entity-reading-probe` under `vault/archive/`, with its History.
> **＋** `guppi lint` reports no `schema` and no `orphan` finding on `entity-reading-probe`.
> **－** The `create` list of `decision-case-614` keeps the slug, and `guppi lint` reports no `ref` finding for it.

> **tasks:**
> - [ ] delete `entity-reading-probe`
>   - impact: `A test page that no live page links to and that has no Estimate. Its slug stays in the create list of decision-case-614 and in the Result of estimate-plan-mode-verified, both records that an archived page keeps true. Its delete removes the schema and orphan findings of make lint.`

> **ratification:**
> ```
> - decision[case 619.2][delete][entity-reading-probe]{ref:entity-reading-probe}
> ```
