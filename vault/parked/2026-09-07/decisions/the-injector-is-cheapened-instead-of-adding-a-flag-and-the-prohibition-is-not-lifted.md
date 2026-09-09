---
title: "The injector is cheapened instead of adding a flag, and the prohibition on hiding a verdict is not lifted"
type: decision
status: current
authority: gate-flag-deferral
binding: deferral
basis: human
sprint: S3
decided: 2026-08-24
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/vault-inject.sh", "scripts/vault-check.sh"]
tags: [harness, vault, testing]
---

# The ruling, 2026-08-24

> **owner:** «пробуем удешевить injector вместо флага. Если не получится - вернемся к обсуждению
> снятия запрета правилом.»

**The flag was designed and not built.** It would have let the gate skip rules 12 and 13 — the
injector check and the authority check — which are the two delegated parts of the run.

# What it meets, and why the meeting is exact rather than arguable

**[[the-tag-density-advisories-move-behind-lint]] carries `binding: prohibition`** and holds two
properties as selftest cases: *the exit code is identical with and without the flag*, and *only
lines that cannot fail may ever go behind it, so nobody can later move a verdict behind the same
argument*.

**Rules 12 and 13 print `note`, which sets `fail=1`.** A flag that skips them moves the exit code by
construction ([[severity-in-the-gate-is-decidable-which-is-what-lets-a-flag-be-safe]]). There is no
reading of the flag under which the prohibition does not reach it.

**Rejected: lifting the prohibition on the same day the flag was wanted.** Lifting a rule is a
conversation with the owner, and a session that wants the exemption is the worst-placed party to
argue it.

# What was done instead, and what it bought

**The injector was made cheaper.** Paired readings taken back to back in a quiet window, three each
way: the injector went from 6.19/6.26/6.34 s to 3.45–3.71 s, and the gate from 17.31/17.04/17.33 s
to 15.42/15.02/15.39 s — **17.2 → 15.3 s, about eleven per cent**.

**The flag is still worth 5.1 s of that 15.3 s.** So the conversation the owner set the condition
for is now due, and it belongs to the next session.

# What it obliges

**The next session meets the prohibition with the same question and the measurement in hand.** The
condition he named — *if it does not work out, we return to discussing lifting the ban by a rule* —
is met in the sense that the cheapening worked and the flag is still the larger prize.

# Carried again, 2026-08-25 — the owner could not decide the fork

> **owner:** «1) не знаю. Я не могу принять решение, давай зафиксируем и перенесем.»

**The prohibition is still not lifted and the flag is still not built.** Both forms of the fork are now
written down with their cost, on a page of their own
([[the-gate-flag-fork-is-recorded-and-nothing-is-built]]).

**What the cheapening bought stands**: the gate reads 15.3 s, and the two delegated rules are 5.1 s of
it. **What that is worth in the suite is the number that had not been stated** — the suite runs the
gate about 171 times against a 34m8s total.
