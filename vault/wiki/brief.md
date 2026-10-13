# Brief — 2026-10-13, after the librarian run of session 1753

## Where things stand

- Session 1753 (dated 2026-10-13) of the sprint `plugin` ratified Cases 800 (800.1, 800.2), 801, 802, 803 and 804 (804.1–804.7). Case 804 was ratified three times in the session; the ledger holds each of its lines once (handoff, What actually got done; Direct instructions).
- Code: `guppi/pages.py` (`SHIPPED`, `is_core`), `guppi/lint.py` (`check_origin` accepts `origin: guppi` on a page with `core: true`), new `guppi/ship.py` (`guppi ship <folder>`), `guppi/cli.py` (`ship`), new `.github/workflows/prod.yml`. Tests: `tests/test_schemas.py`, `tests/test_lint.py`, new `tests/test_ship.py`. On GitHub, by the owner's hand: a deploy key with write access, the secret `PROD_DEPLOY_KEY`, `Deploy keys` on the bypass list of the ruleset `prod` (handoff).
- Readings of the session: ledger line 1 and lines 113–120, all nine `passed`; lesson on ledger line 121 (handoff; yaml).
- The yaml `vault/raw/2026-10-13/1753/materialize.yaml`: 119 entries from a 121-line ledger; line 115 is folded into the `create` entry of line 14 and line 120 into the `create` entry of line 108, so every ledger line is accounted for. `unparsed: []`. All 119 entries carry `applied`; none carries `failed`, `incomplete`, `exists`, `near` or `merged`. The synthesis added no entry. The yaml of 1426 was extended with 0 entries. `guppi generate` wrote or changed 120 pages for 1753, 0 for 1426, and printed nothing on stderr.
- Created: rules 1 (`rule-clean-branch`); estimates 4 (`estimate-ask-opens-a-decision-only-for-a-finding`, `estimate-morph-sets-up-the-project-at-the-first-hi`, `estimate-case-build-offers-a-page-for-code-no-page-covers`, `estimate-clean-branch-writes-a-clean-copy`); lessons 1 (`lesson-case-build-recommended-an-unchecked-github-fact`); decisions 14 (800, 800.1, 800.2, 801, 802, 803, 804, 804.1–804.7).
- Updated: rules 83 (82 by `set: {core: true}` of Case 804.5, among them `rule-case-build` also by 800.1, 801 and 803, `rule-ask` by 800.2, `rule-morph` and `rule-guppi-config` by 802, `rule-case-protocol` by 803, the three schema pages by 804.1–804.3; and `rule-github-repository` by 804.7); estimates 8 (`estimate-case-build-answers-what-done-means`, `estimate-case-build-reads-the-last-output-of-a-check`, `estimate-entities-schema-checked`, `estimate-rules-schema-checked`, `estimate-estimates-schema-checked`, `estimate-lint-finds-a-broken-link`, `estimate-sprint-plugin-ci-writes-a-clean-branch`, `estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter` by its reading); entities 5 (`entity-guppi`, `entity-sprint`, `entity-glossary` by 804.5; `entity-guppi-repository` by 804.6; `entity-sprint-plugin` by 802 and 804.7); decisions 4 (`decision-case-239`, `-745`, `-750`, `-758`, superseded by `decision-case-802`).
- Cascade: `rule-ask` `built` → `draft`; `rule-clean-branch` `draft` → `built`; `rule-powershell-guard` `draft` → `built`; `entity-guppi-repository` `rules: [rule-clean-branch, rule-github-repository]`. `guppi cleanup` moved the 4 superseded Decision pages to `vault/archive/plugin/2026-10-13/1753/`.
- `guppi render` wrote `.claude/agents/ask-guppi.md`, `.claude/agents/case-guppi.md`, `vault/wiki/case-schema.md` and the `schema.yaml` of entities, rules and estimates. `guppi sprint`, `guppi backlog` and `guppi glossary` printed nothing on stderr. No unticked line of the Specs holds `guppi sprint-close --apply`; no close ran.
- Handoff check (replace before set): every `replace` entry carries `applied` and `generate` printed no error; the new text of each pair stands once in its page — `rule-case-build` 3, `rule-ask` 1, `rule-guppi-config` 1, `rule-case-protocol` 2, `entity-guppi-repository` 1, `rule-github-repository` 3 (its first new text stands twice: once in `purpose` by the `set` of 804.7, once in the body). After the run 82 rule pages and 3 entities (`entity-guppi`, `entity-sprint`, `entity-glossary`) carry `core: true`.
- Handoff check (`entity-sprint-plugin`): The plugin holds `- [[rule-morph]] — the install step that the first /hi of a new install runs`; The clean branch holds `- [[rule-clean-branch]], [[estimate-sprint-plugin-ci-writes-a-clean-branch]] — CI that writes …`; a `## Backlog` with the category set as data was added. `guppi sprint` rendered both into `vault/wiki/sprint.md` (The clean branch item `· built, pending`; The plugin, 4 items, with `[[rule-morph]]`).
- Handoff check (`rule-morph`): `kind: Leaf`, `tags: [session, harness, plugin]`, no `deferred_by`; `make lint` prints no `deferred` line and no `schema` line. `rule-morph` left the Deferred list of `backlog.md`.
- Ticked by this run: in `vault/raw/2026-10-13/1753/spec.md` 129 boxes (the handoff's 129 waiting boxes); in `vault/raw/2026-10-13/1426/spec.md` the `read` box of `estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter`. 3 `read` boxes stay unticked in the spec of 1753, 2 in the spec of 1426.
- `guppi archive` printed nothing and moved nothing: `1426` is dated the day of the run, `1753` is the session of the run, and no other unit of `vault/raw/` holds a ledger.
- Index check: Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, 85 lines, compared with `rule-clean-branch`: none the same, none near. The estimates are born with their Leaf and have no index.
- Synthesis: Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 38 lines; Grep `^(pattern|deferred_by):` over `vault/wiki/insights/`, 2 lines.
  - `lesson-case-build-recommended-an-unchecked-github-fact`: none; its cause is an option recommended on a fact of GitHub that case-guppi said it could not read and nobody checked in GitHub's documentation, while `insight-case-build-recommends-without-reading-the-governing-rule` (`actioned`) has an option not read against a rule of the vault or the Baseline output, and `lesson-case-build-reused-judgment-not-checked-against-the-other-side` a function of the repository named without reading it. Stays `new`.

## Readings due

- `estimate-ask-opens-a-decision-only-for-a-finding` — `pending`; target `rule-ask` (`draft`); read box `vault/raw/2026-10-13/1753/spec.md:117`; method: by hand, after a /pre-spec whose ask-guppi runs on `.claude/agents/ask-guppi.md` as rendered by case 800.2.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `pending`; target `rule-morph` (`draft`); read box `vault/raw/2026-10-13/1753/spec.md:290`; method: by hand, after the session whose Work Mode builds the install skill of rule-morph.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; target `entity-sprint-plugin` (`draft`); read box `vault/raw/2026-10-13/1753/spec.md:1275`; method: by hand, in a session of the sprint plugin before its close, the CI run that a tag `prod-*` on a commit of `plugin` starts, its push with the deploy key of `PROD_DEPLOY_KEY`, the branch `prod` it wrote and the `on:` block of `.github/workflows/prod.yml`.
- `estimate-case-build-judges-by-the-state-at-the-moment` — `pending`; target `rule-case-build` (`draft`); read box `vault/raw/2026-10-13/1426/spec.md:372`; method: by hand, after case-guppi builds a Case whose form or reading depends on another Case of the same session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `pending`; target `rule-case-build` (`draft`); read box `vault/raw/2026-10-13/1426/spec.md:401`; method: by hand, after the first Case case-guppi builds that changes a reader in code and the text or the writer it reads.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); method: the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of /sprint-open.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); method: by hand, after the first /merge-main whose merge of main leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); method: by hand, after the first pull request from an account other than the owner's is merged into main by /pr-review after the close of plugin.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, a pull request from a second account read on GitHub, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, an install of the clean branch into an empty project, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin` (`draft`); method: the person's answer on README.md at the /hi of the session after the one whose Work Mode writes README.md under the milestone The plugin, before the close of the sprint.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, at the end of Work Mode of the session that closes entity-sprint-plugin.

