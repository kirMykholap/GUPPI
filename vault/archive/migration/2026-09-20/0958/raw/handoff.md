# Handoff — 2026-09-20, the debts of the Frontier, the Case protocol and the Frontier in two lists (Cases 264–269)

## Notes from memory

- The person chose the order: F2 as work, then F4, F5, F6, then two items of their own —
  the readability of `context` (267) and the split of the Frontier into Cases and Work
  (268). Slice 3b was deferred an eleventh time (269) with "the first item of the next
  session"; the person did not hesitate on that, the two rules of reading came first.
- Case 265 grew at the person's word: "take the four too" — the four Estimates in the shape
  before 193 were recut, one sub-case each, instead of waiting for their rules. Their
  readings: three taken this session, `estimate-documentation-completes` is the
  librarian's run of this one, read next session.
- Two items set a status by hand: `estimate-generate-renames` (264.1, `passed` — the
  reading of 09:38:37 in the 0740 ledger applies before this session's entries, the
  item does not undo it) and the three of 265 (`passed`, the promise unchanged). The
  person accepted both with the reason named; the lesson
  `lesson-estimate-update-must-carry-its-criterion-whole` says why it is heavy.
- The person removed a local memory the agent had written (two files under
  `~/.claude/projects/…/memory`); the rule is: a preference is a Case on a rule page or
  nothing. `lesson-agent-memory-is-not-the-product` records it. A line in
  `rule-claude-md` on it is a possible Case of the next Plan Mode, not decided.
- The seven-sentence cap on story sections was dropped in 267 at the person's question,
  with the reason that the shape of each section bounds it and no script counts sentences.
- 268 was discussed before it was a Case: the third list "Standing" was rejected for an
  exception in `rule-skill-hi` (pull and gh are no item while `sprint.md` names their
  decision); the person's condition was that the kind of an item comes from its source,
  never from reading pages — the librarian sorts in a new brief section, `/hi` places.
- Pre-spec's ask-guppi found six things, all taken as changes to 265, 268.1 and 268.2
  before the plan was approved: a `failed` Estimate in both lists, `rule-carry-over` and
  `rule-git-context` as second copies, two stale sentences of `rule-skill-hi`, the
  `method` of `estimate-hi-writes-frontier` lost between 265 and 268.2, the Deferred
  pages 220 and 243 (named as known, no supersedes).

## Direct instructions to the librarian

- Walk `raw/2026-09-20/0740` first: its line 17, the reading of
  `estimate-generate-renames`, was written after your last run and is uncommitted no
  more; then 0958. In 0958 the order of the yaml matters twice: 265 and 268.2 both update
  `estimate-hi-writes-frontier` — 268.2 comes later and its Criterion and `method` are
  the final state; 264.1 sets `estimate-generate-renames` `passed` after the 0740 reading
  made it so.
- Every `replace` `old` of 264.2, 267, 268.1, 268.2 was checked by grep this session:
  one occurrence each on `rule-prespec`, `rule-case-protocol`, `rule-brief` (three),
  `rule-carry-over`, `rule-skill-hi` (six), `rule-git-context`. A `failed` entry there is
  a fact for the brief, not something to repair.
- The renders due after `generate`: `.claude/skills/pre-spec/SKILL.md`, `CLAUDE.md`,
  `.claude/agents/librarian-guppi.md`, `.claude/skills/carry/SKILL.md`,
  `.claude/skills/hi/SKILL.md`. Your own frame changes in this run (268.1: the section
  Next session); the brief you write is the first by the new frame if the render lands
  before the brief step, as the frame says it does.
- Three Rule-class files were applied by hand: `case-schema.md` (267), `glossary.md`
  (268.2); the History line of 262 on `estimate-generate-renames` was quoted by hand
  (264.1) — the update item of 264.1 carries the Criterion of 262 verbatim and `passed`.
- Synthesis: two new lessons. `lesson-agent-memory-is-not-the-product` (error) has no kin
  I know of. `lesson-estimate-update-must-carry-its-criterion-whole` (knowledge) may sit
  near `lesson-ledger-estimate-line-carried-a-count-not-read` only by tag, not by cause;
  its cause is `lift_criterion` of case 204 — compare with any lesson on the Estimate
  recut (cases 193, 211) before clustering.
- The defer 269 of `rule-work-mode` and `rule-subagent-guppi` is the eleventh; both are
  named by the sprint page, so they stay out of the brief's Deferred list (229.4).
- Expected after your run: `rule-prespec` `built` once `estimate-prespec-reconciles` and
  `-catches-bare-wikilinks` are `passed` — both lines are in the 0958 ledger;
  `rule-event-log`, `rule-retro-commit`, `rule-plan-mode`, `rule-materialize` back to
  `built` by their readings; `rule-documentation`, `rule-brief`, `rule-skill-hi`,
  `rule-case-protocol` `draft` until the readings of the next session (`case-form` is
  read and `passed`, so `rule-case-protocol` may stay `built`). `unmigrated` should read
  25. The lint finding `ref` on `estimate-generate-renames` is gone.
- The two `materialize` warnings on the archived yamls of 2026-09-18/1252 and 2253 need
  no line in the brief: the entries are applied and archived, the walk does not name them.

## What actually got done

- Closed: 264.1, 264.2, 265, 265.1–265.4, 266, 267, 268.1, 268.2; 269 deferred.
- Code, commit `ad57dc0` on `migration`: `guppi/prespec.py` — `plan_prose`,
  `known_slugs`, `check_bare_links`, called from `check`, the docstring bullet;
  `guppi/materialize.py` — `DEFER_KEYS`, the `defer` branch of `_lift_item`, the
  docstring; `tests/test_prespec.py` +9 (eight for 264.2, one for the `C1`/`W1` lines of
  268.2); `tests/test_materialize.py` +1 with two new cases in the schema fixture.
  443 green, style clean.
- By hand: `vault/wiki/estimates/estimate-generate-renames.md` History line of 262;
  `vault/wiki/case-schema.md` the story-sections paragraph; `vault/wiki/glossary.md` the
  `/hi`, Frontier row.
- Readings `passed`, all in the 0958 ledger: `estimate-prespec-reconciles`,
  `estimate-prespec-catches-bare-wikilinks`, `estimate-event-log-records`,
  `estimate-plan-mode-verified`, `estimate-materialize-assembles`,
  `estimate-retro-commit-gates`, `estimate-case-protocol-case-form`.
- Lessons: `lesson-spec-change-text-quotes-a-wikilink-bare` (error),
  `lesson-estimate-update-must-carry-its-criterion-whole` (knowledge),
  `lesson-agent-memory-is-not-the-product` (error).
- Not done: the page updates, creates and renders of every Case (yours); `make lint`
  after your run for 265 (`unmigrated: 25`, no `pre-task` in the seven Criteria); the
  readings of `estimate-documentation-completes` (your run of this session),
  `estimate-brief-written` (the brief you write now, read next session),
  `estimate-hi-writes-frontier` (the first `/hi` of the next session); Slice 3b (269).
- Two open ideas for the next Plan Mode, no Case yet: a `replace` inside an Estimate's
  Criterion signed as the pair alone (the lesson on the whole Criterion); a line in
  `rule-claude-md` that the agent writes no local memory.
