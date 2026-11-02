## Case 997 — The acknowledging reply translates its headings and labels

> **context:**
> When the person ratifies a Case, the main agent writes an acknowledging reply: the `LEDGER` block, a heading that says the Case is ratified, a paragraph of changes, a paragraph of notes and the Frontier. `## The acknowledging reply` of `rule-orchestration` names these parts by their English words in code spans and in bold, and says only at the end of its paragraph, in one short sentence, that headings and labels are in the language of the chat. In session 2227 the agent translated only the Case heading and wrote **Changes:**, **Notes:** and `## Frontier` in English in every acknowledging reply, so the reading L21 of that session set `estimate-orchestration-acknowledging-reply` `failed`; `lesson-acknowledging-reply-labels-left-in-english` (L25 of that session) gives the root cause. The person chose to rewrite the text, not to let the Criterion accept English labels: the paragraph now says first that the reply stands in the language of the chat, that the words in code spans and in bold are the names of the parts in the language of the repository, and that the reply writes each one translated, while slugs, paths, the `LEDGER` tag, the ledger lines and the word `STOP:` that opens a reply keep their own words; the rest of the `STOP:` line stands in the language of the chat, since `rule-prespec-onward` asks only that the reply open with `STOP:`, and line 45 of `rule-orchestration` puts the agent's own text in the language of the chat (a finding of `/pre-spec`). The new text names the languages by `{{chat_lang}}` and `{{documentation_lang}}`, which the render fills from `rule-guppi-config` (`.guppi/guppi/render.py`, lines 14–21), so it writes no Russian word and keeps the promise of `estimate-clean-branch-ships-neutral-texts` that shipped texts name the languages by their role; the rule that governs the choice is `## Language` of `CLAUDE.md`, the Render of `rule-language`: the chat with the owner is in the language of the chat, and only technical terms stay in English, which these labels are not. By the person's choice the fix covers every reply of the Render that shows the Frontier: the reply that closes a Frontier line with no ratification, the reply that acknowledges Cases ratified together (`## Showing and signing a Case`), the reply that carries a defer (`## The short form — deferred decisions`) and the reply that acknowledges the opening Case of `/sprint-open` now point to the translation the acknowledging reply sets, and the old closing sentence of the paragraph is dropped, its source kept in the new sentence; the replies of Cases ratified together and of a defer came in by a finding of `/pre-spec`. The `method` waits for the librarian's render and reads any acknowledging reply written after it, with no word `first`, as `method` in `rule-estimates-schema` sets it. The Criterion of `estimate-orchestration-defers-in-one-reply` says the reply shows the Frontier and sets no language, so it stands.
>
> No code reads these labels literally. A Grep for `Changes:|## Frontier|Notes:|— ratified` over `.guppi/guppi/` printed one hit, `.guppi/guppi/generate.py`, a docstring on Cases ratified after a line, which names no label; over `.claude/` it printed nothing; over `.guppi/tests/` it printed 4 files, `test_onward.py`, `test_generate.py`, `test_casecheck.py` and `test_ratified.py`, whose hits are sample replies built in the test itself, read from no live file, so the Case changes none of them. A Grep for `orchestration\.md|rule-orchestration` over `.guppi/tests/` printed `test_orchestration.py` and `test_onward.py`: `test_orchestration.py`, read whole, reads the live `vault/wiki/orchestration.md` only through `example`, which takes the blocks tagged `showing` and `defer`, and no pair of this Case touches them; `test_onward.py` reads the word `orchestration.md` in the stderr of the hook, not the file. A Grep for `acknowledg` over `.claude/` printed 4 files, `.claude/skills/work/SKILL.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/sprint-open/SKILL.md` and `.claude/skills/pre-spec/SKILL.md`: each names the moment of the acknowledging reply and points to `orchestration.md` for its form, and sets no heading or label, so each stands. A Grep for `## Frontier` over `vault/wiki/` printed `orchestration.md`, `brief.md`, `rules/rule-orchestration.md`, `lessons/lesson-acknowledging-reply-labels-left-in-english.md`, `estimates/estimate-orchestration-acknowledging-reply.md`, `estimates/estimate-orchestration-acknowledges-the-opening-with-the-frontier.md` and `estimates/estimate-orchestration-shows-the-frontier-after-a-closed-line.md`; a Grep for ``\*\*Changes:\*\*|\*\*Notes:\*\*|`Changes:` `` over `vault/wiki/` printed `brief.md`, `orchestration.md`, `lessons/lesson-acknowledging-reply-labels-left-in-english.md`, `estimates/estimate-orchestration-acknowledging-reply.md`, `rules/rule-orchestration.md` and `estimates/estimate-orchestration-says-when-a-rendered-change-lands.md`. The Criteria of `estimate-orchestration-shows-the-frontier-after-a-closed-line` (the form that `estimate-orchestration-acknowledging-reply` sets), `estimate-orchestration-acknowledges-the-opening-with-the-frontier` (the four parts of an acknowledging reply) and `estimate-orchestration-says-when-a-rendered-change-lands` (the paragraph `Changes:`) name the parts by those names and take their language from the Criterion this Case replaces, so they stand; `estimate-orchestration-asks-in-the-grill-me-shape` lets the labels of a question stand translated or not, a reply of another moment, and stands. The blocks of `rule-orchestration`, `vault/wiki/orchestration.md` and `estimate-orchestration-acknowledging-reply` in `.guppi/links.md` were read whole; no neighbour they name sets the language of these labels.
>
> `estimate-orchestration-acknowledging-reply` checks the change: its Criterion is replaced whole, its other lines kept, and the language line names each heading and label translated, so a reading cannot pass on the Case heading alone. Its `method` changes too, since `orchestration.md` changes only at the librarian's render after this session, and a reading at this Retro would read replies written under the old text: the reading waits for that render. Its `purpose` states no part of the language promise and stands. The last run of `uv run --project .guppi guppi check`, as `## Flags` of `vault/wiki/brief.md` reports it, printed `unread: failed` on `estimate-orchestration-acknowledging-reply` among 7 lines; the Estimate set `pending` leaves that line. The lesson stands in the ledger of session 2227, not of this session, so no `{addresses:...}` mark is written: a Grep of `vault/raw/2026-11-02/0039/` for `lesson\[error\]|\{addresses:` printed only `cases/case-997.md`, this file, whose `context` names the two patterns; the session's `ledger.md` does not stand yet.

