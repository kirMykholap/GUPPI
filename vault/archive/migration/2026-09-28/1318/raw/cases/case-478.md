## Case 478 — The file-route Estimate says which lint findings it covers, and the close of a sprint gets a note

> **context:**
> `make lint` prints one line per finding, in the form `<category>/<slug>: <class>: <what>`. `guppi/lint.py` also prints findings on the `schema.yaml` of a category folder. Those findings are named `<category>/schema`, with the class `schema-description` or `schema.yaml is missing`. The Criterion of `estimate-sprint-migration-file-route-gone` ends with "`make lint` has no finding on a schema". The line can be read two ways. If it means "no finding of the class `schema`", it fails today on 64 findings: 62 on the Decision pages of cases 1–28 and 2 on `rule-spec-box`. If it means "no finding on a `<category>/schema`", it passes. The brief lists 98 lint findings, and none of them is on a schema file. Case 320 wrote the line when the file route was the way to change the schema files by hand. The first reading of 2026-09-22 recorded "no finding on a <category>/schema". The Estimate is `pending`. The main agent ran the grep of its `method` on `guppi/` today and it found no match.
> The person decided in one round. The line means no finding on a `<category>/schema`. The Criterion is replaced whole with that wording, and `purpose` and `method` are reworded to match. The person also asked whether an Estimate like this one goes to the archive once its condition holds. An Estimate has three statuses, `pending`, `passed` and `failed`, and no status for "done". The only way to remove it is a `delete`. The person chose to keep the Estimate live until the sprint closes, so that it still catches a regression. The general rule is that the sprint page and its Estimates go to the archive together at the close of a sprint. It belongs to Slice 5 and is not decided here. It becomes a note in the Slice 5 milestone of `entity-sprint-migration`. Under `rule-sprint`, a note is a line with no wikilink before the ` — `: a task not yet cut into pages, never ticked. At pre-spec, the check of the plan found two parts of the note that the `then` of 478.2 did not state: the condition "once each has passed" and the reason. The person accepted the fix, and the `then` of 478.2 now states both.
> The vault's answer: no `create`, so no vault query ran. The frame. Each line of the old Criterion is carried unchanged, except the lint line, which is changed on purpose, so the check notes it as not carried. 478.1 adds a `－` line that leaves the findings on pages to `estimate-sprint-migration-lint-clean`. That Estimate promises that `make lint` exits 0 at the close of the sprint. It stays true and is not touched. The Purpose of `entity-sprint-migration` says "the `file` route out of the scripts", which stays true. The Criterion of `estimate-sprint-migration-lint-clean` wants each item of `## Milestones` to be "a wikilink to a page or a plain line", and the note is a plain line. Under `rule-sprint`, the note keeps Slice 5 open until a Case cuts it or removes it. Slice 5 already stands open. No reader in code changes.
> Not done: this session cannot read the Estimate, because a Case of this session replaces its Criterion (case 428.1). The brief listed it under Work, and it now moves to a later session. The Estimate is not deleted. No rule on the close of a sprint is written, and no Estimate is archived.

> **problem:**
> One line of the Criterion of `estimate-sprint-migration-file-route-gone` has two readings: one passes today and one fails. A reader cannot tell which reading the promise means. No page says what happens to the Estimates of a sprint when it closes.

> **recommend:**
> Two sub-cases. 478.1 replaces the Criterion of `estimate-sprint-migration-file-route-gone` whole, so that the lint line names the findings on a `<category>/schema`. It also rewords `purpose` and `method` to match. 478.2 adds a note to the Slice 5 milestone of `entity-sprint-migration`: at the close of a sprint, once each Estimate has passed, the sprint page and its Estimates go to the archive together. They are two sub-cases because the promise and the note can fail apart and need different fixes. The rejected option was to read the line as every finding of the class `schema`. That would fail this Estimate on Decision pages that have nothing to do with the file route, and it would repeat the promise of `estimate-sprint-migration-lint-clean`. A `delete` now was also rejected: the Estimate still guards against a regression until the sprint closes.

### Case 478.1 — The lint line of the file-route Estimate names the findings on a category schema

