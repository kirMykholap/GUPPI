# Brief — 2026-09-28, the librarian's run over session 2000 of 2026-09-28

## Where things stand

- Session 2000 ratified 482, 483, 484.1–484.7 and 485.1–485.6 (handoff).
- Commit cb12283 took `guppi.toml`; commit 9ed5a9f is the Retro commit of the session folder. No code file or test changed. The session's `make test` gave 876 passed, 2 skipped; `make style` clean; `make lint` exit 2, 104 findings, nothing added under Expected red (handoff).
- Readings of the session: L18–L24 `passed`, L25–L26 `failed`. One lesson, L27: `lesson-wait-what-invents-an-example` (handoff).
- Not done in the session (handoff): the `/wait-what` re-pitch on a made-up example (lesson L27); rounds of `case-guppi` whose options give no before and after (the failed `estimate-case-build-writes-a-plain-round`, to the next Frontier); 23 of the 32 pending readings of the last brief, their events not come; two stale `.pyc` files under `guppi/__pycache__/`.
- The walk named `raw/2026-09-28/0000/` and `raw/2026-09-28/1318/` (each extended with 0 entries; `generate` 0 pages each) and `raw/2026-09-28/2000/` (written with 27 entries from the 27 lines of its ledger).
- Yaml of 2000: 27 entries: 17 `update` (Cases 482–485), 9 `estimate` (7 `passed`, 2 `failed`), 1 `lesson`. No `create`. All 27 `applied`. No `failed`, `incomplete`, `exists`, `near`, `merged` or `librarian` mark; `unparsed: []`.
- Pages (`generate`: 50 pages written or changed, `log.md` included; `cleanup`: 0 pages moved):
  - decisions: 15 created (482, 483, 484.1–484.7, 485.1–485.6).
  - rules: 2 updated by Cases: `rule-close` (482), `rule-retro` (483). Cascade built → draft: `rule-close`, `rule-git-context`, `rule-github-issues`, `rule-ledger-tail`, `rule-prespec`, `rule-session-start`, `rule-skill-hi`. Cascade draft → built: `rule-guppi-config`, `rule-language`, `rule-spec-capture`.
  - estimates: 13 updated by Cases, all `pending`: `estimate-close-commits`, `estimate-retro-report-holds-each-fact-once`, the five `estimate-prespec-catches-*` pages and `estimate-prespec-simulates-the-pairs` (484.1–484.6), `estimate-session-start-context`, `estimate-hi-no-read-calls`, `estimate-git-context-current`, `estimate-github-issues-listed`, `estimate-ledger-tail`. 9 updated by readings: 7 `passed`, 2 `failed`.
  - entities: `entity-sprint-migration` updated (484.7, 485.6), two History lines.
  - lessons: 1 created, `lesson-wait-what-invents-an-example`, `new`.
  - insights: none created or updated.
- Governed files `render` wrote: `.claude/agents/librarian-guppi.md` (`rule-close`) and `.claude/skills/retro/SKILL.md` (`rule-retro`). `guppi sprint` rewrote `vault/wiki/sprint.md`: the file-route item of the sprint is ticked, `passed`. `guppi backlog` and `guppi glossary` left `vault/wiki/backlog.md` and `vault/wiki/glossary.md` unchanged.
- `generate` ticked 19 lines of `raw/2026-09-28/2000/spec.md`, 8 of `raw/2026-09-28/1318/spec.md` and 1 of `raw/2026-09-28/0000/spec.md`.

## Readings due

38 Estimates stand `pending` or `failed` after `generate`: 2 `failed`, 36 `pending`. Every rule or entity they read stands `draft`.

