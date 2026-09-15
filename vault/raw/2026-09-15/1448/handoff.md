# Handoff — 2026-09-15, session R: the derived sections dropped, the librarian's Insight through generate, the gate on a typed command (Cases 164–172)

## Notes from memory

- The owner opened on F3 (the refused Insight), asked twice what an Insight is for and
  whether a person can create one in a session; the answer that held: no — a lesson, a
  defer or a Case cover the need, and an Insight without children is archived by the
  cascade (104.3). Case 164 stayed as proposed.
- F5 (the `parent` mismatch of `rule-lint`) turned into the question "do we need the
  derived sections at all?" The owner chose to drop them (165.2 as a defer, then taken up
  the same session as 166.1–166.4 with a migration). 165.1 (derive on every write) was
  shown and not taken; it has no line.
- 166.3 exists only because one ledger line carries one `supersedes`: 166.2 supersedes
  164, 166.3 supersedes 114. The owner asked why twice; the answer is in the Case.
- 167 is the owner's own item: the `LEDGER` block first in the acknowledging reply. Every
  acknowledging reply of this session still followed 157 (block last), since `CLAUDE.md`
  changes only by the render; the reading of 167 is the next session's first such reply.
- 168 changed shape during the dialogue: from "give 'What the next session does first' a
  source" to a new second section "Readings due" (the Estimates `pending`/`failed` after
  the run, one line per block, the place of reading from the Spec's `- [ ] read` line);
  the "not done" of the handoff stays in "Where things stand". The Insight
  `insight-librarian-frame-omits-required-reads` is `actioned` by 168.
- 169: the claim that a `UserPromptSubmit` hook with exit 2 blocks the typed prompt comes
  from the Claude Code hooks reference, not from a probe; no `knowledge` lesson carries it.
  The reading of 169.1 is the live test.
- Pre-task (`ask-guppi`) found that 166.2's `{supersedes:case 164}` skips every entry of
  164 — hence 171 (164's sentence, `{supersedes:case 124.2}`) and 172 (block 148.1
  restated without "the body sections stay", `{supersedes:case 148.1}`). The lesson line
  L30 records it.
- Known and not acted on (frontier F17): the head Criterion of `estimate-generate-writes`
  and `estimate-cleanup-moves` still names `## Children` and `## Estimates` — no
  `### case` block, so no supersedes reaches it, and an Estimate has no line of its own
  (72.5); `rule-ledger-write` after 169.1 names one refusal text where the gate now has
  two; both are the pattern of `insight-workflow-contract-change-leaves-its-derived-text-stale`.

## Direct instructions to the librarian

- Order matters on `rule-page-generation`: 164 is superseded by 166.2 and must not apply
  (its `replace` would otherwise land before 171's identical one and 171 would fail
  "not unique"). Check after the run that the sentence "A `create` in `insights/` from a
  ledger line is refused…" stands once, marked `case 171`, and that the three `replace` of
  166.2 and the one of 166.3 all applied — they sit in one paragraph on disjoint text.
- `estimate-generate-writes` after the run: blocks 166.2, 166.3, 172 present and
  `pending`; blocks 114, 124.2, 148.1 removed; no block 164. `decision-case-164`,
  `-114`, `-124.2`, `-148.1`, `-150`, `-157`, `-162`, `-165.2` superseded and archived by the
  cascade.
- The `failed` entry of `raw/2026-09-15/1110/materialize.yaml` — the synthesis create of
  `insight-retro-typed-command-is-never-a-tool-call` — is retried by the walk and should
  apply now (the code of 164/166.2 is committed): page written, `severity` 2, the two
  `ref` findings on the retro lessons gone. Report its stderr if it still fails.
- Pages are written without `## Estimates`, `## Children`, `## Parent`,
  `## Implementation`, `## Code`, `## Insight`, `## Addressed by` — the schemas no longer
  name them and the migration removed them from every live and archived page. A page
  that still shows one is a finding for the brief.
- 168 applies to `rule-brief` and renders `.claude/agents/librarian-guppi.md`, but you
  were dispatched with the frame as it was: write this brief by the frame you loaded.
  The reading of 168 is the brief of the next run.
