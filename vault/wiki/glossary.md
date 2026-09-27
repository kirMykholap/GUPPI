# Glossary

Written by `guppi glossary` from the `## Terms` of `entity-glossary`; a term changes by an `update` of that page.

## [[rule-plan-mode]]

| term | meaning | where |
|---|---|---|
| Ratification | Human sign-off on a Decision; nothing in vault or code changes without one | [[rule-case-protocol]] |
| Contract vs implementation | A Decision fixes what "done" means, never how; a contract change is a new Case | [[rule-case-protocol]] |
| `ref`, `slug`, `supersedes` | A pointer to an existing page (absent: query the vault before a `create`; present: `update`); the page id = filename; the earlier case a ledger line corrects, written `{supersedes:case N}`, one block per Case and several on one line, each of which marks every entry of its Case superseded and clears its `deferred_by` (cases 200.2, 429) | [[rule-case-protocol]] |
| Decision | The atomic unit of work: `create`, `update`, `delete`, `defer`; Read is never one | [[rule-case-protocol]] |
| Types | `create` a page (an Estimate is its own `create`, with `ref` on its target, case 193); `update` fields, `result`/`status` included, or `rename` — the page moves to the new slug and every link follows (case 258.1); `delete` sets `status: deleted` after an impact analysis, the librarian archives; `defer` postpones, a placeholder page when no `ref` | [[rule-case-protocol]] |
| Case | The unit of dialogue, not a page: `context`, `problem`, `recommend`, `given`, `when`, `then`, `tasks`, `ratification` (case 163); `given` is the frame of the Case; `when` + `then` is the Estimate criterion, the Estimate named by slug (cases 193, 378.2); the page content is a `then` block in the Spec; splits into dotted sub-cases the parent's sign-off never covers | [[rule-case-protocol]] |
| Main agent, Subagent | Runs Cases and writes ledger lines, until the Retro commit; executes plan tasks, never decides, a fork returns | [[rule-case-protocol]] |
| the vault query | The vault query before a `create` without `ref`, `draft` pages included (case 277.3) | [[rule-ask]] |
| Index line, `ask-guppi` | The Grep of a category's frontmatter — `purpose`, `root_cause` or `pattern`, and `deferred_by` — one line per live page, never compared across categories; no index file (case 147.8); the search agent over these lines, one entry point; Estimates through the target, Decisions through `deferred_by`; the archive answered by slug alone — `free`, `live` or `archived at <path>` — never by meaning (case 105.1) | [[rule-ask]] |
| `/pre-spec` | The check of the ratified set against each other and the vault before the Spec is approved (case 261) | [[rule-prespec]] |
| Spec | The ratified Cases as one document, approved as Claude Code's plan, copied to `raw/<date>/<hi HHMM>/spec.md`, the session's folder (case 73.1) | [[rule-spec-capture]] |

## [[rule-session]]

| term | meaning | where |
|---|---|---|
| Plan Mode | Frontier items discussed as Cases until each is ratified or deferred | [[rule-plan-mode]] |
| Documentation | The librarian's phase, the agent `librarian-guppi`: materialize, index check, synthesis, generate, cleanup, brief, close | [[rule-documentation]] |
| Librarian | Clean context; the only writer to `wiki/`; reads handoff, yaml, indexes; one judgment, `create` to `update` on a duplicate; flags the rest | [[rule-documentation]] |
| Session | Five phases in one order under [[rule-session]]: Session Start, Plan Mode, Work Mode, End of Work, Documentation | [[rule-session]] |
| Executable plan, Work Mode | The Spec as tasks with code, paths, checkboxes; subagents transcribe, a fork comes back as a Case | [[rule-work-mode]] |

## [[rule-harness]]

