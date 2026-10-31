# Librarian report — 2026-10-31, session 0431

The run finished and was committed as `9399031e docs(vault): librarian, 2026-10-31`. The tree is clean after the commit. Claude Code refused my `Write` of `report.md` (details at the end), so this text is the report. The `SubagentStop` hook `guppi libreport` should copy it into `vault/raw/2026-10-31/0431/report.md`.

## Pages created (28)

- **decisions, 23:**
  - 21 live: `decision-case-956`, `956.2`, `956.3`, `956.4`, `956.5`, `957`, `959`, `960`, `960.1`, `960.2`, `960.3`, `961`, `961.1`–`961.5`, `962`, `963`, `964`, `965`.
  - 2 created and archived as superseded: `decision-case-956.1`, `decision-case-961.6`.
- **rules, 1:** `rule-librarian-report-copy`. It is `built`, has `core: true` as a boolean and `parent: rule-documentation`, and stands in the `children` of `rule-documentation`.
- **estimates, 4:**
  - `estimate-sprint-keeps-one-live-page` (`passed`)
  - `estimate-estimates-schema-method-names-its-evidence` (`passed`)
  - `estimate-librarian-report-copy-writes-the-file` (`passed`)
  - `estimate-backlog-keeps-the-work-taken-out-of-a-built-page` (`pending`)
- **lessons, 2:** `lesson-librarian-claude-code-refuses-a-report-file-of-a-subagent-by-its-name`, `lesson-spec-write-lifts-a-create-value-as-a-string`.

## Pages updated (31)

- **rules, 11:** `rule-backlog`, `rule-case-protocol`, `rule-close`, `rule-documentation`, `rule-estimates-schema`, `rule-handoff`, `rule-hook-registry`, `rule-search-leaves-out-decisions`, `rule-spec-box`, `rule-where-to-stop`, `rule-work-mode`.
- **estimates, 16.**
- **entities, 3:** `entity-guppi`, `entity-sprint`, `entity-sprint-plugin`.
- **insights, 1:** `insight-plugin-cli-withholds-approval-of-a-long-plan` (deferred by Case 957).
- **Status changes by the cascade:**
  - `draft → built`: `entity-guppi`, `entity-sprint`, `rule-librarian-report-copy`, `rule-search-leaves-out-decisions`, `rule-where-to-stop`, `rule-work-mode`.
  - `built → draft`: `rule-backlog`, `rule-handoff`, `rule-spec-box`.

## Entries marked incomplete or failed

- **`incomplete`:** line 4, `estimate-librarian-report-copy-writes-the-file` of Case 956.1, lacks `criterion`. Case 965 superseded it, so it was not applied.
- **`failed`:** none. `unparsed: []`.
- **Superseded and not applied, as the handoff asked:** lines 3, 4 and 5 (Case 956.1) and line 26 (Case 961.6).

## Pages archived

- `guppi cleanup` moved `decision-case-956.1` and `decision-case-961.6` to `vault/archive/plugin/2026-10-31/0431/decisions/`.
- `guppi archive` printed nothing and moved no unit. The two units in `raw/`, `2026-10-31/0128` and `2026-10-31/0431`, are dated the day of the run. `guppi archive` only looks at units dated before that day (`.guppi/guppi/archive.py`).

## Index check and synthesis

- **`^(purpose|deferred_by):` over `vault/wiki/rules/`:** 87 lines. No page has the same purpose as `rule-librarian-report-copy`, and none is near.
- **`^(root_cause|deferred_by):` over `vault/wiki/lessons/`:** 56 lines. Neither lesson entry is the same as a page or near one, and neither shares a root cause with another lesson.
- **`^(pattern|deferred_by):` over `vault/wiki/insights/`:** 13 lines. Neither lesson shares a pattern with an Insight.
- The Grep tool cut four long index lines. I printed them with `grep` on their frontmatter lines only: `lesson-case-build-subagent-compaction-fires-below-its-window`, `lesson-hooks-subagentstop-reads-the-last-text-not-the-handback`, `lesson-hooks-subagentstop-fires-before-and-after-the-handback` and `rule-case-check`.
- I opened no page to decide same or near.
- I did not edit the yaml: there is no `merged`, `near` or `synthesis` entry.

## Reads

- **`vault/raw/2026-10-31/0431/ledger.md`, its one read:** 50 lines (`wc -l`), and lines 39–41, which are folded into the entries of lines 34, 14 and 18. Every line is accounted for.
- **`.guppi/guppi/archive.py`:** read to say why `guppi archive` moved nothing.

## Flags

- **Failed Estimates (5):**
  - `estimate-case-build-reads-the-readers-of-a-changed-step`
  - `estimate-ask-query-before-a-create`
  - `estimate-orchestration-shows-the-built-case`
  - `estimate-orchestration-names-related-cases-in-the-dispatch`
  - `estimate-case-build-reads-each-list-of-a-new-member`
- **`estimate-close-reports-the-run`:** it read `failed` at /hi (L2) and now stands `pending`. The `update` of Case 956.2 (line 8) reset it after that reading. The handoff counts six failed Estimates.
- **`estimate-orchestration-signs-items-taken-together`:** the inputs do not show whether its event came in this session. The event is a batch of items taken up together, with a summary line `Other Case`. Its reading stays in Readings due.
- **Stale defer:** `rule-spec-box` has been put off for 8 sessions (`backlog.md`).
- **`guppi sprint`:** it left `vault/wiki/sprint.md` unchanged. The Backlog notes of Case 962 show in `backlog.md`, not in `sprint.md`.
- **Handoff observations carried into the brief:**
  - `ask-guppi` at `/pre-spec` made searches outside its frame.
  - The main agent showed Case 964 again after text of its own.
- No stderr line from `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary` or `archive`.
- No MOC candidate and no contradiction found. No read outside the frame.

## Lint

`guppi check` printed 16 lines and exited 1:
- 11 lines are pages with `core: true` that stand `draft`: `rule-ask`, `rule-backlog`, `rule-case-build`, `rule-close`, `rule-handoff`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-skill-hi`, `rule-spec-box`, `rule-synthesis`.
- 5 lines are `unread: failed`, one for each failed Estimate.

---

**Refused:** Claude Code refused my `Write` of `C:\PROJECTS\GUPPI\vault\raw\2026-10-31\0431\report.md` with: "Subagents should return findings as text, not write report files. Include this content in your final response instead." This is the refusal L49 describes. I did not write the file another way, made the commit, and give the report here as text.
