---
title: "`scripts/vault-archive.sh` gains a `pages` kind, and the archive's clause about retired pages becomes executable"
type: decision
status: archived
authority: archive-kind-list
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-22
created: 2026-08-22
sources: ["scripts/vault-archive.sh", "job_hunt_ai_vault/archive/2026-08-31/2026-08-31-the-families-become-rules/pages/archive-is-dated-by-session-and-holds-what-left-the-working-set.md"]
tags: [vault, process, harness]
---

# The ruling, 2026-08-22

**`bash scripts/vault-archive.sh` accepts `pages` as a kind**, beside `handoffs`, `plans`, `specs`
and `notes`, and a retired wiki page moves to `archive/<date>/<session>/pages/`
([[vault-archive-sh]], [[the-archive-gains-a-folder-per-session-inside-the-date]]).

**The kind list is a decided list, and this is a change to it rather than a typo tolerated.** The
script rejects an unknown kind with exit 2 and creates nothing, which is what makes the list
decidable at all: a misspelling cannot mint a kind, so a new one arrives by a ruling and by nothing
else. The absent `logs` is the same rule from the other side — raised, unbuilt, and not accepted by
the script because nobody has ruled on it.

**And `pages` is the kind that is not an inbox kind.** The others are what leaves `raw/` — a
session's journal and the artefacts written beside it. A retired page leaves `wiki/`, which is a
different door, and until today the tool had no word for it.

# What it makes executable, and the clause had been unexecutable since 2026-08-16

[[archive-is-dated-by-session-and-holds-what-left-the-working-set]] has said since that date that
the dated folder holds *"the wiki pages retired that day, dated by the day they were retired"*.
**The tool could not express that destination.** Every retirement therefore went flat into
`archive/`, and about thirty pages sit there now.

**The practice quietly outvoted the rule for six days and no instrument reported it.** Nothing in
this store compares the archive's shape against the decision that fixed it: `vault-check.sh` reads
`archive/` for links and for `sources:` paths and never for layout, so a flat page and a dated one
are the same tree to every check here. **A rule with no instrument is decided by whatever the tool
happens to do** — which is this project's own failure shape met from the other side, a description
of behaviour inherited as a policy ([[no-rule-reads-a-harness-file]]).

**The disagreement was put to the owner when it surfaced, and he chose the decision over the
practice.** The occasion was retiring [[advisory-is-the-default-for-a-hook]], whose destination is
`archive/2026-08-22/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict/pages/`.

## Rejected: keeping the flat practice

**It is what the plan assumed**, and the assumption came from reading the tree rather than the
corpus — thirty flat pages are a loud precedent, and the decision that contradicts them is a clause
in a page nobody had opened. **Taking it would have meant amending the archive decision to describe
what the tool did**, which is the corpus being edited to agree with an omission in a script.

**Sweeping the flat pages into dated folders is not part of this and is the owner's.** Each move is
an address change inside `archive/`, and `sources:` citations point at those paths
([[a-rewriter-must-be-paired-with-a-detector]]).

# An ordering hole that is real and is not closed

**A session folder is named from the journal's own filename**
([[the-archive-gains-a-folder-per-session-inside-the-date]]), **and the journal does not exist until
`/handoff` runs at the end of the session.** So a page retired at any other moment has no legal
folder name, and every retirement that is not the last act of a session meets this.

**Worked around here rather than solved**: the slug was fixed at the start of the session and
`/handoff` is bound to write its journal under that name. **That is a promise, not a mechanism.**
Nothing compares the session folder holding the page against the journal that names the session, so
if `/handoff` writes anything else the page sits under a folder naming a session that does not
exist — and no check here would say so.

**Named rather than repaired**, because the repair is a change to how a session is named before it
has produced anything, and that is a decision of its own
([[the-archive-gains-a-folder-per-session-inside-the-date]],
[[archive-is-dated-by-session-and-holds-what-left-the-working-set]]).

# The flat pages stay flat, and the clause is forward-only — 2026-08-22

**Owner selected: the roughly thirty pages already sitting flat in `archive/` are not swept**, and
the dated form applies from this date forward.

**Rejected: sweeping them.** Each move is an address change inside `archive/`, and `sources:`
citations point at those paths — thirty addresses moving with a rewriter dragging them
([[a-rewriter-must-be-paired-with-a-detector]], [[a-page-rename-is-sed-and-verify]]).

**The precedent is the English rule**, which is forward-only with the file as its unit: what is
written from here on obeys, and what stands is not rewritten to match
([[the-english-rule-is-forward-only-and-the-unit-is-the-file]]).

**So the tree will hold two shapes at once for as long as nobody sweeps it**, and that is the decided
state rather than a backlog item. A reader looking for a retired page still finds it by name — a
`[[wikilink]]` resolves anywhere under `wiki/` or `archive/`, flat or dated.

# The ordering hole above is now ruled, and still not built — 2026-08-22

**The section *An ordering hole that is real and is not closed* has its answer**: the session slug is
written to a file by whoever first needs it, and `/handoff` reads it rather than inventing one
([[the-session-slug-is-written-to-a-file-and-the-handoff-reads-it]]).

**The section is not edited.** It described the state on the day it was written, and the promise it
names is what this session actually ran on
([[the-region-coverage-figure-is-dated-where-it-stands]]).
