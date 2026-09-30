# Glossary

Written by `guppi glossary` from the `## Terms` of `entity-glossary`; a term changes by an `update` of that page.

## [[rule-plan-mode]]

| term | meaning | where |
|---|---|---|
| Ratification | Human sign-off on a Decision; nothing in vault or code changes without one | [[rule-case-protocol]] |
| Contract vs implementation | A Decision fixes what "done" means, never how; a contract change is a new Case | [[rule-case-protocol]] |
| `ref`, `slug`, `supersedes` | A pointer to an existing page (absent: query the vault before a `create`; present: `update`); the page id = filename; the earlier case a ledger line corrects, written `{supersedes:case N}`, one block per Case and several on one line, each of which marks every entry of its Case superseded; `generate` clears a defer only from the pages that a decision line of the superseding Case names (cases 200.2, 429, 467.3) | [[rule-case-protocol]] |
| Decision | The atomic unit of work: `create`, `update`, `delete`, `defer`; Read is never one | [[rule-case-protocol]] |
| Types | `create` a page (an Estimate is its own `create`, with `ref` on its target, case 193); `update` fields, `result`/`status` included, or `rename` — the page moves to the new slug and every link follows (case 258.1); `delete` sets `status: archived` with a History line `deleted`, after an impact analysis, and `guppi cleanup` moves the file to the archive; `defer` postpones, a placeholder page when no `ref` | [[rule-case-protocol]] |
| Case | The unit of dialogue, not a page: `context`, `problem`, `recommend`, `given`, `when`, `then`, `tasks`, `ratification` (case 163); `given` is the frame of the Case; `when` + `then` is the Estimate criterion, the Estimate named by slug (cases 193, 378.2); the page content is a `then` block in the Spec; splits into dotted sub-cases the parent's sign-off never covers | [[rule-case-protocol]] |
| Main agent, Subagent | Runs Cases and writes ledger lines, the last of them in the one reply that ends Retro, after its commit (case 531.8); executes plan tasks, never decides, a fork returns | [[rule-case-protocol]] |
| Plan Mode | The Frontier worked item by item: an item that needs a decision is a Case until it is ratified or deferred, an item that needs none closes with no Case, an item of the sprint may be left for later and a backlog item kept as it stands; it ends when no item of the Cases list is open (cases 356.1, 356.2, 421.4, 451.1) | [[rule-case-protocol]] |
| the vault query | The vault query before a `create` without `ref`, `draft` pages included (case 277.3) | [[rule-ask]] |
| Index line, `ask-guppi` | The Grep of a category's frontmatter — `purpose`, `root_cause` or `pattern`, and `deferred_by` — one line per live page, never compared across categories; no index file (case 147.8); the search agent over these lines, one entry point; Estimates through the target, Decisions through `deferred_by`; the archive answered by slug alone — `free`, `live` or `archived at <path>` — never by meaning (case 105.1) | [[rule-ask]] |
| `/pre-spec` | The check of the ratified set against each other and the vault before the Spec is approved (case 261) | [[rule-prespec]] |
| Spec | The ratified Cases as one document, approved as Claude Code's plan, copied to `raw/<date>/<hi HHMM>/spec.md`, the session's folder (case 73.1) | [[rule-spec-capture]] |

## [[rule-harness]]

| term | meaning | where |
|---|---|---|
| Vault | `vault/wiki/`: one folder per page category, each page a file named by its slug | [[rule-vault-layout]] |
| Lint | `guppi lint`, run by `make lint` after the render, sprint, backlog and glossary checks: reports a page that breaks its schema, points at nothing, claims a status its Estimates do not support, or waits for a reading; red is a signal, not a gate | [[rule-lint]] |
| Renderer | `guppi render` writes the text of a Rule page into the harness file it governs, so the page stays the source; it runs with lint and as the librarian's step after `cleanup` | [[rule-render-harness]] |
| Harness | The files that `guppi render` writes from the pages of `rules/`, such as `.claude/settings.json` with its hooks, the skills and agents, `CLAUDE.md`, `case-schema.md` and `guppi.toml` | [[rule-harness]] |
| `CLAUDE.md`, `case-schema.md` | The system prompt, the Render of `rule-claude-md`, whole — the description of the project, `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation` in their markers (cases 59.8, 272, 288.3, 360); the Case schema is the Render of `rule-case-protocol`, opened by the one rule, and it arrives with `/hi` together with the glossary (cases 273, 288) | [[rule-claude-md]] |
| Working files | `log.md`, the feed of page changes written by `generate` and `cleanup`; `tags.md`, the registry of tags ratified in a Case; `raw/` and `archive/`, the working folders of a session | [[rule-vault-layout]] |