- `estimate-case-build-writes-a-plain-round` — `failed` — `rule-case-build` draft — by hand, one round of case-guppi read in the chat against the four parts of the Criterion (method). Result: Case 482 Q2 and Q4 give no before, Case 483 Q3 and Q4 give only "After:".
- `estimate-skill-wait-what-re-pitches` — `failed` — `rule-skill-wait-what` draft — `uv run guppi render --check`; by hand, one run of the skill read in the chat (method). Result: the re-pitch of round 2 Q1 on Case 485 showed a made-up example and did not ask the case-guppi of the Case for a real line.
- `estimate-close-commits` — `rule-close` draft — `raw/2026-09-28/2000/spec.md` line 58.
- `estimate-retro-report-holds-each-fact-once` — `rule-retro` draft — `raw/2026-09-28/2000/spec.md` line 129.
- `estimate-prespec-catches-a-command-line-off-form` — `rule-prespec` draft — `raw/2026-09-28/2000/spec.md` line 184.
- `estimate-prespec-catches-a-superseded-case` — `rule-prespec` draft — `raw/2026-09-28/2000/spec.md` line 215.
- `estimate-prespec-catches-a-method-without-a-form` — `rule-prespec` draft — `raw/2026-09-28/2000/spec.md` line 247.
- `estimate-prespec-catches-an-unwrapped-render` — `rule-prespec` draft — `raw/2026-09-28/2000/spec.md` line 280.
- `estimate-prespec-catches-bare-wikilinks` — `rule-prespec` draft — `raw/2026-09-28/2000/spec.md` line 312.
- `estimate-prespec-simulates-the-pairs` — `rule-prespec` draft — `raw/2026-09-28/2000/spec.md` line 342.
- `estimate-session-start-context` — `rule-session-start` draft — `raw/2026-09-28/2000/spec.md` line 413.
- `estimate-hi-no-read-calls` — `rule-skill-hi` draft — `raw/2026-09-28/2000/spec.md` line 446.
- `estimate-git-context-current` — `rule-git-context` draft — `raw/2026-09-28/2000/spec.md` line 478.
- `estimate-github-issues-listed` — `rule-github-issues` draft — `raw/2026-09-28/2000/spec.md` line 507.
- `estimate-ledger-tail` — `rule-ledger-tail` draft — `raw/2026-09-28/2000/spec.md` line 545.
- `estimate-agent-writing-followed` — `rule-agent-writing` draft — by hand in a later session, the person's messages of one session read for a complaint about the agent's text (method).
- `estimate-carry-over-writes` — `rule-carry-over` draft — `uv run guppi render --check`; by hand, the first /carry after the fork of ExitPlanMode (method).
- `estimate-case-build-writes-the-case` — `rule-case-build` draft — by hand, live dispatches in a session after the render (method).
- `estimate-case-check-notes-a-then-line-shared-by-siblings` — `rule-case-check` draft — `uv run pytest tests/test_casecheck.py tests/test_prespec.py -k sibling`, then by hand the first sibling note (method).
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` draft — `uv run pytest tests/test_casecheck.py -k subagent`, then by hand the first answer the hook sends back (method).
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` draft — `uv run pytest tests/test_casecheck.py -k stop`, then by hand the first reply the hook refuses (method).
- `estimate-case-protocol-defers-in-one-reply` — `rule-case-protocol` draft — by hand, the first defer the person asks for after the render (method).
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` draft — by hand, the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together (method).
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` draft — `uv run pytest tests/test_context.py -k limit`; by hand at the first prompt past 400 000 tokens (method).
- `estimate-documentation-completes` — `rule-documentation` draft — `make test-documentation`; the live reading by hand (method).
- `estimate-event-log-records` — `rule-event-log` draft — pytest in `tests/test_event.py` and `tests/test_gate.py`; readings by hand, one /hi outside plan mode (method).
- `estimate-generate-writes-the-decision-page` — `rule-page-generation` draft — `pytest tests/test_generate.py`; the live reading in the librarian's run (method).
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` draft — by hand at the first /handoff after the render (method).
- `estimate-permissions` — `rule-permissions` draft — the allow list of `.claude/settings.json` and the JSON case of `tests/test_render.py`; the person's word on the prompt at a Write of `work.md` (method).
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` draft — by hand at the first /retro whose `work.md` names a check under Expected red (method).
- `estimate-retro-red-in-the-baseline-is-not-charged` — `rule-retro` draft — by hand at the first /retro whose `work.md` Baseline holds a failing test or a lint finding (method).
- `estimate-session-phases-in-order` — `rule-session` draft — by hand at the close of a session, the day's records in order (method).
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` draft — `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change (method).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` draft — by hand, the tree at the close of the sprint (method).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` draft — `make lint` exit 0, or only unread lines on the Estimates of the sprint (method).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` draft — `make test` on the last commit of migration, then `git log` of main after the merge (method).
- `estimate-synthesis-clusters` — `rule-synthesis` draft — by hand, the yaml and the report of a live librarian run whose yaml holds at least two lesson entries (method).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` draft — `uv run guppi render --check`; by hand, the first /work called at the fork and the first /work typed (method).

## Flags

