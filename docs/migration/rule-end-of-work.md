---
type: rule
kind: MOC
purpose: Prevents a session being handed over without a settled account of what happened
status: draft
children: [rule-retro, rule-retro-commit, rule-handoff]
estimates: [estimate-end-of-work-order]
origin: TBD
sprint: TBD
created: TBD
tags: [session, workflow, retro, handoff]
---

## Purpose

Prevents a session being handed over without a settled account of what happened — and
prevents the librarian's writes being indistinguishable from the session's own, by forcing
a commit between the two.

## How it works

Three steps: the Retro conversation, a commit hook that fires on the way to handoff, then
handoff itself.

### Retro is a conversation, not a report

Work Mode already started the harness suite in the background. Retro opens immediately and
the person reads what happened while the suite runs; results land mid-conversation. The
accumulated Cases from Work Mode are discussed here in the ordinary Case format.

**Scope rule: Retro examines only what already happened in this session.** Code edits are
allowed when they finish or correct work already ratified in this session's ledger, and
forbidden when they add new scope.

The test is mechanical, not a judgment call: does this change trace to a decision already
ratified in this session's ledger? If yes, it is finishing ratified work — edit it. If no,
it is new scope — defer it. Do not argue about what counts as "new code"; check the ledger.

**Bugs** become a `lesson[error]`. Fixing one now is fine when it traces to this session's
work. Deferring one means also **opening a GitHub issue** — a deferred bug that exists only
as a ledger line is invisible outside the vault, and the issue is what makes the next
Frontier pick it up. The issue number goes in the ledger line's `source`.

**Red harness tests** produce a `lesson[error]` whose root cause is "why did we reach Retro
with a regression", not "a test failed" — and then the person decides. Handoff still
requires green.

Retro ends by restating every ratification of the session, briefly, and calling `/handoff`.
All of that lives in the `retro` skill.

### The commit is a hook, not an instruction

An instruction to commit before handoff is a step an agent can skip. A PreToolUse hook on
`/handoff` cannot be skipped. This matters because the commit is what makes everything the
librarian writes afterwards visible as a distinct layer — without it, session work and
librarian work land in the same undifferentiated diff.

### Handoff is thin

`handoff.md` carries three things, none of them decisions:

- **Notes from memory** — where the person hesitated, what stayed unclear, which decisions
  carried caveats. Things that happened in conversation and are in no artifact.
- **Direct instructions to the librarian** — "check page X first", "this may duplicate Y".
- **What actually got done** — which Cases closed and where the code landed. This is in
  neither the ledger nor the Spec; it lives in the plan's checkboxes and the commits, and
  only the main agent watched it happen. It is what fills `code_ref`.

The main agent does **not** re-read the artifacts to write it. Doing so would spend the
context advantage that is the note's only reason to exist. Short or empty is a normal
outcome.

Then a quick check that nothing is obviously missing, and the librarian is invoked.

## Children

1. **[[rule-retro]]** — `render` → the `retro` skill. The conversation, the scope rule, bug
   handling, the closing summary of ratifications, and the call to `/handoff`.

2. **[[rule-retro-commit]]** — `hook`, PreToolUse on `/handoff`. Requires a commit. This is
   the baseline the librarian's work is measured against.

3. **[[rule-handoff]]** — `render` → the `handoff` skill. Writes `raw/<date>/handoff.md`
   from memory, checks nothing obvious is missing, invokes the librarian.

   **No commit after handoff** — that would fold the librarian's writes back into the
   session's diff and undo what the previous hook just established.

## Estimates

- [[estimate-end-of-work-order]] — QA. `/handoff` cannot run without a preceding commit;
  `handoff.md` exists before the librarian is invoked; and no commit is made between
  handoff and the librarian's own.

## What happens next

The librarian takes over with a clean context → [[rule-documentation]].

## History

- TBD created
