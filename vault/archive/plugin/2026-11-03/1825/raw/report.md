Librarian run for session 1825 (2026-11-03) is done and committed as 073dc852 `docs(vault): librarian, 2026-11-03`. The tree is clean after the commit.

**Pages created (9)**
- decisions 7: `decision-case-1019`, `decision-case-1019.1` to `decision-case-1019.4`, `decision-case-1020`, `decision-case-1021`
- estimates 2: `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` (`once: true`, `passed`) and `estimate-clean-branch-leaves-out-the-source-pictures` (`passed`)

**Pages updated (9)**
- rules 4:
  - `rule-skill-hi` (1019.1)
  - `rule-raw-archive` (1019.1)
  - `rule-clean-branch` (1020), then draft → built by the cascade
  - `rule-skill-sprint-open`, draft → built by the cascade
- estimates 4:
  - `estimate-hi-takes-its-readings` (1019.1, then passed by L12)
  - `estimate-case-build-reads-the-readers-of-a-new-files-folder` (1019.2, then passed by L13)
  - `estimate-skill-sprint-open-asks-the-opening-questions` (passed by L1)
  - `estimate-clean-branch-refuses-a-draft-core-page` (passed by L2)
- entities 1: `entity-sprint-plugin`. It gained an Estimate (1019.3), a `## Backlog` line (1019.4) and `deferred_by: ["[[decision-case-1021]]"]` (1021).

**Entries marked incomplete or failed:** none. Every entry carries `applied`. Line 10 (the defer of `entity-sprint-plugin`) carries `exists`. No entry is marked `near`, `librarian` or `merged`, and `unparsed: []`.

**Index check and synthesis:** no Grep ran.
- The yaml's only two creates are Estimates, which have no index check.
- The yaml holds no `lesson` entry, so the synthesis added no entry.

**Ledger read (the one read the frame names):** `vault/raw/2026-11-03/1825/ledger.md` has 15 lines. The yaml has entries for lines 1–13. Lines 14 and 15 are folded into the creates of lines 6 and 9. Every line is accounted for.

**Pages opened for the three reasons the frame names:** none.

**Archive:** `guppi archive` printed nothing on stdout or stderr and exited 0. No unit was moved and none was named as kept.
- The two sessions in `raw/` that have a ledger, 0316 and 1825, are both dated 2026-11-03. The script only looks at units dated before the day of the run.
- `vault/raw/2026-10-14/1907/` has no `ledger.md`, so it is not a unit.

**Refusals:** no hook refused a call. The handoff asked for no repair of an entry.

**Flags I raised**
- `vault/wiki/sprint.md` now marks the milestone The clean branch `[x]`. The handoff says the person put off C1, the clean branch, together with The plugin (Case 1021). The line under `## For the next session` covers it.
- `entity-sprint-plugin` is deferred by Case 1021 and is listed first under `## Deferred` of `backlog.md`, but it is still the live sprint page.
- The `old` text of the 1019.1 `replace` on `rule-raw-archive` runs across a line break in the page. A one-line Grep counted 0 matches. `generate` applied it with nothing on stderr, and the page now holds the new sentence.
- The handoff's own checks, as the pages now stand:
  - Both 1019.1 pairs on `rule-skill-hi` matched the page once each before `generate`.
  - `.claude/skills/hi/SKILL.md` renders the new step and the "do not open that chat" sentence.
  - `plugin/assets` is in `implementation_ref` of `rule-clean-branch`, and the folder holds both pictures.
- `generate` ticked two `read` boxes in `vault/raw/2026-11-03/0316/spec.md` (lines 618 and 720) and all 13 boxes of the 1825 `spec.md`.
- Taken from the handoff:
  - `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` passed on the agent's judgment about the root `.gitignore`.
  - `ask-guppi` ran searches outside its frame at `/pre-spec`.
  - `guppi frontierguard` refused one edit of C4.
- Next session, `Cases`: proposals to defer `estimate-morph-sets-up-the-project-at-the-first-hi`, `estimate-morph-takes-in-the-set-aside-files` and `estimate-git-context-offers-git-init` into `backlog.md`, as their Debt lines in the handoff require.
- Next session, `Work`: the readings of `estimate-ask-searches-at-prespec`, `estimate-prespec-finds-a-reader-of-a-new-files-folder` and `estimate-case-build-searches-the-names-of-what-it-changes`, whose events have come.
- One read outside the frame: a Grep for `sprint-close` over `vault/raw/2026-11-03/1825/spec.md` printed line 16, a Case context paragraph that is not an unticked line. Step 2 needed it to look for a task line that runs `guppi sprint-close --apply`. The handoff did not ask for it.

**Lint total:** `guppi check` prints 1 line and exits 1: `rules/rule-morph: status: a page with core: true that is draft`. The handoff calls it the baseline line that Case 1017.8 intends.

The new brief is at C:\PROJECTS\GUPPI\vault\wiki\brief.md.
