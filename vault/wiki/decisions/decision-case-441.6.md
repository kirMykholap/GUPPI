---
type: decision
case: "441.6"
status: current
create: ["[[estimate-spec-write-reaches-the-approved-spec]]"]
update: ["[[rule-spec-write]]", "[[rule-spec-capture]]", "[[rule-case-protocol]]"]
origin: raw/2026-09-26/1745/ledger.md#case-441.6
sprint: migration
created: 2026-09-26
tags: [hooks, harness, workflow, session, ledger]
---

## Context

Today `case-guppi` builds a Case with its name, `context`, `problem` and `recommend` in Russian and its `given`, `when`, `then` and `tasks` in English. The main agent shows the answer unchanged. On `Stop`, `uv run guppi casecheck` compares the whole showing, heading and prose included, line by line with the answer stored in `<plan>.checked.json`. After the reply that carries the ledger lines, the `Stop` hook of `rule-spec-write` writes the stored answer into the plan file and into `<plan>.ratified.md`. Before the approval the agent translates the name, `context` and `problem` in the plan by hand. The `/pre-spec` check refuses a Cyrillic letter there, and a prose-only change is shown as a `DIFF` with no ratification (cases 373, 387). At `ExitPlanMode`, `guppi spec` appends the plan once to `raw/<hi date>/<hi HHMM>/spec.md`.

This goes wrong in three places. First, a hand-made translation does not last. The hook writes from the store, so a Case rebuilt after its translation puts Russian prose back into the plan. The deferred decision on `rule-prespec` (case 438) describes this: a pre-spec finding in the body of a Case goes to its `case-guppi` and a new ratification, prose is fixed in the plan as a `DIFF`, and the translation is the last step. Second, a Case ratified after the approval reaches only the plan and its copy, never `spec.md`, and the scripts read `spec.md`. In session 1337, the sections of Cases 434 and 436.4 there were replaced by hand from the plan, with the person's consent. Third, a Case superseded in its own session must leave the Spec. The hook only replaces or inserts sections, so today the agent removes the Case by hand, and `/pre-spec` reports one still in the plan (case 299.2).

The person chose this scheme:
- `case-guppi` writes the whole Case in English.
- The main agent translates the name, `context`, `problem` and `recommend` into Russian for the chat and shows the rest as the answer holds it.
- The main agent writes a short-form defer in English in the chat.
- The `Stop` comparison reads only `given`, `when`, `then`, `tasks` and `ratification`.
- The Spec hook writes the English answer into the plan, into its copy and, once it stands, into `spec.md`. There it replaces the sections of a Case or places a new one, and keeps the ticks of unchanged task lines.
- The Spec hook removes a Case that a `{supersedes:case N}` line of the reply supersedes.
- The translation step and the prose `DIFF` go.
- A changed ratified Case, in its prose or its body, goes to its `case-guppi`, is shown again whole and is ratified again. The hook writes only a stored answer after a reply with the Case's lines, so a hand edit of the plan would be overwritten.
- The Cyrillic check of `/pre-spec` stays as a safety net.

State of the pages. `rule-case-build` and its Render say the main agent shows the answer unchanged. `rule-case-check` compares the whole showing. `vault/wiki/case-schema.md`, the Render of `rule-case-protocol`, says the prose is Russian in the chat and translated in the Spec. It keeps a reduced re-showing of a ratified Case and the prose `DIFF`, and it leaves the removal of a superseded Case to the agent. `rule-prespec` tells the agent to translate before the run and to fix a wrong fact in the plan as prose. `rule-spec-write` states its purpose as "the words the person signed" and skips a Case whose last mention is a `DIFF`. `rule-spec-capture` names the agent as the writer of `## Deferred` in `spec.md`, which has been out of date since the hook took over the defer. Its Estimate `estimate-spec-capture-appends` keeps that writer in its Criterion. `rule-prespec` carries `deferred_by` case 438; sub-case 441.4 takes it up and supersedes it. Case 440.3 of this session also changes `rule-case-protocol`, and its anchors differ from the ones used here.

The vault's answer. The two `create` items are Estimates with a `ref`. Their slugs, `estimate-spec-write-reaches-the-approved-spec` and `estimate-spec-write-removes-a-superseded-case`, are free: a Glob over `vault/` finds neither.

Findings in the frame, and why each stands:
- Without the prose `DIFF`, the `DIFF` skip of the Spec hook has no use left. It would also silently skip a re-ratification whose last mention is a code diff naming the Case. Sub-cases 441.8 and 441.9 remove it and the lines of the two Estimates that name it.
- The `DIFF` exception of the `Stop` comparison stays in 441.3. A fence tagged `DIFF` is never the showing of a Case, and a diff of code or of a page that quotes a Case must not be compared.
- `estimate-prespec-catches-a-superseded-case` stays true. A superseded Case still in the plan remains a finding, now a net behind the removal by the hook.
- `estimate-case-protocol-defers-in-one-reply` stays true. It says nothing of the language, and the agent still writes nothing of the defer into a file.
- The `## Language` section of `CLAUDE.md` (`rule-language`) and `estimate-language-followed` say that the name, `context` and `problem` "are translated into English in the Spec before its approval". The result still holds; only the step is gone. The person keeps them as they are, and the smallest wording, if they are ever changed, is "are Russian in the chat and English in the Spec".
- The Purpose of `rule-spec-reconcile` gives the Russian prose of the ratified copy as its reason. The `when` of `estimate-spec-reconcile-refuses-an-edit-of-the-plan`, "the agent edits the plan file", no longer happens. Both stand because the page is deferred by case 423, whose question of a guard on the agent's edits of the plan the person has not decided.
- `insight-case-show-built-case-retyped-by-hand` is not actioned. The main agent still writes the showing out, and the retyped lines it records stay compared parts.
- `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-protocol-case-form`, `estimate-case-protocol-loaded`, `estimate-case-protocol-acknowledging-reply`, `estimate-spec-write-writes-a-defer` and `estimate-spec-capture-offers-the-fork` speak of nothing this Case changes.

## Problem

The prose of a Case is written in Russian and translated by hand in the plan, and a later write from the stored answer undoes that translation. A Case ratified after the approval never reaches `spec.md`. A superseded Case leaves the Spec only by hand. Decide how the rules that build, show, check, pre-spec and write a Case take up the person's scheme, so that no hand edit of the plan or of `spec.md` is needed.

## Given

`rule-spec-write` — the rule of the `Stop` hook that writes a ratified Case
**＋** `estimate-spec-write-reaches-the-approved-spec` — the promise of the write into `spec.md`
**＋** `rule-spec-capture` — the rule that names the writers of `spec.md`
**＋** `rule-case-protocol` — its Render says where the Spec hook writes
**＋** `guppi/ratified.py` — the `Stop` hook `uv run guppi ratified`
**＋** `guppi/spec.py` — its docstring names the writers of `spec.md`
**＋** `tests/test_ratified.py` — the tests of the hook
**＋** `raw/<hi date>/<hi HHMM>/spec.md` — the approved Spec of the session

## History

- 2026-09-26 created · raw/2026-09-26/1745/ledger.md#case-441.6
