Librarian report, 2026-11-26, session 1515. The run finished and is committed as `4bc899cf docs(vault): librarian, 2026-11-26`. After the commit `git status` prints nothing.

**Pages created, by category**
- decisions: 14 (`decision-case-1069`, `1069.1`, `1069.2`, `1070`, `1070.1` to `1070.7`, `1071`, `1071.1`, `1071.2`).
- estimates: 7.
  - `passed`: `estimate-frontier-hook-refuses-a-shell-command-on-the-frontier`, `estimate-case-protocol-splits-a-transcript-reading`, `estimate-prespec-hook-reports-a-method-that-reads-a-transcript`.
  - `pending`: `estimate-guppi-config-fills-the-main-branch`, `estimate-sprint-plugin-skills-name-the-main-branch-by-its-setting`, `estimate-sprint-plugin-vault-writer-texts-name-the-main-branch`, `estimate-sprint-plugin-setup-takes-a-main-branch-other-than-main`.

**Pages updated, by category**
- rules: 17. `rule-guppi-config` went `built → draft` by the cascade.
- estimates: 6. Three had their Criterion replaced and are now `passed`; three had one part changed and kept their status.
- entities: 2 (`entity-sprint-plugin`, `entity-glossary`).
- insights: 1. `insight-orchestration-frontier-closer-leaves-the-box-open` is now `actioned`, `addressed_by` `decision-case-1069.1`.
- lessons: none.

**Entries marked incomplete or failed:** none.
- All 51 entries carry `applied`: 37 under `entries`, 14 under `decisions`.
- No entry is marked `exists`, `near` or `librarian`, and `unparsed: []`.

**Pages archived**
- `guppi cleanup` moved 1 page: `lesson-frontier-line-closed-in-two-changes-through-bash`, to `vault/archive/plugin/2026-11-26/1515/lessons/`. It went by the cascade of its Insight being set `actioned`.
- `guppi archive` printed nothing and moved no unit, so nothing it kept has a printed reason.
  - It kept `raw/2026-11-26/1515` because that is the session of the run.
  - It kept `raw/2026-11-26/1336` because it is of today's date, which `sweep` in `.guppi/guppi/archive.py` (line 150) passes over without a line.

**Reads**
- Ledger: one read of `vault/raw/2026-11-26/1515/ledger.md`, for the `Work` line. It has 40 lines.
  - The yaml has entries for lines 1 to 34 and 36 to 38.
  - Lines 35, 39 and 40 are folded into the `create` entries of their Estimates.
  - So every line is accounted for.
- No page opened for a reason that must be named here: no same-or-near check, no shared root cause, no script error.
- One Grep output was saved to a file because it was too long; I read that file: `C:\Users\kir\.claude\projects\c--PROJECTS-GUPPI\86f6e9ab-3ce6-47ac-b6b5-c5e6f1340992\tool-results\toolu_01LaRFFivt5bJgNvytYwiS8Z.txt`.

**Index check and synthesis**
- Index check: every `create` entry is an Estimate, so no Grep of a category ran and the yaml was not edited.
- Synthesis Greps: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 74 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 19 lines.
- The yaml has no `lesson` entry, so the synthesis added nothing.

**Handoff instructions:** all four checked; none asked for a repair.
- Both `## Backlog` pairs of `entity-sprint-plugin` applied. The line from 1070.3 is under `## Closed`, and `## Backlog` has no blank line between items.
- The render filled `{{main_branch}}` with `main`. `guppi.toml` holds `main_branch = "main"`, no rendered file holds the placeholder, and `guppi render --check` exited 0.
- The Insight is `actioned` with `decision-case-1069.1`, as asked.
- `.claude/settings.json` now runs `guppi frontierguard` on Bash and PowerShell. My commit message does not name the Frontier file.

**Flags I raised**
- Handoff note: two lines of Case 1070.6 (its `context` and `given`) speak of the `purpose` only, although the sub-case also gives a new `method`. `ask-guppi` judged this harmless.
- Handoff observation: the three updates of Case 1070.6 set no status, so Retro did not read them. The handoff says `estimate-clean-branch-ships-neutral-texts` covers them.
- From the next session on, any shell command that names the Frontier file is refused, commit messages included.
- No MOC candidate, stale defer or contradiction was found.
- No hook refused a call of mine. I made no read that this frame says my job does not need.

**Lint total:** `guppi check` exited 0 and printed no line, both before the brief and at the close.

**Brief, Next session**
- Cases: sprint item C1, `rule-clean-branch`.
- Work:
  - `estimate-guppi-config-fills-the-main-branch`: its event is this run.
  - `estimate-orchestration-dispatches-case-guppi-at-a-level`: its event is session 1515, which ran with `orchestration.md` from commit `c9677ff7`.
  - `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec`: its event is the re-ratification after `/pre-spec`, from the handoff.
  - The last two are my own reading of whether their event happened. Both methods read a session transcript, which `/hi` may not open, so these lines may stay open from session to session.
- Ask the person: none.

The brief is `c:\PROJECTS\GUPPI\vault\wiki\brief.md`.
