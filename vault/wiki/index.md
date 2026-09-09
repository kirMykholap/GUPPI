# index.md — Operating Rules

Imperative instructions for the agent. These are the permanent rules of the system. Read `glossary.md` for terminology.

---

## 0. The one rule everything else serves

Nothing in the vault or the codebase changes without a Decision ratified by the human.

You never act on your own judgment about *what* to build, change, or remove. You have full autonomy over *how* to implement something once its contract is ratified — and none over the contract itself.

When you are unsure whether something needs ratification: it does.

---

## 1. Vault layout

```
raw/                 session artifacts land here first
  YYYY-MM-DD/
    ledger.md        ratified decisions and lessons (committed)
    event_log.md     tool/agent events (gitignored)
    spec.md          Plan Mode output
    plan.md          executable plan
    handoff.md       the main agent's notes + direct instructions
    materialize.yaml action list for the generation script

wiki/
  decisions/         Decision pages — the journal
    schema.yaml      the machine-readable schema, read by lint
    schema.md        the same schema as prose, with examples
  entities/
    schema.yaml  schema.md
  rules/
    schema.yaml  schema.md
  estimates/
    schema.yaml  schema.md
  lessons/           kind: error | knowledge
    schema.yaml  schema.md
  insights/          clusters of Lessons sharing a root cause
    schema.yaml  schema.md
  archive/           everything archived, same subfolder structure
  entities.index     generated: slug → purpose, one line per live page
  rules.index        generated
  estimates.index    generated
  lessons.index      generated: slug → root_cause
  insights.index     generated: slug → pattern
                     (no decisions.index — see §12)
  index.md           routing table, archival rules, the map of the vault
  glossary.md        terms
  case-schema.md     Case structure — imported into CLAUDE.md
  brief.md           handover to the next session
  sprint.md          current sprint scope
  tags.md            registry of tags in use
  log.md             every page change, written mechanically by a hook
```

The filename **is** the page `slug`. No separate registry of identifiers is needed — `ref` and `origin` point at filenames, and collisions are caught by lint.

**`schema.yaml` and `schema.md` are one schema in two forms.** The yaml carries fields, required-ness, legal values and body sections, and lint reads it; the md carries the same table as prose with worked examples, for the agent writing a page. Lint checks the field table in `schema.md` against `schema.yaml`, so the two cannot drift.

Every page is Markdown with YAML frontmatter holding the fields; the body is prose for humans.

```markdown
---
type: entity
kind: Leaf
purpose: New clients receive a 0% discount
status: built
parent: entity-discount-rules
estimates: [estimate-new-client-discount]
code_ref: [src/discounts/new_client.py]
origin: raw/2026-09-05/ledger.md#case-3
sprint: 2026-Q3-s4
created: 2026-09-05
tags: [discounts, pricing]
---

Body sections vary by category — see each schema.
The last section is always History, appended by hook:
2026-09-05 created · raw/2026-09-05/ledger.md#case-3
2026-09-12 status: draft → built
```

Every page carries `type`, `status`, `origin`, `sprint`, `created` and `tags`. `status` is a flat list per category, never a nested structure.

**`History` is always the last section of a page.** A hook appends one line per change, so the recent history of any page is readable with `tail` — no need to load the page, or `log.md`, into context. `log.md` remains the global feed; `History` is the per-page view.

### System files are Rule-class

Every file that governs how the system behaves changes **only** through a ratified `decision update` — never as a side effect of session work, never by an agent tidying up. The decision goes through the ledger like any other, lands in `materialize.yaml`, and the script applies it. The librarian reads these files as reference and may flag a discrepancy, but never edits them.

| File | Class | How it changes |
|---|---|---|
| `index.md` | Rule | ratified `decision update` |
| `glossary.md` | Rule | ratified `decision update` |
| `<category>/schema.yaml`, `schema.md` | Rule | ratified `decision update` |
| `tags.md` | registry | written during the session — but only registering tags already ratified in a Case |
| `<category>.index` | generated | rebuilt by lint; never edited |
| `brief.md`, `sprint.md` | working | written by the librarian each session |
| `log.md`, page `History` | generated | appended by hook |

