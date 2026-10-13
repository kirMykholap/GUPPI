---
type: entity
kind: Leaf
purpose: The terms of GUPPI, one row each with its meaning and the page that defines it; the source of glossary.md
status: built
parent: "[[entity-guppi]]"
estimates: ["[[estimate-glossary-terms-defined]]"]
rules: ["[[rule-glossary]]"]
origin: raw/2026-09-22/0014/ledger.md#case-306.3
sprint: migration
created: 2026-09-22
tags: [session, harness]
core: true
---

## Purpose

The terms of GUPPI: one row per term — the term, its meaning in one line, and `where`, the live page that defines it. The table is the content of this page; `rule-glossary` is its guard and renders `vault/wiki/glossary.md` from it, grouped by the parent MOC of `where`, for `/hi` to load. A term enters, changes or leaves by an `update` of this page in a Case — a `replace` pair or the section whole — and the `change` line is its History; a retired term is a History line, not a row. Not rows: C4 model (not adopted), Delegate (the agent deciding without ratification; rejected), and the retired terms Proposal, Verify / Accept / Revoke, `deployment_unit` / `authority`, Librarian Report / Session Digest (by the decision of case 306.3; their decisions stand in the archived ledgers of 2026-09-08 and 2026-09-09).

## Terms

| term | meaning | where |
|---|---|---|
| Ratification | Human sign-off on a Decision; nothing in vault or code changes without one | [[rule-ratification]] |
| Contract vs implementation | A Decision fixes what "done" means, never how; a contract change is a new Case | [[rule-ratification]] |
| `ref`, `slug`, `supersedes` | A pointer to an existing page (absent: query the vault before a `create`; present: `update`); the page id = filename; the earlier case a ledger line corrects, written `{supersedes:case N}`, one block per Case and several on one line, each of which marks every entry of its Case and of its sub-cases superseded; `generate` clears a defer under the condition that `rule-case-protocol` sets (cases 200.2, 429, 467.3) | [[rule-case-protocol]] |
| Decision | The atomic unit of work: `create`, `update`, `delete`, `defer`; Read is never one | [[rule-case-protocol]] |
| Types | `create` a page, an Estimate being its own `create` with `ref` on its target (case 193); `update` fields, `result`/`status` included, or `rename` — the page moves to the new slug and every link follows (case 258.1); `delete` sets `status: archived` with a History line `deleted`, after an impact analysis, and `guppi cleanup` moves the file to the archive; `defer` postpones, a placeholder page when no `ref` for a rule or an entity only; an Estimate is put off through the page it would check (case 783), and a defer of any other kind with no page fails (case 786) | [[rule-case-protocol]] |
| Case | The unit of dialogue, not a page: `context`, `problem`, `recommend`, `given`, `when`, `then`, `tasks`, `ratification` (case 163); `given` is the frame of the Case; `when` + `then` is the Estimate criterion, the Estimate named by slug (cases 193, 378.2); the page content is a `then` block in the Spec; splits into dotted sub-cases, each ratified on its own as `rule-ratification` sets | [[rule-case-protocol]] |
| Main agent, Subagent | Runs Cases and writes ledger lines, the last of them in the one reply that ends Retro, after its commit (case 531.8); executes plan tasks, never decides, a fork returns | [[rule-ratification]] |
| Plan Mode | The Frontier worked item by item: an item that needs a decision is a Case until it is ratified or deferred, an item that needs none closes with no Case, an item of the sprint may be left for later and a backlog item kept as it stands; it ends when no item of the Cases list is open (cases 356.1, 356.2, 421.4, 451.1) | [[rule-orchestration]] |
| the vault query | The vault query before a `create` without `ref`, `draft` pages included (case 277.3) | [[rule-ask]] |
| Index line, `ask-guppi` | The Grep of a category's frontmatter — `purpose`, `root_cause` or `pattern`, and `deferred_by` — one line per live page, never compared across categories; no index file (case 147.8); the search agent over these lines, one entry point; Estimates through the target, Decisions through `deferred_by`; the archive answered by slug alone — `free`, `live` or `archived at <path>` — never by meaning (case 105.1) | [[rule-ask]] |
| `/pre-spec` | The check of the ratified set against each other and the vault before the Spec is approved (case 261) | [[rule-prespec]] |
| Spec | The ratified Cases as one document, approved as Claude Code's plan, copied to `raw/<date>/<hi HHMM>/spec.md`, the session's folder (case 73.1) | [[rule-spec-capture]] |
| Vault | `vault/wiki/`: one folder per page category, each page a file named by its slug | [[rule-vault-layout]] |
| Entity fields | `type` the category; `purpose` one line, from which the index line is built; `children` on a MOC; `estimates` on a Leaf its own checks, on a MOC the cross-cutting ones; `code_ref` paths to code, on either kind | [[rule-entities-schema]] |
| Rule fields | `purpose` one line, what the rule prevents; `enforcement` `hook`, `check` or `render`; `implementation_ref` on `hook` and `check`; `governs` and `render_mode` on `render`; `children` ordered, on a MOC; `estimates` that the rule does what it claims | [[rule-rules-schema]] |
| Estimate fields | `method` required, how the promise is checked; `purpose` the promise in one line; `checked` the date of the last reading, written by `generate`; the sections `Criterion` and `Result` | [[rule-estimates-schema]] |
| Lesson fields | `root_cause` one line, what clustering compares; `source` on a `knowledge` lesson, where the material came from; the sections `Trigger` and `Root cause` | [[rule-lessons-schema]] |
| Insight fields | `pattern` one line, the shared root cause; `children` the Lessons clustered; `severity` the count of children not archived, computed by `generate`; `addressed_by` the one decision that actioned it | [[rule-insights-schema]] |
| Atomicity Rule | A unit splits when its closing judgment breaks into parts that fail and are fixed apart | [[rule-atomicity]] |
| MOC | A thing whose parts the person named as things that are built; `children` lists them; its Estimates measure what no child owns; a part comes from the person's words through a Case — the agent proposes a cut, never makes it (case 240.1) | [[rule-entities-schema]] |
| Leaf | A thing whose parts the person has not named; holds `estimates` — empty is legal, the person said nothing yet — and a code pointer; its inner workings are `## How it works`, not pages (case 240.1) | [[rule-entities-schema]] |
| Entity | A thing the developer builds, a noun the person named as part of what is built; the check before a `create`: who makes it — the developer → an Entity; the product's user or the running product → data, outside the vault; MOC or Leaf; never a page for a "why", that is a Decision (case 240.1) | [[rule-entities-schema]] |
| Rule | A standing condition one case can break, with a guard that refuses that case when it occurs; the check: can one case refute it, and is there something to refuse it; a Leaf a condition on each case, a MOC a sequence whose Estimate promises the order; of the harness or of an Entity; force by `hook`, `check` or `render`; in the harness a thing is a Rule when its code is a guard, an Entity when it is measured and its guard is a separate Rule (case 240.2) | [[rule-rules-schema]] |
| Estimate | The evidence: on a Rule a test that the guard works, on an Entity a reading of the whole no single case can break — the target's prefix says which; `QA` the answer is known, `Research` the reading finds it, on an Entity only, `failed` when the finding does not serve the purpose (case 240.3); one promise, one way to check it, the last result with its date (case 182); its own Leaf page under an Entity or Rule only, an explicit `create` with its slug in the Case, `estimate-<target minus its prefix>-<promise>`; fields `purpose`, `method`, `checked`; `QA` checks a known criterion, `Research` finds out; its Criterion is the `when` and `then` of one Case, replaced whole by the `update` that names it, which alone sets `pending`; no index, reached through the target's `estimates` (case 193) | [[rule-estimates-schema]] |
| Estimate (status) | `pending` / `passed` / `failed`; `failed` is debt, archival the default outcome | [[rule-estimates-schema]] |
| Lesson | Something learned; a fact the hook writes, no Case, no Estimate; slug = area + cause; a `knowledge` claim is checked by the Rule that leans on it | [[rule-lessons-schema]] |
| Insight | Over Lessons sharing a root cause, made by the librarian on the second; stands in `backlog.md` while `open` and is the target of the `update` that actions or rejects it, or of a `defer`; never created or deleted by a Decision; `actioned` reopens (case 124) | [[rule-insights-schema]] |
| Decision page | One page per Case in `wiki/decisions/`, slug `decision-case-<N>`, one list per kind present: `create`, `update`, `delete`, `defer`; body `## Problem` and `## Recommend`, `## Deferred` for a Case that put something off, and `## History`; a Case with sub-cases has a page of its own with `## Problem`, `## Recommend` and `children`, and the page of a sub-case carries `parent`, its own `## Recommend` when it has one, and no `## Problem` (case 544.8); `## Context` only for a Case without `given` and without sub-cases, such as the short form of a deferred decision, and in the two-line body of a Case superseded in its own session (case 299.4), never `## Given`; the whole Case, `recommend` included, stays in its Case file `cases/case-<N>.md` in the folder of `origin`; an older page keeps its Context and Given (one written before case 513, case 513); never indexed, reached through `deferred_by`, a History wikilink or `origin` | [[rule-decisions-schema]] |
| Lint | `guppi lint`, run by `make lint` after the render, sprint, backlog and glossary checks: reports a page that breaks its schema, points at nothing, claims a status its Estimates do not support, or waits for a reading; red is a signal, not a gate | [[rule-lint]] |
| Renderer | `guppi render` writes the text of a Rule page into the harness file it governs, so the page stays the source; it runs with lint and as the librarian's step after `cleanup` | [[rule-render-harness]] |
| Harness | The files that `guppi render` writes from the pages of `rules/`, such as `.claude/settings.json` with its hooks, the skills and agents, `CLAUDE.md`, `case-schema.md` and `guppi.toml` | [[rule-harness]] |
| Hook | A script that fires on an event of the session, behind a Rule page; registered in the `hooks` key of `.claude/settings.json`, which `rule-hook-registry` renders, or in an agent's own frontmatter as part of that agent's Render; a new hook in the file is an `update` of `rule-hook-registry` in the Case that creates its Rule | [[rule-hook-registry]] |
| `CLAUDE.md`, `case-schema.md` | The system prompt, the Render of `rule-claude-md`, whole — the description of the project, `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation` in their markers (cases 59.8, 272, 288.3, 360); the Case schema is the Render of `rule-case-protocol`, read by `case-guppi` alone; `/hi` loads, together with the glossary, `orchestration.md`, the Render of `rule-orchestration`, and `ratification.md`, the Render of `rule-ratification`, which the one rule opens (cases 273, 288, 595) | [[rule-claude-md]] |
| `deferred_by` | The Decision pages whose `defer` targets the page; written by `guppi generate` on a defer and cleared by it on a later `supersedes` of that one, under the condition that `rule-case-protocol` sets; the index line of a rule, an entity or an Insight carries it, so `ask-guppi` reaches the deferred decision (case 52.3); an Estimate carries it too but has no index line, and `backlog.md` lists a deferred one (case 781) | [[rule-rules-schema]] |
| `origin` | On a page a Case created: where that Case was ratified, `raw/<date>/<HHMM>/ledger.md#case-N` — the date form `raw/<date>/ledger.md#case-N` on pages born before 2026-09-13 (case 103.6); the folder holds the Spec with the Case and, for a Case built by `case-guppi`, its Case file (from session 2026-09-27/1819 on, case 513); the pointer is not rewritten when the session is archived (cases 100.1, 103.6) | [[rule-decisions-schema]] |
| Entity (status) | `draft` / `built` / `archived`; `built` is set by the cascade of `generate` once every Estimate passes, never by hand | [[rule-entities-schema]] |
| Rule (status) | `draft` / `built` / `archived`; `built` is set by the cascade of `generate` once every Estimate passes, never by hand | [[rule-rules-schema]] |
| Decision (status) | `current` / `superseded` / `archived`; `superseded` once a later Case names it, or the page of a Case it is a sub-case of, in `supersedes`, `archived` when the cascade of `generate` then meets it; a page already `archived` stays `archived` when a later Case names it | [[rule-decisions-schema]] |
| Lesson (status) | `new` / `clustered` / `archived`; `clustered` once it belongs to an Insight, `archived` when its Insight is `actioned` | [[rule-lessons-schema]] |
| Insight (status) | `open` / `actioned` / `archived`; `actioned` when a ratified decision addressed it; a new Lesson of the same root cause reopens it unless its entry carries `addressed_by`, the mark of a decision of its own session that closed its cause (case 284.4); an Insight that a decision of the Lesson's own session sets `actioned`, in the same `materialize.yaml`, counts as `actioned` for that Lesson (case 668); `archived` when the cascade finds an `open` Insight with no live child | [[rule-insights-schema]] |
| `archived` | Set by `delete`, or by the cascade of `guppi generate` — a superseded Decision, the lessons of an actioned Insight, an open Insight with no live child (case 104); `guppi cleanup` moves the file to `vault/archive/<sprint>/<date>/<HHMM>/<category>/` and brings it back on an `update` of `status`; `guppi archive` moves an applied session of `raw/` whole (case 100.1); never physical deletion | [[rule-cleanup]] |
| Routing Table | (type × `ref` × category) to vault action, mechanical | [[rule-materialize]] |
| Sprint | An Entity Leaf `entity-sprint-<id>` under the MOC `entity-sprint`, the sprint as a kind (case 241), whose Estimates are the Definition of done, whose `## Milestones` holds the Slices in order — the first with an open item is current — and whose `## Backlog` the items without a turn, each a wikilink or a plain line; `sprint.md` is its render, written by `guppi sprint` with one tick per item by the statuses of every page its `[[slug]]` before the first ` — ` names, a line without one a note that never ticks, the current milestone whole and the others one line (cases 209, 229); `/hi` takes the Frontier from the current milestone only | [[rule-sprint]] |
| `brief.md` | The handover between sessions, written by the librarian or by `/carry`, which conserves a Spec (case 200.2); no Deferred list — the deferred items stand in `backlog.md` (case 451.8) | [[rule-brief]] |
| `backlog.md` | Every deferred item in one file, written by `guppi backlog`: the conserved Specs with their targets, then each page with `deferred_by`, each open Insight and each line of the sprint page's `## Backlog`, with its `purpose` or `pattern` and the count of the sessions that put it off; `/hi` loads it, writes its count and names the items near a Frontier item (case 451.4) | [[rule-backlog]] |
| Working files | `log.md`, the feed of page changes written by `generate` and `cleanup`; `tags.md`, the registry of tags ratified in a Case; `raw/` and `archive/`, the working folders of a session | [[rule-vault-layout]] |
| `raw/` | One folder per session, `raw/<date>/<HHMM>/`, with its `ledger.md` and `materialize.yaml`; `guppi archive` moves it whole to `vault/archive/<sprint>/<date>/<HHMM>/raw/` once every entry is applied; `event_log.md` stays in `raw/<date>/` | [[rule-raw-archive]] |
| Documentation | The librarian's phase, the agent `librarian-guppi`: materialize, index check, synthesis, generate, cleanup, brief, close | [[rule-documentation]] |
| Librarian | Clean context; the only writer to `wiki/` but for what a merge of `main` by `/merge-main` writes: the joined text of a conflicted page, and the lines of `log.md` and `tags.md` that git joins (case 790); reads handoff, yaml, indexes; one judgment, `create` to `update` on a duplicate; flags the rest | [[rule-documentation]] |
| Session | Five phases in one order under [[rule-session]]: Session Start, Plan Mode, Work Mode, End of Work, Documentation | [[rule-session]] |
| `/hi`, Frontier | Opens a working session and records `hi`; the open items it assembles (brief, sprint, backlog, an unfinished plan, the ledger tail) in three lists, the kind of each by its source — Cases, the Plan Mode agenda; Work, what needs no decision; and Ask, the readings only the person can answer (cases 268.2, 531.11) | [[rule-skill-hi]] |
| Ledger | The record of decisions (routing only), estimates and lessons (with text), written by the `Stop` hook into `raw/<date>/<HHMM>/ledger.md`, the session's folder (case 103.1) | [[rule-ledger-write]] |
| Event log | The gitignored log of tool calls and commits of the day, written by hooks | [[rule-event-log]] |
| Work Mode | `/work` runs the approved Spec on a branch other than `main`: a baseline of `make test` and `make lint` first, the tasks in the order of the Spec, each box ticked, then the Work readings; it ends with `/retro` | [[rule-work-mode]] |
| Retro | `/retro`: an analysis of this session only, called by `/work` in the same turn with no stop for the person — the readings and the lessons in one reply, a commit on green, then `/handoff`, whose `handoff.md` is its report; it writes no short defer, which stands only at the close of Plan Mode, under `## Deferred` in the Spec; edits only finish ratified work; red tests are fixed or reverted into a patch in `raw/` | [[rule-retro]] |
| Handoff | `/handoff`, gated by `guppi gate` on a dirty tree: `handoff.md` from memory, then the librarian | [[rule-handoff]] |

