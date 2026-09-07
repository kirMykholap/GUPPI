# The path-scoped rule probe - how to run it

Laid down 2026-08-18. **Nothing here works until Claude Code is restarted**: a rules file and a
hook are read at session start, so the session that wrote them cannot see them.

Delete this whole directory, `.claude/rules/_probe-paths.md`, `.claude/hooks/instructions-loaded.ps1`
and the `InstructionsLoaded` block in `.claude/settings.json` once the four answers are recorded
**and compiled into `wiki/`** - the closing paragraph states that condition in full. All four are
answered as of 2026-08-19; none of them is in the vault yet.

## What is measured, and why these four

The move of a rule from `CLAUDE.md` into `.claude/rules/` with a `paths:` scope changes what the
rule guarantees: it arrives only when a matching file is read. Four things decide what wiring that
move needs, and the vendor documentation answers none of them.

The rule under test is `.claude/rules/_probe-paths.md`, scoped to `probe/*.md`. It carries two
nonces, neither guessable, so "I can see it" cannot be confused with "I inferred it":

- `PROBE-TEXT-4K7QX2` - plain text, answers probes 1, 2 and 4
- `PROBE-COMMENT-9M3ZR8` - inside an HTML comment, answers probe 3

**Two independent observables, on purpose.** The primary one is a reader quoting a nonce. The
second is `probe/instructions-loaded.log`, written by the hook. If the matcher spelling `"*"` is
wrong the hook never fires, and a probe resting on one instrument cannot tell "the rule did not
load" from "I did not measure". If the log stays empty but a nonce is quoted, the finding is about
the hook, not about the rule.

## The four probes

**1 - does the mechanism work at all.**
Read `probe/probe-target.md`. Then ask the session to quote `PROBE-TEXT-4K7QX2`. Check `/context`
for the rule under memory files, and check the log for a line naming a glob-match reason.
*Pass:* the nonce is quoted. *Fail:* it is not - and then nothing else in this list matters.

**2 - the blocker: does it reach a subagent.**
Dispatch a subagent whose whole task is: read `probe/probe-target.md`, then report verbatim
whether the string `PROBE-TEXT-4K7QX2` is present in its context, and say plainly if it is not.
*Pass:* the subagent quotes it. *Fail:* it reports the string is absent.

Do not ask the subagent to "check whether the rule loaded" - it would reason about the question
instead of reporting an observation. Ask for the string.

**3 - are HTML comments stripped in a rules file.**
Ask the session to quote `PROBE-COMMENT-9M3ZR8`.
*Stripped* (cannot quote it): a "generated, do not edit" banner in a generated rules file costs
nothing, the way region markers in `CLAUDE.md` cost nothing - measured at 1354 of 7213 bytes,
none of them reaching the model.
*Not stripped* (quotes it): the banner costs context, and whether it is worth it becomes a
decision rather than a freebie.

**4 - compaction.**
After probe 1 has loaded the rule, run `/compact`. Then attempt to edit `probe/probe-target.md`
without reading it first.
*Edit demands a re-read:* the compaction question closes completely - the re-read re-triggers the
rule, so it comes back on its own.
*Edit proceeds without one:* the rule is gone and nothing brings it back, the loss is invisible,
and conditional delivery needs a guard before any real rule moves.

## What each outcome decides

| Probe | Outcome | Consequence |
|---|---|---|
| 2 | pass | the move proceeds as designed, no extra wiring |
| 2 | fail, fixable only by a line in every subagent brief | the move is off - that is a promise, not a mechanism |
| 2 | fail, fixable by a hook | build the hook, then move |
| 3 | stripped | the generated-file banner is free |
| 4 | re-read demanded | the compaction question is closed |
| 4 | **measured: no re-read demanded** | conditional delivery needs a guard before any real rule moves |

## What this deliberately does not measure

Whether the rule fires on creating a new file, or on a Bash command touching a matching path. Both
are already known not to fire, and the rule being moved - the AST boundary rule - is edited rather
than created and is never the subject of a bare command. Spending a restart on a known answer buys
nothing.

## Answers, measured 2026-08-18

Three of the four were answered on this date. **Probe 4 was not** - it needed `/compact`, which is
the owner's to run. It was run on 2026-08-19 and its answer is the last section of this file.

**1 - does the mechanism work at all: PASS.** Both instruments agree. `probe/instructions-loaded.log`
took a second line on the Read of `probe/probe-target.md`, naming `"load_reason":"path_glob_match"`,
`"globs":["probe/*.md"]` and the trigger file; and the rule's text arrived in the session's context
attached to the tool result under a `Contents of ...\_probe-paths.md` header.

**The main session cannot be its own instrument for this probe, and was not used as one.** Learning
how to run the probe means reading this file, and this file carries both nonces in plain text — so
by the time the session reads the target it can quote a nonce it was handed. The log is the only
uncontaminated observable the session has, and it is what the PASS rests on.

**2 - does it reach a subagent: PASS, and the move proceeds as designed.** A `general-purpose`
subagent was given a brief that named no nonce and no rules file: read `probe/probe-target.md` with
the Read tool, then report any text that arrived with that read and is not in the file. It made one
tool call, opened nothing else, and returned the whole of `_probe-paths.md` verbatim — including the
standalone line `PROBE-TEXT-4K7QX2` — reporting that it had not opened that file and that the text
was delivered to it.