> **given:**
> `estimate-sprint-migration-file-route-gone` — the promise that the file route is gone; its Criterion replaced whole
> **＋** `guppi/` — the scripts the file route left
> **＋** `guppi/generate.py` — applies or fails the entry of each kind, and ticks the line of an applied entry
> **＋** `guppi/materialize.py` — `category_of` gives the entry of a slug with no prefix `category: unknown`
> **＋** `guppi/prespec.py` — `check_governed` refuses an `update` item that carries `file`
> **＋** `guppi/lint.py` — reports a finding on the `schema.yaml` of a category folder as `<category>/schema`
> **＋** `estimate-sprint-migration-lint-clean` — the promise of `make lint` at the close of the sprint, which stands
> **＋** `vault/wiki/sprint.md` — shows the `purpose` of the Estimate

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
> **＋** `make test` is green, and `make lint` prints no finding on a `<category>/schema`, the `schema.yaml` of a category folder.
> **－** `generate` prints "applied by hand" for no entry.
> **－** A `make lint` finding on a page, a missing field or section of a Decision page or a rule page included, is outside this promise: `estimate-sprint-migration-lint-clean` holds it.

> **tasks:**
> - [ ] update `estimate-sprint-migration-file-route-gone`
>   - set: `{status: pending, purpose: "The file route is out of the scripts — no RULE_CLASS, rule_class, applied by hand or prose_names in guppi/; an update item with file is a pre-spec finding; a slug without a prefix lands category unknown; tests green and no lint finding on the schema.yaml of a category folder", method: "rg 'RULE_CLASS|rule_class|applied by hand|prose_names' guppi/ empty; uv run pytest tests/test_generate.py -k unknown — the update applied in any folder, the create and the page-less defer failed, the delete outside the vault; make test; make lint — no line on a <category>/schema"}`
>   - change: `the Criterion replaced whole — the lint line names the findings on a <category>/schema, and a finding on a page is left to estimate-sprint-migration-lint-clean; purpose and method reworded to match (case 478.1)`
> - [ ] `uv run guppi sprint`
> - [ ] read `estimate-sprint-migration-file-route-gone`

> **ratification:**
> ```
> - decision[case 478.1][update][estimate-sprint-migration-file-route-gone]{ref:estimate-sprint-migration-file-route-gone}
> ```

### Case 478.2 — A note in Slice 5: the sprint page and its Estimates go to the archive together at the close

> **given:**
> `entity-sprint-migration` — the Slice 5 milestone, the closing of the sprint
> **＋** `rule-sprint` — a line with no wikilink before the ` — ` is a note, never ticked
> **＋** `vault/wiki/sprint.md` — rendered from the sprint page by `uv run guppi sprint`

> **when:**
> Someone reads the Slice 5 milestone of `entity-sprint-migration`, or `vault/wiki/sprint.md` after `uv run guppi sprint`.

> **then:**
> Slice 5 holds a note: at the close of a sprint, once each Estimate the sprint page lists has passed, the sprint page and those Estimates go to the archive together.
> **＋** The note gives its reason: a done-condition of a sprint has nothing left to guard after the close.
> **＋** The note is never ticked, and it keeps Slice 5 open until a Case cuts it into pages or removes it.
> **－** No Estimate goes to the archive, and no status changes: the note decides nothing.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - old: `- [[rule-morph]] — the morph mechanism: the initiation at install sets the category set of the project, the development set by default, held as data so that a changed set rewrites no rule; case 239`
>   - new:
>     ````
>     - [[rule-morph]] — the morph mechanism: the initiation at install sets the category set of the project, the development set by default, held as data so that a changed set rewrites no rule; case 239
>     - the close of a sprint — `entity-sprint-<id>` and the Estimates it lists go to the archive together once each has passed: a done-condition of a sprint has nothing left to guard after the close; not yet decided (case 478.2)
>     ````
>   - change: `a note in Slice 5: the sprint page and its Estimates go to the archive together at the close of a sprint, once each has passed (case 478.2)`
> - [ ] `uv run guppi sprint`

> **ratification:**
> ```
> - decision[case 478.2][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
