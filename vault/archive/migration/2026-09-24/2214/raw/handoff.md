# Handoff — 2026-09-24, the Spec of 1916 finished; Case 406; Case 407 deferred

## Notes from memory

- Case 406 went through three places. The first showing put the rule in `rule-case-protocol`. The person moved it to `rule-agent-writing`, then asked whether `CLAUDE.md` is the place at all: it must stay universal, working without `/hi`. The agent weighed `.claude/rules/` with `paths:` and advised against it — such a rule loads on a Read of a matching file, the Case is written in the chat, and the parked measurement of 2026-08-19 shows it does not come back after `/compact`. The person took `case-schema.md`. A path-scoped rule for text written into the vault outside a Case (the brief of `/carry`, the librarian's reports) was named as a possible Backlog item and not recorded.
- Case 407 was ratified with five sub-cases, then `ask-guppi` at pre-spec found contradictions in it; the person chose to take it out of the Spec by the defer Case 412 and spend the session on Work Mode. The findings stand in the `context` of 412; the next session answers them first.
- The person observed after Retro began:
  - The plugin showed `frame-guppi` on Opus. The subagent transcripts show all three dispatches on `claude-sonnet-5`; the one Opus dispatch was `ask-guppi` at pre-spec. The person accepts this, but holds that 160 thousand tokens is too much for Sonnet, which in their experience loses context past about 100 thousand, and proposes `frame-guppi` on Opus with `effort: medium` — the frontmatter field `effort` exists (code.claude.com/docs/en/sub-agents.md). Not confirmed by this session: `frame-guppi` got a paraphrase of Case 407, `ask-guppi` the exact plan text, so input and model are confounded. Input to defer 408.
  - The main context grew by about 70 thousand tokens around the check of Case 407: about 44 thousand were the agent's own reads before the dispatch, about 5 thousand the prompt and the report, about 21 thousand the showing of Case 407. The person proposes that `frame-guppi` write the Case itself from the item and the person's choice, a `SubagentStop` hook check its form (it receives `agent_transcript_path` and `last_assistant_message`, and can send the subagent back, not change its answer), and the main agent show it; the Stop hook of `rule-spec-write` copies it as today. Open: whether the showing in the chat may come from the subagent's answer rather than the main agent's text — that changes the form of ratification. Input to defers 408 and 412.
- Case 405 is ratified but not rendered; the defers of this session (408, 409, 412, 413) were already written in the reply that asked for them, as 405 says.

## Direct instructions to the librarian

- Two units to apply: `raw/2026-09-24/1916/` (its `carry.md` is removed in commit 2b21779, so it is no longer skipped) and `raw/2026-09-24/2214/`. Apply 1916 first: Case 406 of 2214 replaces the Criterion of `estimate-case-protocol-case-form` that Case 396.1 of 1916 replaces too, and the later text must stand.
- In 2214, Cases 407.1–407.5 and 410 are superseded by 412, and 411 by 413; their sections are not in the Spec. The parent heading of 407 stands in the ratified copy only; `prespec --check` reported it (`lesson-prespec-parent-of-superseded-sub-cases`).
- Several Cases change `rule-case-protocol`: 402 and 405 in 1916, 406 in 2214; the render of `vault/wiki/case-schema.md` follows them all.
- `rule-prespec` is deferred twice in 2214 (412 and 413) and `rule-spec-reconcile` by three lines of 412 with different `supersedes` — one `deferred_by` entry per Decision page.

## What actually got done

- Closed in Plan Mode: Case 406 (ratified); defers 408, 409, 412, 413. Frontier C1 left `[-] · sprint`; C2 closed `· work`, taken up by Case 402.
- Work Mode on the Spec of 1916: the code of Case 402 in `guppi/ratified.py` (`code_value` refuses an unpadded value holding a backtick, `read_tasks` gives the reason) and `tests/test_ratified.py` (the fixture `SHOWING` padded, two tests); `make test` 626 passed, 2 skipped; `make style` clean. The readings by `pytest` and `guppi render --check` stand in the ledger of 2214; `estimate-plan-mode-names-its-estimates` read by hand.
- Not done: the pages, renders and `guppi sprint` of both Specs — the librarian's; the reading of `estimate-case-protocol-case-form` (after the render, next session); the reading of `estimate-case-protocol-defers-in-one-reply` (at the first defer after the render).
