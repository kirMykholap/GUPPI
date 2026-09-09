---
title: "The length of a title is deliberately unbounded, and no check measures it"
type: decision
status: archived
authority: title-length
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-19
sources: ["log.md", "scripts/vault-check.sh"]
tags: [retrieval, vault]
---

# Closed 2026-08-19: a length limit was offered and refused

**No check measures the length of a title, and none should.** This is a **closed** question, not an
open one: the next reader who notices a very long title in this corpus is looking at a title the
owner has already read and accepted.

Three options were put to him after the corpus clean-up pushed three titles well past anything the
vault had held before — **cap the length in the check**, **retitle the three back**, or **accept
them as they stand**. He took the third.

# Why: the length was paid for accuracy, on his own ruling

**Naming what is counted is longer than counting it, by construction.** That is the whole technique
[[a-title-names-what-is-counted-instead-of-counting-it]] prescribes, and the three longest titles in
the corpus are all direct products of the pass that applied it:

| the title before | what replaced the count | grew |
|---|---|---|
| *"Two measurements lied in opposite directions in one day…"* | *"A silent tool failure and a wrong denominator lied…"* | 143 → 175 |
| *"…and criterion 6 does not move because of it"* | *"…and the criterion that every governed file carries a region does not move because of it"* | 121 → 165 |
| *"…the owner's third lint check, asked for once and built by nothing"* | *"…the one of the owner's lint checks that was never made mechanical…"* | 121 → 158 |

The reasoning the owner accepted: **the corpus had just paid length for accuracy on his own
ruling, and a limit added afterwards would undo half of it.** A page cannot satisfy both rules
where the accurate name is long, and the rule that would give way is the one that exists to keep a
title from going false.

# The reading, and the instrument it was taken with

```
rg -N --no-filename '^title:' wiki | sed 's/^title:[ \t]*//; s/^"//; s/"$//' | awk '{print length($0)}' | sort -rn | head
```

Run from the vault root on 2026-08-19 it prints **175, 165, 158**, then 146 and 144. At `a1b89d9`,
before the pass, the same reading over the same corpus tops out at **143** — and that 143 is the
predecessor of the 175, so the longest title in this vault has been on the same page throughout.

**One figure quoted at the retrospective needs correcting, and it is an instrument difference
rather than a change in the corpus.** The previous maximum was stated as **145**: that is the same
title measured with its surrounding quotation marks counted, where 175, 165 and 158 are measured
without them. By one instrument the maximum was 143 and by the other it was 145, and the three new
figures are comparable only to the first
([[the-evidence-was-not-wrong-the-instrument-was-too-coarse]],
[[a-measurement-agreeing-with-no-expectation-needs-a-different-instrument]]). *(The command counts
bytes, not characters: `LC_CTYPE` is `C.UTF-8` and `LANG` is empty here, so the third title reads
158 while its em dash makes it 156 characters. The other two are ASCII throughout.)*

# Why there is no check, in principle and not only today

- **A long title cannot go false.** Rule 10 exists because a counting title makes an assertion that
  the world can contradict without anyone touching the page. Length asserts nothing; at worst it is
  inconvenient, and inconvenience is not what a gate is for.
- **A limit would charge its price to correct prose.** The same argument keeps rule 10's word list
  short: with no way for a page to declare itself exempt, a false positive is paid for by rewriting
  a title that was already right ([[ordinals-count-and-first-does-not]],
  [[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]).
- **Two checks over one string can leave a page with no legal title.** The accurate name for a
  counted set is sometimes long, and a page failing the quantity rule one way and the length rule
  the other has nowhere to go.

**Rejected, explicitly:** a red verdict on length; an advisory on length, which would print a line
nobody can act on, beside the standing tag advisories nobody has acted on
([[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]); and retitling the
three back, which would put the counts the owner had just ruled out back into the corpus.

# If length ever costs something, the evidence is a miss and not a threshold

Nothing has reported a cost yet: no answer, brief or retrieval has failed on a long title. If one
does, the route already exists — a `- miss:` line in `log.md` naming what failed
and where ([[the-growth-signal-is-the-brief]]). **A threshold invented before that evidence
would be a number nobody measured**, which this corpus has paid for before
([[a-page-that-says-measured-can-carry-a-figure-nobody-measured]]).

The companion rules on what a title may not contain and what shape it takes are
[[a-title-names-what-is-counted-instead-of-counting-it]] and
[[the-titles-form-follows-the-records-type]]; the boundary on which strings the quantity rule reads
at all is [[the-no-quantity-rule-reads-the-title-and-the-filename-and-never-the-body]].