- 169.2 renders `.claude/settings.json` with `uv run guppi gate` as the second
  `UserPromptSubmit` command; `guppi render --check` must exit 0 at the close. The typed
  `/retro` of this session (17:5x) left no mark and met no gate — expected, the render
  had not happened; do not flag it as a failure of 169.
- The lesson `lesson-supersedes-in-the-same-session-skips-the-earlier-cases-entries`
  (L30): compare with the lessons on `supersedes` and on `materialize`; I know of none with
  this cause. Its Insight candidate, if any, is
  `insight-workflow-contract-change-leaves-its-derived-text-stale` — different mechanism
  (stale text vs skipped entries); my judgment is not the same cause.
- `sprint.md`: no change.
- Expected lint after the run: 72 → 70 (the two `ref` of the retro lessons gone); the 62
  of Cases 1–28 and the 8 `schema` + 2 `orphan` of the placeholders stay.

## What actually got done

- Ratified: 164 (`rule-page-generation`, supersedes 124.2; superseded by 166.2 before
  it applies), 165.2 (defer, taken up by 166.1), 166.1 (eight schema files by hand),
  166.2 (`generate` writes no derived section; migration; supersedes 164), 166.3 (the
  cascade of 114 removed; supersedes 114), 166.4 (`rule-cleanup`), 167
  (`rule-case-protocol`, supersedes 157), 168 (`rule-brief`,
  `insight-librarian-frame-omits-required-reads` actioned), 169.1 (`rule-retro-commit`;
  `rule-event-log`, `rule-ledger-write` text), 169.2 (`rule-hook-registry`), 169.3
  (`rule-retro`, supersedes 150), 170 (defer Slice 3b, supersedes 162), 171
  (`rule-page-generation`, contract same, supersedes 124.2), 172 (`rule-page-generation`,
  supersedes 148.1).
- Readings: `estimate-index-check-merges` (147.3) and `estimate-synthesis-clusters`
  (147.4) `passed` against the brief of Q's run; `estimate-case-protocol-loaded` blocks
  159 and 157 `passed` on Case 164 and its acknowledging reply. 160's second box ticked
  in `1110/spec.md` (lint raised no `ref` on the two pages at `/hi`).
- Code, commit `f78747c` on `migration`: `guppi/generate.py` (SECTION_ORDER without the
  seven sections; `create` writes none; `rebuild_list`, `derive_insight`,
  `derive_addressed_by`, `links`, `paths_list` removed; `save` writes as is; the cascade
  step of 114 removed; a `create` in `insights` passes when the entry carries
  `librarian`, the refusal line now says case 171), `guppi/cleanup.py` (`unlink` edits the
  field only), `guppi/gate.py` (`skill_of` reads `prompt` of a `UserPromptSubmit` payload
  for `/pre-task`, `/retro`, `/handoff`; `typed()`; the refusal text for the person),
  `tests/test_generate.py` (+2 tests, four rewritten on the fields),
  `tests/test_cleanup.py` (one assertion), `tests/test_gate.py` (+5),
  `tests/test_lint.py` (schema copies, three anchors moved to Purpose). 377 green,
  `make style` clean, `guppi render --check` exit 0, `guppi lint` 72.
- By hand: `vault/wiki/{rules,entities,lessons,insights}/schema.yaml` and `schema.md`
  (166.1). The migration from the scratchpad: 80 pages under `wiki/` and `archive/`
  (rules, lessons, insights) lost their derived sections; the `write_page` round-trip was
  byte-identical on every page before the removal; `git diff` on the vault shows
  removals only outside the schemas.
- Not done: the live halves of every reading — 166.2, 166.3, 166.4, 172 (the pages after
  this run, the backlinks in Obsidian — the owner's half), 167 (the first acknowledging
  reply of the next session), 168 (the brief of the next run), 169.1–169.3 (the first
  typed `/retro` of the next session, after the render of `settings.json`); the head
  Criterion texts and the second refusal text (F17); Slice 3b (170).