> **problem:**
> The text of the acknowledging reply names its labels by English words and gives their language only at the end, so the agent copied the English words into a chat in another language, and the check of that reply failed.

> **recommend:**
> - **How the fix works**
>   - Recommended: (a) rewrite the text of `orchestration.md` so it says first that each heading and label is translated into the language of the chat, the words in code spans being only the English names of the parts.
>   - Answer: agreed, (a).
> - **Which replies the fix covers**
>   - Recommended: (a) every reply in `orchestration.md` that shows the Frontier.
>   - Answer: agreed, (a).
> - **How done is checked**
>   - Recommended: (a) replace the Criterion of `estimate-orchestration-acknowledging-reply`, naming each label, and make its reading wait for the librarian's render.
>   - Answer: agreed, (a).

> **given:**
> `rule-orchestration`: the Rule page whose Render sets the acknowledging reply and the replies that show the Frontier.
> **＋** `vault/wiki/orchestration.md`: the file rendered from it, which the main agent follows.
> **＋** `estimate-orchestration-acknowledging-reply`: its Criterion and its `method` are replaced.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier that the reply shows.
> **＋** `rule-ledger-write`: the ledger hook that writes the `LEDGER` block.
> **＋** `rule-prespec-onward`: the hook that sends the agent on after `/pre-spec`.
> **＋** `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec`: the check of the `STOP:` line.
> **＋** `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`: the check of a decision line the ledger hook holds.
> **＋** `CLAUDE.md`: its `## Language` sets the language of the chat.