**The brief this file prescribes for probe 2 would have contaminated it** and was not used. Telling
the subagent to "report verbatim whether the string `PROBE-TEXT-4K7QX2` is present in its context"
puts the string in its context, so a subagent quoting it proves nothing — which is the defeat of
this file's own principle that "I can see it" cannot be confused with "I inferred it". Ask for the
delta between the file and what arrived, and name nothing.

**3 - are HTML comments stripped: STRIPPED. The generated-file banner is free.** On disk the rule
file's line 6 is `<!-- PROBE-COMMENT-9M3ZR8 -->`. In what reached the session, the text begins at
`# Path-scoped probe rule`: the frontmatter and the comment are both absent. The subagent, reading
independently and told nothing, reported that no `<!-- ... -->` markup arrived anywhere in its
context. This matches what the corpus already measured on `CLAUDE.md` region markers - 1354 of 7213
bytes not reaching the model.

**This probe was designed so that it could not answer cleanly, and nearly did not.** The rule file's
own prose says *"`PROBE-COMMENT-9M3ZR8` sits inside an HTML comment"* - in plain text, outside the
comment. A reader asked only "can you quote it?" answers yes for the wrong reason. Both readings
here rest on the *absence of the markup*, not on the presence of the string. A nonce that is
supposed to arrive only by one route must not be named on any other.

### One thing measured that was not on the list

The `auto mode` instruction — prefer Bash over the Read tool — **is delivered to subagents too**,
and it contradicted the brief this subagent was given. It followed the brief, used Read, and
reported the conflict rather than resolving it silently. Worth knowing before any brief depends on
which tool a subagent reaches for.

## Probe 4, measured 2026-08-19

**4 - compaction: the Edit proceeds without a re-read.** The rule is gone, nothing brings it back,
the loss is invisible, and conditional delivery needs a guard before any real rule moves.

Sequence, in one session across `/compact`:

1. probe 1 loaded the rule at 23:45:03;
2. `/compact` ran at 03:19:43;
3. an Edit on `probe/probe-target.md` was attempted with no read in the post-compaction context. It
   returned `String to replace not found in file` - the read gate did not fire, so no re-read was
   demanded - and nothing arrived attached to the result;
4. a Read of the same file immediately afterwards re-delivered the whole of `_probe-paths.md`.

**The log is what this rests on, not the session's introspection**, for the reason probe 1 records:
a session that has read this file can quote either nonce for the wrong reason. Two log lines decide
it, and neither is a thing the session could talk itself into:

- `03:19:43 ... "file_path":"...\CLAUDE.md","load_reason":"compact"` - **compaction has its own
  reload event, and it reloaded only the unscoped project memory.** No `path_glob_match` line
  accompanies it. The scoped rule was dropped and not restored.
- **the Edit produced no line at all** - not "loaded but not shown", the hook never fired. The Read
  a minute later produced `03:20:37 ... "load_reason":"path_glob_match"`, so the mechanism was alive
  the whole time and simply does not fire on Edit.

### Two things measured that were not on the list

**Delivery is triggered by the Read tool, not by touching a matching path.** Edit on a matching path
delivers nothing. The section above excusing creation and bare Bash commands as known negatives was
right about those and **silently assumed Edit was a positive** - which is the assumption that made
probe 4 look capable of closing the question rather than opening a wider one.

**The hole has exactly one shape and it is narrow.** The Edit tool's "you must read it first" gate
is *session*-scoped, not context-scoped: it survived the compaction here, which is why the Edit
sailed past it. So a governed file read before a compaction and edited after it is edited **with no
rule in context and no signal that one is missing**. Every other route - a fresh session, a
subagent, a first touch of the file - goes through a Read and does get the rule.

### Why those three behaved differently, which is what a guard has to answer

Three things crossed the same `/compact` and only one was lost, so the difference is the finding
rather than the loss:

| what | mechanism | after `/compact` |
|---|---|---|
| `brief.md` | the `SessionStart` hook, whose matcher names `compact` | **arrived** |
| `CLAUDE.md` | unconditional project memory | **reloaded**, `"load_reason":"compact"` |
| `.claude/rules/_probe-paths.md` | conditional delivery scoped by `paths:` | **did not return** |

**What survives a compaction is whatever has something that runs it again.** The brief has a hook
bound to the compaction event itself; project memory has an unconditional reload. A path-scoped
rule's trigger is a Read that already happened, and it does not happen a second time on its own.

A guard is therefore not "remind the model" - it is **a second trigger**, and it has to be bound to
something that recurs. The `PreToolUse` hook on `Edit|Write` is the obvious candidate, since it
already fires on exactly the operation that was measured going through unguarded. Note also that
`probe/instructions-loaded.log` is silent about the brief and always will be: the brief is
`SessionStart` context, not a memory file, so that log is not an instrument for it.

### What it decides

The AST boundary rule does not move on the strength of "whoever edits it will have read it". A
guard comes first and it has to cover the post-compaction edit specifically; which guard is open and
is not answered here.

**Do not delete this directory yet.** All four probes are answered, but the answers above reached
the repository after this session's journal was written and ingested, so the vault does not hold
them. Delete `probe/`, `.claude/rules/_probe-paths.md`, `.claude/hooks/instructions-loaded.ps1` and
the `InstructionsLoaded` block in `.claude/settings.json` once probe 4 is compiled into `wiki/`.
