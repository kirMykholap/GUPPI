---
title: "A forked skill starts empty and a `/subtask` fork inherits everything, under the same word"
type: concept
status: current
authority: fork-word-collision
basis: external
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md"]
tags: [agents, harness, process]
---

# The mechanisms

| | what "fork" means there | what the callee starts with |
|---|---|---|
| **`context: fork` in a skill's frontmatter** | the skill runs as a subagent whose prompt **is** the `SKILL.md` | **nothing** — no access to the caller's conversation history |
| **a `/subtask` fork** | a child that continues the parent | the **entire** parent conversation, reusing its prompt cache |

**They are opposites, and they share a word.** Read off `code.claude.com/docs`, the skills and
sub-agents pages, on 2026-08-29 — the source is a vendor document rather than a path in this
repository, which is why `sources:` names only the journal and this sentence names the rest.

# Why the collision matters here and is not a curiosity

**This store has been burned by exactly this shape before.** *Retrospective* meant a session's end and
a sprint's ritual for three days, and the ambiguity put two live, contradictory answers into the vault
about when `/ingest` runs ([[a-retrospective-is-a-sessions-end-not-a-sprints-ritual]]).

**The difference is the whole cost question for `vault-ask`.** Forking the skill starts a clean
context and pays for everything the caller wants known to travel as arguments; a `/subtask` fork pays
nothing for context and inherits the pollution the dispatch was meant to avoid
([[a-skill-is-a-mask-and-a-subagent-is-a-body]], [[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]).

# The consequence nobody had written down: a rendered region can change audience

**`.claude/skills/vault-ask/SKILL.md` carries the rendered region
[[speak-the-feedback-in-the-turn-and-the-hook-files-it]], whose text is addressed to the *caller*.**
Under `context: fork` that file becomes the forked agent's own prompt, so the region would instruct
the fork to speak a `VAULT-FEEDBACK` block no hook reads and no caller sees.

**Nothing in this vault says a rule region's audience changes when its host file changes execution
mode, and this is the first case where it does.** The owner removed that region from that skill on
2026-08-29 rather than leaving it to be discovered at the fork
([[the-feedback-region-leaves-vault-ask-and-the-destination-leaves-the-rules-governs-list]]).

# What is not measured

**Nothing here has run a forked skill.** The claim is read off the documentation and carries
`basis: external`; the first fork is the measurement, and `vault-ask` as `context: fork` is designed
and unbuilt.

# The fork exists and the measurement still has not been taken — 2026-08-30

**`.claude/skills/vault-ask/SKILL.md` became the first `context: fork` in this repository**, and the
paragraph above is left standing because its last clause is what changed: the skill is built and the
first fork run against a librarian dispatch **has not happened**
([[the-vault-ask-skill]], [[the-dividend-of-the-forked-vault-ask-is-unmeasured]]).

**Building it surfaced a third property of a fork that the table above does not carry.** The agent
type matters: `agent: Explore` **loads neither `CLAUDE.md`** — not the repository's and not the
vault's. So a fork does not merely start without the caller's conversation; **it can start without the
project's own instructions**, and which instructions it gets is a frontmatter choice rather than a
property of forking.

**Here that is a saving and it is conditional.** The reading discipline is rendered into the skill by
the injector, so the fork is told to read `$VAULT/CLAUDE.md` explicitly. **If that region ever leaves
the file, the fork loses the rules of the store and nothing says so.**

**The audience consequence this page predicted was paid before the fork, in the order the store had
ruled.** The feedback region left `vault-ask` first and the rule's `governs:` list lost that
destination afterwards. **Both halves of that decision landed on 2026-08-30** and the injector
reported `1 region(s) rewritten, 0 problem(s)` when the shared reading discipline took the file as its
fourth destination.

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
