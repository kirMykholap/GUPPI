## Case 458 — A round of questions keeps its grill-me form when it is shown in Russian

> **context:**
> When `case-guppi` has a fork open, it answers with a round of questions in the form of `.claude/skills/grill-me/SKILL.md`. Each question opens with `❓ **Qn** - **<title>**:` and closes with a `➡️` line that holds the recommended answer. The main agent translates the round into Russian and shows it. In session 1819, for Case 457, the main agent rebuilt the rounds into its own bold headings and a "Recommendation" line, and the markers were gone (`lesson-case-show-grill-round-reformatted-in-translation`). The Render of `rule-case-protocol` says only that a round is shown "translated into Russian, slugs, paths and quotations unchanged". It names no form to keep, and no hook reads a round: `casecheck --subagent` does not check or store an answer that has no Case heading, and the `Stop` hook compares only Cases.
> In the rounds, the person chose three answers. The rule is text only, with no hook. The round is kept line by line. The promise is the replaced Criterion of `estimate-case-protocol-shows-the-built-case`, whose round line already speaks of the showing. Its purpose is that a built Case is shown unchanged, and its method is by hand on the showings of a session, so its method stays. The Render sentence "In the chat one horizontal rule at most, after the Case or its last sub-case" would forbid a horizontal rule after a round, so the Case changes it too. `estimate-case-protocol-loaded` promises only that the file equals the Render, so it is not touched (case 378.5). `estimate-language-followed` speaks of the language of a round, not its form, so it stays as it is. `.claude/skills/grill-me/SKILL.md` and `.claude/agents/case-guppi.md` already write the form, so they do not change. No `create`, so no vault query ran.

> **problem:**
> The main agent can meet the rule and still lose the form of a round: it translates the round but rebuilds its questions into its own headings. The person then sees the questions without the `❓ **Qn**` and `➡️` markers. The agent's recommended answer also no longer stands apart from the question. No sentence of the vault tells the main agent to keep that form.

> **recommend:**
> Name the form in the Render of `rule-case-protocol`. The main agent shows a round line by line. Each question keeps its order, its number, its `❓ **Qn** - **<title>**:` opening and its `➡️` line. Its text is translated in place, nothing is merged, dropped or added, and the agent's own text stands after one horizontal rule. Replace the Criterion of `estimate-case-protocol-shows-the-built-case` whole to hold this. The error came from a missing sentence, not from ignoring one, so a text rule is enough for now. The rejected option was a `Stop` hook check on the count of markers. It needs `casecheck` to store rounds, which is a larger change and can be a later Case if the text rule fails again.

> **given:**
> `rule-case-protocol` — its Render, the paragraphs "Who builds a Case" and "Language", where a round is shown
> **＋** `vault/wiki/case-schema.md` — the file rendered from `rule-case-protocol`
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise of the showing, its Criterion replaced whole
> **＋** `.claude/agents/case-guppi.md` — the agent that builds a Case and writes a round
> **＋** `.claude/skills/grill-me/SKILL.md` — the form of a question in a round
> **＋** `rule-case-check` — the hooks that write the file of a Case and compare its showing
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of a Case that the main agent sends
> **＋** `.claude/agents/ask-guppi.md` — the vault query the main agent dispatches at pre-spec

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions or answers a shown Case with a question or a change, or a ratified Case changes and is shown again, in Plan Mode or in Work Mode.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case.
> **＋** An answer with no Case heading is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged — each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows the Case of an answer at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file the hook of `rule-case-check` wrote from the answer; in the same reply, under the heading of each Case and sub-case, it writes a short text in Russian on what the Case changes and the `ratification` section as the answer holds it, then its own text after one horizontal rule.
> **＋** A reply that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is sent and ratified again; the main agent edits no Case in the plan file.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` once, at pre-spec, and not before a showing.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: ``which the agent shows translated into Russian, slugs, paths and quotations unchanged, and no Case is shown``
>   - new: `` which the agent shows translated into Russian line by line, slugs, paths and quotations unchanged — each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule — and no Case is shown ``
>   - old: `after the Case or its last sub-case, and only when the agent's own text follows`
>   - new: `after the Case, its last sub-case or the last question of a round, and only when the agent's own text follows`
>   - change: `a round of questions of case-guppi is shown in Russian line by line, each question keeping its ❓ **Qn** and ➡️ lines (case 458)`
> - [ ] update `estimate-case-protocol-shows-the-built-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a round is shown in Russian line by line, in the form of grill-me (case 458)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-shows-the-built-case` — by hand, the rounds shown in a session after the render, against the answers of `case-guppi` in the transcript

> **ratification:**
> ```
> - decision[case 458][update][rule-case-protocol]{ref:rule-case-protocol}{addresses:lesson-case-show-grill-round-reformatted-in-translation}
> - decision[case 458][update][estimate-case-protocol-shows-the-built-case]{ref:estimate-case-protocol-shows-the-built-case}
> ```
