# Handoff — 2026-09-23, the passed-over sprint item, the chat form of a Case, the Frontier closers

## Notes from memory

- The person proposed Case 354 themself: a script counts how often a sprint item is put off and moves it to the Backlog, no agent judgment. The threshold was set by the person to ">= 3". They agreed that the counter reads the archived `frontier.md` files, consecutive sessions, reset by an `[x]` line.
- The person corrected the chat form twice (Case 355): `ratification` holds the ledger preview only, the agent's own text goes after one horizontal rule; a Case with sub-cases is shown in one reply. Before that, the agent showed the sub-cases of 354 one per reply with no instruction saying so.
- The person asked for the lint check of Case 362 in the same message that ratified 361. The agent went straight to 362 and wrote no LEDGER block for 361; `guppi gate` refused `/pre-spec` on the two items without lines. The lines of 361 were written late, at 01:39:48, with a lesson (L42).
- The agent changed ratified Spec text without showing it again, twice: a `problem` for Case 359 that the chat form lacked, and a sentence removed from the `context` of 361 after its re-ratification. Both were named in Notes; the person did not object. A lesson stands in the ledger. It is the same pattern Case 358 signs for Case 347.
- Pre-spec: ask-guppi returned 15 contradictions and 2 unnamed Estimates. 11 were repaired by amending Cases 354.1–354.4, 355.2, 356, 358, 360, 361, 362.1, 362.2, each re-ratified by the person; 4 were named as known (the `writes nothing else` sentence of `rule-page-generation`, the `needs nothing` line of `estimate-prespec-binds-a-sprint-line`, the archive paths — all 33 archived Frontiers sit under `<date>/<HHMM>/raw/` — and the render guard of Case 360, as for `rule-agent-writing`).
- Case 358 is the first Case that updates a Decision page (`decision-case-347`, `change` alone), and it changes `rule-decisions-schema` to allow that one History line. If `generate` refuses an update of a Decision page, it is a flag, not a repair.
- Two readings failed at Work Mode, and the person asked for them to be in this handoff:
  - `estimate-generate-fails-alone`: its Criterion expects the message "an update with no content in the Spec; applied by hand"; the code prints "…; nothing applied" since case 320. The Criterion is stale, not the code. A Case is due.
  - `estimate-sprint-migration-index-dissolved`: two live pointers at `index.md` remain — the docstring of `guppi/materialize.py:11` ("its route computed from `index.md` §5") and the Given of `estimate-case-protocol-case-form.md:18` ("`index.md` … are the Renders of their rule pages"). A Case is due.
- Readings not taken, with the reason:
  - `estimate-carry-over-writes` — needs a live `/carry` with the new step 1 of Case 347.
  - `estimate-generate-ticks-the-spec` — its second leg reads this session's `spec.md` after the librarian's run.
  - `estimate-sprint-migration-rule-class-files-dissolved` — its `method` requires `make lint` exit 0, which `estimate-sprint-migration-lint-clean` expects only at the close of the sprint; the two conflict. A question for a Case.
  - The 22 Estimates whose Criterion this session replaces — read after this run, in the next session (case 283).
- After some Edit calls `git diff` warned of CRLF in five files; the agent normalized them to LF with `sed`. The cause was not established.

## Direct instructions to the librarian

- Check first: Case 354's move runs in your own `generate`, after the cascade. On the live vault it counts 29 passes in a row for `rule-work-mode` and for `rule-subagent-guppi` (sessions 0652 of 2026-09-13 to 0034 of 2026-09-23, 1724 passed by since its line has no code span). Both lines move to the Backlog of `entity-sprint-migration`, and Slice 3b leaves the Milestones: expect two `moved to the Backlog` lines and one `milestone … left the Milestones` line in its History, each ending `· generate`, and the matching stdout lines. Slice 4 becomes the current milestone. The brief names them in Flags by the frame of 354.4 — your loaded frame is the one before 354.4, so read this paragraph as the instruction for this run.
- The same page takes several entries in one Spec, applied in entry order: `rule-sprint` (354.1 then 354.2 over its text), `rule-page-generation` (the same), `rule-case-protocol` (355.1, 355.2, 356.1, 356.2), `estimate-case-protocol-loaded` (four insertions before one anchor), `estimate-insights-schema-checked` (361, 362.1, 362.2), `estimate-decisions-schema-checked` (358, 362.1), `rule-skill-hi` and `estimate-hi-writes-frontier` (354.3, 356.1, 356.2). `guppi prespec --check` simulated all pairs and exited 0.
- Case 362.2 inserts a line with indentation into the YAML Render of `rule-insights-schema`; the agent checked in memory that the result parses and holds `single: [addressed_by]`. After your render, `vault/wiki/insights/schema.yaml` must parse and lint must give no finding on `insights/schema`.
- Case 360 creates `rule-one-judgment-one-implementation` with `ref: rule-claude-md`; `children` of `rule-claude-md` comes from that `ref`, not from a `set` (removed at pre-spec). The Render of `rule-claude-md` gains its marker line after `<!-- rule-agent-writing -->`.
- `{supersedes:case 352}` stands on L17: it clears `deferred_by` 352 on `rule-skill-hi`.
- Two Insights go `actioned` by Cases 359 and 360; their clustered lessons go to the archive by the cascade.
- One task line of Case 362.1 names seven Estimates; `generate` ticks it by the first slug, and the six other entries find no line of their own — no error.
- `addressed_by` in the `then` blocks of 359 and 360 is written as a bare slug, as Case 351 did; `generate` writes the wikilink.

## What actually got done

- Plan Mode: Cases 354–362 ratified (354.1–354.4, 355.1–355.2, 356.1–356.2, 357, 358, 359, 360, 361, 362.1–362.2), 56 decision lines, one lesson (L42). Frontier closed: C1, C2 `[-] · sprint`, C3–C12 by Cases, W1, W2 `· work`. Defer 352 taken up by 356.
- Work Mode, commit `f71b821`: the move of Case 354 in `guppi/generate.py` (`move_passed_over`, `frontiers`, `frontier_marks`, `passes_in_a_row`), `sprint.milestone_blocks` as the one parse of `## Milestones`; `check_frontier` of Case 356 in `guppi/prespec.py`, with `FRONTIER_LINE` imported from `generate`; `properties.single` of Case 362.1 in `guppi/lint.py`; tests in `tests/test_generate.py`, `tests/test_prespec.py`, `tests/test_lint.py`. `make test` 581 passed, 2 skipped; `make style` clean. The 10 code and test boxes of the Spec are ticked.
- Readings written (L57–L63): passed — `estimate-generate-cascades`, `estimate-prespec-binds-a-sprint-line`, `estimate-harness-pipeline`, `estimate-case-protocol-ledger-line-form`, `estimate-prespec-reconciles`; failed — `estimate-generate-fails-alone`, `estimate-sprint-migration-index-dissolved`.
- Not done: every page, render and `read` line of the Spec — this run and the next session; the two failed Estimates need Cases; `rule-work-mode` and `rule-subagent-guppi` were not taken and move to the Backlog.
