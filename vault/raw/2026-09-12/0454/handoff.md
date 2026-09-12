# Handoff — 2026-09-12, session I: the artifacts of Plan Mode (Cases 58–69)

## Notes from memory

- The owner reshaped four Cases mid-discussion, each ratified in their variant: 58 (the
  librarian may read the Makefile, `guppi/`, `tests/`; only the wiki is rationed), 59.5
  (one short-form Case per deferred decision under `## Deferred`, not one Case for all;
  ratified twice, the second time with `rule-retro` and `rule-spec-capture` added), 59.6
  (no governed file has a hand-written part, `CLAUDE.md` included), 59.8 (the slug renamed
  from rule-system-prompt to `rule-claude-md`). Case 59 is a parent with shared context and
  problem; its eight sub-cases carry their own given, when, then.
- The owner said a Work Mode fork is never a return to Plan Mode: the fork becomes a
  short-form Case under `## Deferred`, worked next session. That clause is recorded in the
  problem of Case 59 and in Case 64; it belongs to `rule-work-mode` (Slice 3b).
- The ledger of the day holds every decision line twice: the first writing, before 10:09,
  lacks the word `case` (`decision[58]…`) and will not parse; the second, at 10:59:36, is
  the grammar `materialize` reads. Treat the 33 malformed lines under `unparsed` as
  expected; `lesson-ledger-decision-line-written-without-the-case-word` records it and Case
  67 defers the fix of the schema table.
- Case 66 amended earlier Cases at pre-task: `rule-case-protocol` moves under
  `rule-claude-md` and leaves the children of `rule-plan-mode`; `rule-render-harness` keeps
  enforcement `check`; `rule-pretask` has no `implementation_ref`; `rule-claude-md` has its
  own nested Estimate `estimate-claude-md-rendered`.
- `rule-case-protocol` is updated by seven Cases (59.2, 59.3, 59.5, 59.6, 60, 62, 66) and
  `rule-pretask` by four (59.1, 59.2, 59.3, 59.6): the `replace` pairs were written to
  apply in ledger order, each `old` against the text the previous Case leaves. If a
  `replace` fails, the entry is a flag, not a repair.

## Direct instructions to the librarian

- Materialize walks three dates again; the yaml of 2026-09-12 is new. Expect 33 lines
  under `unparsed` (the malformed first writing) and no entry for them.
- `sprint.md` was already changed in Work Mode under Cases 58 and 59.5 (Slice 3 closed; the
  four Slice-5 items moved there). Do not change it again.
- The Deferred list of the brief: by case 59.5 it is built from the `defer` entries of the
  yamls — Cases 63, 64, 65, 67, 68, 69 — with the count of the previous brief plus one where
  the item was there (Slice 3c: 3; Slice 3b: 4; the archive in ask-guppi: 4); the four
  Slice-5 items leave the list. The count for 67, 68, 69 is 1.
- Two lessons on the ledger hook exist now: `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call`
  (session H) and today's `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn`.
  The owner asks you to compare them and say in the brief whether they share a root cause
  and what the next session should read in `guppi/ledger.py`.
- `lesson-subagents-parallel-on-one-tree-red-mid-flight` is a `knowledge` lesson; the owner
  will discuss it with Slice 3b, not before.
- The tag `tests` is declared under Case 61 (`new_tags`); `generate` should print no tag
  line this time.
- `make lint` will be red at `render --check` on `CLAUDE.md`, `.claude/settings.json`, the
  skills and agents whose pages this run changes: that is the next session's render, not a
  defect. `guppi lint` will show `ref` findings on `[[decision-case-59.4]]` and
  `[[decision-case-60]]` until your run creates those pages.

## What actually got done

- Commits, in order: `f2b2d83` render of four files, the ledger tail of session H, the Spec
  and Frontier; `8404072` Cases 59.4 and 60 (`generate`, `lint`, decisions schema, the 78
  pages migrated, `## Given` on ten pages); `7c745f3` 59.8, 60, 61 (`materialize`);
  `0ff3af5` 59.6, 59.7 (`guppi guard`, `render --sync`, BOM in `read_payload`); `2b7dd42`
  59.1–59.3, 59.6 (`guppi pretask --check`); `70588a8` Rule-class files by hand, `sprint.md`,
  the Spec ticked, the ledger; `a35f851` the Retro.
- `make test` 211 green, `make style` clean, `guppi pretask --check` on the Spec prints
  nothing. Readings passed: `estimate-spec-capture-appends`, `estimate-documentation-completes`
  (Slice 3 closes), `estimate-lint-catches`, `estimate-materialize-assembles`,
  `estimate-retro-loads`.
- Not done, for the next session: one manual `uv run guppi render` at its start (after
  that the hooks `guard` and `render --sync` are registered and `CLAUDE.md` is rendered whole
  from `rule-claude-md`); the live readings of `estimate-pretask-reconciles` (at its
  `/pre-task`), `estimate-hi-writes-frontier` (at its `/hi`), `estimate-generate-writes`
  (the live half, against this run), `estimate-governed-files-hook-refuses` (one refused
  Edit), `estimate-render-sync-reports` (the session after next), `estimate-claude-md-rendered`
  and `estimate-render-harness-reproduces` (the first render).
- Deferred: 63 Slice 3c, 64 Slice 3b, 65 the archive in `ask-guppi`, 67 the ledger grammar
  in `case-schema.md` and `rule-case-protocol`, 68 the wording of `rule-pretask`, 69 a
  show-only mode of `materialize`.
- The memory directory of the agent is empty (Case 62). `vault/Untitled.canvas`, an empty
  file Obsidian left, was deleted so the handoff gate passed.