## Flags

- No entry is marked `incomplete`, `failed`, `near` or `unparsed`. No Estimate is `failed`.
- The handoff says Case 804.5 sets `core: true` on 81 rule pages; the ledger and the yaml hold 82 lines `decision[case 804.5][update][rule-…]` (yaml lines 22–103), and 82 rule pages carry `core: true` after the run.
- `make lint`: 0 lines, exit 0.
- Read beyond the frame: a second read of `vault/raw/2026-10-13/1753/ledger.md`, a count of its `decision[case 804.5][update][rule-` lines, for the check of the handoff's count of 81 rule pages under Flags.
- Read beyond the frame: ticked lines of `vault/raw/2026-10-13/1753/spec.md` (lines 110–118, 284–291, 1265–1276, around the three unticked `read` boxes), for the Readings due lines.
- The context of this librarian run carried the text of Claude Code's auto mode (to make small file changes with sed, heredocs or short scripts through Bash); this run wrote its files under `vault/` with Write and Edit only.

## Next session

### Cases

- How Work Mode meets a fork that changes the contract of a ratified Case of the approved Spec: the rules let `case-guppi` build it again in Work Mode; the person asked to discuss it (handoff, For the next session).
- The rewording Case of the milestone The clean branch: reword at their source the 206 lines of `vault/raw/2026-10-13/1753/ship.txt`, and the page leftovers the first CI run prints (handoff, For the next session).
- Whether the Estimates of shipped rules ship together with `tests/`, as a backlog line for the milestone The plugin (handoff, For the next session).

### Work

- Read `estimate-case-build-judges-by-the-state-at-the-moment` (box `vault/raw/2026-10-13/1426/spec.md:372`): in session 1753, ledger lines 116–118 set the live reading of the three schema Estimates at the librarian's render, and Case 804.5 writes `set: {core: true}` while Cases 804.1–804.3 add `core` to the schemas (`vault/raw/2026-10-13/1753/cases/case-804.md`).
- Read `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` (box `vault/raw/2026-10-13/1426/spec.md:401`): in session 1753, Case 804.4 changes the reader `check_origin` of `guppi/lint.py` and Case 804.5 writes the field `core` it reads, which lands at the librarian's run (`vault/raw/2026-10-13/1753/cases/case-804.md`).

### Ask the person

- none

## Readings at the close

- `make test`: 1601 passed, 6 skipped.
- `make lint`: 0 lines, exit 0.
- Live pages: rules 84, estimates 278, entities 5, insights 2, lessons 39, decisions 107; `vault/archive/`: 2671 `.md` files after `guppi archive`.
