# Brief — 2026-09-16, after session 1034 (the Spec conserved, nothing built)

Written by hand, not by the librarian. This session reached a ratified Spec and stopped
there: no Work Mode, no Retro, no handoff, no librarian. `materialize`, `generate`,
`cleanup` and `render` were not run, and **not one page of `vault/wiki/` was written**. The
short shape of this brief is the one Case 190.4 ratifies; the skill that should write it,
`/carry`, is Case 190.1 of the Spec below and does not exist yet, so this is its first run
by hand.

## The conserved Spec — what the next session does first

`vault/raw/2026-09-16/1034/spec.md`, 52 KB, Cases 186–192, ratified and not executed.
`vault/raw/2026-09-16/1034/carry.md` marks the unit. `guppi materialize` does not yet know
that mark — the skip is Case 190.3 of this very Spec — so **until it is built, nothing
mechanical stops a librarian from applying this unit blind.** A librarian run over
`raw/2026-09-16/1034/` before its work is done would make the vault claim behaviour no code
implements, and would splice a Render into `CLAUDE.md`.

**The Spec is not executable as it stands.** `guppi pretask --check` and `ask-guppi` found
nine defects, listed below. The next session opens by repairing them — that is Plan Mode
work and new Cases, not code — and only then goes into Work Mode.

Order of the work, forced by dependencies:

1. Repair the Spec (the nine defects).
2. Case 190 — `/carry` exists from then on.
3. Case 189 — `materialize` must read the new form of the `then` blocks before any librarian
   runs, because Cases 187–190 are written in it.
4. Cases 186, 187, 188, and the hand migration of the Estimate pages.
5. Delete `carry.md`, then Retro, handoff, librarian.

`spec.md` was left exactly as ratified. Nothing in it was corrected after capture: the record
shows what was signed, and this list shows what is wrong with it.

## What was ratified

- **186** (`rule-page-generation`, `decisions-schema`, `decisions-schema-yaml`;
  `rule-pretask`; `rule-lint`) — the `purpose` of a `defer` is written to the Decision page
  under `## Deferred`, verbatim, one `### [[slug]]` heading per target; pre-task stops
  sending the body of a deferred Case to `ask-guppi`; lint replaces the eight `schema` and
  `orphan` findings on a placeholder with one, `deferred: N times since case M`.
- **187** (`rule-plan-mode`, `estimate-plan-mode-names-its-estimates`) — which Estimate a
  ratified Case changes is the judgment of the Case, named by slug; only a replaced Criterion
  sets `pending`; the `contract` flag decides nothing.
- **188** (`rule-case-protocol` `{supersedes:case 185}`, `case-schema`, four Estimates) —
  `given` holds the conditions of the behaviour, `given` + `when` + `then` are the Criterion
  replaced whole, `tasks` without `contract` and "block N" lines, a `create` without
  `method`, `estimate_kind`, `estimate_slug`. `estimate-case-protocol-loaded` is recut into
  four pages.
- **189** (`rule-materialize`, two Estimates updated, six created) — the script derives no
  Estimate from `contract`, `method` or `supersedes`; an Estimate has its own ledger line and
  its own entry, its Criterion lifted from the Case. Nine blocks are recut; block 90.1 dies
  with the derivation.
- **190** (five sub-cases: `rule-carry-over`, `rule-end-of-work`, `rule-materialize`,
  `rule-brief`, `rule-spec-capture`) — a session has a second end: `/carry` straight after
  Plan Mode, which writes the brief and the mark, commits, and runs nothing else;
  `materialize` skips a marked unit; the `guppi spec` hook prints the fork.
- **191** — `defer` of `rule-page-generation`, `rule-lint`, `rule-pretask`,
  `{supersedes:case 182}`.
- **192** — `defer` of `insight-ledger-hi-tied-to-its-session-by-position`.

Reading `passed`: `estimate-retro-commit-gates`, block 180 — the live half, a typed `/retro`
as the first command of the session, refused with "nothing to review". That refusal cannot be
taken twice in one session: the estimate line itself becomes a record in the window.

## What the Spec lacks — the nine defects

1. **No Case updates `index.md` or the schemas.** §5 of the map still says a Leaf `create`
   carries `method` and an `update` carries `contract: changed`; §12 still says a `create`
   without `method` is `incomplete`. All of it contradicts 187, 188 and 189 word for word.
   `estimates/schema.yaml` and `rules/schema.yaml` are untouched although point 5 of the
   model changes the Estimate's fields. Point 16 named these files; no Case was written.
2. **`rule-case-protocol`: the new Render is nowhere.** The `then` block carries
   `sections: Purpose` and `change` only. The page is `enforcement: render`, and the task
   demands `render --check` exit 0 — which would splice the **old** Render back into
   `CLAUDE.md`. Worse, `rule-page-generation` says "a section a page still carries is left as
   it is", so `## How it works` cannot be dropped by `generate` at all.
3. **`rule-materialize` (189): dropping `## How it works` has no text and no mechanism**, and
   the move of the field list into the docstring is named only in a task.
4. **Four Estimates would sit `pending` with their old Criterion.**
   `estimate-materialize-assembles`, `-walks-dates`, `estimate-end-of-work-order` and
   `estimate-brief-written` carry `set: {status: pending}` and `change: the Criterion replaced
   whole` with no `sections: Criterion`. 189 thereby breaks the very form 189 ratifies.
5. **Ten new Estimate pages carry no `## Context`**, which `estimates/schema.yaml` requires.
   The new model removes Context — but that schema change is defect 1.
