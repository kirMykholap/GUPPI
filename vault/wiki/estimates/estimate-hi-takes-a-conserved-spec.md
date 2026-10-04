---
type: estimate
kind: QA
status: pending
target: "[[rule-skill-hi]]"
purpose: Whether a session takes a conserved Spec of the Frontier whole — only with no decision line of its own but a defer, its line closed, the plan file created with a title line that names the conserved spec.md, the other lines closed as left
method: "uv run guppi render --check; by hand, a session whose person takes a conserved Spec at the Frontier: frontier.md, the title line of the plan file and the session's ledger read against the Criterion; and the /hi of the session after the close of a sprint: its frontier.md and backlog.md"
checked: 2026-10-04
origin: raw/2026-10-02/1202/ledger.md#case-593.1
sprint: migration
created: 2026-10-02
tags: [session, workflow, harness]
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

2026-10-04, the Work readings of session 1934: `uv run guppi render --check` exit 0; by hand, the person took C1, the conserved Spec of raw/2026-10-04/1439/, at the Frontier: the session's ledger then held 3 estimate lines and no decision line, and after it the session wrote one lesson line and no decision line; frontier.md closes C1 `[x] … · backlog · work`, and the plan file magical-noodling-papert.md holds the one line `# Session 1934 — runs the conserved Spec vault/raw/2026-10-04/1439/spec.md`, the path backlog.md names; C2 and C3, items of the sprint, closed `[-] … · sprint · defer`, no other line under Cases closed `[x]`; /pre-spec ran next, `uv run guppi prespec --check` printed nothing, and the 12 findings of ask-guppi on Cases 627–629 went to the handoff, no Case of the conserved Spec built or ratified again; not exercised: a line whose target a defer item of the Spec puts off, closed `[-] … · defer case N`

## History

- 2026-10-02 created · [[decision-case-593.1]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-03 status: pending → failed · raw/2026-10-03/1416/ledger.md#L8
- 2026-10-04 updated: the Criterion replaced whole — a line put off by a defer of the conserved Spec closes defer case N with that Spec's Case · [[decision-case-620.1]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/1934/ledger.md#L5
- 2026-10-04 updated: the Criterion replaced whole — a session that does not open a sprint takes a conserved Spec as before; the session that opens the next sprint takes none (case 632.7) · [[decision-case-632.7]]
