# Handoff — 2026-10-28, sprint plugin: the guard writes the file of case-guppi, the clean copy keeps the event logs out of git, a test of a subagent's compaction

## Notes from memory

- The person added C5 in the session: each write of `case-guppi` to its case file asked for permission. The Claude Code page on subagents says a subagent stays in plan mode in a plan-mode session whatever its `permissionMode`; the person said the main agent's write of `frontier.md`, which the allow list names, asked too. The person chose that the guard writes the file itself and stops the call, "let us try it this way", knowing that the documentation does not say whether Claude Code checks an `Edit` (read first, unchanged since) before the `PreToolUse` hooks run. Case 894.3 has `case-guppi` read its file before its next `Edit` for that reason; whether that is enough is seen only in a later Plan Mode.
- C2 (the growing context of `case-guppi`) went through nine rounds. The person rejected a fresh helper per change and asked for a procedure where the same helper writes an interim Case when a hook says its context is large, then compacts and goes on. The person chose to test that first; Case 895 holds only the test. The size the person chose for "too large" is 400 000 tokens (as in the main session).
- At `/pre-spec` the person agreed that the reading of `estimate-clean-branch-ships-neutral-texts` waits for this run, so the copy holds the new texts of Case 894.
- C1 (the CI run on a tag `prod-x.y.z`) was put off again with no Case: a push to the remote is the owner's step.

## Direct instructions to the librarian

- Case 893.1 carries `{supersedes:case 882.3}` and puts `rule-clean-branch` off again with the rest of the list of 882.3; 893.2 carries `{supersedes:case 891}`, which also names `estimate-spec-write-writes-a-defer` — the Case context says by `clear_deferred_by` that page keeps `decision-case-891` in its `deferred_by` and stays in `backlog.md`; check what `guppi backlog` lists for it.
- Cases 892, 893 and 894 were built again on the findings of `/pre-spec` and ratified again with the same decision lines; take the `then` blocks from the Spec.
- Case 894.1 changes `rule-spec-reconcile` and 894.3 `rule-case-build`; `guppi render` writes `.claude/agents/case-guppi.md` from the second. The Render of `rule-permissions` does not change, so `.claude/settings.json` stays as it is.
- The root `.gitignore` lost its event-log lines and `vault/.gitignore` holds them; `git check-ignore` showed `vault/.gitignore:2` ignoring the day's log.

## What actually got done

- Cases ratified: 892, 893 (893.1, 893.2), 894 (894.1, 894.2, 894.3), 895.
- Code: `.guppi/guppi/ratified.py` (`guard` writes a call of `case-guppi` on its case file itself by `builder_write` and `builder_file`, logs `ratified wrote`, exits 2; `held_number` returns its refusal with whether it judged, so its own error lets the call run; `event`; docstrings), `.guppi/guppi/ship.py` (`VAULT_IGNORE`, taken into the copy; docstring), `vault/.gitignore` (new), `.gitignore` (the event-log lines removed).
- Tests: `test_ratified.py` (the guard tests and the `number_held` tests expect the hook's write; 9 new tests of the write), `test_ship.py` (`tree` writes `vault/.gitignore`, the set test holds it, one new test), `test_casecheck.py` (a docstring and a comment name the sibling Case with no number), `test_caseid.py` (`held_number` read as a pair).
- `uv run --project .guppi guppi test`: 1790 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- The test of Case 895 ran in `scratchpad/compact-test` of the session's temporary area by `claude -p` 2.1.301, three runs, about 2.4 USD.
- Readings L13–L19: six `passed` (the two Work readings of the joint send included), `estimate-case-build-goes-on-after-a-compaction` `failed`. Lessons L20–L22: one `knowledge`, two `error`.

## Debt

- No box of the Spec is debt; no patch.
- 19 boxes wait for the librarian (page, render and `read` lines).
- `estimate-clean-branch-ships-neutral-texts` — waits for the librarian's run of this session, with a tag `prod-x.y.z`: `guppi ship --allow-draft` into an empty folder, each sentence read whole.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — waits for the owner's push of `plugin` and a tag `prod-x.y.z`, before the close of `plugin`.
- `estimate-clean-branch-writes-the-session-files`, `estimate-git-context-offers-git-init`, `estimate-plugin-install-offers-to-install-uv`, `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` — wait for an install from a tag `prod-x.y.z`, as before.

## Observations

- Red before the work: `guppi check` exit 1 with the 15 lines of `## Baseline` of `work.md`; the two `ship` lines on `test_casecheck.py` are gone after Case 892 (`guppi ship --check` prints nothing).
- The guard runs from the working tree: while `held_number` was changed before its caller, the live hook refused every Edit and Write; `git checkout` of `ratified.py` and the edits again, caller first, fixed it (lesson L21).
- The compaction test: the helper compacted three times at preTokens 72126, 74307 and 75012 with `autoCompactWindow: 100000`; the earlier transcript lines stayed; `SubagentStop` fired for it after; Claude Code itself put the interim file back after the second and third compactions; `PreCompact`/`PostCompact` fired with no `agent_type` or `agent_id` and the main transcript path, and each compaction ran a summarizer that fired `SubagentStop` with an empty `agent_type` (lesson L20).
- The new guard works in this repository from this session on: a `case-guppi` of the next Plan Mode has its file written by the hook before the librarian's render tells it to take the "written" line as done; the guard's own line tells it not to call again.

## For the next session

- The procedure for a full `case-guppi`, put off on `rule-orchestration` by Case 884, can be built from lesson L20: the compaction comes near three quarters of `autoCompactWindow`, and a hook on `PostCompact` cannot tell which subagent compacted, so the procedure's trigger has to come from `SubagentStop` of `case-guppi` or from its own size; `estimate-case-build-goes-on-after-a-compaction` stands `failed` on its first line until a Case replaces that line with what the test showed.
- Whether a `Read` before the next `Edit` is enough after the guard wrote a case file is seen at the first build of a Case in Plan Mode; a refusal of Claude Code ("modified since read") there would need a Case on `rule-case-build`.

## Ask the person

- `estimate-permissions` — needs the person — In the next Plan Mode, after the librarian's render, does Claude Code ask you anything when `case-guppi` writes or edits its Case file, and does it ask at a Grep of a subagent on the folder of the saved transcripts and on a file under it?
- `estimate-guppi-package-is-ready-after-the-install` — needs the person — In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?
