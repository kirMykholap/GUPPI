# Vault methodology — reading order

A governance system for agent-assisted development. The atomic unit is a **Decision**
ratified by a human; nothing reaches the codebase or the vault without one.

## Read in this order

1. **`index.md`** — what the vault is made of and the rules that hold in every phase.
   Start here.
2. **`glossary.md`** — every term, precisely. Consult while reading the rest.
3. **`case-schema.md`** — the Case, the unit of dialogue where content gets ratified.
4. **Page schemas** — `decision-`, `entity-`, `rule-`, `estimate-`, `lesson-`,
   `insight-schema.md`. One per category: properties, body, history, worked examples.
5. **`moc/`** — the session workflow, one Rule MOC per phase. Read in session order:
   `rule-session-start` → `rule-plan-mode` → `rule-work-mode` → `rule-subagent-guppi` →
   `rule-end-of-work` → `rule-documentation`.
6. **`migration-plan.md`** — the one-time conversion of an existing vault. Read last, and
   only when doing that work.

**`superseded/`** holds earlier drafts. They contradict the current model. Do not read them
as instructions.

## Which file is authoritative for what

The split matters, because several things could plausibly live in two places:

| Question | Answer lives in |
|---|---|
| What page categories exist, what fields they have | the page schemas |
| What the vault directory structure is | `index.md` §1 |
| How a decision routes to a page | `index.md` §5 |
| When to split something into children | `index.md` §6 |
| How a session actually runs, step by step | `moc/` — **not** `index.md` |
| What a term means | `glossary.md` |

`index.md` deliberately does **not** describe the session workflow. That lives in the Rule
MOCs, which are simultaneously the documentation and, through `enforcement: render`, the
harness itself. Duplicating it would create two sources that drift apart.

## The five ideas everything else follows from

**1. Decision is the atomic unit.** Every agent action traces to a decision a human
explicitly ratified. The bottleneck in agent-assisted development is no longer writing code
— it is understanding and verifying what the agent did. This is the mechanism that keeps
that visible.

**2. Decisions govern contracts, not implementations.** Ratification happens at contract
boundaries — what "done" means, what the acceptance criteria are. Between two ratification
points the agent has full autonomy over how it writes code. A contract that needs to change
mid-build is a new Case, never a silent deviation.

**3. One atomicity rule, applied everywhere.** A unit stays whole as long as its closing act
— ratification, verification, "built" — is a single indivisible judgment. The moment it
decomposes into two conditions that can fail independently and need different fixes, split
it. This governs Cases, Entities, Rules and Estimates identically.

**4. Rules are the harness.** A Rule page with `enforcement: render` *is* its implementation
— a script writes its body into the skill or agent file it governs. Changing how the system
behaves therefore requires a ratified decision, and there is no second copy to drift.

**5. The system learns.** Lessons are recorded facts; two sharing a root cause become an
Insight; an Insight reaches the human through `brief.md` and becomes an ordinary ratified
decision that changes a Rule. That loop is what makes the overhead compound into something
rather than staying flat.

## Things that are deliberately absent

Listed because their absence looks like an oversight otherwise:

- **No `Proposal` category.** It dissolved into Entity with `status: draft`.
- **No `ratification` field on a Decision page.** A Decision cannot exist without
  ratification; a field with one possible value carries no information.
- **No worktrees.** Ordinary git branches only.
- **No `decisions.index`.** Nothing scans decisions; they are read by following `origin`.
- **No embeddings.** The per-category indexes are small enough to read whole.
- **No `Delegate` decision kind.** It would let an agent decide without ratification, which
  is the hole the whole system exists to close.
