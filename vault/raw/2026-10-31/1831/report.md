Librarian run for 2026-10-31, session 1831: all steps ran and the vault is committed as `6ccb92a0 docs(vault): librarian, 2026-10-31`. After the commit `git status` is clean. `guppi check` printed 18 lines: 16 before the work, by the handoff.

**Pages created (23)**
- decisions: 15 (`decision-case-966`, `967`, `967.1`, `967.2`, `967.3`, `968`, `969`, `969.1`, `969.2`, `969.3`, `970`, `970.1`, `970.2`, `970.3`, `971`)
- entities: 1 (`entity-link-graph`, `built`)
- rules: 1 (`rule-link-graph-at-session-start`, `draft`)
- estimates: 5 (`estimate-link-graph-prints-the-neighbours` `passed`; four `pending`: `estimate-case-build-reads-the-link-graph-of-what-it-changes`, `estimate-link-graph-at-session-start-writes-the-file`, `estimate-materialize-lifts-a-create-value-by-the-schema`, `estimate-case-build-runs-the-vault-query-first`)
- lessons: 1 (`lesson-case-build-names-a-file-without-the-readers-of-its-folder`, `clustered`)

**Pages updated (19)**
- rules: 8 (`rule-ask`, `rule-backlog`, `rule-case-build`, `rule-case-protocol`, `rule-estimates-schema`, `rule-harness`, `rule-hook-registry`, `rule-materialize`)
- estimates: 9 (`estimate-ask-query-before-a-create`, `estimate-ask-searches-at-prespec`, `estimate-case-build-reads-the-readers-of-a-changed-step`, `estimate-estimates-schema-checked`, `estimate-lint-checks-the-statuses`, and the four that Case 971 defers)
- entities: 1 (`entity-guppi`)
- insights: 1 (`insight-case-build-changes-a-step-without-reading-its-readers`)

**Entries marked incomplete or failed:** none. Every entry is `applied`, and `unparsed: []`. The 4 `defer` entries (lines 26–29) carry `exists`. No entry is marked `near` or `merged`.

**Pages archived:** `cleanup` moved 3 pages into `vault/archive/plugin/2026-10-31/1831/`:
- `estimates/estimate-backlog-keeps-the-work-taken-out-of-a-built-page` (deleted by Case 969.3, after its reading of line 1 applied)
- `estimates/estimate-guppi-keeps-no-defer-of-its-shape` (deleted by Case 969.3)
- `decisions/decision-case-963` (superseded by Case 969.1)

**Archive:** `guppi archive` printed nothing and exited 0. It moved no unit and kept none with a reason. Units 0128 and 0431 are dated the day of the run, which the archive step does not look at. 1831 is the session of the run.

**Index check**
- `entity-link-graph` against `^(purpose|deferred_by):` over `vault/wiki/entities/` (5 lines): not the same as any page, and not near.
- `rule-link-graph-at-session-start` against `^(purpose|deferred_by):` over `vault/wiki/rules/` (89 lines): not the same as any page, and not near.
- No page was opened for the index check.

**Synthesis**
- `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 58 lines. `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 14 lines.
- I opened `vault/wiki/insights/insight-case-build-changes-a-step-without-reading-its-readers.md` because its index line did not settle whether it shares the root cause of the new lesson. Outcome: clustered.
- Two update entries were appended, marked `librarian: synthesis`:
  - The Insight: the new lesson added to `children`, and `status: open`. It stood `actioned` by `decision-case-924`, and the lesson carries no `addressed_by`.
  - The lesson: `status: clustered`, with `insight` set to that Insight.

**Ledger read:** the one read of `vault/raw/2026-10-31/1831/ledger.md`, by `wc -l` and line 30. It has 32 lines. The yaml covers lines 1–29, 31 and 32, and line 30 is folded into the entry of line 6, so no line is outside the yaml.

**The handoff's instructions, checked**
- `core: true`: `entity-link-graph` and `rule-link-graph-at-session-start` both hold it as a boolean. No flag.
- Replace pairs: the three pairs of `rule-case-build` and the two of `rule-case-protocol` applied with no error, and each new text stands once in its page.
- Order: the reading of `estimate-backlog-keeps-the-work-taken-out-of-a-built-page` applied before its delete.
- Backlog: `rule-estimates-schema` left `backlog.md` and the four Estimates of Case 971 entered it (8 items to 12).
- Render: it wrote `.claude/settings.json` (with `guppi links --write`), `.claude/agents/case-guppi.md`, `.claude/agents/ask-guppi.md`, `vault/wiki/case-schema.md` and `vault/wiki/estimates/schema.yaml` (with `once`).

The handoff asked for no repair of an entry, and no hook refused a call.

**Flags raised**
1. No script printed anything on stderr: generate, cleanup, render, sprint, backlog, glossary, archive.
2. Three failed Estimates, all deferred by Case 971: `estimate-case-build-reads-each-list-of-a-new-member`, `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-orchestration-shows-the-built-case`.
3. Lint on the new `estimate-link-graph-prints-the-neighbours`: `ref: body names slug, which no live or archived page carries`. Lint reads the word `slug` in the code span `[[slug]]` of its Criterion as a link to a page. The brief lists this under Cases as a defect.
4. The new `estimate-link-graph-at-session-start-writes-the-file` has `unread: pending`. The by-hand part of its `method` opens with `and by hand, after`, which lint does not read as waiting for a later moment. The brief lists this under Cases as a defect, plus a proposal to defer it into `backlog.md` (from the handoff's Debt).
5. Two defers have been put off in 2 or more sessions: `rule-ratification` (2) and `estimate-orchestration-shows-the-built-case` (3).
6. The cascade moved `rule-estimates-schema` and `rule-materialize` from `built` to `draft`, and `entity-link-graph` and `rule-backlog` from `draft` to `built`.
7. No MOC candidate, contradiction or read outside the frame was seen.

**Lint total:** `guppi check` printed 18 lines and exited 1:
- 13 `status: a page with core: true that is draft`
- 3 `unread: failed`
- 1 `unread: pending`
- 1 `ref`

The new brief is `c:\PROJECTS\GUPPI\vault\wiki\brief.md`.
