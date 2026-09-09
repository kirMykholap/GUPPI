---
title: "The librarian dispatches its own reading agents, waits for them, and returns once"
type: decision
status: current
authority: librarian-dispatch-owner
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", ".claude/agents/vault-librarian.md", ".claude/skills/ingest/SKILL.md"]
tags: [vault, agents, process]
---

# The ruling, 2026-08-29

**owner:** «Я уже говорил ранее, что ingest должен передавать инструкции библиотекарю. В таком случае
библиотекарь сам запускает субагентов и ждет их вердикта. Это один запуск бибилотекаря, а не два и не
три.»

**owner:** «У librarian нет инструмента dispatch - значит нужно добавить ему такой инструмент. Судя по
документации claude : субагенты могут вызывать своих субагентов.»

**`/ingest` hands the librarian a workflow.** The librarian dispatches the decisions agent and the
lessons collector itself, waits for their verdicts, writes, and **returns once**. The main session
reviews after it has finished. One librarian dispatch, not two and not three.

**Rejected: the session's reading that the librarian would be dispatched twice** — once to collect
and once to write.

**It reverses the ruling of 2026-08-28**, `the-ingest-dispatches-the-reading-agents-and-the-librarian-writes-what-they-return`,
which is in `archive/`. **That page's stated ground was that the librarian carries no dispatch tool**,
and the ground is repairable in one line: `.claude/agents/vault-librarian.md:4` reads
`tools: Read, Grep, Glob, Bash, Write, Edit`, and adding `Agent` is the whole obstacle. A missing entry
in a tool list had been recorded as settled design ([[vault-librarian]]).

**A fresh `authority:` slug rather than the archived page's.** `ingest-dispatch-owner` is still worn by
the page in `archive/`, which keeps its slug under the repeal of the same day
([[the-authority-register-step-is-repealed-and-an-archived-page-keeps-its-slug]]). Two live answers to
one question is what rule 3 forbids; one live answer beside one frozen one is what this store now
looks like, and the live one is here.

# What it obliges

**The librarian gets `Agent` in its tool list.** Nothing else about the agent file changes for this
ruling — its contents were ruled on separately
([[the-librarian-agent-file-carries-capabilities-and-the-ingest-process-lives-in-the-skill]]).

**The reading agents still only read.** A decisions or lessons agent returns verdicts and writes
nothing; the librarian writes what they return. Who holds the dispatch changed, not who holds the pen
([[dispatch-librarians-in-parallel-only-for-reading]], [[the-librarian-writes-unattended]]).

**Not built.** It is S3 item 36, outside the day's scope, and the design carrying it is
[[the-ingest-rewired-so-the-librarian-dispatches-and-returns-once]].

# The cost nobody has reconciled

**Nested dispatch has never been measured here.** `/ingest` costs **271,465 tokens and 34m08s** for one
source; the rewiring adds two reading dispatches — 143–230k for the decisions agent, and 388,649 tokens
and 17m23s for the lessons collector's only real run — plus a second librarian round trip, at every
session.

**So items 34–36 raise the per-session cost that the optimisation topic's third member exists to
lower, and no page in the vault reconciles the two.** That is recorded here rather than argued: the
ruling is the owner's and the arithmetic is what a plan for it has to answer
([[a-subagent-cannot-report-its-own-cost]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# Built the day after it was ruled — 2026-08-29

**The obstacle was one word in one line and it is gone.** `.claude/agents/vault-librarian.md:4` reads
`tools: Read, Grep, Glob, Bash, Write, Edit, Agent`, and the file carries a table of the two subagents
it may dispatch, what each returns, and that they read while it writes. `/ingest` gained step 2b — both
readers dispatched **before any write**, in parallel, because neither writes and neither depends on the
other ([[the-decisions-agent]], [[the-lessons-agent]], [[vault-librarian]]).

**The first execution was the ingest of 2026-08-29**, and both dispatches returned findings the
librarian would not have made: seven live-versus-live disagreements under different `authority:` slugs,
and two corrections to the journal's own counts.

**Nesting is bounded and configurable** — a subagent may dispatch subagents to a default depth of 3
levels, set by `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` — which no page here said before
([[claude-code-config-loading]]).

**And a cost figure reached `log.md` by a new route.** A subagent still cannot see its own usage, but
the *dispatching* agent sees its children's, so the librarian recorded both readers' costs directly
rather than through the main session ([[a-subagent-cannot-report-its-own-cost]]).

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
