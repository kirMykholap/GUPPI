---
title: "`raw/` is emptied by a script rather than by hand, and the move lives inside the ingest"
type: decision
status: current
authority: raw-emptying-mechanism
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", ".claude/skills/ingest/SKILL.md"]
tags: [vault, process, harness]
---

# The ruling, 2026-08-19

> **owner:** «raw должен обработаться и после очиститься… Я знаю, что у нас есть правило "не удалять
> ничего из raw и archive" - поэтому для такой процедуры предлагаю скрипт.»
>
> «агент все обработал, записал, разнес по категориям и где-то в конце хуком запускается скрипт по
> очистке raw»
>
> «таблица соответствий - мне нравится… нужно подумать как автоматизировать скриптом а не агентом.»

**The mechanical half belongs in a script the ingest calls, not in an agent's hands.** That half is
exactly three operations: **move the file**, **emit the old-path-to-new-path mapping table**, and
**rewrite `sources:` from it**.

**Rejected: the agent doing the mechanical half.** It is the shape a `sed` does correctly and an
agent does approximately, over 150 pages, and the failure would be silent.

**The agent's part is the one thing a script cannot do**: deciding that the source is compiled —
already a command, `vault-coverage.sh` printing `INGEST COMPLETE`
([[handoff-retires-only-when-every-unit-has-a-verdict]]) — and reading the prose diff.

## The move lives inside the ingest, and that is decided

**The dispatch that wrote a citation is the one that fixes it.** A hook firing afterwards would have
to rediscover what the ingest already knew, which is the cheaper-shape argument
[[moving-raw-into-a-dated-archive]] already made from the other side.

**Still open and not settled here:** whether the *trigger* is a hook, whether the *check* is a hook,
or both. The two can be split — the ingest moving, a hook afterwards asserting that nothing compiled
is still sitting in `raw/`. That is the owner's and is written down as open rather than assumed.

## The prose half cannot be automated, and the eye pass is accepted for now

> **owner:** «хочется полностью автоматизировать этот процесс».

**It is not satisfiable, and the reason is on the record.** A path in a body is one string with two
jobs — an address that must move and a quotation that must not — and nothing in the text separates
them ([[sed-cannot-tell-an-address-from-a-quotation]]). The owner accepted the eye pass **for now**,
which makes this a standing question rather than a closed one.

**A detector for prose paths is buildable and bounded**, and it is designed rather than assumed:
[[a-path-detector-for-prose-references]]. It can only ever be an advisory.

## What it obliges

- **`/ingest` gains a step**, which is a skill file the librarian does not write.
- **The script is the design in [[emptying-raw-by-a-script-that-moves-and-rewrites-its-citations]]**,
  and none of it exists yet.
- **`raw/` gains its internal structure first**
  ([[raw-gains-its-internal-structure-before-the-move]]), or the rewrite runs twice.

## The step is wired, and it is forward-only — 2026-08-21

**`/ingest` calls `bash scripts/vault-archive.sh` as its step 12**, which is what *the move lives
inside the ingest* above had asserted for two days about a script nothing called
([[vault-archive-sh]]).

**It is last, and the ordering is load-bearing**: step 10 runs `vault-coverage.sh` against the
source path, and this step moves that path. Between the move and the `^sources:` rewrite the tree is
red, which is why the script does both in one run and then runs the gate itself.

> **owner: сначала только вперёд.**

**Only the source the ingest just compiled moves.** The journals that accumulated before the step
existed stay where they are: sweeping them is **480 `sources:` lines in one commit** across 20
journals, and it is its own piece of work rather than a fold-in
([[moving-raw-into-a-dated-archive]], [[order-a-split-change-against-its-failure-not-for-convenience]]).

**The open question above is answered in one half.** *Whether the trigger is a hook* is settled — it
is the ingest, not a hook. *Whether the check is a hook* is still open, and the hook that would ask
it already exists in another job: `.claude/hooks/session-brief.ps1` reads sidecar absence in
`raw/handoffs/` and, now that compiled journals leave, a non-empty `raw/handoffs/` means work that
was never compiled ([[the-sidecar-is-the-single-definition-of-compiled]], [[session-hooks]]).

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*

# The forward-only clause is overturned by the owner — 2026-08-26

> **owner:** «Тогда передай библиотекарю, что raw нужно почистить сегодня.»

**The paragraph above — *only the source the ingest just compiled moves*, on **сначала только
вперёд** — is struck.** `raw/handoffs/` is swept whole, backlog included, and the sweep ran at this
ingest ([[raw-handoffs-is-swept-whole-today-and-the-forward-only-clause-is-overturned]]).

**The clause is left standing as written rather than edited**, because it is the record of what was
decided on 2026-08-21 and of the ground it was decided on. What changes is that it is no longer the
live instruction.

**Its own figure understated the job.** It quotes 480 `sources:` lines across 20 journals; measured
2026-08-26, **464 of the 682 live pages name a `raw/` file on their `sources:` line — 68% of the
corpus.**

**Everything else on this page is untouched**: the mechanical half is still a script's, the agent's
part is still deciding that a source is compiled, the prose half still cannot be automated, and the
rewrite is still `^sources:` only under `wiki/` and `archive/`
([[sed-cannot-tell-an-address-from-a-quotation]]).

**And the nearest mechanical help for the prose half is now refused rather than pending**
([[the-prose-path-detector-is-refused-on-its-own-measurement]]).

*(Compiled from `raw/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md`.)*
