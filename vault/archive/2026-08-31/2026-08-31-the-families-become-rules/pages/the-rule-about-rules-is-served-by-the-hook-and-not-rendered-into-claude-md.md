---
title: "The rule about rules is served by the hook on a touch of `wiki/rules/`, and is rendered into no file"
type: decision
status: archived
authority: rule-about-rules-delivery
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: rule
target: a-rule-page-carries-a-family-slug-and-the-decision-that-caused-it
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "job_hunt_ai_vault/CLAUDE.md", ".claude/hooks/serve-the-rule.ps1"]
tags: [vault, harness, record-schema]
---

# Context

**The family mechanism needs a rule stating how a rule page is written** — what slug it takes, where
the slug comes from, what a clause is, and what it links back to. The session proposed rendering that
into the vault's own `CLAUDE.md`, on the ground that whoever writes a rule must know the shape before
writing it, and a delivery triggered by touching a file arrives after the decision to write is made.

**The counter-measurement the session had taken that same day and did not weigh**:
`job_hunt_ai_vault/CLAUDE.md` is 25,020 bytes and is the largest fixed context cost this store has —
paid by every dispatched agent, on every dispatch.

**Files this touches:** `job_hunt_ai_vault/CLAUDE.md`, `job_hunt_ai_vault/wiki/rules/`,
`.claude/hooks/serve-the-rule.ps1`, `.claude/skills/vault-ask/SKILL.md`.

# The question

**Is the rule about rules rendered into the vault's `CLAUDE.md`, or served by the same hook when
`wiki/rules/` is read or written?**

# How it works after

**Served by the hook, under `render: authority`, written into no file.** Anyone reading or writing
inside `wiki/rules/` is handed it at that moment.

**His ground is a claim about how work actually happens**: one almost always searches first and acts
afterwards, so the search is where the rule can catch you. `/pre-task` dispatches `vault-ask`, which
goes and reads `wiki/rules/` and would trip the hook on the read — **so `vault-ask` must have this
hook**, which he named explicitly as important.

**The librarian is excluded, and by path.** His premise was that the librarian simply does not have
the hook; that half is wrong. Hooks in `settings.json` **do** reach subagents, proved in this
repository on 2026-08-20 ([[hooks-in-the-settings-file-apply-inside-subagents]]), and no documented
way exists to exclude one — an agent's frontmatter may add hooks and may not remove them. **So the
exclusion is by path: the hook is silent for writes inside `wiki/`**, which reaches the same outcome
and needs no separate declaration for `vault-ask` ([[the-rule-server-hook]]).

**The ordering this obliges, and it is a gate rather than advice.**
[[a-rule-moving-to-conditional-delivery-needs-its-page-first]], widened by
[[the-conditional-delivery-gate-covers-any-departure-from-unconditional-delivery]] to any rule that
stops arriving unconditionally, demands a dated decision with a rejected alternative **before** the
move. This page is that decision, and it is written **before** the rule pages exist rather than after
— which is the order the 53 family rules must also follow.

**The `Read` matcher is not wired and the `authority:` branch is not written**, so nothing is served
by this route today ([[the-hooks-authority-branch-is-not-written-and-the-read-matcher-is-downstream]]).

# The rule text

**A rule page in `wiki/rules/` takes its `authority:` slug from the decision that caused it, and one
slug is carried by one rule page.** When a decision with `binding: prohibition` and
`target_kind: rule` is ratified, the librarian assigns it an `authority:` and then looks the slug up:
**if a rule already carries it, that rule is extended with the decision's `# The rule text` clause; if
none does, a rule page is created and inherits the slug.** Each clause names the decision it came
from. A rule delivered by lookup carries `authority:` and no `governs:`; a rule delivered by injection
carries `governs:` and no slug.

# Recommendation

**The session withdrew its objection.** His premise about the librarian was half wrong and the outcome
survives it, which is the test of a ruling rather than of an argument. Against it stands the 25 KB
measurement the session had in hand and did not use: rendering this into the vault's `CLAUDE.md` would
have charged every dispatch for a rule that concerns one folder.

**Rejected: rendering it into `job_hunt_ai_vault/CLAUDE.md`.**

# Ratification

**owner, 2026-08-30:** «А почему мы не можем это правило сделать тоже внутри самого rules/. Как только
кто-либо read/write rules/ - хук подкладывает "правило о правилах". ТВое возражение что мы должны
знать заранее могу опровергнуть тем, что мы практичсеки всегда сначала ищем что-то, а потом делаем.
Тот же pre-task должен диспатчить vault-ask, который пойдет читать rules и словит хук при read.(нужно
будет ему этот хук добавить кстати, это важно). А вот у библиотекаря этого хука какраз нет, чтобы он
не визжал ему каждый раз, когда библиотекарь пишет.»

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
