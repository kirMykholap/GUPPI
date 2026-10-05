## Case 677 — The idea that a complaint becomes a lesson leaves the backlog

> **context:**
> The draft `rule-complaint-becomes-a-lesson` keeps an idea of session 0137 in the backlog: after each reply of the person a hook asks whether the reply holds a complaint about the agent's text or work, and a complaint becomes a lesson line. Case 504 put it off as a placeholder, and nobody ever decided it; the page holds only its Purpose. The main agent proposed to delete it while the backlog was reviewed, since Retro already writes a lesson line for a finding by its own judgment (`rule-retro`), and `estimate-agent-writing-followed` already takes the person's complaint as the test of the agent's text. The person agreed to close it as proposed. So this Case deletes the draft page and adds no hook, no rule and no Estimate.
> The vault's answer: the Case creates no page, so no vault query on a `create` ran. The Frontier line has the source `backlog`, and the page carries `deferred_by` the Decision of case 504, so the delete line carries `{supersedes:case 504}`, as case 675 did for the draft it deleted. The page has no `estimates` and is governed by no code.
> The frame. A Grep `rule-complaint-becomes-a-lesson` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed 3 files: `vault/wiki/brief.md`, `vault/wiki/backlog.md` and `vault/wiki/log.md`. The librarian writes `backlog.md` and `brief.md` from the pages, and `log.md` is history; they were not read, and they stand. The deleted page carries no promise. `estimate-backlog-renders` checks that `## Deferred` of `backlog.md` lists each live page with `deferred_by`; once the page is gone it is not listed, so its Criterion stays true and stands, and it checks this Case. The `make lint` of the librarian's run checks that no live page links to the deleted page.

> **problem:**
> A draft page holds in the backlog an idea that was never decided and that the person no longer wants to keep: a hook that turns each complaint of the person into a lesson line.

> **recommend:**
> - Recommended: delete the draft page; Retro already writes lessons and the person's complaint already tests the agent's text.
>   Answer: ratified as built

> **given:**
> `rule-complaint-becomes-a-lesson`: the draft page of the backlog item, which this Case deletes.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which deletes the page and retires its defer.
> **＋** `vault/wiki/backlog.md`: the backlog that lists a deferred page with its purpose.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decisions of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `rule-complaint-becomes-a-lesson` no longer stands under `vault/wiki/`.
> **＋** `vault/wiki/backlog.md` no longer lists it under `## Deferred`.
> **－** No hook asks after a reply of the person whether it holds a complaint.

> **tasks:**
> - [ ] delete `rule-complaint-becomes-a-lesson`
>   - impact: `the draft of the backlog leaves; no hook turns a complaint of the person into a lesson line; Retro writes lessons by its own judgment as rule-retro sets it; the defer of case 504 is retired by the supersedes mark of this line`

> **ratification:**
> ```
> - decision[case 677][delete][rule-complaint-becomes-a-lesson]{ref:rule-complaint-becomes-a-lesson}{supersedes:case 504}
> ```
