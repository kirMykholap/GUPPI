## Case 543 — Two faults in the form of a round of case-guppi

> **context:**
> Two readings failed on the rounds of questions that `case-guppi` writes. First, `estimate-case-build-writes-a-plain-round` failed because the first round on Case 534 ended, after its last question, with a list of the files the agent checked, named by session ids alone. The frame `.claude/agents/case-guppi.md`, rendered from `rule-case-build`, already says that a round holds nothing else but the context of a first round. But Claude Code also gives every sub-agent a general note: in its final response, share the file paths that are relevant to the task. The frame does not say that this note does not apply to a round. The list does not help the person, and it does not help the main agent either: the main agent shows the round translated line by line, it reads none of those files to do so, and it asks `case-guppi` for a fact when it needs one.
> Second, `estimate-skill-grill-me-asks-in-rounds` failed because the label `**Options:**` came out indented by four spaces in most rounds. This session saw the same in the rounds on Cases 541 and 542. Markdown shows a line indented four spaces after a blank line as code. The cause is the question template of `.claude/skills/grill-me/SKILL.md`, rendered from `rule-skill-grill-me`. The whole template is an indented code block, and its Options label has eight spaces where the `**Now:**` line and each option have four. `case-guppi` copies it as it stands.
> The eight spaces came from the page writer. `replace_hits` of `guppi/generate.py` splits the `old` of a pair into its words and joins them with any whitespace, so the leading spaces of `old` are never matched. The pair of case 511.1 had an `old` that opened with four spaces and a `new` that opened with four spaces. The match started at the first word, so the page kept its four spaces and `new` added four more. Pre-spec replays each pair by the same function (`check_pairs` of `guppi/prespec.py`), and the Case check hook of `rule-case-check` runs the same checks through `judge`. So neither of them could see the doubled indent. No live `materialize.yaml` under `vault/raw/` holds a pair whose `old` or `new` opens with whitespace, so no signed pair waits on the old matching.
> In the frame, `estimate-case-build-writes-the-case` already promises that a round holds nothing else. Its Criterion stands, and so does that of `estimate-case-build-writes-a-plain-round`: the person chose to replace no Criterion for the note after a round. The Criterion of `estimate-skill-grill-me-asks-in-rounds` already asks for the label alone on its line, so it stands too. `estimate-generate-writes` promises a `replace` with whitespace collapsed and exactly one occurrence, and `estimate-prespec-simulates-the-pairs` promises a replay with whitespace collapsed as `generate` collapses it. Both stay true: the leading spaces never make an anchor miss or hit twice. So the new promises go to new Estimates, and those two Criteria are not replaced. The Criterion of `estimate-case-check-sends-back-a-faulty-case` says the hook runs `judge` of `guppi/prespec.py`, so a new finding of `judge` reaches it with no change there. Both new slugs are free, and each `create` carries a `ref`, so no vault query ran. No open backlog line of the Frontier names a page of this Case.

> **problem:**
> A round of `case-guppi` can end with a list of files, because a general instruction of Claude Code asks for one and the frame does not set it aside. The grill-me template shows the `**Options:**` label four spaces too deep, so each round shows it as code. The writer made that indent: the leading spaces of an `old` are never matched, and the leading spaces of a `new` are added after the ones on the page. Neither pre-spec nor the Case check catches a pair that doubles an indent.

> **recommend:**
> Four sub-cases, one promise each. The frame says that a round ends with the recommendation of its last question (543.1). The template line gets its four spaces back (543.2). The writer takes the spaces and tabs before the first word of an `old` that opens with them, and the schema of a Case says so (543.3). Pre-spec, and with it the Case check hook, reports a pair whose `new` opens with spaces or tabs while its `old` opens with neither (543.4). The person chose these in the rounds. They rejected keeping the list after a round, because it would need an exception in two rules for text nobody uses. Matching the leading spaces exactly was rejected because it could make a pair that hits today miss.

### Case 543.1 — A round of case-guppi ends with its last question

> **given:**
> `rule-case-build` — the rule whose Render is the frame of `case-guppi`
> **＋** `.claude/agents/case-guppi.md` — the frame rendered from it

