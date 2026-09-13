# Sprint

## migration — open since 2026-09-09

**Goal.** The repository works by the model in `wiki/index.md`: Phase 1 (the harness built
by its own rules) and Phase 2 (the surviving pages brought into conformance) of
`docs/migration/migration-plan.md` are closed.

**Done when** (the Definition of done of `migration-plan.md`):

1. Every page in `entities/` and `rules/` has a `type`, `purpose`, `status` and `origin` as
   its schema says, and at least one Estimate ref.
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
hooks) · 3c raw lifecycle, built 2026-09-13 (session L): the archive of an applied session of
`raw/` (case 100), the tail `/hi` prints (101), one archive root `vault/archive/` (102), the
ledger of a session (103), the status cascades over the archive (104), the slug checked
against the archive (105); `decided_by` dropped — `origin` is the one pointer, resolved in
`raw/` or in the archive, never rewritten; 3b before 4) · 4 conversion of the parked pages by
group · 5 closing: `/grill-me` kept without a page; `git pull` in `/hi` without an upstream
(owner's decision 11.1); `gh` not logged in, no GitHub remote (11.2); the fate of `vault/parked/`,
`docs/superpowers/`, `docs/HANDOFF.md`, `docs/migration/rule-*.md`
and the 2026-08 documents under `docs/` — moved here from the brief's Deferred list by case 59.5;
the old `vault/archive/` of August left by case 102.1.
Slices 0–2 closed by 2026-09-10; Slice 3 built 2026-09-10, closed 2026-09-12:
`estimate-documentation-completes` passed on the librarian's run of session H read against the
criterion of case 58, the other readings of Slice 3 passed on 2026-09-11.
