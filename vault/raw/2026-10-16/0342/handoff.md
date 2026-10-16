# Handoff — 2026-10-16, sprint plugin: /hi outside a git repository and the install of GUPPI

## Notes from memory

- The person asked whether the main branch should be a setting of GUPPI instead of `main` everywhere. The person agreed to leave it to the setup Case of `rule-morph`. Until that Case is built, a project whose main branch has another name still meets `main` in the code and the skills.
- Case 851 changed twice after its first ratification. At /pre-spec, the person chose that after the yes `/hi` runs `git init -b main` and ends, with no going on in the same turn. The person also chose that `git init` stays out of `allowed-tools` and that `rule-default-mode` gets the one exception. One thing rests on no checked source: that Claude Code asks the person before a Bash call that `allowed-tools` does not name. The hand reading of `estimate-git-context-offers-git-init` checks it.
- The case-guppi of Case 851 first rebuilt it as Case 856 with supersedes marks. The main agent sent it back to rebuild under 851, and `cases/case-856.md` is empty. The id 856 was never printed by `guppi caseid`, and 854 was printed for C6 and not used, since C6 closed by a reading.
- Case 853 deletes what the install copied when `uv sync` fails. The person agreed to the deletion, which is limited to files the install wrote into a project that held none of them.
- The person kept the tag `prod-0.2.0` on GitHub as history. The next version takes a new number.
- The context of Case 855 still says that Case 851 makes `/hi` "go on to `/sprint-open`". After the /pre-spec change, the `/hi` that runs `git init` ends, and the next `/hi` starts `/sprint-open`. The defer itself stands.

## Direct instructions to the librarian

- Cases 852.1 and 853 both update `rule-plugin-install`. Case 852.1 changes the description, the Purpose sentence on a missing `uv`, step 1 and step 7. Case 853 changes step 6 and adds one Purpose sentence after the sentence on `uv sync`. Apply 852.1 first, then 853; their `old` texts do not overlap.
- Cases 851.1 and 851.2 both touch `/hi`. Case 851.1 updates `rule-git-context`, `rule-skill-hi` and `rule-default-mode`. Case 851.2 replaces the Criterion of `estimate-hi-no-read-calls`. After the render, check that `.claude/skills/hi/SKILL.md` runs `uv run --project .guppi guppi gitstate` on its `Branch:` line and that `allowed-tools` names it and no `git init`.
- `case-856.md` under `cases/` is empty; no ledger line names case 856.
- Case 852.2 replaces the Criterion of `estimate-guppi-package-is-ready-after-the-install`. This session's ledger also holds a `failed` reading of that Estimate on its old Criterion, taken at /hi, so the reading predates the update.

## What actually got done

- Cases ratified: 851 (851.1, 851.2, 851.3), 852 (852.1, 852.2), 853, and the short defer 855.
- Code: `.guppi/guppi/gitstate.py` (new: `guppi gitstate`) and `.guppi/guppi/cli.py` (the command in `COMMANDS`). Test: `.guppi/tests/test_gitstate.py` (new, 4 tests).
- The `stop:` box of the tag `prod-0.2.0` in `vault/archive/plugin/2026-10-15/0553/raw/spec.md` is ticked.
- The commands of the standalone installer of `uv` in the new step 1 of `rule-plugin-install` were read against `https://docs.astral.sh/uv/getting-started/installation/`. Both match.
- `uv run --project .guppi guppi test`: 1719 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: at /hi L1, L2, L3, L4, L14, L16; at Retro L19. Lessons: L20, L21.

## Debt

None.

Boxes that wait for the librarian or a later reading: 20 (page lines, render lines and read lines).

- `estimate-git-context-offers-git-init` — after the librarian's run: an install by hand into an empty folder with no git, `/hi` answered no, then yes, then `/hi` again.
- `estimate-hi-no-read-calls` — after the librarian's run of this session: the first `/hi` after it, read in its transcript.
- `estimate-plugin-install-offers-to-install-uv` — after the librarian's run, with a tag `prod-x.y.z` in the history of HEAD: an install by hand from a terminal whose PATH holds no `uv`, answered no, then yes.
- `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` — after the librarian's run, with a tag `prod-x.y.z` in the history of HEAD: an install by hand offline with an empty cache of `uv`.
- `estimate-clean-branch-writes-the-session-files` — deferred by case 855; after the render of Case 851, beside the hand installs above.

## Observations

- The red of `uv run --project .guppi guppi check` in Work Mode is the 13 lines of `## Baseline` of `work.md`, red before the work: seven draft pages with `core: true`, three `unread: failed` and three `method` lines. Three readings of this session change that: `estimate-clean-branch-ships-the-tests` and `estimate-harness-pipeline` now read `passed`, and `estimate-clean-branch-writes-the-session-files` stays `failed` until its reading after the render.
- The reading L2 of `estimate-clean-branch-ships-neutral-texts` failed. Three sentences of the clean version hold only in the repository of GUPPI: the `core` field in the Render of `rule-rules-schema` and of `rule-entities-schema` ("a page without it stays in this repository only"), and `rule-ratification` ("the sprints `migration` and `plugin` keep that form to their close"). The reading was a keyword grep, not a read of every sentence.
- `guppi caseid --session` takes the session id of the `hi:` line, not its HHMM. A first call with `0342` printed no id.

## For the next session

- Failed `estimate-clean-branch-ships-neutral-texts`: rewrite the three sentences named in Observations, and the Estimates listed in its reading, so that the clean version holds no sentence true only in the repository of GUPPI.
- The milestone item `rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch` was left for later: the seven draft pages with `core: true` stop every build of `prod`, and the next tag after `prod-0.2.0` is open.
- The four hand readings under `## Debt` wait for one install session: an empty folder with no git, a terminal with no `uv`, and an offline install, all from a copy built after the librarian's render.

## Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — this reading follows the new Criterion of Case 852.2. In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?
