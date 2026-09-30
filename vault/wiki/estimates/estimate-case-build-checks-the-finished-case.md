---
type: estimate
kind: QA
status: failed
target: "[[rule-case-build]]"
purpose: Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the sub-cases that change one page — counted by what ask-guppi still finds at pre-spec
method: "by hand: at /pre-spec of a later session after the render, the report of ask-guppi read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, two sub-cases whose texts on one page contradict; the count of each in the reading line"
checked: 2026-09-30
origin: raw/2026-09-30/1306/ledger.md#case-544.1
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.

Then:
It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one.
**＋** Where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
**＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit.
**＋** For a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
**＋** Each hit that the change makes false enters the Case, or its `context` says why it stands, and a claim of `context` about every text names the search it rests on.
**＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
**－** A hit in a History line, in `log.md` or in `brief.md` is not read.

## Result

2026-09-30, by hand, the report of ask-guppi at /pre-spec of session 1736 read for Cases 547, 548, 549, 550 and 552 that case-guppi built: 0 Cases that depart from a chosen option; 0 pairs of sub-cases whose texts on one page contradict; 1 frame hit found by meaning and missed — Case 547 widened the Frontier rule to the first reply of /hi, whose form rule-skill-hi sets and estimate-hi-writes-frontier reads, and neither stood in the Case; and 2 claims of context not borne out by the search they name — Case 548 said the Grep for estimate-decisions-schema-checked finds only the page and brief.md (it finds brief.md, log.md and rule-decisions-schema), Case 552 listed the Grep hits of parse_line without three of them; 552.4 also contradicted itself on the payload error, fixed after the report

## History

- 2026-09-30 created · [[decision-case-544.1]]
- 2026-09-30 status: pending → failed · raw/2026-09-30/1736/ledger.md#L38
