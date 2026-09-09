---
title: "The dividend of the forked `vault-ask` is unmeasured, and the measurement is named rather than scheduled"
type: decision
status: current
authority: fork-dividend-measurement
binding: deferral
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: none
target: none
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", ".claude/skills/vault-ask/SKILL.md"]
tags: [agents, retrieval, process]
---

# Context

**`vault-ask` stopped dispatching the librarian and became a forked skill on 2026-08-30**
([[the-vault-ask-skill]]). The saving claimed for it is that a fork starts empty, so the pages it
reads never enter the caller's context and only the report comes back.

**The owner asked directly whether it pays** — «принесёт ли нам это сейчас дивиденды? Да, но я не
знаю насколько много» — **and the mechanism was built without answering.**

**Nothing here has ever run a forked skill.** The claim about what a fork inherits is read off vendor
documentation and carries `basis: external`
([[a-forked-skill-starts-empty-and-a-subtask-fork-inherits-everything]]).

# The question

**What does the fork save, and against what?**

# How it works after

**Unmeasured, and the measurement is named: the first real fork run against a librarian dispatch on
the same question.** Both numbers are obtainable in one session and neither has been taken.

**Naming it is what keeps this out of `undesigned`.** A deferral with no test behind it cannot be
discharged; this one can be discharged by one comparison.

**What makes the arithmetic hard, and it is not laziness.** A subagent cannot report its own token
cost ([[a-subagent-cannot-report-its-own-cost]]), and an earlier attempt to net a dispatch against
what it saved summed an isolated subagent's budget into the caller's and was wrong. **So the
comparison has to be caller-side context growth, not subagent tokens.**

**And this architecture adds reading dispatches rather than removing them** — measured on its first
run at 281k tokens across the two readers — inside a topic opened to reduce per-session cost
([[who-reads-the-vault-and-who-writes-it]]).

**No sprint is named.**

# Recommendation

**Take the measurement on the next real question rather than building a benchmark for it.** A
synthetic question would measure the fork against a shape neither party runs in, which is the failure
this store recorded the same day about a hook
([[a-process-is-measured-with-the-stdin-it-will-have]]).

**Rejected: measuring it before building**, which would have blocked the build on a run that needs the
build.

# Ratification

**The session understood it, and the owner's question is the record that it was not answered.** He did
not defer this; he asked it and the session proceeded. That is what is written here.

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
