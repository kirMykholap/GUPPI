---
session: 2026-08-13
sprint: S0
commits: 2620998..HEAD
---

# Handoff — 2026-08-13

The second brain, phase 1. Design, plan, and tasks 1–4 of 10.

## 1. State

**Done.** Spec and plan written and committed to `main`. Branch `feature/second-brain` carries:

- **Task 1** — the vault: layout, schema (`CLAUDE.md`), `index.md`, `tags.md`, `log.md`, and
  `scripts/vault-check.sh`.
- **Task 2** — `decisions/` and `concepts/` compiled from `docs/HANDOFF.md` and `CLAUDE.md`.
- **Task 3** — `lessons/` and `entities/`.
- **Task 4** — `.claude/agents/vault-librarian.md`, `.claude/skills/vault-ask/`, and the acceptance
  questions, **all four passing**.
- Out of plan order: the old `docs/HANDOFF.md` copied whole into `raw/handoffs/`, the ingest
  redefined as units and verdicts, and `raw/handoffs/TEMPLATE.md`, which is the first half of task 5.

**Not done.** Tasks 5 (the `/handoff` skill), 6 (`/ingest` and the brief), 7 (the `SessionStart`
hook), 8 (`/pre-task` and the guard), 9 (`/lint`, the sprint record, the growth signal), 10 (retiring
`docs/HANDOFF.md` and shrinking `CLAUDE.md`).

**In flight.** Nothing. Every commit is on the branch and the working tree is clean.

**Next step.** Task 5, then 6 and 7 — those three together are what makes the vault arrive by
itself. **Until task 7 nothing loads the vault automatically**, so a new session still reads the old
129 KB handoff and must be told to ask.

**Checks.** `bash scripts/vault-check.sh` — clean; 8 rules, each verified by removal. **The Python
suite was not run and did not need to be: no task touched `src/` or `tests/`.** `ruff` likewise
untouched.

## 2. Entities

**Appeared.** `vault-librarian` (agent) and `vault-ask` (skill); `scripts/vault-check.sh`,
`vault-units.sh`, `vault-coverage.sh`; the vault directory itself, renamed four times by the owner
and now `job_hunt_ai_vault/` — Obsidian displays the folder name, so it is his to choose and no
script may depend on it.

**Changed.** `.gitignore` now ignores `.obsidian/`.

**Out of service.** None.

## 3. Decisions

- **Ingest is units with verdicts, not "read and file"** — the owner's, and the most consequential
  of the session. "Fully processed?" must be answerable mechanically, on any document. Rejected:
  the previous definition, which only worked on documents written to our own template.
- **Coverage and fidelity are separate checks.** Coverage is free and mandatory; fidelity needs
  sampling or known answers.
- **Vectors are deferred, not rejected** — reframed mid-session after the owner objected that the
  first draft undersold them. Two claims in that draft were wrong and are recorded as corrections.
- **The librarian writes the vault unattended**; detection replaces permission, made real by git,
  by never deleting text, and by refusing to resolve contradictions.
- **Sprints close on their goal, not on an empty backlog**, and the growth alarm measures the brief
  rather than a proxy. Its threshold is to be **measured in sprint 1**, not set now.

## 4. How it is built

Compiled into the vault, 60 pages. The load-bearing shapes: three artefacts with three owners
(journal / vault / brief, and the brief is never a source); one librarian with two entry points; a
map rather than a catalogue, because retrieval is grep plus links; and a tag dictionary whose
aliases are how a Russian question reaches an English page.

## 5. Lessons

**Six times in one session a check passed for the wrong reason.** The htmx invariant satisfied by
prose in a script comment; the link check satisfied by its own schema examples; the same check
satisfied by inline code; `VAULT-CHECK: ok` printed after an unquoted `$(find)` word-split a path
containing a space and read nothing; a **0-byte file** satisfying a wikilink to a page that did not
exist; and orphan pages regressing from 7 to 11 inside the wave that was fixing them.

**Every one of them is now a rule in `vault-check.sh`, and every rule was verified by removal.**
The orphan rule caught the next page written, within a minute. That is the difference between a
rule and an intention.

**The migration committed the exact failure the vault exists to prevent.** `docs/HANDOFF.md` carried
two versions of the post-collection chain, the superseded one earlier in the file; the first pass
copied the first it met and the page then contradicted its own second half.

**A measurement travels with the class of work it was taken on.** The 5–35 minute round-trip figure
was applied to a retrieval agent, overstating it by two orders of magnitude.

## 6. Deferred

- **The coverage sidecar for `docs/HANDOFF.md`** — 245 units needing a verdict each. **This is the
  gate for task 10**: do not retire the file while any unit lacks one.
- **Vectors** — see the miss log for the evidence that would reopen it. One data point so far, and
  it was closed by a dictionary entry.
- **Beads** — the brief's "active tasks" section stays empty until it exists.
- **The AST test pinning the JavaScript boundary** — owed since 2026-08-12, still unwritten.

## 7. Feedback to the librarian

- **The first recorded miss is in `log.md` and is word-shaped**: no alias reached the JavaScript and
  React pages, and two Russian questions landed only because English words appear in filenames.
  Closed the same day by the `frontend` tag.
- **Q5 of the acceptance questions is still the owner's to write.** The four that exist were drafted
  by the party that already knew the corpus.
- **The acceptance run was a proxy.** `.claude/agents/` is read at session start, so the librarian
  could not be dispatched by name; a general agent was told to read its definition instead. **The
  corpus and the instructions are tested; registration is not.** The first real use is
  `/vault-ask <question>` in a fresh session.
- Gaps the librarian itself reported, which no reviewer had found: no test guards the one-finaliser
  rule; the 5-minute lower bound of the round-trip range has no named instance; reviewer trips are
  unmeasured; the 2026-08-11 recalibration has no post-hoc confirmation.

## 8. Anything else worth keeping

The owner asked twice, in different words, how any of this could be checked — and was right both
times. Both questions changed the design: the first produced the coverage script, the second
produced the units-and-verdicts definition of ingest. **The session's two best design decisions came
from his scepticism rather than from the plan.**
