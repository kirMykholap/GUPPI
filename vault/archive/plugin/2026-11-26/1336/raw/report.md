Librarian run, 2026-11-26, session 1336. Committed as c9677ff7 `docs(vault): librarian, 2026-11-26`. After the commit, `git status` shows a clean tree.

**Pages created**
- decisions: 5 (`decision-case-1064` to `decision-case-1068`)
- estimates: 1 (`estimate-orchestration-leaves-the-number-to-case-guppi`, pending)
- lessons: 1 (`lesson-frontier-line-closed-in-two-changes-through-bash`, clustered)

**Pages updated**
- rules: 2
  - `rule-orchestration`, by 1064 then 1066. It is draft.
  - `rule-backlog`, by 1067. It is built.
- estimates: 4
  - `estimate-orchestration-dispatches-case-guppi-at-a-level`: failed by L1, then pending by 1064.
  - `estimate-case-build-settles-form-by-itself`: failed by L2, pending by 1065, then passed by L13.
  - `estimate-backlog-renders`: passed by L12.
  - `estimate-sprint-plugin-readme-describes-the-project`: passed by L3.
- entities: 1 (`entity-guppi-repository`, `deferred_by` set to `decision-case-1068`)
- insights: 1 (`insight-orchestration-frontier-closer-leaves-the-box-open`, by the synthesis)

**Entries marked incomplete or failed:** none. All 16 entries carry `applied`. No entry is `near` and nothing is `unparsed`. The defer entry of line 11 carries `exists: true`, set by materialize.

**Ledger read (for the Work line of the brief):** `vault/raw/2026-11-26/1336/ledger.md` has 14 lines (`wc -l`). The yaml holds entries for lines 1 to 14, so it accounts for every line.

**Index check:** the only `create` entry is an Estimate, so no Grep of a category ran for it, and the index check made no yaml edit.

**Synthesis**
- Greps:
  - `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 73 lines. The output was saved to a tool-results file, and I read that file.
  - `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 19 lines.
- Pages opened because an index line did not settle the root cause:
  - `vault/wiki/insights/insight-orchestration-frontier-closer-leaves-the-box-open.md`. Its Pattern was the same cause: the box and the closer of one Frontier line written in two changes. Outcome: clustered.
    - I added an `update` of the Insight: the new lesson added to its `children`, and `status: open`. It had stood actioned by `decision-case-1012`, and its `addressed_by` stands.
    - I added an `update` of the lesson: `clustered` under that Insight.
  - `vault/wiki/lessons/lesson-work-mode-edited-a-source-file-through-the-shell.md`. It is about a shell edit of a source file and different hooks. Outcome: not clustered.
- I added 2 yaml entries, both marked `librarian: synthesis`.

**Handoff instructions**
- The three replace anchors of 1064 and 1066 in `rule-orchestration` each hit once (Grep `-o` printed lines 39, 43, 43). `log.md` shows 1064 applied before 1066.
- `log.md` shows the readings and updates applied in ledger order.
- `guppi backlog` dropped `rule-work-mode` and added `entity-guppi-repository`.
- The 1068 defer is on `entity-guppi-repository`.
- No instruction asked to repair an entry, so I refused none.

**Pages archived:** cleanup moved 0 pages. `guppi archive` moved `raw/2026-11-25/2003` to `archive/plugin/2026-11-25/2003/raw`. It kept `raw/2026-11-26/1336` because that is the session of this run.

**Flags I raised**
- The synthesis moved `insight-orchestration-frontier-closer-leaves-the-box-open` from actioned back to open (severity 1), so it is in `backlog.md` now.
- `backlog.md` counts 11 items. The handoff's two moves give 10; the extra item is the reopened Insight.
- The handoff's expected red, `guppi backlog --check`, no longer prints.
- Handoff note: Case 1064 gives no `update` to `estimate-sprint-plugin-case-guppi-level-trial-decided`, and `ask-guppi` accepted the reason.
- Handoff observation: session 2003 still has an empty `cases/case-1062.md`.
- No step printed anything on stderr: generate, cleanup, render, sprint, backlog, glossary, archive.
- No hook refused any call.
- I made no read that the frame says my job does not need.

**Lint total:** `guppi check` exited 0 and printed no line, both before and after the archive.
