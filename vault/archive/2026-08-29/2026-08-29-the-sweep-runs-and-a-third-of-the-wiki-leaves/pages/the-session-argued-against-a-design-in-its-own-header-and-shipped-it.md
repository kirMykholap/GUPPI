---
title: "The session argued against a design in its own header and shipped that design"
type: lesson
status: archived
authority: argued-and-shipped-anyway
basis: measurement
sprint: S3
created: 2026-08-28
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", ".claude/hooks/remind-the-feedback.ps1"]
tags: [harness, process, agents]
---

# Both instances, on one day

**The first `remind-the-feedback.ps1` carried eighteen lines of header explaining why a
per-invocation reminder becomes furniture — and was a per-invocation reminder.** The owner supplied
what the session had already argued for
([[the-feedback-reminder-fires-on-the-owners-prompt-and-speaks-when-the-channel-is-quiet]],
[[a-reminder-that-fires-every-time-becomes-furniture-and-a-silence-counter-avoids-it]]).

**And the session filed `measure:` and `miss:` lines freely through eleven owner rulings and filed
no `decision:` line at all**, having written the rule about that channel into a hook earlier the
same session. It recorded nothing until he asked about it directly.

# What the pattern is

**Writing the argument down is not the same act as obeying it.** In both cases the reasoning was
correct, was written into a file that shipped, and did not reach the decision beside it. Nothing in
the harness compares a design against the argument in its own header, and nothing could.

**This is the third recorded instance of the quiet-channel half** — a session that stays silent
inside a long conversation — and both existing defences fire once per invocation rather than per
turn ([[divergence-the-retro-filed-no-feedback-block-while-it-ran]],
[[feedback-is-recorded-in-the-turn-it-is-noticed]]).

# What was done about it

**The counter answers the first half**, and it is the owner's design rather than the session's.
**The second half is uncovered**: `MessageDisplay` fires on every assistant reply and is where a
turn counter for the session's own silence would live. It was found this session and not used
([[the-session-speaks-the-feedback-line-and-a-hook-files-it]]).

# The reading the extract gives, and its limit

**The session's dialogue extract for 2026-08-28**: 12 owner turns, 77 session replies, 15 feedback
marks, zero menus, 193,109 bytes. **The marks yielded 48 `decision:` lines, which are 24 distinct
decisions each listed twice.** Zero menus means every ruling that day arrived as prose rather than
as the result of a tool.

**And the marks carry only decisions.** The open-questions list of the retro held 17 items and not
one of them came from a mark: a fork closed silently and a mistake corrected in flight are invisible
to that channel by construction ([[the-session-dialogue-extract]]).
