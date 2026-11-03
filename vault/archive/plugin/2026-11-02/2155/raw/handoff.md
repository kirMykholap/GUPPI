# Handoff — 2026-11-02, sprint plugin: the note of names, the Frontier hook, the clean branch read

## Notes from memory

- Case 1011: the person first took a limit of 20 counted over unread files, then said that no fixed number makes sense, since any number is a guess; the hook should point to the files by their purpose, require no reading of everything, and leave a miss for `/pre-spec` to show. The person then put the purpose-first reading of Estimates into the same Case ("В одном кейсе решим сразу вопрос"), against the recommendation to split it into a Case of its own.
- Case 1013: the person softened the rule: a heading of a reply may keep a harness term in English, and the current behaviour suits the person. The person asked that an Estimate `failed` for that reason be set `passed`; none stood `failed`, so the Case replaced the Criterion of `estimate-orchestration-acknowledging-reply` instead.
- C1 of the Frontier closed as work with no Case: the person pushed `plugin` and the tag `prod-0.3.0` by hand, after asking what a tag number and a commit hash are.
- `ask-guppi` at `/pre-spec` reported more searches of code than its frame allows, as in session 2035; no finding rested on them.

## Direct instructions to the librarian

- `rule-case-build` takes three `update` items from Cases 1011.2 and 1011.3, with `replace` pairs in different passages; apply them in ledger order, each against the text the one before leaves.
- Case 1011.3 also updates `rule-case-protocol`, whose Render is `vault/wiki/case-schema.md`; render both `.claude/agents/case-guppi.md` and `case-schema.md`.
- Case 1012 creates `rule-frontier-hook` with `core: true`; its `update` of `rule-hook-registry` registers `guppi frontierguard` on `PreToolUse` of `Edit|Write|MultiEdit`, which `guppi render` writes into `.claude/settings.json`.
- Case 1013 updates `rule-orchestration` with four `replace` pairs; render `vault/wiki/orchestration.md`.
- Cases 1012 and 1013 set their Insights `actioned` with `addressed_by` — the first item of the sprint page's milestone may tick once `estimate-sprint-plugin-ci-writes-a-clean-branch` stands `passed` (L15).

## What actually got done

- Cases ratified: 1011 with 1011.1, 1011.2, 1011.3 and 1011.4; 1012; 1013. Each was built again on the findings of `/pre-spec` and ratified again.
- Code: `.guppi/guppi/casecheck.py` (`names_notes` gives one note per Case listing each unread file once, with `NAMES_ASK`, `NAMES_LINE` and `listed_files`; `BROAD_NAME` gone), `.guppi/guppi/prespec.py` (`open_box_closers`), `.guppi/guppi/ratified.py` (`text_after`, which `builder_write` calls), `.guppi/guppi/frontierguard.py` (new), `.guppi/guppi/cli.py` (`frontierguard`).
- Tests: `.guppi/tests/test_casecheck.py` (the broad-name tests replaced by the list tests), `.guppi/tests/test_frontierguard.py` (new, 13 tests).
- `uv run --project .guppi guppi test`: 1921 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L15 `estimate-sprint-plugin-ci-writes-a-clean-branch` passed (CI run on `prod-0.3.0`); L18, L19, L20, L21 passed. Lessons: L22, L23 (error).

## Debt

- No box of code, test or command is left unticked.
- Boxes that wait for the librarian: 24 of the 26 unticked (page lines, render lines and read lines); the other two are the read lines of the two Estimates below.
- `estimate-case-build-searches-the-names-of-what-it-changes`: waits for the `/pre-spec` of the first session in which the hook sends `case-guppi` the list note, on the Render of `rule-case-build` this run renders.
- `estimate-orchestration-acknowledging-reply`: waits for the librarian's render of `vault/wiki/orchestration.md` with the sentence of Case 1013, then an acknowledging reply and a reply that acknowledges Cases ratified together, read in their transcript.

## Observations

- `claude plugin validate` in the run of `prod.yml` on `prod-0.3.0` printed one note: the plugin has no icon (`ICON_MISSING`); the run passed.
- The hook `guppi frontierguard` does not fire in this session: it runs once the librarian renders `.claude/settings.json`.
- `## Expected red` of `work.md` is empty; no check went red in Work Mode.

## For the next session

- Whether the plugin gets an icon, since `claude plugin validate` notes `ICON_MISSING` on the clean version.
- Whether `ask-guppi` keeps to its one search of code at `/pre-spec`, or its frame changes: it reported more searches than allowed in two sessions running.

## Ask the person
