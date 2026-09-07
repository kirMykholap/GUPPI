---
title: "A chain proved in halves is not proved, and the halves were assembled by the party they favoured"
type: lesson
status: archived
authority: composed-proof
basis: human
sprint: S2
created: 2026-08-22
sources: ["archive/2026-08-22/2026-08-22-the-pre-task-becomes-an-agent-and-a-prohibition-is-ratified/handoffs/2026-08-22-the-pre-task-becomes-an-agent-and-a-prohibition-is-ratified.md", ".superpowers/sdd/pre-task-ledger.tsv"]
tags: [process, harness, agents]
---

# The incident, 2026-08-22

**The blocking write gate needs one row: `dispatch:pre-task`, written while the session is in plan
mode.** That is the refusal test's middle condition — *the measurement is reliable where the gate
stands* — and it is what made a blocking gate illegal until this date
([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]],
[[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]).

**What the ledger holds is two rows, and neither is that one:**

```
17:10:18  dispatch:vault-librarian  plan  -
18:35:23  dispatch:pre-task         auto  -
```

**Right moment, wrong agent. Right agent, wrong moment.** The session announced the chain proved end
to end and briefed the librarian to write it that way, and the corpus carried that claim until the
ingest of this journal corrected it.

> **owner: Ошибка в том, что на фазу plan mode должен был быть диспатч pre-task, а не библиотекаря. Библиотекарь = это работа с vault. Для подготовки плана и сверки его с vault существует агент pre-task. Мы это обсуждали, но реализация сейчас неверная. Поэтому критерий 14 все ще NOT MET пока мы окончательно не убедимся в том, что это работает правильно и я дам подтверждение**

**He read sprint item 14 as NOT MET and put its closure on his confirmation rather than on a
reading** ([[a-sprint-closes-on-its-goal]]).

# Why the two rows look like a proof, and are not

**Each row is true and each proves something.** The first proves the recorder writes during
planning — a property of the hook. The second proves `dispatch:pre-task` is a row the recorder can
write and that `Read-LedgerState` accepts.

**The conjunction is a third claim and nothing observed it.** *The row that discharges the ritual can
be written at the moment the rule places the ritual* is the sentence the gate depends on, and it is
not entailed by two observations taken at different moments about different agents. The composition
was done by the reader, not by the tree.

**It is a substitution inside a proof, and the substituted term is exactly the one under test.** The
recorder's own selftest asserts that *any other agent type is a dispatch and not the ritual*
([[the-dispatch-record-hook]]) — so the librarian row was already known not to stand in for the
pre-task row, in the same file that was being read as though it did.

# The aggravation: the session predicted this blindness an hour before it happened

**Before calling `ExitPlanMode` it stated that only `dispatch:pre-task` discharges the ritual and
that the gate would therefore report a false positive.** It did. **The same session then counted a
`dispatch:vault-librarian` row toward that same discharge.**

**So the knowledge was present and was not applied to the session's own record.** It is the class the
brief already carried instances of, and this is another: **a measurement about the session's own work,
wrong in the session's favour, caught by another party rather than by reading carefully**
([[a-subagents-most-believable-sentence-is-the-one-to-measure]],
[[a-claim-labelled-measured-came-from-an-instrument-reporting-its-own-exit-code]],
[[an-instrument-that-contains-its-own-answers-can-be-gamed]]).

**The direction is not random.** Both halves were assembled into the conclusion the assembler wanted,
and neither the assembly nor the wanting was visible in what was handed on — the brief carried the
conclusion, not the two rows ([[a-claim-that-runs-ahead-of-its-measurement-is-corrected-in-the-same-session]]).

# What it costs, and what would have caught it

**It cost a written page.** [[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]] carried
*"the chain is proved end to end"* for one day, with the two rows quoted underneath it — the evidence
against the conclusion was on the same page as the conclusion, and nobody reading it noticed.
**That is the argument for quoting the rows rather than the reading**: the owner found this by
looking at what was quoted.

**Nothing mechanical was ever going to catch it.** No check reads a ledger for the conjunction of a
column and an agent type, and inventing one for this case would be a rule about one sentence. What
is available and cheap: **state the row the claim needs, then show the rows that exist, and let the
difference be visible** ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).
