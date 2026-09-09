# Glossary

Complete vocabulary for the vault methodology. Every term used in the system, with its precise meaning.

---

## Core principle

**Ratification** — explicit human sign-off on a Decision. Nothing in the vault or the codebase may change without a Decision that a human has ratified. This is the foundational rule the entire methodology exists to enforce.

**Contract vs implementation** — a Decision governs the *contract* (what "done" means, what the acceptance criteria are), never the implementation directly. Between two ratification points the agent has full autonomy over how it writes code. If the contract itself must change mid-build, that is a new case and a new Decision, never a silent deviation.

**Universal Atomicity Rule** — the single rule that governs splitting for every unit type in the system:

> A unit stays whole as long as its closing act (ratification / verification / "built") is a single, indivisible judgment. The moment it decomposes into ≥2 conditions that can fail independently and need different fixes — split into separate children.

---

## Structural vocabulary

**Vault** — the knowledge base itself: a folder of plain Markdown pages, human-readable and agent-readable, holding every Entity, Rule, Estimate, Lesson and Insight.

**MOC** (Map of Content) — a page that has no direct acceptance criteria of its own. Its `children` field lists refs to child pages. Applies to Entity, Rule and Insight.

**Leaf** — a page with direct, checkable behavior of its own. Holds its own `estimates` and its implementation pointer (`code_ref` / `hook_ref`).

**Recursion** — MOC pages may contain MOC children to arbitrary depth. Depth is never fixed in advance; it is determined by repeatedly applying the Universal Atomicity Rule.

**C4 model** — an external architecture-modelling convention (Context/Container/Component/Code). Deliberately *not* adopted as a level hierarchy. Only one idea is borrowed, asked once when a brand-new top-level Entity is born: is this a new deployment unit (new service/container, with real infrastructure consequences), or a feature inside something that already exists? The answer surfaces as content in that Entity's `estimates` (infrastructure criteria), never as a separate field.

---

## Page categories

**Entity** — a terminal page category: the thing that gets built. May be MOC or Leaf. Leaf Entities carry `code_ref`.

**Rule** — a terminal page category: a hook governing *how the work happens* (blocking a commit, enforcing a workflow step, formatting). Structurally identical to Entity, with `hook_ref` instead of `code_ref`. Requires an Estimate for the same reason Entity does — a broken hook breaks the workflow just as thoroughly as broken product code.

**Estimate** — the verification artifact: how a piece of behavior was checked and what the outcome was. Always a standalone Leaf page — never inline, never composite. Two types:
- **QA** — the expected result is known in advance, defined by an existing requirement. Verification is a check against an already-stated criterion.

A `failed` Estimate is debt, not an endpoint: its Entity stays `draft` and the librarian surfaces it in `brief.md` until a human decides. Absent a decision to fix, the default is archival.
- **Research** — the result is not known in advance. Verifying requires investigation, and the process produces new content (hypotheses, findings) that did not exist before.

