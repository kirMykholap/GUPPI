# Brief — 2026-09-28, the librarian's run over session 1318 of 2026-09-28

## Where things stand

- Session 1318 ratified 476.1, 476.2, 476.3, 476.4, 477.1, 477.2, 477.3, 477.4, 478.1, 478.2, 479.1, 479.2, 479.3, 479.4, 479.5 and 480 (a short defer); Case 481 is a short defer on ledger line L40 (handoff).
- Code, commit 0af5b01: `guppi/config.py` and `tests/test_config.py` new; `guppi/render.py`, `guppi/ratified.py`, `guppi/prespec.py`, `guppi/spec.py`, their tests and `vault/wiki/rules/rule-render-harness.md` changed. The session's `make test` gave 876 passed, 2 skipped; `make style` clean (handoff).
- Readings of the session, L35–L39: `estimate-prespec-checks-the-form-of-an-item`, `estimate-prespec-requires-a-backlog-item-decided-on-its-page`, `estimate-skill-grill-me-asks-in-rounds` and `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` `passed`; `estimate-retro-report-holds-each-fact-once` `failed`. One lesson, L41: `lesson-plan-mode-agent-and-sendmessage-pass-the-auto-mode-classifier` (handoff).
- Not done in the session (handoff): the `guppi.toml: missing` finding of pre-spec (a note, expected until this run's render); the language finding counts Latin slugs in code spans (defer, Case 481); the reading of `estimate-context-size-warns-past-the-limit` not taken; the hand edit of `rule-render-harness` in Work Mode (a note, intended).
- The walk named `raw/2026-09-28/0000/` (extended with 0 entries; `generate` 0 pages) and `raw/2026-09-28/1318/` (written with 41 entries from the 41 lines of its ledger).
- Yaml of 1318: 41 entries: 26 `update`, 7 `create` (lines 1, 15 rules; lines 2, 14, 16, 26, 31 Estimates), 5 `estimate`, 2 `defer` (lines 34, 40, each on a new slug, `exists: false`), 1 `lesson` (line 41). The librarian added 1 `near` (line 1) and 2 entries by synthesis. All 43 entries `applied`. No `failed`, no `incomplete`, no `merged`, `unparsed: []`.
- Pages (`generate`: 78 pages written or changed; `cleanup`: 22 pages moved):
  - decisions: 17 created (476.1–476.4, 477.1–477.4, 478.1, 478.2, 479.1–479.5, 480, 481). 20 archived, superseded by 479.2: 183, 206, 218, 231, 242, 248, 252, 254, 260, 263, 269, 276, 281, 285, 289, 293, 303, 307, 322, 447.
  - rules: 4 created: `rule-guppi-config` (476.1), `rule-skill-wait-what` (477.2), and the defer placeholders `rule-case-build-checks-its-sub-cases` (480) and `rule-prespec-script-skips-code-spans` (481). 11 updated by Cases: `rule-render-harness`, `rule-harness` (476.1); `rule-case-protocol` (476.2, 477.3); `rule-case-build` (476.2, 477.1, 477.3); `rule-ask` (476.2); `rule-prespec` (476.3); `rule-language` (476.4); `rule-spec-capture` (479.1); `rule-work-mode` (479.2, every `deferred_by` cleared); `rule-retro` (479.3, 479.4); `rule-permissions` (479.5). `rule-plan-mode` got the child `rule-skill-wait-what`. Cascade draft → built: `rule-skill-grill-me`.
  - estimates: 5 created, `pending`: `estimate-guppi-config-fills-the-languages`, `estimate-case-build-writes-a-plain-round`, `estimate-skill-wait-what-re-pitches`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-retro-red-in-the-baseline-is-not-charged`. 8 updated by Cases, all `pending`. 5 updated by readings: 4 `passed`, 1 `failed`.
  - entities: `entity-sprint-migration` updated (478.2, 479.2).
  - insights: `insight-session-reply-language-follows-the-english-text-read` → `actioned` (`addressed_by` 476.4). `insight-hi-skill-substitution-checked-by-a-model-call` → `open` by synthesis, severity 1, 4 children.
  - lessons: 1 created, `lesson-plan-mode-agent-and-sendmessage-pass-the-auto-mode-classifier`, `clustered` by synthesis. 2 archived because their Insight went `actioned`: `lesson-chat-language-follows-the-last-english-file-read`, `lesson-retro-answered-in-the-skills-language`.
- Governed files `render` wrote: `CLAUDE.md`, `guppi.toml` (new), `.claude/settings.json`, `.claude/agents/ask-guppi.md`, `.claude/agents/case-guppi.md`, `.claude/skills/pre-spec/SKILL.md`, `.claude/skills/retro/SKILL.md`, `.claude/skills/wait-what/` (new), `.claude/skills/work/` (new), `vault/wiki/case-schema.md`. `guppi sprint` rewrote `vault/wiki/sprint.md`: the file-route item reworded (478.1); Slice 5 got a fifth item, the close of a sprint, not yet decided (478.2). `guppi backlog` rewrote `vault/wiki/backlog.md`: 18 items, was 17; added `rule-case-build-checks-its-sub-cases` and `rule-prespec-script-skips-code-spans`; removed `insight-session-reply-language-follows-the-english-text-read`; `insight-hi-skill-substitution-checked-by-a-model-call` now severity 1; `rule-work-mode` stands from the sprint page's `## Backlog`. `guppi glossary` left `vault/wiki/glossary.md` unchanged.
- `generate` ticked 49 lines of `raw/2026-09-28/1318/spec.md` and 3 of `raw/2026-09-28/0000/spec.md`.

## Readings due

33 Estimates stand `pending` or `failed` after `generate`: 1 `failed`, 32 `pending`. Every rule or entity they read stands `draft`.

- `estimate-retro-report-holds-each-fact-once` — `failed` — `rule-retro` draft — by hand at the first /retro after the render (method). Result: the Retro report of 1318 named Case 481 in two parts and wrote the end of each frontier item twice.
- `estimate-guppi-config-fills-the-languages` — `rule-guppi-config` draft — `raw/2026-09-28/1318/spec.md` line 105.
- `estimate-language-spec-prose-in-english` — `rule-language` draft — `raw/2026-09-28/1318/spec.md` line 216.
- `estimate-language-followed` — `rule-language` draft — `raw/2026-09-28/1318/spec.md` line 277.
- `estimate-case-build-writes-a-plain-round` — `rule-case-build` draft — `raw/2026-09-28/1318/spec.md` line 337.
- `estimate-skill-wait-what-re-pitches` — `rule-skill-wait-what` draft — `raw/2026-09-28/1318/spec.md` line 411.
- `estimate-case-protocol-shows-the-built-case` — `rule-case-protocol` draft — `raw/2026-09-28/1318/spec.md` line 467.
- `estimate-agent-writing-followed` — `rule-agent-writing` draft — `raw/2026-09-28/1318/spec.md` line 497.
- `estimate-sprint-migration-file-route-gone` — `entity-sprint-migration` draft — `raw/2026-09-28/1318/spec.md` line 551.
- `estimate-spec-capture-offers-the-fork` — `rule-spec-capture` draft — `raw/2026-09-28/1318/spec.md` line 650.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` draft — `raw/2026-09-28/1318/spec.md` line 743.
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` draft — `raw/2026-09-28/1318/spec.md` line 788 (and `raw/2026-09-28/0000/spec.md` line 303).
- `estimate-retro-red-in-the-baseline-is-not-charged` — `rule-retro` draft — `raw/2026-09-28/1318/spec.md` line 838.
- `estimate-permissions` — `rule-permissions` draft — `raw/2026-09-28/1318/spec.md` line 886.
- `estimate-case-check-notes-a-criterion-line-not-carried` — `rule-case-check` draft — `raw/2026-09-28/0000/spec.md` line 123.
- `estimate-case-check-notes-a-then-line-shared-by-siblings` — `rule-case-check` draft — `raw/2026-09-28/0000/spec.md` line 181.
- `estimate-documentation-completes` — `rule-documentation` draft — `raw/2026-09-28/0000/spec.md` line 468.
- `estimate-synthesis-clusters` — `rule-synthesis` draft — `raw/2026-09-28/0000/spec.md` line 504.
- `estimate-case-build-writes-the-case` — `rule-case-build` draft — by hand, live dispatches in a session after the render (method).
- `estimate-carry-over-writes` — `rule-carry-over` draft — `uv run guppi render --check`; by hand, the first /carry after the fork of ExitPlanMode (method).
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` draft — `uv run pytest tests/test_casecheck.py -k subagent`, then by hand the first answer the hook sends back (method).
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` draft — `uv run pytest tests/test_casecheck.py -k stop`, then by hand the first reply the hook refuses (method).
- `estimate-case-protocol-defers-in-one-reply` — `rule-case-protocol` draft — by hand, the first defer the person asks for after the render (method).
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` draft — by hand, the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together (method).
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` draft — `uv run pytest tests/test_context.py -k limit`; by hand at the first prompt past 400 000 tokens (method).
- `estimate-event-log-records` — `rule-event-log` draft — pytest in `tests/test_event.py` and `tests/test_gate.py`; readings by hand (method).
- `estimate-generate-writes-the-decision-page` — `rule-page-generation` draft — `pytest tests/test_generate.py`, the live reading in the librarian's run (method).
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` draft — by hand at the first /handoff after the render (method).
- `estimate-session-phases-in-order` — `rule-session` draft — by hand at the close of a session, the day's records in order (method).
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` draft — `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change (method).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` draft — by hand, the tree at the close of the sprint (method).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` draft — `make lint` exit 0, or only unread lines on the Estimates of the sprint (method).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` draft — `make test` on the last commit of migration, then `git log` of main after the merge (method).

## Flags

- `near`: line 1, `rule-guppi-config` near `rule-morph`. Both hold project settings as data set at install; the page of 476.1 leaves the install questions and the category set to `rule-morph`.
- `incomplete`, `failed`, `merged`, `unparsed`: none in the yamls of 0000 and 1318.
- `exists: false`: lines 34 and 40, the defers 480 and 481 on new slugs; placeholder pages written.
- Synthesis: `lesson-plan-mode-agent-and-sendmessage-pass-the-auto-mode-classifier` shares its cause with `insight-hi-skill-substitution-checked-by-a-model-call` (its child `lesson-hi-substitution-gets-no-verdict-from-the-server-side-classifier`): a call Claude Code checks by the server-side classifier is refused when the check gives no verdict. The Insight was `actioned` (`addressed_by` 439) and is `open` again, with the lesson as its fourth child; the lesson is `clustered`. The field `addressed_by` 439 stands on the reopened Insight.
- Failed Estimates: 1, listed first under Readings due.
- `guppi.toml`: `render` wrote it at the repository root. The librarian's commit takes only `vault`, `CLAUDE.md` and `.claude`, so `guppi.toml` stays untracked after this run.
- Handoff: the 19 defers of `rule-subagent-guppi` (cases 183–322) point at Decisions that 479.2 superseded and `cleanup` archived in this run. The person chose to leave them for the Case that takes that page up.
- Handoff: `guppi prespec --check` printed `guppi.toml: missing` on this session's plan; the file exists after this run's render. Its reading is the first pre-spec after this run.
- Handoff: `estimate-context-size-warns-past-the-limit` — the test gave 3 passed and the `UserPromptSubmit` line came at 406 944 tokens as the Criterion says; the agent cannot see the `Stop` line and passed the note only in the Retro reply. The reading is not taken.
- Handoff: Work Mode ran without `/work`; the baseline was taken by hand (`make test` 856 passed, 2 skipped; `make lint` exit 2, 98 findings, the same 98 after the work).
- Handoff: a bug found in Work Mode, the language finding read the whole heading, `Case` included; fixed in `ratified.untranslated` in the same session.
- Handoff: git warned that `tests/test_spec.py` holds CRLF in the working copy and gets LF at the next touch.
- Handoff: on C5 the person chose to keep a done-condition Estimate live until the close of the sprint; Slice 5 holds the item, not yet decided (478.2).
- Handoff: the `update` of 476.1 on `rule-render-harness` carries only `set` and `change`; the removed `## How it works` section is intended.
- Contradictions: none found in this run.
- MOC candidates: none named by lint.
- Stale defers, from lint: `rule-subagent-guppi` 31 times since case 29; `rule-morph` once since case 239; `rule-orchestration` once since case 424; `rule-case-build-checks-its-sub-cases` once since case 480; `rule-prespec-script-skips-code-spans` once since case 481. `rule-work-mode` is no longer named.
- Backlog moves by `generate`: none printed. Milestones dropped: none printed.
- `materialize`, `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary`: no stderr lines.
- `archive` (run after the brief): exit 0, no output. It moved no unit: `raw/2026-09-28/0000/` and `raw/2026-09-28/1318/` are dated today, and `archive` skips a unit of today's date.
- `make lint`, after the render: exit 2, 104 findings.
  - `decisions/decision-case-N: schema: missing section ## Context` and `## Problem` on 31 pages (cases 1–28). That is 62 findings.
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`, and `orphan: no other live page names it in its frontmatter`.
  - 5 `deferred` findings, the stale defers above.
  - `unread: pending` on 32 Estimates and `unread: failed` on 1. These are the 33 Estimates of Readings due.
  - `estimates: unmigrated: 18 pages in the shape before case 193`.

## Next session

Cases:
- `estimate-retro-report-holds-each-fact-once` `failed` (L39 of `raw/2026-09-28/1318/ledger.md`): the Retro report writes a fact twice.
- `guppi.toml` is written by `render` at the repository root, and the librarian's commit takes only `vault`, `CLAUDE.md` and `.claude`; the file is untracked after this run (found in this run).

Work:
- The 32 `pending` readings of Readings due, by slug; the unticked boxes of `raw/2026-09-28/1318/spec.md` (13) and `raw/2026-09-28/0000/spec.md` (5) are `read` lines of those Estimates.
- The first `guppi prespec --check` after this run, for the `guppi.toml: missing` finding (handoff).
- Ledger lines this run did not apply: none; the 41 lines of `raw/2026-09-28/1318/ledger.md` each have an entry.

## Readings at the close

- `make test`: 876 passed, 2 skipped.
- `make lint`: exit 2, 104 findings.
- Pages: decisions 681, estimates 154, rules 72, lessons 57, insights 26, entities 4.
