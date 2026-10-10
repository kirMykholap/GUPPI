# Handoff — 2026-10-10, sprint plugin: the checks that wait for the sprint, the opening before the Frontier, the sprint of cleanup

## Notes from memory

- The person asked why so many `W` lines stayed open after the sprint was opened. The answer was that a `W` line closes only by a reading or a Case. That question led to Case 764, later Case 772.
- The person agreed to every recommended option of every round and of the pre-spec report. No answer of the person's own changed a Case.
- C5 of the Frontier, the form of the opening of a sprint, was merged into the milestone line C1 at the person's question. Case 769 settled that form, and the milestone line stays open for the merge step and the close of `plugin`.
- Retro left the four checks of `entity-sprint-plugin` that this session updates `pending`, by Case 772.2, though the rendered `/retro` of this session still sets an unread Estimate `failed`. The ratified contract was taken over the text that renders only at the librarian's run.

## Direct instructions to the librarian

- Case 764 and its sub-cases are superseded by Case 772. The file `cases/case-764.md` stands unchanged, and its decision lines stand in the ledger beside the lines of Case 772, which carry `{supersedes:case 764}` and `{supersedes:case 764.N}`.
- Cases 765 to 770 were ratified twice: once before `/pre-spec`, and again after `case-guppi` built them anew on its findings. The ledger holds each of their lines once. Their content is the one in the Spec.
- `rule-skill-sprint-open` is both changed by Case 769.1 and deferred by Case 771, for two different questions: the order of the opening, and the merge step. Both apply.
- Check first that `.claude/skills/retro/SKILL.md`, `.claude/skills/handoff/SKILL.md`, `.claude/agents/librarian-guppi.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/sprint-open/SKILL.md`, `vault/wiki/orchestration.md` and `vault/wiki/case-schema.md` render with the new texts. This run's brief is written from the old text of `rule-brief`, so the checks of `entity-sprint-plugin` may still stand under its `Work`.

## What actually got done

- Ratified: Cases 765, 766, 767, 768, 769 (769.1 to 769.5), 770, 771 (a defer of `rule-skill-sprint-open` and `rule-skill-sprint-close`) and 772 (772.1 to 772.5).
- Code: `guppi/materialize.py`, `guppi/archive.py`, `guppi/generate.py`, `guppi/cleanup.py`, `guppi/ledger.py`, `guppi/lint.py`, `guppi/prespec.py`, `guppi/sprint.py`, `guppi/sprint_close.py`, `guppi/backlog.py`.
  - `unit_sprint` is now the one judgment of a unit's sprint.
  - `SPRINT_PAGE` and `is_sprint_page` in `guppi/ledger.py` are the one judgment of a sprint page.
  - `ANOTHER_SESSION` catches a session of a sprint and the session that closes one.
  - Pre-spec spares an Estimate of a sprint page.
- Tests: `tests/test_cleanup.py` (2 new), `tests/test_lint.py` (2 new methods in the predicate test), `tests/test_prespec.py` (2 new).
- Migration: `decision-case-757` and `decision-case-759` moved from `vault/archive/migration/2026-10-10/1713/decisions/` to `vault/archive/plugin/2026-10-10/1713/decisions/`. The empty folder of 1713 under `migration` is gone.
- `make test`: 1494 passed, 6 skipped. `make style`: clean.
- Readings: ledger lines 35 to 43, all `passed`. Lessons: ledger lines 44 and 45.

## Debt

- No box of the Spec is debt.
- 39 boxes wait for the librarian: the page lines, the `guppi render` lines and the `read` lines whose readings stand in the ledger.
- `estimate-sprint-plugin-readme-describes-the-project`: its work is not done. It waits for the Retro of the session of sprint `plugin` whose Work Mode writes `README.md`, which names it under `## Ask the person`.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github`: its work is not done. It waits for the Retro of the session that sets up the repository on GitHub, or for the close of `plugin`.
- `estimate-sprint-plugin-ci-writes-a-clean-branch`: its work is not done. It waits for the Retro of the session that finishes the milestone The clean branch, or for the close of `plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin`: its work is not done. It waits for the Retro of the session that finishes the milestone The plugin, or for the close of `plugin`.
- `estimate-sprint-plugin-close-steps-run-from-the-line`: it waits for the end of Work Mode of the session that closes `plugin`.

## Observations

- `make lint` before and after the work printed the same 8 lines, red before the work: the defer count of `rule-morph`, and 7 `unread: pending` lines. No expected red: no check changed by this session reads a page that this Spec updates.
- The first build of Case 765 set the README reading at Retro, though Retro asks the person nothing. Pre-spec caught it, and the reading moved to the `/hi` after the session that writes the README.
- Pre-spec found that Case 766 meant one thing in its History line while keeping a Criterion that said another. It also found that its pull request targeted `main`, which does not move before the close. The Case was built again with a Criterion replaced whole, targeting `plugin`.
- `backlog.py` imported the `PREFIX` constant from `guppi/sprint.py`, a fifth user of the sprint-page constant that the Case did not name. It now imports `SPRINT_PAGE` from `guppi/ledger.py`.

## For the next session

- The milestone line "the opening and the close of a sprint run with no fix by hand and each flaw found in them is fixed" stays open. Its open flaw is the merge step at the opening of a sprint, deferred by Case 771, and the close of `plugin` is not yet run.
- The milestone line "the repository on GitHub set up so that a pull request from another person is easy to review" was put off untouched.
- The method of `estimate-sprint-close-next-session-opens-the-sprint` no longer names a transcript, by Case 769.5. The earlier wish of the person, to fix that method by a later Case before the close of `plugin`, is settled by that Case.

## Ask the person

- `estimate-hi-writes-frontier` — needs the person — in the session after the close of `plugin`, at the reply that acknowledges the opening Case of `/sprint-open`: did the Frontier come out as the Criterion says, with the opening line first and closed by the opening Case, and the items of the first milestone taken from the opening Case?
- `estimate-brief-written` — needs the person — at the `/hi` after the librarian's run of the session that closes `plugin`, on that brief and the one before it: does `Cases` of Next session hold each contradiction of Flags once, and do `Work` and `Ask the person` leave out a reading of the live sprint page whose work is not done, and one whose method names the close of a sprint, except in the brief of the closing run?
