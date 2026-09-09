---
type: rule
kind: MOC
purpose: Prevents ratified decisions from ending the session without becoming vault pages
status: draft
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: full
children: [rule-materialize, rule-index-check, rule-page-generation, rule-synthesis, rule-brief, rule-lint-commit]
estimates: [estimate-documentation-completes]
origin: TBD
sprint: TBD
created: TBD
tags: [session, workflow, librarian]
---

## Purpose

Prevents ratified decisions from ending the session as ledger lines nobody turned into
pages — and prevents the librarian inventing anything while doing it.

## How it works

This MOC **is** the `librarian-guppi` agent definition: it renders in full into the agent
file, and its children splice into the frame in order. The agent runs start to finish
without human involvement; the main agent returns only for a closing check.

### Clean context is structural, not disciplinary

The librarian is an **agent**, not a skill — it gets its own context window. That is what
makes the clean context real: it is not a rule the agent must follow, it is a property of
how it is invoked. A skill would inherit the main agent's context and the whole argument
below would rest on discipline instead.

By handoff the main agent's context holds the entire session — dead ends, noise, abandoned
approaches. The librarian starts empty and reads exactly four things: `handoff.md`,
`materialize.yaml`, the category indexes, and `lessons.index`.

Not `ledger.md`, not `spec.md`, not `plan.md`, not the pages themselves. `materialize.yaml`
is script-assembled and already carries every `purpose`, `criterion` and tag. Raw artifacts
are opened only when a script reports a problem.

This also tests the system: if routing cannot be derived from the ledger alone, that is a
defect in the ledger, and it surfaces here rather than months later.

### One judgment it acts on, everything else a flag

**Duplicates it merges** — by editing `materialize.yaml` *before* generation, turning a
`create` into an `update`. Safe because `delete` only archives, so an over-eager merge is
recoverable from `History` and `log.md`; worth acting on because catching it beforehand
avoids a page being born and merged in the same session, and because a brief that opens
with housekeeping every time is a real cost. Only the route may change — ratified content
is never rewritten.

**Everything else is a flag**: MOC candidates, over-broad MOCs, stale defers, failed
Estimates, incomplete pages, contradictions. It never stops to ask — the person is gone —
so it runs to the end and records what it could not resolve.

Its actions are marked `librarian:` in `History`, distinct from entries carrying an
`origin` back to a ratified Case. Six months on, "a human decided this" and "the librarian
tidied up" must stay tellable apart.

## Children

1. **[[rule-materialize]]** — script. Assembles `materialize.yaml` from ledger lines,
   routing table and ratified content in `spec.md`. `origin`, `slug` and `status` are all
   derived — `status` follows from the decision kind, so no agent touches it.

   `decision` lines produce actions. `estimate` lines produce none — the page already
   exists from its own earlier decision — so the script fills in that entry's `status` and
   `result` from the line, or adds an `update` entry if the page predates this session.
   `lesson` lines produce a `create`, taking content from the line itself.

2. **[[rule-index-check]]** — `render: partial`. Check each new page's `purpose` against
   its own category index via `/ask`, plus whatever `handoff.md` asked for specifically.
   **Per category only** — an Estimate and an Entity sharing a purpose is division of
   labour, not duplication.

3. **[[rule-page-generation]]** — script. Writes files from `materialize.yaml`, fills
   backlinks both ways from the ledger's refs, applies tags ratified in the Case, registers
   genuinely new ones in `tags.md`, writes the first `History` line and the `log.md` entry.

   **A slug collision is an error, not a rename.** Pre-task checked it when the Case was
   formed, but it can still be taken by generation time. Producing `entity-cart-2` silently
   would put an unratified name in the vault. The script errors; the librarian judges.

   **A page is always created, even when incomplete.** Red lint is an accurate signal of
   debt; a ratified decision with no page at all is worse, because then the ledger and the
   vault disagree silently.

4. **[[rule-synthesis]]** — `render: partial`. Cluster Lessons sharing a `root_cause` into
   an Insight, archive included — a recurrence carries the information that our previous
   answer did not work, and that belongs in the new Lesson. Then collect the remaining
   flags.

5. **[[rule-brief]]** — `render: partial`. Write `brief.md` and update `sprint.md`.
   **Deferred items capped at 7** — a shop window, not storage: everything deferred lives on
   as a `draft` page and pre-task finds it regardless. Rank by related Insight `severity`,
   then by how many times an item has already been postponed. The librarian's own flags
   have no cap.

6. **[[rule-lint-commit]]** — script. Lint and cleanup run **after all judgment**, so they
   see the final graph: broken refs, schema conformance, orphans, status contradictions,
   and cascading statuses — an Entity is `built` only once all its Estimates pass, which is
   a graph property. Regenerate the indexes, move `archived` pages into `wiki/archive/`,
   and archive this session's `raw/` alongside them. Then commit.

   A lint failure nothing can fix mechanically is a flag, not a blocker. The session still
   closes.

## Estimates

- [[estimate-documentation-completes]] — QA. Every ratified decision in the ledger has a
  corresponding page after the librarian runs; no page exists that no decision produced;
  and the librarian's commit is separate from the Retro baseline.

## What happens next

Control returns to the main agent for a final check — anything left over? — and the session
closes.

## History

- TBD created
