The librarian run for session 0141 (2026-11-01) is done and committed as d0f9b153 (`docs(vault): librarian, 2026-11-01`). The tree is clean after the commit. All 17 entries were applied, none was marked incomplete or failed, and `guppi check` ends at 13 lines (exit 1).

**Pages created (11):**
- decisions 7: `decision-case-977`, `-978`, `-979`, `-980`, `-981`, `-981.1`, `-981.2`
- estimates 3: `estimate-ledger-write-refuses-a-bare-link-to-no-page` (passed), `estimate-case-check-sends-back-a-summary-after-text` (passed), `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link` (pending)
- lessons 1: `lesson-orchestration-closes-a-frontier-line-by-its-closer-alone` (new)

**Pages updated (13):**
- estimates 7:
  - passed: `estimate-rules-schema-checked`, `estimate-ask-searches-at-prespec`, `estimate-orchestration-shows-the-built-case`
  - failed: `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-case-build-reads-the-link-graph-of-what-it-changes`, `estimate-case-build-reads-the-readers-of-a-changed-step`
  - pending: `estimate-case-build-reads-each-list-of-a-new-member`
- rules 4: `rule-ledger-write`, `rule-case-build`, `rule-case-check` by Cases; `rule-rules-schema` went draft → built by the cascade.
- lessons 1: `lesson-ledger-reading-writes-a-bare-wikilink`.
- entities 1: `entity-sprint-plugin` (its `estimates` list).

**Entries marked incomplete or failed:** none. No entry is marked `exists`, `near`, `librarian` or `merged`, and `unparsed: []`.

**Pages archived:**
- Generate set `decision-case-971` and `decision-case-976` to `archived · superseded`, because Cases 979, 980 and 981.2 supersede them. Cleanup moved both to `vault/archive/plugin/2026-11-01/0141/decisions/` and printed `2 page(s) moved`.
- `guppi archive` moved one unit: `raw/2026-10-31/2307 → archive/plugin/2026-10-31/2307/raw`, nothing on stderr.
- Units kept: `raw/2026-11-01/0141`, the session of this run, which is never moved. `raw/2026-10-14/1907` holds no `ledger.md`, so it is not a unit.
- No pending Estimate's `method` names the archive step, so no Readings due line gained archive output.

**Flags I raised:**
- Three failed Estimates: `estimate-case-build-reads-the-link-graph-of-what-it-changes`, `estimate-case-build-reads-the-readers-of-a-changed-step`, `estimate-orchestration-names-related-cases-in-the-dispatch`.
- Stale defer:
  - `estimate-close-reports-the-run` keeps `deferred_by: ["[[decision-case-971]]"]`.
  - `estimate-handoff-dispatches` keeps `deferred_by: ["[[decision-case-976]]"]`.
  - Both Decision pages were archived as superseded in this run, and both Estimates still stand in `backlog.md`.
  - The supersedes of 979, 980 and 981.2 retired those defers on three other Estimates only.
  - This is also under Cases in the brief.
- Defers put off in 2 or more sessions: `rule-spec-box` (8) and `rule-ratification` (2).
- Nothing printed on stderr by generate, cleanup, render, sprint, backlog, glossary or archive.

**Lint total:** `guppi check` prints 13 lines, exit 1:
- 10 lines: `status: a page with core: true that is draft`.
- 3 lines: `unread: failed`, for the three failed Estimates above.
- The `ref` line on `lesson-ledger-reading-writes-a-bare-wikilink` is gone. No `backlog.md differs from its sources` line was printed.

**Index check:**
- One `create` other than an Estimate: `lesson-orchestration-closes-a-frontier-line-by-its-closer-alone`.
- I ran the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`; it printed 60 lines. The output was too long, so the harness saved it to `C:\Users\kir\.claude\projects\c--PROJECTS-GUPPI\b91d8531-1bea-46ba-a54a-0282b108e453\tool-results\toolu_019iDcYpqyTHD6Edb41PSM9F.txt`, and I read that file.
- No index line names the same page or a near one, so the yaml was not edited.

**Synthesis:**
- Lessons Grep: 60 lines. Insights Grep `^(pattern|deferred_by):` over `vault/wiki/insights/`: 14 lines.
- `lesson-orchestration-closes-a-frontier-line-by-its-closer-alone` joined nothing. Its cause is an Edit that matched only the end of a Frontier line and so left the box open.
- `lesson-frontier-sprint-line-closed-by-a-case-that-updates-no-sprint-page` and `lesson-frontier-closed-a-backlog-item-deferred-again-as-a-case` are about which closer to choose, not about the edit that writes it.
- No entry was added.

**Pages opened for the first three reasons of the frame:** none.

**Ledger read:** I read `vault/raw/2026-11-01/0141/ledger.md` once, with `wc -l` and a listing, for the `Work` line. It has 19 lines. The yaml holds entries for lines 1–11 and 14–19, and lines 12 and 13 are folded into the creates of lines 3 and 10, so every line is accounted for.

**Handoff instructions:**
- All four are descriptions that match the yaml as `guppi materialize` wrote it: the 10 `implementation_ref` paths, both places of the 978 root cause, the supersedes on 979, 980 and 981.2, and the failed readings.
- None asked for a repair, so nothing was refused.

**Reads my frame says my job does not need:** none.

**Hook refusals:** none.