- `incomplete`, `failed`, `near`, `merged`, `unparsed`: none in the yaml of 2000. The yaml of 0000 still carries `incomplete` on lines 4, 22 and 23, entries marked `superseded_by` and never applied; no script changed them in this run.
- Index check: no `create` entry in the yaml of 2000; no index line compared.
- Synthesis: `lesson-wait-what-invents-an-example` compared with 57 index lines of `lessons/` and 26 of `insights/`; no shared root cause found. It stays `new`.
- Failed Estimates: 2, listed first under Readings due.
- Defect, found in this run: the third `replace` pair of 483 on `rule-retro` ends its `new` with the closing fence of the skeleton, and the sentence after the anchor joins that line: "``` When the person approves, commit …" (`vault/wiki/rules/rule-retro.md` line 73, `.claude/skills/retro/SKILL.md` line 47). A closing fence with text after it does not close the block in Markdown, so the rest of the skill reads as code. The skeleton stands inside the Render markers of `rule-retro` (lines 26 and 74).
- Handoff instruction on `entity-sprint-migration`: 484.7 and 485.6 wrote two History lines and no other change; the Slice 3g note stays unticked.
- Handoff instruction on the 13 Estimates: all 13 stand `pending`; their 13 `read` lines stand unticked in `raw/2026-09-28/2000/spec.md`.
- Handoff instruction on Case 482: after this run's render `git ls-files` lists `guppi.toml`, and `git status` shows no untracked file outside `vault/`.
- Handoff: on 485 the person still sees nuance on Estimates that promise a one-time act; it may come back at Slice 5 (478.2).
- Handoff: on round 2 of 485 the person picked (b) against the recommendation; no line of an old Criterion that the code no longer honours was found in the group.
- Handoff: 482, 484 and 485 were ratified a second time after pre-spec; the ledger holds each decision line once.
- Handoff: Slice 3g stays open — 37 `Given:` pages in about 24 groups and 12 old-layout pages in three groups.
- Handoff: two stale `.pyc` files, `guppi/__pycache__/materialize.cpython-314.pyc` and `pretask.cpython-312.pyc`, hold the file-route strings; untracked.
- Contradictions: none found in this run beyond the defect above.
- MOC candidates: none named by lint.
- Stale defers, from lint: `rule-subagent-guppi` 31 times since case 29; `rule-morph` once since case 239; `rule-orchestration` once since case 424; `rule-case-build-checks-its-sub-cases` once since case 480; `rule-prespec-script-skips-code-spans` once since case 481.
- Backlog moves by `generate`: none printed. Milestones dropped: none printed.
- `materialize`, `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary`: no stderr lines.
- `archive` (run after the brief): exit 0, no output. It moved no unit: `raw/2026-09-28/0000/`, `1318/` and `2000/` are dated today, and `archive` skips a unit of today's date.
- `make lint`, after the render: exit 2, 109 findings (104 at the handoff; the `unread` lines went from 33 to 38).
  - `decisions/decision-case-N: schema: missing section ## Context` and `## Problem` on 31 pages (cases 1–28). That is 62 findings.
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`, and `orphan: no other live page names it in its frontmatter`.
  - 5 `deferred` findings, the stale defers above.
  - `unread: pending` on 36 Estimates and `unread: failed` on 2. These are the 38 Estimates of Readings due.
  - `estimates: unmigrated: 12 pages in the shape before case 193`.

## Next session

Cases:
- `estimate-case-build-writes-a-plain-round` `failed` (L25 of `raw/2026-09-28/2000/ledger.md`): rounds of case-guppi whose options give no before and after.
- `estimate-skill-wait-what-re-pitches` `failed` (L26 of `raw/2026-09-28/2000/ledger.md`): the re-pitch showed a made-up example; lesson L27.
- The closing fence of the Retro skeleton carries the next sentence on its line, in `rule-retro` and `.claude/skills/retro/SKILL.md` (found in this run).

Work:
- The 36 `pending` readings of Readings due, by slug.
- The unticked boxes of `raw/2026-09-28/2000/spec.md` (13), `raw/2026-09-28/1318/spec.md` (5) and `raw/2026-09-28/0000/spec.md` (4) are `read` lines of those Estimates.
- The two stale `.pyc` files under `guppi/__pycache__/` (handoff).
- Ledger lines this run did not apply: none; the 27 lines of `raw/2026-09-28/2000/ledger.md` each have an entry.

## Readings at the close

- `make test`: 876 passed, 2 skipped.
- `make lint`: exit 2, 109 findings.
- Pages: decisions 696, estimates 154, rules 72, lessons 58, insights 26, entities 4.
