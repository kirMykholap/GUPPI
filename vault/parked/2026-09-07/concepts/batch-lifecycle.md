---
title: "A collection batch has exactly one finaliser"
type: concept
status: current
authority: batch-finalisation
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "CLAUDE.md"]
tags: [batches, collection]
---

# A collection batch has exactly one finaliser

A batch's **normal** end is written by `run_profile` and by nobody else. Adding a second finaliser
to the runner or to the worker thread produces two owners that disagree about the end time and the
status.

Two other closers exist, and they exist only for a process that can no longer speak for itself:
the startup sweep and the staleness rule, both in `ingest/batches.py`. Neither can disagree with
`run_profile`, because `finish_batch` is scoped to `status='running'` — **the first verdict wins**.

Two supporting mechanics, which are the reason the rule is not merely tidy:

- `open_batch` commits on purpose — the worker thread and the CLI live in other sessions, and an
  uncommitted batch is invisible to them;
- `run_source` commits the journal row as `running` **before** the request. That is what makes
  progress observable at all, and it is also what makes a killed process leave a dangling row,
  which `sweep_interrupted` and `STALE_AFTER` clean up.

For where a run lives and how a second press is refused, see [[collection-runs-in-a-thread]].

**A crashed run closes as `interrupted`, never as `finished`.** A review caught the panel reporting
a completed collection for a run that had exploded — the status a batch ends in is a claim about
what happened, and «finished» would have been a false one.

The three closers are not interchangeable, and the difference has teeth: `finish_batch` inside
`run_profile`'s `finally` fires most often; the startup sweep closes **only** `started_by='web'`
batches, because a CLI batch lives in another process and may still be running — interrupting it
would be a lie; and what protects against a CLI batch left behind by a killed terminal is
[[stale-after-thirty-minutes]], not the sweep. See [[sweep-runs-only-under-docker]].

See [[collection-runs-in-a-thread]] for where the run lives, [[stale-after-thirty-minutes]] for
why the staleness window is the size it is, and [[architectural-boundaries]] for the write
boundary that keeps batch writes in `ingest/batches.py`.



## The panel reads the *latest* batch, which is how a stale one can hide

`load_state` reads the profile's **latest** batch by `started_at`. A stale `running` batch sitting
behind a newer closed one is therefore **invisible to the panel** — discovered when the `stale`
branch was rendered live for the first time and the synthetic row had to be moved to the end of the
timeline before it showed at all.

Rendered correctly once it was visible: a `running` batch with `last_progress_at` 20 minutes old
produced «Прогон не подаёт признаков жизни с 19:55 — похоже, он оборвался. Можно запустить заново.»,
with the buttons **enabled** and no polling. Both are right: nothing is running that we should wait
for. See [[stale-after-thirty-minutes]].

## An unguarded rule, recorded on 2026-08-13

**No test enforces the one-finaliser rule.** The seven AST boundaries hold *where* a batch may be
written ([[architectural-boundaries]]); none of them holds that `run_profile` is the only writer of
a batch's normal end. A second finaliser added to the runner or the thread would pass the suite
and disagree with the first only about the end time and the status — the quietest possible defect.
Until such a test exists, this page is the whole guard.

*(That line read «the **five** AST boundaries» until 2026-08-15. Measured that day: **seven**
boundary test files under `tests/unit/`, which is what [[architectural-boundaries]] has said since
2026-08-14 — this page was carrying the exact five-for-seven drift that
[[a-stated-count-drifts-from-the-list-it-heads]] uses as its opening example, uncorrected inside the
corpus that diagnosed it. Found by the first `/vault-lint`.)*
