## Case 582 — The check of ask-guppi allows a list of file paths after the five lines

> **context:**
> `ask-guppi` is the read-only helper that searches the vault. Its frame, `.claude/agents/ask-guppi.md`, rendered from `rule-ask`, tells it to answer in exactly five lines: `exists`, `near`, `missing`, `rules` and the tags/slug line. Claude Code separately gives every sub-agent a general note: in its final response, share the file paths that are relevant to the task. On 2026-10-01, in session 1441, the check of `estimate-ask-finds` sent three dispatches. Two of the answers added a `Files:` list of six and five page paths after the five lines. The third, the Russian answer, held only the five lines. The Criterion says "exactly five lines" and "No index line or page text reaches the caller beyond them", so the Estimate failed (ledger line 33 of `raw/2026-10-01/1441/ledger.md`). The librarian's last report ended with the same kind of list even though its frame ends with "Nothing else". So the list comes from the general note, not from the frame of `ask-guppi`. A frame can set the note aside, as `.claude/agents/case-guppi.md` does (case 543.1), but the person chose not to compete with the note. The main agent sees only the helper's final answer, so the list is not otherwise in its context. Still, the list mostly repeats the pages the five lines name, and a slug gives its path. No rule reads the list, and no parser or hook reads the answer of `ask-guppi`, so nothing breaks. This Case replaces the Criterion of `estimate-ask-finds` whole. Its first line, which asked for an answer of exactly five lines, gives way to a line that asks for an answer that opens with them. A line is added that allows the list, and another that forbids anything else. The other lines are carried over unchanged. The `purpose` of the Estimate is set anew, since it promises an answer in five lines. The method of three dispatches read against the event log stays, because it states no form of the answer. In the frame, `rule-ask` and its render stay as they are. The render's line that asks for exactly five lines is an instruction to the agent, and it stays true: the five lines are still required. The list comes from an instruction outside the frame. The `## Purpose` of `rule-ask` says that the index lines and pages never enter the main agent's context, and a path is neither, so it stands. `rule-ask` carries `deferred_by: decision-case-553`, which is about reading Decision pages. This Case does not change `rule-ask`, so that defer stays open. The pre-spec dispatch set by `rule-prespec` asks `ask-guppi` three questions on the plan rather than for five lines. That gap is outside this item and stays. The search for the slug, pattern `estimate-ask-finds` over the repository outside `vault/raw/` and `vault/archive/`, printed these files:
> - `vault/wiki/log.md`
> - `vault/wiki/brief.md`
> - `vault/wiki/rules/rule-ask.md` (its `estimates` field)
> - `vault/wiki/lessons/lesson-agents-at-import-not-expanded.md` (its `source` line names an old reading)
> - `vault/wiki/estimates/estimate-ask-finds.md`
> - the Decision pages of cases 105.1–105.3, 147.1–147.8, 155, 391.1–391.2, 419.1–419.4, 476.1–476.4, 485.1–485.6 and 500.1–500.6
>
> None of the live hits is made false. The search for pattern `five lines` over the same paths printed these files:
> - `vault/wiki/brief.md`
> - `.claude/agents/ask-guppi.md`
> - `vault/wiki/estimates/estimate-ask-finds.md`
> - `vault/wiki/rules/rule-ask.md`
> - the Decision pages of cases 172, 398.1–398.3 and 399.1–399.5
>
> Of these, only the Estimate changes. The search for `ask-guppi` over `vault/wiki/rules/` printed these files:
> - `schema.yaml`
> - `rule-prespec.md`
> - `rule-case-build.md`
> - `rule-case-protocol.md`
> - `rule-skill-hi.md`
> - `rule-ask.md`
> - `rule-rules-schema.md`
>
> The search for `ask-guppi` over `.claude/` printed these files:
> - `.claude/skills/hi/SKILL.md`
> - `.claude/skills/pre-spec/SKILL.md`
> - `.claude/agents/case-guppi.md`
> - `.claude/agents/ask-guppi.md`
>
> Of these, only `rule-ask` and its render set the form of the answer. The person chose to leave the librarian's list out of this Case. No `create` is made, so no vault query ran.

