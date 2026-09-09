---
title: "uvicorn runs without --reload and Jinja auto_reload is off, so every change needs a restart"
type: entity
status: current
authority: restart-to-see-changes
basis: code
sprint: S0
created: 2026-08-13
sources: ["CLAUDE.md"]
tags: [web, process]
---

# Any change needs `docker compose restart app`

uvicorn runs **without `--reload`** and Jinja's `auto_reload` is **off** — the latter is enforced by
an AST boundary, see [[architectural-boundaries]].

So **any** change to code or templates is invisible in the browser until:

```
docker compose restart app
```

This is the single most common reason a browser walk appears to disprove a change that is in fact
correct. Restart first, then doubt the code. See
[[a-browser-walk-watches-the-network-not-the-screen]] for the other members of that family.

The console the CLI half of this project prints to has its own constraint: [[windows-console-encoding]].

The harness has the same property for its own configuration: [[claude-code-config-loading]].

---

**Found mis-filed on 2026-08-16**, and left where it is. This page is typed `entity` while its
`authority: restart-to-see-changes` is an **obligation** rather than a thing with properties. It is
one of two such records, and both are the same defect: nothing in the schema says what a record of
each type asserts, or what expires it ([[a-schema-per-type-says-what-a-record-asserts]]). Re-typing
it is supersession and waits on the owner.
