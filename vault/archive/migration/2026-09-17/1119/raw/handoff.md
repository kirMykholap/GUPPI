# Handoff — 2026-09-17, session 1119: the ledger Insight settled, the Spec ticked by the scripts, the sprint as milestones, the categories discussion

## Notes from memory

- The session began with the person picking items one at a time (F2, F4, F3, F6) and
  asking for the plain meaning twice — on 225 and on 227. Each time the Case stood as
  proposed.
- F6 (`sprint --check`) opened a long discussion — what an Entity is, how it stands to a
  Rule and an Estimate, whether the model holds without product code. Six candidate
  definitions fell in turn; the person's last position: the vault is a base of promises,
  fine for development, not for "a helper for a car mechanic"; Entity always ends up
  about code; no universality in sight. The agent's position: universality is at the
  level of the mechanism, and the missing step is the category set as data of the
  project. Nothing decided. The record is `raw/2026-09-17/1119/categories-discussion.md`;
  Case 230 defers `index` to the next session. The person wants to think more.
- The person asked for the milestones model themselves (F11 → 229): the Frontier from
  the current milestone only, a Backlog for "some day", the brief's Deferred without what
  the sprint page names. Two Backlog lines are plain text without a page — by choice,
  no placeholder.
- Case 233 (pre-task's ten findings) was ratified whole; one finding crosses the defer of
  `index` (230) — shown, accepted: the defer is about the definitions of §1/§6, the
  change a table row.
- At Retro the person asked why pre-task did not see that `sprint --check` reads a page
  shape the same plan changes. Discussed: the information is in the Spec, the check is
  cheap, the value is low — the answer never changes the plan. Decided: no pre-task
  change; a lesson (`lesson-work-mode-check-reads-a-page-the-same-spec-changes`) and one
  sentence for `rule-work-mode` in Slice 3b — a check that reads a page the Spec updates
  is read after the librarian's run, its red in Work Mode is an expectation, not a
  finding. Case 235 was proposed and withdrawn.
- Caveat on 224.3: the new knowledge lesson is *not* a child of the Insight — its root
  cause is the opposite of the Insight's pattern; the Insight's `pattern` is updated by
  `set` and stays `actioned`. Synthesis should not reopen it on that lesson.
- Caveat on the readings: `estimate-generate-walks-dates` was read against the Criterion
  as recut by 211.3 (the `method` fields), not against "walks dates"; the person accepted.

## Direct instructions to the librarian

- Check first: the two `update` entries of `rule-sprint` (227 and 229.2) and of
  `rule-carry-over` (225 with `change` alone, `{supersedes:case 223}`; 233.4 with a
  `replace`) apply in ledger order; the second `replace` of 229.2 and of 224.1 are in the
  same entry as the first.
- `index` appears twice: a `defer` (230, a Rule-class file — nothing to do but the
  Decision page's `## Deferred`) and an `update` (233.3, by hand, done). Not a conflict.
- The six in-place amendments of Case 233 live inside Cases 224.2, 224.3, 226.2, 229.2,
  229.3 and 229.4 of the Spec — no separate line; do not look for a 233 entry for them.
- 229.1 puts `## Milestones` and `## Backlog` on `entity-sprint-migration` through
  `sections`; `SECTION_ORDER` in `generate` now orders them after `How it works`. After
  `generate`, step 5 `guppi sprint` rewrites `sprint.md`, and `make lint`'s new second
  step `sprint --check` goes green; until then it is red — expected.
- Synthesis: `lesson-transcript-keeps-the-text-before-a-tool-call` (knowledge) is the
  opposite of `insight-ledger-hook-reads-only-the-final-text`'s old pattern; do not
  cluster it there. `lesson-work-mode-check-reads-a-page-the-same-spec-changes` (error)
  and `lesson-hi-substitution-refused-when-the-permission-classifier-is-unavailable`
  (knowledge) are new; compare with the lessons index.
- New Estimate pages: `estimate-generate-ticks-the-spec`, `estimate-render-harness-ticks-the-spec`,
  `estimate-sprint-checks-the-file`. Recuts with `set.method`: `estimate-ledger-write-lifts`,
  `estimate-case-protocol-loaded` (with `sections: Criterion`), `estimate-hi-writes-frontier`,
  `estimate-harness-pipeline`, `estimate-retro-loads`. `unmigrated` should fall by five.
- The Spec's page and render lines: `generate` ticks the page lines (226.1) and the plain
  `guppi render` ticks the render lines (226.2) — the first live reading of both; the
  Spec is `raw/2026-09-17/1119/spec.md`. Expect 27 page lines and 5 render lines to turn
  `[x]` in that run; report the count.
- Renders this run: `CLAUDE.md` (224.2), `.claude/skills/hi/SKILL.md` (229.3),
  `.claude/agents/librarian-guppi.md` (229.4), `.claude/skills/retro/SKILL.md` (233.2),
  `.claude/skills/carry/SKILL.md` (233.4).
- The brief: by 229.4 the Deferred list leaves out `rule-work-mode`, `rule-subagent-guppi`,
  `rule-spec-box` — they stand on the sprint page. `index` (230) has no page: list it from
  the Decision page's purpose.
- Readings due, none takeable in the session: `estimate-case-protocol-loaded` (the first
  turn of the next session), `-generate-ticks-the-spec` and `-render-harness-ticks-the-spec`
  (this run's ticks — the next session reads them), `-sprint-checks-the-file` and
  `-harness-pipeline` (`make lint` after this run), `-sprint-renders-the-backlog` (the
  rendered `sprint.md`), `-brief-written` (this brief), `-hi-writes-frontier` (the next
  `/hi`), `-retro-loads` (the next `/retro`), `-carry-over-writes` (a live `/carry`), the
  three of the sprint (the close).
- Flags for the next Plan Mode: (1) the definitions of the categories — defer 230, the
  record in the session folder; (2) one sentence for `rule-work-mode` on a check that
  reads a page the Spec updates (Slice 3b, defer 231); (3) `schema-prose` in lint reads
  one section per table row of a schema.md — three sections in one cell gave two false
  findings; the row was split; (4) `render --sync` at `/hi` was refused by the permission
  classifier once — the lesson above; (5) `rule-git-context` / `rule-github-issues`
  (defer 220) still at the close of the sprint.

## What actually got done

- Ratified: 224.1–224.3, 225, 226.1, 226.2, 227, 229.1–229.4, 233.1–233.5, 234; deferred
  230 (`index`), 231 (`rule-work-mode`, `rule-subagent-guppi`), 232 (`rule-spec-box`).
  Readings `passed`: `estimate-generate-walks-dates`, `estimate-documentation-completes`,
  `estimate-pretask-reconciles`, `estimate-ledger-write-lifts`. Three lessons.
- Code, commit `d64a399` on `migration`: `guppi/gate.py` (the advice), `guppi/generate.py`
  (`tick_spec`, `SECTION_ORDER`), `guppi/render.py` (`tick_render_lines`),
  `guppi/sprint.py` (`--check`, the render by milestone, the plain line), `Makefile`
  (`lint` — three steps); tests 411 → 424, all green; `make style` clean.
- One-off: the `ref` field removed from `rule-carry-over` by a script (225).
- Rule-class by hand: `entities/schema.md` and `schema.yaml`, `index.md` (the `sprint.md`
  row, §2), `glossary.md` (the Sprint row), `case-schema.md`.
- Not done: every page create and update (this run); the five renders (this run); the
  first `guppi sprint` on the milestones page (this run); the readings listed above;
  Slice 3b; the definitions (230).
