# Brief — 2026-09-27, the librarian's run over session 1255 of 2026-09-27

## Where things stand

- Session 1255 ratified Cases 449, 450, 451.1–451.15, 452.1–452.5 and 453, and deferred Cases 454 (`rule-claude-md`), 455 (`rule-one-judgment-one-implementation`) and 456 (`rule-page-generation`). Frontier C5 closed `· work`; C1 and C2 `· sprint`; C10, C12, C13 and C14 `· deferred · kept` (handoff).
- Code, commit e1ea55c: `guppi/prespec.py` (451.2, 451.3), `guppi/backlog.py`, `guppi/cli.py`, `Makefile`, `guppi/sprint.py` (451.4–451.6), `guppi/casecheck.py`, `guppi/ratified.py` (449, 452.1–452.3, 453); tests `test_prespec.py`, `test_backlog.py`, `test_sprint.py`, `test_casecheck.py`, `test_ratified.py`. The session's `make test` gave 811 passed, 2 skipped; `make style` was clean (handoff).
- Readings of the session: 1, `estimate-case-protocol-defers-in-one-reply` `failed` again. One `knowledge` lesson: `harness-senduserfile-renders-a-markdown-file-on-the-phone` (handoff, ledger lines 53–54).
- Not done in the session: the `read` lines of the Estimates the session creates or updates; Frontier Work lines W1–W34 (handoff).
- The walk named `raw/2026-09-26/2300/` (0 new entries, 0 pages written) and `raw/2026-09-27/1255/`.
- Yaml of 1255: 54 entries from the 54 lines of the ledger: 46 `update`, 3 `create`, 3 `defer` (all `exists`), 1 `estimate`, 1 `lesson`. All 54 are `applied`. The librarian added no entry; it marked line 12 `near`.
- Pages (`generate`: 77 pages written or changed; `cleanup`: 3 pages moved):
  - decisions: 26 created (449, 450, 451.1–451.15, 452.1–452.5, 453, 454, 455, 456).
  - rules: 1 created: `rule-backlog` (451.4, child of `rule-documentation`). 17 updated: `rule-case-protocol` (449, 451.1, 451.10, 452.4, 452.5), `rule-case-check` (449, 452.1, 452.2), `rule-skill-hi` (451.1), `rule-prespec` (451.2), `rule-insights-schema` (451.4), `rule-lint` (451.5), `rule-sprint` (451.6), `rule-brief` (451.8), `rule-carry-over` (451.9), `rule-vault-layout` (451.11), `rule-internal-context` (451.12), `rule-documentation` (451.13), `rule-harness` (451.14), `rule-spec-write` (452.3), `rule-case-build` (452.4), `rule-language` (452.5), `rule-spec-reconcile` (453). 3 deferred: `rule-claude-md` (454), `rule-one-judgment-one-implementation` (455), `rule-page-generation` (456). Cascade built → draft: `rule-brief`, `rule-harness`, `rule-insights-schema`, `rule-internal-context`, `rule-skill-hi`.
  - estimates: 2 created, `pending`: `estimate-backlog-renders` (451.4), `estimate-backlog-checks-the-file` (451.5). 20 updated by Cases, all `pending`. 1 updated by a reading: `estimate-case-protocol-defers-in-one-reply`, `failed` → `failed`.
  - lessons: 1 created: `harness-senduserfile-renders-a-markdown-file-on-the-phone` (`new`). 3 archived by the cascade of the actioned Insights and moved by `cleanup`: `lesson-case-build-a-list-in-context`, `lesson-case-show-ref-of-a-ratification-line-retyped`, `lesson-case-show-sub-case-ratification-retyped`.
  - insights: 2 updated, both `actioned`: `insight-case-form-chat-form-read-by-no-script` (449, its proposal for the story sections rejected), `insight-case-show-built-case-retyped-by-hand` (452.4).
  - entities: 1 updated: `entity-glossary` (451.4, the term `backlog.md`).
- Governed files `render` rewrote: `CLAUDE.md`, `.claude/agents/case-guppi.md`, `.claude/agents/librarian-guppi.md`, `.claude/skills/carry/SKILL.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`, `vault/wiki/case-schema.md`, `vault/wiki/insights/schema.yaml`. `guppi sprint` rewrote `vault/wiki/sprint.md` (its `## Backlog` no longer rendered, case 451.6). `guppi backlog` wrote `vault/wiki/backlog.md` for the first time: 19 items, no conserved Spec. `guppi glossary` rewrote `vault/wiki/glossary.md`.
- This brief has no Deferred list: case 451.8; the deferred items stand in `vault/wiki/backlog.md`.

## Readings due

