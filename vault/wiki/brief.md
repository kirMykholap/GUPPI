# Brief — 2026-10-13, after the librarian run of session 2349

## Where things stand

- Session 2349 (dated 2026-10-12) of the sprint `plugin` ratified Cases 785, 786 (786.1, 786.2), 787.2, 788 (788.1–788.7), 789 (789.1–789.3), 790, 791, 793 (a defer) and 794; Case 787.1 is superseded by 794 (handoff, What actually got done).
- Code: `guppi/materialize.py`, `guppi/generate.py`, `guppi/prespec.py`, `guppi/lint.py` (786); new `guppi/caseid.py` (`guppi caseid --next`), `guppi/casecheck.py`, `guppi/ratified.py`, `guppi/gate.py`, `guppi/box.py`, `guppi/ledger.py`, `guppi/cli.py` (788); `.gitattributes` with `merge=union` for `vault/wiki/log.md` and `vault/wiki/tags.md` (790); `.github/workflows/checks.yml` and the history sentence of `README.md` (787, 794) (handoff).
- GitHub: public repository `kirMykholap/GUPPI`, history cut at the commit that removed the former product; `main` and `plugin` pushed; rulesets `main` and `prod`; first CI run on `plugin`: `style` and `test` passed, `lint` failed on the 8 lines of the local Baseline (handoff).
- Readings of the session: ledger lines 44–56, all `passed`; lessons on ledger lines 57–59 (handoff).
- The yaml `vault/raw/2026-10-12/2349/materialize.yaml`: 59 entries from a 59-line ledger; lines 47 and 48 are folded into the `create` entries of lines 14 and 18, so every ledger line is accounted for. 6 entries added by the synthesis. `unparsed: []`. No entry carries `failed`, `near` or `merged`. Line 31 (defer of `rule-page-generation`, case 793) carries `exists: true`. Lines 8, 9 and 32 (case 787.1) carry `superseded_by: 794`. Line 41 carries `incomplete: [parent]`. The yamls of 1449, 1604 and 2252 were extended with 0 entries. `guppi generate` wrote or changed 64 pages for 2349, 0 for the others.
- Created: rules 3 (`rule-github-repository`, `rule-skill-pr-review`, `rule-skill-merge-main`); estimates 4 (`estimate-skill-sprint-open-refuses-a-taken-sprint-id`, `estimate-ratification-case-id-carries-the-sprint`, `estimate-skill-pr-review-takes-a-pull-request-whole`, `estimate-skill-merge-main-joins-a-conflicted-page`); lessons 3; insights 1 (`insight-case-build-recommends-without-reading-the-governing-rule`, synthesis); decisions 23 (785, 786, 786.1, 786.2, 787, 787.1, 787.2, 788, 788.1–788.7, 789, 789.1–789.3, 790, 791, 793, 794).
- Updated: rules 13 (`rule-case-build`, `rule-decisions-schema`, `rule-documentation`, `rule-git-context`, `rule-ledger-write`, `rule-orchestration`, `rule-page-generation`, `rule-plan-mode` (children `rule-skill-pr-review`, `rule-skill-merge-main`), `rule-ratification`, `rule-skill-sprint-close`, `rule-skill-sprint-open`, `rule-vault-layout`, `rule-where-to-stop`); estimates 13; entities 2 (`entity-glossary`, `entity-sprint-plugin`); insights 1 (`insight-workflow-code-live-before-the-page-it-reads`); lessons 1 (`lesson-case-build-recommended-a-trigger-that-keeps-the-defect`).
- `guppi archive` moved `raw/2026-10-12/1449`, `1604` and `2252` to `archive/plugin/2026-10-12/<HHMM>/raw`; it kept `2349`, the session of this run.
- `guppi cleanup` moved 1 page: `decision-case-787.1` to `vault/archive/plugin/2026-10-13/2349/decisions/`.
- Handoff check (Direct instructions, first line): `rule-github-repository` was created once, from case 794 (its History holds one `created` line, `decision-case-794`); the 787.1 entries were not applied. `entity-sprint-plugin` lost `### The sprint turn and GitHub` from `## Milestones` and holds it once in the new `## Closed`.
- Handoff check (second line): every `replace` entry of `rule-skill-sprint-open` (788.1, 788.3, 789.1), `rule-page-generation` and `entity-glossary` (786.1, 790) and `rule-orchestration` (786.2, 788.2) carries `applied` and none carries `failed`.
- Handoff check (fourth line): `rule-ratification` was updated by 788.2.
- Ticked by this run in `vault/raw/2026-10-12/2349/spec.md`: every page, render, glossary and sprint box and the `read` boxes of the 13 passed readings; 4 `read` boxes stay unticked. No unticked line of the spec holds `guppi sprint-close --apply`; no close ran.
- Index check: Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, 80 lines; compared with `rule-github-repository` (cases 787.1 and 794), `rule-skill-pr-review` and `rule-skill-merge-main`: no page is the same, none near.
- Synthesis: Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 35 lines; Grep `^(pattern|deferred_by):` over `vault/wiki/insights/`, 1 line.
  - `lesson-case-build-made-an-always-red-check-required`: joined `lesson-case-build-recommended-a-trigger-that-keeps-the-defect` in the new Insight `insight-case-build-recommends-without-reading-the-governing-rule` (`open`, severity 2); both lessons `clustered`.
  - `lesson-case-build-chose-a-key-its-own-session-adds`: joined `insight-workflow-code-live-before-the-page-it-reads` (`open`, kept); lesson `clustered`.
  - `lesson-work-mode-edited-a-source-file-through-the-shell`: none; the nearest line, `lesson-bash-tool-heredoc-escapes-interpreted`, has as its cause how the shell layer treats escapes, not an agent's choice of the shell over the Edit tool. Stays `new`.

