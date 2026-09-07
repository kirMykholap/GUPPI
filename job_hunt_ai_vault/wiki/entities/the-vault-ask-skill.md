---
title: "`vault-ask` — the forked search skill, and the first `context: fork` in this repository"
type: entity
status: current
authority: vault-ask-skill
basis: code
sprint: S3
created: 2026-08-30
sources: [".claude/skills/vault-ask/SKILL.md", "archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md"]
tags: [agents, retrieval, harness]
---

# What it is now

**Changed on 2026-08-30, and it is a different thing.** It was a wrapper that dispatched
`vault-librarian`; it is now a skill that runs as a fork, searches, reports, and writes nothing.

```yaml
context: fork
agent: Explore
background: false
```

**It is the first `context: fork` in this repository** — there were none before it. The design is the
store's own, written on 2026-08-29 and unbuilt until this day: one search entry point, forked, used by
everyone including the librarian ([[who-reads-the-vault-and-who-writes-it]]).

# The three frontmatter choices, each ratified after the fact

**`agent: Explore` changes what the search can see.** That agent type loads no `CLAUDE.md` — neither
the repository's nor the vault's. Here that is a saving rather than a loss, and only because the
rendered reading discipline inside the skill tells the fork to read `$VAULT/CLAUDE.md` explicitly. If
that region ever leaves the file, the fork loses the rules of the store silently.

**`background: false`** — the caller waits for the report.

**Both were closed by the session without asking and ratified afterwards**
([[the-forks-the-session-closed-without-asking-are-ratified]]).

# What it adds to the shared reading discipline

**It became the fourth destination of
[[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]]** rather than
restating the procedure, and it carries three things that rule does not:

- **the catalogue without the archive** — `bash scripts/vault-catalogue.sh`, one row per live page,
  131,604 bytes since the `## archive` section left it;
- **walking a page's links by grep instead of by opening it** — outgoing with one `grep -o` over the
  file, inbound with one `grep -rl` over `wiki/`;
- **`grep -rl "^authority: <slug>" wiki`**, which returns the whole chain of one question across types
  ([[a-slug-shared-across-types-is-the-graph-the-links-field-would-have-cached]]).

# What it does not promise, and the line is load-bearing

**`/vault-ask` promises relevance; `/pre-task` promises completeness over a scope.** Asking a good
question about a plan feels like checking it and is not, and the difference shows up only in what was
never returned. **A `vault-ask` row in the ledger asserts nothing about the pre-task ritual** and its
`pre_task` column reads `-`.

**Its own row is the caller's to write.** A fork has no session identifier and
`scripts/record-pre-task.ps1` keys on one.

# The feedback region had to leave before the fork, and the order was ruled first

**The channel is a fenced block lifted out of a displayed message by a `MessageDisplay` hook, and a
fork returns a result rather than a message.** Under `context: fork` this file becomes the forked
agent's own prompt, so the region would have instructed the fork to speak a block no hook reads and no
caller sees — an instruction addressed to a party that cannot carry it out.

**The region left, and only then did the destination leave the rule's `governs:` list.** That order
was fixed by the decision of 2026-08-29, because the reverse leaves an orphan region in a file the
injector no longer writes
([[the-feedback-region-leaves-vault-ask-and-the-destination-leaves-the-rules-governs-list]]).

# The dividend is unmeasured

**The owner asked directly whether the fork pays** — «принесёт ли нам это сейчас дивиденды? Да, но я
не знаю насколько много» — **and the mechanism was built without answering.** The measurement is
named: the first real fork run against a librarian dispatch on the same question. It has not run
([[the-dividend-of-the-forked-vault-ask-is-unmeasured]]).

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md` and from the skill itself.)*