**Lesson** — a page in `wiki/lessons/` recording something learned, `kind` `error` or `knowledge`. Always flat. A recorded fact, not a ratified decision: the ledger hook writes it directly, no Case required. Slug is **area + cause** (`lesson-hooks-sessionstart-cannot-block`), so the area groups related lessons in a file listing and the cause makes near-duplicates visible before opening the index.
- **error** — something went wrong. Self-verifying: it was observed, so its Estimate is created already `passed` and archived immediately, purely as a record that this was checked.
- **knowledge** — external material (an article, another team's solution, a worked example) read once and captured so the source never needs to be supplied again. Its Estimate is Research-type and **must reach `passed`** before an Insight may build on it.

**Insight** — its own page type in `wiki/insights/`, **not** a kind of Lesson: it shares no content fields with one (no `trigger`, `root_cause`, `source` or Estimate; instead `pattern`, `children`, `severity`, `addressed_by`). "A MOC over Lessons" describes a relationship, not an identity — Estimates belong to Entities without being a kind of Entity. Created by the librarian on the second Lesson sharing a root cause, archive included. Never the target of a Decision: it reaches the human through `brief.md` and becomes an ordinary ratified Case. `actioned` is not terminal — a new matching Lesson reopens it, archived children stay archived, and `severity` counts only the current run.

**Issue** — an item tracked in an external system (GitHub). Never becomes a vault page; referenced via `ref` only, since the external system is already its source of truth.

---

## Fields

**`type`** — `MOC | Leaf` for Entity/Rule; `QA | Research` for Estimate; `error | knowledge` for Lesson.

**`purpose`** — why this page exists.

**`children`** — list of refs to child pages. MOC only.

**`estimates`** — list of refs to Estimate pages. Present on both MOC and Leaf: on a MOC it covers cross-cutting/non-functional checks that belong to no single child; on a Leaf it covers that page's own behavior.

**`origin`** — a ref back to the Decision or Case that created (or deleted) this page. Preserved on archived pages so the reasoning survives archiving.

**`code_ref`** — pointer(s) to code, commits or PRs. Entity Leaf only.

**`hook_ref`** — pointer(s) to a hook implementation. Rule Leaf only.

**`criterion` / `method` / `result`** — Estimate fields: what is being checked, how, and the outcome.

**`trigger`** — Lesson field: what happened (error) or what was read (knowledge).

**`root_cause`** — Lesson field: why it happened (error) or the mechanism the source claims (knowledge).

**`source`** — on a Lesson: the external link. In a ledger line: the external origin (e.g. a GitHub issue number), recorded for traceability only and never affecting routing.

**`severity`** — Insight field. Computed as the count of children whose status is not `archived`. Rises as the same pattern recurs.

**`addressed_by`** — Insight field: ref to the Decision that fixed the pattern.

**`ref`** — a pointer to an existing, explicit vault page, supplied via the brief or a pre-check. Its presence or absence drives routing: no ref means a potential `create` (query the vault first); a ref present means go straight to `update`.

**`slug`** — in a ledger line, the id of the affected page.

**`supersedes`** — in a ledger line, marks a retroactive correction pointing at the earlier case being overridden.

**`status`** — see the state models below.

---

## Status models

**Entity / Rule** — `draft` / `built` / `archived`. Flat, like every other category. `built` is computed by lint once all Estimates pass, never set by hand.

**Decision** — `current` / `superseded` / `archived`.

**Lesson** — `new` / `clustered` / `archived`.

**Insight** — `open` / `actioned` / `archived`. `actioned` is not terminal.

**Estimate** — `pending` / `passed` / `failed`.

**Lesson** — `new` → `reviewed` → `actioned`.

**Insight** — `open` ⇄ `actioned`. Not terminal: a new Lesson sharing the same root cause reopens it.

**`archived`** — set by the librarian once a page (or its parent) is `actioned`; a cleanup script then moves the file to `wiki/archive/`. Applies to every category. Archived pages remain addressable by `ref`.

**`deleted`** — the marker set by a `delete` Decision. Never a physical deletion; the librarian archives it. Restoring is an ordinary `update` back to `current`.

---

## Decision vocabulary

**Decision** — the atomic unit of work. Two families only.

**CRUD (no Read)** — Read happens automatically via hooks and instructions, never as a ratified Decision.
- **Create** — spawns a new page. Creating a Leaf Entity or Rule requires the session agent to log a paired `create` for its Estimate in the same ratified case.
- **Update** — modifies an existing page's fields, including setting an Estimate's `result`/`status`.
- **Delete** — sets `status: deleted`; the librarian archives. No dedicated Estimate page: the agent queries the vault for what depends on the target, states the impact in the case's `recommend`/`then`, and the human ratifies with that analysis in hand.

**Defer** — postpone something not started, or pause something in progress. With a `ref` to something already tracked: logged only, resurfaces via the next Frontier. Without a `ref`: the librarian materializes a minimal placeholder page.

**Delegate** — the agent deciding autonomously, without ratification. Considered and rejected; risks reopening the exact hole the system exists to close. Parked, not permanently ruled out.

**Routing Table** — the mapping (Decision type × presence of `ref` × target category) → resulting vault action. The mechanical rule the librarian applies; it never invents a decision that isn't in the ledger.

---

## Session vocabulary

**Session** — one working cycle: Session Start → Plan Mode → Work Mode → End of Session.

**Session Start hook** — fires at session start: loads `brief.md`, runs `git pull`, applies the optional Enterprise admin gate, sets sprint context, and assembles the Frontier.

**Frontier** — the auto-assembled list of open items at session start, built from `brief.md` + sprint + GitHub issues. The agenda for Plan Mode.

**Sprint** — a time-limited backlog providing the session's scope context.

**`brief.md`** — the handover note between sessions, written by the librarian. **Deferred items are capped at 7** — it is a shop window, not storage: everything deferred lives on as a `draft` page and is found by pre-task regardless. Ranking is by the `severity` of any related Insight, then by how many times an item has already been postponed. Librarian flags and notes have no cap; they are not competing for the same space.

**Case** — the unit of dialogue (roughly one agent response = one case). Not a vault page; exists only inside a session. Fields: `context` / `now` / `problem` / `recommend` / `then` / `ratification`.
- **`context`** — short introduction to what this is about. Never omitted, but in Work Mode it may shrink to a back-reference to an earlier case.
- **`now`** — how things work today, including any `ref` found by a pre-check.
- **`problem`** — what actually requires a decision.
- **`recommend`** — the agent's suggested course of action.
- **`then`** — what happens if the recommendation is accepted. Holds the page draft itself, structured per the page schema, so the human ratifies content rather than intent.
- **`ratification`** — the human's sign-off, question, or alternative.

**Sub-case** — a child case produced when the Atomicity Rule splits a case. Recursive dotted ids (1.1, 1.1.1...). Ratifying a parent does not ratify its children. A follow-up question that merely justifies an existing choice does not split a case; one that itself requires a new choice does.

**Pre-check** (pre-task) — the vault query the agent must run before a `create` when no `ref` is present. Not a name lookup: it asks whether this already exists, whether there are similar cases, what might obstruct the work, and what contradicts the plan — Estimates included, since a `create` spawns one and an identical check may already exist elsewhere. **Must include `draft` pages**: everything ever deferred lives on as one, whether or not it reached the capped `brief.md`. Skipping them means re-deciding something already decided and leaving the original `defer` as dead weight. Distinct from the librarian's duplicate search, which happens later and works from finished content rather than intent.

**Plan Mode** — the phase where Frontier items are discussed as cases until all are ratified or deferred.

**Ledger** (`ledger.md`) — the mechanical, chronological record, carrying two kinds of line. **Decisions** are routing only — their content already sits ratified in `spec.md`, so the line just names what happens to which page. **Estimates and lessons carry text**, because their content is born in the moment and exists nowhere else: a measurement taken after the tests were written, a failure understood while still fresh. An `estimate[...]` line does not replace the `decision[...]` that created the page — the decision made it exist, the estimate line fills it. A hook active for the whole session listens for the decision pattern in chat and writes it verbatim, with no interpretation. Created lazily on the first ratified decision, not at session start. Committed to git, because page `origin` fields point at its lines. Ledger line format:
```
- decision[case_id][type][slug]{ref:parent_or_target}{source:external_id}
```

**Event log** (`event_log.md`) — the separate, noisy record of tool calls, agent dispatches, commits and test runs. Fed by hooks, never by instructions inside a skill, so it still fires when the agent deviates or crashes. Gitignored: it is debugging material, not traceability.

**Spec** — the output of Plan Mode: all ratified Cases collected into one readable document the human reviews as a whole and approves in a single act. Always derived from the ledger, never the reverse — disagreement produces a new Case with `supersedes`, and the Spec is rebuilt.

**Executable plan** (`plan.md`) — the Spec broken into tasks: complete code (tests first), exact paths, checkboxes, parallelization markers. Produced after Spec approval, once the branch exists. Handed to subagents, who transcribe rather than invent.

**Work Mode** — the implementation phase. Subagents execute against the executable plan and check off tasks. Contract changes and Estimate validations arising here go through the same Decision routing and the same ledger.

**Retro** — the end-of-session review. Examines only what already happened in this session; it never expands scope. Code edits are allowed when they finish or correct work already ratified in this session's ledger, and forbidden when they add new scope — the test is mechanical, check the ledger rather than arguing over what counts as "new code". Every edit is still an ordinary ratified Case. Bugs become `lesson[error]`; deferred ones must also open a GitHub issue, whose number goes in the line's `source`. Harness tests run in the background; Handoff still requires green. Ends with a commit — the clean baseline before the librarian writes anything.

**Handoff** — the handover point, deliberately thin. `handoff.md` carries three things, none of them decisions: notes from memory (hesitations, unclear points, caveats), direct instructions to the librarian ("check X first", "this may duplicate Y"), and **what actually got done** — which Cases closed and where the code landed, which exists in neither the ledger nor the Spec and fills `code_ref`. The main agent does not re-read the artifacts to write it — that would spend the context advantage that is the note's only reason to exist. Short or empty is a normal outcome.

**`materialize.yaml`** — the action list for the page-generation script, assembled **by script** from ledger lines + routing table + ratified content in `spec.md`. Mechanical, because the fields were laid out per schema back in the Case's `then`. This is what the librarian reads instead of the raw artifacts.

**Decision page** — every ratified decision is a page in `wiki/decisions/`, with a meaningful slug (`decision-create-cart`). Not indexed and not archived on completion: nothing scans decisions, so they cost nothing to leave in place, and one stays valid as long as the page it created. It leaves the live vault only when superseded, or by cascade when its target is archived.

**Index** (`wiki/<category>.index`) — one generated line per live page, `slug: purpose`; for lessons, `slug: root_cause`. Regenerated by lint, never hand-edited. Makes semantic checks affordable: hundreds of pages are a few thousand tokens read in one pass, so no embeddings are needed until the index itself stops fitting in context. **Per-category, and comparison never crosses categories** — an Estimate and an Entity sharing a purpose is normal division of labour, not duplication.

**`/ask`** — the search mechanism over the indexes. One tool, two moments: pre-task queries by intent before a decision exists; the librarian queries by finished content after.

**Documentation** — the librarian's phase: routing table → page generation → tags → statuses → synthesis (Insights, duplicates, stale defers) → flags into `brief.md` → `brief.md` and `sprint.md` → **lint and cleanup, after all judgment** → commit → control back to the main agent. A lint failure nothing can fix mechanically is flagged, not a blocker; the session still closes.

---

## Agents and machinery

**Main agent** (session agent) — the agent in the conversation. Runs Cases, proposes decisions, writes ledger lines, decides Estimate creation while context is fresh. Its job ends at the Retro commit; the librarian takes over from Handoff, and the main agent returns only for the closing check.

**Subagent** — executes discrete tasks from the executable plan during Work Mode. Has no authority to decide and never writes to the ledger: on hitting a fork it stops and returns to the main agent, who raises an ordinary Case.

**Librarian** — runs every session, from Handoff onward, in a **clean context**: it reads `handoff.md`, `ledger.md`, `spec.md`, `plan.md` and the schemas, nothing else. **The only actor that writes to `wiki/`** — a rule that is checkable, since the vault should only ever change through the scripts it invokes. **Reads only** `handoff.md`, `materialize.yaml` and the category indexes — not `ledger.md`, `spec.md`, `plan.md` or the pages, since the yaml is script-assembled and already carries every `purpose`, `criterion` and tag. **Does three things:** checks new pages against the indexes, synthesizes Lessons, writes the brief. Statuses, backlinks and cascading status resolution are script and lint work, not its own. **Acts on exactly one judgment:** turning a `create` into an `update` when the indexes reveal a duplicate, before generation runs. Flags everything else — MOC candidates, over-broad MOCs, stale defers, `failed` Estimates, contradictions. Its actions are marked `librarian:` in `History`. It never authors content, never rewrites ratified content, never restructures, never invents semantic links, never edits Rule-class files, never stops to ask, and never does lint's work.

**Page-generation script** — creates the page files from the handoff action list. Fills the mechanically derivable fields (`origin`, `slug`, `status`); the judgment fields (`type`, `purpose`, `criterion`, `method`) come from the ratified Case.

**Cleanup script** — moves pages marked `archived` into `wiki/archive/`.

**Lint scripts** — mechanical vault integrity checks: broken refs, schema conformance, status contradictions, orphans, and **cascading statuses** (an Entity is `built` only once all its Estimates pass — a graph property, not derivable line by line). Also regenerate the indexes. Run **after** all the librarian's judgment, so they see the final state of the graph. A page created incomplete will fail lint — correctly: red lint is an accurate signal of outstanding debt, and is better than a ratified decision with no page at all.

**`log.md`** — the global feed of every page change, written by a hook rather than by an agent following an instruction, so it still fires when the agent deviates or crashes.

**`History`** — always the last section of a page. A hook appends one line per change, making a page's recent history readable with `tail` without loading the page or `log.md` into context. `log.md` is the global view; `History` is the per-page one.

**`raw/`** — where session artifacts land: `ledger.md`, `event_log.md`, `spec.md`, `plan.md`, `handoff.md`, one folder per date. Separate from `wiki/`, which holds only materialized pages.

**`tags.md`** — the registry of tags in use. Tags are chosen during pre-task, which returns relevant existing tags alongside its other findings; they go into the Case's `then` and are ratified with everything else. A genuinely new tag is proposed explicitly so the human signs it. The librarian only registers what is already ratified — which is why the registry cannot grow uncontrolled.

**`sprint.md`** — current sprint scope, updated by the librarian at the end of each session.

**`schema.yaml`** — one per page category, at `wiki/<category>/schema.yaml`. Defines that category's required fields. Rule-class content.

**Rule-class files** — `index.md`, `glossary.md` and every `schema.yaml`. They govern how the system behaves, so changing one is a decision: a ratified `decision update` that goes through the ledger, lands in `materialize.yaml`, and is applied by script. Never edited as a side effect of session work, never by an agent tidying up. Distinct from registries (`tags.md` — written during the session, but only recording what a Case already ratified) and generated files (`<category>.index`, `log.md`, page `History` — rebuilt or appended mechanically, never edited).

**Harness** — the operational layer rendered from `rules/` pages: hooks, dynamic instructions, agents, skills. What makes the system able to improve itself.

**Hook** — an event-triggered script. Used for the ledger writer, the event log, pre-plan checks. Each hook is implemented behind a Rule page. `SessionStart` cannot block (exit 2 is a no-op there); gating belongs on `PreToolUse`.

**`CLAUDE.md`** — read automatically at session start and placed in the system prompt. Uses `@path` import syntax to expand `glossary.md` inline, so terminology is available without a read-tool call. Also carries a short pointer to `index.md`'s sections — the file itself is too large to import.

**`@import`** — the `@path/to/file` syntax in `CLAUDE.md` that expands a file's contents inline at load time. Distinct from an instruction to "read this file," which the agent has no trigger to execute at session start.

**`index.md`** — the vault's map: routing table, archival rules, where things live and what to do with them. Rule-class content — changes only through a ratified `decision update`. Not loaded wholesale into context; `CLAUDE.md` carries a short pointer to its sections so the agent can grep the one it needs.

**`glossary.md`** — this document, in its vault-resident form.

**`/hi`** — the command that starts a working session. Bash substitutions in its body resolve branch, `brief.md`, sprint and open issues before the agent sees anything, so no read-tool calls are needed. Without `/hi` the session is an ordinary one: nothing is loaded and no governance applies.

---

## Retired terms

Present in the existing vault and in earlier drafts; must not be reintroduced.

**Proposal** — formerly a page category ("specification + plan"). Dissolved: its two jobs are now covered by a parent Entity's own structure and by the session Spec. What was a Proposal is simply an Entity with `status: draft`.

**Verify** — formerly a Decision type. Dissolved into `create` + a ref to a new Estimate page.

**Accept** — formerly a Decision type. Dissolved into `update` setting a field (`result`, `status`) on the target page.

**Revoke** — formerly a Decision type conflating "cancelled", "stopped" and "paused". Cancellation is `delete`; pausing is `defer`.

**Delegate** — see above. Parked, never adopted.

**`deployment_unit`** — a proposed Entity field, removed: nothing downstream consumed it.

**`authority`** — formerly a slug grouping several pages together. Dissolved: grouping is what a MOC's `children` already does, and page identity is the filename. Tag registration survives separately as `tags.md`.

**Librarian Report** — formerly a separate artifact. Its content is now lint output plus a section in `brief.md`.

**Session Digest** — earlier name for what is now `ledger.md`, before the decision record and the event record were split apart.
