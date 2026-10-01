## Case 550 — The parent Decision pages of session 0248 are kept as written

> **context:**
> Case 544.6 gave a Case with sub-cases a decision record of its own in `materialize`, and case 544.7 gave it a Decision page in `generate`. `materialize` goes over every session folder still under `raw/`, including folders it has processed before. So the librarian run of session 1306 added parent records to the older folder `raw/2026-09-30/0248/`, and `generate` wrote `decision-case-534`, `decision-case-538` and `decision-case-539` from them. The handoff of 1306 noted that nobody had decided this for Cases of earlier sessions. Each of the three pages holds the ratified `## Problem` of its Case and a `children` list of its sub-case pages. A Grep of `^(parent|## )` over the sub-case pages of 534, 538 and 539 found `## Problem` on each of them and `parent` on none. Those pages were written before 544, and the Criterion of `estimate-generate-writes-the-decision-page` says existing Decision pages are not rewritten. Parent Cases of archived sessions have no page. The other older folder under `raw/`, `raw/2026-09-30/0138/`, has no sub-case line in its ledger. `guppi archive` moves both older folders out at the first run on a later day (`rule-raw-archive`), so after that no folder from before 544 stays under `raw/`, and the code has no case left to limit. The three pages hold text no Case signed. Case 358 is the model for this: an `update` with `change` alone, which adds one `updated:` History line and changes nothing else. `rule-decisions-schema` allows that line for a Case that signs a page's text after the fact. That same schema text says a sub-case page carries `parent` and no `## Problem`, which the older sub-case pages contradict. The person keeps that sentence as it is: Decision pages move to the archive over time, and an added exception would stay behind to describe pages already archived. No Estimate is touched. The code of `materialize` and `generate` does not change, and the only thing that changes on the three pages is a History line. This Case creates nothing, so no vault query was run.

> **problem:**
> The librarian run of session 1306 wrote parent Decision pages for Cases 534, 538 and 539 of session 0248, and no Case decided that for Cases ratified before case 544. The question was whether to keep these pages, change them or remove them, and whether to limit the code that wrote them.

> **recommend:**
> - **What to do with the three parent pages**
>   Recommended: (a) keep them as they are; their sub-case pages keep no link back.
>   Answer: (a) keep them as they are.
> - **Should `materialize` be limited so that it adds no parent record to an older folder**
>   Recommended: (a) no code change; after the two older folders are archived, the case cannot happen again.
>   Answer: (a) no code change.
> - **Should `rule-decisions-schema` say how sub-case pages written before the new rule look**
>   Recommended: (a) add one sentence: a sub-case page written before case 544 keeps its `## Problem` and carries no `parent`.
>   Answer: (b) leave the text as it is. Decision pages move to the archive over time, and the added sentence would stay behind and describe pages that are already archived.

> **given:**
> `decision-case-534`, `decision-case-538`, `decision-case-539` — the parent pages that the librarian run of session 1306 wrote for Cases of session 0248
> **＋** `rule-decisions-schema` — a decision is not edited; one `updated:` History line of a Case that signs the page's text after the fact is allowed
> **＋** `guppi/materialize.py` — writes the parent record of a Case whose sub-cases stand in a folder under `raw/`
> **＋** `guppi/generate.py` — writes the Decision page of the record and applies an `update` with `change` alone as one History line

> **when:**
> The librarian's `uv run guppi generate` applies this Case.

> **then:**
> `decision-case-534`, `decision-case-538` and `decision-case-539` keep their fields and their `## Problem` as they stand, and the History of each gets one line `updated:` naming this Case as the one that signs the page after the fact.
> **－** The sub-case pages of Cases 534, 538 and 539 do not change: they carry no `parent` and keep their `## Problem`.
> **－** `guppi/materialize.py` and `guppi/generate.py` do not change.
> **－** The text of `rule-decisions-schema` does not change.

> **tasks:**
> - [ ] update `decision-case-534`
>   - change: `the parent page written for a Case of session 0248 by the librarian run of session 1306, kept as written and signed after the fact (case 550)`
> - [ ] update `decision-case-538`
>   - change: `the parent page written for a Case of session 0248 by the librarian run of session 1306, kept as written and signed after the fact (case 550)`
> - [ ] update `decision-case-539`
>   - change: `the parent page written for a Case of session 0248 by the librarian run of session 1306, kept as written and signed after the fact (case 550)`

> **ratification:**
> ```
> - decision[case 550][update][decision-case-534]{ref:decision-case-534}
> - decision[case 550][update][decision-case-538]{ref:decision-case-538}
> - decision[case 550][update][decision-case-539]{ref:decision-case-539}
> ```
