# Handoff — 2026-09-18, session 1957: the sprint page names its deferred targets; the /hi Insight rejected; Slice 3b deferred

## Notes from memory

- The person opened with F5 (two readings), then F2. My first Case 245 proposed to action
  `insight-workflow-code-live-before-the-page-it-reads` now; the person stopped it: the
  Insight "should have gone into the milestone of Slice 3b". The Case was rebuilt as an
  `update` of `entity-sprint-migration` — the Insight named in the text of the
  `rule-work-mode` item, not as a line of its own (an Insight `actioned` is not in `DONE`
  of `guppi sprint`, so its own line would never tick). The Insight stays `open`,
  `deferred_by: decision-case-238`; the defer of 238 still carries no `purpose` — the
  Flags entry will repeat; it closes with Slice 3b.
- F3: the person said "we already discussed this"; checked — no Case ever touched the
  Insight, session 1252 closed it with the lesson. Case 246 rejects: `actioned`,
  `addressed_by: [[decision-case-246]]`, `rule-skill-hi` unchanged. The cascade archives
  both `/hi` lessons (1119 classifier, 1252 login). The one alternative weighed: one
  sentence in the Render, rejected for the cost — a recut of `estimate-hi-no-read-calls`
  (old shape) and a reading only a live lapsed login can take.
- F4 (the person's doubt on 240.2) and F7 (the "contradiction" of the two permissions
  lessons) closed as `work`: nothing to decide. F7: the lessons complement — the agent
  writes the frontier in Plan Mode, the client asks, the person approves; 237 holds the
  promise. The one wrong shade is in the 1651 lesson's root cause ("the allow list …
  for exactly this", as if it made the write silent); a lesson is a fact of the hook, not
  a page under `update`. Please do not raise the contradiction flag again unless a third
  lesson lands.
- F6: the person asked for the two rules in Slice 5, not Slice 4 where
  `estimate-sprint-migration-leftovers-gone` (their reader) sits. Case 247 wrote them on
  the `-merges` item as "decided at the merge"; pre-task (`ask-guppi`) found the
  Criterion of `-merges` holds no such promise. Case 249 supersedes 247 with the same
  place and a text that names `-leftovers-gone` as the reading. The place is the person's
  choice; the wording is mine.
- Case 248 defers Slice 3b with a `purpose` per target; no `supersedes` on the earlier
  defers (183, 206, 218, 231, 242 accumulate in `deferred_by`, as before).
- This session in Plan Mode: the Write of `frontier.md`, the Edits of it and of the 1252
  Spec (two `read` lines ticked) went through; I cannot see whether the client prompted.

## Direct instructions to the librarian

- Two `replace` items on `entity-sprint-migration` in one yaml: 245 (line of
  `rule-work-mode`, Slice 3b) and 249 (line of `estimate-sprint-migration-merges`,
  Slice 5). 247 targets the same line as 249 and is superseded by 249 — check that
  `materialize` marks 247's entry `superseded` and `generate` applies 249's text, not
  247's. The two task lines of 247 in the Spec stay `[ ]` by design.
- `guppi sprint` after generate: Slice 3b's `rule-work-mode` line now carries a second
  wikilink in its text; Slice 5 stays collapsed (one line, four names) — the new text of
  the `-merges` item is not visible there until Slice 5 is current. Confirm the render
  and `sprint --check` are green.
- 246: the cascade should archive `lesson-hi-substitution-refused-when-the-permission-classifier-is-unavailable`
  and `lesson-hi-substitution-fails-when-the-login-has-lapsed` (`clustered` children of
  an `actioned` Insight, case 104.2); the Insight stays live with its `pattern`.
- The new lesson `lesson-defer-to-a-milestone-leaves-the-sprint-page-silent` (error;
  tags `sprint`, `workflow`, `session`) may share a cause with nothing yet; the nearest
  Insight is `insight-workflow-code-live-before-the-page-it-reads`, which is not it.
  Possible near page: none known.
- Readings taken from the ledger: `estimate-render-harness-ticks-the-spec` and
  `estimate-sprint-renders-the-backlog`, both `passed` (lines 1–2). With them
  `rule-render-harness` and `rule-sprint` should cascade `draft` → `built` if no other
  Estimate of theirs is `pending`.
- Brief: `rule-work-mode`, `rule-subagent-guppi` (248), the Insight of 238, and
  `rule-git-context` / `rule-github-issues` are all named by the sprint page after this
  run — Deferred should hold none of them (229.4). Please state in Readings due the path
  of a Spec that lives in the archive (`archive/migration/<date>/<HHMM>/raw/spec.md`), not
  a bare line number: this session looked for the 1119 Spec under `raw/`.
- Handoff flags, each a Case of the next Plan Mode: Slice 3b first (248), with the
  sentence of the Insight into `rule-work-mode`; then nothing else is open from this
  session.

## What actually got done

- Cases: 245 (`update` `entity-sprint-migration`, Slice 3b item names the Insight), 246
  (`update` Insight, rejected), 247 (superseded), 248 (`defer` ×2), 249 (`update`
  `entity-sprint-migration`, Slice 5 item names the two rules and their reading).
- Readings: 2 `passed` (`estimate-render-harness-ticks-the-spec`,
  `estimate-sprint-renders-the-backlog`); the two `read` lines of
  `raw/2026-09-18/1252/spec.md` ticked.
- Frontier: 7 items — F5, F4, F7 `work`; F2, F3, F6 by Case; F1 deferred (248).
- Lesson: 1 (`lesson-defer-to-a-milestone-leaves-the-sprint-page-silent`).
- Code: none. Tests 425 green, `make style` clean. Commit `e4f0351` on `migration`:
  the session folder and the 1252 Spec ticks.
- Not done: every page change of the Spec (this run); Slice 3b (defer 248);
  `estimate-carry-over-writes` (a live `/carry`, none yet); the three
  `estimate-sprint-migration-*` readings (the close); `estimate-hi-no-read-calls` stays
  in the old shape (unmigrated, untouched by choice).
