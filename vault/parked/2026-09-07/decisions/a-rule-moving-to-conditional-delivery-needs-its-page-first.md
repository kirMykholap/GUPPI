---
title: "Moving a rule from unconditional to conditional delivery needs a `decisions/` page before the move"
type: decision
status: current
authority: conditional-delivery-gate
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md"]
tags: [harness, process, agents]
---

# Decided by the owner on 2026-08-18: the page comes first

**A rule that renders into `CLAUDE.md` today reaches every session unconditionally.** A rule moved
into `.claude/rules/` with a `paths:` scope reaches a session **only when a matching file is read**.
That is a change in what the rule guarantees, not a change of address, and it needs its own dated
decision with a rejected alternative before any rule moves.

**Rejected alternative, named in advance: leave both in `CLAUDE.md`.** Unconditional delivery costs
context and nothing else; conditional delivery costs a rule that does not arrive.

## The criterion the decision has to be written against

> **A path-scoped rule is safe only when the dangerous action requires reading a matching file
> first.**

Derived, and already applied twice with opposite results
([[moving-a-rule-into-claude-rules-with-a-paths-scope]]):

- **`an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test` passes it** — the dangerous action
  is editing a boundary test, which requires reading it. Six files, measured.
- **`our-javascript-does-not-choose-which-rows-are-on-screen` fails it** — writing a *new* JavaScript
  file matches no read, and our JavaScript is three inline blocks in a template with nothing under
  `static/`, so a `static/**/*.js` scope protects nothing.
- **`the-suite-never-runs-against-the-production-database` fails it** — `uv run pytest` reads no file
  under `tests/`, so the rule would never load, and the fixture builds and drops schema.

## What it obliges

- **The measurement comes before the wiring, not before the decision.** Whether a `paths:`-scoped
  rule fires inside a subagent that reads a matching file is documented nowhere, and every task here
  is reviewed by a subagent ([[claude-code-loads-a-rules-file-at-launch-and-a-scoped-one-on-a-read]]).
  It decides what wiring the move needs, not whether it happens.
- **`governs:` changes and the region leaves `CLAUDE.md` in the same change**, or rule 11's address
  verdict fires on the leftover ([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]).
- **One page goes false on the day of the first move**:
  [[wiki-rules-holds-the-rules-of-the-repository-claude-md]] says each rule governs that one file. A
  title corrected in place is not a supersession
  ([[a-title-corrected-in-place-is-not-a-supersession]]).

# The first page written under this gate, and a correction — 2026-08-18

**The first instance is the JavaScript rule**, agreed for removal from `CLAUDE.md` on the same day
and not yet executed: [[the-javascript-rule-leaves-claude-md-and-is-not-yet-removed]]. It is the
shape this gate was written for — the guarantee changes, the address barely does.

**"Six files, measured" above is wrong**, and it is corrected on the page it was taken from. The
glob `tests/unit/*boundary*.py` matches six files but reaches **one of the three** that import
`_ast_boundary`; `tests/unit/*boundar*.py` is what the scope now carries
([[moving-a-rule-into-claude-rules-with-a-paths-scope]],
[[paths-lives-on-the-vault-page-and-is-written-widest]]). The verdict — that this rule and no other
passes the criterion — is unaffected: it turns on the dangerous action requiring a read, not on how
many files match ([[a-scoped-rule-fires-on-a-read-and-an-edit-implies-one]]).

**The ground for going ahead with that one move is the owner's and is recorded separately**
([[the-ast-rule-moves-to-prove-the-mechanism]]).

# The second move met this gate — 2026-08-20

**`/pre-task` moved from `CLAUDE.md` to a hook message**, and its dated page was written before the
move, with the rejected alternative named on it: *add the hook and keep the region*
([[the-pre-task-rule-leaves-claude-md-for-a-hook-message]]).

**It is a move of this class with a destination outside `.claude/rules/`.** The gate is written
about a `paths:` scope, and what it is really about — *a rule that reached every session now reaches
only some of them* — covers this one exactly: the rule arrives when a plan is presented or a first
write happens, and not otherwise.

**The reading this page left open is still open.** The AST move satisfied the strict reading *"for
whoever brings the second move to it"* ([[the-ast-rule-moves-to-prove-the-mechanism]]); this move
satisfies it the same way, by naming the alternative on its own page. **Neither reading has been
ruled on**, and the librarian does not choose between them — it is raised in the brief a second
time ([[ask-before-weakening-or-working-around-a-rule]]).

**One obligation of this gate was met and is worth naming as met**: *`governs:` changes and the
region leaves `CLAUDE.md` in the same change*. It did, at the ingest of 2026-08-20, so rule 11's
address verdict never had a leftover to fire on
([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]).

# The subject is widened to any departure from unconditional delivery — 2026-08-26

*(the owner selected it, against enumerating the delivery modes.)*

**This gate's subject is not `CLAUDE.md` → `.claude/rules/` with a `paths:` scope. It is any rule
that stops arriving unconditionally, wherever it is going**
([[the-conditional-delivery-gate-covers-any-departure-from-unconditional-delivery]]).

**The criterion written above stays attached to `paths:` scoping alone** — *the dangerous action
must force a matching read* — because a hook has its own trigger and reads no file. So the gate now
has a wide subject and a narrow safety test, and the second is not the whole of the first
([[a-path-scoped-rule-is-delivered-by-a-read-and-by-nothing-else]]).

**The section above headed *The second move met this gate* was arguing the point this settles.** It
says the move to a hook message *"is a move of this class with a destination outside
`.claude/rules/`"* and reasons from what the gate *is really about*; that reading is now the gate's
own text rather than an inference from it. **The reading it left open is still open and is not this
one** — whether a page written after the move satisfies *"for whoever brings the second move to it"*
was not ruled on.
