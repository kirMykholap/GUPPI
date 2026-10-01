---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the rules that act at the moment the change sets, the Cases of the session its prompt names, the purpose and method of an Estimate whose Criterion it replaces, what each search printed, the sub-cases that change one page — counted by what ask-guppi still finds at pre-spec
method: "by hand: at /pre-spec of a later session after the render, the report of ask-guppi read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a rule acting at the same moment that the Case misses, a Case of the session named in the prompt whose page or moment the Case clashes with, an Estimate whose purpose or method still states the promise its replaced Criterion dropped, a claim of context that its search did not print, two sub-cases whose texts on one page contradict; the count of each in the reading line"
checked: 2026-10-01
origin: raw/2026-09-30/1306/ledger.md#case-544.1
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.

Then:
It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one; where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
**＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit; for a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
**＋** When the change sets what happens at a moment — a reply, a hook event, a command — it searches `vault/wiki/rules/` and `.claude/` for the words that name that moment, reads each passage of each hit that sets a form or a behaviour at that moment, and the Case either does not cover that moment or names the other rule in `given`.
**＋** It reads the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of each Case of the session that the prompt of its call names, and no other Case of the session; where that Case changes a page the Case changes or sets what happens at the same moment, the Case does not cover that moment or names the case file in `given`, and its new text of that page does not contradict the text of that Case.
**＋** When the Case replaces the Criterion of an Estimate, it reads the `purpose` and `method` of that Estimate, and the same `update` sets anew each one that states the old promise.
**＋** Each hit that the change makes false enters the Case, or its `context` says why it stands.
**＋** A claim of `context` about a text names the search it rests on: its pattern, the paths it ran over, and each file the search printed, a file it does not read included, or the count it printed; it claims nothing the search did not print.
**＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
**－** A hit in a History line, in `log.md` or in `brief.md` is not read.

## Result

2026-10-01, by hand, the report of ask-guppi at the /pre-spec of session 2356 over Cases 561 and 562 built after the render of session 2042: a Case that departs from a chosen option 0; a page made false that the Case missed 2 (561.13 missed estimate-hi-takes-its-readings and rule-skill-hi on the question of an A line; 561.3 left the purpose of estimate-prespec-hook-gates stating the old promise); a rule acting at the same moment that the Case missed 1 (562 refused the gathered list of the loop of 561.1 and 561.2, one turn after /pre-spec); a claim of context its search did not print 0; two sub-cases contradicting on one page 0; besides, 561.1 missed the defer of case 503 on rule-prespec and put the mechanism of a Leaf into its Purpose against rule-rules-schema

## History

- 2026-09-30 created · [[decision-case-544.1]]
- 2026-09-30 status: pending → failed · raw/2026-09-30/1736/ledger.md#L38
- 2026-09-30 updated: the Criterion replaced whole — the search for rules at the same moment, and a claim about a search that lists what it printed (case 557.1) · [[decision-case-557.1]]
- 2026-10-01 status: pending → failed · raw/2026-09-30/2356/ledger.md#L44
- 2026-10-01 deferred · [[decision-case-571]]
- 2026-10-01 updated: the Criterion replaced whole — the case files of the related Cases the prompt names, and the purpose and method of an Estimate whose Criterion is replaced; the defer of case 571 retired (case 579.2) · [[decision-case-579.2]]
