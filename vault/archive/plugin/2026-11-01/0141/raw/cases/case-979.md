## Case 979 — The builder recognises a hook, a command and a docstring list as a list and reports its search

> **context:**
> When a Case adds a member to a list that texts spell out one by one, `case-guppi` must search for a member already in that list, so it finds every text that names the members and can update each one. `estimate-case-build-reads-each-list-of-a-new-member` failed at the Retro of session 0431 (ledger line 47 of `vault/archive/plugin/2026-10-31/0431/raw/ledger.md`): the build of Case 956.1 added `guppi libreport` to the `SubagentStop` hooks and ran no such search, so its Case named the module docstring of `.guppi/guppi/cli.py` nowhere. That docstring lists the hook commands; a Grep for `libreport` over that file prints 3 lines, line 3 in that docstring among them. Work Mode later added the command there by hand. The paragraph of case 948.1 was in the agent file at that build: a Grep of its transcript `agent-ad69e15a458d77050.jsonl` for `list that texts spell out one by one` printed 3 lines, all reads of the paragraph, and a Grep for `adds a member|member of a list|new member|already in the list` printed only those reads, so the agent never reasoned about a member. The paragraph names four kinds of list, a key of an item, a kind, a status or a field, and a hook is none of them; and nothing in a finished Case shows whether the search ran. Cases 971 and 976 put the item off. The person chose that the series also names a hook of an event, a command and an item of a list in a comment or docstring of code. The person also chose that `context` names the search, and that the step stays in the check before the summary. This Case changes that sentence of the Render of `rule-case-build`, replaces the Criterion of the failed Estimate, and sets it `pending` with a reading after the first build of a later session whose Case adds a member to a list, since the new text reaches `.claude/agents/case-guppi.md` only at the render of the librarian's run. Its decision line on the Estimate carries one `{supersedes:...}` mark for each of Cases 971 and 976, so both defers are retired. The new Criterion keeps each line of the old one word for word but the `when`, which is replaced on purpose, since its series of kinds of list widens. A Grep for `a key of an item, a kind, a status or a field` over the repository outside `vault/raw/` and `vault/archive/` printed 3 files: `.claude/agents/case-guppi.md`, `vault/wiki/rules/rule-case-build.md` and `vault/wiki/estimates/estimate-case-build-reads-each-list-of-a-new-member.md`, so no other text holds the series. A Grep for `case-guppi\.md|rule-case-build\.md|agents/case-guppi` over `.guppi/tests/` printed nothing, so no test reads either file live. In `.guppi/links.md`, the block of `rule-case-build` names `estimate-case-build-checks-the-finished-case`. Its Criterion says that `context` names a search only when the Case rests on it, and it stands: the new sentence names the search as the one that the claim that no text listing the members is missed rests on. The block of the Estimate names `rule-hook-registry` only through its old `method`, which this Case replaces. The block of `.claude/agents/case-guppi.md` names no neighbour that the change makes false. The session's ledger holds no `error` lesson, so no `addresses` mark is written.

> **problem:**
> The builder misses the search for a member already in a list when the list is not one of the four named kinds, and nothing in the Case shows that the search was skipped.

> **recommend:**
> - **What changes so the search runs**
>   - Recommended: (b) name the missed kinds of list (a hook of an event, a command, a list in a comment or docstring of code), and have `context` report the search.
>   - Answer: agreed, (b).
> - **Where the step stands**
>   - Recommended: (a) it stays in the check before the summary.
>   - Answer: agreed, (a).
> - **When the check is read again**
>   - Recommended: (a) read it after the first later build that adds a member to a list.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule whose Render holds the step of the search.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from it.
> **＋** `estimate-case-build-reads-each-list-of-a-new-member`: the failed check of the step, its Criterion replaced whole.
> **＋** `vault/wiki/`: the live pages searched, outside `decisions/`.
> **＋** `.claude/`: the harness searched.
> **＋** `.guppi/guppi/`: the code searched, its comments and docstrings included.
> **＋** `log.md`: the log of the vault, `vault/wiki/log.md`, whose hits are not read.
> **＋** `brief.md`: the brief of the vault, `vault/wiki/brief.md`, whose hits are not read.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that adds a member to a list that texts spell out one by one, such as a key of an item, a kind, a status, a field, a hook of an event, a command or an item of a list in a comment or a docstring of code, and is about to answer with its summary.

> **then:**
> It searches the live pages of `vault/wiki/` outside `decisions/`, `.claude/` and `.guppi/guppi/` for a member that stands in the list already.
> **＋** It reads each hit that lists the members of the list.
> **＋** A hit in a comment or a docstring of code under `.guppi/guppi/` that lists the members is read like a hit in a page.
> **＋** Each text that lists the members and would miss the new member enters the Case, or the `context` of the Case names it and says why it stands.
> **＋** The `context` of the Case names that search: the member it searched for, its pattern, its paths, and each file it printed or the count it printed.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` When the Case adds a member to a list that texts spell out one by one — a key of an item, a kind, a status or a field — Grep the live pages of `vault/wiki/` outside `decisions/`, `.claude/` and `.guppi/guppi/` for a member that stands in the list already, since the new member stands in no text yet, and read each hit that lists the members; a hit in a History line, in `log.md` or in `brief.md` is not read; each text that would miss the new member enters the Case, or `context` names it and says why it stands (as set in case 948.1). ``
>   - new: `` When the Case adds a member to a list that texts spell out one by one — a key of an item, a kind, a status, a field, a hook of an event, a command, or an item of a list in a comment or a docstring of code — Grep the live pages of `vault/wiki/` outside `decisions/`, `.claude/` and `.guppi/guppi/` for a member that stands in the list already, since the new member stands in no text yet, and read each hit that lists the members, a comment or a docstring of code included; a hit in a History line, in `log.md` or in `brief.md` is not read; each text that would miss the new member enters the Case, or `context` names it and says why it stands; `context` names that search, with the member it searched for, its pattern, its paths, and each file it printed or the count it printed, since the claim that the Case misses no text that lists the members rests on it (as set in cases 948.1 and 979). ``
>   - change: `the search for a member already in a list names a hook of an event, a command and a list in a comment or docstring of code, and context names that search`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] update `estimate-case-build-reads-each-list-of-a-new-member`
>   - set:
>     ```
>     status: pending
>     purpose: Whether case-guppi, when its Case adds a member to a list that texts spell out one by one, a hook of an event, a command or a list in a comment or docstring of code among them, searches for a member already in the list, enters each text that would miss the new member in the Case or names it in context, and names that search in context
>     method: "by hand, after the first build of case-guppi in a later session whose Case adds a member to a list that texts spell out one by one: the agent transcript of that build under ~/.claude/projects/ read for its search of a member that stands in the list already and the hits it read, and its case file read for each text that lists the members and for the search named in context, both against the Criterion, recorded in one estimate line with the transcript and the case file"
>     ```
>   - change: `the Criterion replaced whole — the list names a hook of an event, a command and a list in a comment or docstring of code, and context names the search; the purpose and method set anew, the reading after the first build of a later session that adds a member to a list`
> - [ ] read `estimate-case-build-reads-each-list-of-a-new-member`

> **ratification:**
> ```
> - decision[case 979][update][rule-case-build]{ref:rule-case-build}
> - decision[case 979][update][estimate-case-build-reads-each-list-of-a-new-member]{ref:rule-case-build}{supersedes:case 971}{supersedes:case 976}
> ```
