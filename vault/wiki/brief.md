# Brief — 2026-10-13, after the librarian run of session 1426

## Where things stand

- Session 1426 (dated 2026-10-13) of the sprint `plugin` ratified Cases 795 (795.1, 795.2), 796 (796.1, 796.2), 797 (797.1, 797.2), 798 (798.1, 798.2) and 799. Cases 796–799 were built again on the findings of `/pre-spec` and ratified again with the same decision lines (handoff, What actually got done).
- Code: `guppi/materialize.py` (`create_lacks` judges the parent of a Leaf rule, with its `ref` or `applies_to`); `guppi/prespec.py`; `guppi/bashguard.py` (`interpreter`, the third reason `it feeds <interpreter>`); new `guppi/powershellguard.py`; `guppi/cli.py` (`powershellguard`); `guppi/lint.py` (`waits_for_a_later_moment`). Tests: `tests/test_prespec.py`, `tests/test_bashguard.py`, new `tests/test_powershellguard.py`, `tests/test_lint.py`. Page by hand: `## How it works` removed from `rule-bash-guard` (Case 796.1) (handoff).
- Readings of the session: ledger lines 22–28, six `passed` and one `failed` (line 28); lessons on ledger lines 29 and 30 (handoff).
- The yaml `vault/raw/2026-10-13/1426/materialize.yaml`: 29 entries from a 30-line ledger; line 28 is folded into the `create` entry of line 19, so every ledger line is accounted for. `unparsed: []`. All 29 entries carry `applied`; none carries `failed`, `incomplete`, `exists` or `merged`; one carries `near` (line 8). The synthesis added no entry. The yaml of 2349 was extended with 0 entries. `guppi generate` wrote or changed 39 pages for 1426, 0 for 2349.
- Created: entities 1 (`entity-guppi-repository`); rules 1 (`rule-powershell-guard`); estimates 3 (`estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter`, `estimate-case-build-judges-by-the-state-at-the-moment`, `estimate-case-build-reads-the-last-output-of-a-check`); lessons 2 (`lesson-case-build-gave-a-sub-case-no-estimate`, `lesson-ask-guppi-read-a-decision-page-without-a-reason`); decisions 13 (795, 795.1, 795.2, 796, 796.1, 796.2, 797, 797.1, 797.2, 798, 798.1, 798.2, 799).
- Updated: rules 6 (`rule-github-repository`, `rule-bash-guard`, `rule-harness` by 796.1 and 796.2, `rule-hook-registry`, `rule-case-build` by 797.1, 798.1 and 798.2, `rule-lint`); estimates 7 (`estimate-prespec-hook-reports-a-create-without-a-required-field`, `estimate-bash-guard`, `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`, `estimate-case-build-judges-options-against-the-broken-rule`, `estimate-lint-checks-the-statuses`, `estimate-ask-finds`, `estimate-git-context-current`); entities 1 (`entity-guppi`, child `entity-guppi-repository`); insights 1 (`insight-case-build-recommends-without-reading-the-governing-rule`, `actioned`, `addressed_by: decision-case-798.1`).
- Cascade: `rule-ask` and `rule-git-context` `draft` → `built`; `rule-case-build` `built` → `draft`; `entity-guppi-repository` `rules: [rule-github-repository]`; `lesson-case-build-made-an-always-red-check-required` and `lesson-case-build-recommended-a-trigger-that-keeps-the-defect` archived (insight actioned). `guppi cleanup` moved those 2 pages to `vault/archive/plugin/2026-10-13/1426/lessons/`.
- `guppi render` wrote `.claude/settings.json` and `.claude/agents/case-guppi.md`. `guppi sprint`, `guppi backlog` and `guppi glossary` printed nothing on stderr. No unticked line of the spec holds `guppi sprint-close --apply`; no close ran.
- Handoff check (795.1): `entity-guppi-repository` lists `rule-github-repository` in `rules`, written by the cascade in this run; `rule-github-repository` carries `applies_to: [entity-guppi-repository]` and no `parent`; `make lint` prints no `orphan` line.
- Handoff check (796.1): `rule-bash-guard` holds `## Purpose` and `## History` only; `## How it works` was not brought back.
- Handoff check (797.1, 798.1, 798.2): the three `replace` entries of `rule-case-build` (yaml lines 12, 15, 18) each carry `applied`; one render wrote `.claude/agents/case-guppi.md`, which holds the new sentences of cases 797.1, 798.1 and 798.2.
- Handoff check (796.2): `.claude/settings.json` holds `{ "matcher": "PowerShell", "hooks": [ { "type": "command", "command": "uv run guppi powershellguard", "timeout": 30 } ] }` right after the `Bash` entry of `guppi bashguard`.
- Handoff check (798.1): `insight-case-build-recommends-without-reading-the-governing-rule` is `actioned` with `addressed_by: decision-case-798.1`; its two lessons were archived by the cascade.
- Ticked by this run: in `vault/raw/2026-10-13/1426/spec.md` every page and render box and the `read` boxes of the readings it applied; in the spec of 2349 the `read` box of `estimate-git-context-current`. 3 `read` boxes stay unticked in the spec of 1426, 3 in the spec of 2349.
- `guppi archive` moved `raw/2026-10-12/2349` to `archive/plugin/2026-10-12/2349/raw`; it kept `1426`, the session of this run.
- Index check: Grep `^(purpose|deferred_by):` over `vault/wiki/entities/`, 5 lines, compared with `entity-guppi-repository`: none the same, none near. Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, 84 lines, compared with `rule-powershell-guard`: none the same; `rule-bash-guard` near (the same refusal for a Bash heredoc). Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 38 lines, compared with the two lessons: none the same.
- Synthesis: Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 38 lines; Grep `^(pattern|deferred_by):` over `vault/wiki/insights/`, 2 lines.
  - `lesson-case-build-gave-a-sub-case-no-estimate`: none; its cause is a reading of the person's answer ("no new Estimate" as "no Estimate") with no search for an existing Estimate, while `insight-case-build-recommends-without-reading-the-governing-rule` has a recommended option not checked against the rule it changes. Stays `new`.
  - `lesson-ask-guppi-read-a-decision-page-without-a-reason`: none; no lesson or Insight has ask-guppi reading a Decision page as its cause. Stays `new`.