6. **`rule-carry-over` has no `sections: Render`**, required when `enforcement: render`. The
   text of `.claude/skills/carry/SKILL.md` is signed by nobody.
7. **186.2 edits the right paragraph of `rule-pretask` but the wrong sentence.** The first
   sentence still requires `slug — decision type — purpose` in the list, contradicting the
   appended one. The `purpose` requirement must come out of the first sentence.
8. **Case 186's blocks are in the old form** (`contract: changed`, `estimate_slug`) and no
   task rewrites them, although the `given` of 187 asserts one exists. Under 189's
   `materialize` the `contract` key is ignored, so `estimate-generate-writes`,
   `estimate-pretask-reconciles` and `estimate-lint-catches` would get nothing and never go
   `pending`; three task lines still say "block 186.1/.2/.3", and blocks are abolished.
9. **190.1 writes `status: draft` and `parent` by hand** — derivable fields that
   `case-schema.md` says are not written in a `then` block. And 190.2–190.5 carry `change`
   only, with no text for the pages they change.

Two more, minor: the task line of 187 says `{supersedes:case 182}` goes on the last Case of
the group, while the ratified line puts it on 191 and 192 is last; and the `given` of 187
says the librarian runs the scripts at the close of this session, which the decision to
conserve made false.

## Deferred

The `purpose` of each is quoted in full: Case 186.1, which would put it on the Decision page,
is itself unbuilt, so when these defers are applied their purposes will be dropped exactly as
the purpose of case 182 was. This list is the only place they survive besides `spec.md`.

1. **`rule-page-generation`** — case 191 (supersedes 182), Slice 3d. "`generate` without
   Criterion blocks and without `remove_criterion`; the Criterion replaced whole; the fields
   `purpose`, `method`, `checked`; the recut of `estimate-generate-writes` and
   `estimate-generate-walks-dates` at this touch. The change of case 186.1 — the
   `## Deferred` section on a decision page — is not part of this defer and stands ratified."
   (stood in 3 briefs)
2. **`rule-lint`** — case 191, Slice 3d. "The finding `unread` on every `pending` and `failed`
   Estimate; the Estimate schema without `## Context` and without the `## Method` section; the
   `unmigrated` counter for the transition, and the removal of the old shape when it reaches
   zero. The change of case 186.3 — the `deferred` finding on a placeholder — is not part of
   this defer." (stood in 2 briefs)
3. **`rule-pretask`** — case 191, Slice 3d. "Pre-task checks the Estimates of the rule named
   in `context` and asks `ask-guppi` whether an unnamed one speaks of the same thing; the
   checks of the old model are removed — `method` on a Leaf `create`, `contract` on a Leaf
   `update`, and the split of a Case with two Leaf contracts. The change of case 186.2 is not
   part of this defer." (stood in 2 briefs)
4. **`insight-ledger-hi-tied-to-its-session-by-position`** — case 192, `open`, severity 1.
   "Retire the binding by position: `pretask.resolve_session` resolves the session from the
   stamped `hi` and walks back to the date of that `hi`, instead of falling back to the last
   `session-start` of today's event log; the ledger hook's window is checked against it so the
   two readers do not disagree at midnight. Closes all four children of the Insight. Needs its
   own Estimate and one live reading across midnight." (stood in 2 briefs)
5. **`rule-work-mode`** — case 183, Slice 3b: the Spec as tasks with code, the ticked boxes,
   the test of each Estimate written first and turned green; after Slice 3d and before Slice
   4. Placeholder, `draft`, a lint orphan. (stood in 16 briefs)
6. **`rule-subagent-guppi`** — case 183, Slice 3b: what a subagent may do in Work Mode, and
   the fork that comes back to the main agent as a Case; with `rule-work-mode`. Placeholder,
   `draft`, a lint orphan. (stood in 16 briefs)

Retired from the previous brief: `rule-plan-mode` (182) taken up by case 187;
`rule-case-protocol` (185) taken up by case 188; `rule-materialize` (182) taken up by case
189. `deferred_by` on all five targets of 182 clears only when case 191 is applied.

## Flags

- **The vault is untouched.** Zero pages created, updated or archived; no Estimate changed
  status; no `deferred_by` set or cleared. `decision-case-182` still marks all five of its
  targets and `decision-case-185` still marks `rule-case-protocol` — both are cleared by the
  lines of this session's ledger when it is finally materialized.
- **Lint unchanged at 70 findings**; `make test` unchanged at 385 green — no code was touched.
  Neither was re-run at the close: there was nothing to re-run.
- **`guppi pretask --check` ends at exit 1, deliberately.** Seven findings stand: one is the
  frontier, written after `ExitPlanMode` because Plan Mode blocks every write but the plan
  file; six are `no contract` and `no method`, the exact checks that 187–190 abolish and that
  case 191 defers the removal of. They are not defects of the plan; they are the difference
  between the two models, and they will stand until Slice 3d is built.
- **The frontier could not be written at `/hi`.** Plan Mode blocks it, and `/hi` is where the
  rule says to write it. Every planning session hits this. It is recorded here rather than as
  a lesson: no ledger line was written for it.
- **The ledger of this session holds ~30 decision lines and one estimate line**, none of them
  covered by a page. `guppi tail` will print every one of them at the next `/hi`. That is the
  honest signal, and it is the second guard after this brief.
- **`sprint.md` was not touched.** Slice 3d is partly taken — 187, 188, 189, 190 ratified,
  three targets re-deferred by 191 — and the sprint line still reads as it did. The next
  librarian updates it.
