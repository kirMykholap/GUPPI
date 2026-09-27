## Case 466 — The first round of `case-guppi` on an item opens with a short context of the item

> **context:**
> When an item has an open fork, `case-guppi` answers with a round of questions in the form of `.claude/skills/grill-me/SKILL.md`. The main agent translates the round into Russian and shows it line by line. The Render of `rule-case-build` makes the round "its numbered questions ... with no Case heading and nothing else". The Render of `rule-case-protocol` has the main agent add nothing between the questions and put its own text only after the last question. So the round opens straight with `❓ **Q1**`. In session 2050 the first rounds for Cases 464 and 465 did this, and the person saw the questions with nothing to explain the item.
> In the rounds, the person chose these answers. `case-guppi` writes the context, because it has read the frame before it asks, and the main agent has not. Only the first round on an item carries it. The person's own `/grill-me` stays as it is, so `rule-skill-grill-me`, its Render and `estimate-skill-grill-me-asks-in-rounds` do not change. The context is one prose paragraph under the label `**Context:**`, with no fixed limit. Its parts follow the Language paragraph of `case-schema.md` (case 449): a sentence per part where one is enough, and a part with nothing to say left out, such as "where it goes wrong" for an item that is not a defect. The person judges its length.
> The change touches two promises, so there are two sub-cases (`rule-atomicity`). 466.1 covers the round `case-guppi` writes. 466.2 covers how the main agent shows it. `rule-case-check` neither checks nor stores an answer with no Case heading, and its `Stop` comparison reads only Cases. So a round with a context passes both hooks unchanged, if the context carries no Case heading. `.claude/settings.json` and `guppi/casecheck.py` do not change, and no code judges the form of a round. `estimate-language-followed` says a round of `case-guppi` is shown "translated from the answer". The context is part of the answer, so that line stays true. `estimate-case-protocol-loaded` promises three things: `case-schema.md` equals the Render, it stands in the context after `/hi`, and `CLAUDE.md` repeats no paragraph of it. None of these speaks of a round, so it is not touched (case 378.5). The Language paragraph of `case-schema.md` still holds. The Case has no `create`, so no vault query ran.

> **problem:**
> The first round on an item reaches the person with no framing. The person reads questions about a mechanism before being told what the item is, what goes wrong today, or what the round decides. No sentence of the vault lets `case-guppi` or the main agent put a context before the first question, and two sentences forbid it.

> **recommend:**
> Let the first round on an item open with one `**Context:**` paragraph, written by `case-guppi` and shown translated in place by the main agent before `❓ **Q1**`. Replace the Criterion of `estimate-case-build-writes-the-case` and of `estimate-case-protocol-shows-the-built-case` whole to hold this. `case-guppi` is the one agent that has read the pages and the code when it asks. The rejected option was a Russian text by the main agent, written from the Frontier line alone.

### Case 466.1 — `case-guppi` opens its first round on an item with a context paragraph

> **given:**
> `rule-case-build` — its Render, the paragraph on the forks and the round
> **＋** `.claude/agents/case-guppi.md` — the file rendered from `rule-case-build`
> **＋** `estimate-case-build-writes-the-case` — the promise of the agent, its Criterion replaced whole
> **＋** `.claude/skills/grill-me/SKILL.md` — the form of a question in a round, unchanged
> **＋** `vault/wiki/case-schema.md` — the form of the Case the agent reads first, and the Language paragraph the context follows
> **＋** `.claude/agents/ask-guppi.md` — the vault query the agent runs before a `create` without a `ref`
> **＋** `.claude/settings.json` — the hooks the agent reads for a Case that changes a hook
> **＋** `rule-case-check` — the `SubagentStop` hook that checks and stores only an answer with a Case heading

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
> **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
> **＋** When no fork is open, its answer is the Case whole in English in the chat form of `vault/wiki/case-schema.md`, from the heading to the fence of `ratification`, and nothing else.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** It runs on `model: opus` with `effort: medium` and the tools Read, Grep and Glob.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round.
> **－** It writes no file and no ledger line.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `in English, with no Case heading and nothing else.`
>   - new: `` in English, with no Case heading and nothing else but the context of a first round. The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out. A later round on the item, a round after a message on a Case you built and a round in Work Mode carry no context, and no context carries a Case heading. ``
>   - change: `the first round of case-guppi on an item opens with a short context of the item (case 466.1)`
> - [ ] update `estimate-case-build-writes-the-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the first round on an item opens with a Context paragraph (case 466.1)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-writes-the-case` — by hand, the first and a later round of a dispatch on an item with a fork, in a session after the render

> **ratification:**
> ```
> - decision[case 466.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 466.1][update][estimate-case-build-writes-the-case]{ref:estimate-case-build-writes-the-case}
> ```

### Case 466.2 — The main agent shows the context of a first round translated before its first question

> **given:**
> `rule-case-protocol` — its Render, the paragraph "Who builds a Case", where a round is shown
> **＋** `vault/wiki/case-schema.md` — the file rendered from `rule-case-protocol`
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise of the showing, its Criterion replaced whole
> **＋** `.claude/agents/case-guppi.md` — the agent that writes the round and its context
> **＋** `.claude/skills/grill-me/SKILL.md` — the form of a question in a round
> **＋** `rule-case-check` — the hooks that write the file of a Case and compare its showing
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of a Case that the main agent sends
> **＋** `.claude/agents/ask-guppi.md` — the vault query the main agent dispatches at pre-spec

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions or answers a shown Case with a question or a change, or a ratified Case changes and is shown again, in Plan Mode or in Work Mode.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case.
> **＋** An answer with no Case heading is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows the Case of an answer at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file the hook of `rule-case-check` wrote from the answer; in the same reply, under the heading of each Case and sub-case, it writes a short text in Russian on what the Case changes and the `ratification` section as the answer holds it, then its own text after one horizontal rule.
> **＋** A reply that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is sent and ratified again; the main agent edits no Case in the plan file.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` once, at pre-spec, and not before a showing.
> **－** The main agent writes no context of its own before the first question of a round.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `line by line, slugs, paths and quotations unchanged — each question in the order`
>   - new: `` line by line, slugs, paths and quotations unchanged — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order ``
>   - change: `the main agent shows the context of a first round translated in place before its first question (case 466.2)`
> - [ ] update `estimate-case-protocol-shows-the-built-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the context of a first round shown translated before its first question (case 466.2)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-shows-the-built-case` — by hand, the first rounds shown in a session after the render, against the answers of `case-guppi` in the transcript

> **ratification:**
> ```
> - decision[case 466.2][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 466.2][update][estimate-case-protocol-shows-the-built-case]{ref:estimate-case-protocol-shows-the-built-case}
> ```
