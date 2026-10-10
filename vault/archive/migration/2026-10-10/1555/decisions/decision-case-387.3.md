---
type: decision
case: "387.3"
status: archived
create: ["[[rule-spec-reconcile]]", "[[estimate-spec-reconcile-refuses-an-edit-of-the-plan]]"]
update: ["[[rule-case-protocol]]", "[[rule-hook-registry]]"]
origin: raw/2026-09-23/1859/ledger.md#case-387.3
sprint: migration
created: 2026-09-23
tags: [hooks, harness, workflow, session, ledger, render]
---

## Context

Today the agent writes each ratified Case into the plan file itself, in the reply with its ledger lines, and translates the whole Case into English. When a signed Case changes later — the person's change, a finding of pre-spec, a change of the model — the agent shows it again whole: `given`, `when`, `then`, `tasks` and `ratification`, even for a change of one word; in session 1355 a change of the model made three Cases signed again this way. Also, the English the vault receives is the agent's translation, which nobody compares with the signed text, and `when` and `then` become the Criterion of an Estimate word for word. The vault (ask-guppi): no rule covers a Spec written by a hook or a reconciliation; `rule-case-protocol` (`draft`) says the agent writes the Spec and a re-showing is always whole; `rule-language` (`built`) says Russian in all sections; `rule-prespec` (`draft`) checks the plan against the ledger lines, not against a copy; `rule-hook-registry` takes the registration of a hook in the Case that creates its rule; `rule-spec-write` and `rule-spec-reconcile` are free. `estimate-language-followed` is replaced, since it asks for Russian in all sections; `estimate-case-protocol-loaded` and `estimate-hook-registry-rendered` are not touched — an `update` of a Render touches no Estimate of the live reading (case 378.5); `estimate-case-protocol-case-form` speaks of the chat form, not of its language or of who writes the Spec. The re-showing in Work Mode stays as it is: the Spec there is `spec.md`, not the plan file.

## Problem

A small change of a signed Case costs a whole re-showing, and the English the vault receives is a translation nobody compares with what was signed.

## Given

`rule-spec-reconcile` — the new hook rule, a child of `rule-plan-mode`.
**＋** `estimate-spec-reconcile-refuses-an-edit-of-the-plan` — its Estimate.
**＋** `guppi/ratified.py` — one comparison function for the edit hook, `Stop` and pre-spec; `tests/test_ratified.py` — its tests.
**＋** `<plan>.ratified.md` — the ratified copy 387.2 writes.
**＋** `rule-case-protocol` — the `ratification` row of its Render says when a Case is shown again.
**＋** `rule-hook-registry` — the Render of the `"hooks"` key.

## History

- 2026-09-24 created · raw/2026-09-23/1859/ledger.md#case-387.3
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
