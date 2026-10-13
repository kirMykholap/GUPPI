# Handoff — 2026-10-14, the clean branch: bare case numbers in the code and pointers in the shipped pages

## Notes from memory

- The person agreed with every recommendation of every round of Cases 808 and 809, and with the fix of each pre-spec finding; no option was weighed against another.
- Case 809 is wide: one `create` and 49 `update` items, the rewording of each `core: true` page whose sentences hold a pointer outside a bracket. Its `context` says the pairs come from `vault/raw/2026-10-13/2118/ship-review.txt`; the `ask-guppi` run did not read the sentence around each `new` whole but for six pages, and did not count each hit of each `old` on its own.
- Cases 808 and 809 were ratified twice, before and after `/pre-spec`; the ledger holds each line once but for `update` `entity-sprint-plugin`, which only the second ratification of 809 carries.

## Direct instructions to the librarian

- Case 809 holds many `replace` pairs over 47 rule pages and 2 entities: an `old` that misses or hits twice fails its entry. Check the yaml for `failed` and `incomplete` on the entries of 809 first.
- Case 809 `update`s `rule-page-generation` and `rule-work-mode`, which stand in `backlog.md` under `## Deferred`; the `update` rewords text and puts nothing off or takes nothing up.
- 808.1 and 809 both write to `rule-clean-branch`: 808.1 a `replace` in its `## Purpose`, 809 the new Estimate added to its `estimates`. They share no sentence.
- After the render, `make lint` runs `guppi ship --check` over `.claude/` and `CLAUDE.md` as rendered from the reworded pages; a red line there is the reading of whether 809 reworded the Renders whole.

## What actually got done

- Cases ratified: 808 (808.1, 808.2) and 809.
- Code: `guppi/ship.py` gained `bare_numbers`, the one judgment of a bare case number in a comment or a docstring of a Python file, read by `tokenize`; `leftovers` adds its lines for a `.py` file, so `guppi ship`, `--review` and `--check` exit 1 on one. The comments and docstrings of `guppi/casecheck.py`, `cleanup.py`, `gate.py`, `generate.py`, `ledger.py`, `lint.py`, `materialize.py`, `onward.py`, `prespec.py` and `ratified.py` write each case number with its word; where the longer comment pushed a code line past the formatter's width, the comment moved to its own line above it.
- Tests: `tests/test_ship.py`, three new tests.
- At the end of Work Mode: `make test` 1615 passed, 6 skipped; `make style` clean; `uv run guppi ship --check` printed no line.
- Readings: ledger lines 55–57, all `passed`. Lesson: ledger line 58.

## Debt

- None.
- 70 boxes of the Spec wait for the librarian.
- `estimate-clean-branch-pages-hold-pointers-only-in-brackets` waits for the event its `method` names: the librarian's run of this session that applies the pages of Case 809.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` waits for a session of the sprint after the librarian's run of this session: the owner pushes a tag `prod-*` on a commit of `plugin` and the CI run it starts is read.

## Observations

- The bare-number judgment takes an opening of one case number and a colon; a docstring that opened with a list, such as `387.4, 445.4, 476.3:`, was no finding of it and was reworded by hand all the same.
- `uv run guppi ship --review` still lists `(split it, case 472.3)` in `guppi/prespec.py` and `(case 320: no file route)` in `guppi/materialize.py`: the words in these brackets add to the sentence, and the clean copy drops them. The reading of session 2118 accepted the same 31 lines.
- A comment that was a case number alone, such as `# 786`, needed words of its own, since the copy would hold an empty `#` once its bracket goes.

## For the next session

- Whether the bare-number judgment also takes an opening of a list of case numbers and a colon, such as `387.4, 445.4:`.
- Whether `guppi/caseid.py` takes the session stamp from the newest `hi:` line when `--session` is not given, or `orchestration.md` names `--session <id>` in the command it gives (the lesson of this session).

## Ask the person