> **problem:**
> The Criterion of `estimate-ask-finds` forbids anything after the five lines. A general note of Claude Code, which the vault does not control, makes `ask-guppi` add a list of file paths there in some answers. The check fails on text that breaks nothing. The question was whether the frame forbids the list or the check allows it.

> **recommend:**
> - **Forbid the file list in the frame, or allow it in the check**
>   - Recommended: (a) the frame forbids the list, with one sentence that sets aside the general note as the frame of `case-guppi` does, and the check stays strict.
>   - Answer: (b) the check allows the list. Before answering, the person asked two things. First, whether anyone uses the list, or whether it only repeats what is already in the context. The answer: the list is not otherwise in the main agent's context, but it repeats the pages the five lines name, and no rule reads it. Second, whether the vault should compete with an instruction of Claude Code it cannot change, or whether the list breaks anything. The answer: nothing breaks, and the choice is only how strict the form of the answer is. The person then chose to accept the list.
> - **Does this Case also cover the librarian's file list**
>   - Recommended: (a) only `ask-guppi`; the librarian's list stays, and it can be an item of its own later.
>   - Answer: (a) only `ask-guppi`.

> **given:**
> `estimate-ask-finds` — the promise of `ask-guppi`, its Criterion replaced whole
> **＋** `rule-ask` — the rule whose Render is the frame of `ask-guppi`, unchanged
> **＋** `.claude/agents/ask-guppi.md` — the frame rendered from it, unchanged
> **＋** `vault/wiki/rules/` — the rule pages whose index lines the agent searches first
> **＋** `vault/archive/` — the archive, where a named slug is checked by a Glob
> **＋** `vault/raw/<date>/event_log.md` — the log where each dispatch stands

> **when:**
> The main agent dispatches `ask-guppi` through the `Agent` tool with a question, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The answer opens with exactly five lines: `exists`, `near`, `missing`, `rules` and the tags/slug line, each present, "none" when empty.
> **＋** After the five lines a list of the paths of files the agent read may stand, as the general note of Claude Code asks of a sub-agent.
> **＋** The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** A question about an existing page names its slug under `exists`, whether it is asked in English or in Russian.
> **＋** A proposal that crosses a rule or a lesson, such as a `SessionStart` hook meant to block, names it on the `rules` line.
> **＋** A named slug gets on the tags/slug line `free`, `live` with its category, or `archived at <path> by [[decision-case-N]]`, found by a Glob over `vault/archive/`, N from the `origin` of the archived page.
> **＋** The agent opens an archived page only when the question names its slug and asks what it said or why it was withdrawn.
> **＋** Each dispatch stands in `vault/raw/<date>/event_log.md`.
> **－** No index line, page text or other note reaches the caller beyond the five lines and that list of paths.
> **－** An answer with no list after the five lines holds the promise as well.
> **－** The archive is not searched by meaning: the `exists` and `near` lines name live pages only.

> **tasks:**
> - [ ] update `estimate-ask-finds`
>   - set: `{status: pending, purpose: "ask-guppi finds a page by meaning in either language, names the rule a proposal crosses and the state of a named slug, and answers in five lines, a list of the paths of the files it read allowed after them"}`
>   - change: `the Criterion replaced whole — a list of file paths may follow the five lines, as the general note of Claude Code asks of a sub-agent; nothing else follows them (case 582)`
> - [ ] read `estimate-ask-finds` — by hand in a later session: three dispatches of `ask-guppi`, one existing page asked in English and in Russian, one proposal that crosses a known rule, each read against the event log and the Criterion

> **ratification:**
> ```
> - decision[case 582][update][estimate-ask-finds]{ref:rule-ask}
> ```
