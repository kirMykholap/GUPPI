---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-hi]]"
purpose: Whether a session takes a conserved Spec of the Frontier whole — only with no decision line of its own but a defer, its line closed, the plan file created with a title line that names the conserved spec.md, the other lines closed as left
method: "uv run --project .guppi guppi render --check; by hand, a session whose person takes a conserved Spec at the Frontier: frontier.md, the title line of the plan file and the session's ledger read against the Criterion; and the /hi of the session after the close of a sprint: its frontier.md and backlog.md"
checked: 2026-10-10
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
In a session that `/hi` opened from `.claude/skills/hi/SKILL.md` as rendered from `rule-skill-hi`, the person takes a conserved Spec of `## Cases` of `raw/<date>/<hi HHMM>/frontier.md`.
**＋** Or `/hi` opens the session after the close of a sprint, while the first line of the `Cases` of Next session in `vault/wiki/brief.md` opens with `open the next sprint`.

Then:
In a session whose `/hi` found no first line `open the next sprint` in the `Cases` of Next session of `vault/wiki/brief.md`, the agent takes the Spec whole, to be run by `/box`, only while the session's ledger holds no decision line other than a `defer`, and after it ratifies no Case but a short-form defer.
**＋** In such a session it closes the line of that Spec `[x] … · work`.
**＋** It creates the plan file with one title line, `# Session <hi HHMM> — runs the conserved Spec vault/raw/<date>/<HHMM>/spec.md`, the path that `vault/wiki/backlog.md` names for that Spec.
**＋** It closes each other open line under `## Cases` as left — `[-] … · backlog · kept`, `[-] … · sprint · defer` or `[-] … · defer case N` — and goes on to `/pre-spec`.
**＋** A line whose target a `defer` item of that Spec puts off closes `[-] … · defer case N`, N being the Case of that Spec that holds the item, and the session writes no short-form Case and no ledger line for it.
**－** In the session that opens the next sprint no conserved Spec stands under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md`, and the agent takes none; each stays in `vault/wiki/backlog.md` for a later session.
**－** No other line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` closes `[x]`.
**－** No Case of the conserved Spec is built again or ratified again in the session that takes it.
**－** `.claude/skills/hi/SKILL.md` equals the Render of `rule-skill-hi` and is not edited by hand.

## Result

2026-10-10, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
