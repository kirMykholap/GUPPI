---
title: "`/pre-task` becomes an agent rather than a skill, and the ritual is enforced rather than advised"
type: decision
status: archived
authority: pre-task-enforcement
binding: deferral
basis: human
sprint: S2
decided: 2026-08-21
created: 2026-08-21
sources: ["archive/2026-08-21/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md", ".claude/agents/pre-task.md", ".claude/hooks/check-the-plan.ps1"]
tags: [agents, harness, process]
---

# The ruling, 2026-08-21, and it is a deferral because none of it is built

> **owner: я считаю, что мы должны соблюдать ритуал. Да, мы платим за это 90 секунд в среднем, но
> зато мы всегда знаем что план сверен с vault.**

**Two things were decided at once**: the ritual becomes its own agent rather than a skill the caller
performs, and the gate that watches for it stops advising and starts refusing
([[advisory-is-the-default-for-a-hook]], [[a-skill-is-a-mask-and-a-subagent-is-a-body]]).

**The design behind it is [[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]]**, which
is the proposal the owner asked for by name and the thing to be discussed before anything is
written. This page is the ruling; that page is what it would take.

# The order is part of the decision, and the last step is the dangerous one

**The write gate becomes blocking last, and only after a real ingest has proved the librarian does
not deadlock behind it.** Making `Test-PreTaskOwedForWrite` block means removing two short-circuits
— `Advised` and `ScopeAt` — and **the librarian writes about fifty pages per ingest**. Hooks apply
inside subagents, so the vault-path exclusion has to hold under a blocking gate or every ingest
deadlocks, and that has already happened once here
([[the-vault-is-excluded-from-the-pre-task-net]], [[the-librarian-lock-hook]],
[[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]).

**It cannot be verified except by running a real ingest.** That is the highest-severity item on the
deferral and the reason the order is not negotiable
([[a-deferred-check-must-be-run-when-its-condition-arrives]]).

# The number the owner ruled on was wrong, and the ruling stands anyway

**«90 секунд» was the wall clock of one scout reading one folder**, not the price of a pre-task
agent. The honest figure is about 90 s for the empty case and **3–5 minutes where there are
findings**, because an agent doing the whole ritual returns to the measured 5m54s minus the
enumeration saving ([[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]],
[[agent-round-trip-cost]]).

**The correction arrived after the ruling and the ruling was not revisited.** That is recorded here
rather than resolved: whether a price four times the quoted one changes his answer is his to say,
and nobody has asked ([[a-vault-page-is-a-question-to-the-owner-not-a-settled-fact]]).

# A conditional deferral that travels with it

**`governs:` learns to take a list only when a second reading agent exists.** It is a condition and
not a schedule: the injector reads the field with `head -1`, so one address is all it can deliver
today, and nothing is blocked without the change because the mechanism would have no customer
([[governs-is-a-property-of-wiki-rules-alone]], [[a-refusal-is-conditional-or-absolute-and-nothing-else]]).

**What waiting costs:** the shared reading discipline stays copied into each reader rather than
rendered into them, which is the divergence failure this project builds against
([[one-librarian-behind-every-caller]], [[the-harness-is-compiled-not-maintained]]).

# The enforcement half was re-argued when the rule under it was struck, and its ground moved twice — 2026-08-22

**The clause *"the gate that watches for it stops advising and starts refusing"* cites
[[advisory-is-the-default-for-a-hook]], which the owner disowned on 2026-08-21 and which is now
retired to `archive/`.** The sentence above is kept exactly as written: it records the ground this
ruling was actually taken on, and a page that carried a struck rule is testimony about the day it
was written ([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]],
[[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**This page was not on the list of dependents re-pointed earlier today, and being late is the whole
of what changed here** — the ruling itself is untouched and no disposition is inherited from the
struck page ([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]]).

## Under the struck rule it turned on *irreversible*; under the ratified test it turns on the middle condition

The gate this clause is about is the write net — `Test-PreTaskOwedForWrite`, inside the
`PreToolUse` guard on `Edit|Write` ([[the-guard-branch-lives-inside-a-hook-that-already-runs]],
[[the-pre-task-state-machine-has-a-flag-for-the-plan-and-a-flag-for-the-write]]).

| the condition | this gate, read on 2026-08-22 |
|---|---|
| the condition is measured rather than judged | **satisfied.** *Is a pre-task on the record for this session* is a ledger read and not an opinion ([[the-pre-task-ledger]]) |
| the measurement is reliable where the gate stands | **not satisfied today.** A ledger row cannot be written in plan mode, which is the exact moment the rule places the ritual, so a ritual performed exactly right leaves the ledger silent and a blocking gate would refuse the session that performed it ([[a-pre-task-runs-between-the-plan-and-its-approval]], [[plan-mode-blocks-edits-and-not-a-subagent-dispatch]]) |
| the refusal says how to clear it | **it could.** The advisory the net already returns carries the rule's own text and names the ritual that clears it |

**Where it cannot measure, it allows and says so aloud** — which is what the net does today. **The
disposition is the new test's own consequence rather than a default it falls back to**, and it is
the same condition `check-the-plan.ps1` fails on, for the same reason
([[the-plan-check-hook]]).

**Same answer as before, on a checkable ground.** *Skipping the ritual is irreversible* was a
judgement about the act; *the ledger cannot be written at the moment the rule names* is a property
of where the gate stands, and anyone can check it.

## What moved on this date, and it is the middle condition that moved

**`.claude/hooks/record-the-dispatch.ps1` was built and registered on `PostToolUse` for
`Agent|Task`.** It writes `dispatch:<subagent_type>` per **returned** dispatch, and
`Read-LedgerState` treats `dispatch:pre-task` as discharging the ritual
([[the-dispatch-record-hook]]).

**So once `/pre-task` is an agent, the row exists and is written by a hook — and a hook can write
during planning**, which the rows already carrying `plan` in their permission-mode column prove
([[one-ledger-is-the-record-the-heartbeat-and-the-permission-mode]]). **That is what makes the
blocking gate legal**: the measurement becomes reliable where the gate stands.

**It is legal-once-proved rather than scheduled.** The recorder has **not** run for real: it was
registered after this date's dispatches had already begun, so its live firing is **owed against a
session restart** ([[claude-code-config-loading]]). Until that is observed, the middle condition is
satisfied on paper and not on the tree.

## The ordering argument on this page is untouched and is a second gate, not the same one

**The deadlock risk is independent of the refusal test and survives it whole.** Removing the
`Advised` and `ScopeAt` short-circuits while the librarian writes about fifty pages per ingest is a
risk about what a blocking gate does to the one writer, not about whether it may refuse at all
([[the-vault-is-excluded-from-the-pre-task-net]],
[[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]). **Both gates have to clear before the
last step is taken**, and the order this page fixes is unchanged
([[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]]).

**And the conditional deferral at the foot of this page is discharged.** `governs:` takes a list from
2026-08-21, and the first page to write one landed today
([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]],
[[a-block-attributed-to-the-owner-is-written-in-his-own-russian]]) — **on a rule other than the
shared reading discipline**, so what waiting cost is unchanged and the second reading agent still
does not exist.

# The citation is repointed to what this ruling produced, and three of its open items moved — 2026-08-22

**`sources:` cited `.claude/skills/pre-task/SKILL.md` and now cites `.claude/agents/pre-task.md`.**
The skill was deleted on this date and `.claude/agents/pre-task.md` is the file this ruling asked
for, so the citation moves from the thing replaced to the thing built; rule 5 of the gate requires
every repository path in `sources:` to resolve, and a citation to a file that is not there reads as
provenance and is not ([[vault-scripts]]). **The address moves and the history stays readable**: this
page was compiled on 2026-08-21, while the skill was still what `/pre-task` meant, and nothing above
is rewritten.

**The conditional deferral at the foot of this page is discharged in the half that was still owed.**
The section above ends *"the second reading agent still does not exist"*, which was true when it was
written this morning. **It exists now.** `.claude/agents/pre-task.md` is the second reader, and the
shared discipline is **rendered into both** rather than copied — a `governs:` list of two, which is
the customer the `governs:`-takes-a-list change was waiting for
([[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]],
[[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]]). **What waiting cost is
therefore paid rather than still accruing.**

**The recorder has now fired for real, and the specific row that discharges the ritual has not.**
`.superpowers/sdd/pre-task-ledger.tsv` carries three `dispatch:vault-librarian` rows written by
`.claude/hooks/record-the-dispatch.ps1` in the session of 2026-08-22, so *registered but never
observed* no longer describes it ([[the-dispatch-record-hook]]). **No `dispatch:pre-task` row exists
yet**, and that is the row `Read-LedgerState` treats as discharging the ritual — so the middle
condition of the table above is satisfied for the hook and still unobserved for the path that makes
the blocking gate legal.

**The ordering argument is untouched.** The deadlock risk of removing the two short-circuits while
the librarian writes about fifty pages per ingest is a second gate and nothing here clears it.

# The price the owner ruled on has a measurement now, and it is further from his number than the correction was — 2026-08-22

**Measured: 233,165 tokens, 49 tool uses, 10m40s, 65 pages opened in full, over a 43-page
shortlist**, read off the harness's usage report rather than reported by the subagent
([[a-subagent-cannot-report-its-own-cost]],
[[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]).

**The section above corrected «90 секунд» to *about 90 s for the empty case and 3–5 minutes where
there are findings*, and said the correction arrived after the ruling and the ruling was not
revisited.** The measured reading is roughly three times that corrected estimate and about seven
times the number he had in front of him. **The same disposition applies and is not being changed
here**: whether a price that far from the quoted one changes his answer is his to say, and nobody has
asked ([[a-vault-page-is-a-question-to-the-owner-not-a-settled-fact]]).

# The chain is proved end to end, and the first of the two gates is fully discharged — 2026-08-22

**The section above says *"No `dispatch:pre-task` row exists yet, and that is the row
`Read-LedgerState` treats as discharging the ritual"*. It exists.** Off
`.superpowers/sdd/pre-task-ledger.tsv`, in the session that began at 16:40:11 — five dispatch rows
were written in it and these are the two that carry the argument:

```
17:10:18  dispatch:vault-librarian  plan  -
18:35:23  dispatch:pre-task         auto  -
```

**Both observations this ruling had outstanding are now taken**, and they are different claims:

- **the recorder fires in a live session** — the first session to start with it registered, and it
  wrote a row for every dispatch without being asked ([[the-dispatch-record-hook]]);
- **the recorder writes during planning** — `plan` in the first row's mode column, on a row this
  hook wrote. That is the refusal test's **middle condition**, which is the one a blocking write gate
  failed, and it is now a property observed of this hook rather than inferred from rows other hooks
  wrote ([[plan-mode-blocks-edits-and-not-a-subagent-dispatch]],
  [[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]]).

**And `dispatch:pre-task` is on the record**, so the ritual is discharged by the path the design
named and not by a branch that had never run. **The table of the three conditions above therefore
reads *satisfied* on all three for the write gate**, and it reads so on the tree.

## The second gate is untouched and it is the higher-severity one

**Step 4 is still not built.** The deadlock risk stands exactly as this page states it: removing the
`Advised` and `ScopeAt` short-circuits while the librarian writes about fifty pages per ingest, and
**it cannot be verified except by running a real ingest**
([[the-vault-is-excluded-from-the-pre-task-net]],
[[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]],
[[a-deferred-check-must-be-run-when-its-condition-arrives]]).

**Nothing here shortens the order.** The refusal test clearing is one of the two conditions, and the
ordering argument on this page was written to survive the other one clearing
([[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]]).

## The gate the chain replaces fired a false positive on the way, and it was predicted first

**`check-the-plan.ps1` asked for a `/pre-task` on this session's `ExitPlanMode` after the ritual had
run in full, both phases.** The ritual was performed by a `vault-librarian` dispatch, because the
`pre-task` agent did not exist yet; only `dispatch:pre-task` discharges the ledger, so the gate
advised against a session that had done the work ([[the-plan-check-hook]]).

**It is the predicted behaviour and not a defect** — *any other agent type is a dispatch and not the
ritual* is a stated property of the recorder with a selftest case behind it
([[the-dispatch-record-hook]]). **It was named before it happened and then observed**, which is the
only version of this evidence worth anything ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

**It is also the argument against taking step 4 on a single green reading.** The same false positive
under a **blocking** gate would have refused a session that obeyed the rule exactly, and the
advisory disposition is what made it cost a line instead
([[a-refusal-is-conditional-or-absolute-and-nothing-else]],
[[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]]).

# The section above is wrong, and the owner caught it — 2026-08-22, at the ingest of that session's journal

**The heading *"The chain is proved end to end"* is false and is left standing**, because it is what
this page asserted for a day and because the two rows it quotes are the evidence against it
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**Read the rows it quotes.** `dispatch:vault-librarian` at `plan`; `dispatch:pre-task` at `auto`.
**The row the blocking gate needs is `dispatch:pre-task` in plan mode, and it is not there.** Right
moment with the wrong agent, right agent at the wrong moment — and the recorder's own selftest
already asserts that any other agent type is a dispatch and not the ritual
([[the-dispatch-record-hook]]). The conjunction was composed by the reader
([[a-chain-proved-in-halves-is-not-proved]]).

> **owner: Ошибка в том, что на фазу plan mode должен был быть диспатч pre-task, а не библиотекаря. Библиотекарь = это работа с vault. Для подготовки плана и сверки его с vault существует агент pre-task. Мы это обсуждали, но реализация сейчас неверная. Поэтому критерий 14 все ще NOT MET пока мы окончательно не убедимся в том, что это работает правильно и я дам подтверждение**

**What the table of conditions actually reads on this date.** The middle condition — *the measurement
is reliable where the gate stands* — is **satisfied for the recorder** and **unobserved for the path
that makes the blocking gate legal**. That is exactly what the earlier section on this page said
before the one above it overwrote the reading, and it is the reading that stands.

**Sprint item 14 is NOT MET, and it does not close on a reading.** He ruled that it closes when he is
satisfied the mechanism works and gives his confirmation — a criterion whose decider is his word
rather than a command, which is a departure from how every other criterion here is written and is
his to make ([[a-sprint-closes-on-its-goal]]).

**The clause that was already right is untouched.** The second gate — the deadlock risk of removing
the `Advised` and `ScopeAt` short-circuits while the librarian writes about fifty pages per ingest —
is unchanged, unverified, and still the higher-severity one.
