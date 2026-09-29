## Case 515 — Each glossary row points at the page that defines its term

> **context:**
> The glossary that `/hi` loads is the `## Terms` table of `entity-glossary`. `guppi glossary` renders the table into `vault/wiki/glossary.md`. Each row holds a term, its meaning in one line, and in `where` one wikilink to the page that defines the term. The script stops on a `where` cell that holds more than one link. The promise `estimate-glossary-terms-defined` says that each `where` page defines its term. The reading at the `/hi` of this session failed on six rows. "Plan Mode" points at `rule-plan-mode`, whose Purpose names neither the term nor its meaning. "Page fields" and "Category fields" point at `rule-page-schemas`, which leaves the fields to its six child schemas. "Scripts" points at `rule-harness`, which names the renderer and lint but not page generation or cleanup. "Decision, Lesson, Insight (status)" points at `rule-page-generation`, which names none of `current`, `clustered` or `actioned`. "Working files" points at `rule-raw-archive`, which names neither `log.md` nor `tags.md`. The main agent found a seventh row. "Executable plan, Work Mode" says "subagents transcribe, a fork comes back as a Case", but `rule-work-mode` says "Subagents in Work Mode, the test of each Estimate written first and the rest of the model are not decided yet (case 479.2)".
>
> In one round the person chose to fix only the glossary table. Each row points at a page that already defines its term. A term spread over several pages becomes one row per page, and each meaning is cut down to what its page says. The rule pages stay as they are. The person rejected adding sentences to those pages, because `rule-page-schemas` would copy what its children hold. The person also rejected several links in one `where` cell, which would change `guppi/glossary.py`, its tests and the Criterion. About Work Mode, the person said "Executable plan" is a term for a future Work Mode: after the Spec is approved, a plan that maps the tasks is written. That plan is not built yet, and the person left the wording of the row to `case-guppi`. No live page defines "Executable plan". Its only other uses are `docs/migration/`, which Case 510 deletes, and old Decision pages. So the term leaves the table. It comes back as a row with the Case that decides the plan. The row "Work Mode" says what `rule-work-mode` says today. The rule that a subagent never decides and returns at a fork stays in the row "Main agent, Subagent", whose `where` is `rule-case-protocol`.
>
> At pre-spec, `ask-guppi` found an eighth row, and the person accepted the fix. The row "Decision page" says the body is "Context, Problem, Given — the frame of the Case (case 378.3)". Case 513.1 of this session changes `rule-decisions-schema`. After it, a new Decision page carries `## Problem`, `## Deferred` for a Case that put something off, and `## History`. It carries `## Context` only for a Case without `given`, such as the short form of a deferred decision, and never carries `## Given`. The Case file `cases/case-<N>.md` in the folder of `origin` holds the whole Case, and a page written before case 513 keeps its Context and Given. This Case rewrites the row to say what that schema will say. Both pages land at the same librarian run, so the reading in a later session finds them in agreement.
>
> What `case-guppi` found in the frame. Each new meaning was checked against its page. `rule-case-protocol` defines Plan Mode in "Plan Mode and the Frontier". The schema rules list the fields and the status values of their categories. The old "Page fields" row said `code_ref` is on an Entity Leaf only, but `rule-entities-schema` allows it on both kinds, so the new row follows the schema. `rule-lint` and `rule-render-harness` define lint and the renderer. Page generation and cleanup already have rows: `origin`, `deferred_by`, "Entity / Rule (status)" and `archived`. `rule-vault-layout` names `log.md` as written by `generate` and `cleanup`, so the old words "by hook" were wrong. It also names `tags.md` as the registry of ratified tags, and `raw/` and `archive/` as the working folders. `rule-raw-archive` defines the session folders and `event_log.md`. The rows move to the groups of their new pages' parent MOCs, as `rule-glossary` says. `glossary.py` accepts the new rows as they are, so no reader has to accept an old form.
>
> This session's other Cases touch two pages this Case names. Case 513.1 updates `rule-decisions-schema`, and the row "Decision page" follows it. Case 513.3 updates `rule-case-protocol` only in its sentences on `given`, so the Plan Mode section that the row "Plan Mode" rests on stays as it is. Cases 511, 512 and 514 touch none of the pages named here. The Criterion of `estimate-glossary-terms-defined` stands. It already promises what this Case makes true, and the Case does not change the promise. The reading waits for a later session, after the librarian's run renders the table. The other 41 rows passed the reading and are not touched. The Purpose of `entity-glossary` says a term enters, changes or leaves by an `update` of the page, and its `change` line is the History. That stays true. No other page or test uses the removed terms except the old Decision pages, which are records. The Case creates no page, so no vault query was run. Not done: "Executable plan" gets no page and no defer here. That would be a Case of its own.

