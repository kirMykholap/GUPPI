# Ratification — the one rule and the ledger

## The one rule

Nothing in the vault or the codebase changes without a Decision ratified by the human. The agent has full autonomy over *how* to implement something once its contract is ratified, and none over the contract itself. When unsure whether something needs ratification: it does. A new tag needs no Decision when a lesson line declares it with its meaning and its Russian aliases, and the librarian's run adds it to `tags.md` (as set in case 827.3). The vault is the only memory: no note outside the repository — not the harness's memory directory, not a file outside `vault/`; what is worth keeping is a `lesson` line or a Case on a Rule page (case 272.1).

`wiki/ratification.md` — the Render of `rule-ratification`, loaded by `/hi` and read whole by `case-guppi`, so both agents hold what each of them needs: the one rule, the form of the ledger lines, atomicity and the harness (case 595). What the main agent alone does is `orchestration.md`; the form of a Case is `case-schema.md`. A session without `/hi` holds no Case: the ledger hook refuses it. A Case is ratified by the person's reply in the chat — a sign-off, a question or their own alternative —, never by a picker tool, and ratifying a parent does not ratify its children.

<!-- rule-atomicity -->
## Atomicity — when a unit splits

A unit stays whole as long as its closing act — ratification, a reading, `built` — is one indivisible judgment. The moment it breaks into two or more conditions that can fail independently and need different fixes, it splits into children.

The test is mechanical. List the conditions of "done". For each pair, ask: could one fail while the other passes, and would the fix be a different one? Yes for any pair — split.

It holds for a Case, an Entity, a Rule and an Estimate alike. Not for a Lesson: a recorded fact does not split. Not for an Insight: it is born by clustering, which is this rule running in reverse. Depth is not fixed in advance — it follows the rule and nothing else. Two conditions that are different behaviours are two children; the same behaviour checked from two angles is one page and two Estimates.
<!-- /rule-atomicity -->

## What a Case produces

| Outcome | Ledger line |
|---|---|
| ratified decision | `- decision[case 12][update][rule-x]{ref:rule-x}` or `- decision[case 12][create][rule-y]{ref:rule-x}{tags:a,b}` |
| a measurement taken | `- estimate[slug][passed\|failed] <date, command or place; the result>` (case 199) |
| something learned | `- lesson[error\|knowledge][slug]{tags:a,b} trigger: <...> root_cause: <...>` |

The id is `case N` — the word and a space — in the first bracket and in `{supersedes:case N}` alike. N is the id of the sprint, a hyphen and the number of the Case in that sprint, from 1 in each sprint, with a dot for each sub-case level, such as `case kir-plugin-12.1`; a sprint id holds no dot and starts with the GitHub name of its author, so two people never share one. An N with no sprint part, such as `case 785.1`, is a Case from before sprint ids, and the sprints `migration` and `plugin` keep that form to their close: every reader takes both forms, and no such id is renamed. `uv run --project .guppi guppi caseid --next --session <stamp>`, `<stamp>` the stamp of the `hi:` line of the session, prints the id of the next Case of the open sprint and holds it in the store of the session's plan file, and prints no id without `--session` or without that plan file, and the opening Case of a sprint is `<id>-1` (case 788.2). In a line, `{source:...}` and `{supersedes:...}` are present only when they apply (case 75.1), and a line carries one `{supersedes:case N}` block per Case it supersedes, several side by side, never a list inside one block (case 429); `{addresses:<lesson slug>}` stands on a decision line whose Case closes the root cause of a lesson of this session — written when the lesson line already stands in the session's ledger, one mark per lesson; a lesson line written after the Case of this session that closed its cause carries `{addressed_by:case N}` instead, naming that Case — for a Case with sub-cases the sub-case whose decision line closes the cause, since the parent has no decision line and the ledger hook refuses a mark with no decision line of its Case before it (case 497.4) — one of the two marks per pair, by the order of the lines (case 379); a lesson whose fix is ratified in another session gets no mark (case 284.2).

**Decision lines are markup only** — their content already sits ratified in the Spec, so the
line just names what happens to which page, and the tags a `create` was ratified with.

**Estimate and lesson lines carry their text inline.** Their content is born in the moment
and exists nowhere else: a measurement taken after the tests were written, a failure
understood while still fresh. There is nothing in the Spec to point at.

An `estimate[...]` line does not replace the `decision[...]` that created the page — the
decision made it exist, the estimate line fills it.

Only the **main agent** writes ledger lines. A subagent that takes a measurement returns it; the main agent records it. A subagent that hits a fork stops and returns — it never decides.

Ledger lines are written by the `Stop` hook, from the reply, verbatim, each with the time of writing. A record is a `- decision[...]`, `- estimate[...]` or `- lesson[...]` line inside a fenced block opened with the `LEDGER` tag; the same line anywhere else — bare, or in a block with another tag or none — is a preview and is never written. A `create` line carries the ratified tags: `{tags:a,b}`. A lesson line whose tag `tags.md` does not hold declares it by one `{newtag:<tag>|<meaning>|<aliases>}` block per new tag, before `trigger:`, the tag also in its `{tags:...}`, the meaning one line and the aliases the Russian words for it; the ledger hook writes the line, and the librarian's run adds the row to `tags.md` (as set in case 827.3). A `knowledge` lesson line carries `{source:...}`, the url or reference the lesson studied — a file of the harness, a probe, a client version; the schema requires it, and a line without it is `incomplete: [source]` in the yaml and a lint finding on the page. An `error` lesson never carries one. When each line is written, and what a reply that carries a `LEDGER` block does after it, is `orchestration.md`.

## The harness

The harness — hooks, skills, agents, `settings.json`, `CLAUDE.md`, this file, `orchestration.md` and `case-schema.md` — is rendered from `rules/`. A harness file changes through an `update` of its Rule page, never by hand; a hook refuses the edit.