The distinction: **Rule-class files decide what the system does, so changing them is a decision.** Registries and generated files record what already happened, so they are written mechanically.

`brief.md`, `sprint.md`, `tags.md` and `log.md` are not pages and have no schema — lint must not check them against the page template.

A new term appearing mid-session is not an exception. If it belongs in the glossary, that is a `decision update` on `glossary.md`, ratified like anything else. The librarian may notice a term in the ledger that the glossary lacks and flag it in `brief.md` — the human decides next session.

**`log.md`** is written by a hook on every page change — never by an agent following an instruction. A hook fires even when the agent deviates or crashes, which is exactly when the log matters.

---

## 2. Case protocol

The Case is the unit of dialogue — roughly one agent response — and the only place content gets ratified. Whatever is not in a Case was signed by nobody.

**Its structure lives in `wiki/case-schema.md`**, imported into `CLAUDE.md` so it is present from the first turn. Six sections: `context`, `now`, `problem`, `recommend`, `then`, `ratification`. For a `create`, `then` holds the page draft itself, laid out per the target category's schema — the human signs content, not the fact that a decision occurred.

Not duplicated here: one description, one place to change it.

**Never move to another Case until the current one is ratified or deferred.**

---

## 3. Decisions

Four types. There are no others.

| Type | Use when |
|---|---|
| `create` | a new page must exist |
| `update` | an existing page's fields change (including setting an Estimate's `result`/`status`) |
| `delete` | a page or part of one should stop being active |
| `defer` | postpone something not started, or pause something in progress |

**Read is not a decision.** You read the vault freely, without asking.

### Before any `create`

If the Case has no `ref`, you must query the vault first to confirm nothing already covers this. Put the result in `now`. Only after that may you propose `create`.

**Pre-task is not a name lookup.** It asks the broader question: does this already exist, are there similar cases, what might obstruct this, what contradicts the plan. Estimates count too — a `create` spawns one, and an identical check may already be sitting on another page.

**It also returns relevant tags** from `tags.md`. Put them in `then` alongside `purpose` and `criterion`, so the human ratifies the tagging with everything else. If no existing tag fits, propose a new one explicitly — the human sees "a new tag X will be created" and signs or objects. This is why `tags.md` cannot grow uncontrolled: every new tag was ratified, and the librarian only registers what is already signed.

**The query must include `draft` pages.** Everything ever deferred lives on as one, whether or not it made this session's capped `brief.md`. Skipping them means re-deciding something already decided, doing the work, and leaving the original `defer` behind as dead weight.

If the Case arrived with a `ref` (from the brief, the Frontier, or a pre-check), do not query — go straight to `update`.

### Paired Estimate on create

Creating a Leaf Entity or Rule requires you to also decide and log its Estimate, in the same ratified Case:

```
- decision[case 3][create][entity-x]
- decision[case 3][create][estimate-x]{ref:entity-x}
```

You write the acceptance criteria into the Case's `then` so the human ratifies them along with the page itself. Never leave this for the librarian to infer. If the criteria turn out to be contested enough to need their own discussion, split into a sub-case — that's the normal atomicity test, not an exception.

### Delete

No dedicated Estimate page. Instead: query the vault for what depends on the target, state the impact in `recommend`/`then`, and let the human ratify with that analysis in hand. Delete never means physical deletion — it sets `status: deleted`, the librarian archives, a cleanup script moves the file.

Restoring is an ordinary `update` setting `status` back to `draft` or `built`.

---

## 4. Ledger

`raw/<date>/ledger.md` carries two kinds of line, written mechanically by a hook that interprets nothing.

**Decisions** — routing only. The content already exists in `spec.md`, ratified in the Case, so the line just says what happens to which page:

```
- decision[case_id][kind][slug]{ref:parent}{source:external_id}
```