> **problem:**
> Eight rows of the glossary point at a page that does not define their term, claim what the page leaves undecided, or will be made false by a change ratified this session. So the glossary that `/hi` loads sends the reader to the wrong page, and in some places it states a fact no page holds.

> **recommend:**
> Fix `entity-glossary` alone. Each row points at the page that already defines its term, a term spread over several pages is split into one row per page, and each meaning holds only what its page says. One page changes and no text is copied. Adding the definitions to the pages the rows name now is rejected: `rule-page-schemas` would repeat what its six children already hold.

> **given:**
> `entity-glossary` — the page whose `## Terms` table this Case changes
> **＋** `vault/wiki/glossary.md` — the file `guppi glossary` renders from the table
> **＋** `estimate-glossary-terms-defined` — the promise the table is brought back in line with; its Criterion stands
> **＋** `rule-case-protocol` — the page that defines Plan Mode
> **＋** `rule-entities-schema`, `rule-rules-schema`, `rule-estimates-schema`, `rule-lessons-schema`, `rule-insights-schema`, `rule-decisions-schema` — the schema rules that define the fields and the status values of each category, and the Decision page and its Case file
> **＋** `rule-lint` and `rule-render-harness` — the pages of lint and of the renderer
> **＋** `rule-vault-layout` and `rule-raw-archive` — the pages of the working files and of the session folders
> **＋** `rule-work-mode` — the page of Work Mode, which leaves subagents undecided

> **when:**
> `uv run guppi glossary` writes `vault/wiki/glossary.md` from the `## Terms` table of `entity-glossary` at the librarian's run, and a reader reads each row against the page its `where` names.

> **then:**
> `uv run guppi glossary` exits 0, and each row names in `where` one live page that defines the term of the row.
> **＋** The row of Plan Mode names `rule-case-protocol`.
> **＋** The fields of each page category stand in a row of their own, whose `where` is the schema rule of that category.
> **＋** The status values of Decision, Lesson and Insight stand in a row each, whose `where` is the schema rule of that category.
> **＋** The row of the Decision page says what `rule-decisions-schema` says of the body of a new page and of the Case file that holds the whole Case.
> **＋** A row for lint names `rule-lint`, and a row for the renderer names `rule-render-harness`, in place of the row Scripts.
> **＋** The row of the working files names `rule-vault-layout`, and a row of the session folders names `rule-raw-archive`.
> **＋** The row of Work Mode says what `rule-work-mode` says, and names no subagent.
> **－** No row names the term "Executable plan", since no live page defines it yet.

