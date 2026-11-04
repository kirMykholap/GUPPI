Librarian run for session 0316 (2026-11-03) is finished and committed as `8e0a10f4 docs(vault): librarian, 2026-11-03`. The tree is clean after the commit.

**Pages created (25):**
- decisions 18: `decision-case-1014`, `1015`, `1015.1`, `1015.2`, `1016`, `1017`, `1017.1` to `1017.9`, `1018`, `1018.1`, `1018.2`
- rules 1: `rule-skill-setup`. It has `core: true`, and the cascade moved it from `draft` to `built`.
- estimates 4, each `passed` by a reading folded into its create:
  - `estimate-clean-branch-ships-the-plugin-icon`
  - `estimate-clean-branch-ships-the-setup-not-done`
  - `estimate-ledger-write-passes-every-line-before-the-setup`
  - `estimate-skill-setup-starts-at-hi`
- lessons 2: `lesson-case-build-crop-spec-ignores-the-alpha-channel` (`new`) and `lesson-orchestration-batch-asks-one-fork-twice-with-opposite-answers` (`clustered`)

**Pages updated (21):**
- rules 10: `rule-ask`, `rule-clean-branch`, `rule-guppi-config`, `rule-ledger-write`, `rule-skill-hi`, `rule-session-start`, `rule-morph`, `rule-skill-sprint-open`, `rule-orchestration`, `rule-git-context`
  - The cascade moved `rule-clean-branch`, `rule-skill-sprint-open` and `rule-git-context` from `built` to `draft`.
- estimates 9: `estimate-ask-searches-at-prespec`, `estimate-prespec-finds-a-reader-of-a-new-files-folder`, `estimate-morph-sets-up-the-project-at-the-first-hi`, `estimate-morph-takes-in-the-set-aside-files`, `estimate-skill-sprint-open-asks-the-opening-questions`, `estimate-orchestration-acknowledging-reply`, `estimate-clean-branch-refuses-a-draft-core-page`, `estimate-skill-sprint-open-asks-the-goal-as-an-open-question`, `estimate-git-context-offers-git-init`
- entities 1: `entity-sprint-plugin`
- insights 1: `insight-case-build-sibling-texts-unchecked-before-the-showing`

**Entries and marks:**
- No entry is marked `incomplete` or `failed`, and `unparsed` is empty.
- Line 1, the `defer` of `estimate-orchestration-acknowledging-reply`, carries `exists: true` from materialize.
- Line 12, the `create` of `rule-skill-setup`, carries `near: rule-morph`, set by me.
- Every entry carries `applied`.

**Ledger read (the one read):** `vault/raw/2026-11-03/0316/ledger.md` has 33 lines. The yaml has entries for lines 1–26 and 31–33. Lines 27–30 are folded into the creates of their Estimates (entry lines 6, 9, 11, 14). Every line is accounted for.

**Index check:**
- The Grep `^(purpose|deferred_by):` over `vault/wiki/rules/` printed 90 lines.
- `rule-skill-setup` is near `rule-morph`: `rule-morph` sets the setup Case, and `rule-skill-setup` governs the skill `/setup` that builds it. The index line and the entry's `governs` field settled this, so I opened no page.
- The four Estimate creates have no index check.

**Synthesis:**
- The Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 64 lines. Its output was too long to show, so I read it from the saved tool-result file.
- The Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 18 lines.
- `lesson-case-build-crop-spec-ignores-the-alpha-channel` has no pair and stays `new`.
- `lesson-orchestration-batch-asks-one-fork-twice-with-opposite-answers` joins `insight-case-build-sibling-texts-unchecked-before-the-showing`.
  - I opened `vault/wiki/insights/insight-case-build-sibling-texts-unchecked-before-the-showing.md` to settle whether the cause is the same and to take its children and status. Outcome: clustered.
  - The Insight stood `actioned` (`addressed_by: [[decision-case-872.1]]`) and the lesson carries no `addressed_by`. I appended an `update` with the three children and `status: open`, and an `update` of the lesson to `clustered`. Both are marked `librarian: synthesis`. The Insight's `addressed_by` stands, and its severity went from 0 to 1.

**Handoff instructions (all checks, none asked for a repair, none refused):**
- `estimate-orchestration-acknowledging-reply` holds the new Criterion and `method` from 1017.7, and keeps `deferred_by: [[decision-case-1014]]`.
- `rule-skill-sprint-open` holds the texts of both 1017.6 and 1018.1, applied in that order.
- `rule-clean-branch` holds the texts of both 1016 and 1017.1.
- `guppi.toml` holds `setup_done = true` after the render.

**Steps:**
- `guppi generate`: 46 pages for 0316, 0 for 2155, nothing on stderr.
- No unticked Spec line holds `guppi sprint-close --apply`.
- `guppi cleanup`: 0 pages moved.
- `guppi render`, `guppi sprint`, `guppi backlog` and `guppi glossary`: nothing on stderr.

**Archive:**
- Moved: `raw/2026-11-02/2155` → `archive/plugin/2026-11-02/2155/raw`. Nothing on stderr.
- Kept: `raw/2026-11-03/0316`, because it is the session of the run.
- No pending Estimate's `method` names the archive step, so no Readings due line took its output.
- No wiki pages were archived (cleanup moved 0).

**Flags:**
1. `near`: `rule-skill-setup` is near `rule-morph` (line 12).
2. Lint total, 1 line: `rules/rule-morph: status: a page with core: true that is draft`. The handoff says this is intended by 1017.8.
3. `rule-skill-setup` stands `built`, not `draft`. The cascade set it when L30 passed its one Estimate. The handoff expected both `rule-morph` and `rule-skill-setup` to be `draft` with `core: true`. Only `rule-morph` blocks the clean build.
4. The synthesis reopened `insight-case-build-sibling-texts-unchecked-before-the-showing`, from `actioned` to `open`.
5. Handoff observations, carried into the brief:
   - Case 1016's task text says the icon is padded with white, but the file has a transparent background.
   - Nobody has checked whether the field `icon` clears `ICON_MISSING`.
   - `ask-guppi` searched code beyond its frame for the third session running. The Render of Case 1015, which lifts that limit, landed in this run.
   - `guppi ship` does not take `guppi-assets/`.
6. No failed Estimate, MOC candidate, stale defer or contradiction was found.
7. I made no read that the frame says my job does not need.

**Brief:** `c:\PROJECTS\GUPPI\vault\wiki\brief.md` is rewritten. It lists 28 pending readings and no failed ones.
- Next session, Cases: 3 lines from the handoff's `## For the next session`.
- Next session, Work: `estimate-morph-sets-up-the-project-at-the-first-hi`, `estimate-morph-takes-in-the-set-aside-files`, `estimate-skill-sprint-open-asks-the-opening-questions`, `estimate-clean-branch-refuses-a-draft-core-page`, `estimate-git-context-offers-git-init`.
- Next session, Ask the person: none.

`guppi check` at the close: exit 1, with the one lint line above.

Files:
- `c:\PROJECTS\GUPPI\vault\raw\2026-11-03\0316\materialize.yaml`
- `c:\PROJECTS\GUPPI\vault\wiki\brief.md`
