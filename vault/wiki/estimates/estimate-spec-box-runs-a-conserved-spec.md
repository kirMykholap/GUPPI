---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-box]]"
purpose: Whether /box checks a conserved Spec, runs it on its own branch brought up to the shared branch by a fast-forward, merges the branch back by a fast-forward after the handoff, has the librarian write the pages on the shared branch, and shows report.md and commits it alone after the librarian's commit, stopping when the check or a merge refuses
method: "uv run --project .guppi guppi render --check; by hand, after the librarian's run that applies the update of rule-spec-box pointing to the Backlog of entity-sprint-plugin and renders .claude/skills/box/SKILL.md: on a copy of the repository, one session saves a small Spec by /carry and a second session takes it at its Frontier and runs it by /box; git log, the branches, the folders of that session and of the conserved Spec, the librarian's commit and the commit of report.md read in the copy, and the dispatch line and the text shown to the person read in the transcript of the second session under ~/.claude/projects/, recorded in the estimate line with that transcript named"
checked: 2026-11-02
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
**＋** Then it dispatches `librarian-guppi` with the path of the session's `handoff.md`, shows the text of `vault/raw/<hi date>/<hi HHMM>/report.md` unchanged, or, when no `report.md` stands there, the returned report unchanged and one line that says that `report.md` is missing, and then the exit code of `uv run --project .guppi guppi test`.
**＋** When `report.md` stands, it commits it alone, in one commit after the librarian's, with the message `docs(vault): librarian report, <hi date>`, and never with `--amend`.
**－** Nothing under `vault/wiki/` is written on `spec/<date>-<HHMM>`, and the librarian runs once, on the branch the session came from.
**－** No commit follows the handoff but the librarian's and the commit of `report.md`.

## Result

2026-11-02, guppi render --check at the /hi of session 1337: exit 0; the person's trial, session 1429 of the clone C:\PROJECTS\GUPPI-trial (transcript 21f5559f) took the conserved Spec of 1412, a Spec of two short-form defers, Cases 1002–1003, with no task, and ran it by /box; git log of the clone: the session commits, the handoff, then docs(vault): librarian and docs(vault): librarian report as the last commit alone; git branch shows plugin alone, the spec branch deleted; the person found the report right; /work did not load as a skill, see lesson-work-skill-fails-to-load-on-a-red-check, and the agent ran Work Mode by the text of its SKILL.md in the same turn

## History

- 2026-10-02 created · [[decision-case-593.2]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/0004/ledger.md#L3
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make test` → `uv run --project .guppi guppi test` · [[decision-case-820.7]]
- 2026-10-31 updated: the Criterion replaced whole — /box shows report.md and commits it alone · [[decision-case-956.4]]
- 2026-11-01 updated: method: a trial run of /box on a copy of the repository, after the librarian's run that renders the skill · [[decision-case-989]]
- 2026-11-02 status: pending → passed · raw/2026-11-02/1337/ledger.md#L6