## [[rule-page-schemas]]

| term | meaning | where |
|---|---|---|
| Entity fields | `type` the category; `purpose` one line, from which the index line is built; `children` on a MOC; `estimates` on a Leaf its own checks, on a MOC the cross-cutting ones; `code_ref` paths to code, on either kind | [[rule-entities-schema]] |
| Rule fields | `purpose` one line, what the rule prevents; `enforcement` `hook`, `check` or `render`; `implementation_ref` on `hook` and `check`; `governs` and `render_mode` on `render`; `children` ordered, on a MOC; `estimates` that the rule does what it claims | [[rule-rules-schema]] |
| Estimate fields | `method` required, how the promise is checked; `purpose` the promise in one line; `checked` the date of the last reading, written by `generate`; the sections `Criterion` and `Result` | [[rule-estimates-schema]] |
| Lesson fields | `root_cause` one line, what clustering compares; `source` on a `knowledge` lesson, where the material came from; the sections `Trigger` and `Root cause` | [[rule-lessons-schema]] |
| Insight fields | `pattern` one line, the shared root cause; `children` the Lessons clustered; `severity` the count of children not archived, computed by `generate`; `addressed_by` the one decision that actioned it | [[rule-insights-schema]] |
| MOC | A thing whose parts the person named as things that are built; `children` lists them; its Estimates measure what no child owns; a part comes from the person's words through a Case — the agent proposes a cut, never makes it (case 240.1) | [[rule-entities-schema]] |
| Leaf | A thing whose parts the person has not named; holds `estimates` — empty is legal, the person said nothing yet — and a code pointer; its inner workings are `## How it works`, not pages (case 240.1) | [[rule-entities-schema]] |
| Entity | A thing the developer builds, a noun the person named as part of what is built; the check before a `create`: who makes it — the developer → an Entity; the product's user or the running product → data, outside the vault; MOC or Leaf; never a page for a "why", that is a Decision (case 240.1) | [[rule-entities-schema]] |
| Rule | A standing condition one case can break, with a guard that refuses that case when it occurs; the check: can one case refute it, and is there something to refuse it; a Leaf a condition on each case, a MOC a sequence whose Estimate promises the order; of the harness or of an Entity; force by `hook`, `check` or `render`; in the harness a thing is a Rule when its code is a guard, an Entity when it is measured and its guard is a separate Rule (case 240.2) | [[rule-rules-schema]] |
| Estimate | The evidence: on a Rule a test that the guard works, on an Entity a reading of the whole no single case can break — the target's prefix says which; `QA` the answer is known, `Research` the reading finds it, on an Entity only, `failed` when the finding does not serve the purpose (case 240.3); one promise, one way to check it, the last result with its date (case 182); its own Leaf page under an Entity or Rule only, an explicit `create` with its slug in the Case, `estimate-<target minus its prefix>-<promise>`; fields `purpose`, `method`, `checked`; `QA` checks a known criterion, `Research` finds out; its Criterion is the `when` and `then` of one Case, replaced whole by the `update` that names it, which alone sets `pending`; no index, reached through the target's `estimates` (case 193) | [[rule-estimates-schema]] |
| Estimate (status) | `pending` / `passed` / `failed`; `failed` is debt, archival the default outcome | [[rule-estimates-schema]] |
| Lesson | Something learned; a fact the hook writes, no Case, no Estimate; slug = area + cause; a `knowledge` claim is checked by the Rule that leans on it | [[rule-lessons-schema]] |
| Insight | Over Lessons sharing a root cause, made by the librarian on the second; stands in `backlog.md` while `open` and is the target of the `update` that actions or rejects it, or of a `defer`; never created or deleted by a Decision; `actioned` reopens (case 124) | [[rule-insights-schema]] |
| Decision page | One page per Case in `wiki/decisions/`, slug `decision-case-<N>`, one list per kind present: `create`, `update`, `delete`, `defer`; body `## Problem` and `## Recommend`, `## Deferred` for a Case that put something off, and `## History`; a Case with sub-cases has a page of its own with `## Problem`, `## Recommend` and `children`, and the page of a sub-case carries `parent`, its own `## Recommend` when it has one, and no `## Problem` (case 544.8); `## Context` only for a Case without `given` and without sub-cases, such as the short form of a deferred decision, and in the two-line body of a Case superseded in its own session (case 299.4), never `## Given`; the whole Case, `recommend` included, stays in its Case file `cases/case-<N>.md` in the folder of `origin`; a page written before case 513 keeps its Context and Given (case 513); never indexed, reached through `deferred_by`, a History wikilink or `origin` | [[rule-decisions-schema]] |
| `deferred_by` | The Decision pages whose `defer` targets the page; written by `guppi generate` on a defer, cleared when a later Case `supersedes` that one; the index line carries it, so `ask-guppi` reaches the deferred decision (case 52.3) | [[rule-rules-schema]] |
| `origin` | On a page a Case created: where that Case was ratified, `raw/<date>/<HHMM>/ledger.md#case-N` — the date form `raw/<date>/ledger.md#case-N` on pages born before 2026-09-13 (case 103.6); the folder holds the Spec with the Case and, for a Case built by `case-guppi` from session 2026-09-27/1819 on, its Case file (case 513); the pointer is not rewritten when the session is archived (cases 100.1, 103.6) | [[rule-decisions-schema]] |
| Entity (status) | `draft` / `built` / `archived`; `built` is set by the cascade of `generate` once every Estimate passes, never by hand | [[rule-entities-schema]] |
| Rule (status) | `draft` / `built` / `archived`; `built` is set by the cascade of `generate` once every Estimate passes, never by hand | [[rule-rules-schema]] |
| Decision (status) | `current` / `superseded` / `archived`; `superseded` once a later Case names it in `supersedes`, `archived` when the cascade of `generate` then meets it | [[rule-decisions-schema]] |
| Lesson (status) | `new` / `clustered` / `archived`; `clustered` once it belongs to an Insight, `archived` when its Insight is `actioned` | [[rule-lessons-schema]] |
| Insight (status) | `open` / `actioned` / `archived`; `actioned` when a ratified decision addressed it; a new Lesson of the same root cause reopens it unless a decision of its own session closed its cause (case 284.4); `archived` when the cascade finds an `open` Insight with no live child | [[rule-insights-schema]] |

