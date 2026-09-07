---
session: YYYY-MM-DD
sprint: S0
commits: <first>..<last>          # or "none" if nothing was committed
---

# Handoff — YYYY-MM-DD

Anywhere below, a line beginning **owner:** is the owner's own testimony. It outranks the line
it stands beside, and whatever page it reaches earns `basis: human`.

Every section stays, always. An empty one is a legal answer — write "none". A dropped one is
knowledge that was never asked for, and nothing else in this repository looks inside `raw/`.

Each section names where `/ingest` files it. **That mapping lives here and nowhere else** — the
skill reads it rather than carrying a copy, because a copy drifts from what it copied and this
one drifted for three days as `section 7`.

## State
Done / not done / in flight / next step.
Checks: tests (how many), `ruff check`, `ruff format --check`, browser walk.
Never compiled into the wiki — it feeds the brief and dies with it.
→ ingest: `journal` — never compiled. State is a lie within a sprint; it feeds the brief and dies with it.

## Entities
Appeared | changed | taken out of service (and why).
Entities, not files — Docker, htmx, a module. Git records the files, and records them better.
→ ingest: `entities/`

## Decisions
What we chose | what we rejected | why | what it now obliges.
A divergence belongs here too: going against a written rule is a decision, with a date and a
rejected alternative — "obey the rule".
→ ingest: `decisions/`

## How it is built
Mechanisms understood or corrected. Invariants and their consequences.
→ ingest: `concepts/`

## Lessons
What burned us, and the incident that produced it. With the number, if there is one.
**If a `/pre-task` ran, its two counts belong here** — how many pages the shortlist named, and how
many the agent opened in full. The agent returns both and writes neither, nothing else records them,
and neither can be recovered afterwards; across runs they are the only evidence on whether phase 1
discards too much. **This is not the ledger drain**, which the owner cancelled on 2026-08-21: these
two numbers come out of the agent's answer, never out of `.superpowers/sdd/pre-task-ledger.tsv`.
→ ingest: `lessons/`

## Deferred
What we are not doing now | the consequence of not doing it.
→ ingest: `decisions/` for the deferral, **and `proposals/` as well** where a design sits behind it. One item routinely becomes two pages.

## Feedback to the librarian
Drained from `.superpowers/sdd/vault-feedback.md`, which the session no longer writes by hand: it
prints a fenced `VAULT-FEEDBACK` block in its reply and a `MessageDisplay` hook files it there.
→ ingest: `elsewhere:log.md`, filed under the kind each line names — `- miss:`, `- measure:` or `- decision:`. `- harness:` lines go to `Harness` below.

## Anything else worth keeping
A catch-all. Its units are `skip:` unless the librarian finds them a category — and if it fills
up repeatedly, the template is missing a section.
→ ingest: free-form. Its units are `skip:` unless a category is found for them.

## Harness
Changes to the files that instruct an agent — skills, hooks, `CLAUDE.md`, templates, the check —
decided this session. A work queue rather than an account of the session, which is why it stands
last. Drained from the marked lines of the same file.
→ ingest: `decisions/` for what was decided, `proposals/` for a design behind it, `elsewhere:<file>` for a bare work item that names the file to change.
