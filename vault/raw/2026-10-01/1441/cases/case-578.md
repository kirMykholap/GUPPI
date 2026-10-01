## Case 578 — A later Frontier folds the open Work lines into one line

> **context:**
> After the first reply of `/hi`, three kinds of reply show the Frontier, the checklist of `frontier.md`. They are the reply that closes a line with no ratification, the reply that acknowledges a ratification and the reply that records a defer. The first reply of `/hi` shows the Work list as one block. `rule-skill-hi` says the Work is one block. Every later Frontier follows the form that the acknowledging-reply paragraph of `rule-case-protocol` sets, and that paragraph says the open ones stand one per line with a short title. In session 1237 the main agent folded the open `W` lines into one line in the later replies too. So the reading of `estimate-case-protocol-shows-the-frontier-after-a-closed-line` failed, and the reading of `estimate-case-protocol-acknowledging-reply` failed on the same point. In session 1441 the later replies kept the rule and listed 28 `W` lines before the question about which Case is next. The person decided that folding the `W` lines is the norm and that the Estimate is what is wrong. They also decided that the fold covers every later Frontier of Plan Mode. The `W` lines are readings the agent closes at `/hi`, in Work Mode or at Retro. The person does not pick them, and `frontier.md` keeps the full list.
>
> The text of the form stands in one sentence of the Render of `rule-case-protocol`, in its acknowledging-reply paragraph. The paragraph on Plan Mode and the Frontier makes the reply that closes a line end "as the acknowledging reply ends", so one `replace` pair changes both replies. Sub-case 578.2 carries that pair and replaces the Criterion of `estimate-case-protocol-acknowledging-reply` whole. Sub-case 578.1 replaces the Criterion of `estimate-case-protocol-shows-the-frontier-after-a-closed-line` whole. That Criterion states the fold itself and does not only point to the other Estimate. The reply that records a defer has no line form of its own. Its Estimate, `estimate-case-protocol-defers-in-one-reply`, checks only that the Frontier stands with the deferred line closed and the question after it, so its Criterion stands. The closing line of the old Criterion of 578.1 already says that the defer reply keeps the form of the acknowledging reply. The first reply of `/hi` keeps its own form, and `rule-skill-hi` does not change.
>
> Item C2 of the Frontier also failed `estimate-case-protocol-acknowledging-reply` on the length of the `Changes:` paragraph. After this Case was ratified, the person took C2 up. They kept the rule of one or two sentences as it stands, with no Case, and judged the length point passed. `raw/2026-10-01/1441/frontier.md` now shows the line closed `[x] C2 … · brief · work`. So 578.2 keeps that rule word for word. No reading line on the length point could be written in this session, because 578.2 updates `estimate-case-protocol-acknowledging-reply` and the ledger hook refuses a reading of an Estimate that a decision line of the same session updates. The reading in a later session covers that point.
>
> The check of the answer noted Criterion lines that the two sub-cases do not carry word for word. Each was changed on purpose. The `when` of each Estimate gains the clause that the schema is rendered from `rule-case-protocol`. In 578.1 the line on the checklist is split, so that the fold of the `W` lines stands on a line of its own. In 578.2 the four-part line now ends at the checklist, and the fold moves to the lines after it. The check also noted that some `then` lines of 578.2 share most of their words with lines of 578.1. That is on purpose. Both Estimates promise one form of the Frontier and one rule for the question after it, so each Criterion says the same thing in the same words.
>
> No code reads the Frontier of a reply. A Grep of `Frontier` over `guppi/*.py` printed `casecheck.py`, `backlog.py`, `recall.py`, `generate.py`, `ratified.py`, `prespec.py`, `context.py` and `onward.py`. Their hit lines read `frontier.md` or describe it, and none of them judges the checklist a reply shows. So no old form is kept. The schema reaches the chat only at the render of the librarian's run, so until then the loaded `case-schema.md` still asks for one line per open item. No vault query was run, because no page is created.
>
> Searches:
> - A Grep of `one per line|one line per open|Work is one block` over `vault/wiki/` outside `decisions/` printed seven files: `brief.md`, `case-schema.md`, `rule-case-protocol`, `rule-skill-hi`, `rule-skill-grill-me`, `estimate-case-protocol-acknowledging-reply` and `estimate-case-protocol-shows-the-frontier-after-a-closed-line`. The hit in `rule-skill-grill-me` is the list rule of a round. It says nothing of a Frontier and stands. The hit in `rule-skill-hi` sets the first reply of `/hi`, which stays. `case-schema.md` is the render of `rule-case-protocol` and follows it. `brief.md` was not read.
> - A Grep of `## Frontier` over `vault/wiki/rules/` printed one file, `rule-case-protocol`. Over `.claude/` it printed no file.
> - A Grep of `Frontier` over `.claude/` printed three files: `.claude/skills/pre-spec/SKILL.md`, `.claude/skills/hi/SKILL.md` and `.claude/agents/case-guppi.md`. The skill `hi` is rendered from `rule-skill-hi`, which was read. The other two hits speak of the open lines that `/pre-spec` checks and of the Frontier item of a dispatch, and they set no form for a shown Frontier.
> - A Grep of `Frontier` over `vault/wiki/estimates/estimate-case-protocol-*.md` printed six files. Beyond the two Estimates replaced here and `estimate-case-protocol-defers-in-one-reply`, the hits in `estimate-case-protocol-asks-in-the-grill-me-shape`, `estimate-case-protocol-shows-the-built-case` and `estimate-case-protocol-loaded` speak of the question which item is next, of the item of a dispatch and of a History line. None of them speaks of the form of the open lines, so they stand. `estimate-hi-writes-frontier` sets the file `frontier.md` and not a reply, so it stands too.

