Librarian report, 2026-11-01, session 2227. Commit `d05eaa5a docs(vault): librarian, 2026-11-01`. The working tree is clean after it.

**Pages created and updated (33, as `guppi generate` printed for 2227)**
- Created (15):
  - decisions 12: `decision-case-993`, `993.1`, `993.2`, `994`, `995`, `995.1`, `995.2`, `995.3`, `996`, `996.1`, `996.2`, `996.3`.
  - estimates 2: `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` and `estimate-prespec-finds-a-reader-of-a-new-files-folder`, both `pending`.
  - lessons 1: `lesson-acknowledging-reply-labels-left-in-english`, `new`.
- Updated (18):
  - rules 8: `rule-close`, `rule-documentation`, `rule-case-build`, `rule-prespec`, `rule-ask`, `rule-clean-branch`, `rule-lint`, `rule-orchestration`. `rule-close` and `rule-prespec` went `built → draft` by the cascade.
  - estimates 9: three readings `failed`, three `passed`, three Criteria set `pending`.
  - entities 1: `entity-sprint-plugin`.

**Marks**
- No entry is `incomplete`, `failed`, `exists` or `near`, and `unparsed: []`.
- All 25 entries and all 12 decision items are `applied`.

**Pages archived**
- `guppi cleanup` moved 0 pages.
- `guppi archive` moved three units to `archive/plugin/2026-11-01/<HHMM>/raw`: `raw/2026-11-01/0141`, `raw/2026-11-01/1721` and `raw/2026-11-01/2038`.
- It kept `raw/2026-11-01/2227`, because it is the session of the run.
- `raw/2026-10-14/1907` has no `ledger.md`, so it is not a unit and was not looked at.
- `guppi archive` printed nothing on stderr.

**Index check and synthesis**
- One `create` entry other than an Estimate was checked: L25.
- The Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 59 lines. No lesson has the same or a near root cause, so no mark was added.
- The Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 14 lines.
- `lesson-acknowledging-reply-labels-left-in-english` joined no lesson or Insight and stays `new`.
- I opened no page under `vault/wiki/` to settle "same", "near" or "shared root cause". No script named a page in an error.

**Ledger read**
- I read `vault/raw/2026-11-01/2227/ledger.md` once: 25 lines.
- The yaml holds entries for lines 1–25, so every line is accounted for and no line was left unapplied.

**Handoff instructions**
- I checked every `old` of the `replace` pairs against its own page before `generate`. Each occurs once:
  - the two pairs of `rule-clean-branch`;
  - the two pairs of `rule-prespec`, the second checked against `rule-prespec` itself;
  - the pair of `rule-ask` and the pair of `rule-case-build`.
- Both updates of `estimate-lint-checks-the-statuses` (from 996.1 and 996.3) are applied.
- No instruction asked for a repair.

**Flags**
- Three Estimates stand `failed`: `estimate-case-build-reads-the-readers-of-a-changed-step` (L19), `estimate-case-build-reads-the-link-graph-of-what-it-changes` (L20) and `estimate-orchestration-acknowledging-reply` (L21). These three are the `Cases` of Next session in the brief.
- Because `estimate-orchestration-acknowledging-reply` is `failed`, `rule-orchestration` now draws the lint line `a page with core: true that is draft`.
- No step printed anything on stderr: materialize, generate, cleanup, render, sprint, backlog, glossary and archive. No Spec line holds `guppi sprint-close --apply`, so no sprint close ran.
- There is no stale defer, MOC candidate or contradiction. I made no read that this frame says my job does not need. No hook refused a call.
- This run started on the old close text of the frame. The render of this run wrote the Case 994 version into `.claude/agents/librarian-guppi.md`. This report is given back once, by this handback.

**Lint total**
`guppi check` exits 1 with 7 lines:
- 4 lines `status: a page with core: true that is draft`: `rule-case-build`, `rule-morph`, `rule-orchestration`, `rule-skill-approve-spec`.
- 3 lines `unread: failed`: the three failed Estimates above.

The new brief is at `c:\PROJECTS\GUPPI\vault\wiki\brief.md`.
