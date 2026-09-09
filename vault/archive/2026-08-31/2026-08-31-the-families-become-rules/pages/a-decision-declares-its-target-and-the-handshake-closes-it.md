---
title: "A decision declares its target, and the handshake between them is what closes it"
type: decision
status: archived
authority: decision-target-declaration
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: date-scope-the-decision-fields
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", "wiki/decisions/_schema.yaml", "wiki/proposals/_schema.yaml", "scripts/vault-check.sh"]
tags: [vault, record-schema, process]
---

# Context

**Nothing in `scripts/` produces a list of decisions taken and not built.** The vault's own
`CLAUDE.md` delegates task status to a tracker that does not exist — `wiki/tasks/` is deferred to S4
([[the-folder-set-is-closed-and-tasks-is-not-in-it]]). **299 decision pages stand with no mechanical
way to ask which are open**, and the owner named that as the single thing he wants and cannot get:
«Я хочу получить инстурмент, который будет подсказывать и доводить решения до реализации - а вместо
этого мы бесконечно что-то решаем.»

**The predicate that existed read the wrong arrow.** A decision left `wiki/decisions/` when some live
page named it in `decided_by:` — which records **causation**, not carriage.

# The question

**What does a decision declare about where it is going, and what mechanically decides that it got
there?**

# How it works after

**A decision page carries two new fields.**

- **`target_kind:`** — a closed list of five values on the model of `binding:`: `rule`, `proposal`,
  `action`, `repeal`, `none`.
- **`target:`** — a plain-text pointer, **never a `[[wikilink]]`**. At ratification the target does
  not exist; that is what *open* means. Rules 4 and 5 sweep a wikilink in frontmatter exactly as they
  sweep one in the body, so a link would be dead from the moment it was written until the page
  landed. `authority.md` already solved this shape the same way and says so
  ([[authority-md-is-a-register-the-one-writer-clause-names]]).

**A `repeal` decision never leaves the folder.** It is the only live carrier of the fact that
something no longer exists, so `scripts/vault-archive.sh` refuses to release one. **The catalogue of
what was cancelled is a command over those live decisions, not a maintained file.**

**A proposal carries a `# Decisions` section**, with the same heading on every proposal: one line per
decision it must close before implementation, written as a checkbox, a link and a verdict. Only the
checkbox and the link are machine-read.

**The handshake is two arrows and both must agree.** The decision names its target forward in plain
text; the target names the decision back in `decided_by:` when it lands. **A target that does not
exist is not red** — that is the state the whole open list is read from. What is red is the
half-finished landing: the page exists and does not name the decision. Rule 17 of
`scripts/vault-check.sh` performs it, **scoped to targets in `proposals/` and `rules/`** because
`decided_by:` is legal nowhere else.

**The handshake caught its first half-finished landing at this ingest.** The proposal container
[[the-decision-lifecycle]] was written before it named the decision that opened it, and rule 17
reddened [[a-case-that-grows-becomes-a-proposal-and-is-announced-when-it-happens]] until the
back-pointer was added — the verdict working on its own author, the day it was built.

**A decision page cannot reuse `decided_by:` for the forward half**, and a body wikilink cannot serve
either: the `# Context` section obliges a decision to name the pages and modules it touches, so its
body carries many links and nothing distinguishes the target from a mention.

# Recommendation

**Two fields and a handshake**, against a single field read in one direction. The session put the
forward pointer as plain text with its ground; `/pre-task` had already found that a wikilink there
would be a dead link the sweep reports.

# Ratification

**The owner said it**, on 2026-08-30, twice — for the chain and targets: «Цепочка и мишени -
ратифицирую»; and for the fields, the section and the criterion: «Case 2.3 - ратифицирую».

**Built on 2026-08-30 in the schemas and the gate.** `wiki/decisions/_schema.yaml` carries the two
keys and the five values; `wiki/proposals/_schema.yaml` carries the section; rules 16 and 17 of
`scripts/vault-check.sh` read both. **The archiver does not yet read the handshake**
([[the-sweep-reads-the-handshake-before-it-releases-a-decision]]).

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