- `slug` — the affected page
- `ref` — the parent, for a `create` that adds a child. Omitted for update/delete: `slug` already identifies the target.
- `source` — optional external origin (a GitHub issue). Traceability only; never affects routing.

**Estimates and lessons** — these carry text, not just markup. Their content is born in the moment and exists nowhere else: a measurement taken after the tests were written, a failure understood while it was still fresh. There is nothing in `spec.md` to point at.

```
- estimate[slug][passed|failed] <the result, in full>
- lesson[error|knowledge][slug] trigger: <...> root_cause: <...>
```

An `estimate[...]` line does not replace the `decision[...]` that created the page — the decision made it exist, the estimate line fills it. Both are needed, and they do different jobs.

**Only the main agent writes ledger lines.** A subagent that takes a measurement returns it and the main agent records it; a subagent that hits a fork stops and returns rather than deciding.

**How the script reads them.** `decision` lines produce actions, with content pulled from `spec.md`. `estimate` lines produce no action — the page already exists from its own earlier `decision` — so the script finds that page's entry in `materialize.yaml` and fills in `status` and `result` from the line. If the referenced page is not in the yaml at all (the measurement belongs to a page created in an earlier session), it becomes an ordinary `update` entry. `lesson` lines produce a `create`, taking their content from the line itself rather than from `spec.md`.

**Changed your mind mid-session?** Never edit or delete an earlier line. Write a new one that supersedes it:

```
- decision[case 4][update][slug-x]{supersedes:case1}
```

The librarian reads the log as a chain and applies the last link.

**`#case-N` in an `origin`** names the ledger line carrying `[case N]`. It is a grep target, not a Markdown anchor; lint checks that the line exists.

## 5. Routing

**Every ratified decision produces two things**: a page in `wiki/decisions/` recording the decision itself, and an effect on the target page. The table below describes the second; the first happens unconditionally.

| Decision | `ref` | Effect on the target |
|---|---|---|
| `create` | none | Query vault. Nothing found → new top-level page |
| `create` | parent | New child page, added to the parent's `children` |
| `create` | — (Leaf) | Also log a paired `create` for its Estimate |
| `update` | target | Edit the target's fields |
| `update` | none | **Invalid.** This Case should have been a `create` |
| `delete` | target | Impact analysis in-case → librarian archives → `origin` preserved |
| `defer` | existing | Log only; it resurfaces via the next Frontier |
| `defer` | none | Librarian creates a minimal placeholder page |

`target_category` on the decision page says which folder the effect lands in, so the script never infers it from a slug prefix.

---

## 6. Splitting pages (the atomicity rule)

Applies identically to Case, Entity, Rule and Estimate. Not to Lesson (a recorded fact does not split) and not to Insight (it is produced by clustering, which is the rule running in reverse):

> A unit stays whole as long as its closing act — ratification, verification, or "built" — is a single indivisible judgment. The moment it decomposes into ≥2 conditions that can fail independently and need different fixes, split into children.

Test it mechanically: list the conditions of "done". For each pair, ask whether one could fail while the other passes, needing a different fix. If yes for any pair, split.