## [[rule-case-protocol]]

| term | meaning | where |
|---|---|---|
| Atomicity Rule | A unit splits when its closing judgment breaks into parts that fail and are fixed apart | [[rule-atomicity]] |

## [[rule-settings]]

| term | meaning | where |
|---|---|---|
| Hook | A script that fires on an event of the session, behind a Rule page; registered in the `hooks` key of `.claude/settings.json`, which `rule-hook-registry` renders, or in an agent's own frontmatter as part of that agent's Render; a new hook in the file is an `update` of `rule-hook-registry` in the Case that creates its Rule | [[rule-hook-registry]] |

## [[rule-documentation]]

| term | meaning | where |
|---|---|---|
| `archived` | Set by `delete`, or by the cascade of `guppi generate` — a superseded Decision, the lessons of an actioned Insight, an open Insight with no live child (case 104); `guppi cleanup` moves the file to `vault/archive/<sprint>/<date>/<HHMM>/<category>/` and brings it back on an `update` of `status`; `guppi archive` moves an applied session of `raw/` whole (case 100.1); never physical deletion | [[rule-cleanup]] |
| Routing Table | (type × `ref` × category) to vault action, mechanical | [[rule-materialize]] |
| Sprint | An Entity Leaf `entity-sprint-<id>` under the MOC `entity-sprint`, the sprint as a kind (case 241), whose Estimates are the Definition of done, whose `## Milestones` holds the Slices in order — the first with an open item is current — and whose `## Backlog` the items without a turn, each a wikilink or a plain line; `sprint.md` is its render, written by `guppi sprint` with one tick per item by the statuses of every page its `[[slug]]` before the first ` — ` names, a line without one a note that never ticks, the current milestone whole and the others one line (cases 209, 229); `/hi` takes the Frontier from the current milestone only | [[rule-sprint]] |
| `brief.md` | The handover between sessions, written by the librarian or by `/carry`, which conserves a Spec (case 200.2); no Deferred list — the deferred items stand in `backlog.md` (case 451.8) | [[rule-brief]] |
| `backlog.md` | Every deferred item in one file, written by `guppi backlog`: the conserved Specs with their targets, then each page with `deferred_by`, each open Insight and each line of the sprint page's `## Backlog`, with its `purpose` or `pattern` and the count of the sessions that put it off; `/hi` loads it, writes its count and names the items near a Frontier item (case 451.4) | [[rule-backlog]] |
| `raw/` | One folder per session, `raw/<date>/<HHMM>/`, with its `ledger.md` and `materialize.yaml`; `guppi archive` moves it whole to `vault/archive/<sprint>/<date>/<HHMM>/raw/` once every entry is applied; `event_log.md` stays in `raw/<date>/` | [[rule-raw-archive]] |

