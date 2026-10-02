---
type: estimate
kind: QA
status: pending
target: "[[rule-spec-box]]"
purpose: Whether /box checks a conserved Spec, runs it on its own branch brought up to the shared branch by a fast-forward, merges the branch back by a fast-forward after the handoff, and has the librarian write the pages on the shared branch, stopping when the check or a merge refuses
method: "uv run guppi render --check; by hand, the first session that takes a conserved Spec at the Frontier and runs it by /box: git log, the branches, the folders of the session and of the conserved Spec, the dispatch line and the librarian's commit, recorded in the estimate line"
origin: raw/2026-10-02/1202/ledger.md#case-593.2
sprint: migration
created: 2026-10-02
tags: [session, workflow, git, harness]
---

## Criterion

When:
The agent calls `/box` on `PreToolUse Skill` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec, on the line that the hook of `rule-spec-capture` printed after `ExitPlanMode`, and runs `.claude/skills/box/SKILL.md` as rendered from `rule-spec-box`.

Then:
`uv run guppi render --check` exits 0: `.claude/skills/box/SKILL.md` equals the Render of `rule-spec-box`.
**＋** The agent first runs `uv run guppi box --check` on the folder; when it prints a line, the agent changes nothing, shows the lines and asks the person.
**＋** Otherwise the agent commits the tree, runs `git switch` to `spec/<date>-<HHMM>`, and brings that branch up to the branch it came from by `git merge --ff-only`; when the merge refuses, it switches back, shows the refusal and asks the person.
**＋** It calls `/work` with the folder, and Work Mode, the Work readings, `/retro` and `/handoff` run in one turn.
**＋** After `handoff.md` stands, it switches back, brings the branch it came from up to `spec/<date>-<HHMM>` by `git merge --ff-only`, deletes `spec/<date>-<HHMM>` by `git branch -d` and runs `make test`; a merge that refuses is a stop.
**＋** Then it dispatches `librarian-guppi` with the path of the session's `handoff.md`, and shows the librarian's report unchanged with the exit code of `make test`.
**－** Nothing under `vault/wiki/` is written on `spec/<date>-<HHMM>`, and the librarian runs once, on the branch the session came from.
**－** No commit follows the handoff but the librarian's own.

## History

- 2026-10-02 created · [[decision-case-593.2]]
