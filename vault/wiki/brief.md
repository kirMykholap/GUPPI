# Brief — 2026-10-14, after the librarian run of session 0232

## Where things stand

- Session 0232 (dated 2026-10-14) of the sprint `plugin` ratified Case 811 and Case 812 with its sub-cases 812.1 and 812.2. Case 810, ratified first, is superseded whole by 812.1 in its own session and is not counted (handoff, What actually got done; Notes from memory).
- Code: `guppi/ship.py` has one pattern `NUMBERS`, a list of case numbers joined by a comma, a semicolon, `and` or a dash, that serves `BARE_BRACKET`, `BARE_OPENING` and `BARE_ALONE`. `guppi/caseid.py` requires `--session` (exit 2 without it), and with no plan file of the session prints one stderr line, no id, holds nothing and exits 1. Tests: one new test in `tests/test_ship.py`, two in `tests/test_caseid.py`. At the end of Work Mode: `make test` 1619 passed, 6 skipped; `make style` clean; `uv run guppi ship --check` printed no line; `make lint` exit 0 with no line (handoff).
- Pushed on the person's word: the branch `plugin` and the tag `prod-1`. The workflow `prod` ran on `prod-1` (run 38489789184) and failed at `actions/checkout` with "Permission denied (publickey)"; no branch `prod` was written (handoff, What actually got done; Observations).
- Readings of the session: ledger lines 1 and 11–13, all four `passed`; lessons on ledger lines 14–16 (handoff; yaml).
- The yaml `vault/raw/2026-10-14/0232/materialize.yaml`: 16 entries from a 16-line ledger, one entry per line, so every ledger line is accounted for; 5 decisions (810, 811, 812, 812.1, 812.2). Entries of lines 2–4 (Case 810) carry `superseded_by: 812.1` and were not applied; the other 13 entries, the 4 entries of the synthesis and the 5 decisions carry `applied`. No entry carries `failed`, `incomplete`, `exists` or `merged`; one carries `near`. The yaml of 0101 was extended with 0 entries. `guppi generate` wrote or changed 0 pages for 0101 and 17 for 0232, and printed nothing on stderr.
- Created: decisions 5 (`decision-case-810`, `decision-case-811`, `decision-case-812`, `decision-case-812.1`, `decision-case-812.2`); lessons 3 (`lesson-ci-prod-deploy-key-refused-at-checkout`, `lesson-caseid-run-before-the-plan-file-held-no-id`, `lesson-caseid-run-to-check-an-id-held-a-new-one`); insights 1 (`insight-caseid-printed-an-id-it-did-not-hold`, born `actioned`).
- Updated: rules 3 (`rule-clean-branch` by 811; `rule-orchestration` and `rule-ratification` by 812.1); estimates 4 (`estimate-clean-branch-writes-a-clean-copy` by 811 and its reading, `estimate-ratification-case-id-carries-the-sprint` by 812.1 and its reading, `estimate-orchestration-shows-the-built-case` by 812.2 and its reading, `estimate-clean-branch-pages-hold-pointers-only-in-brackets` by its reading); lessons 1 (`lesson-caseid-held-no-id-without-the-session-option`, `clustered`).
- Cascade: `rule-clean-branch` `draft` → `built`. `guppi cleanup` moved 3 pages to `vault/archive/plugin/2026-10-14/0232/`: `decision-case-810` (superseded), `lesson-caseid-held-no-id-without-the-session-option` and `lesson-caseid-run-before-the-plan-file-held-no-id` (insight actioned).
- `guppi render` wrote `vault/wiki/orchestration.md` and `vault/wiki/ratification.md`, and printed nothing on stderr. `guppi sprint`, `guppi backlog` and `guppi glossary` printed nothing on stderr; `vault/wiki/sprint.md` changed in the line of the milestone The clean branch; `backlog.md` and `glossary.md` did not change. No unticked line of the Specs holds `guppi sprint-close --apply`; no close ran.
- `guppi archive` printed nothing on stdout or stderr and moved no unit: the units left in `vault/raw/` are `2026-10-14/0101` and `2026-10-14/0232`, both dated the day of the run, and 0232 is the session of the run; the folders of 2026-10-09 to 2026-10-13 hold only `event_log.md`. No `pending` Estimate's `method` names the archive step.
- Handoff check (Case 810): its three `update` entries carry `superseded_by` and `guppi generate` did not apply them; `decision-case-810` is marked superseded by `decision-case-812.1` and archived.
- Handoff check (`replace` pairs of 812.1 on `rule-orchestration`): before `generate`, each of the three `old` texts, the sentence ending "before the first dispatch of the session." included, was found once in `vault/wiki/rules/rule-orchestration.md`; the `old` of 812.1 on `rule-ratification` and of 811 on `rule-clean-branch` were found once each; `generate` failed none.
- Handoff check (render): after the render, `vault/wiki/orchestration.md` names `caseid --next --session <stamp>` twice and `vault/wiki/ratification.md` once.
- Ticked by this run: in `vault/raw/2026-10-14/0232/spec.md` 11 boxes (9 by `generate`, the two render lines by `render`); in `vault/raw/2026-10-14/0101/spec.md` 1 box (`read estimate-clean-branch-pages-hold-pointers-only-in-brackets`). Unticked after the run: none in either Spec.
- Index check: the yaml holds no `create` entry; the three `lesson` entries were compared with the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 41 lines. None is the same page as an existing lesson; `lesson-caseid-run-before-the-plan-file-held-no-id` is marked `near: lesson-caseid-held-no-id-without-the-session-option`.
- Synthesis: Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 41 lines; Grep `^(pattern|deferred_by):` over `vault/wiki/insights/`, 3 lines.
  - `lesson-ci-prod-deploy-key-refused-at-checkout`: none — no index line names a key pair, a secret or a deploy key; it stays `new`.
  - `lesson-caseid-run-before-the-plan-file-held-no-id`: joined `lesson-caseid-held-no-id-without-the-session-option` in the new `insight-caseid-printed-an-id-it-did-not-hold` — both runs printed an id and exited 0 with no plan file of the session found. The lesson carries `addressed_by: decision-case-812.1`, so the Insight was born `actioned` with `addressed_by: decision-case-812.1`, and both lessons went to the archive by the cascade.
  - `lesson-caseid-run-to-check-an-id-held-a-new-one`: none — the index lines on `guppi caseid` speak of an id the command did not hold; this one of a run taken for a read of the store, which held a new id; it stays `new`.

