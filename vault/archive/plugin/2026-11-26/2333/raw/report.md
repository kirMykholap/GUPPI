Librarian run for session 2333 (2026-11-26) is done and committed as `ddf961b3` ("docs(vault): librarian, 2026-11-26"). The tree is clean after the commit.

**Commands.** materialize exited 0. It wrote `vault/raw/2026-11-26/2333/materialize.yaml` with 11 entries and extended the yaml of 1336 and of 1515 with 0 entries each. generate printed 23 pages written or changed for 2333 and 0 for 1336 and 1515. No unticked Spec line holds `guppi sprint-close --apply`, so no close ran. cleanup printed `5 page(s) moved`. render, sprint, backlog and glossary printed nothing on stderr. The render changed no file.

**Pages created, per category:**
- decisions 6: `decision-case-1072`, `1072.1`, `1072.2`, `1073`, `1074`, `1075`.
- estimates 3:
  - `estimate-sprint-plugin-retro-loads-in-the-cli`, pending
  - `estimate-guppi-repository-readme-shows-the-path-of-a-decision`, pending
  - `estimate-sprint-plugin-plugin-milestone-holds-the-merge-and-the-close`, passed

**Pages updated, per category:**
- estimates 4:
  - `estimate-guppi-config-fills-the-main-branch`, passed
  - `estimate-orchestration-dispatches-case-guppi-at-a-level`, passed
  - `estimate-retro-loads-on-a-red-command`: `purpose`, `method` and Criterion replaced, defer of 1007 cleared, passed
  - `estimate-synthesis-keeps-actioned-by-the-mark`: passed by the person's decision, defer of 1009 cleared
- entities 2:
  - `entity-guppi-repository`: defer of 1068 cleared; the cascade set it `built → draft`
  - `entity-sprint-plugin`: milestone The plugin and `## Closed` changed, defers of 1021 and 1050 cleared
- rules 3, each set `draft → built` by the cascade: `rule-guppi-config`, `rule-retro`, `rule-synthesis`.
- No lesson or insight was created or updated.

**Entries marked incomplete or failed:** none. All 10 entries and all 6 decisions carry `applied`. None is marked `exists`, `near`, `librarian` or `merged`, and `unparsed: []`.

**Pages archived:**
- By cleanup: `decision-case-1007`, `1009`, `1021`, `1050` and `1068` (all superseded) moved to `vault/archive/plugin/2026-11-27/2333/decisions/`.
- By `guppi archive`, units moved: `raw/2026-11-26/1336` → `archive/plugin/2026-11-26/1336/raw` and `raw/2026-11-26/1515` → `archive/plugin/2026-11-26/1515/raw`. Nothing on stderr.
- Units kept: `raw/2026-11-26/2333`, because it is the session of the run.
- No pending Estimate's `method` names the archive step.

**Index check and synthesis:**
- Every `create` entry is an Estimate, so no category Grep ran for the index check. I made no yaml edit.
- Synthesis Greps: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 73 lines, and `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 19 lines. The yaml holds no `lesson` entry, so I added no entry.
- No page was opened for a same-or-near question, for a shared root cause, or for a script error.

**Ledger read (the one named read):** `vault/raw/2026-11-26/2333/ledger.md` has 11 lines. The yaml has entries for lines 1 to 10. Line 11 is folded into the `create` entry of `estimate-sprint-plugin-plugin-milestone-holds-the-merge-and-the-close`, so every line is accounted for.

**Handoff instructions, checked:**
1. The update of `entity-sprint-plugin` applied. The milestone The plugin now holds the merge line and then the close line. `## Closed` holds the line of Case 1070 before the three new lines of Case 1075.
2. `backlog.md` went from 8 items to 4. `rule-ratification` and the three plain lines stay.
3. `rule-synthesis` stands `built` by the cascade.
4. The ledger holds each decision line once.
No handoff instruction asked for a repair, and none asked for a read outside my frame.

**Flags raised (in the brief):**
- Handoff observation: frontierguard refused two Edits of `frontier.md`.
- Handoff observation: `guppi prespec --check` printed five `note:` lines on Case 1072.
- Handoff note: the event of `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` did not stand in session 1515.
- Handoff note: the `recommend` of Case 1074 still says "at the Retro of this session".
- No MOC candidate, stale defer or contradiction was printed.
- I made no read that my frame says the job does not need.
- No hook refused a call.

**Next session in the brief:**
- Cases: C1 `rule-clean-branch` (from the handoff).
- Work: two readings whose events I saw this run.
  - `estimate-case-build-names-a-stale-line-of-another-case`: the `context` of Case 1072.1 says the check of its file also named `case-1073.md`.
  - `estimate-orchestration-leaves-the-number-to-case-guppi`: Cases 1072 to 1074 were ratified twice, after `/pre-spec`.
- Ask the person: `estimate-guppi-repository-readme-shows-the-path-of-a-decision`.

**Lint total:** `guppi check` exit 0, no line.

Brief: `c:\PROJECTS\GUPPI\vault\wiki\brief.md`