## Readings due

- `estimate-case-build-reads-the-last-output-of-a-check` — `failed`; target `rule-case-build` (`draft`); method: by hand at the Retro of this session, the new Render of rule-case-build in the Spec read against the Criterion. Result (ledger line 28): the new sentence of case 798.2 says only that `context` names the output, while the first Then line asks that it quotes the output with its source.
- `estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter` — `pending`; target `rule-powershell-guard` (`draft`); read box `vault/raw/2026-10-13/1426/spec.md:300`; method: `uv run pytest tests/test_powershellguard.py`; after the librarian's run of this session renders rule-hook-registry, the PowerShell entry of `.claude/settings.json` read against the Criterion. This run: `guppi render` exited 0 and wrote `.claude/settings.json`, whose `PreToolUse` list holds `{ "matcher": "PowerShell", "hooks": [ { "type": "command", "command": "uv run guppi powershellguard", "timeout": 30 } ] }` right after `{ "matcher": "Bash", ... "uv run guppi bashguard" ... }`; `make test`: 1587 passed, 6 skipped.
- `estimate-case-build-judges-by-the-state-at-the-moment` — `pending`; target `rule-case-build` (`draft`); read box `vault/raw/2026-10-13/1426/spec.md:372`; method: by hand, after case-guppi builds a Case whose form or reading depends on another Case of the same session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `pending`; target `rule-case-build` (`draft`); read box `vault/raw/2026-10-13/1426/spec.md:401`; method: by hand, after the first Case case-guppi builds that changes a reader in code and the text or the writer it reads.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); method: the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of /sprint-open.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); read box `vault/archive/plugin/2026-10-12/2349/raw/spec.md:1145`; method: by hand, after the first /merge-main whose merge of main leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); read box `vault/archive/plugin/2026-10-12/2349/raw/spec.md:910`; method: by hand, after the first pull request from an account other than the owner's is merged into main by /pr-review after the close of plugin.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin` (`draft`); read box `vault/archive/plugin/2026-10-12/2349/raw/spec.md:1353`; method: by hand, a pull request from a second account read on GitHub, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, a CI run on GitHub and the clean branch it wrote, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, an install of the clean branch into an empty project, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin` (`draft`); method: the person's answer on README.md at the /hi of the session after the one whose Work Mode writes README.md under the milestone The plugin, before the close of the sprint.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, at the end of Work Mode of the session that closes entity-sprint-plugin.

## Flags

- `near`: line 8 of the 1426 yaml, the `create` of `rule-powershell-guard` (case 796.2), carries `near: rule-bash-guard`; the page was written.
- Failed Estimate: `estimate-case-build-reads-the-last-output-of-a-check` (ledger line 28).
- No entry is marked `incomplete`, `failed` or `unparsed`.
- Stale defer: `rules/rule-morph: deferred: 4 times since case 239` (lint).
- `make lint`, 2 lines (the handoff names 3 red lines before and after the work; the `orphan` line of `rule-github-repository` and the `backlog` line are gone after this run, the `unread: failed` line comes from this run's reading):
  - `rules/rule-morph: deferred: 4 times since case 239`
  - `estimates/estimate-case-build-reads-the-last-output-of-a-check: unread: failed`
- The context of this librarian run carried the same text of Claude Code's auto mode that the handoff names under Observations (to make small file changes with sed, heredocs or short scripts through Bash); this run wrote its files under `vault/` with Write and Edit only.

## Next session

### Cases

- The `failed` reading of `estimate-case-build-reads-the-last-output-of-a-check`: change the sentence of `rule-case-build` so that `context` quotes the output with its source, or change the Criterion to "names" (handoff, For the next session).
- The milestone The clean branch (CI that writes `prod`) is still the current one; it was put off in session 1426 (handoff, For the next session).
- `rule-morph` is still a placeholder, put off 4 times; the person wanted it taken up, then left it in the backlog as it stood (handoff, For the next session).
- The cause of `lesson-case-build-gave-a-sub-case-no-estimate`, and the cause of `lesson-ask-guppi-read-a-decision-page-without-a-reason` (handoff, For the next session).

### Work

- Read `estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter` (box `vault/raw/2026-10-13/1426/spec.md:300`): this run's render wrote the PowerShell entry of `.claude/settings.json`.

### Ask the person

- none

## Readings at the close

- `make test`: 1587 passed, 6 skipped.
- `make lint`: 2 lines, listed under Flags.
- Live pages: rules 83, estimates 274, entities 5, insights 2, lessons 38, decisions 97; `vault/archive/`: 2667 `.md` files after `guppi archive`.