## Readings due

- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `pending`; target `rule-work-mode` (`draft`); method: by hand, at Retro, the new Render of rule-work-mode in the Spec; `uv run guppi render --check`; by hand, after the first /work that runs on the rendered `.claude/skills/work/SKILL.md` and in which a Case is ratified in Work Mode.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `pending`; target `rule-morph` (`draft`); method: by hand, after the session whose Work Mode builds the install skill of rule-morph.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); method: by hand, after the first /merge-main whose merge of main leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); method: by hand, after the first pull request from an account other than the owner's is merged into main by /pr-review after the close of plugin.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); method: the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of /sprint-open.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, in a session of the sprint plugin before its close, the CI run that a tag `prod-*` on a commit of `plugin` starts, its push with the deploy key of `PROD_DEPLOY_KEY`, the branch `prod` it wrote and the `on:` block of `.github/workflows/prod.yml`.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, an install of the clean branch into an empty project, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, a pull request from a second account read on GitHub, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin` (`draft`); method: the person's answer on README.md at the /hi of the session after the one whose Work Mode writes README.md under the milestone The plugin, before the close of the sprint.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, at the end of Work Mode of the session that closes entity-sprint-plugin.

## Flags

- `near`: `lesson-caseid-run-before-the-plan-file-held-no-id` is near `lesson-caseid-held-no-id-without-the-session-option` (index check); both now stand in the archive under `insight-caseid-printed-an-id-it-did-not-hold`.
- No entry is marked `incomplete`, `failed` or `unparsed`. No Estimate is `failed`.
- `make lint`: 0 lines, exit 0.
- Handoff note: the reading of `estimate-clean-branch-pages-hold-pointers-only-in-brackets` judged the brackets such as `(one written before case 513, case 513)` beside the words "older page" as history of the repository, which its second Then line allows; the person was told that a stricter reading makes it `failed`, and did not object.
- Handoff note: the id 813 is held in the store of the plan file of session 0232 and names no Case.
- Handoff observation: with the new list pattern, a dash-joined opening such as a year and a month before a colon (`2026-10:`) in a comment or a docstring would be a finding, since `NUMBER` excludes only a full date; no such text stands in `guppi/` today.
- Handoff observation: the deploy key `prod_deploy_pub` stands with write access, `verified: true`, `last_used: null`; the secret `PROD_DEPLOY_KEY` was set on 2026-10-13; the private half in the secret does not open that deploy key, and no local copy of the key pair was found.

## Next session

### Cases

- The deploy key of `prod`: the owner makes a new key pair, sets its public half as the deploy key with write access and its private half as `PROD_DEPLOY_KEY`, then runs `gh run rerun 38489789184` or pushes a new tag `prod-*`; whether this needs a Case or is work of the owner alone is for the next Plan Mode (handoff, For the next session; `lesson-ci-prod-deploy-key-refused-at-checkout`).
- Whether `guppi caseid` gets a mode that reads the store without holding an id, or `orchestration.md` says that the main agent never runs the command to check an id (handoff, For the next session; `lesson-caseid-run-to-check-an-id-held-a-new-one`).

### Work

- Ledger of session 0232: 16 lines, 16 yaml entries; lines 2–4 (Case 810) were not applied, superseded by Case 812.1 in its session, which applied the texts that stand.

### Ask the person

- none

## Readings at the close

- `make test`: 1619 passed, 6 skipped.
- `make lint`: 0 lines, exit 0.
- Live pages: rules 84, estimates 281, entities 5, insights 4, lessons 42, decisions 126; `vault/archive/`: 2701 `.md` files after `guppi archive`.
