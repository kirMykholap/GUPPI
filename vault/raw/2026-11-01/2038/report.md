Librarian report, 2026-11-01, session 2038

The run finished and is committed as `079217a6` (`docs(vault): librarian, 2026-11-01`). After the commit the tree is clean. The yaml had no entry marked incomplete or failed, and the librarian merged nothing. Lint has 9 lines.

Pages created (11):
- decisions 9: `decision-case-990`, `991`, `991.1`, `991.2`, `991.3`, `991.4`, `992`, `992.1`, `992.2`. `decision-case-990` was archived in the same run, marked superseded.
- estimates 1: `estimate-orchestration-closes-a-line-by-what-its-case-does`, `passed`.
- lessons 1: `lesson-showing-sent-only-the-files-of-the-case-headings`, `new`.

Pages updated (15):
- rules 5: `rule-orchestration` (991.1 and 992.2), `rule-skill-hi` (991.1), `rule-prespec-onward` (992.1). `rule-close` and `rule-handoff` went `draft → built` by the cascade.
- estimates 9:
  - `estimate-hi-writes-frontier`: Criterion and `method` set, `pending`.
  - Criterion replaced, then `passed` by their readings: `estimate-orchestration-takes-back-a-ratified-case`, `estimate-orchestration-defers-in-one-reply`, `estimate-prespec-onward-sends-the-agent-on`, `estimate-orchestration-acknowledging-reply`.
  - `passed`: `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-close-reports-the-run`, `estimate-handoff-dispatches`.
  - `failed`: `estimate-case-build-reads-the-readers-of-a-new-files-folder`.
- insights 1: `insight-frontier-line-closed-by-the-case-built-on-its-item`, `open → actioned`, `addressed_by: decision-case-991.1`.

Marks in the yaml:
- No entry is marked `incomplete`, `failed`, `exists` or `near`, and `unparsed: []`.
- Entries 1 and 2 (Case 990) carry `superseded_by` and were not applied, as the handoff asked.
- 29 entries are `applied`: 20 entries and 9 decisions.

Pages archived (4), moved by cleanup to `vault/archive/plugin/2026-11-01/2038/`:
- `decision-case-990` (superseded)
- `lesson-frontier-sprint-line-closed-by-a-case-that-updates-no-sprint-page`
- `lesson-frontier-closed-a-backlog-item-deferred-again-as-a-case`
- `lesson-frontier-backlog-line-closed-by-a-case-that-keeps-its-defer`

The three lessons left because their Insight was actioned.

`guppi archive` printed nothing on stdout or stderr. It moved no unit and named none it kept.

Index check:
- One `create` entry other than an Estimate: L23.
- Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 61 lines. No lesson has the same or a near root cause, so no mark was added.

Synthesis:
- The same lessons Grep printed 61 lines. Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 14 lines.
- `lesson-showing-sent-only-the-files-of-the-case-headings` joined nothing and stays `new`.
- I opened `vault/wiki/insights/insight-orchestration-writes-from-its-own-reading.md` because its index line did not settle whether it shares the root cause. Outcome: not clustered. Its pattern is a fact or line written from the agent's own reading instead of the source of record; the lesson is about which files were sent.

Ledger read (for the Work line): `vault/raw/2026-11-01/2038/ledger.md` has 23 lines. The yaml holds entries for lines 1–17 and 19–23. Line 18 is folded into the `create` of line 5. Every line is accounted for.

Handoff instructions:
- All four were checked against the yaml, the log and the pages, and each holds.
- Both updates of `rule-orchestration` (991.1 and 992.2) applied with nothing on the stderr of `generate`. So each `old` text still matched after the other update.
- The handoff asked for no repair and no read beyond the frame.

Flags:
- `estimate-case-build-reads-the-readers-of-a-new-files-folder` is `failed` (L17).
- `estimate-orchestration-acknowledging-reply`: in this run Case 992.2 replaced its Criterion and set it `pending`. Then reading L22 set it `passed`. That reading was taken on the Render before Case 992.2 and says the new `STOP:` line was not exercised.
- Count check: the handoff's Debt says 19 boxes wait for the librarian. This run ticked 19 boxes in the 2038 Spec and 1 in the 1721 Spec. Line 162 of the 2038 Spec (`read estimate-hi-writes-frontier`) stays unticked.
- No stale defer and no MOC candidate.
- No step's stderr printed anything, no hook refused a call, and I made no read that the frame says my job does not need.

Lint (`guppi check`, exit 1, 9 lines):
- 8 lines `status: a page with core: true that is draft`: `rule-ask`, `rule-case-build`, `rule-morph`, `rule-orchestration`, `rule-skill-approve-spec`, `rule-skill-hi`, `rule-spec-box`, `rule-synthesis`.
- 1 line `estimates/estimate-case-build-reads-the-readers-of-a-new-files-folder: unread: failed`.

The brief is at `c:\PROJECTS\GUPPI\vault\wiki\brief.md`.
