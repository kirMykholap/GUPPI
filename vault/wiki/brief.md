# Brief — 2026-10-14, after the librarian run of session 0101

## Where things stand

- Session 0101 (dated 2026-10-14) of the sprint `plugin` ratified Cases 808 (808.1, 808.2) and 809. Both were ratified twice, before and after `/pre-spec`; the ledger holds each line once, and the `update` of `entity-sprint-plugin` (ledger line 54) comes from the second ratification of 809 only (handoff, What actually got done; Notes from memory).
- Code: `guppi/ship.py` gained `bare_numbers`, the one judgment of a bare case number in a comment or a docstring of a Python file, read by `tokenize`; `leftovers` adds its lines for a `.py` file, so `guppi ship`, `--review` and `--check` exit 1 on one. The comments and docstrings of `guppi/casecheck.py`, `cleanup.py`, `gate.py`, `generate.py`, `ledger.py`, `lint.py`, `materialize.py`, `onward.py`, `prespec.py` and `ratified.py` write each case number with its word. Tests: `tests/test_ship.py`, three new tests. At the end of Work Mode: `make test` 1615 passed, 6 skipped; `make style` clean; `uv run guppi ship --check` printed no line (handoff).
- Readings of the session: ledger lines 55–57, all three `passed`; the lesson on ledger line 58 (handoff; yaml).
- The yaml `vault/raw/2026-10-14/0101/materialize.yaml`: 58 entries from a 58-line ledger, one entry per line, so every ledger line is accounted for; 4 decisions (808, 808.1, 808.2, 809). The yaml of 2118 was extended with 0 entries. All 58 entries and the 4 decisions carry `applied`; none carries `failed`, `incomplete`, `exists`, `near` or `merged`. `guppi generate` wrote or changed 61 pages for 0101, 0 for 2118, and printed nothing on stderr.
- Created: decisions 4 (`decision-case-808`, `decision-case-808.1`, `decision-case-808.2`, `decision-case-809`); estimates 1 (`estimate-clean-branch-pages-hold-pointers-only-in-brackets`, `pending`); lessons 1 (`lesson-caseid-held-no-id-without-the-session-option`, `new`).
- Updated: rules 48 by entries (`rule-clean-branch` by 808.1 and its `estimates` by 809; 47 rules reworded by 809); entities 3 (`entity-glossary`, `entity-sprint`, `entity-sprint-plugin`, all by 809); estimates 3 (`estimate-clean-branch-writes-a-clean-copy` by 808.1 and its reading, `estimate-clean-branch-code-holds-pointers-only-in-brackets` by 808.2 and its reading, `estimate-ask-opens-a-decision-only-for-a-finding` by its reading).
- Cascade: `rule-ask` `draft` → `built`; `rule-clean-branch` `built` → `draft`. `guppi cleanup` moved 0 pages.
- `guppi render` wrote `vault/wiki/case-schema.md`, `vault/wiki/orchestration.md`, the `schema.yaml` of the six categories, `.claude/agents/librarian-guppi.md` and the `SKILL.md` of `hi`, `carry`, `retro` and `work`, and printed nothing on stderr. `guppi sprint`, `guppi backlog` and `guppi glossary` printed nothing on stderr; `vault/wiki/sprint.md` changed in the line of the milestone The clean branch (the text of 809 and `draft, pending`); `backlog.md` did not change. No unticked line of the Specs holds `guppi sprint-close --apply`; no close ran.
- Handoff check (809 entries): none of the 51 entries of Case 809 carries `failed` or `incomplete`.
- Handoff check (`rule-page-generation`, `rule-work-mode`): both still stand under `## Deferred` of `backlog.md`, and `backlog.md` did not change.
- Handoff check (`rule-clean-branch`): the page carries the `replace` of 808.1 and the new Estimate in its `estimates` by 809, each with its `## History` line.
- Handoff check (`guppi ship --check` after the render): `make lint` after the render printed 0 lines and exited 0.
- Ticked by this run: in `vault/raw/2026-10-14/0101/spec.md` 70 boxes. Unticked after the run: line 652 (`read estimate-clean-branch-pages-hold-pointers-only-in-brackets`); in the spec of 2118 line 266, now `vault/archive/plugin/2026-10-13/2118/raw/spec.md`; in `vault/archive/plugin/2026-10-13/1753/raw/spec.md` lines 117, 290, 1275.
- `guppi archive` moved `raw/2026-10-13/2118` to `archive/plugin/2026-10-13/2118/raw`; it kept `2026-10-14/0101`, the session of the run, and printed nothing on stderr. No `pending` Estimate's `method` names the archive step.
- Index check: the one `create` entry other than the lesson is an Estimate, born with its Leaf, with no index; no Grep of a category was run for it.
- Synthesis: Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 40 lines; Grep `^(pattern|deferred_by):` over `vault/wiki/insights/`, 3 lines.
  - `lesson-caseid-held-no-id-without-the-session-option`: none — no index line names `guppi caseid` or a command that `orchestration.md` gives without an option its script needs to find the session; it stays `new`.

