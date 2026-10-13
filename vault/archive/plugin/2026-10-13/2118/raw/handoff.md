# Handoff — 2026-10-13, sprint plugin: Work Mode at a fork, and the pointer rule of the clean branch

## Notes from memory

- Case 806: the person turned down the recommendation to move a fork of Work Mode to the next session. The person wants a new Case that replaces only the sub-case the fork touches. The person chose that the replaced sub-case leaves the Spec, once told that the librarian takes the content of a page only from the Spec, "so that only what is confirmed reaches the wiki". Several times the person asked to discuss the item rather than answer a round.
- Case 807: the person did not trust a script that removes text by itself and asked who checks it; a worked example on real lines settled it. The person widened the rule: a pointer and every word that goes with it, sessions and times included, stand in one bracket, which `guppi ship` removes whole. The person first chose to reword the pages in this Case on a claim of `case-guppi` that proved false, then moved the pages to the next session.
- Case 807 keeps the exemption of `case-example.md` and of the Render of `rule-case-example` by name, though its `context` says the fence rule alone covers that example; the person may drop it later.
- At `/pre-spec` the person agreed to every recommendation. Sub-case 806.4 was born from that report. The last two fixes — the sentence of `## The acknowledging reply` of `rule-orchestration` for Work Mode, and `uv.lock` left out of the `then` of 807.1 — came after the confirmation run of `ask-guppi`, so no agent checked them a second time.

## Direct instructions to the librarian

- Cases 806 and 807 were ratified twice, once before `/pre-spec` and once after it; the ledger holds each line once, and 806.4 has lines of the second ratification only.
- `entity-sprint-plugin` takes an `update` of 807.1, a `change` alone, and the `defer` of Case 805; both name the page.
- The new step of `make lint`, `guppi ship --check`, judges `.claude/` and `CLAUDE.md` as the render writes them. The new Renders of this session write their pointers in brackets of their own; a red line of that step after the render names new text that does not, and belongs in the brief.
- `vault/raw/2026-10-13/2118/ship-review.txt` is the run of the changed `guppi ship --review` into an empty folder: the page leftovers and the brackets with words for the Case of the next session.

## What actually got done

- Cases ratified: 805 (a short defer), 806 (806.1–806.4), 807 (807.1–807.4).
- Code: `guppi/ship.py` (a bracket that holds a pointer removed whole, a link to a page left out written as its slug, fenced blocks and `schema.yaml` text masked, `--review`, `--check`, the one judgment `outside`), `guppi/prespec.py` (`check_pointers`), `Makefile` (`guppi ship --check` as the last step of `lint`), and the comments and docstrings of 21 modules of `guppi/`, each pointer moved into a bracket of its own. Tests: `tests/test_ship.py`, `tests/test_lint.py`, `tests/test_prespec.py`.
- `make test`: 1612 passed, 6 skipped. `make style`: clean. `make lint`: exit 0 at the end of Work Mode.
- Readings: ledger lines 1–2 at `/hi`; the seven readings of Retro and one lesson, `lesson-case-build-recommended-on-a-claim-about-code-it-did-not-read`, at the end of the ledger.

## Debt

- No box is debt.
- 29 boxes wait for the librarian.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: its `method` waits for the first `/work` that runs on the rendered `.claude/skills/work/SKILL.md` and in which a Case is ratified in Work Mode.
- `estimate-sprint-plugin-ci-writes-a-clean-branch`: waits for the Case of the next session that rewords the pages, and the CI run after it.

## Observations

- The expected red of `work.md` did not come: `guppi ship --check` printed no line on `.claude/` or `CLAUDE.md` at the end of Work Mode.
- A pointer written as a bare number, such as `(274.1)` or `# 786`, is no pointer by the rule and stays in the clean copy; many comments of `guppi/generate.py`, `guppi/materialize.py` and `guppi/prespec.py` use that form.
- `guppi ship` also removes a bracket inside a string literal that the program prints: the message of the `/hi` hook in `guppi/sprint.py` loses `(rule-skill-sprint-open, case 743.7)` in the copy, and a message of `guppi/generate.py` loses `(case 201.1)`. Both still read whole.
- `guppi ship` removes a bracket of code that holds a pointer, such as a call whose argument line carries a comment with a pointer; the rewording moved every such comment out of its bracket in `guppi/ledger.py`, and `--review` is the only guard.
- The sentence of case 713 that in Work Mode a Case of a later session may replace a ratified Case stands beside the new route of 806, which replaces a sub-case in the same Work Mode; the `context` of 806 says why, and a reader may still take it for a contradiction.

## For the next session

- The Case of the milestone The clean branch that rewords the pages: the leftovers and the brackets with words under `vault/wiki/` and `.claude/` in `vault/raw/2026-10-13/2118/ship-review.txt`, then a CI run by a tag `prod-*`.
- Whether a bare case number such as `(274.1)` becomes a pointer of the rule, so that `guppi ship` removes it.

## Ask the person