## [[rule-session]]

| term | meaning | where |
|---|---|---|
| Documentation | The librarian's phase, the agent `librarian-guppi`: materialize, index check, synthesis, generate, cleanup, brief, close | [[rule-documentation]] |
| Librarian | Clean context; the only writer to `wiki/`; reads handoff, yaml, indexes; one judgment, `create` to `update` on a duplicate; flags the rest | [[rule-documentation]] |
| Session | Five phases in one order under [[rule-session]]: Session Start, Plan Mode, Work Mode, End of Work, Documentation | [[rule-session]] |
| Work Mode | `/work` runs the approved Spec on a branch other than `main`: a baseline of `make test` and `make lint` first, the tasks in the order of the Spec, each box ticked, then the Work readings; it ends with `/retro` | [[rule-work-mode]] |

## [[rule-session-start]]

| term | meaning | where |
|---|---|---|
| `/hi`, Frontier | Opens a working session and records `hi`; the open items it assembles (brief, sprint, backlog, an unfinished plan, the ledger tail) in three lists, the kind of each by its source — Cases, the Plan Mode agenda; Work, what needs no decision; and Ask, the readings only the person can answer (cases 268.2, 531.11) | [[rule-skill-hi]] |
| Ledger | The record of decisions (routing only), estimates and lessons (with text), written by the `Stop` hook into `raw/<date>/<HHMM>/ledger.md`, the session's folder (case 103.1) | [[rule-ledger-write]] |
| Event log | The gitignored log of tool calls and commits of the day, written by hooks | [[rule-event-log]] |

## [[rule-end-of-work]]

| term | meaning | where |
|---|---|---|
| Retro | `/retro`: an analysis of this session only, called by `/work` in the same turn with no stop for the person — the readings and the lessons in one reply, a commit on green, then `/handoff`, whose `handoff.md` is its report; it writes no short defer, which stands only at the close of Plan Mode, under `## Deferred` in the Spec; edits only finish ratified work; red tests are fixed or reverted into a patch in `raw/` | [[rule-retro]] |
| Handoff | `/handoff`, gated by `guppi gate` on a dirty tree: `handoff.md` from memory, then the librarian | [[rule-handoff]] |