## Readings due

- `estimate-ask-finds` — `pending`; target `rule-ask` (`draft`); read box `vault/archive/plugin/2026-10-12/2252/raw/spec.md:124`; method: by hand, after a /pre-spec whose ask-guppi runs on `.claude/agents/ask-guppi.md` as rendered by case 782: the answer of ask-guppi in its agent transcript read against the Criterion and the event log.
- `estimate-git-context-current` — `pending`; target `rule-git-context` (`draft`); read box `vault/raw/2026-10-12/2349/spec.md:294`; method: by hand, after the first /hi that follows the first push to GitHub.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); read box `vault/archive/plugin/2026-10-12/1604/raw/spec.md:549`; method: the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of /sprint-open.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); read box `vault/raw/2026-10-12/2349/spec.md:1145`; method: by hand, after the first /merge-main whose merge of main leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); read box `vault/raw/2026-10-12/2349/spec.md:910`; method: by hand, after the first pull request from an account other than the owner's is merged into main by /pr-review after the close of plugin.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin` (`draft`); read box `vault/raw/2026-10-12/2349/spec.md:1353`; method: by hand, a pull request from a second account read on GitHub, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, a CI run on GitHub and the clean branch it wrote, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, an install of the clean branch into an empty project, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin` (`draft`); method: the person's answer on README.md at the /hi of the session after the one whose Work Mode writes README.md under the milestone The plugin, before the close of the sprint.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, at the end of Work Mode of the session that closes entity-sprint-plugin.

## Flags

- `incomplete`: line 41 of the 2349 yaml, the `create` of `rule-github-repository` (case 794), lacks `parent`; the page was written without it.
- `superseded`: lines 8, 9 and 32 (case 787.1) were not applied; `decision-case-787.1` was written and moved to the archive by `guppi cleanup`.
- No entry is marked `failed`, `near` or `unparsed`. No Estimate is `failed`.
- Stale defer: `rules/rule-morph: deferred: 4 times since case 239` (lint).
- Handoff `## For the next session`, its last line ("The test pull request from a second account against `main`, to read `estimate-sprint-plugin-pull-requests-reviewed-on-github`"), names a reading whose target is the live sprint page; it stands in Readings due alone and in no list of Next session (rule-brief, case 772.1).
- `make lint`, 12 lines (the handoff names 8 at the Baseline; the orphan line and three `unread: pending` lines, `estimate-git-context-current`, `estimate-skill-merge-main-joins-a-conflicted-page`, `estimate-skill-pr-review-takes-a-pull-request-whole`, come from this run's pages):
  - `rules/rule-github-repository: orphan: no other live page names it in its frontmatter`
  - `rules/rule-morph: deferred: 4 times since case 239`
  - `estimates/estimate-ask-finds: unread: pending`
  - `estimates/estimate-git-context-current: unread: pending`
  - `estimates/estimate-hi-writes-frontier: unread: pending`
  - `estimates/estimate-skill-merge-main-joins-a-conflicted-page: unread: pending`
  - `estimates/estimate-skill-pr-review-takes-a-pull-request-whole: unread: pending`
  - `estimates/estimate-sprint-plugin-ci-writes-a-clean-branch: unread: pending`
  - `estimates/estimate-sprint-plugin-close-steps-run-from-the-line: unread: pending`
  - `estimates/estimate-sprint-plugin-installs-as-a-plugin: unread: pending`
  - `estimates/estimate-sprint-plugin-pull-requests-reviewed-on-github: unread: pending`
  - `estimates/estimate-sprint-plugin-readme-describes-the-project: unread: pending`

## Next session

### Cases

- The cause of `lesson-case-build-made-an-always-red-check-required`: `case-guppi` recommended a required check without reading what `make lint` prints at the Baseline or `rule-lint` (handoff, For the next session).
- The cause of `lesson-case-build-chose-a-key-its-own-session-adds`: a Case may not use a form of an update that only its own session's Work Mode makes valid; it clusters with `insight-workflow-code-live-before-the-page-it-reads` (handoff, For the next session).
- The cause of `lesson-work-mode-edited-a-source-file-through-the-shell` (handoff, For the next session).
- The milestone The clean branch is now the current one: CI that writes `prod`, and whether `prod` leaves out `.github/` and `rule-github-repository`; the CI writer goes into the bypass list of the ruleset on `prod` (handoff, For the next session).
- Defect: `rule-github-repository` has no parent — the decision line of case 794 named none (yaml line 41, `incomplete: [parent]`), and `make lint` prints it as an orphan.

### Work

- Read `estimate-ask-finds` (box `vault/archive/plugin/2026-10-12/2252/raw/spec.md:124`): the /pre-spec of session 2349 ran ask-guppi after the render of case 782 (commit 279c853; handoff, Observations).

### Ask the person

- none

## Readings at the close

- `make test`: 1563 passed, 6 skipped.
- `make lint`: 12 lines, listed under Flags.
- Live pages: rules 82, estimates 271, entities 4, insights 2, lessons 38, decisions 84; `vault/archive/`: 2651 `.md` files after `guppi archive`.
