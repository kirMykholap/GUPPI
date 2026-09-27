---
type: decision
case: "449"
status: current
update: ["[[rule-case-protocol]]", "[[estimate-case-protocol-case-form]]", "[[rule-case-check]]", "[[insight-case-form-chat-form-read-by-no-script]]"]
origin: raw/2026-09-27/1255/ledger.md#case-449
sprint: migration
created: 2026-09-27
tags: [session, workflow, ledger, hooks, harness]
---

## Context

The `## Language` section of `vault/wiki/case-schema.md` is the Render of `rule-case-protocol`. It allows a case number in `context` or `problem` only when the Case is about that case. It allows no count of items, no line number and no quotation there unless the Case is about one. `estimate-case-protocol-case-form` promises the same rules, and it failed again in session 2300. The context of Case 446 cited cases 378.5 and 428.1 as sources and counted "three places". The problem of Case 445 cited case 410. The case-number rule also conflicts with `CLAUDE.md`, which asks for a real source.
The person decided the following. The story sections never enter an Estimate, so they must be short and readable. The person's complaint is their test, not a script. So far the only complaint is their length. The rules on case numbers, counts, line numbers and quotations leave the story sections. A count goes stale in `given`, `when` and `then`, because `when` and `then` become a Criterion. So the count rule moves there. A number that states a condition stays.
Since Case 452, a built Case reaches the person as the file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the chat holds a short Russian text and the `ratification`. So the Criterion names the file as the place where the form stands, and a new `purpose` says so. The chat keeps the wording of `estimate-case-protocol-shows-the-built-case`, which Case 452.4 signed. The Purpose of `rule-case-check` and the docstring of `guppi/casecheck.py` say that no script checks a count in a story section. They now say that the person judges the text of those sections, while the check still requires the sections and their order. This Case actions `insight-case-form-chat-form-read-by-no-script` and rejects its proposal for the story sections. No page is created, so no vault query was run. `estimate-case-protocol-case-form` stays `pending` until a later session reads it.

## Problem

The rules on case numbers and counts in `context`, `problem` and `recommend` fail at almost every reading. The case-number rule conflicts with the rule to name a real source. Neither rule serves the person, whose only complaint is the length of `context`. Meanwhile, nothing keeps counts out of `given`, `when` and `then`, where they go stale.

## Given

`rule-case-protocol` — its Render `vault/wiki/case-schema.md`, the `## Language` section on the story sections and on `given`, `when` and `then`
**＋** `.claude/agents/case-guppi.md` — the agent that builds the Case, unchanged
**＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file that holds a built Case
**＋** `estimate-case-protocol-case-form` — the promise of the form of a built Case
**＋** `estimate-case-protocol-shows-the-built-case` — the promise of what the chat shows, unchanged
**＋** `rule-case-check` — the hook that writes the file, and its Purpose, which names what the check does not read
**＋** `guppi/casecheck.py` — the check on `SubagentStop`, whose docstring says the same
**＋** `insight-case-form-chat-form-read-by-no-script` — the Insight this Case actions

## History

- 2026-09-27 created · raw/2026-09-27/1255/ledger.md#case-449
