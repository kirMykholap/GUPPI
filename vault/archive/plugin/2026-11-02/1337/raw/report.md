Librarian, 2026-11-02, session 1337. The run finished and is committed as `2b0df617 docs(vault): librarian, 2026-11-02`. The tree is clean after the commit. `guppi check` exits 1 with 5 lines.

**Pages created (10):**
- decisions 6: `decision-case-1002`, `decision-case-1003`, `decision-case-1003.1` to `decision-case-1003.4`.
- estimates 1: `estimate-retro-loads-on-a-red-command` (`pending`).
- lessons 2: `lesson-work-skill-fails-to-load-on-a-red-check` (created, clustered, then archived in the same run) and `lesson-vs-code-extension-hands-the-skill-preamble-to-the-agent` (`new`).
- insights 1: `insight-harness-skill-refused-when-a-preamble-command-exits-non-zero`, from the synthesis. It was born `actioned` with `addressed_by: decision-case-1003.3`.

**Pages updated (20):**
- rules 8:
  - by Cases: `rule-orchestration` (1002), `rule-guppi-config` (1003.1), `rule-lint` (1003.2), `rule-work-mode` (1003.3), `rule-retro` (1003.4).
  - The cascade then set `rule-work-mode` and `rule-retro` from `built` to `draft`.
  - The cascade set `rule-clean-branch`, `rule-skill-approve-spec` and `rule-spec-box` from `draft` to `built`.
- estimates 11:
  - by readings: L1, L4, L5, L6 and L16 passed; L17 and L18 failed.
  - by Cases: `estimate-guppi-config-runs-the-test-and-style-commands` and `estimate-lint-runs-every-step`, both then passed (L19, L20); `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, now `pending`; `estimate-orchestration-acknowledging-reply`, only its `method` changed, still `failed`.
- lessons 1: `lesson-hi-fails-outside-a-git-repository`, `new` to `clustered`, then archived.

**Entries marked incomplete or failed:** none. No entry is marked `exists`, `near` or `merged`, and `unparsed: []`. All 25 entries (21 from materialize, 4 from the synthesis) and all 6 items of `decisions` carry `applied`.

**Pages archived (2):** `guppi cleanup` printed `2 page(s) moved`:
- `lesson-hi-fails-outside-a-git-repository`
- `lesson-work-skill-fails-to-load-on-a-red-check`

Both now stand in `vault/archive/plugin/2026-11-02/1337/lessons/`, moved because their Insight is `actioned`.

**Archive step:** `guppi archive` printed nothing, exited 0 and moved no unit. It kept:
- `raw/2026-11-02/0039` and `raw/2026-11-02/0254`, because they are dated the day of the run and only units dated before that day are looked at.
- `raw/2026-11-02/1337`, because it is the session of the run.
- `raw/2026-10-14/1907`, because it has no `ledger.md`, so it is not a unit.

**Index check:** the yaml has no `create` entry other than an Estimate, so I ran no Grep for it.

**Synthesis:**
- The Greps I ran:
  - `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 62 lines. The output was saved to a file and I read that file.
  - `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 15 lines.
- Page opened: `vault/wiki/lessons/lesson-hi-fails-outside-a-git-repository.md`. I read its Trigger and Root cause because its index line did not say whether it shares a root cause with L7, as the handoff asked me to check. Outcome: clustered. Its Trigger shows the same refusal, "Shell command failed for pattern".
- Result: a new Insight with both lessons as children. Because the lesson entry of L7 carries `addressed_by: decision-case-1003.3`, the Insight was born `actioned` and both lessons went to the archive.
- L21 was not clustered. No index line of either Grep names how a client runs a skill preamble.

**Ledger read:** I read `vault/raw/2026-11-02/1337/ledger.md` once, for the Work line. It has 21 lines, and the yaml holds entries for lines 1–21, so no line was left unapplied.

**Handoff instructions:**
- L7 and the hi lesson share a root cause, and they are clustered as described above.
- The cascade did set `rule-skill-approve-spec` to `built`. After the run, `guppi check` names two pages as `core: true` and `draft`: `rule-case-build` and `rule-orchestration`.
  - `rule-work-mode` and `rule-retro` also carry `core: true` and stand `draft`, but the check does not name them. The reason is `is_draft_core` in `.guppi/guppi/pages.py`: it leaves out a page whose History has a line that once set it `built`.
- The `replace` of Case 1003.1 on `rule-guppi-config` was applied.
- `estimate-orchestration-acknowledging-reply` stays `failed`.

No repair was asked for and none was refused.

**Flags I raised:**
- Three Estimates are `failed`: L17 `estimate-case-build-searches-the-names-of-what-it-changes`, L18 `estimate-case-build-reads-each-list-of-a-new-member`, and `estimate-orchestration-acknowledging-reply`.
- Defect, also a Cases line in the brief: Case 1003.3 changed only the Tests and Lint lines of `/work`, yet the Insight it closed sent `lesson-hi-fails-outside-a-git-repository` to the archive. Skill preamble lines that run `git` still stand in `work`, `box`, `carry` and `handoff`.
- `rule-work-mode` and `rule-retro` are `core: true` and `draft` after the cascade, and `guppi check` does not name them.
- I listed `estimate-synthesis-keeps-actioned-by-the-mark` under Work. I read this run as the event its `method` waits for, but the Insight was born `actioned` in this same run rather than standing `actioned` before it, so it is open to question.
- Reads my frame says the job does not need: none.
- No stderr line came from `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary` or `archive`. No unticked Spec line holds `guppi sprint-close --apply`. No hook refused any call.

**Lint total:** `guppi check` exits 1 with 5 lines:
- `status: a page with core: true that is draft` on `rule-case-build` and `rule-orchestration`.
- `unread: failed` on `estimate-case-build-reads-each-list-of-a-new-member`, `estimate-case-build-searches-the-names-of-what-it-changes` and `estimate-orchestration-acknowledging-reply`.

Files:
- C:\PROJECTS\GUPPI\vault\wiki\brief.md
- C:\PROJECTS\GUPPI\vault\raw\2026-11-02\1337\materialize.yaml
- C:\PROJECTS\GUPPI\vault\wiki\insights\insight-harness-skill-refused-when-a-preamble-command-exits-non-zero.md
