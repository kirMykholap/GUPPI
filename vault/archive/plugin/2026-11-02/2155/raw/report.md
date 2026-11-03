Librarian report — session 2155 (2026-11-02). Committed as 14a82de8 `docs(vault): librarian, 2026-11-02`. The tree is clean after the commit.

**Pages created (12):** decisions 7 (`decision-case-1011`, `decision-case-1011.1` to `decision-case-1011.4`, `decision-case-1012`, `decision-case-1013`); rules 1 (`rule-frontier-hook`, `core: true`, set `built` by the cascade); estimates 1 (`estimate-frontier-hook-refuses-an-open-box-with-a-closer`, `passed` by L19); lessons 2 (`lesson-ship-docstring-sample-writes-a-real-case-number`, `lesson-caseid-session-option-takes-the-hhmm`); insights 1 (`insight-ship-live-code-writes-a-case-number-outside-a-bracket`, made by the synthesis, `open`, severity 2).

**Pages updated (15):** rules 6 (`rule-case-check`, `rule-case-build`, `rule-case-protocol`, `rule-hook-registry`, `rule-orchestration`, `rule-plan-mode`); estimates 6 (`estimate-case-check-notes-the-files-that-name-what-a-case-changes`, `estimate-case-build-searches-the-names-of-what-it-changes`, `estimate-case-build-reads-by-need-and-in-parts`, `estimate-case-build-writes-the-case`, `estimate-orchestration-acknowledging-reply`, `estimate-sprint-plugin-ci-writes-a-clean-branch`); insights 2 (`insight-orchestration-frontier-closer-leaves-the-box-open` and `insight-orchestration-acknowledging-reply-keeps-headings-in-english`, both now `actioned`); lessons 1 (`lesson-ship-test-comment-writes-a-bare-case-reference`, now `clustered`).

**Deleted:** 1 page, `estimate-case-check-sends-one-note-for-a-broad-name`, by Case 1011.1.

**Entries marked incomplete or failed:** none. Every entry carries `applied`, and `unparsed: []`.

**Pages archived:**
- `guppi cleanup` moved 4 pages to `vault/archive/plugin/2026-11-03/2155/`:
  - `estimate-case-check-sends-one-note-for-a-broad-name`
  - `lesson-frontier-closer-appended-without-ticking-the-box`
  - `lesson-orchestration-closes-a-frontier-line-by-its-closer-alone`
  - `lesson-orchestration-defer-reply-frontier-heading-in-english`
- `guppi archive` moved 5 units and printed nothing on stderr. Each of `raw/2026-11-02/0039`, `0254`, `1337`, `1548` and `2035` went to `archive/plugin/2026-11-02/<HHMM>/raw`. It kept `raw/2026-11-02/2155` because it is the session of this run.

**Index check:**
- The Grep `^(purpose|deferred_by):` over `vault/wiki/rules/` printed 89 lines. No line matches `rule-frontier-hook`, so it got no mark.
- The Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 65 lines (the harness saved the output to a file, and I read that file).
  - `lesson-ship-docstring-sample-writes-a-real-case-number` got `near: lesson-ship-test-comment-writes-a-bare-case-reference`.
  - `lesson-caseid-session-option-takes-the-hhmm` got no mark.
- The `create` of `estimate-frontier-hook-refuses-an-open-box-with-a-closer` is an Estimate, so it has no index check.
- No entry was merged.

**Synthesis:**
- The lessons Grep printed 65 lines, and `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 17 lines.
- `lesson-ship-docstring-sample-writes-a-real-case-number` shares its cause with `lesson-ship-test-comment-writes-a-bare-case-reference`: in both, the agent wrote a case number in the live code outside a bracket. I added 3 entries marked `librarian: synthesis`: the `create` of the new Insight and one `update` for each lesson setting `clustered`. The lesson entry carries no `addressed_by`, so the Insight was born `open`.
- `lesson-caseid-session-option-takes-the-hhmm` joined nothing. No line of either Grep shares its cause; the closest, `insight-caseid-printed-an-id-it-did-not-hold`, is about a different failure.

**Pages opened for the reasons named in my frame:**
- `vault/wiki/lessons/lesson-ship-test-comment-writes-a-bare-case-reference.md`, to check whether a lesson shares its root cause, and to get its status and tags. Outcome: the two lessons are clustered under the new Insight.
- No script named a page in an error, so I opened no archived page.

**Ledger read:** one `wc -l` of `vault/raw/2026-11-02/2155/ledger.md` gave 23 lines. The yaml holds lines 1–18 and 20–23, and line 19 is folded into the `create` of line 9, so every line is accounted for.

**Handoff instructions:**
- Every direct instruction was carried out by the scripts: the three `rule-case-build` items applied in ledger order, the renders of `case-guppi.md`, `case-schema.md`, `orchestration.md` and `.claude/settings.json` (with `guppi frontierguard` on `PreToolUse`), and the creation of `rule-frontier-hook` with `core: true`.
- `guppi sprint` wrote the milestone "The clean branch" `[x]` in `vault/wiki/sprint.md`.
- No instruction asked for a repair, and nothing was refused.

**Flags raised:**
- `near` on line 22, as above.
- From the handoff: `ask-guppi` ran more searches of code than its frame allows, in two sessions running.
- From the handoff: `claude plugin validate` printed `ICON_MISSING` on `prod-0.3.0`.
- The `shellwrite` hook reported that, during the move by `guppi archive`, it turned the CRLF line endings of `vault/archive/plugin/2026-11-02/0039/raw/report.md` into LF.
- A read my frame says my job does not need: a Grep of `vault/raw/2026-11-02/2155/spec.md` for `frontierguard`, beyond its unticked and ticked lines. The Next session part of the brief needed it, to see whether a Case of session 2155 adds a file that is no page of `vault/wiki/`. The handoff did not ask for it.
- Under `Cases` of Next session, the brief proposes to defer `estimate-orchestration-acknowledging-reply` into `backlog.md`, because the handoff lists it under Debt, as `rule-brief` sets for such a reading.
- No hook refused any of my calls. The scripts printed nothing on stderr.

**Lint total:** `guppi check` printed nothing and exited 0, so the total is 0.

Files: `c:\PROJECTS\GUPPI\vault\wiki\brief.md`, `c:\PROJECTS\GUPPI\vault\raw\2026-11-02\2155\materialize.yaml`
