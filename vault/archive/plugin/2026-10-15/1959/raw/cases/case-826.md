## Case 826 — The tags retro and box stand in tags.md and on their lessons

> **context:**
> A tag enters `vault/wiki/tags.md` only from a ratified Case, and the ledger hook refuses a lesson line whose tag that file does not hold and no ratified Case of the session declares (case 703.2). At the Retro of session 1739 two lessons wanted the tags `retro`, `box` and `pre-spec`. No Case could be ratified there, so they were written with listed tags: `lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian` carries `workflow` and `tests`, and `lesson-box-cannot-act-on-the-prespec-findings-of-a-conserved-spec` carries `prespec` and `workflow`. The handoff of session 1739 left the new tags to a later session. `vault/wiki/tags.md`, read whole, has no row `retro` or `box`, and its row `prespec` covers what `pre-spec` would mean, so this Case adds no second spelling. This Case declares the two tags and adds each to its lesson; an earlier Case gave a lesson the tags the ledger hook had refused in the same way (`vault/wiki/log.md`, the line of 2026-10-08 on case 737). The rules `rule-retro` and `rule-spec-box` and their Estimates keep their tags; each takes the new tag when a later Case changes it. No Estimate is created: `estimate-generate-writes` already checks both writes, since its Criterion says that a tag of `new_tags` lands in `tags.md` and that an `update` applies `set` to the frontmatter; its Criterion stands, since this Case changes neither behaviour. The lessons list no Estimates. The person asked why a new tag needs a Case at all; the guard stays in this Case, and its change is left to a separate Frontier item for the main agent to add, since it touches the ledger hook, the check of a Case file and the one rule of `ratification.md`.

> **problem:**
> The tags `retro` and `box` that two lessons of session 1739 wanted are not registered, so the lessons stand without them.

> **recommend:**
> - **Which new tags to register, with what meaning and Russian aliases**
>   - Recommended: (a) both `retro` and `box`, with the proposed meanings and aliases; no `pre-spec`, since `prespec` covers it.
>   - Answer: agreed with the new tags, (a).
> - **Which pages take the new tags in this Case**
>   - Recommended: (a) the two lessons only.
>   - Answer: agreed, (a).
> - **Which Estimate checks the change**
>   - Recommended: (a) no new Estimate; `estimate-generate-writes` checks it.
>   - Answer: agreed, (a).
> - **Should a new tag still need a ratified Case**
>   - Recommended: (b) keep this Case to the two tags, and add a separate Frontier item that changes the guard.
>   - Answer: agreed, (b).

> **given:**
> `vault/wiki/tags.md`: the registry of tags, which gains the two rows.
> **＋** `lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian`: the lesson that takes `retro`.
> **＋** `lesson-box-cannot-act-on-the-prespec-findings-of-a-conserved-spec`: the lesson that takes `box`.

> **when:**
> The librarian's run of `guppi generate` applies this Case to `vault/wiki/tags.md` and the two lessons.

> **then:**
> `vault/wiki/tags.md` holds a row `retro` and a row `box`, each with its meaning and its Russian aliases.
> **＋** `lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian` carries the tags `workflow`, `tests` and `retro`.
> **＋** `lesson-box-cannot-act-on-the-prespec-findings-of-a-conserved-spec` carries the tags `prespec`, `workflow` and `box`.
> **－** `vault/wiki/tags.md` gains no row `pre-spec`.

> **tasks:**
> - [ ] tag `retro`
>   - meaning: `the Retro phase: the review of the session's work against its ledger, the readings of Estimates, the lessons and the handoff`
>   - aliases: `ретро, ретроспектива`
> - [ ] tag `box`
>   - meaning: `/box: a later session running a conserved Spec on its own branch`
>   - aliases: `бокс, законсервированный спек`
> - [ ] update `lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian`
>   - set: `{tags: [workflow, tests, retro]}`
>   - change: `tagged retro, the tag the ledger hook refused at the Retro of session 1739`
> - [ ] update `lesson-box-cannot-act-on-the-prespec-findings-of-a-conserved-spec`
>   - set: `{tags: [prespec, workflow, box]}`
>   - change: `tagged box, the tag the ledger hook refused at the Retro of session 1739`

> **ratification:**
> ```
> - decision[case 826][update][lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian]{ref:lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian}
> - decision[case 826][update][lesson-box-cannot-act-on-the-prespec-findings-of-a-conserved-spec]{ref:lesson-box-cannot-act-on-the-prespec-findings-of-a-conserved-spec}
> ```
