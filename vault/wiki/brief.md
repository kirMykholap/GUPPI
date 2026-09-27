# Brief — 2026-09-27, the librarian's run over session 1819 of 2026-09-27

## Where things stand

- Session 1819 ratified Cases 457, 458, 459, 460.1, 460.3, 460.4, 460.5, 461, 462 and 463; 460.2 was superseded by 460.5 in the same session. Frontier C3–C9 closed `· case N`; C1 and C2 (Slice 3g) `[-] · sprint · defer` (handoff).
- Code, commit 49acdff: `Makefile` (457), `guppi/lint.py` (459, 460.3), `guppi/generate.py` (460.1 docstring, 463), `guppi/ledger.py` (460.5), `guppi/materialize.py`, `guppi/ratified.py`, `guppi/casecheck.py` (462); tests in `test_lint`, `test_generate`, `test_ledger`, `test_materialize`, `test_ratified`. The session's `make test` gave 827 passed, 2 skipped; `make style` clean; `make help`, `style`, `test` exit 0 from PowerShell and from Git Bash (handoff).
- Readings of the session: 16 `passed`, 1 `failed` (`estimate-retro-report-holds-each-fact-once`). Four lessons (ledger lines 1, 36–38) (handoff).
- Not done in the session: the `read` lines of the Spec; the Frontier Work readings W1, W4–W7, W9–W12, W16, W21, W23–W25, W29–W32, W34–W37, W39–W44; every Estimate the session creates or updates waits for a later session (handoff).
- The walk named `raw/2026-09-27/1255/` (extended with 0 entries; `generate` 0 pages) and `raw/2026-09-27/1819/` (written with 39 entries from the 39 lines of its ledger). `materialize` added `superseded_by` marks to the 1255 entries of Cases 454 and 455 (by 459 and 462); the entry of 456 was already applied.
- Yaml of 1819: 39 entries: 15 `update` (lines 3–7, 9–16, 20, 22), 3 `create` (lines 2, 8, 21), 17 `estimate`, 4 `lesson`. Lines 8–10 carry `superseded_by: 460.5` and were not applied; the other 36 entries are `applied`. The librarian added 5 `update` entries (`librarian: synthesis`), all `applied`. No `near`, no `merged`.
- Pages (`generate`: 61 pages written or changed; `cleanup`: 5 pages moved):
  - decisions: 11 created (457, 458, 459, 460.1, 460.2, 460.3, 460.4, 460.5, 461, 462, 463). 4 archived and moved: `decision-case-454`, `-455`, `-456` (superseded by 459, 462, 463), `decision-case-460.2` (superseded by 460.5).
  - estimates: 2 created, `pending`: `estimate-harness-make-runs-in-both-shells` (457), `estimate-ledger-write-refuses-a-lesson-without-its-prefix` (460.5). 7 updated by Cases, all `pending`: `estimate-case-protocol-shows-the-built-case` (458), `estimate-lint-checks-the-method` (459), `estimate-lint-finds-a-broken-link` (460.3), `estimate-case-protocol-defers-in-one-reply` (461), `estimate-materialize-judges-a-fence` (462), `estimate-generate-ticks-the-spec` (463), `estimate-ledger-write-lifts` (460.4). 17 updated by readings: 16 `passed`, 1 `failed`.
  - rules: 4 updated by Cases: `rule-case-protocol` (458, 461), `rule-estimates-schema` (459), `rule-page-generation` (463), `rule-ledger-write` (460.5). `deferred_by` cleared on `rule-claude-md` (459), `rule-one-judgment-one-implementation` (462), `rule-page-generation` (463). Cascade draft → built: `rule-backlog`, `rule-insights-schema`, `rule-internal-context`, `rule-skill-hi`, `rule-spec-capture`, `rule-spec-reconcile`; built → draft: `rule-ledger-write`, `rule-lint`, `rule-page-generation`.
  - lessons: 4 created: `lesson-case-show-grill-round-reformatted-in-translation`, `lesson-ledger-block-written-with-a-placeholder-line`, `lesson-case-build-two-promises-in-one-sub-case-with-a-written-criterion`, `lesson-case-build-a-rewritten-criterion-loses-a-finding-text`. 1 renamed (460.1): `harness-senduserfile-renders-a-markdown-file-on-the-phone` → `lesson-harness-senduserfile-renders-a-markdown-file-on-the-phone`. 3 clustered by synthesis; 1 archived by the cascade and moved by `cleanup`: `lesson-case-show-grill-round-reformatted-in-translation`.
  - insights: 2 updated by synthesis: `insight-case-show-built-case-retyped-by-hand` (`actioned`, severity 0), `insight-case-build-promise-lines-compared-by-no-check` (`open`, severity 2 → 4).