## Readings due

- `estimate-clean-branch-pages-hold-pointers-only-in-brackets` — `pending`; target `rule-clean-branch` (`draft`); read box `vault/raw/2026-10-14/0101/spec.md:652`; method: by hand, after the librarian's run that applies case 809, the lines of `uv run guppi ship --review` into an empty temporary folder on `vault/wiki/` and `.claude/`. This run: `guppi generate` applied all 51 entries of Case 809; no step of this run ran `guppi ship --review`; `make lint`, whose last step is `guppi ship --check`, printed 0 lines and exited 0 after the render.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `pending`; target `rule-work-mode` (`draft`); read box `vault/archive/plugin/2026-10-13/2118/raw/spec.md:266`; method: by hand, after the first /work that runs on the rendered `.claude/skills/work/SKILL.md` and in which a Case is ratified in Work Mode.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `pending`; target `rule-morph` (`draft`); read box `vault/archive/plugin/2026-10-13/1753/raw/spec.md:290`; method: by hand, after the session whose Work Mode builds the install skill of rule-morph.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; target `entity-sprint-plugin` (`draft`); read box `vault/archive/plugin/2026-10-13/1753/raw/spec.md:1275`; method: by hand, in a session of the sprint plugin before its close, the CI run that a tag `prod-*` on a commit of `plugin` starts, its push with the deploy key of `PROD_DEPLOY_KEY`, the branch `prod` it wrote and the `on:` block of `.github/workflows/prod.yml`.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); method: the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of /sprint-open.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); method: by hand, after the first /merge-main whose merge of main leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); method: by hand, after the first pull request from an account other than the owner's is merged into main by /pr-review after the close of plugin.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, a pull request from a second account read on GitHub, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, an install of the clean branch into an empty project, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin` (`draft`); method: the person's answer on README.md at the /hi of the session after the one whose Work Mode writes README.md under the milestone The plugin, before the close of the sprint.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, at the end of Work Mode of the session that closes entity-sprint-plugin.

## Flags

- No entry is marked `incomplete`, `failed`, `near` or `unparsed`. No Estimate is `failed`.
- `make lint`: 0 lines, exit 0.
- The `read` box of `estimate-ask-opens-a-decision-only-for-a-finding` at `vault/archive/plugin/2026-10-13/1753/raw/spec.md:117` stays unticked, though this run applied its `passed` reading (ledger line 55).
- Handoff note: the `ask-guppi` run on Case 809 read the sentence around each `new` whole for six pages only, and did not count each hit of each `old` on its own; `guppi generate` failed none of the 51 entries of 809.
- Handoff observation: `uv run guppi ship --review` still lists `(split it, case 472.3)` in `guppi/prespec.py` and `(case 320: no file route)` in `guppi/materialize.py`, brackets whose words add to the sentence and which the clean copy drops; the reading of session 2118 accepted the same 31 lines.
- Handoff observation: a comment that was a case number alone, such as `# 786`, needed words of its own, since the copy would hold an empty `#` once its bracket goes.

## Next session

### Cases

- Whether the bare-number judgment also takes an opening of a list of case numbers and a colon, such as `387.4, 445.4:` (handoff, For the next session).
- Whether `guppi/caseid.py` takes the session stamp from the newest `hi:` line when `--session` is not given, or `orchestration.md` names `--session <id>` in the command it gives (handoff, For the next session; `lesson-caseid-held-no-id-without-the-session-option`).

### Work

- Read `estimate-clean-branch-pages-hold-pointers-only-in-brackets` (box `vault/raw/2026-10-14/0101/spec.md:652`): the librarian's run of 2026-10-14 applied Case 809.

### Ask the person

- none

## Readings at the close

- `make test`: 1615 passed, 6 skipped.
- `make lint`: 0 lines, exit 0.
- Live pages: rules 84, estimates 281, entities 5, insights 3, lessons 41, decisions 122; `vault/archive/`: 2698 `.md` files after `guppi archive`.