**Entity vs Estimate.** If two conditions are genuinely different behaviors (fixing one doesn't touch the other) → two child Entities. If they're the same logic checked from different angles (one fix covers both) → one Entity, two Estimates.

A MOC has no direct criteria — its `children` are the functional requirements, and its `estimates` cover only cross-cutting/non-functional checks that belong to no single child.

Do not impose a fixed hierarchy of levels. Depth follows the rule, nothing else. The one question worth asking when a brand-new top-level Entity appears: is this a new deployment unit, or a feature inside an existing one? The answer becomes content in that Entity's `estimates`, not a field.

### MOC means different things for Entity and Rule

**Entity MOC = decomposition.** Children are independent requirements; order among them is arbitrary and must not be recorded as structure. If the product itself has a sequence (cart → address → payment), that sequence is prose in `How it works` plus a cross-cutting Estimate that checks the order holds — never a structural field, because a field would duplicate the prose without being checked by anything.

**Rule MOC = workflow.** Children are an **ordered** sequence, and the order is the content: `retro → handoff → documentation`. Scripts rebuilding backlinks must preserve it; lint must not normalize it. A Rule MOC's Estimate checks the sequence itself — that handoff cannot start before Retro closes.

This is why our own process is described as Rule MOCs — session-start, plan-mode, work-mode, end-of-work, documentation — each holding ordered children, recursing where the atomicity rule calls for it.

---

## 7. Estimates

Always its own page. Never inline, never composite.

- **QA** — the expected result is known in advance. Check against a stated criterion.
- **Research** — the result is not known in advance. Investigating produces new content.

Fields: `criterion`, `method`, `result`, `status` (`pending`/`passed`/`failed`), `origin`.

**A `failed` Estimate is debt, not an endpoint.** Its Entity stays `draft` and the librarian surfaces it in `brief.md` until a human decides what to do. The default outcome, absent a decision to fix, is archival — an Entity that cannot pass its own criterion should not sit in the vault pretending to be work in progress.

Rules require Estimates for the same reason Entities do: a broken hook breaks the workflow as badly as broken product code.

---

## 8. Lessons and Insights

Not driven by the routing table. Lessons are recorded facts, not ratified decisions — the hook writes them directly, no Case required.

### Lesson

Two kinds, both flat, both in `wiki/lessons/`:
- `error` — something went wrong
- `knowledge` — external material studied once, so the source never has to be supplied again

```
- lesson[error|knowledge][slug] trigger: <...> root_cause: <...>
```

Write `trigger` and `root_cause` yourself, in the moment, while the context is cheap. For `knowledge`, record `source` too.

**Estimates:** an `error` Lesson gets one created already `passed` and archived immediately — the failure was observed directly, so it is a record that this was verified. A `knowledge` Lesson gets a Research Estimate that must actually reach `passed`; unverified external claims are not usable.

**Slug is area + cause** — `lesson-hooks-sessionstart-cannot-block`. The area groups related lessons in a plain file listing; the cause makes near-duplicates visible before anyone opens the index. Naming by symptom was rejected: unrelated failures often share a symptom, and the symptom is not what clustering compares.

### Insight

**A separate type, not a kind of Lesson.** It shares no content fields with one — no `trigger`, `root_cause`, `source` or Estimate; instead `pattern`, `children`, `severity`, `addressed_by`. That "Insight is a MOC over Lessons" describes a relationship, not an identity: Estimates belong to Entities without being a kind of Entity.

Created by the librarian on the **second** Lesson sharing a root cause — one occurrence is an incident, two is a pattern. The archive is searched too: a recurrence after the pattern was supposedly fixed carries information a first occurrence does not, and that belongs in the new Lesson.

`severity` = count of children not archived, recomputed by lint.

An Insight is never the target of a Decision. It reaches you as a `brief.md` candidate in a later session and becomes an ordinary ratified Case there. `actioned` is not terminal: a new matching Lesson reopens it, previously archived children stay archived, and `severity` counts only the current run.

## 9. The session workflow

**The process is not described here.** It lives in the Rule MOCs, which are both the
documentation and — through `enforcement: render` — the harness itself. One source, no
drift.

| Phase | Rule MOC | What it covers |
|---|---|---|
| Session Start | `rule-session-start` | `/hi`, context loading, the event-log and ledger hooks |
| Plan Mode | `rule-plan-mode` | Case protocol, `/ask`, pre-task reconciliation |
| Work Mode | `rule-work-mode` | executable plan, branch, `subagent-guppi`, harness tests |
| — | `rule-subagent-guppi` | task dispatch, review, model tiers |
| End of Work | `rule-end-of-work` | Retro, the commit hook, handoff |
| Documentation | `rule-documentation` | the `librarian-guppi` agent |

Read those for how the session runs. Read this file for what the vault is made of and the
rules that hold regardless of phase.

**Order of the whole thing**, for orientation only:

```
/hi → Frontier → Cases (ratified one at a time) → Spec approved
    → executable plan → branch + baseline commit → subagents → harness tests
    → Retro → commit → handoff → librarian → commit → closed
```

The branch is created **after** the plan is written, not before: Plan Mode touches no code,
so there is nothing to isolate until there is a plan to execute.

---

## 10. Librarian boundaries

Runs every session, in a clean context. **The only actor that writes to `wiki/`** — everything reaches the vault through the scripts it invokes.

**Reads:** `handoff.md`, `materialize.yaml`, the category indexes, and `lessons.index`. That is all. Not `ledger.md`, not `spec.md`, not `plan.md`, not the pages themselves — the yaml is assembled by script and already carries every `purpose`, `criterion` and tag. Raw artifacts are opened only when a script reports a problem.

**Does three things:** checks new pages against the indexes, synthesizes Lessons, and writes the brief. Statuses, backlinks and cascades are all script or lint work.

**Acts on exactly one judgment:** turning a `create` into an `update` when the indexes reveal a duplicate, before generation runs. Safe because `delete` only archives and every action is marked `librarian:` in `History`; worth acting on because catching it beforehand avoids a page being created and merged in the same session, and because a brief that opens with housekeeping every time is a real cost.

**Flags everything else:** MOC candidates, over-broad MOCs, stale defers, `failed` Estimates, incomplete pages, contradictions.

**Never:**
- authors content — a missing required field is flagged, never invented
- rewrites ratified content — only the route in `materialize.yaml` may change
- restructures — creating or splitting a MOC is a ratified decision
- invents semantic links — structural backlinks come from ledger refs via script; thematic association is what tags are for
- edits `index.md`, `glossary.md` or any `schema.yaml` — Rule-class content
- stops to ask — the human is gone; it runs to the end
- does lint's work

---

---

## 11. The indexes

`wiki/<category>.index` — one generated line per live page, `slug: purpose` (for lessons,
`slug: root_cause`). Regenerated by lint every session, never edited by hand.

```
entity-cart-total: recalculates the order total
entity-discount-new-client: new clients receive a 0% discount
```

This is what makes semantic checks affordable: five hundred pages are a few thousand
tokens, read in one pass, and the agent compares meanings directly. No embeddings, no extra
dependencies, and no reason to add them until the index itself stops fitting in context.

**Per-category, and comparison never crosses categories.** An Estimate and an Entity sharing
a purpose is not duplication — it is the normal division of labour between a thing and its
check.

**There is no `decisions.index`, and Decision pages are never archived on completion.**
Everything worth searching for is reachable through entities and rules: if something was
decided and built, its page is in the index; if it was deferred, it exists as a `draft` page
and pre-task finds it. Decisions are a journal — read by following a page's `origin` to ask
"why is this the way it is", never by scanning. Since nothing scans them, they cost nothing
to leave in place, and a decision stays valid for exactly as long as the page it created. It
leaves the live vault only when superseded, or by cascade when its target is archived.

The one lookup that does happen — finding the decision a new one supersedes — is a targeted
grep by slug, which is why Decision slugs are meaningful (`decision-create-cart`, never
`decision-2026-09-08-01`).

`/ask` is the search mechanism over these indexes. One tool, two moments: pre-task queries
by intent before a decision exists; the librarian queries by finished content afterwards.

---

## 12. Where content comes from

Two artifacts carry two different things, and confusing them is how unratified text ends up
in the vault.

- **Ledger** — the index. What was decided, in what order, against which target.
- **Case / Spec** — the content, ratified by the human in Plan Mode.

Ratifying `create entity-x` without seeing what that page will claim is an empty
ratification. The human signs content, not the fact that a decision occurred.

The librarian lays that ratified content into schema fields. **It reshapes; it never adds.**
If a Case is missing a required field — a `create` with no `criterion` — it does not invent
one. The page is marked incomplete and recorded in `brief.md`.

Fields split by origin: `type`, `purpose`, `criterion`, `method` and `tags` come from the
ratified Case. `origin`, `slug`, `status`, `parent`, `children` and backlinks are derived
mechanically by the generation script.