- Governed files `render` rewrote: `vault/wiki/case-schema.md` (458, 461), `vault/wiki/estimates/schema.yaml` (459). `guppi sprint` left `vault/wiki/sprint.md` unchanged. `guppi backlog` rewrote `vault/wiki/backlog.md`: 19 → 16 items (`rule-claude-md`, `rule-one-judgment-one-implementation`, `rule-page-generation` dropped). `guppi glossary` left `vault/wiki/glossary.md` unchanged.

## Readings due

35 Estimates stand `pending` or `failed` after `generate`: 1 `failed`, 34 `pending`. Every rule or entity they read stands `draft`.

- `estimate-retro-report-holds-each-fact-once` — `failed` — `rule-retro` draft — by hand at the first `/retro` after the render (method). Result: the `/retro` of session 1819 named the unticked boxes per Case, named every ratification per Case with the same pages again, and repeated parts of the opening list under what got done and what is not done.
- `estimate-harness-make-runs-in-both-shells` — `rule-harness` draft — `raw/2026-09-27/1819/spec.md` line 49.
- `estimate-case-protocol-shows-the-built-case` — `rule-case-protocol` draft — `raw/2026-09-27/1819/spec.md` line 104.
- `estimate-lint-checks-the-method` — `rule-lint` draft — `raw/2026-09-27/1819/spec.md` line 162.
- `estimate-lint-finds-a-broken-link` — `rule-lint` draft — `raw/2026-09-27/1819/spec.md` line 256.
- `estimate-ledger-write-lifts` — `rule-ledger-write` draft — `raw/2026-09-27/1819/spec.md` line 293.
- `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — `rule-ledger-write` draft — `raw/2026-09-27/1819/spec.md` line 345.
- `estimate-case-protocol-defers-in-one-reply` — `rule-case-protocol` draft — `raw/2026-09-27/1819/spec.md` line 396.
- `estimate-materialize-judges-a-fence` — `rule-materialize` draft — `raw/2026-09-27/1819/spec.md` line 449.
- `estimate-generate-ticks-the-spec` — `rule-page-generation` draft — `raw/2026-09-27/1819/spec.md` line 510.
- `estimate-agent-writing-followed` — `rule-agent-writing` draft — by hand, the person's messages of one session read for a complaint about the agent's text (method).
- `estimate-brief-written` — `rule-brief` draft — by hand after the first librarian run (method).
- `estimate-carry-over-writes` — `rule-carry-over` draft — pytest over the skill's render, plus one live reading of a carried-over session (method).
- `estimate-case-build-writes-the-case` — `rule-case-build` draft — by hand, live dispatches in a session after the render (method).
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` draft — `uv run pytest tests/test_casecheck.py -k subagent`, then by hand (method).
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` draft — `uv run pytest tests/test_casecheck.py -k stop`, then by hand (method).
- `estimate-case-protocol-case-form` — `rule-case-protocol` draft — by hand, the Cases of a session at its close (method).
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` draft — by hand, the ledger and preview of the first session where a lesson and the Case that closes its cause stand together (method).
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` draft — `uv run pytest tests/test_context.py -k limit`; by hand at the first prompt past 400 000 tokens (method).
- `estimate-documentation-completes` — `rule-documentation` draft — `make test-documentation`; the live reading by hand (method).
- `estimate-event-log-records` — `rule-event-log` draft — pytest in `tests/test_event.py` and `tests/test_gate.py`; readings by hand (method).
- `estimate-harness-pipeline` — `rule-harness` draft — `make test-harness`; the live reading of `make lint` by hand (method).
- `estimate-language-followed` — `rule-language` draft — by hand in the next session (method).
- `estimate-materialize-assembles` — `rule-materialize` draft — pytest in `tests/test_materialize.py`; the live reading once by hand (method).
- `estimate-prespec-reconciles` — `rule-prespec` draft — by hand, the first `/pre-spec` after the render (method).
- `estimate-retro-loads` — `rule-retro` draft — by hand at the first `/retro` (method).
- `estimate-session-phases-in-order` — `rule-session` draft — by hand at the close of a session, the day's records in order (method).
- `estimate-skill-grill-me-asks-in-rounds` — `rule-skill-grill-me` draft — `uv run guppi render --check`; by hand, one `/grill-me` after the render (method).
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` draft — `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change (method).
- `estimate-sprint-moves-a-passed-over-item` — `rule-sprint` draft — `pytest tests/test_generate.py` and the History of the sprint page after the librarian's run (method).
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` draft — by hand, the yaml and the brief after the librarian's run on the first marked lesson clustered under an actioned Insight (method).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` draft — by hand, the tree at the close of the sprint (method).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` draft — `make lint` exit 0, or only unread lines on the Estimates of the sprint (method).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` draft — `make test` on the last commit of migration, then `git log` of main after the merge (method).
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` draft — by hand, the listed `ls`, `grep`, `render --check` and `glossary --check` (method).

## Flags

- `incomplete`: line 7 (`harness-senduserfile-renders-a-markdown-file-on-the-phone`, 460.1), `[category]` — `category: unknown`; applied and renamed, as the handoff expected. Lines 8 and 9 (460.2), `[criterion]` — superseded by 460.5, not applied.
- `failed`, `near`, `merged`, `unparsed`: none in the yamls of 1255 and 1819.
- Superseded in the session: lines 8–10 (Case 460.2) carry `superseded_by: 460.5` and were not applied; 460.4 (line 20) and 460.5 (lines 21–22) applied. `decision-case-460.2` was written with the two-line body and archived.
- Synthesis: `lesson-case-show-grill-round-reformatted-in-translation` clustered under `insight-case-show-built-case-retyped-by-hand` (the main agent rewrites the answer of `case-guppi` when showing it). The lesson carries `addressed_by: decision-case-458`; the Insight stood `actioned` by `decision-case-452.4`; 458 is later, so its `addressed_by` became `decision-case-458` and `status` stayed `actioned`. The cascade archived the lesson.
- Synthesis: `lesson-case-build-two-promises-in-one-sub-case-with-a-written-criterion` and `lesson-case-build-a-rewritten-criterion-loses-a-finding-text` clustered under the `open` `insight-case-build-promise-lines-compared-by-no-check`; severity 2 → 4.
- Synthesis: `lesson-ledger-block-written-with-a-placeholder-line` has no pair among the lessons and the Insights and stays `new`.
- Failed Estimates: 1, listed first under Readings due.
- Contradiction, from the handoff: `estimate-sprint-migration-file-route-gone` says "generate reports an error" for an entry of unknown category; an `update` or `delete` of `category: unknown` applies and ticks (460.1). The person chose to leave the Estimate as it stands (Q7).
- Handoff: `prespec --check` finds two Estimate items in one Case only when neither writes its Criterion under `sections`; 460.2 did, so the check did not fire (lesson line 37).
- Handoff: `estimate-carry-over-writes` — its method names pytest over the skill's render, and no test targets the carry skill (`pytest tests/test_render.py -k skill`: 26 deselected).
- Handoff: `estimate-harness-pipeline` (W12) was not read in the session; readable after commit 49acdff.
- Handoff: a Work Mode subagent's `sed` rewrote one extra line of `apply` in `generate.py` and restored it; `git diff` showed only the intended change.
- Handoff: `make lint` exit 2 from PowerShell and Git Bash (the known findings); `guppi lint` 115 lines in the session.
- MOC candidates: none named by lint.
- Stale defers, from lint: `rule-work-mode` deferred 32 times since case 29; `rule-subagent-guppi` 31 times since case 29; `rule-morph` once since case 239; `rule-orchestration` once since case 424.
- Backlog moves by `generate`: none printed. Milestones dropped: none printed.
- `materialize`, `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary`: no stderr lines.
- `archive` (run after the brief): exit 0, no stdout and no stderr line; it moved no unit. `raw/2026-09-27/1255/` and `raw/2026-09-27/1819/` are dated the day of the run, which `archive` does not look at; 1819 is the session of the run.
- `make lint`, after the render: exit 2, 105 findings.
  - `decisions/decision-case-N: schema: missing section ## Context` and `## Problem` on 31 pages (cases 1–28). That is 62 findings.
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`, and `orphan: no other live page names it in its frontmatter`.
  - `rules/rule-morph: deferred: 1 time since case 239`; `rules/rule-orchestration: deferred: 1 time since case 424`; `rules/rule-subagent-guppi: deferred: 31 times since case 29`; `rules/rule-work-mode: deferred: 32 times since case 29`.
  - `unread: pending` on 34 Estimates and `unread: failed` on 1. These are the 35 Estimates of Readings due.
  - `estimates: unmigrated: 19 pages in the shape before case 193`.
  - The `method` contradiction on `estimate-claude-md-rendered` of the previous brief is gone.

## Next session

Cases:
- The retro report standard: `estimate-retro-report-holds-each-fact-once` failed; the person asked to agree one standard for writing the retro (handoff).
- The method of `estimate-carry-over-writes`: no test targets the carry skill; a test to write or a method to change (handoff).
- Contradiction: `estimate-sprint-migration-file-route-gone` against the apply of an unknown-category update (460.1); left by the person (Q7) (handoff).

Work:
- `estimate-harness-make-runs-in-both-shells`
- `estimate-case-protocol-shows-the-built-case`
- `estimate-lint-checks-the-method`
- `estimate-lint-finds-a-broken-link`
- `estimate-ledger-write-lifts`
- `estimate-ledger-write-refuses-a-lesson-without-its-prefix`
- `estimate-case-protocol-defers-in-one-reply`
- `estimate-materialize-judges-a-fence`
- `estimate-generate-ticks-the-spec`
- `estimate-agent-writing-followed`
- `estimate-brief-written`
- `estimate-case-build-writes-the-case`
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-case-check-shows-only-the-checked-case`
- `estimate-case-protocol-case-form`
- `estimate-case-protocol-ledger-line-form`
- `estimate-context-size-warns-past-the-limit`
- `estimate-documentation-completes`
- `estimate-event-log-records`
- `estimate-harness-pipeline`
- `estimate-language-followed`
- `estimate-materialize-assembles`
- `estimate-prespec-reconciles`
- `estimate-retro-loads`
- `estimate-session-phases-in-order`
- `estimate-skill-grill-me-asks-in-rounds`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-sprint-moves-a-passed-over-item`
- `estimate-synthesis-keeps-actioned-by-the-mark` — this run clustered a lesson with `addressed_by` under an actioned Insight
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-sprint-migration-rule-class-files-dissolved`
- The unticked boxes of the Specs, all `read` lines: `raw/2026-09-27/1819/spec.md` lines 49, 104, 162, 256, 293, 345, 396, 449, 510; `raw/2026-09-27/1255/spec.md` lines 72, 110, 496, 542, 595, 755, 791, 895, 944, 1065, 1117.
- Ledger lines not applied: lines 8–10 of `raw/2026-09-27/1819/ledger.md` (Case 460.2, superseded by 460.5); every other of its 39 lines has an applied entry.
- Dirty tree: none after the librarian's commit.

## Readings at the close

- `make test`: 827 passed, 2 skipped.
- `make lint`: exit 2, 105 findings (listed under Flags).
- Pages in `vault/wiki/`: decisions 666, estimates 142, rules 68, lessons 61, insights 25, entities 4.