> **when:**
> The person ratifies a Case, ratifies again a Case shown again after its ratification, or ratifies in one answer Cases shown together, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The reply has four parts, in this order. First, the `LEDGER` block, before which stands nothing but the `STOP:` line that `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` checks. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist.
> **＋** Each heading and label of the reply stands translated into the language of the chat that `CLAUDE.md` sets: the heading `## Case N — ratified`, the labels `Changes:` and `Notes:` and the heading `## Frontier` stand in that language, not in the English words by which this Criterion names them.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** The open `W` lines are folded into one line that lists their ids, and each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` is open, the question which item is next ends the reply.
> **＋** When none is open before `/pre-spec`, the question whether to go on to `/pre-spec` ends the reply, in the plain form of the question which item is next. The agent calls `/pre-spec` only after the person says to go on. A reply that answers a question of the person instead ends with the same question again.
> **＋** When none is open after `/pre-spec`, the reply ends with the Frontier and asks nothing, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** One reply acknowledges every Case and sub-case ratified in one answer, a Case with its sub-cases or Cases shown together for one ratification: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names their ids, one paragraph `Changes:`, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** Slugs, paths, the tag of the `LEDGER` block, the ledger lines and the word `STOP:` that opens a reply keep their own words in any language of the chat; the rest of the `STOP:` line stands in the language of the chat.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written, but for a decision line the ledger hook holds, as `estimate-ledger-write-holds-a-decision-line-off-the-stored-case` sets it.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` comes in the turn that the answer `**Dropped:**` of that `case-guppi` opens (case 701.6): a heading `## Frontier`, the lines of `frontier.md` as a checklist in its form ``
>   - new: `` comes in the turn that the answer `**Dropped:**` of that `case-guppi` opens (case 701.6): a heading `## Frontier`, its word translated into {{chat_lang}} as `## The acknowledging reply` sets it, the lines of `frontier.md` as a checklist in its form ``
>   - old: `` The reply that acknowledges a ratification has four parts, in this order: the `LEDGER` block first, ``
>   - new: `` The reply that acknowledges a ratification stands in {{chat_lang}}, its headings and labels too: the words of its headings and labels in this paragraph, in code spans and in bold, are their names in {{documentation_lang}}, and the reply writes each one translated into {{chat_lang}} — the heading `## Case N — ratified`, the labels **Changes:** and **Notes:** and the heading `## Frontier` alike —, while slugs, paths, the `LEDGER` tag, the ledger lines and the word `STOP:` that opens a reply keep their own words, the rest of that line standing in {{chat_lang}} (as set in cases 167 and 997). It has four parts, in this order: the `LEDGER` block first, ``
>   - old: `Headings and labels in the language of the chat (case 167, supersedes 157). The reply that acknowledges the opening Case`
>   - new: `The reply that acknowledges the opening Case`
>   - old: `` its `## Frontier` shows the new Frontier; ``
>   - new: `` its `## Frontier`, translated as the acknowledging reply sets it above, shows the new Frontier; ``
>   - old: `` one heading `## Case N — ratified` naming their ids, one **Changes:** paragraph and one Frontier (case 598.2) ``
>   - new: `` one heading `## Case N — ratified` naming their ids, one **Changes:** paragraph and one Frontier, each heading and label translated as `## The acknowledging reply` sets it (case 598.2) ``
>   - old: `` then the Frontier with the line closed `[-] … · defer case N` ``
>   - new: `` then the Frontier, its heading translated as `## The acknowledging reply` sets it, with the line closed `[-] … · defer case N` ``
>   - change: `the acknowledging reply and each reply that shows the Frontier write their headings and labels translated into the language of the chat, the English words named as the names of the parts`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] update `estimate-orchestration-acknowledging-reply`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after the librarian's render that writes into vault/wiki/orchestration.md the paragraph of rule-orchestration that names the headings and labels of the acknowledging reply as translated: an acknowledging reply and a reply that acknowledges Cases ratified together in one answer, each written after that render, each read against the Criterion in the transcript of its session under ~/.claude/projects/"
>     ```
>   - change: `the Criterion replaced whole — each heading and label of the reply stands translated into the language of the chat; the reading waits for the render`
> - [ ] read `estimate-orchestration-acknowledging-reply`

> **ratification:**
> ```
> - decision[case 997][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 997][update][estimate-orchestration-acknowledging-reply]{ref:rule-orchestration}
> ```
