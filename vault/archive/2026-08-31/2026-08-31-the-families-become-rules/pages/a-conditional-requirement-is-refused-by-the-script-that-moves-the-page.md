---
title: "A conditional requirement is refused by the script that moves the page, not by the gate"
type: decision
status: archived
authority: conditional-requirement-placement
binding: prohibition
basis: code
sprint: S3
decided: 2026-08-23
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md", "scripts/vault-archive.sh", "job_hunt_ai_vault/wiki/rules/_schema.yaml"]
tags: [record-schema, harness, vault]
---

# The shape, and this store already had it

**A per-folder `_schema.yaml` states one required set for a whole folder.** It cannot say
*required when the status is `refused`*, or *required when `render:` is `whole`* — there is no
syntax for a condition and adding one would make the schema a program.

**So the conditional lives in whatever code already has the condition in front of it.**
`wiki/rules/_schema.yaml` says exactly this about `paths`: the field is optional there, and the
injector reports a `render: whole` page that carries none, because the injector is where
`render:` is known ([[paths-is-required-where-it-is-read-and-nowhere-else]],
[[paths-lives-on-the-vault-page-and-is-written-widest]]).

# Where the refusal for `refused` landed, and why it moved

**`scripts/vault-archive.sh` refuses to release a proposal carrying `status: refused` without
`decided_by:`.** It is the second precondition on that script and it fires before anything moves
([[vault-archive-sh]], [[a-refused-proposal-is-archived-and-takes-status-refused]]).

**The owner had accepted a verdict in `scripts/vault-check.sh` instead, and this placement is the
session's consequence rather than his ruling.** `/pre-task` found the accepted form unreachable: a
refused proposal is in `archive/` by the time the rule applies, and the gate's frontmatter pass
reads `wiki/` alone. The verdict would have been a rule that can never fire, which this store has
already paid for once ([[a-verdict-that-cannot-fire-is-worse-than-no-verdict]],
[[the-unreachable-verdict-is-dropped-and-replaced]]).

**The move is to the last point at which anything sees the page.** After the archive step nothing
checks, sweeps or reads it — not the gate, not the injector, not `vault-authority.sh`, not
`/pre-task` — so the moment of the move is the only place a condition about an archived page can be
enforced at all ([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).

# The rule this gives, and what it is chosen against

**Put a conditional requirement in the reader that already knows the condition, and say in the
schema that it lives there.** Both `_schema.yaml` files that carry such a condition name the script
that enforces it, so a reader of the schema is not left thinking the field is merely optional.

**Chosen against a conditional syntax in the schema files.** That would give the gate a second
parser and a second set of failure modes, for two conditions.

**Chosen against leaving it unenforced** and relying on the ruling being remembered. A requirement
nothing checks is the class of claim this sprint exists to remove.

# What it obliges

**A verdict has to be reachable from where it is written**, and the check is cheap: name the file
set the reader walks and ask whether the page is still in it when the rule applies. That question
went unasked in a design pass and an approval here, and `/pre-task` is what asked it
([[a-pre-task-runs-between-the-plan-and-its-approval]]).
