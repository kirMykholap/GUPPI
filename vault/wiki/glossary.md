# Glossary

One line per term and where it is defined: `§N` a section of `index.md`, a slug the Rule
page (`draft` while in `docs/migration/`), `here` this row. Rule-class; imported into `CLAUDE.md`.

## Core principle

| term | meaning | where |
|---|---|---|
| Ratification | Human sign-off on a Decision; nothing in vault or code changes without one | §0 |
| Contract vs implementation | A Decision fixes what "done" means, never how; a contract change is a new Case | §0 |
| Atomicity Rule | A unit splits when its closing judgment breaks into parts that fail and are fixed apart | §6 |

## Structure

| term | meaning | where |
|---|---|---|
| Vault | The folder of Markdown pages, one per category below | §1 |
| MOC | A page with no criteria of its own; `children` lists its pages; nests to any depth | §6 |
| Leaf | A page with checkable behaviour of its own; holds `estimates` and a code pointer | §6 |
| C4 model | Not adopted; one question kept for a new top-level Entity, deployment unit or feature, answered as a criterion in `estimates` | here |

## Page categories

| term | meaning | where |
|---|---|---|
| Entity | The thing that gets built; MOC or Leaf; a Leaf carries `code_ref` | entities/schema.md |
| Rule | How the work happens; force by `hook`, `check` or `render`; needs an Estimate | rules/schema.md |
| Estimate | How a behaviour was checked and the outcome; its own Leaf page; `QA` checks a known criterion, `Research` finds out | estimates/schema.md |
| Lesson | Something learned; a fact the hook writes, no Case; slug = area + cause. `error`'s Estimate is born `passed`; `knowledge` needs its Research Estimate passed before an Insight builds on it | lessons/schema.md |
| Insight | Over Lessons sharing a root cause, made by the librarian on the second; never a Decision target; `actioned` reopens | insights/schema.md, §8 |
| Issue | Tracked on GitHub; never a page, a `ref` only | here |

## Fields

| term | meaning | where |
|---|---|---|
| Page fields | `type` the kind; `purpose` one line the index is built from; `children` MOC only, ordered on a Rule; `estimates` cross-cutting on a MOC; `code_ref` (Entity Leaf), `implementation_ref` (`hook`, `check` rules) | schema.md |
| `origin` | The Decision that created or deleted the page; kept when archived; `#case-N` is a grep target lint checks | §4 |
| Category fields | Estimate: `criterion`, `method`, `result`. Lesson: `trigger`, `root_cause`, `source` (in a ledger line, the external origin). Insight: `severity` (children not archived), `addressed_by` | schema.md |
| `ref`, `slug`, `supersedes` | A pointer to an existing page (absent: query the vault before a `create`; present: `update`); the page id = filename; the earlier case a ledger line corrects | §3, §4, §5 |

## Status models

| term | meaning | where |
|---|---|---|
| Entity / Rule | `draft` / `built` / `archived`; `built` is computed once every Estimate passes, never by hand | §7 |
| Decision, Lesson, Insight | `current`/`superseded`/`archived`; `new`/`clustered`/`archived`; `open`/`actioned`/`archived`, a new Lesson reopens `actioned` | schema.md |
| Estimate | `pending` / `passed` / `failed`; `failed` is debt, archival the default outcome | §7 |
| `archived` | Set by `delete` or by `guppi generate`; `guppi cleanup` moves the file to `vault/archived/<sprint>/<date>/<category>/` and brings it back on an `update` of `status`; never physical deletion | §1, §3, rule-cleanup |

## Decisions

| term | meaning | where |
|---|---|---|
| Decision | The atomic unit of work: `create`, `update`, `delete`, `defer`; Read is never one | §3 |
| Types | `create` a page (a Leaf brings a paired Estimate `create`); `update` fields, `result`/`status` included; `delete` sets `status: deleted` after an impact analysis, the librarian archives; `defer` postpones, a placeholder page when no `ref` | §3, §5 |
| Delegate | The agent deciding without ratification; rejected, parked | here |
| Routing Table, Decision page | (type × `ref` × category) to vault action, mechanical; one page per Case in `wiki/decisions/`, slug `decision-case-<N>`, `targets` per ledger line, never indexed, never opened by `ask-guppi` unless asked why | §5, §11 |