| term | meaning | where |
|---|---|---|
| Vault | The folder of Markdown pages, one per category | [[rule-page-schemas]] |
| Page fields | `type` the kind; `purpose` one line the index is built from; `children` MOC only, ordered on a Rule; `estimates` cross-cutting on a MOC; `code_ref` (Entity Leaf), `implementation_ref` (`hook`, `check` rules) | [[rule-page-schemas]] |
| Category fields | Estimate: `purpose`, `method`, `checked`, the sections `Criterion` and `Result` (case 193). Lesson: `trigger`, `root_cause`, `source` (in a ledger line, the external origin). Insight: `severity` (children not archived), `addressed_by` | [[rule-page-schemas]] |
| Scripts | Page generation (fills `origin`, `slug`, `status`); cleanup (moves `archived` pages); lint (refs, schema, statuses, orphans); renderer (Rule body into the file it governs) | [[rule-harness]] |
| Harness | Hooks, agents, skills rendered from `rules/` pages | [[rule-harness]] |
| `CLAUDE.md`, `case-schema.md` | The system prompt, the Render of `rule-claude-md`, whole — the description of the project, `rule-language` and `rule-agent-writing` in their markers (cases 59.8, 272, 288.3); the Case schema is the Render of `rule-case-protocol`, opened by the one rule, and it arrives with `/hi` together with the glossary (cases 273, 288) | [[rule-claude-md]] |

## [[rule-case-protocol]]

| term | meaning | where |
|---|---|---|
| Atomicity Rule | A unit splits when its closing judgment breaks into parts that fail and are fixed apart | [[rule-atomicity]] |

## [[rule-page-schemas]]

| term | meaning | where |
|---|---|---|
| MOC | A thing whose parts the person named as things that are built; `children` lists them; its Estimates measure what no child owns; a part comes from the person's words through a Case — the agent proposes a cut, never makes it (case 240.1) | [[rule-entities-schema]] |
| Leaf | A thing whose parts the person has not named; holds `estimates` — empty is legal, the person said nothing yet — and a code pointer; its inner workings are `## How it works`, not pages (case 240.1) | [[rule-entities-schema]] |
| Entity | A thing the developer builds, a noun the person named as part of what is built; the check before a `create`: who makes it — the developer → an Entity; the product's user or the running product → data, outside the vault; MOC or Leaf; never a page for a "why", that is a Decision (case 240.1) | [[rule-entities-schema]] |
| Rule | A standing condition one case can break, with a guard that refuses that case when it occurs; the check: can one case refute it, and is there something to refuse it; a Leaf a condition on each case, a MOC a sequence whose Estimate promises the order; of the harness or of an Entity; force by `hook`, `check` or `render`; in the harness a thing is a Rule when its code is a guard, an Entity when it is measured and its guard is a separate Rule (case 240.2) | [[rule-rules-schema]] |
| Estimate | The evidence: on a Rule a test that the guard works, on an Entity a reading of the whole no single case can break — the target's prefix says which; `QA` the answer is known, `Research` the reading finds it, on an Entity only, `failed` when the finding does not serve the purpose (case 240.3); one promise, one way to check it, the last result with its date (case 182); its own Leaf page under an Entity or Rule only, an explicit `create` with its slug in the Case, `estimate-<target minus its prefix>-<promise>`; fields `purpose`, `method`, `checked`; `QA` checks a known criterion, `Research` finds out; its Criterion is the `when` and `then` of one Case, replaced whole by the `update` that names it, which alone sets `pending`; no index, reached through the target's `estimates` (case 193) | [[rule-estimates-schema]] |
| Estimate (status) | `pending` / `passed` / `failed`; `failed` is debt, archival the default outcome | [[rule-estimates-schema]] |
| Lesson | Something learned; a fact the hook writes, no Case, no Estimate; slug = area + cause; a `knowledge` claim is checked by the Rule that leans on it | [[rule-lessons-schema]] |
| Insight | Over Lessons sharing a root cause, made by the librarian on the second; stands in `backlog.md` while `open` and is the target of the `update` that actions or rejects it, or of a `defer`; never created or deleted by a Decision; `actioned` reopens (case 124) | [[rule-insights-schema]] |
| Decision page | One page per Case in `wiki/decisions/`, slug `decision-case-<N>`, one list per kind present: `create`, `update`, `delete`, `defer`, body Context, Problem, Given — the frame of the Case (case 378.3); never indexed, reached through `deferred_by`, a History wikilink or `origin` | [[rule-decisions-schema]] |

## [[rule-settings]]

| term | meaning | where |
|---|---|---|
| Hook | An event-triggered script behind a Rule page, the ledger writer on `Stop`, which reads the session's transcript back, keeps its `hi` window across midnight, and can block | [[rule-hook-registry]] |

## [[rule-documentation]]

