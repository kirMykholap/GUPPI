Librarian report, 2026-11-04, session 0807 (run 2026-11-20). Committed as `428dc383 docs(vault): librarian, 2026-11-04`. After the commit, `git status` printed nothing.

**Pages created (39, from `git status`)**
- decisions: 29
- estimates: 7
- lessons: 3

**Pages updated (37)**
- estimates: 17
- rules: 18
- entities: 1 (`entity-sprint-plugin`)
- insights: 1 (`insight-case-build-sibling-texts-unchecked-before-the-showing`)

Besides these, `decision-case-1008` was superseded by 1034.2 and archived. `rule-guppi-package` went `built` → `draft` by the cascade.

**Entries marked incomplete or failed:** none. All 58 entries carry `applied`: the 56 that `guppi materialize` wrote and the 2 the synthesis added. The two defers (1037, 1038) also carry `exists`. `unparsed: []`.

**Pages archived**
- `guppi cleanup` moved `decision-case-1008` (superseded) to `vault/archive/plugin/2026-11-20/0807/decisions/`.
- `guppi archive` printed one line on stdout, exit 0: `raw/2026-11-04/0358 → archive/plugin/2026-11-04/0358/raw`.
- It kept `raw/2026-11-04/0807`, the session of the run. `vault/raw/2026-10-14/1907/` holds no `ledger.md`, so it is no unit.
- I ran `guppi archive` before writing the brief rather than after; the brief carries its output. No `pending` Estimate's `method` names the archive step.

**Index check:** the seven `create` entries are all Estimates, so no category Grep ran and no entry was merged or marked `near`.

**Synthesis**
- Greps:
  - `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 68 lines. The output was too long to show; the harness saved it to a file, and I read that file.
  - `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 18 lines.
- `lesson-case-build-a-later-case-leaves-a-ratified-text-stale` joined `insight-case-build-sibling-texts-unchecked-before-the-showing`. I added two `update` entries marked `librarian: synthesis`: the Insight gains the child, and the lesson is set `clustered`. The Insight stays `open`, and its `addressed_by` stands.
- `lesson-session-background-agent-stopped-at-process-end` and `lesson-harness-empty-grep-taken-as-absence` have no pair and stay `new`.

**Pages opened for the synthesis**
- `vault/wiki/insights/insight-case-build-sibling-texts-unchecked-before-the-showing.md`: opened to check whether the lesson of L60 shares its pattern, and for the Insight's `status` and `children`. Outcome: clustered.
- `vault/wiki/lessons/lesson-grep-glob-brace-list-of-paths-matches-nothing.md`: opened because its index line did not settle whether it shares the root cause of L59. Outcome: not clustered. It names a fact of the tool (why a brace list of paths matches nothing), while L59 names an unchecked claim of absence.

**The read of `ledger.md`:** `wc -l` gives 60 lines. The yaml holds entries for lines 1–44, 47, 49–53 and 55–60. Lines 45, 46, 48 and 54 are readings folded into the `create` entries of their Estimates, and `log.md` shows each one applied. Every line is accounted for.

**Handoff instructions (what the run found)**
1. `estimate-case-build-writes-the-case` and `estimate-case-build-settles-form-by-itself` share no line. Where the first speaks of a change asked on a Case, or of a fix that adds a second behaviour, it points to the second. Both say the ratified file stays as it is, but under different conditions: the first for a new Case in Work Mode with `{supersedes:…}`, the second for a new Case beside a ratified one with no such mark.
2. After the render, `guppi render --check` exited 0 and `test_every_hook_command_runs_the_code_from_the_project_folder` passed (1 test). All 16 commands in `.claude/settings.json` name `${CLAUDE_PROJECT_DIR}/.guppi`, and none names `--project .guppi`. The hook in the frontmatter of `.claude/agents/librarian-guppi.md` names it too.
3. `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` left `backlog.md`.
4. The update of `estimate-clean-branch-writes-the-session-files` changed only its `method`. Its `status: passed` and its Criterion stand.
5. I did not read `agents-baseline.md`; the instruction about it only describes the file.

No instruction of the handoff asked to repair an entry.

**Flags raised**
- 4 failed Estimates:
  - `estimate-case-build-offers-a-page-for-code-no-page-covers` (L57)
  - `estimate-ask-searches-at-prespec` (deferred by 1037)
  - `estimate-case-build-searches-the-names-of-what-it-changes` (deferred by 1038)
  - `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` (targets the live sprint page)
- The cascade set `rule-guppi-package` to `draft`.
- `guppi materialize` printed `60 entries` for a yaml that holds 56 entries; the 4 folded readings make up the difference.
- The handoff's observations are listed in the brief.
- A Bash hook (`bashguard`) refused a heredoc that wrote a script to the scratchpad. As it said, I wrote the script with the Write tool instead.
- No script printed anything on stderr. No MOC candidate, no stale defer, no contradiction.
- No read outside the frame was needed.

**Lint total:** `guppi check` exit 1, 7 lines:
- 3 core rules stand `draft`: `rule-ask`, `rule-case-build`, `rule-morph`.
- 4 Estimates are `unread: failed`.

Brief: `c:\PROJECTS\GUPPI\vault\wiki\brief.md`. Yaml: `c:\PROJECTS\GUPPI\vault\raw\2026-11-04\0807\materialize.yaml`.