## History

- 2026-09-22 created · [[decision-case-306.3]]
- 2026-09-22 updated: the term Atomicity Rule is defined by rule-atomicity (case 317) · [[decision-case-317]]
- 2026-09-22 updated: index.md out of the two rows that named it (case 318) · [[decision-case-318]]
- 2026-09-22 updated: the term Rule-class files retired with its thing; the map leaves the CLAUDE.md row (case 321) · [[decision-case-321]]
- 2026-09-22 updated: the rows Sprint and Session by cases 313 and 316 (case 323) · [[decision-case-323]]
- 2026-09-22 status: draft → built · cascade
- 2026-09-22 rules: [rule-glossary] · cascade
- 2026-09-23 updated: the Criterion is when and then (case 378.2) · [[decision-case-378.2]]
- 2026-09-23 updated: the body of a decision page (case 378.3) · [[decision-case-378.3]]
- 2026-09-25 updated: the term supersedes: one block per Case, several on one line (case 429) · [[decision-case-429]]
- 2026-09-27 updated: the term backlog.md added; the brief without a Deferred list, an open Insight in the backlog, the backlog among the sources of the Frontier (case 451.4) · [[decision-case-451.4]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 updated: each row points at the page that defines its term: Plan Mode, the fields and statuses by category, the Decision page by its schema after case 513, lint and the renderer for Scripts, the working files and raw/, Work Mode without subagents; Executable plan leaves until it is decided (case 515) · [[decision-case-515]]
- 2026-09-29 updated: the rows Vault, Hook, deferred_by and origin point at the page that defines each, their meanings cut to it; Entity / Rule (status) splits into Entity (status) and Rule (status) (case 520) · [[decision-case-520]]
- 2026-09-30 updated: the row Harness defines the harness as the files guppi render writes from rules/; the row Retro puts the short defer under ## Deferred, as case-schema.md does (case 527.1) · [[decision-case-527.1]]
- 2026-09-30 updated: the row Issue removed: rule-github-issues left the harness with the remote (case 528.2) · [[decision-case-528.2]]
- 2026-09-30 updated: the row Retro: no frontier and no short defer; one reply of lines, a commit on green, then /handoff (case 531.1) · [[decision-case-531.1]]
- 2026-09-30 updated: the row /hi, Frontier: no issues, three lists with Ask (case 531.11) · [[decision-case-531.11]]
- 2026-09-30 updated: the rows Decision page, Main agent, Plan Mode, Types and CLAUDE.md agree with the pages that define them (case 535) · [[decision-case-535]]
- 2026-09-30 updated: the row ref, slug, supersedes: a supersede clears a defer only from the pages the superseding Case names (case 541) · [[decision-case-541]]
- 2026-09-30 updated: the row Decision page names Recommend and the pages of a parent and a sub-case (case 544.8) · [[decision-case-544.8]]
- 2026-09-30 updated: the rows deferred_by and ref, slug, supersedes: a supersede clears a defer under the condition that rule-case-protocol sets (case 549) · [[decision-case-549]]
- 2026-09-30 status: draft → built · cascade
- 2026-10-02 updated: the rows Ratification, Contract vs implementation, Main agent and Plan Mode point to rule-ratification and rule-orchestration; the row Case says each sub-case is ratified on its own; the row of case-schema.md says what /hi loads (case 595.20) · [[decision-case-595.20]]
- 2026-10-05 updated: the row of supersedes: a tag marks the sub-cases too (case 660.2) · [[decision-case-660.2]]
- 2026-10-05 updated: the row of the status of a Decision: the page of a sub-case is superseded with its parent (case 660.3) · [[decision-case-660.3]]
- 2026-10-05 updated: the row of the status of an Insight names the mark and the status a decision of the lesson's own session sets (case 668) · [[decision-case-668]]
- 2026-10-06 updated: the row Decision (status): a page already archived stays archived when a later Case supersedes it (case 683) · [[decision-case-683]]
- 2026-10-12 updated: deferred_by: an Estimate may carry it, and backlog.md lists a deferred one (case 781) · [[decision-case-781.7]]
- 2026-10-12 updated: Types: a defer writes no placeholder for an Estimate (case 783) · [[decision-case-783.1]]
- 2026-10-13 updated: Types: a defer writes a placeholder only for a rule or an entity (case 786) · [[decision-case-786.1]]
- 2026-10-13 updated: Librarian: the only writer to wiki/ but for what a merge of main by /merge-main writes (case 790) · [[decision-case-790]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: each pointer stands in a bracket of its own, a definition outside it · [[decision-case-809]]
