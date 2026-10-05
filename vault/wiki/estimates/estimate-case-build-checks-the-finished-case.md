---
type: estimate
kind: QA
status: failed
target: "[[rule-case-build]]"
purpose: Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the rules that act at the moment the change sets, the Cases of the session its prompt names, the purpose and method of an Estimate whose Criterion it replaces, what each search printed and that the context keeps only the searches the Case rests on, the sub-cases that change one page — counted by what ask-guppi still finds at pre-spec
method: "by hand: at /pre-spec of a later session after the render, the answers of the ask-guppi runs, one per top-level Case, read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a rule acting at the same moment that the Case misses, a Case of the session named in the prompt whose page or moment the Case clashes with, an Estimate whose purpose or method still states the promise its replaced Criterion dropped, a claim of context that its search did not print, a search in context that the Case does not rest on, two sub-cases whose texts on one page contradict; the count of each in the reading line"
checked: 2026-10-05
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
**＋** The `context` names a search only when the Case rests on it: a search with a hit that enters the Case, a search with a hit that stands and needs the reason why, or a search that a claim that no text says something rests on; a search that found nothing to change and that no claim rests on is left out.
**＋** A claim of `context` about a text names the search it rests on: its pattern, the paths it ran over, and each file the search printed, a file it does not read included, or the count it printed; just before it answers, it runs each search that `context` names again, with the pattern and the paths that `context` writes, and the files and counts in `context` are the ones that run printed, not the files it read during the build; it claims nothing the search did not print.
**＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
**－** A hit in a History line, in `log.md` or in `brief.md` is not read.

## Result

2026-10-05, in the Work Mode of session 0109, by hand: the first answers of the four ask-guppi runs at the /pre-spec of session 0109, one per top-level Case 638, 639, 640 and 641, each built by case-guppi after the render of .claude/agents/case-guppi.md by case 636: 0 Cases departing from a chosen option; 1 page whose text the change makes false missed (640: estimate-harness-pipeline lists the rules in no pipeline that the Purpose of rule-harness names); 4 rules bearing on the same moment missed (638: rule-agent-writing; 640: rule-page-read, rule-documentation with the librarian's frame, rule-claude-md) and 1 lesson (640: lesson-harness-a-paths-rule-misses-a-new-file-and-a-compaction); 1 clash with a Case named in the prompt (640: its context on the broken-rule line of Case 639); 0 Estimates whose purpose or method kept a dropped promise; 4 claims of context the vault or the transcripts do not bear out (638: the sentence counts and the lists of the 636 confirmation, both taken from the main agent's prompt; 639: two lists where the Result names one; 640: the librarian's `git` allowance); 0 searches in context the Case does not rest on; 0 contradicting sub-cases, no Case had sub-cases; besides, 2 Estimates not named that cover the new target of 641 (estimate-harness-make-runs-in-both-shells, estimate-tests-clock-pinned)

## History

- 2026-09-30 created · [[decision-case-544.1]]
- 2026-09-30 status: pending → failed · raw/2026-09-30/1736/ledger.md#L38
- 2026-09-30 updated: the Criterion replaced whole — the search for rules at the same moment, and a claim about a search that lists what it printed (case 557.1) · [[decision-case-557.1]]
- 2026-10-01 status: pending → failed · raw/2026-09-30/2356/ledger.md#L44
- 2026-10-01 deferred · [[decision-case-571]]
- 2026-10-01 updated: the Criterion replaced whole — the case files of the related Cases the prompt names, and the purpose and method of an Estimate whose Criterion is replaced; the defer of case 571 retired (case 579.2) · [[decision-case-579.2]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1725/ledger.md#L16
- 2026-10-04 updated: the Criterion replaced whole — the context names only the searches the Case rests on (case 629.5) · [[decision-case-629.5]]
- 2026-10-04 updated: the method reads the answers of the ask-guppi runs, one per top-level Case (case 634.1) · [[decision-case-634.1]]
- 2026-10-05 updated: the Criterion replaced whole — each search the context names is run again just before the answer, and its files and counts come from that run (case 636) · [[decision-case-636]]
- 2026-10-05 status: pending → failed · raw/2026-10-05/0109/ledger.md#L22
- 2026-10-05 deferred · [[decision-case-647]]
- 2026-10-05 deferred · [[decision-case-657]]
