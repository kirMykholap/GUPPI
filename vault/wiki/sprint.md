# Sprint

## migration — open since 2026-09-09

**Goal.** The repository works by the model in `wiki/index.md`: Phase 1 (the harness built
by its own rules) and Phase 2 (the surviving pages brought into conformance) of
`docs/migration/migration-plan.md` are closed.

**Done when** (the Definition of done of `migration-plan.md`):

1. Every page in `entities/` and `rules/` has a `type`, `purpose`, `status`, `decided_by`
   or `origin` as its schema says, and at least one Estimate ref.
2. Every Estimate page referenced actually exists, with `criterion`, `method`, `status`.
3. Lint passes: no broken refs, no schema violations, no orphans, no status contradictions.
4. Every harness element listed in Phase 1 exists as a conformant Rule page with its own
   Estimate.
5. The ledger hook works, and the ledger for the final migration session was written by the
   hook rather than by hand.
6. `brief.md` carries anything deferred during migration, so it surfaces in the next
   session's Frontier.
7. Tests are green, and the branch `migration` is ready to merge into `main`.

**Slices**, each its own Plan Mode and approval: 0 layout · 1 ledger, event log, `/hi` ·
2 renderer, lint, indexes, `/ask`, pre-task · 3 materialize, generate, cleanup, librarian, retro,
handoff · 3b Work Mode (`rule-work-mode`, `rule-subagent-guppi`, `to-executable-plan`, its
hooks) · 3c raw lifecycle (`decided_by` on pages born of a Case, `origin` as a ledger
pointer, `raw/<date>/` of a fully applied date archived by run stamp with its paths
rewritten, a fresh ledger as the tail `/hi` prints, lint on both fields, the pages
migrated by script; 3b and 3c both before 4) · 4 conversion of the parked pages by
group · 5 closing. Slices 0–2 closed by
2026-09-10; Slice 3 built 2026-09-10, closes when the librarian's first run and the `/retro`
and `/handoff` readings pass in the next session (see `brief.md`).