> **when:**
> `case-guppi` answers with a round of questions, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> The round ends with the `➡️` line of its last question and the lines of a list under it.
> **＋** No horizontal rule, no list of the files `case-guppi` read and no note stand after it, even where a general instruction of Claude Code asks a sub-agent to share file paths.
> **－** A first round still opens with its `**Context:**` paragraph before its first question.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `no step of confirmation follows the last round.`
>   - new:
>     ````
>     no step of confirmation follows the last round. A round ends with the `➡️` line of its last question and the lines of a list under it: no horizontal rule, no list of the files you read and no note stand after it, even where a general instruction asks you to share file paths.
>     ````
>   - change: `a round of case-guppi ends with its last question: no list of files and no note after it (case 543.1)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-writes-a-plain-round` — in a later session after the render: one first round and one later round of `case-guppi` read in the chat against the Criterion

> **ratification:**
> ```
> - decision[case 543.1][update][rule-case-build]{ref:rule-case-build}
> ```

### Case 543.2 — The Options label of the grill-me template stands at the indent of the other lines

> **given:**
> `rule-skill-grill-me` — the rule whose Render is the grill-me skill and its question template
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill rendered from it
> **＋** `.claude/agents/case-guppi.md` — the agent that loads the skill by its `skills` field

> **when:**
> `uv run guppi render` writes `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`, and `case-guppi`, which loads it by `.claude/agents/case-guppi.md`, answers with a round of questions.

> **then:**
> In the question template the label `**Options:**` stands at the indent of the `**Now:**` line and of each option.
> **＋** In a round the label stands alone on the line before the first option, at column 0, and shows as bold text, not as code.
> **－** No other line of the template changes.

> **tasks:**
> - [ ] update `rule-skill-grill-me`
>   - old:
>     ````
>     > <the quoted words, as the source holds them>
>
>             **Options:**
>     ````
>   - new:
>     ````
>     > <the quoted words, as the source holds them>
>
>         **Options:**
>     ````
>   - change: `the Options label of the question template stands at the indent of the other lines (case 543.2)`
> - [ ] `uv run guppi render`: `.claude/skills/grill-me/SKILL.md`
> - [ ] read `estimate-skill-grill-me-asks-in-rounds` — in a later session after the render: `uv run guppi render --check`, then one round of `case-guppi` read in the chat against the Criterion

> **ratification:**
> ```
> - decision[case 543.2][update][rule-skill-grill-me]{ref:rule-skill-grill-me}
> ```

### Case 543.3 — A replace old that opens with spaces takes the spaces before its first word

> **given:**
> `rule-page-generation` — the rule of the writer of pages
> **＋** `guppi/generate.py` — `replace_hits` and `replace_once`, the one matching rule of a `replace` pair
> **＋** `guppi/prespec.py` — `check_pairs`, which replays the pairs by the same function
> **＋** `tests/test_generate.py` — the tests of the writer
> **＋** `rule-case-protocol` — the schema of a Case, whose Render is `vault/wiki/case-schema.md`
> **＋** `vault/wiki/case-schema.md` — the schema rendered from it
> **＋** `estimate-generate-replace-takes-the-leading-indent` — the promise this sub-case creates

> **when:**
> `guppi generate` applies a `replace` pair of an `update` entry to a page, or `check_pairs` of `guppi/prespec.py` applies it to a copy of the page, both by `replace_once` of `guppi/generate.py`.

> **then:**
> An `old` that opens with a space or a tab matches, besides its words, every space and tab on the page just before its first word, and `new` takes their place.
> **＋** An `old` that opens with neither matches from its first word, and the spaces and tabs before it on the page stay.
> **＋** Between the words of `old` whitespace stays collapsed: a line break matches any whitespace.
> **－** The spaces and tabs before the first word never make an anchor miss or hit twice: a pair that hits the page once without them still hits it once.

