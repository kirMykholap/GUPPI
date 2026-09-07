---
title: "The hook matches the exact `authority:` slug and resolves nothing through the register"
type: decision
status: current
authority: lookup-rule-delivery
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-31
created: 2026-08-31
target_kind: action
target: serve-the-rule-ps1-matches-the-authority-slug-exactly-and-carries-no-paths
sources: ["archive/2026-08-31/2026-08-31-the-families-become-rules/handoffs/2026-08-31-the-families-become-rules.md", ".claude/hooks/serve-the-rule.ps1", ".claude/settings.json", "job_hunt_ai_vault/authority.md"]
tags: [harness, vault, agents]
---

# Context

**A family rule carries one `authority:` slug and the family it was compiled from holds up to fifteen.**
The hook's match is slug against slug, so eleven of twelve members of a family would serve nothing —
found by working an example through the mechanism rather than by any page saying so.

**The session's own recommendation was to close that gap by resolution**: teach
`.claude/hooks/serve-the-rule.ps1` to look a member slug up in `job_hunt_ai_vault/authority.md` and
serve the rule of whichever family group holds it. That would have made the family register a runtime
dependency.

**The second half of the question is what a `render: authority` rule does about a file with no
frontmatter.** The key is the touched file's own slug, and a slug exists only under `wiki/`, while most
of the prohibitions the cleanup surveyed are about `.claude/`, `scripts/` and `src/`.

**Files and pages this touches:** `.claude/hooks/serve-the-rule.ps1`, `.claude/settings.json`,
[[a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug]],
[[the-rule-server-hook]], [[a-rule-page-carries-a-family-slug-and-the-decision-that-caused-it]],
[[the-hooks-authority-branch-is-not-written-and-the-read-matcher-is-downstream]].

# The question

**Does the hook resolve a member slug through its family group, or does it match the slug it is given
and nothing else?**

# How it works after

**It matches the slug it is given, exactly, and resolves nothing.** A `render: authority` rule is found
by the touched file's own `authority:` slug, by string equality, and `job_hunt_ai_vault/authority.md`
is not read at runtime at all.

**That mode serves pages inside the vault alone.** Everything outside the vault carries no
`authority:`, and it is delivered by rendering into a named file — `governs:` with
`render: region` or `render: whole`. The two deliveries do not overlap and neither covers for the
other.

**`paths:` left the hook entirely.** The field was going to carry the second matcher; with the
resolution refused there is nothing for it to key, so it gains no second reader and needs no second
checker. Measured on the file the day it landed: `paths` appears nowhere in
`.claude/hooks/serve-the-rule.ps1`.

**The gap the resolution was going to close is closed by convergence instead**, which is work on the
corpus rather than logic in a hook — one slug carried along a chain of types, moved by hand
([[the-slug-converges-by-hand-along-the-chain-of-types]]).

# Recommendation

**The session recommended resolution and the owner refused it.** What is recorded here is his ruling
and the session's own proposal as the rejected alternative, because the proposal is the reading a
later session will arrive at again from the same starting point.

**Rejected: resolving a member slug through its family group in `authority.md`.** The family register
is an instrument of the cleanup; a runtime reading of it would outlive the cleanup as a dependency
nobody asked for, and the cheap register would become a thing that must not break.

# Ratification

**owner, 2026-08-31:** «Все, что внутри vault - по правилу A. Все, что вне - не имеет authority. Там
только рендер в конкретный файл.»

**And, put as his own position and then ratified:** «Я считаю, что хук не должен искать ничего кроме
конкретного Authority. А уже наша задача будет сделать так, чтобы authority у файлов были одни у
разных типов страниц.»

# What this obliges

- **A rule page under `render: authority` is reached only by a page that already carries its slug.**
  Writing the rule is half the act; the other half is a live `concepts/` or `entities/` page carrying
  the same slug, and until that exists the rule is served to nobody.
- **No instrument may start reading `authority.md` at runtime.** It is read by
  `bash scripts/vault-authority.sh` and by whoever is doing a cleanup, and by nothing that runs on a
  tool call.
- **A prohibition about a file outside the vault is not a candidate for this delivery.** It needs
  `governs:` and a written region, which is prose somebody writes rather than a list of titles a
  script assembles ([[the-prohibition-families-become-rule-pages-served-by-a-hook]]).

*(Compiled from `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
