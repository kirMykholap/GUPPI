# Brief — 2026-09-24, after the librarian's run on session 1303

Written by the librarian from `vault/raw/2026-09-24/1303/handoff.md`, the two `materialize.yaml`
the walk named (`2026-09-23/1859`, extended with 0 entries; `2026-09-24/1303`, written by
`materialize` with 26 entries, 4 appended by the librarian's synthesis) and `tags.md`.

## Where things stand

- Plan Mode of session 1303 ratified Cases 390, 391.1, 391.2, 392.1–392.4 and 393, and deferred
  394 at Retro. Cases 391.2, 392.1, 392.2 and 393 were shown and ratified again after pre-spec;
  their decision lines stand once, from the first ratification. Frontier: C2 and W3 closed
  `· work`, C3 → 391, C4 → 390, C5 → 392, C6 → 393, C1 left `[-] · sprint`. From the handoff.
- Work Mode, commit `00089c4`: `guppi/context.py` (new), `guppi/ledger.py` (`is_main`,
  `transcript_records`), `guppi/cli.py`; tests `tests/test_context.py` (new, 7),
  `tests/test_ratified.py` (+1). The handoff reports `make test` 624 passed, 2 skipped, and
  `make style` clean.
- The session's readings: 6, all `passed` — `estimate-spec-write-copies-the-ratified-case` (L3),
  `estimate-case-protocol-acknowledging-reply` (L16, against the Criterion Case 390 wrote at L2),
  `estimate-spec-reconcile-shows-a-changed-case` (L21), `estimate-generate-fails-alone` (L22),
  `estimate-prespec-binds-a-sprint-line` (L23), `estimate-rules-schema-checked` (L24).
- This run, 1303 yaml: 26 entries from the ledger and 4 from synthesis, 30 of 30 `applied`. None
  `failed`, none `incomplete`, none `unparsed`; 2 marked `near`; the defer of 394 marked `exists`.
  The ledger has 26 lines; the yaml has an entry for each of them. `generate` wrote 0 pages for
  the 1859 yaml and 38 for the 1303 yaml.
- Pages created: 9 decisions (390, 391.1, 391.2, 392.1–392.4, 393, 394), 2 rules
  (`rule-frame-check`, `rule-context-size`), 4 estimates
  (`estimate-frame-check-finds-a-contradiction`, `estimate-case-protocol-checks-its-frame`,
  `estimate-context-size-shown-after-each-reply`, `estimate-context-size-warns-past-the-limit`),
  2 lessons (clustered by synthesis and archived by cleanup in the same run).
- Pages updated: 9 rules — `rule-case-protocol` by 390 (its defer of 389 superseded), 391.2 and 393
  in ledger order; `rule-hook-registry` by 392.1 then 392.2, `built → draft` by the cascade;
  `rule-context-size` by 392.2; `rule-harness` by 392.3 and its new child, `built → draft` by the
  cascade; `rule-spec-write` by the defer of 394, `draft → built` by the cascade; `rule-plan-mode`
  by the backlink of `rule-frame-check`; `rule-page-generation`, `rule-rules-schema` and
  `rule-spec-reconcile` `draft → built` by the cascade. 8 estimates — 6 `pending → passed` by the
  readings above (`estimate-case-protocol-acknowledging-reply` first had its Criterion replaced by
  390); `estimate-harness-pipeline` (392.3) and `estimate-hook-registry-rendered` (392.4)
  `passed → pending`, Criterion replaced whole. 2 insights. The 2 new lessons, set `clustered`.
- Insights: `insight-workflow-case-written-without-reading-the-pages-it-changes` `actioned` by
  391.2.
- Synthesis, the pairs beside it:
  - `lesson-case-frame-read-without-the-estimates-of-the-pages-it-edits` (L25,
    `addressed_by: decision-case-391.2`) → a child of
    `insight-workflow-case-written-without-reading-the-pages-it-changes`. The Insight's
    `addressed_by` names 391.2 as well, a case not later, so the field stands and the Insight stays
    `actioned` (case 385).
  - `lesson-spec-write-sub-point-opening-with-a-code-span-unpadded` (L15,
    `addressed_by: decision-case-393`) → a child of
    `insight-workflow-case-schema-silent-on-what-the-scripts-accept`, `actioned`; 393 is later than
    383, so its `addressed_by` moves to `decision-case-393`, status kept (case 385).
- Cleanup moved 5 pages to the archive: `decision-case-389` (superseded by 390), the 2 new lessons,
  and the 2 earlier children of the Insight actioned by 391.2
  (`lesson-plan-mode-contract-change-skips-the-estimates-blocks`,
  `lesson-case-designed-in-dialogue-not-checked-against-its-rules`).
- Renders: `.claude/settings.json` (the hooks `guppi context` on `Stop` and
  `guppi context --prompt` on `UserPromptSubmit`), `.claude/agents/frame-guppi.md` (new),
  `vault/wiki/case-schema.md`. `render`, `sprint` and `glossary` printed nothing on stderr;
  `sprint.md` and `glossary.md` did not change.

## Readings due

No Estimate stands `failed`. 23 stand `pending`; every target stands `draft`: each rule named
below and `entity-sprint-migration`.

From an unticked `- [ ] read …` line of `vault/raw/2026-09-24/1303/spec.md`:

- `estimate-frame-check-finds-a-contradiction` — `rule-frame-check` — L131, by hand, two live
  dispatches in the next session.
- `estimate-case-protocol-checks-its-frame` — `rule-case-protocol` — L184, by hand, at the close of
  the first session with `frame-guppi`.
- `estimate-context-size-shown-after-each-reply` — `rule-context-size` — L261,
  `uv run pytest tests/test_context.py`, then by hand in the VS Code chat in the next session.
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` — L314,
  `uv run pytest tests/test_context.py -k limit`, then by hand at the first prompt past 400 000
  tokens.
- `estimate-harness-pipeline` — `rule-harness` — L349, `make test-harness`, the first three steps
  of `make lint`, and the Purpose by hand.
- `estimate-hook-registry-rendered` — `rule-hook-registry` — L378,
  `uv run pytest tests/test_render.py` and `uv run guppi render --check` after the render.

From an unticked `- [ ] read …` line of `vault/raw/2026-09-23/1859/spec.md`:

- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` — L161.
- `estimate-sprint-renders-the-backlog` — `rule-sprint` — L203.
- `estimate-language-followed` — `rule-language` — L261.
- `estimate-prespec-reconciles` — `rule-prespec` — L497.

No read line in a Spec of the walk; the place is the page's `method`:

- `estimate-agent-writing-followed` — `rule-agent-writing` — by hand in the next session: the
  section in `CLAUDE.md` and one reply of the agent against it.
- `estimate-carry-over-writes` — `rule-carry-over` — pytest over the skill's render, plus one live
  reading of a carried-over session.
- `estimate-case-protocol-case-form` — `rule-case-protocol` — by hand, the Cases of a session at its
  close.
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` — by hand, the ledger and the
  preview of the first session where a lesson and the Case that closes its cause stand together.
- `estimate-case-protocol-loaded` — `rule-case-protocol` — at the first `/hi` of a session by hand,
  plus the preview cases of `tests/test_ledger.py`.
- `estimate-documentation-completes` — `rule-documentation` — `make test-documentation`; the live
  reading by hand.
- `estimate-one-judgment-one-implementation-followed` — `rule-one-judgment-one-implementation` —
  `render --check` exit 0, then by hand the section in `CLAUDE.md` and the diff of the next Work
  Mode session.
- `estimate-retro-report-holds-each-fact-once` — `rule-retro` — by hand at the first `/retro` after
  the render.
- `estimate-session-phases-in-order` — `rule-session` — by hand at the close of a session.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — the tree by hand at the
  close of the sprint.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — `make lint` exit 0, or only
  unread lines on the sprint page's own Estimates.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — `make test` on the last commit
  of `migration`, then `git log` of `main` after the merge.
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` — by hand:
  `ls vault/wiki/*/schema.md` empty, `index.md` absent, the grep over `guppi/` and `tests/` empty,
  `render --check` and `glossary --check` exit 0.

## Deferred

One item. The previous brief's two left the list:
`insight-workflow-case-written-without-reading-the-pages-it-changes` went `actioned` by Case 391.2;
the defer of `rule-case-protocol` by Case 389 was retired by Case 390 (`supersedes: case 389`).
`insight-workflow-code-live-before-the-page-it-reads` is `open` and named by the sprint page's
Backlog, so it is not listed here (case 229.4).

1. `rule-spec-write` — deferred by Case 394, standing in 1 brief. Related Insight
   `insight-workflow-case-schema-silent-on-what-the-scripts-accept`, `severity` 0, `actioned`. The
   deferred behaviour: a sub-point value whose outer span is unpadded and whose content opens and
   closes with a code span is read with its edge backticks eaten, not refused.

## Flags

- `near`, from the index check (no page merged):
  - `rule-frame-check` near `rule-prespec`: both check a Case against the pages of the vault; the
    first before the Case is shown, the second after ratification, before the Spec.
  - `lesson-case-frame-read-without-the-estimates-of-the-pages-it-edits` near
    `lesson-plan-mode-contract-change-skips-the-estimates-blocks` (archived in this run): both name
    the Estimate pages a Case edits as left unread; the new lesson adds the Purpose of the parent
    and the code that already makes the judgment.
- No entry is marked `failed`, `incomplete` or `unparsed`. No Estimate stands `failed`.
- `generate` printed no move to the Backlog and dropped no milestone in this run.
- No contradiction found in this run.
- Stale defers, from lint: `rule-work-mode` and `rule-subagent-guppi` 31 times since case 29,
  `rule-morph` 1 time since case 239. All three are on the sprint page.
- `rule-spec-box`: three findings — missing `kind`, missing `estimates`, orphan.
- No MOC candidate: no input this run names a threshold crossed.
- `make lint`: 92 findings, exit 1 — 62 on 31 legacy decision pages (`missing section ## Context`
  / `## Problem`), 23 `unread` (all `pending`), 3 on `rule-spec-box`, 3 `deferred` counters,
  1 `unmigrated: 21 pages in the shape before case 193`.

## Next session

Cases — what needs a decision:

- The handoff gives the rewrite of `estimate-case-protocol-case-form` (to take in 391.2) and of
  `estimate-case-protocol-loaded` (to take in 390, 391.2 and 393) to Slice 3g; the Slice 3g
  heading of `sprint.md` names no item. From the handoff and `sprint.md`.
- The person judges from the numbers of the next session whether `frame-guppi` pays; if not, it is
  rolled back by a Case. From the handoff.
- The 400 000 limit of 392.2, a constant in `guppi/context.py`, was proposed by the person as a
  figure to discuss. From the handoff.
- If the `systemMessage` of the `Stop` hook is not shown in the VS Code chat, the handoff names
  about 20 tokens a reply written by the agent as the accepted fallback. From the handoff.

Work — what is done without a decision:

- Take the pending readings of Readings due, by slug: `estimate-frame-check-finds-a-contradiction`,
  `estimate-case-protocol-checks-its-frame`, `estimate-context-size-shown-after-each-reply`,
  `estimate-context-size-warns-past-the-limit`, `estimate-harness-pipeline`,
  `estimate-hook-registry-rendered`, `estimate-synthesis-keeps-actioned-by-the-mark`,
  `estimate-sprint-renders-the-backlog`, `estimate-language-followed`,
  `estimate-prespec-reconciles`, `estimate-agent-writing-followed`, `estimate-carry-over-writes`,
  `estimate-case-protocol-case-form`, `estimate-case-protocol-ledger-line-form`,
  `estimate-case-protocol-loaded`, `estimate-documentation-completes`,
  `estimate-one-judgment-one-implementation-followed`,
  `estimate-retro-report-holds-each-fact-once`, `estimate-session-phases-in-order`,
  `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`,
  `estimate-sprint-migration-merges`, `estimate-sprint-migration-rule-class-files-dissolved`.
- The unticked boxes of the Specs: 6 `read` lines in `vault/raw/2026-09-24/1303/spec.md`; 4 in
  the Spec of 1859, moved with its unit to `vault/archive/migration/2026-09-23/1859/raw/spec.md`
  by `guppi archive` in this run.
- No ledger line of 1303 was left unapplied. The tree at the close of this run holds only the
  librarian's own writes and the session's `handoff.md`; this brief's commit covers `vault`,
  `CLAUDE.md` and `.claude`.

## Readings at the close

- `make test`: 624 passed, 2 skipped.
- `make lint`: 92 findings, exit 1.
- Pages: 63 rules, 117 estimates, 48 lessons, 21 insights, 541 decisions, 4 entities.
