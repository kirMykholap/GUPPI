# Handoff — 2026-09-28, Slice 3g and the librarian's commit

## Notes from memory

- On Case 485 the person asked what to do with Estimates that promise a one-time act, and whether they need a status of their own. The answer they accepted: a one-time act is a `tasks` line, never an Estimate; the fate of a sprint's done-conditions after the close stays with the open item of Slice 5 (478.2). The person still sees nuance here; it may come back at Slice 5.
- On round 2 of Case 485 the person picked (b) against the recommendation: a line of an old Criterion that the code no longer honours is dropped and named in `context`, not kept to fail. None such was found in the group of 485.
- Cases 482, 484 and 485 were ratified a second time after pre-spec: `purpose` added and a path fact fixed in 482, the Render claim in the `context` of 484 fixed, the exit-2 line dropped from 485.1 and `partial` restored in 485.5. The ledger holds each decision line once (the hook does not append a line it already holds).
- Slice 3g stays open: 37 `Given:` pages in about 24 groups and 12 old-layout pages in three groups (render and settings; end of session and the librarian; `estimate-ask-finds` with `estimate-tests-clock-pinned`). The sprint note stands until the last group; that Case ticks it and adds a note to remove the old-layout code once lint shows zero.

## Direct instructions to the librarian

- Case 483 replaces an `old` in `rule-retro` with a `new` that holds a fenced block; its `then` block is fenced with four backticks. Check the page renders the skeleton inside the Render markers.
- 484.7 and 485.6 both carry an `update` of `entity-sprint-migration` with only `change`: two History lines, the note on Slice 3g unticked.
- The 13 Estimates this session updates go `pending`; their `read` lines wait for a later session, not for this run.
- After this run's render, `git status` must show `guppi.toml` tracked and no rendered file untracked — the first sight of Case 482 (its reading is the next run).

## What actually got done

Ratified: 482, 483, 484.1–484.7, 485.1–485.6.

What got done: commit cb12283 took `guppi.toml`; commit 9ed5a9f is the Retro commit of the session folder. No code file or test changed. `make test` 876 passed, 2 skipped; `make style` clean; `make lint` at the baseline exit 2, 104 findings, nothing added under Expected red. Readings L18–L24 passed, L25–L26 failed.

What is not done:
- the `/wait-what` re-pitch that used a made-up example — lesson L27, `lesson-wait-what-invents-an-example`.
- rounds of `case-guppi` whose options give no before and after — note: the failed `estimate-case-build-writes-a-plain-round` goes to the next Frontier.
- 23 of the 32 pending readings of the last brief not taken — note: their events have not come (a typed `/work`, a `create` without a `ref` and a Case on a hook for `estimate-case-build-writes-the-case`, a Write of `work.md` for `estimate-permissions`, a `/hi` outside plan mode, a hook refusal, the librarian's run, `/handoff`, `/carry`, the close of the sprint, a prompt past 400 000 tokens); `estimate-agent-writing-followed` is read in the next session by its method.
- two stale `.pyc` files under `guppi/__pycache__/` (`materialize.cpython-314.pyc`, `pretask.cpython-312.pyc`) that hold the file-route strings — note: untracked, `rg` skips them; delete them when convenient.

19 boxes wait for the librarian.
Read in a later session: `estimate-close-commits`, `estimate-retro-report-holds-each-fact-once`, `estimate-prespec-catches-a-command-line-off-form`, `estimate-prespec-catches-a-superseded-case`, `estimate-prespec-catches-a-method-without-a-form`, `estimate-prespec-catches-an-unwrapped-render`, `estimate-prespec-catches-bare-wikilinks`, `estimate-prespec-simulates-the-pairs`, `estimate-session-start-context`, `estimate-hi-no-read-calls`, `estimate-git-context-current`, `estimate-github-issues-listed`, `estimate-ledger-tail`.