## Session

| term | meaning | where |
|---|---|---|
| Session | Session Start, Plan Mode, Work Mode, End of Session | §9 |
| `/hi`, Frontier | Opens a working session and records `hi`; the open items it assembles (brief, sprint, issues, an unfinished plan) are the Plan Mode agenda | rule-skill-hi |
| Sprint, `brief.md` | The backlog giving the session its scope (`migration` during the move); the handover between sessions, deferred items capped at 7, ranked by Insight severity then postponements | sprint.md, rule-brief |
| Case | The unit of dialogue, not a page: `context`, `problem`, `recommend`, `given`, `when`, `then`, `ratification`; `when` + `then` is the Estimate criterion; the page content is a `then` block in the Spec; splits into dotted sub-cases the parent's sign-off never covers | case-schema.md |
| Plan Mode, Pre-task | Frontier items discussed as Cases until each is ratified or deferred; the vault query before a `create` without `ref`, `draft` pages included | rule-plan-mode, rule-pretask |
| Ledger, Event log | The record of decisions (routing only), estimates and lessons (with text), written by the `Stop` hook; the gitignored log of tool calls and commits, written by hooks | §4, rule-ledger-write, rule-event-log |
| Spec | The ratified Cases as one document, approved as Claude Code's plan, copied to `raw/<date>/spec.md` | rule-spec-capture |
| Executable plan, Work Mode | The Spec as tasks with code, paths, checkboxes; subagents transcribe, a fork comes back as a Case | rule-work-mode (draft) |
| Retro, Handoff | `/retro`: review of this session only, edits only finish ratified work, bugs become `lesson[error]`, ends with a commit; `/handoff`, gated by `guppi gate` on a dirty tree: `handoff.md` from memory, then the librarian | rule-end-of-work |
| Index, `ask-guppi` | `wiki/<category>-index.md`, one line per live page, never compared across categories; the search agent over them, one entry point | §11, rule-index, rule-ask |
| Documentation | The librarian's phase, the agent `librarian-guppi`: materialize, index check, synthesis, generate, cleanup, brief, close | rule-documentation |

## Agents and machinery

| term | meaning | where |
|---|---|---|
| Main agent, Subagent | Runs Cases and writes ledger lines, until the Retro commit; executes plan tasks, never decides, a fork returns | §9, case-schema.md |
| Librarian | Clean context; the only writer to `wiki/`; reads handoff, yaml, indexes; one judgment, `create` to `update` on a duplicate; flags the rest | §10 |
| Scripts | Page generation (fills `origin`, `slug`, `status`); cleanup (moves `archived` pages); lint (refs, schema, statuses, orphans); renderer (Rule body into the file it governs) | rule-lint, rule-render-harness |
| Working files | `log.md` and page `History`, the feed of page changes by hook; `raw/`, session artifacts by date; `tags.md`, ratified tags with Russian aliases | §1 |
| Rule-class files | `index.md`, `glossary.md`, `case-schema.md`, every schema; change only by ratified `update` | §1 |
| Harness, Hook | Hooks, agents, skills rendered from `rules/` pages; a hook is an event-triggered script behind a Rule page, the ledger writer on `Stop`, which sees the reply and can block | §9, rule-ledger-write |
| `CLAUDE.md`, `index.md` | The system prompt: `@path` expands this file and `case-schema.md` inline, and points at the sections of the map — layout, routing, ledger, splitting, librarian — read one at a time | CLAUDE.md |

## Retired terms

| term | was | now |
|---|---|---|
| Proposal | A page category, "specification + plan" | An Entity with `status: draft`, plus the Spec |
| Verify, Accept, Revoke | Decision types | `create` + Estimate ref; `update` of `result`/`status`; `delete` or `defer` |
| `deployment_unit`, `authority` | An Entity field; a slug grouping pages | Removed; a MOC's `children` and `tags.md` |
| Librarian Report, Session Digest | Separate artifacts | Lint output + a `brief.md` section; `ledger.md` |
