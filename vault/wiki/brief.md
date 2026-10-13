# Brief — 2026-10-14, after the librarian run of session 2118

## Where things stand

- Session 2118 (dated 2026-10-13) of the sprint `plugin` ratified Cases 805 (a short defer), 806 (806.1–806.4) and 807 (807.1–807.4). Cases 806 and 807 were ratified twice, before and after `/pre-spec`; the ledger holds each line once, and 806.4 has lines of the second ratification only (handoff, What actually got done; Direct instructions).
- Code: `guppi/ship.py` (a bracket that holds a pointer removed whole, a link to a page left out written as its slug, fenced blocks and `schema.yaml` text masked, `--review`, `--check`, the one judgment `outside`), `guppi/prespec.py` (`check_pointers`), `Makefile` (`guppi ship --check` as the last step of `lint`), and the comments and docstrings of 21 modules of `guppi/`. Tests: `tests/test_ship.py`, `tests/test_lint.py`, `tests/test_prespec.py`. At the end of Work Mode: `make test` 1612 passed, 6 skipped; `make style` clean; `make lint` exit 0 (handoff).
- Readings of the session: ledger lines 1–2 at `/hi`, lines 20–26 at Retro, all nine `passed` (lines 22 and 23 among them); the lesson on ledger line 27 (handoff; yaml).
- The yaml `vault/raw/2026-10-13/2118/materialize.yaml`: 25 entries from a 27-line ledger; line 22 is folded into the `create` entry of line 15 and line 23 into the `create` entry of line 16, so every ledger line is accounted for. `unparsed: []`. The synthesis added 3 entries. All 28 entries and the 11 decisions carry `applied`; none carries `failed`, `incomplete`, `near` or `merged`; the `defer` of line 3 carries `exists: true` (`entity-sprint-plugin` stands). The yamls of 1426 and 1753 were extended with 0 entries. `guppi generate` wrote or changed 33 pages for 2118, 0 for 1426 and 1753, and printed nothing on stderr.
- Created: decisions 11 (805, 806, 806.1–806.4, 807, 807.1–807.4); estimates 2 (`estimate-clean-branch-code-holds-pointers-only-in-brackets`, `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`, both `passed` by their folded readings); lessons 1 (`lesson-case-build-recommended-on-a-claim-about-code-it-did-not-read`); insights 1 (`insight-case-build-claims-what-code-does-without-reading-it`, by the synthesis).
- Updated: rules 8 (`rule-orchestration` 806.1, `rule-case-build` 806.2, `rule-work-mode` 806.3, `rule-where-to-stop` 806.4, `rule-clean-branch` 807.1 and its `estimates` by 807.3, `rule-lint` 807.2, `rule-case-protocol` 807.4, `rule-prespec-hook` its `estimates` by 807.4); estimates 8 (`estimate-orchestration-shows-the-built-case`, `estimate-case-build-writes-the-case`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-clean-branch-writes-a-clean-copy`, `estimate-lint-runs-every-step` by their Cases; `estimate-case-build-judges-by-the-state-at-the-moment`, `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` by their readings); entities 1 (`entity-sprint-plugin`, the defer of 805 and the `change` of 807.1); lessons 1 (`lesson-case-build-reused-judgment-not-checked-against-the-other-side`, clustered).
- Cascade: `rule-case-build` `draft` → `built`; `rule-work-mode` `built` → `draft`. `guppi cleanup` moved 0 pages.
- `guppi render` wrote `.claude/agents/case-guppi.md`, `.claude/skills/work/SKILL.md`, `vault/wiki/orchestration.md`, `vault/wiki/where-to-stop.md` and `vault/wiki/case-schema.md`, and printed nothing on stderr. `guppi sprint`, `guppi backlog` and `guppi glossary` printed nothing on stderr; `vault/wiki/sprint.md` did not change; `backlog.md` went from 4 to 7 items. No unticked line of the Specs holds `guppi sprint-close --apply`; no close ran.
- Handoff check (`entity-sprint-plugin`): the page gained `deferred_by: ["[[decision-case-805]]"]` and two `## History` lines, `deferred · [[decision-case-805]]` and the `change` of 807.1; no other line of the page changed.
- Handoff check (`guppi ship --check` after the render): `make lint` after the render printed 0 lines and exited 0, so its last step printed no red line on `.claude/` or `CLAUDE.md`.
- Ticked by this run: in `vault/raw/2026-10-13/2118/spec.md` 28 of the 29 waiting boxes; in the spec of 1426 the `read` boxes of `estimate-case-build-judges-by-the-state-at-the-moment` and `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`. Unticked after the run: 1 `read` box in the spec of 2118 (line 266), 3 in the spec of 1753 (lines 117, 290, 1275), now `vault/archive/plugin/2026-10-13/1753/raw/spec.md`.
- `guppi archive` moved `raw/2026-10-13/1426` to `archive/plugin/2026-10-13/1426/raw` and `raw/2026-10-13/1753` to `archive/plugin/2026-10-13/1753/raw`; it kept `2118`, the session of the run, and printed nothing on stderr.
- Index check: the two `create` entries are Estimates, born with their Leaf, with no index. The lesson entry: Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 39 lines: none the same page; its cause is shared, as the synthesis says.
- Synthesis: Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 39 lines; Grep `^(pattern|deferred_by):` over `vault/wiki/insights/`, 2 lines.
  - `lesson-case-build-recommended-on-a-claim-about-code-it-did-not-read`: joined `lesson-case-build-reused-judgment-not-checked-against-the-other-side` (live, `new`) under the new `insight-case-build-claims-what-code-does-without-reading-it` (`open`, severity 2): in both case-guppi stated what a function of the code does without reading the function that decides it. `insight-case-build-recommends-without-reading-the-governing-rule` (`actioned`) is about a rule of the vault, not code, and `lesson-case-build-recommended-an-unchecked-github-fact` about a fact of GitHub; neither joined. No lesson entry carries `addressed_by`.

## Readings due

- `estimate-ask-opens-a-decision-only-for-a-finding` — `pending`; target `rule-ask` (`draft`); read box `vault/archive/plugin/2026-10-13/1753/raw/spec.md:117`; method: by hand, after a /pre-spec whose ask-guppi runs on `.claude/agents/ask-guppi.md` as rendered by case 800.2.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `pending`; target `rule-work-mode` (`draft`); read box `vault/raw/2026-10-13/2118/spec.md:266`; method: by hand, after the first /work that runs on the rendered `.claude/skills/work/SKILL.md` and in which a Case is ratified in Work Mode.
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
- `backlog.md`: `entity-sprint-plugin`, the live sprint page, now stands under `## Deferred` by its `deferred_by` of Case 805, and its line shows the page's own `purpose`, not the question Case 805 put off (whether the clean version ships the Estimates of its shipped rules together with `tests/`).
- `backlog.md`: `rule-work-mode` (no `deferred_by`) stands under `## Deferred` as "put off in 31 sessions" since its cascade `built` → `draft`: `deferred` of `guppi/backlog.py` lists a line of the `## Backlog` of an archived sprint page that names it once its page is not finished.
- Handoff observation: `guppi ship` removes a bracket inside a string literal the program prints — the `/hi` hook message of `guppi/sprint.py` loses `(rule-skill-sprint-open, case 743.7)` and a message of `guppi/generate.py` loses `(case 201.1)`; both still read whole.
- Handoff observation: `guppi ship` removes a bracket of code that holds a pointer, such as a call whose argument line carries a comment with a pointer; `--review` is the only guard.
- Handoff observation: the sentence of case 713 that in Work Mode a Case of a later session may replace a ratified Case stands beside the route of 806, which replaces a sub-case in the same Work Mode; the `context` of 806 says why, and a reader may take it for a contradiction.
- Handoff note: Case 807 keeps the exemption of `case-example.md` and of the Render of `rule-case-example` by name, though its `context` says the fence rule alone covers that example.
- Handoff note: the sentence of `## The acknowledging reply` of `rule-orchestration` for Work Mode and `uv.lock` left out of the `then` of 807.1 came after the confirmation run of `ask-guppi`; no agent checked them a second time.
- Read beyond the frame: a Grep of `vault/raw/2026-10-13/1753/ledger.md` and of the `ledger.md` files under `vault/raw/` for `merge-main` and `pr-review`, for the event check of `estimate-skill-merge-main-joins-a-conflicted-page` and `estimate-skill-pr-review-takes-a-pull-request-whole` (Readings due, Next session).

## Next session

### Cases

- The Case of the milestone The clean branch that rewords the pages: the leftovers and the brackets with words under `vault/wiki/` and `.claude/` in `vault/raw/2026-10-13/2118/ship-review.txt`, then a CI run by a tag `prod-*` (handoff, For the next session).
- Whether a bare case number such as `(274.1)` becomes a pointer of the rule, so that `guppi ship` removes it (handoff, For the next session).

### Work

- Read `estimate-ask-opens-a-decision-only-for-a-finding` (box `vault/archive/plugin/2026-10-13/1753/raw/spec.md:117`): the `/pre-spec` of session 2118 dispatched `ask-guppi` (event log `vault/raw/2026-10-14/event_log.md`, `00:07:54 747ffece tool Agent: ask-guppi`) on `.claude/agents/ask-guppi.md` as rendered at commit 6d9afab, the librarian run that applied case 800.2.

### Ask the person

- none

## Readings at the close

- `make test`: 1612 passed, 6 skipped.
- `make lint`: 0 lines, exit 0 (after `guppi archive`).
- Live pages: rules 84, estimates 280, entities 5, insights 3, lessons 40, decisions 118; `vault/archive/`: 2691 `.md` files after `guppi archive`.