> **tasks:**
> - [ ] update `rule-page-generation`
>   - change: `a replace old that opens with spaces or tabs takes the spaces and tabs before its first word on the page (case 543.3)`
> - [ ] create `estimate-generate-replace-takes-the-leading-indent`
>   - ref: `rule-page-generation`
>   - kind: `QA`
>   - purpose: `Whether a replace pair whose old opens with spaces or tabs leaves the indent of its new on the page, and no indent added twice`
>   - method: `pytest in tests/test_generate.py against a temp vault: an old that opens with spaces over an indented line, one that opens with none, and one whose hit count is the same with and without its leading spaces`
>   - tags: `[harness, workflow]`
> - [ ] update `rule-case-protocol`
>   - old: `and one that misses or hits twice fails the entry)`
>   - new:
>     ````
>     and one that misses or hits twice fails the entry; an `old` that opens with spaces or tabs takes the spaces and tabs before its first word on the page too, so the indent of `new` replaces them, and a `new` that opens with spaces or tabs takes an `old` that opens with them, or pre-spec reports the pair — case 543)
>     ````
>   - change: `how the leading spaces and tabs of a replace pair match (case 543.3)`
> - [ ] `guppi/generate.py`: in `replace_hits`, an `old` that opens with a space or a tab gets a pattern that takes the spaces and tabs before its first word; the docstrings of `replace_hits` and `replace_once` say so
> - [ ] `tests/test_generate.py`: an `old` and a `new` that both open with four spaces over a line indented four spaces leave four; an `old` with no leading space leaves the page's spaces; the hit count of an anchor is the same with and without its leading spaces
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-generate-replace-takes-the-leading-indent`

> **ratification:**
> ```
> - decision[case 543.3][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 543.3][create][estimate-generate-replace-takes-the-leading-indent]{ref:rule-page-generation}{tags:harness,workflow}
> - decision[case 543.3][update][rule-case-protocol]{ref:rule-case-protocol}
> ```

### Case 543.4 — Pre-spec and the Case check report a pair that adds an indent twice

> **given:**
> `rule-prespec` — the rule of pre-spec, whose Render is `.claude/skills/pre-spec/SKILL.md`
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill rendered from it
> **＋** `guppi/prespec.py` — `check_pairs` and `judge`
> **＋** `guppi/generate.py` — the home of the predicate, beside the matching rule of a pair
> **＋** `tests/test_prespec.py` — the tests of pre-spec
> **＋** `rule-case-check` — its hook runs `judge` of `guppi/prespec.py` on each answer of `case-guppi`
> **＋** `estimate-prespec-catches-an-indent-added-twice` — the promise this sub-case creates

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads a plan whose Cases carry `replace` pairs, or the hook of `rule-case-check` runs `judge` of `guppi/prespec.py` over an answer of `case-guppi`.

> **then:**
> A `replace` pair whose `new` opens with a space or a tab while its `old` opens with neither gives one finding with its Case, the page's slug and the opening of its `old`.
> **＋** The predicate lives in `guppi/generate.py`, beside the matching rule of a pair, and `check_pairs` of `guppi/prespec.py` imports it.
> **＋** The hook of `rule-case-check` sends such a Case back to `case-guppi` before the person sees it.
> **－** A pair whose `old` and `new` both open with spaces or tabs, or whose `new` opens with neither, gives no such finding.
> **－** `guppi generate` applies such a pair as before: the finding stands at pre-spec and at the check of the Case only.

> **tasks:**
> - [ ] update `rule-prespec`
>   - old: `judged on its own and not applied to the copies (case 487.1).`
>   - new:
>     ````
>     judged on its own and not applied to the copies (case 487.1). It prints one line too for every `replace` pair whose `new` opens with a space or a tab while its `old` opens with neither, with its Case, the page's slug and the opening of its `old`: the page keeps its own indent before the match, and the indent of `new` would stand after it (case 543.4).
>     ````
>   - change: `pre-spec reports a replace pair whose new opens with spaces or tabs while its old does not (case 543.4)`
> - [ ] create `estimate-prespec-catches-an-indent-added-twice`
>   - ref: `rule-prespec`
>   - kind: `QA`
>   - purpose: `Whether pre-spec, and the Case check through judge, report a replace pair whose new opens with spaces or tabs while its old opens with neither`
>   - method: `pytest tests/test_prespec.py on a temp plan over temp pages: a pair whose new opens with spaces and old with none, one where both open with spaces, one where neither does`
>   - tags: `[harness, workflow]`
> - [ ] `guppi/generate.py`: a predicate beside `replace_hits` that says whether a pair adds an indent twice
> - [ ] `guppi/prespec.py`: `check_pairs` imports the predicate and gives the finding for each pair it judges true
> - [ ] `tests/test_prespec.py`: the three pairs of the method
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] read `estimate-prespec-catches-an-indent-added-twice`

> **ratification:**
> ```
> - decision[case 543.4][update][rule-prespec]{ref:rule-prespec}
> - decision[case 543.4][create][estimate-prespec-catches-an-indent-added-twice]{ref:rule-prespec}{tags:harness,workflow}
> ```
