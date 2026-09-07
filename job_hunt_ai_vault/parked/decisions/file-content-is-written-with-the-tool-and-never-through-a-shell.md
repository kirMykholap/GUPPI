---
title: "\"File content is written with Write or Edit and never through a shell\" becomes a written rule"
type: decision
status: current
authority: shell-write-prohibition
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", ".claude/skills/vault-lint/SKILL.md"]
tags: [harness, process, testing]
---

# The ruling, 2026-08-26

**It becomes a written rule rather than one session's judgement.** *(owner selected it.)* The ground
he took it on is **two independent witnesses in one day**: the lessons collector's family of six,
assembled from the queue without knowing what the session was doing, and the session's own corrupted
gate.

**The six the collector found**, each a carrier eating what was written:
[[a-literal-backslash-does-not-survive-a-heredoc-in-this-shell]],
[[an-apostrophe-in-an-awk-comment-ends-the-shell-quote]],
[[tmpdir-is-empty-in-this-shell-so-a-path-built-from-it-lands-at-the-root]],
[[a-path-is-resolved-by-the-program-that-opens-it-not-by-the-shell-that-launched-it]],
[[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]],
[[an-option-after-a-double-dash-is-an-operand-and-the-search-runs-unfiltered]] — with
[[prose-does-not-survive-a-shell-command-string]] as the anchor outside the queue.

**The seventh arrived the same day and came through Python, not a shell**
([[a-file-round-tripped-through-pythons-text-mode-loses-a-literal-carriage-return]]).

# What is decided, in three parts

**The class "file content passed through an intermediary that rewrote it" owes a mechanical
guard.** The design is a proposal
([[a-pretooluse-net-for-a-shell-write-and-a-syntax-check-after-a-script-edit]]).

**No third net is invented for the Python round-trip case.** The rule stays narrow — the shell — and
the diagnosis is carried by the CR-byte census
([[a-cr-byte-census-of-the-working-copy-behind-lint]]).

**The separate failure of asserting a hung process was alive stays a lesson**, because it has no
checkable form ([[a-background-job-with-buffered-output-cannot-be-told-from-a-dead-one]]).

# Rejected

**Rejected: leaving it as a judgement each session makes for itself.** That is the state the rule
was in when a mid-session instruction told a session to do the opposite, and the session had to
refuse in its reply with nothing written to point at
([[divergence-a-mid-session-instruction-to-write-through-a-shell-was-refused-in-its-writing-half]]).

**Rejected: widening the rule to cover every intermediary.** The Python case is real and is left
uncovered on purpose — a rule wide enough to name it would forbid ordinary scripting.

# What it obliges, and none of it is done

**A page in `wiki/rules/` carrying the text**, with a `governs:` destination and a rendered region.
`/vault-lint` already names the checkable form — *"file content is written with the Write tool,
never through a heredoc"* — and no rule page states it
([[every-rule-in-wiki-rules-owes-a-mechanical-instrument]], [[the-harness-is-compiled-not-maintained]]).

