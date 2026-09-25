---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: case-guppi builds a Case against the vault and its frame and answers with the Case alone
method: "by hand: two live dispatches in a session after the render, one Case with a create without a ref and one that changes a hook; the tokens and seconds of each dispatch in the estimate line"
origin: raw/2026-09-24/1303/ledger.md#case-391.1
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness]
---

## Criterion

When:
The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it the person's question or change by `SendMessage`.

Then:
`case-guppi` reads `vault/wiki/case-schema.md` whole before it writes the Case.
**＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
**＋** It reads each page and file the `given` of the Case names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`.
**＋** Each contradiction it finds is fixed in the Case, or the `context` says why it stands.
**＋** Its answer is the Case in the chat form of `vault/wiki/case-schema.md`, from the heading to the fence of `ratification`, and nothing else; asked again, it answers with the Case whole again.
**＋** An answer that needs a choice the person has not made is that question alone, with no Case heading.
**＋** It runs on `model: opus` with `effort: medium` and the tools Read, Grep and Glob.
**－** It writes no file and no ledger line.

## History

- 2026-09-24 created · [[decision-case-391.1]]
- 2026-09-25 renamed from `estimate-frame-check-finds-a-contradiction` · [[decision-case-419.2]]
- 2026-09-25 updated: renamed; the Criterion replaced whole — case-guppi builds the Case; the method measures its cost (case 419.2) · [[decision-case-419.2]]
- 2026-09-25 ref `rule-frame-check` → `rule-case-build` · [[decision-case-425]]