> **tasks:**
> - [ ] update `entity-glossary`
>   - old:
>     ```
>     | Plan Mode | Frontier items discussed as Cases until each is ratified or deferred | [[rule-plan-mode]] |
>     ```
>   - new:
>     ```
>     | Plan Mode | Frontier items discussed as Cases until each is ratified or deferred | [[rule-case-protocol]] |
>     ```
>   - old:
>     ```
>     | Page fields | `type` the kind; `purpose` one line the index is built from; `children` MOC only, ordered on a Rule; `estimates` cross-cutting on a MOC; `code_ref` (Entity Leaf), `implementation_ref` (`hook`, `check` rules) | [[rule-page-schemas]] |
>     | Category fields | Estimate: `purpose`, `method`, `checked`, the sections `Criterion` and `Result` (case 193). Lesson: `trigger`, `root_cause`, `source` (in a ledger line, the external origin). Insight: `severity` (children not archived), `addressed_by` | [[rule-page-schemas]] |
>     ```
>   - new:
>     ```
>     | Entity fields | `type` the category; `purpose` one line, from which the index line is built; `children` on a MOC; `estimates` on a Leaf its own checks, on a MOC the cross-cutting ones; `code_ref` paths to code, on either kind | [[rule-entities-schema]] |
>     | Rule fields | `purpose` one line, what the rule prevents; `enforcement` `hook`, `check` or `render`; `implementation_ref` on `hook` and `check`; `governs` and `render_mode` on `render`; `children` ordered, on a MOC; `estimates` that the rule does what it claims | [[rule-rules-schema]] |
>     | Estimate fields | `method` required, how the promise is checked; `purpose` the promise in one line; `checked` the date of the last reading, written by `generate`; the sections `Criterion` and `Result` | [[rule-estimates-schema]] |
>     | Lesson fields | `root_cause` one line, what clustering compares; `source` on a `knowledge` lesson, where the material came from; the sections `Trigger` and `Root cause` | [[rule-lessons-schema]] |
>     | Insight fields | `pattern` one line, the shared root cause; `children` the Lessons clustered; `severity` the count of children not archived, computed by `generate`; `addressed_by` the one decision that actioned it | [[rule-insights-schema]] |
>     ```
>   - old:
>     ```
>     | Decision page | One page per Case in `wiki/decisions/`, slug `decision-case-<N>`, one list per kind present: `create`, `update`, `delete`, `defer`, body Context, Problem, Given — the frame of the Case (case 378.3); never indexed, reached through `deferred_by`, a History wikilink or `origin` | [[rule-decisions-schema]] |
>     ```
>   - new:
>     ```
>     | Decision page | One page per Case in `wiki/decisions/`, slug `decision-case-<N>`, one list per kind present: `create`, `update`, `delete`, `defer`; body `## Problem`, `## Deferred` for a Case that put something off, and `## History`; `## Context` only for a Case without `given`, such as the short form of a deferred decision, and never `## Given`; the whole Case, `recommend` included, stays in its Case file `cases/case-<N>.md` in the folder of `origin`; a page written before case 513 keeps its Context and Given (case 513); never indexed, reached through `deferred_by`, a History wikilink or `origin` | [[rule-decisions-schema]] |
>     ```
>   - old:
>     ```
>     | Scripts | Page generation (fills `origin`, `slug`, `status`); cleanup (moves `archived` pages); lint (refs, schema, statuses, orphans); renderer (Rule body into the file it governs) | [[rule-harness]] |
>     ```
>   - new:
>     ```
>     | Lint | `guppi lint`, run by `make lint` after the render, sprint, backlog and glossary checks: reports a page that breaks its schema, points at nothing, claims a status its Estimates do not support, or waits for a reading; red is a signal, not a gate | [[rule-lint]] |
>     | Renderer | `guppi render` writes the text of a Rule page into the harness file it governs, so the page stays the source; it runs with lint and as the librarian's step after `cleanup` | [[rule-render-harness]] |
>     ```
>   - old:
>     ```
>     | Decision, Lesson, Insight (status) | `current`/`superseded`/`archived`; `new`/`clustered`/`archived`; `open`/`actioned`/`archived`, a new Lesson reopens `actioned` unless a decision of its own session closed its cause (case 284.4) | [[rule-page-generation]] |
>     ```
>   - new:
>     ```
>     | Decision (status) | `current` / `superseded` / `archived`; `superseded` once a later Case names it in `supersedes`, `archived` when the cascade of `generate` then meets it | [[rule-decisions-schema]] |
>     | Lesson (status) | `new` / `clustered` / `archived`; `clustered` once it belongs to an Insight, `archived` when its Insight is `actioned` | [[rule-lessons-schema]] |
>     | Insight (status) | `open` / `actioned` / `archived`; `actioned` when a ratified decision addressed it; a new Lesson of the same root cause reopens it unless a decision of its own session closed its cause (case 284.4); `archived` when the cascade finds an `open` Insight with no live child | [[rule-insights-schema]] |
>     ```
>   - old:
>     ```
>     | Working files | `log.md` and page `History`, the feed of page changes by hook; `raw/`: `event_log.md` of the day and one folder per session, named by its `hi` time (case 73.1), with its ledger, yaml, Spec, Frontier and handoff, moved whole into the archive once applied (cases 100.1, 103.6); `tags.md`, ratified tags with Russian aliases | [[rule-raw-archive]] |
>     ```
>   - new:
>     ```
>     | Working files | `log.md`, the feed of page changes written by `generate` and `cleanup`; `tags.md`, the registry of tags ratified in a Case; `raw/` and `archive/`, the working folders of a session | [[rule-vault-layout]] |
>     | `raw/` | One folder per session, `raw/<date>/<HHMM>/`, with its `ledger.md` and `materialize.yaml`; `guppi archive` moves it whole to `vault/archive/<sprint>/<date>/<HHMM>/raw/` once every entry is applied; `event_log.md` stays in `raw/<date>/` | [[rule-raw-archive]] |
>     ```
>   - old:
>     ```
>     | Executable plan, Work Mode | The Spec as tasks with code, paths, checkboxes; subagents transcribe, a fork comes back as a Case | [[rule-work-mode]] |
>     ```
>   - new:
>     ```
>     | Work Mode | `/work` runs the approved Spec on a branch other than `main`: a baseline of `make test` and `make lint` first, the tasks in the order of the Spec, each box ticked, then the Work readings; it ends with `/retro` | [[rule-work-mode]] |
>     ```
>   - change: `each row points at the page that defines its term: Plan Mode, the fields and statuses by category, the Decision page by its schema after case 513, lint and the renderer for Scripts, the working files and raw/, Work Mode without subagents; Executable plan leaves until it is decided (case 515)`
> - [ ] `uv run guppi glossary`
> - [ ] read `estimate-glossary-terms-defined` — by hand in a later session after the librarian's run: the table of `vault/wiki/glossary.md` and `make lint`

> **ratification:**
> ```
> - decision[case 515][update][entity-glossary]{ref:entity-glossary}
> ```