45 Estimates stand `pending` or `failed` after `generate`: 1 `failed`, 44 `pending`. Every rule or entity they read stands `draft`.

- `estimate-case-protocol-defers-in-one-reply` — `failed` — `rule-case-protocol` draft — by hand, the first defer the person asks for after the render (method). Result: the defer reply of session 1255 for Cases 454–456 was right in the short Cases, the LEDGER block and the Stop hook's writing, but a paragraph proposing `/pre-spec` with a question followed the Frontier.
- `estimate-agent-writing-followed` — `rule-agent-writing` draft — `raw/2026-09-27/1255/spec.md` line 110.
- `estimate-backlog-checks-the-file` — `rule-backlog` draft — `raw/2026-09-27/1255/spec.md` line 419.
- `estimate-backlog-renders` — `rule-backlog` draft — `raw/2026-09-27/1255/spec.md` line 373.
- `estimate-brief-written` — `rule-brief` draft — `raw/2026-09-27/1255/spec.md` line 542.
- `estimate-carry-over-writes` — `rule-carry-over` draft — `raw/2026-09-27/1255/spec.md` line 595.
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` draft — `raw/2026-09-27/1255/spec.md` line 895.
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` draft — `raw/2026-09-27/1255/spec.md` line 944.
- `estimate-case-protocol-acknowledging-reply` — `rule-case-protocol` draft — `raw/2026-09-27/1255/spec.md` line 635.
- `estimate-case-protocol-case-form` — `rule-case-protocol` draft — `raw/2026-09-27/1255/spec.md` line 72.
- `estimate-case-protocol-shows-the-built-case` — `rule-case-protocol` draft — `raw/2026-09-27/1255/spec.md` line 1065; `archive/migration/2026-09-26/2300/raw/spec.md` line 209.
- `estimate-documentation-completes` — `rule-documentation` draft — `raw/2026-09-27/1255/spec.md` line 755.
- `estimate-harness-pipeline` — `rule-harness` draft — `raw/2026-09-27/1255/spec.md` line 791.
- `estimate-hi-writes-frontier` — `rule-skill-hi` draft — `raw/2026-09-27/1255/spec.md` line 203.
- `estimate-insights-schema-checked` — `rule-insights-schema` draft — `raw/2026-09-27/1255/spec.md` line 835.
- `estimate-internal-context-loaded` — `rule-internal-context` draft — `raw/2026-09-27/1255/spec.md` line 706.
- `estimate-language-followed` — `rule-language` draft — `raw/2026-09-27/1255/spec.md` line 1117; `archive/migration/2026-09-26/2300/raw/spec.md` line 732.
- `estimate-prespec-binds-a-sprint-line` — `rule-prespec` draft — `raw/2026-09-27/1255/spec.md` line 282.
- `estimate-prespec-checks-the-frontier` — `rule-prespec` draft — `raw/2026-09-27/1255/spec.md` line 249.
- `estimate-spec-reconcile-refuses-an-edit-of-the-plan` — `rule-spec-reconcile` draft — `raw/2026-09-27/1255/spec.md` line 1188; `archive/migration/2026-09-26/2300/raw/spec.md` line 436.
- `estimate-spec-write-copies-the-ratified-case` — `rule-spec-write` draft — `raw/2026-09-27/1255/spec.md` line 995; `archive/migration/2026-09-26/2300/raw/spec.md` line 328.
- `estimate-sprint-moves-a-passed-over-item` — `rule-sprint` draft — `raw/2026-09-27/1255/spec.md` line 496.
- `estimate-sprint-renders-the-backlog` — `rule-sprint` draft — `raw/2026-09-27/1255/spec.md` line 464.
- `estimate-skill-grill-me-asks-in-rounds` — `rule-skill-grill-me` draft — `archive/migration/2026-09-26/2300/raw/spec.md` line 99.
- `estimate-case-build-writes-the-case` — `rule-case-build` draft — `archive/migration/2026-09-26/2300/raw/spec.md` line 161.
- `estimate-materialize-judges-a-fence` — `rule-materialize` draft — `archive/migration/2026-09-26/2300/raw/spec.md` line 269.
- `estimate-spec-write-checks-the-written-case` — `rule-spec-write` draft — `archive/migration/2026-09-26/2300/raw/spec.md` line 507.
- `estimate-spec-write-removes-a-superseded-case` — `rule-spec-write` draft — `archive/migration/2026-09-26/2300/raw/spec.md` line 541.
- `estimate-language-spec-prose-in-english` — `rule-language` draft — `archive/migration/2026-09-26/2300/raw/spec.md` line 596.
- `estimate-event-log-records` — `rule-event-log` draft — `archive/migration/2026-09-26/2300/raw/spec.md` line 651.
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` draft — by hand, the ledger and preview of the first session where a lesson and the Case that closes its cause stand together, and of the first Case that takes up a decision with more than one Case in its `deferred_by` (method).
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` draft — `uv run pytest tests/test_context.py -k limit`; by hand at the first prompt past 400 000 tokens (method).
- `estimate-materialize-assembles` — `rule-materialize` draft — pytest in `tests/test_materialize.py`; the live reading once by hand (method).
- `estimate-materialize-lifts-a-create-by-the-schema` — `rule-materialize` draft — `uv run pytest tests/test_materialize.py` (method).
- `estimate-prespec-reconciles` — `rule-prespec` draft — by hand, the first `/pre-spec` after the render (method).
- `estimate-retro-loads` — `rule-retro` draft — by hand at the first `/retro` (method).
- `estimate-retro-report-holds-each-fact-once` — `rule-retro` draft — by hand at the first `/retro` after the render (method).
- `estimate-session-phases-in-order` — `rule-session` draft — by hand at the close of a session, the day's records in order (method).
- `estimate-spec-capture-appends` — `rule-spec-capture` draft — pytest in `tests/test_spec.py`; by hand, the next approval of a session after the change (method).
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` draft — `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change (method).
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` draft — by hand, the yaml and the brief after the librarian's run on the first marked lesson clustered under an actioned Insight (method).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` draft — by hand, the tree at the close of the sprint (method).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` draft — `make lint` exit 0, or only unread lines on the Estimates of the sprint (method).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` draft — `make test` on the last commit of migration, then `git log` of main after the merge (method).
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` draft — by hand, the listed `ls`, `grep`, `render --check` and `glossary --check` (method).

## Flags

- `near`, this run: line 12 of `raw/2026-09-27/1255/materialize.yaml`, the create of `rule-backlog`, near `rule-github-issues` (both keep deferred items in view at session start; `rule-github-issues` covers bugs tracked outside the vault). The page was created.
- `incomplete`, `failed`, `unparsed`, `merged`: none in the yamls of 2300 and 1255.
- Synthesis: `harness-senduserfile-renders-a-markdown-file-on-the-phone` has no pair among the lessons and the Insights and stays `new`.
- Failed Estimates: 1, listed first under Readings due.
- Contradiction, from lint: `estimates/estimate-claude-md-rendered: method: says by hand while estimate-language-spec-prose-in-english names a test file`; Case 454 deferred it (`rule-claude-md`, in `backlog.md`).
- Deferred by this session and now in `backlog.md`: `rule-one-judgment-one-implementation` (455: `materialize.case_text` and `ratified.quoted_sections` are two copies of one section reader); `rule-page-generation` (456: a `read` box of an Estimate that a delete removed stays unticked in its Spec).
- Defect, this run: the new lesson's slug `harness-senduserfile-renders-a-markdown-file-on-the-phone` is the only one of the 58 live lessons that does not open with `lesson-`; it came so from ledger line 54, and lint names no finding on it.
- Handoff: the store `<plan>.checked.json` of session 1255 holds no `stored` time; ratifying one of its Cases again needs `case-guppi` again first (the Spec hook refuses "no time held").
- Handoff: unmeasured risk — `SubagentStop` may fire twice, and a second store newer than the sending of the file makes the Spec hook refuse.
- Handoff: `make style` fails under PowerShell on `< /dev/null` of the Makefile; it runs under Bash.
- Handoff: the Frontier of session 1255 closes with the old closers (`· sprint`, `· deferred · kept`); the check of 451.2 applies from the next session.
- Handoff: the re-ratified Cases (449, 450, 451.1, 451.2, 451.4, 452.2–452.4) repeat decision lines the ledger holds; the ledger hook did not append them twice; the new lines are L50–L52 (451.14, 451.15).
- Handoff note: from Case 452 on, a built Case is sent as a file by `SendUserFile` with `display: render`; the Cases of this session still had long contexts, built under the old rule; context passed 400 000 tokens before Work Mode and the code went to three subagents.
- Order the handoff asked: `guppi backlog` run after `guppi sprint`; the `replace` pairs of `rule-case-protocol` (449, 451.1, 451.10, 452.4, 452.5) and `rule-case-check` (449, 452.1, 452.2) applied in one run of `generate`, which printed no stderr line.
- MOC candidates: none named by lint.
- Stale defers, from lint: `rule-work-mode` deferred 32 times since case 29; `rule-subagent-guppi` 31 times since case 29; `rule-morph` once since case 239; `rule-orchestration` once since case 424.
- Backlog moves by `generate`: none printed. Milestones dropped: none printed.
- `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary`: no stderr lines. `cleanup` moved 3 lessons to `archive/migration/2026-09-27/1255/lessons/`.
- `archive` (run after the brief): no stderr line. It moved `raw/2026-09-26/2300` to `archive/migration/2026-09-26/2300/raw`; the line numbers of its Spec above point there. It kept `raw/2026-09-27/1255/`, the session of the run.
- `make lint`, after the render: exit 2, 116 findings.
  - `decisions/decision-case-N: schema: missing section ## Context` and `## Problem` on 31 pages (cases 1–28). That is 62 findings.
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`, and `orphan: no other live page names it in its frontmatter`.
  - `rules/rule-morph: deferred: 1 time since case 239`; `rules/rule-orchestration: deferred: 1 time since case 424`; `rules/rule-subagent-guppi: deferred: 31 times since case 29`; `rules/rule-work-mode: deferred: 32 times since case 29`.
  - `estimates/estimate-claude-md-rendered: method: says by hand while estimate-language-spec-prose-in-english names a test file`.
  - `unread: pending` on 44 Estimates and `unread: failed` on 1. These are the 45 Estimates of Readings due.
  - `estimates: unmigrated: 19 pages in the shape before case 193`.
  - No line from `render --check`, `sprint --check`, `backlog --check` or `glossary --check`.

## Next session

Cases:
- `estimate-case-protocol-defers-in-one-reply` failed: text followed the Frontier in the defer reply (reading of session 1255).
- Contradiction from lint: the method of `estimate-claude-md-rendered` says by hand while `estimate-language-spec-prose-in-english` names a test file (deferred by Case 454).
- Defect from the handoff: `make style` fails under PowerShell on `< /dev/null` of the Makefile.
- Defect found in this run: the lesson slug `harness-senduserfile-renders-a-markdown-file-on-the-phone` lacks the `lesson-` prefix the other lessons carry.

Work:
- `estimate-agent-writing-followed`
- `estimate-backlog-checks-the-file`
- `estimate-backlog-renders`
- `estimate-brief-written`
- `estimate-carry-over-writes`
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-case-check-shows-only-the-checked-case`
- `estimate-case-protocol-acknowledging-reply`
- `estimate-case-protocol-case-form`
- `estimate-case-protocol-shows-the-built-case`
- `estimate-documentation-completes`
- `estimate-harness-pipeline`
- `estimate-hi-writes-frontier`
- `estimate-insights-schema-checked`
- `estimate-internal-context-loaded`
- `estimate-language-followed`
- `estimate-prespec-binds-a-sprint-line`
- `estimate-prespec-checks-the-frontier`
- `estimate-spec-reconcile-refuses-an-edit-of-the-plan`
- `estimate-spec-write-copies-the-ratified-case`
- `estimate-sprint-moves-a-passed-over-item`
- `estimate-sprint-renders-the-backlog`
- `estimate-skill-grill-me-asks-in-rounds`
- `estimate-case-build-writes-the-case`
- `estimate-materialize-judges-a-fence`
- `estimate-spec-write-checks-the-written-case`
- `estimate-spec-write-removes-a-superseded-case`
- `estimate-language-spec-prose-in-english`
- `estimate-event-log-records`
- `estimate-case-protocol-ledger-line-form`
- `estimate-context-size-warns-past-the-limit`
- `estimate-materialize-assembles`
- `estimate-materialize-lifts-a-create-by-the-schema`
- `estimate-prespec-reconciles`
- `estimate-retro-loads`
- `estimate-retro-report-holds-each-fact-once`
- `estimate-session-phases-in-order`
- `estimate-spec-capture-appends`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-synthesis-keeps-actioned-by-the-mark`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-sprint-migration-rule-class-files-dissolved`
- The unticked boxes of the Specs are the `read` lines of the readings above: `raw/2026-09-27/1255/spec.md` lines 72, 110, 203, 249, 282, 373, 419, 464, 496, 542, 595, 635, 706, 755, 791, 835, 895, 944, 995, 1065, 1117, 1188; `archive/migration/2026-09-26/2300/raw/spec.md` lines 99, 161, 209, 269, 328, 436, 507, 541, 596, 651, 732.
- Frontier Work lines W1–W34 of session 1255 (handoff: the readings and boxes of the previous brief).
- Check at the first live Case whether `SubagentStop` fires twice and a second store makes the Spec hook refuse (handoff).
- Ledger lines not applied: none; all 54 lines of `raw/2026-09-27/1255/ledger.md` have an entry, all applied.

## Readings at the close

- `make test`: 811 passed, 2 skipped.
- `make lint`: exit 2, 116 findings (listed under Flags).
- Pages in `vault/wiki/`: decisions 659, estimates 140, rules 68, lessons 58, insights 25, entities 4.