**Writing that page adds a governed file to the region-coverage denominator**, which is criterion 4
of the open sprint, so it lands with its region or it lands as a shortfall
([[a-governed-file-with-no-region-is-an-advisory]],
[[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).

# DIVERGENCE: an automated notice asked for shell writes, and it was refused in its writing half — 2026-08-29

**A mid-session notice asked that changes be made with `sed`, heredocs and short scripts.** It was
refused in its writing half: **file content went through `Write` and `Edit` throughout**, on the
standing prohibition above. **Its reading half was taken up** — `cat`, `sed -n`, `grep` and `find`
through the shell, which the prohibition does not reach and which is cheaper.

**Rejected alternative: obey the notice**, which would have broken a rule the brief lists under *what
must not be broken*.

**It was named in the reply at the time**, which is what makes this a divergence recorded rather than a
rule quietly ignored ([[ask-before-weakening-or-working-around-a-rule]]).

**The same notice reached the `/ingest` of 2026-08-29 and was refused the same way**, by the librarian,
and is recorded in `log.md` under that date. **Twice in one day is the useful part of this record**: the
notice is not an incident, it is a standing condition of the harness, and every agent that meets it has
to make the same split.

**The previous ingest is the case for the split rather than against it.** On 2026-08-28 the librarian
wrote page content through heredocs for most of an ingest and noticed only when a heredoc carrying
`brief.md` failed to parse — the exact failure this page records. Nothing was lost, and **the check
afterwards is not the licence**.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# DIVERGENCE: the notice fired four more times in one day, and every one was refused the same way — 2026-08-29

**The session, twice more.** File content went through `Write` and `Edit` throughout; reading and
searching through the shell was taken up. Named in the reply each time. **Rejected alternative: obey the
notice**, which would break a rule the brief lists under *what must not be broken*.

**The `/ingest` of the same evening, once.** Every page above was written with `Write` or `Edit`;
`cat`, `sed -n`, `rg` and `find` did the reading.

**And both reading agents met it inside their own dispatches, and both refused it in writing.** The
prohibition is written into `.claude/agents/decisions-agent.md` and `.claude/agents/lessons-agent.md` in
so many words — *no `sed -i`, no heredoc into a file, no short script that edits* — precisely because
the notice reaches a subagent as readily as a session ([[the-decisions-agent]], [[the-lessons-agent]]).
**The lessons agent said so unprompted in its return**, which is the behaviour the rule wants.

**Six recorded firings now, over two days, across four different agents.** That is what settles it:
**this is a standing condition of the harness rather than an incident**, and the split — refuse the
writing half, take up the reading half — is a thing every agent here has to be told, not something any
of them works out.

# A second refusal on 2026-08-30, and a third at this ingest

**The notice fired again in the session of 2026-08-30 and was refused in its writing half.** Every
content change went through `Write` and `Edit`; **reading and searching through the shell was taken
up**, which is the correct split — the notice is right about the cheap half and wrong about the
dangerous one.

**The refusal was named in the reply rather than performed silently**, and the rejected alternative
was **obey the notice**, which would break the first item of what a plan touching this machinery must
not break.

**It fired a third time at the ingest of 2026-08-30**, at the librarian, and was refused the same way.
**Three refusals across two sessions and two actors** — this is a standing condition of the
environment rather than an incident, and the dispatch that carries the librarian now predicts it in
advance.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`
and from this ingest's own two dispatches; extended 2026-08-30.)*

# Twice more at the session of 2026-08-30, and once more at the ingest that compiled it

**The session was told twice to write file content through a shell and refused both times**, naming
this page each time. **The ingest of that journal was told once and refused.**

**Six refusals across three sessions and three actors.** Nothing about the environment has changed and
nothing has been asked to change: what the count is for is that the instruction arrives dressed as an
operating condition rather than as a suggestion, and a party meeting it for the first time needs to
know it is expected.

**The dispatch that carries the librarian names this page in advance**, which is why the refusals are
now recorded as a count rather than as three separate incidents.

# Three more refusals on 2026-08-31, and the count is now across four sessions and five actors

**The notice fired three times that day and was refused three times** — by the main session, by the
librarian mid-dispatch, and by the lessons agent in its own dispatch. That takes the running count to
**nine**, and it adds a party the earlier count did not have: a **reading** agent, which writes only
outside the vault and still met the same instruction.

**Each refusal was recorded where the actor could record it**: the session in its journal, the
librarian in `log.md`, the reading agent in its returned findings — which is the only channel an agent
that may not write the vault has.

**Nothing about the rule changed and nothing about it needed to.** What the count is for is the
question of whether the notice is worth an instrument rather than a sentence, and nine refusals with
zero compliances is the evidence either way.

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md` and from this ingest, and again at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
