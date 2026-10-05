# Handoff — 2026-10-05, one reading of supersedes, the summary names its Case, a hook for Decision pages

## Notes from memory

- The person agreed with every recommendation of the rounds but one: at `/pre-spec` they chose to keep a Grep inside `vault/wiki/decisions/` allowed for the two reasons of the frame, against the recommendation to allow only a Read (Case 664).
- The person's "Идём работать" was taken as the close of Plan Mode: C1 and C2 of the sprint left, and C5, C6 and C9 put off by the short defers 665, 666 and 667. The person did not see those three defers before they were written.
- The person answered A1 "no prompt", but no `case-guppi` of this session made a Read, Grep or Glob under `~/.claude/projects/c--PROJECTS-GUPPI/` (checked in all five transcripts), so no reading was written.
- Case 663 was renamed at `/pre-spec` (its new Estimate's slug) and had to be rebuilt as Case 668 with `{supersedes:case 663}`, since the line of its first ratification stays in the ledger.

## Direct instructions to the librarian

- Check first that the entries of Case 663 (L25–L27 and L36) carry `superseded_by: '668'` and are not applied, and that `estimate-synthesis-reads-the-status-the-run-sets` is not created.
- Cases 660, 661, 662 and 664 were ratified again after `/pre-spec`; the ledger holds their lines once, and the Spec holds the rebuilt text.
- `entity-glossary` takes three updates (660.2, 660.3, 668): check that their pairs do not touch the same words.
- After the render: `.claude/settings.json` registers `uv run guppi grepguard` on `PreToolUse` of `Grep` (664.1, `rule-hook-registry`); `.claude/agents/case-guppi.md` asks for the `**Case:**` line (662.1); `uv run pytest tests/test_orchestration.py` passes with 6 tests and none skipped after the render of `rule-orchestration` (662.2).

## What actually got done

- Cases ratified: 660 (660.1–660.4), 661 (661.1, 661.2), 662 (662.1–662.3), 664 (664.1–664.3), 668; the defers 665, 666, 667.
- Code: `guppi/materialize.py` (`in_family`, the marks of `mark_superseded`, `refold` and the records over the family of a Case), `guppi/prespec.py` (`retired_by`), `guppi/ratified.py` and `guppi/casecheck.py` import `in_family`; `guppi/generate.py` (`supersede_children`); `guppi/casecheck.py` (`summary_findings`, `top_heading`, `summary_names`, `summary_sent` kept by a later store); `guppi/grepguard.py` new, `guppi/cli.py`.
- Tests: `tests/test_prespec.py`, `tests/test_materialize.py`, `tests/test_generate.py`, `tests/test_orchestration.py` (fails in place of skipping, one new test), `tests/test_casecheck.py` (`-k summary_names_the_case`, 10), `tests/test_grepguard.py` new (15).
- `make test`: 1244 passed, 6 skipped (baseline 1207 passed, 6 skipped). `make style` clean.
- Readings: L1–L6 at `/hi`; the Work reading L40. Lessons: L41–L43.

## Debt

No box of code, test or command is unticked.
50 boxes wait: the page, render and glossary lines for the librarian, and the `read` lines of the Estimates below.
- `estimate-prespec-catches-a-superseded-case`, `estimate-materialize-marks-superseded`, `estimate-generate-writes-the-decision-page` — updated by 660.1–660.3; their pytest at the `/hi` of a later session.
- `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case` — created by 660.4; a later Retro whose session retired a parent by one tag.
- `estimate-orchestration-showing-example-passes-the-check`, `estimate-orchestration-defer-example-passes-the-hook` — updated by 661; the `/hi` of a later session.
- `estimate-case-build-writes-the-case` — updated by 662.1; live dispatches after the render.
- `estimate-orchestration-shows-the-built-case` — updated by 662.2; the close of a later session after the render.
- `estimate-case-check-sends-back-a-summary-without-the-case-name` — created by 662.3; the `/hi` of a later session.
- `estimate-search-leaves-out-decisions-by-the-grep-hook` — created by 664.1; its test and one live search in the main agent and one in a subagent after the render of `.claude/settings.json`.
- `estimate-search-leaves-out-decisions-in-every-agent`, `estimate-ask-searches-at-prespec` — updated by 664.2, 664.3; a later session.
- `estimate-synthesis-reads-the-status-its-yaml-sets` — created by 668; a librarian run in which a lesson joins an Insight a decision of its own yaml sets `actioned`.
- `estimate-case-protocol-case-form`, `estimate-prespec-confirms-the-findings-once`, `estimate-case-build-checks-the-finished-case` — failed and put off by 665, 666, 667.
- `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds` — its pytest passes (11), but the entry the guard writes at the first Write of a live `case-guppi` was replaced by the check's store before it could be seen; it waits for a look at the store between that Write and the agent's stop.
- `estimate-case-check-sends-back-a-faulty-case` — a file sent back, fixed by Edit and passed stands live (660, 662, 664); a round after a built Case with no edit of its file did not come (the round 660 Q7 came with Edits of the file).
- `estimate-ask-query-before-a-create` — a `create` without a `ref`.
- `estimate-case-check-requires-a-backlog-item-decided-on-its-page` — an item taken from the backlog.
- `estimate-case-check-shows-only-the-checked-case` — the first reply the `Stop` check refuses.
- `estimate-spec-write-reaches-the-approved-spec` — a Case ratified in Work Mode.
- The Estimates of the sprint close (`estimate-hi-writes-frontier`, `estimate-hi-takes-a-conserved-spec`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-brief-written`, `estimate-backlog-renders`, the three `estimate-sprint-close-*`, the three `estimate-sprint-migration-*`) — the session that closes the sprint, or the one after it.

## Observations

- Expected red: `guppi casecheck --subagent` sends back a summary of `case-guppi` with no `**Case:**` line until the librarian renders `.claude/agents/case-guppi.md` from `rule-case-build`.
- `guppi grepguard` runs only after the render of `.claude/settings.json`. Probed by hand with the Grep tool: the glob `!**/decisions/** *.md !**/decisions/**` over `vault/wiki/` printed no Decision page, and `**/{handoff,work}.md !**/decisions/**` at the root still matched the handoff files.
- `supersede_children` of `generate` finds a child page only when it stands: in one unit a parent page is written through the first record of its sub-cases, and the superseding record comes later in the yaml order; an order where the superseding record comes before the parent's page is not covered by a test.
- `estimate-ask-searches-at-prespec` failed at `/hi` (L4) on the order of the searches, and 664.3 updates the same page; the failure stands in the ledger before the update.

## For the next session

- `estimate-ask-searches-at-prespec` failed (L4): in two of three ask-guppi runs a Read came between the rules Grep and the Greps of the other categories — whether the frame of `ask-guppi` or the Criterion changes.
- A renamed or dropped target of a ratified Case needs a new number, and no check says so before the Spec hook (`rule-ledger-line-withdrawn-on-re-ratification` stands in the backlog).
- C1 and C2 of the sprint were left for a later session.

## Ask the person

- `estimate-permissions` — needs the person — in a session after the render of `.claude/settings.json`, did a Read, Grep or Glob of `case-guppi` under `~/.claude/projects/c--PROJECTS-GUPPI/` ask for permission? (No `case-guppi` of session 1616 made such a call.)
