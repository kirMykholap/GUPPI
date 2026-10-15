---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-box]]"
purpose: Whether /box checks a conserved Spec, runs it on its own branch brought up to the shared branch by a fast-forward, merges the branch back by a fast-forward after the handoff, and has the librarian write the pages on the shared branch, stopping when the check or a merge refuses
method: "uv run --project .guppi guppi render --check; by hand, a session that takes a conserved Spec at the Frontier and runs it by /box: git log, the branches, the folders of the session and of the conserved Spec, the dispatch line and the librarian's commit, recorded in the estimate line"
checked: 2026-10-04
origin: raw/2026-10-02/1202/ledger.md#case-593.2
sprint: migration
created: 2026-10-02
tags: [session, workflow, git, harness]
---

## Criterion

When:
The agent calls `/box` on `PreToolUse Skill` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec, on the line that the hook of `rule-spec-capture` printed after `ExitPlanMode`, and runs `.claude/skills/box/SKILL.md` as rendered from `rule-spec-box`.

Then:
`uv run --project .guppi guppi render --check` exits 0: `.claude/skills/box/SKILL.md` equals the Render of `rule-spec-box`.
**＋** The agent first runs `uv run --project .guppi guppi box --check` on the folder; when it prints a line, the agent changes nothing, shows the lines and asks the person.
**＋** Otherwise the agent commits the tree, runs `git switch` to `spec/<date>-<HHMM>`, and brings that branch up to the branch it came from by `git merge --ff-only`; when the merge refuses, it switches back, shows the refusal and asks the person.
**＋** It calls `/work` with the folder, and Work Mode, the Work readings, `/retro` and `/handoff` run in one turn.
**＋** After `handoff.md` stands, it switches back, brings the branch it came from up to `spec/<date>-<HHMM>` by `git merge --ff-only`, deletes `spec/<date>-<HHMM>` by `git branch -d` and runs `uv run --project .guppi guppi test`; a merge that refuses is a stop.
**＋** Then it dispatches `librarian-guppi` with the path of the session's `handoff.md`, and shows the librarian's report unchanged with the exit code of `uv run --project .guppi guppi test`.
**－** Nothing under `vault/wiki/` is written on `spec/<date>-<HHMM>`, and the librarian runs once, on the branch the session came from.
**－** No commit follows the handoff but the librarian's own.

## Result

2026-10-04, at the /hi of session 0004: `uv run guppi render --check` exit 0; by hand, session 1416 (transcript 682b0e2f), which took the conserved Spec of raw/2026-10-03/1341/ at the Frontier: /box called at 14:37:13 with that folder on the line printed after ExitPlanMode; `uv run guppi box --check` printed nothing, exit 0; the agent committed the session folder as 3243a81d on `migration`, switched to `spec/2026-10-03-1341` and brought it up by `git merge --ff-only migration`, 9e0296ca..3243a81d; /work called with the folder at 14:37:26, and the Work readings, /retro and /handoff ran with no word of the person, the one Stop before the report, at 14:40:45, sending the agent on; after handoff.md at 14:41:19 it switched back, merged by `git merge --ff-only` 3243a81d..a67b0339, ran `git branch -d spec/2026-10-03-1341` and make test, exit 0, 1129 passed, 6 skipped; librarian-guppi dispatched once, at 14:41:51, with the path of raw/2026-10-03/1416/handoff.md, its report shown unchanged, 16 of 16 lines, with the exit code of make test; the commits of the Spec branch, bda8f3f4 and a67b0339, touch only vault/raw/, and the only commit after the handoff is the librarian's da671ebe on `migration`; not exercised: a line printed by the check, a merge that refuses

## History

- 2026-10-02 created · [[decision-case-593.2]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/0004/ledger.md#L3
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make test` → `uv run --project .guppi guppi test` · [[decision-case-820.7]]
