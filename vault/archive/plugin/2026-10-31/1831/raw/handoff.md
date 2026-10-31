# Handoff — 2026-10-31, the graph of links, a create value by its schema, one-time Estimates

## Notes from memory

- The person asked twice how to find every link of a change (C2), and added the graph as a new Frontier item (C10) instead of folding it into Case 966. They asked for a plain explanation of how the graph is built before answering its round.
- Case 967, Q10 (how `case-guppi` gets the output of the command): the person first took (a), Bash with a hook in the agent's header. `case-guppi` then read the Claude Code permission pages, found that in plan mode a `PreToolUse` hook's `allow` has no effect on a call that is not read-only, and asked again with (b) recommended. The person took (b), asked why the graph covers all pages, and kept (b) after the answer that the builder reads only the blocks of what its Case changes.
- Case 969: the person chose (c) on Q1 against the recommended (a): a one-time Estimate both targets the live sprint page and carries `once: true`, with a lint finding when the two disagree.
- The person put off C1 (the clean branch) and C4–C7 at the close of Plan Mode with one word, "let's put off the rest".
- Case 967.3 keeps `rule-link-graph-at-session-start` a Rule although its hook refuses nothing; its `context` leaves the gap between the Enforcement sentence of the rules schema and the hook Rules that write a file to a later Case.

## Direct instructions to the librarian

- Check first that `entity-link-graph` and `rule-link-graph-at-session-start` come out with `core: true` as a boolean: their `create` items write `core` as the text `'true'`, and the lift of this session's code (Case 968) loads it by the schema. If either page holds the string, flag it.
- `rule-case-build` takes three `replace` pairs from Cases 966, 967.2 and 970.1 in three different paragraphs; `rule-case-protocol` takes two, from Cases 968 and 969.1, in different sections. Check that each `old` matched once.
- Case 969.3 deletes `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`, which the ledger of this session also reads `passed` at /hi; the reading comes before the delete.
- Case 969.1 supersedes the defer of Case 963 on `rule-estimates-schema`, so `rule-estimates-schema` leaves `backlog.md`; Case 971 defers four Estimates, which enter it.
- The render after this run writes `.claude/settings.json` with the `SessionStart` hook `guppi links --write`, `.claude/agents/case-guppi.md`, `.claude/agents/ask-guppi.md`, `vault/wiki/case-schema.md` and `vault/wiki/estimates/schema.yaml` with the field `once`.

## What actually got done

- Cases ratified: 966, 967 (967.1, 967.2, 967.3), 968, 969 (969.1, 969.2, 969.3), 970 (970.1, 970.2, 970.3), and the short-form defer 971. Cases 967, 968 and 969 were built again on the findings of `/pre-spec` and ratified again.
- Code: `.guppi/guppi/links.py` (new: `guppi links <slug or path>` and `guppi links --write`), `.guppi/guppi/cli.py` (`links` in `COMMANDS`, its docstring), `.guppi/guppi/pages.py` (docstring), `.guppi/.gitignore` (`links.md`), `.guppi/guppi/materialize.py` (`schema_values`, `is_allowed`, `typed_value`; the lift reads a create value through them), `.guppi/guppi/ratified.py` (`put` and `read_tasks` through `typed_value`, `key_judge` carries `values_for`), `.guppi/guppi/prespec.py` (`core_as_left`), `.guppi/guppi/lint.py` (`check_schema` imports `is_allowed`; `check_status` reports a one-time Estimate off a sprint page), `.guppi/guppi/ship.py` (`.guppi/links.md` in `LEFT_OUT`).
- Tests: `.guppi/tests/test_links.py` (new, 13 tests), `.guppi/tests/test_materialize.py` (6 new), `.guppi/tests/test_lint.py` (2 new), `.guppi/tests/test_schemas.py` (2 new, skipped until the live schema lists `once`).
- `guppi test`: 1830 passed, 6 skipped, 1 deselected at the baseline; 1851 passed, 8 skipped, 1 deselected at Retro. `guppi style` clean.
- By hand in Work Mode: the unticked box of Case 956.3 in `vault/raw/2026-10-31/0431/spec.md`, ticked. In the transcript of session 0431 (`8727d5ce`), the reply after the librarian's report shows the 79 lines of `vault/raw/2026-10-31/0431/report.md` unchanged before its own text, and `report.md` was committed alone after the librarian's commit, with no `--amend`.
- Readings: L1 passed (at /hi), L30 and L31 passed (at Retro). Lesson: L32 (error).

## Debt

- No box of code, a test or a command is unticked.
- 42 boxes wait for the librarian: the page, render and `read` lines of the Spec.
- `estimate-case-build-reads-the-readers-of-a-changed-step` — the `/pre-spec` of the first session whose `case-guppi` runs on the new Render of `rule-case-build`.
- `estimate-case-build-reads-the-link-graph-of-what-it-changes` — the `/pre-spec` of the first session on that Render whose start wrote `.guppi/links.md`.
- `estimate-link-graph-at-session-start-writes-the-file` — the first session start whose `.claude/settings.json` holds the hook; its test part passes.
- `estimate-materialize-lifts-a-create-value-by-the-schema` — this session's librarian run, which creates the two pages with `core` written as `true`; its test part passes.
- `estimate-estimates-schema-checked` — the librarian's render of `vault/wiki/estimates/schema.yaml` with `once`.
- `estimate-case-build-runs-the-vault-query-first` and `estimate-ask-query-before-a-create` — the first build of `case-guppi` on the new Renders whose Case proposes a create without a ref.
- `estimate-ask-searches-at-prespec` — the first `/pre-spec` whose `ask-guppi` runs on the new Render of `rule-ask`.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` and the other Estimates of `entity-sprint-plugin` — the Retro of the session that finishes their work, or the close of `plugin`.

## Observations

- `guppi check` printed 16 lines before the work and the same 16 at the end: 11 pages with `core: true` that stand `draft` and 5 `unread: failed`. All were red before the work.
- The `.guppi/links.md` that `guppi links --write` wrote broke `test_the_live_code_holds_no_pointer_outside_a_bracket` of `test_ship.py`, since the tree walk of `guppi ship` takes every file under `.guppi/`; Work Mode added the file to `LEFT_OUT` of `ship.py`, which Case 967 did not name (L32).
- This session's `/pre-spec` read the `create` items of `entity-link-graph` and `rule-link-graph-at-session-start` as not core, since it ran on the code before Case 968, so their new texts and their Estimates were not judged for a pointer outside a bracket.
- `ask-guppi` at `/pre-spec` reported 7 findings, all closed at its confirmation; it did not read most Estimates of the changed pages, nor the code that several `context` texts cite.
- The harness marked two subagent answers as matching an instruction pattern (`settings-json`); both were a round and a report that named `.claude/settings.json`, with no instruction in them.
- Case 967 builds no check of a link named only in prose; the reading of names in the rendered files takes its place, as the person chose. A text that sets a general form and names nothing is still found only by meaning.
- `estimate-handoff-dispatches` can now be read: its `method` reads the transcript of session 0431, whose evidence is above.

## For the next session

- C1, the clean branch: push `plugin` and a tag `prod-x.y.z` on its last commit, and read the CI run by its Estimate.
- Whether the Enforcement sentence of the rules schema should name a hook that writes a file, such as `rule-librarian-report-copy` and `rule-link-graph-at-session-start`, which refuse nothing (Case 967.3).
- Whether `case-guppi` reads, for a new generated file, the readers of its folder, such as the tree walk of `guppi ship` (L32).
- `estimate-handoff-dispatches`, read against its Criterion from the transcript of session 0431.

## Ask the person

