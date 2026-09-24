# Handoff — 2026-09-23, session 1859: the Spec written by a hook, the re-showing by a ratified copy

## Notes from memory

- The session crossed midnight: it opened on 2026-09-23 at 18:59 and closed on 2026-09-24. Every ledger line stands in `raw/2026-09-23/1859/ledger.md`.
- The person found the re-showing of Cases heavy and asked for a lighter form. The design of Case 387 came out of a long discussion. The person proposed that a hook, not the agent, writes the Spec, and that `given`, `when`, `then` and `tasks` are English in the chat. The person does not like to read English prose, but accepted English in those sections because they become the Criterion word for word.
- The ratified copy was placed beside the plan file, outside the repository (`<plan>.ratified.md`). The person said it is a temporary file and the place does not matter much.
- The pre-spec of this session found eight contradictions in Case 387 and three frame findings in 384–386. Cases 384–388 were shown again in one reply and ratified again. The re-ratification carried no `LEDGER` block: the lines were the same as the ones already written. That gap is Case 389 (defer).
- The person asked for the agent's report after the ask-guppi findings — each finding numbered, the fix proposed, the decisions needed — to become a rule. It is in Case 388 (Frontier line C10).
- `estimate-case-protocol-case-form` and `estimate-case-protocol-loaded` speak of the re-showing that Case 387 changes. The person gave both to Slice 3g, the one pass over the Estimates, which rewrites them whole.
- C1, the one pass of Slice 3g, was left for a later session (`[-] · sprint`).

## Direct instructions to the librarian

- The yaml of `2026-09-23/1859` holds several `update`s of one page from different Cases. Apply them in ledger order: `rule-case-protocol` by 383, 387.1, 387.2, 387.3; `rule-prespec` by 387.4, then 388; `rule-hook-registry` by 387.2, then 387.3. The anchors were checked in that order by `prespec --check` (exit 0).
- The re-ratification of 384–388 wrote no new decision lines. The Spec in `spec.md` holds the texts as ratified again; the decision lines of the first ratification stand for them.
- Case 384 carries `{supersedes:case 382}`, Case 388 carries `{supersedes:case 380}`: both take up earlier defers.
- Two Insights go `actioned`: `insight-workflow-case-schema-silent-on-what-the-scripts-accept` (383) and `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` (388). By Case 385, `insight-workflow-contract-change-leaves-its-derived-text-stale` gets `addressed_by: decision-case-378.5` back. Case 385 also changes the rule of synthesis itself: from this run on, `addressed_by` moves only to a later case.
- The render of `.claude/settings.json` registers the new hooks `guppi ratified` (on `Stop`) and `guppi ratified --edit` (on `PostToolUse`). The code is already in commit `733132c`.
- Case 386 changes `guppi sprint`: after `uv run guppi sprint`, `sprint.md` should have a blank line after every milestone heading. The same run is the reading place of `estimate-sprint-renders-the-backlog`.
- The new lesson `lesson-case-designed-in-dialogue-not-checked-against-its-rules` may sit near `lesson-case-context-claim-wider-than-its-search` and the lessons of `insight-workflow-case-schema-silent-on-what-the-scripts-accept`. Judge the cluster by its root cause.

## What actually got done

- Ratified: Cases 383, 384, 385, 386, 387.1–387.4, 388; deferred: 389 (at Retro). Frontier: C2 closed `· work` by a reading; C3–C10 closed by Cases; C1 left `[-] · sprint`; C11 deferred by Case 389; W1 and W2 stay open.
- Code, commit `733132c`: `guppi/ratified.py` (new: the Spec writer, the reconciliation, the one comparison `differences`), `guppi/prespec.py` (`check_ratified`), `guppi/bashguard.py`, `guppi/sprint.py`, `guppi/cli.py`; `plan_path` moved from `gate.py` to `ledger.py`, `tagged_blocks` from `prespec.py` to `materialize.py`; tests `tests/test_ratified.py` (new, 15), `tests/test_prespec.py` (+5), `tests/test_bashguard.py`, `tests/test_sprint.py`. `make test`: 616 passed, 2 skipped; `make style` clean.
- A probe in the scratchpad parsed this session's own Cases 383–388 with the new chat parser: no error. The then blocks matched the approved Spec, except that the hook writes a multi-line `sections` value as `|-` with no final newline. `generate` strips that newline.
- Readings in the ledger: `estimate-sprint-migration-index-dissolved` passed; `estimate-prespec-checks-the-ratified-copy` passed; `estimate-bash-guard` passed.
- Readings not yet possible: `estimate-synthesis-keeps-actioned-by-the-mark` (a librarian run on a marked lesson under an `actioned` Insight); `estimate-sprint-renders-the-backlog` (`sprint.md` after this run); `estimate-language-followed` (by hand, next session); `estimate-spec-write-copies-the-ratified-case` and `estimate-spec-reconcile-shows-a-changed-case` (live, first ratification and first edit of the next session); `estimate-prespec-reconciles` (by hand, first `/pre-spec` after the render).
- Not done: the 19 pending readings of the previous brief and the old unticked boxes of the Specs (W1, W2); the one pass of Slice 3g (C1). From the next session, the agent creates the plan file with its title line before the first Case, so that the hook finds it.
