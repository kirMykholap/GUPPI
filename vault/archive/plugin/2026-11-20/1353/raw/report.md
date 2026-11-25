Librarian report for 2026-11-20, session 1353 (`vault/raw/2026-11-20/1353/handoff.md`)

All steps ran and the vault is committed as `bdd59900 docs(vault): librarian, 2026-11-20`. After the commit the tree is clean. No script failed, nothing was printed on stderr, and no hook refused a call.

**Pages created (16)**
- Decisions (11): `decision-case-1039`, `-1039.1`, `-1039.2`, `-1040`, `-1041`, `-1042`, `-1042.1`, `-1042.2`, `-1043`, `-1043.1`, `-1043.2`.
- Estimates (4):
  - `estimate-case-build-names-a-stale-line-of-another-case`, pending.
  - `estimate-plugin-install-asks-one-approval-in-plan-mode`, pending.
  - `estimate-clean-branch-prod-commits-only-a-tested-copy`, pending.
  - `estimate-guppi-repository-carries-the-mit-license`, passed. Its reading is ledger line 22, folded into its `create` entry.
- Lessons (1): `lesson-case-build-context-claims-a-run-it-did-not-make`, `new`.

**Pages updated (18)**
- Rules (7): `rule-case-build`, `rule-case-check`, `rule-clean-branch`, `rule-guppi-package`, `rule-orchestration`, `rule-plugin-install`, `rule-work-mode`.
- Estimates (6).
- Entities (2): `entity-guppi-repository`, `entity-sprint-plugin`.
- Insights (1): `insight-case-build-sibling-texts-unchecked-before-the-showing` went `open` → `actioned`, `addressed_by` `decision-case-1039.1`.
- Lessons (2): the two children of that Insight, archived by the cascade.
- Status changes by the cascade: `rule-clean-branch` `built` → `draft`; `rule-guppi-package` and `rule-work-mode` `draft` → `built`.
- `guppi generate` printed 34 pages for 1353 and 0 for 0807.

**Entries marked incomplete or failed:** none. The yaml has 33 `applied` (22 entries and 11 decisions), with `unparsed: []`.

**Pages archived**
- `guppi cleanup` moved 2 pages into `vault/archive/plugin/2026-11-23/1353/lessons/`:
  - `lesson-case-build-a-later-case-leaves-a-ratified-text-stale`
  - `lesson-orchestration-batch-asks-one-fork-twice-with-opposite-answers`
- `guppi archive` moved one unit: `raw/2026-11-04/0807 → archive/plugin/2026-11-04/0807/raw`.
- It kept two folders:
  - `raw/2026-11-20/1353`, because it is the session of this run.
  - `vault/raw/2026-10-14/1907/`, because it holds no `ledger.md`, so it is not a unit.

**Index check and synthesis**
- All four `create` entries are Estimates, so no category Grep ran for them.
- For the `lesson` entry I ran two Greps:
  - `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 70 lines. The output was saved to a file by the harness and I read that file.
  - `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 18 lines.
- Pages I opened because the index line did not settle same or near:
  - `vault/wiki/lessons/lesson-case-build-states-what-a-past-decision-did-from-its-effect-on-one-page.md`: close but not the same. I added `near:` with this slug to the entry for `lesson-case-build-context-claims-a-run-it-did-not-make`.
  - `vault/wiki/lessons/lesson-librarian-writes-a-total-no-count-printed.md`: not the same cause, not clustered.
  - `vault/wiki/insights/insight-case-build-claims-what-code-does-without-reading-it.md`: not the same pattern, not clustered.
- The synthesis added no entry, and the lesson stays `new`.

**Ledger read**
- I read `ledger.md` once: `wc -l` gives 23 lines, and I read line 22, the only line with no entry of its own.
- Line 22 is folded into the `create` entry of line 15, and `log.md` shows it applied as `#L22`.
- Every ledger line is accounted for.

**Handoff instructions**
- Spec taken as it stands: done.
- `.claude/agents/case-guppi.md` holds both changes to the Render of `rule-case-build`: one line with `as set in case 1039.2` and one with `and why you chose it (as set in case 1041)`.
- The Insight went `actioned`, and its two live children were archived.
- `backlog.md` gained the line from case 1043.2.
- The handoff asked for no repair.

**Flags raised (all in the brief)**
- The `near` mark on `lesson-case-build-context-claims-a-run-it-did-not-make`.
- 3 failed Estimates:
  - `estimate-ask-searches-at-prespec`, deferred by Case 1037.
  - `estimate-case-build-searches-the-names-of-what-it-changes`, deferred by Case 1038.
  - `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`, whose target is the live sprint page.
- `rule-clean-branch` went back to `draft`, so `sprint.md` shows the milestone The clean branch open again.
- The handoff's Debt says the first part of the method of two Estimates meets the Criterion, but no ledger line records either reading:
  - `estimate-case-build-offers-a-page-for-code-no-page-covers`
  - `estimate-clean-branch-prod-commits-only-a-tested-copy`
- A contradiction the handoff noted: the `given` of Case 1042.1 says "the two tests", while its `context`, `rule-clean-branch` and the Criterion name the two selections.
- Four handoff observations and notes:
  - The suite has not yet run on Linux.
  - The copy on `prod` carries no license text.
  - The quotes in `LICENSE` are ASCII where the opensource.org page shows typographic ones.
  - `README.md` and `LICENSE` are on the branch `plugin` only.
- No read was outside what my job needs, so there is no flag of that kind.

**Lint total:** `guppi check` exits 1 with 6 lines:
- `rule-ask`, `rule-case-build` and `rule-morph` are core pages that stand `draft`.
- The 3 failed Estimates above give `unread: failed`.

Brief: `c:\PROJECTS\GUPPI\vault\wiki\brief.md`
Yaml: `c:\PROJECTS\GUPPI\vault\raw\2026-11-20\1353\materialize.yaml`
