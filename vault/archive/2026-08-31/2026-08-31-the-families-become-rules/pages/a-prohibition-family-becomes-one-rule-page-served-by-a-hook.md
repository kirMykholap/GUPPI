---
title: "A prohibition family becomes one rule page served by a hook, and the decisions behind it then leave"
type: decision
status: archived
authority: prohibition-family-rule
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: proposal
target: the-prohibition-families-become-rule-pages-served-by-a-hook
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "job_hunt_ai_vault/authority.md", ".claude/hooks/serve-the-rule.ps1", "docs/vault-cleanup-families.md"]
tags: [vault, harness, process]
---

# Context

**`wiki/decisions/` holds 321 live pages and 283 carry `binding: prohibition`.** They are the largest
fixed cost any dispatch pays, and most of a session never sees them: a prohibition reaches a reader
only if that reader runs `/pre-task` and reads the folder.

**The owner opened the session saying most of the folder is not needed and that reading the corpus
costs a session its budget.** He also refused a criterion that would have him read 282 pages: that was
*«слишком дорого»*, and he asked for a grouping.

**The grouping already existed.** `job_hunt_ai_vault/authority.md` puts the 282 prohibitions into 53
of its 63 families with no slug left over
([[the-authority-register-groups-the-corpus-and-the-family-is-the-unit-of-a-cleanup]]).

**Files this touches:** `job_hunt_ai_vault/authority.md`, `job_hunt_ai_vault/wiki/rules/`,
`.claude/hooks/serve-the-rule.ps1`, `scripts/vault-authority.sh`,
`job_hunt_ai_vault/wiki/decisions/_schema.yaml`, `docs/vault-cleanup-families.md`.

# The question

**Do the live prohibitions stay where they are, or does each family become one rule page that a hook
delivers?**

# How it works after

**Each prohibition family becomes one page in `wiki/rules/`, carrying the family's `authority:`
slug**, with one clause per member and a link from each clause to the decision it came from. **A hook
serves that page when a file the slug answers for is touched.** The decisions then leave for
`archive/`, where their ground, their rejected alternatives and their measurements stay reachable.

**The future flow he stated, and it is the part that makes this mechanical:** a decision is written
with `binding: prohibition` and `target_kind: rule`; the librarian assigns it an `authority:`;
find-or-extend — if a rule already carries that slug it is extended, otherwise a rule is created and
inherits the slug from the decision.

**A sixth decision section carries the clause in the words it will be read in.**
`sections_when_target_kind_rule:` in `wiki/decisions/_schema.yaml` obliges `# The rule text` of any
decision whose target is a rule, scoped by `lifecycle_from:`. **Without it "mechanical" is untrue** —
assembling a family rule would need a human to write each clause from the body of a decision, which is
the step this store cannot automate and would therefore skip.

**The review table is for the owner and the folder is for the hook.** `docs/vault-cleanup-families.md`
carries the families for him to mark; the hook reads `wiki/rules/` directly and no generated table
stands between them.

# Three things that are true of this ruling and are not in the sentence above

**Its precondition is not met.** The delivery this trades the prohibitions' reachability for does not
exist: `.claude/hooks/serve-the-rule.ps1` has no `authority:` matching branch, and a page under
`render: authority` cannot be served by any matcher it has
([[the-rule-server-hook]],
[[the-hooks-authority-branch-is-not-written-and-the-read-matcher-is-downstream]]). **Until that branch
exists, archiving a prohibition leaves it with no reader at all**, which is exactly the condition
[[the-cleanup-suspends-the-rules-that-would-refuse-it]] said the hook was built to remove.

**One live rule was checked and does **not** need lifting.**
[[a-rule-ships-one-piece-of-text-or-it-is-more-than-one-rule]] refuses a page carrying *two* text
slices; a family rule under `render: authority` carries none. It is named here so the next reader does
not read its absence from the repeal as an omission.

**The 53 `authority.md` rows land in the same pass as the 53 pages**, or rule 13 reddens on 53
ungrouped slugs and locks out the only party permitted to write them
([[the-authority-rows-are-written-in-the-same-pass-as-the-rule-pages]]).

# Recommendation

**Take the mechanism, with the four corrections the session added.** The alternative he had opened —
*any live page citing a decision permits archiving it* — was already refused by the corpus with
measurements, and he withdrew it himself inside the same conversation
([[a-citation-is-not-a-test-in-a-corpus-this-densely-linked]]).

**Rejected: converting the 282 pages one at a time**, and rejected: leaving them where they are, which
is the state he opened the session objecting to.

# Ratification

**owner, 2026-08-30:** «все descisions, которые у нас есть с prohibition мы фасуем на семейства и
записываем их как rule в нашем wiki/rules с конкретным authority. Далее мы строим хук, который ловит
любой edit/write md файлов, смотрит файл который пытаются прочитать или запсиать в него и выдает
конкретный rule c authority, которая есть у этого файла… Да, мы вводим authority для rules, который он
получает от descision. Сейчас мы все делаем быстро и не по правлоам, но в будущем будет так : мы
создали descision с prohibition и мишенью на rule. Библиотекарь должен определить ему authority и
перейти к правилу: если такой authority у rule уже есть - расширить. Если нет - создать и передать
authority от descision.»

**The session added four corrections and he took all four**: two matchers rather than one; the eleven
`CLAUDE.md` rules stay rendered because they must be known before any write happens; the sixth
decision section; and the table is for the owner while the hook reads the folder.

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