> **problem:**
> The schema wants each open line of a later Frontier on its own line, while the first reply of `/hi` folds the Work list. So a long list of open readings pushes the question about the next item far down each reply, and the Estimates fail the fold the person holds to be correct. The question was whether a later Frontier may fold the open `W` lines, and which replies that covers.

> **recommend:**
> - **Should a later Frontier fold the open Work lines into one line?**
>   - Recommended: (b) fold the open `W` lines into one line that lists their ids, as `/hi` does; each open `C` and `A` line stays on its own line with its title, and `frontier.md` keeps the full list.
>   - Answer: (b). Folding the `W` lines is the norm, so the Estimate is what is wrong.
> - **Which replies does the fold cover?**
>   - Recommended: (a) every later Frontier in Plan Mode: the reply that closes a line, the acknowledging reply and the defer reply fold alike, and this Case replaces the Criterion of both Estimates.
>   - Answer: (a).

### Case 578.1 — The reply that closes a line folds the open Work lines

> **given:**
> `estimate-case-protocol-shows-the-frontier-after-a-closed-line` — the promise whose Criterion this sub-case replaces
> **＋** `rule-case-protocol` — the Case schema, whose Render makes this reply end as the acknowledging reply ends
> **＋** `vault/wiki/case-schema.md` — the file rendered from that Render
> **＋** `estimate-case-protocol-acknowledging-reply` — the promise of the form this reply takes
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier of the session
> **＋** `rule-skill-hi` — the rule of the first reply of `/hi`
> **＋** `/pre-spec` — the step of `rule-prespec`, which the reply calls when no line under `## Cases` is open
> **＋** `rule-prespec-onward` — the hook that sends the agent on when no line under `## Cases` is open

> **when:**
> After the first reply of `/hi` and before the end of Plan Mode, with `vault/wiki/case-schema.md` rendered from `rule-case-protocol`, the agent closes a line of `raw/<date>/<hi HHMM>/frontier.md` in a reply that carries no ratification and no defer. Examples are an `A` line closed by the person's answer, a `W` line closed by a reading, a `C` line that needs no decision, or an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept`.

> **then:**
> The reply ends with the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist, in the form that `estimate-case-protocol-acknowledging-reply` sets.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as they are closed.
> **＋** The open `W` lines are folded into one line that lists their ids.
> **＋** Each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
> **＋** When no line under `## Cases` is open, no question follows the Frontier: a reply with no `LEDGER` block calls `/pre-spec` after it, and a reply with a `LEDGER` block ends with the Frontier, for the hook of `rule-prespec-onward` to send the agent on.
> **＋** A reply that closes several lines shows one Frontier, after its `LEDGER` block when it carries one.
> **－** The first reply of `/hi` keeps the form that `rule-skill-hi` sets, the lines it closes included.
> **－** A line closed in Work Mode or at Retro shows no Frontier.
> **－** The reply that acknowledges a ratification and the reply that carries a defer keep their own form, as `estimate-case-protocol-acknowledging-reply` sets it.

> **tasks:**
> - [ ] update `estimate-case-protocol-shows-the-frontier-after-a-closed-line`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the open W lines are folded into one line that lists their ids; each other open line stands on its own line (case 578.1)`
> - [ ] read `estimate-case-protocol-shows-the-frontier-after-a-closed-line` — by hand, in a later session after the render, the first Plan Mode reply after the first reply of `/hi` that closes a line of `frontier.md` with no ratification and no defer

> **ratification:**
> ```
> - decision[case 578.1][update][estimate-case-protocol-shows-the-frontier-after-a-closed-line]{ref:rule-case-protocol}
> ```

### Case 578.2 — The acknowledging reply folds the open Work lines

> **given:**
> `rule-case-protocol` — the Case schema, whose Render sets the reply that acknowledges a ratification
> **＋** `vault/wiki/case-schema.md` — the file rendered from that Render
> **＋** `estimate-case-protocol-acknowledging-reply` — the promise whose Criterion this sub-case replaces
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier of the session
> **＋** `rule-ledger-write` — the ledger hook that writes the `LEDGER` block
> **＋** `rule-prespec-onward` — the hook that sends the agent on when no line under `## Cases` is open

> **when:**
> The person ratifies a Case, or ratifies again a Case shown again after its ratification, and the agent writes the reply that acknowledges it, with `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

> **then:**
> The reply has four parts, in this order. First, the `LEDGER` block. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** The open `W` lines are folded into one line that lists their ids, and each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` is open, the question which item is next ends the reply; when none is open, the reply ends with the Frontier and asks nothing, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** For a Case with sub-cases, one reply acknowledges every sub-case ratified: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names the ids, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** The headings and labels are in the language of the chat.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written.

> **tasks:**
> - [ ] update `rule-case-protocol` — the acknowledging reply folds the open `W` lines into one line of their ids
>   - old:
>     ````
>     the closed lines folded into one, the open ones one per line with a short title,
>     ````
>   - new:
>     ````
>     the closed lines folded into one, the open `W` lines folded into one line that lists their ids, the other open ones one per line with a short title (case 578.2),
>     ````
>   - change: `a later Frontier folds the open W lines into one line that lists their ids; the other open lines stand one per line (case 578.2)`
> - [ ] update `estimate-case-protocol-acknowledging-reply`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the open W lines are folded into one line that lists their ids; each other open line stands on its own line (case 578.2)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-acknowledging-reply` — by hand, the first acknowledging reply of a later session after the render

> **ratification:**
> ```
> - decision[case 578.2][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 578.2][update][estimate-case-protocol-acknowledging-reply]{ref:rule-case-protocol}
> ```
