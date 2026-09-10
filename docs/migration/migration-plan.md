# Migration Plan

One-time plan for converting the existing vault into the model described in `index.md`. Discard this document once migration is complete. The permanent set is `index.md`, `glossary.md`, `case-schema.md`, and the six page schemas (decision, entity, rule, estimate, lesson, insight).


---

## Starting position

- A working harness already exists, partially. Some of it is undocumented here but functional.
- The human has manually cleaned the active vault before you start: only `entities/` and `rules/` pages survive. Everything else was removed by hand.
- A copy of the pre-migration state lives on a separate git branch. Nothing is lost; you never need to preserve garbage "just in case."
- Migration happens on its own branch.

**What is already wrong, and known to be wrong:**
- `estimates/` does not exist. No page has one. Every surviving Entity and Rule is therefore non-conformant by definition.
- Surviving pages have no `origin` — they predate the ledger, so there is no ratified decision behind them.
- Some pages describe things that work; some describe things that don't. You cannot tell which from the page alone.

---

## The rule that governs this migration

**Migration is not an exception to ratification.**

You have more context than the people who wrote this plan, and you are expected to use it — but "use your judgment" means *propose, then wait*. For every page, you produce a Case and the human ratifies it. You never silently convert, archive, or backfill.

The one thing you may do without asking is **read**.

---

## Phase 1 — Build the harness by its own rules

Do not build the harness "outside the system" and then switch the system on. Build it as the system's first real work.

1. `rules/` is where the harness lives. Read what already exists there and in the working harness.
2. Each existing harness element (hook, script, instruction) is a Case:
   - `context` — what this element does
   - `now` — how it currently works, and whether it already conforms
   - `problem` — what must change for it to be a conformant Rule page
   - `recommend` / `plan` — including the acceptance criteria for its Estimate
   - wait for ratification
3. Apply the atomicity rule as you go. A hook that does two independently-breakable things is two Rules.
4. The ledger hook is itself a Rule. Until it exists and works, **write ledger lines into the session digest by hand**, in exactly the format `index.md` specifies. Hand-written and hook-written lines must be indistinguishable.

Order matters: build the ledger hook first if it doesn't exist, so the rest of the migration is recorded properly.

Describe the process itself as **Rule MOCs** with ordered children — session-start, plan-mode, work-mode, end-of-work, documentation — since a Rule MOC's order is its content.

**Required Rules by the end of this phase** (create any that are missing — each as a ratified Case with its own Estimate):
- Session Start hook (brief, git pull, sprint context, Frontier assembly)
- Ledger hook (listens for the decision pattern, writes to the session digest, no interpretation)
- Lesson hook (same, for the lesson pattern)
- Pre-plan hook (librarian pre-check before plan approval)
- Page-generation script
- Cleanup script (moves `archived` pages to `wiki/archive/`)
- Lint scripts (broken refs, schema conformance, status contradictions, orphans)
- Librarian agent definition, with the boundary from `index.md` §10
- Index-generation (one `<category>.index` per category, `slug: purpose`)
- `materialize.yaml` assembly from the ledger
- **Archive script** (Slice 3c, raw lifecycle) — after generate and cleanup the librarian
  moves `raw/<date>/` of every fully applied date to
  `vault/archived/<sprint>/raw/<date>/<stamp>/` (one stamp per librarian run, several a
  day) and rewrites every path that pointed there. A page born of a Case carries
  `decided_by` (a Decision slug); a Decision, Lesson or Insight page and a History line
  carry `origin` (a ledger pointer). Lint checks `decided_by` as a ref and `origin` as a
  grep target in `raw/` or `archived/`. A ledger line written after the librarian's
  commit lands in a fresh `raw/<date>/ledger.md`, and `/hi` prints every
  `raw/*/ledger.md`. The existing pages are migrated by script.
- **Harness renderer** — reads every Rule page with `enforcement: render` and writes its
  `## Render` body into the file named by `governs`: `full` replaces the file, `partial`
  splices between `<!-- slug -->` markers, in the order the parent MOC lists its children.

  Build this early. Without it `enforcement: render` does nothing, and every skill and
  agent file has to be maintained by hand — which is the exact drift the rule pages exist
  to prevent.

---

## Phase 2 — Bring surviving Entities and Rules into conformance

Every surviving page needs, at minimum: correct `type`, `purpose`, `status`, and at least one Estimate.

Work page by page. For each, one Case:

- **context** — what this page claims to describe
- **now** — what you found: does it match reality? Is it covered by tests? Is it MOC or Leaf under the atomicity rule? Does it duplicate another page?
- **problem** — what's missing or wrong
- **recommend** — your proposal, which may be any of:
  - conform it as-is (add Estimate, fix fields)
  - split it (atomicity rule says it's really several pages)
  - merge it into another page
  - archive it (it describes something that no longer exists or never worked)
- **plan** — the resulting page(s) and the acceptance criteria for their Estimates
- **ratification** — wait

**On Estimates specifically.** You decide, per page, whether to backfill a real Estimate now or leave the page `status: draft` with a `pending` Estimate to be filled when something next touches it. Pages already covered by passing tests are the cheap case — the criterion is close to mechanical there. Pages where nobody knows whether the behavior works are the expensive case, and `draft` + `pending` is an honest answer. **Recommend which, per page; the human decides.**

**On `origin`.** Surviving pages have no ratified decision behind them. The Case that brings a page into conformance *is* that decision — set `origin` to it. Do not invent a fictional prior origin.

**Order.** Process MOC pages before their children where the structure is already clear; otherwise work bottom-up from the pages you understand best. State your chosen order in the first Case of the phase and let the human adjust it.

---

## Phase 3 — Remaining garbage, if any

Only if the human brings it back from the other branch. Same protocol as Phase 2: one Case per page, propose, wait.

Default assumption: if it wasn't worth keeping in the manual cleanup, it isn't worth restoring.

---

## Retired terms — never reintroduce

The existing vault may contain these. They are gone from the model. If you find them:

| Found | Becomes |
|---|---|
| `Proposal` page | An Entity with `status: draft` |
| `Verify` decision | `create` + `ref` to a new Estimate |
| `Accept` decision | `update` setting a field on the target |
| `Revoke` decision | `delete` (cancellation) or `defer` (pausing) |
| `deployment_unit` field | Delete the field; the concept lives as content in `estimates` |
| `Delegate` decision | Does not exist. Every decision is ratified by the human |

---

## Definition of done

Migration is complete when:

1. Every page in `entities/` and `rules/` has a `type`, `purpose`, `status`, `decided_by` or `origin` as its schema says, and at least one Estimate ref.
2. Every Estimate page referenced actually exists, with `criterion`, `method`, `status`.
3. Lint passes: no broken refs, no schema violations, no orphans, no status contradictions.
4. Every harness element listed in Phase 1 exists as a conformant Rule page with its own Estimate.
5. The ledger hook works, and the session digest for the final migration session was written by the hook rather than by hand.
6. `brief.md` carries anything deferred during migration, so it surfaces in the next session's Frontier.
7. Tests are green, and the branch is ready to merge.

---

## What to do when this plan and reality disagree

This plan was written without seeing the vault. You will see it.

If something here is wrong or impossible, that is a Case like any other — raise it, recommend an alternative, and wait for ratification. Do not silently work around it, and do not follow it off a cliff.