| term | meaning | where |
|---|---|---|
| `deferred_by` | On an Entity, Rule or Insight, the Decision pages whose `defer` targets it; set by `generate`, cleared by a `supersedes`, shown in the index line, followed by `ask-guppi` | [[rule-page-generation]] |
| `origin` | The Decision that created or deleted the page, as `raw/<date>/<HHMM>/ledger.md#case-N` — the date form on older pages; kept when archived, never rewritten; `#case-N` is a grep target lint checks in `raw/` or in the archive (case 103.6) | [[rule-page-generation]] |
| Entity / Rule (status) | `draft` / `built` / `archived`; `built` is computed once every Estimate passes, never by hand | [[rule-page-generation]] |
| Decision, Lesson, Insight (status) | `current`/`superseded`/`archived`; `new`/`clustered`/`archived`; `open`/`actioned`/`archived`, a new Lesson reopens `actioned` unless a decision of its own session closed its cause (case 284.4) | [[rule-page-generation]] |
| `archived` | Set by `delete`, or by the cascade of `guppi generate` — a superseded Decision, the lessons of an actioned Insight, an open Insight with no live child (case 104); `guppi cleanup` moves the file to `vault/archive/<sprint>/<date>/<HHMM>/<category>/` and brings it back on an `update` of `status`; `guppi archive` moves an applied session of `raw/` whole (case 100.1); never physical deletion | [[rule-cleanup]] |
| Routing Table | (type × `ref` × category) to vault action, mechanical | [[rule-materialize]] |
| Sprint | An Entity Leaf `entity-sprint-<id>` under the MOC `entity-sprint`, the sprint as a kind (case 241), whose Estimates are the Definition of done, whose `## Milestones` holds the Slices in order — the first with an open item is current — and whose `## Backlog` the items without a turn, each a wikilink or a plain line; `sprint.md` is its render, written by `guppi sprint` with one tick per item by the statuses of every page its `[[slug]]` before the first ` — ` names, a line without one a note that never ticks, the current milestone whole and the others one line (cases 209, 229); `/hi` takes the Frontier from the current milestone only | [[rule-sprint]] |
| `brief.md` | The handover between sessions, written by the librarian or by `/carry`, which conserves a Spec (case 200.2); no Deferred list — the deferred items stand in `backlog.md` (case 451.8) | [[rule-brief]] |
| `backlog.md` | Every deferred item in one file, written by `guppi backlog`: the conserved Specs with their targets, then each page with `deferred_by`, each open Insight and each line of the sprint page's `## Backlog`, with its `purpose` or `pattern` and the count of the sessions that put it off; `/hi` loads it, writes its count and names the items near a Frontier item (case 451.4) | [[rule-backlog]] |
| Working files | `log.md` and page `History`, the feed of page changes by hook; `raw/`: `event_log.md` of the day and one folder per session, named by its `hi` time (case 73.1), with its ledger, yaml, Spec, Frontier and handoff, moved whole into the archive once applied (cases 100.1, 103.6); `tags.md`, ratified tags with Russian aliases | [[rule-raw-archive]] |

## [[rule-session-start]]

| term | meaning | where |
|---|---|---|
| `/hi`, Frontier | Opens a working session and records `hi`; the open items it assembles (brief, sprint, backlog, issues, an unfinished plan, the ledger tail) in two lists, the kind of each by its source — Cases, the Plan Mode agenda, and Work, what needs no decision (case 268.2) | [[rule-skill-hi]] |
| Ledger | The record of decisions (routing only), estimates and lessons (with text), written by the `Stop` hook into `raw/<date>/<HHMM>/ledger.md`, the session's folder (case 103.1) | [[rule-ledger-write]] |
| Event log | The gitignored log of tool calls and commits of the day, written by hooks | [[rule-event-log]] |

## [[rule-skill-hi]]

| term | meaning | where |
|---|---|---|
| Issue | Tracked on GitHub; never a page, a `ref` only | [[rule-github-issues]] |

## [[rule-end-of-work]]

| term | meaning | where |
|---|---|---|
| Retro | `/retro`: an analysis of this session only — the frontier first, then every item ends as a lesson, a reading, a short defer (a Case of `context`, `problem`, `purpose` under `## Retro` in the Spec) or a handoff note; edits only finish ratified work; red tests are fixed or reverted into a patch in `raw/`; ends with a commit | [[rule-retro]] |
| Handoff | `/handoff`, gated by `guppi gate` on a dirty tree: `handoff.md` from memory, then the librarian | [[rule-handoff]] |
