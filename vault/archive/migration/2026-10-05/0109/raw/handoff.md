# Handoff — 2026-10-05, the form and the searches of ask-guppi, the session's make target

## Notes from memory

- Case 638: the person was not sure about the rule on the main agent's confirmation message and chose to try it as planned.
- Case 640: the person chose `.claude/rules/` against the main agent's recommendation of `CLAUDE.md`, as a trial. `rule-page-read` and a lesson doubt that such a file loads in a subagent; if the first reading shows it does not, a later Case moves the text to `CLAUDE.md`.
- At `/pre-spec` the person asked why the Cases are checked one by one and never the Spec as a whole, and said the earlier check of the whole plan worked better. Case 643 puts that off.
- C2 (sprint) and C4 (brief) were one item, the close of migration, from two sources.

## Direct instructions to the librarian

- Cases 638 and 639 both `update` `rule-ask`, in two different paragraphs: 638 the confirmation, 639 the first answer. The new text of 638 points to the paragraph that 639 changes for the form of the list of what was not checked. Check that both `replace` anchors land, and that the render of `.claude/agents/ask-guppi.md` holds both.
- Case 640 creates `rule-search-leaves-out-decisions`, a render rule whose `governs` is `.claude/rules/search-leaves-out-decisions.md`. The folder `.claude/rules/` does not exist yet.
- `estimate-ask-finds` and `estimate-ask-searches-at-prespec` each have a failed reading of this session (ledger L8, L9) and an `update` of this session (639 sets `status: pending`; 640 sets `method` alone). Check the status that each page ends with after `generate`.
- Case 643 is a `defer` with no `ref`: its target `rule-prespec-judges-the-spec-whole` is a new placeholder slug.
- Case 642 defers `entity-sprint-migration`; the sprint page and `guppi sprint` read that page.

## What actually got done

- Cases ratified: 638, 639, 640, 641 — each built again on the findings of `/pre-spec` and ratified again — and the short-form defers 642 and 643.
- Code: `Makefile`, the target `test-session` over `test-session-start`, `test-plan-mode`, `test-end-of-work` and `test-documentation` (641). No test changed.
- `make test`: 1168 passed, 6 skipped. `make style`: clean. `make test-session` ran the four pipelines and passed.
- Readings: L1–L7 passed, L8 and L9 failed, all at `/hi`; L22 failed (`estimate-case-build-checks-the-finished-case`, in Work Mode).
- Lessons: L23, L24, L25.

## Debt

- No box of the Spec is debt. No patch.
- 17 boxes wait for the librarian: the `update`, `create`, `render` and `read` lines of Cases 638–641.
- `estimate-prespec-confirms-the-findings-once` (updated by 638): the `/pre-spec` of a later session whose findings send a Case back, after the render by 638.
- `estimate-ask-finds` (updated by 639): the `/hi` of a later session, the answer of `ask-guppi` at a `/pre-spec` after the render by 639.
- `estimate-search-leaves-out-decisions-in-every-agent` (created by 640): the `/hi` of a later session, the transcripts of a session after the render by 640.
- `estimate-ask-searches-at-prespec` (updated by 640): the `/hi` of a later session, the calls of `ask-guppi` at a `/pre-spec` after the render by 640.
- `estimate-session-phases-in-order` (updated by 641): `make test-session` and the reading by hand at the close of a later session.
- `estimate-ask-query-before-a-create`: a `case-guppi` that builds a Case with a `create` without a `ref`; none did in this session.
- `estimate-case-build-writes-the-case`: live dispatches with a `create` without a `ref`, a change of a hook and a change on one sub-case; this session gave only forks.
- `estimate-spec-write-reaches-the-approved-spec`: a Case ratified in Work Mode.
- `estimate-synthesis-clusters`: a librarian run whose yaml holds at least two lesson entries; this run's may be the first.
- `estimate-hi-writes-frontier`, `estimate-hi-takes-a-conserved-spec`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-brief-written`, `estimate-backlog-renders`, `estimate-sprint-close-next-session-opens-the-sprint`, `estimate-sprint-close-runs-in-the-librarian-run`, `estimate-sprint-close-takes-the-readings-in-groups`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-merges`: the session that closes the sprint, or the one after it.

## Observations

- Red before the work: `make lint` exit 2, 31 finding lines in the Baseline of `work.md` — 4 `deferred`, 26 `unread`, 1 `method` on `estimate-session-phases-in-order`, which Case 641 clears at this run.
- No expected red.
- The hook `guppi onward --plan` said "the Cases built again on the findings of /pre-spec are ratified" after the reply of the defer 643, before any Case had been sent back to its `case-guppi`; it judged the loop after the findings ended while it had not started.
- The ledger hook did not append the decision lines of Cases 638–641 again at their second ratification, since it held them; the plan file took the Cases built again.

## For the next session

- `estimate-case-build-checks-the-finished-case` failed: the four `case-guppi` of this session missed 4 rules at the same moment, 1 page made false, 1 clash and 4 claims of context, all found at `/pre-spec`. Decide what the frame of `case-guppi` changes, or whether the Criterion asks too much of one build.
- The Stop hook `guppi ratified` writes nothing on the reply that answers a refusal (`stop_hook_active`), and `orchestration.md` does not say so: decide whether the rule says it or the hook writes there too.
- The hook `guppi onward --plan` sent the agent to the check and the exit while the loop after the findings had not started: decide whether it is a bug of the hook.

## Ask the person

none
