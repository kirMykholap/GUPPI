#!/usr/bin/env bash
# Structural checks over the vault. Exits 1 and prints one line per violation.
# Run: bash scripts/vault-check.sh
#
# Every rule here exists because that failure has already happened in this project at least
# once, and `scripts/vault-check-selftest.sh` breaks each of them on purpose to prove the rule
# is still there. If a rule fails, fix the vault; if you think the rule is wrong, change it in
# the selftest first.
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1
fail=0
note() { echo "VAULT-CHECK: $*"; fail=1; }

# `--lint` ADDS THE CORPUS-STATE ADVISORIES; IT NEVER TAKES A CHECK AWAY (2026-08-20).
#
# A bare run answers one question: is anything wrong with the tree in front of me. Tag density
# is not that question - it is a statistic about the whole corpus, it can never fail, and the
# decision it feeds is made once a sprint at `/vault-lint`. Printed on every run it buried the
# one advisory that IS about this run, and the store has the cost on the record three times
# over: an always-firing advisory stops being read, starts being managed, and becomes
# indistinguishable from one that was scheduled and skipped - which is how the `record-schema`
# sweep went missing for three days.
#
# TWO PROPERTIES HOLD THIS, AND BOTH ARE SELFTEST CASES RATHER THAN PROMISES:
#   - the exit code is IDENTICAL with and without the flag. A flag that can change the exit code
#     is hiding a check, not a report, and that is a defect rather than a setting;
#   - only lines that CANNOT FAIL may ever go behind it. Severity here is `note` (which sets
#     `fail=1`) against a bare `echo`, with no third state - so the class is decidable rather
#     than a matter of judgement, and nobody can later move a verdict behind this flag by
#     appealing to the same argument.
LINT=0
RULES=0
for arg in "$@"; do
  case "$arg" in
    --lint) LINT=1 ;;
    --rules) RULES=1 ;;
    *) echo "VAULT-CHECK: unknown argument: $arg (the legal ones are --lint and --rules)"; exit 2 ;;
  esac
done

# `--rules` IS A MODE, NOT A FILTER, and the difference is what keeps it clear of the prohibition
# above. That prohibition governs a flag that changes what a RUN reports: the exit code must be
# identical with and without it, and only lines that cannot fail may go behind it. `--rules` runs
# no check at all - it never reaches the vault, never prints `VAULT-CHECK: ok`, and always exits 0.
# There is no run for it to hide anything from. A flag that filtered rules OUT of a run would be
# the forbidden thing, and this is not that; the distinction is written here because the next
# reader will meet the two in the same `case` and has to be able to tell them apart.
#
# THE REGISTER IS SWEPT FROM THE SCRIPT'S OWN HEADINGS AND IS NEVER A LIST. Three copies of this
# numbering have drifted already: `wiki/entities/vault-scripts.md` carries eighteen conditions that
# never matched the script, and the correction it wrote about that in 2026-08-17 is itself stale -
# it says "rules 1-8 plus 5b, then 10, 11 and 12", knowing nothing of 5c, 13 or 14. A drifted copy
# is repaired by deleting it, so this prints rather than restates.
#
# WHAT IT DOES NOT PROMISE: that the register is COMPLETE. A rule the gate can emit but that
# carries no heading is invisible here and nothing would report it. The sweep proves the list is
# derived, never that it is whole.
#
# The headings are printed verbatim, including `4 and 5.` on one line and `9. RETIRED`. Neither is
# tidied: 4 and 5 are two questions over one set built once, and a retired number is never reused,
# so a register that renumbered either would be lying about what the pages cite. For the same
# reason the order is the FILE's - `5c` stands above `5b` here because it does in the script - and
# a heading that opens a multi-line comment prints its first line and no more. Both are the script
# as it is; imposing a sort or reassembling a sentence would make this a second opinion about the
# numbering rather than a reading of it.
if [ "$RULES" = 1 ]; then
  swept=$(grep '^# [0-9]' "${BASH_SOURCE[0]}" | sed 's/^# //')
  echo "VAULT-CHECK: rules: $(printf '%s\n' "$swept" | wc -l | tr -d ' ') heading(s), swept from this script"
  printf '%s\n' "$swept" | sed 's/^/VAULT-CHECK: rules:   /'
  exit 0
fi

# The vault's directory name is the name Obsidian shows, so the owner may rename it - it has
# changed four times. Nothing here may depend on that name. Dot-directories are excluded and
# the rest sorted, so this answers the same as `.claude/hooks/vault-path.ps1`: two discovery
# rules that can disagree are worse than either of them.
VAULT="${VAULT:-}"
if [ -z "$VAULT" ]; then
  VAULT=$(find . -maxdepth 2 -type d -name wiki -not -path './.*' 2>/dev/null \
          | sed 's|/wiki$||; s|^\./||' | sort | head -1)
fi
[ -n "$VAULT" ] || { echo "VAULT-CHECK: no vault found (no top-level directory contains a wiki/)"; exit 1; }

pages=$(find "$VAULT/wiki" -name '*.md' 2>/dev/null | sort)

# NAMED RATHER THAN TYPED. A newline written literally inside a `case` pattern survives this file
# and every quoting layer around it right up until something copies the line through a shell, and
# this repository has spent six failures in one session on exactly that class. `$'\n'` says which
# character it is, once, where a reader can see it.
NL=$'\n'

# THE TYPE WORDS ARE SWEPT OFF THE TREE, NEVER LISTED (2026-08-18).
#
# A marker carries its record's type - `<!-- concept: some-slug -->` - and the type word is the
# SINGULAR, which is the same string rule 2 below already computes from the folder. So one
# derivation serves both directions and is written once, here, as `singular:plural` pairs read
# out of `wiki/` itself.
#
# It is a sweep because the folder set already exists in four places - rule 1, the catalogue,
# the vault's `CLAUDE.md` and `index.md` - and was forgotten in one of them within a day of
# being written. A fifth literal copy inside this file would be the same mistake with the same
# outcome, so legality of a type word is not "is it in a list" but "does its folder exist",
# which rule 1 already sweeps immediately below.
#
# The singularisation is `ies -> y` then a trailing `s`, which covers the six and would cover a
# seventh spelled regularly. A folder whose singular this gets wrong shows up the moment rule 2
# reports every page in it as disagreeing with its own folder - loudly, on every page, rather
# than as one silent unresolvable marker.
# Built with parameter expansion, not a `sed` per folder: a process costs about 40 ms on this
# platform and the selftest runs this file about ninety times. Six folders spent half a second
# in the first draft of these five lines, for a substitution bash does for nothing.
typemap=""
while IFS= read -r d; do
  [ -n "$d" ] || continue
  d=${d##*/}
  case "$d" in
    *ies) typemap="$typemap${d%ies}y:$d " ;;
    *s)   typemap="$typemap${d%s}:$d " ;;
    *)    typemap="$typemap$d:$d " ;;
  esac
done < <(find "$VAULT/wiki" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | sort)

# 1. Layout exists
# `wiki/proposals/` is the fifth category, added 2026-08-15: what was raised or deferred and
# never built. It is a folder rather than a `status:` value on a page in `decisions/`, because
# this project has twice compiled intent as though it were a record of something built, and a
# folder makes that mistake structurally impossible where a field asks to be read carefully.
# Nothing else here needs changing: `want` is the folder minus its trailing s, so a page in
# proposals/ must carry `type: proposal` and the type rule enforces it for free.
#
# `wiki/rules/` is the sixth, added 2026-08-17 for the same reason and by the same mechanism: a
# rule is a record whose text is RENDERED into the file it governs, and a folder is what stops it
# being filed as a description of something that merely happened. It is a folder rather than a
# status because that argument has already been had twice here. Rule 11 below is what reads it.
for d in raw/handoffs wiki/decisions wiki/concepts wiki/entities wiki/lessons wiki/proposals wiki/rules archive; do
  [ -d "$VAULT/$d" ] || note "missing directory: $VAULT/$d"
done
# `authority.md` joined this list on 2026-08-21 with the register itself. It is the librarian's
# dictionary of authority families - the grouping that is nowhere in the tree and cannot be derived
# from it - and rule 13 below asks its question by running a tool that reads it, so a vault without
# it has a lookup that answers nothing rather than a lookup that fails
# ([[authority-becomes-the-index-and-is-required-outside-rules]]).
for f in CLAUDE.md index.md tags.md log.md authority.md; do
  [ -f "$VAULT/$f" ] || note "missing file: $VAULT/$f"
done

# 2. Everything the frontmatter has to answer for, in one pass over the corpus.
#
#    - the six required fields are present;
#    - `type` agrees with the folder the page sits in;
#    - `status` is one of the two the schema defines, and a deprecated page has left `wiki/`;
#    - a decision carries the date it was taken - `created:` is the ingest date and is
#      identical on every page migrated in one pass, so without `decided:` a decision from
#      slice 2b is indistinguishable from one taken last week, which is most of what a
#      decision is for;
#    - every repository path in `sources:` still exists, because a citation to a file that is
#      not there is worse than none: it reads as provenance and is not. Seventeen pages went
#      on citing `vault/raw/handoffs/...` after the vault was renamed and nothing noticed. A
#      path inside the vault is written relative to it, one outside relative to the repository
#      root, and a URL is not a path at all;
#    - `authority` is collected here rather than grepped, and only from `current` pages;
#    - and so are the tags, which is the whole point of doing this in one place.
#
#    ONLY THE FRONTMATTER BLOCK COUNTS. Read line-wise, a fenced ```yaml example containing
#    the six field names satisfies the required-fields rule on a page that has no frontmatter
#    at all, and an `authority:` line inside such an example forges a duplicate against a real
#    page - whose obvious "fix" is to change the real page. The link rules below have stripped
#    fences since the day a `<script>` comment satisfied an id search; these rules had not.
#
#    Tags are parsed from both spellings YAML allows. Only the inline `[a, b]` form was read
#    before, so a page written by Obsidian's own property editor - which emits a block list -
#    contributed no tags at all: an unregistered tag on it went unreported and the 2-to-4 rule
#    never fired, because a page with no entries never reaches the count. The vault is opened
#    in Obsidian by design, so that spelling is not hypothetical.
#
#    One pass, not one grep per field per page: that was some 700 processes for 75 pages and
#    the larger half of this script's running time. A check the librarian is told to run after
#    every write must stay cheap enough that it is actually run.
#    AND THE KEY SET COMES FROM THE FOLDER, NOT FROM THIS FILE (owner, 2026-08-19). Each
#    `wiki/` folder carries `_schema.yaml` naming the keys a page there must and may hold, and
#    this check reads it. The alternative was a list here beside the one in the store's schema,
#    and rule 11 already records what this project thinks of two lists of one set: they drift,
#    and two selftest cases were lost to exactly that.
#
#    A FOLDER WITH NO SCHEMA IS RED, not permissive. The failure to design around is a parse
#    that yields nothing and turns the gate into "every key is fine" - silently, and in the
#    direction of passing. That is why this is a verdict and not a default.
schemamap=""
valuemap=""
while IFS= read -r sfolder; do
  [ -n "$sfolder" ] || continue
  sfile="$VAULT/wiki/$sfolder/_schema.yaml"
  if [ ! -f "$sfile" ]; then
    note "wiki/$sfolder: no _schema.yaml - the check reads the folder's key set from it and cannot judge a page without it"
    continue
  fi
  sreq=$(awk '{sub(/$/,"")} /^required:/{m=1;next} /^optional:/{m=2;next} /^[a-z]/{m=0} m==1 && /^[ 	]*-[ 	]*/{sub(/^[ 	]*-[ 	]*/,"");print}' "$sfile" | tr '
' ',')
  sopt=$(awk '{sub(/$/,"")} /^optional:/{m=1;next} /^[a-z]/{m=0} m==1 && /^[ 	]*-[ 	]*/{sub(/^[ 	]*-[ 	]*/,"");print}' "$sfile" | tr '
' ',')
  if [ -z "$sreq" ]; then
    note "wiki/$sfolder/_schema.yaml: no required: keys parsed - a schema that yields nothing would let every key through"
    continue
  fi
  schemamap="$schemamap$sfolder>$sreq>$sopt "

  #    AND THE SAME FILE NAMES THE LEGAL VALUES OF A FIELD (owner, 2026-08-19). The block is
  #    `values:`, one indented `field:` under it, and that field's values as a list. Before this
  #    the gate asked only whether `basis` was PRESENT, so `basis: banana` passed on the one
  #    field every conflict is resolved by. Read here rather than listed in this script, for the
  #    reason the key set is: two lists of one set drift, and this store has lost cases to it.
  #
  #    A `values:` header present and parsing to nothing is RED, not permissive - an empty legal
  #    set would pass every value silently, which is the direction that hides a defect.
  if grep -q '^values:' "$sfile"; then
    sval=$(awk -v fo="$sfolder" '
      { sub(/$/, "") }          # a CRLF schema must read the same as an LF one, as the page pass does
      /^values:/ { m = 1; next }
      /^[a-z]/   { m = 0 }
      m == 1 && /^[ \t]+[A-Za-z_]+:[ \t]*$/ { f = $1; sub(/:$/, "", f); next }
      m == 1 && f != "" && /^[ \t]+-[ \t]*/ {
          v = $0; sub(/^[ \t]*-[ \t]*/, "", v); gsub(/[ \t]+$/, "", v)
          if (v != "") acc[f] = acc[f] (acc[f] == "" ? "" : ",") v }
      END { for (k in acc) printf "%s>%s>%s ", fo, k, acc[k] }' "$sfile")
    if [ -z "$sval" ]; then
      note "wiki/$sfolder/_schema.yaml: a values: block that parses to nothing - an empty legal set would let every value through, silently and in the direction of passing"
    else
      valuemap="$valuemap$sval"
    fi
  fi
done < <(find "$VAULT/wiki" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | sed 's|.*/||' | sort)

# THE AWK PROGRAM BELOW IS ONE ARGUMENT AND IT IS CLOSE TO A HARD CEILING. Found on 2026-08-30 by
# walking into it: about 1.7 KB of comments were added inside the program, `xargs` answered
# `cannot fit single argument within argument list size limit` ON STDERR ONLY, the pass produced
# NOTHING, and the gate went on exiting 0. The single visible symptom was every registered tag
# reported as used on no page - which reads as a corpus problem and is not one.
#
# THE NUMBERS, so the next reader has a distance rather than a warning: the program region ran to
# 78,516 bytes at `0da5e96`, is 79,109 today, and 82,425 is a size that FAILS on this machine. So
# the headroom is under four kilobytes and it has been that way for some time - nothing measured
# it, and nothing measures it now except the selftest case asserting this script writes no stderr.
#
# WHAT TO DO WHEN IT IS HIT: move the program into a file of its own and call `awk -f`, which
# removes the limit rather than deferring it. DO NOT buy room by deleting the reasoning inside the
# program - that is what this comment block is, reasoning evicted to the outside of the quotes
# because it costs nothing here and counts against the ceiling there.
#
# THE REASONING EVICTED ON 2026-08-30, kept here in full:
#
#   `render:` is captured with the other frontmatter fields because three verdicts branch on it and
#   re-reading each page for one field would be a second process per rule. The value itself is
#   judged by the generic legal-values pass.
#
#   `nogoverns` skips a page under `render: authority`. That mode delivers a rule by lookup rather
#   than by injection - a hook hands over the rule whose `authority:` matches the file being
#   touched - so there is no destination to name, and demanding one would make the mode illegal on
#   the day it was minted. The condition lives here rather than in the schema because a per-folder
#   schema cannot say "required unless another field says otherwise", which is the arrangement
#   `paths:` under `render: whole` already has.
#
#   `authoritygoverns` and `authoritynoslug` are what make the new mode cost something. A mode that
#   only ever switched a check off would be a per-page waiver, which this store has refused before;
#   so `authority` carries obligations of its own, and each verdict names an edit that turns it
#   green - drop the field, or add the field.
#
#   `ruleclaim` is unchanged and still fires on any page carrying both fields. A `render: authority`
#   rule carries `authority:` and no `governs:`, so it never trips it.
#
#   The `authority` fact is emitted under its FOLDER, and that is what makes rule 3 compare within
#   a type rather than across the corpus (owner, 2026-08-30): two pages of the same type may not
#   answer one question, and two of different types may - and should, because they inherit the slug
#   from the decision or proposal that produced them. `rg "^authority: X" wiki` then returns the
#   whole chain of one question. What is given up: a decision and the concept describing it can now
#   disagree under one slug and nothing reddens. `folder` and `type:` are the same word - the type
#   verdict reddens any page where they differ - so keying on the folder is keying on the type.
#
# AND NO APOSTROPHE MAY APPEAR INSIDE THE PROGRAM. It is a single-quoted shell string: one
# apostrophe closes the quote and the next backtick becomes a command substitution. That was the
# first way this same comment block broke the gate, an hour before it broke it the second way.
authorities=""
rulegoverns=""
if [ -n "$pages" ]; then
  facts=$(printf '%s\n' "$pages" | tr '\n' '\0' | xargs -0 awk -v typemap="$typemap" -v schemamap="$schemamap" -v valuemap="$valuemap" '
    #    `governs:` MAY NAME MORE THAN ONE FILE (2026-08-21), and the scalar is the one-element
    #    case. The same two spellings the injector accepts and no third: `scripts/vault-inject.sh`
    #    holds the authoritative parser and this one has to agree with it, so both were written
    #    from the same four rules - trim, strip one layer of quotes, split an inline list on
    #    commas, and a bare value is a list of one. Two readers of one field that can disagree
    #    about how it is spelled are worse than either of them, which is why this vault already
    #    derives its category words identically in two places rather than sharing one copy.
    function govsplit(v, out,   line, n, parts, i, t, c) {
        line = v
        gsub(/^[ \t]+|[ \t]+$/, "", line)
        c = 0
        if (line ~ /^\[.*\]$/) {
            sub(/^\[/, "", line); sub(/\]$/, "", line)
            n = split(line, parts, /,/)
            for (i = 1; i <= n; i++) {
                t = parts[i]
                gsub(/^[ \t]+|[ \t]+$/, "", t)
                gsub(/^["\047]|["\047]$/, "", t)
                if (t != "") out[++c] = t
            }
        } else {
            gsub(/^["\047]|["\047]$/, "", line)
            if (line != "") out[++c] = line
        }
        return c
    }
    BEGIN { n = split(typemap, pairs, " ")
            for (i = 1; i <= n; i++) { split(pairs[i], p, ":"); if (p[2] != "") single[p[2]] = p[1] }
            n = split(schemamap, entries, " ")
            for (i = 1; i <= n; i++) {
                if (entries[i] == "") continue
                split(entries[i], parts, ">")
                fo = parts[1]; hasschema[fo] = 1
                m = split(parts[2], rr, ",")
                for (j = 1; j <= m; j++) if (rr[j] != "") { reqn[fo]++; reqof[fo, reqn[fo]] = rr[j]; allowed[fo, rr[j]] = 1 }
                m = split(parts[3], oo, ",")
                for (j = 1; j <= m; j++) if (oo[j] != "") allowed[fo, oo[j]] = 1
            }
            n = split(valuemap, ventries, " ")
            for (i = 1; i <= n; i++) {
                if (ventries[i] == "") continue
                split(ventries[i], vp, ">")
                fo = vp[1]; fld = vp[2]
                if (!((fo SUBSEP fld) in hasvalues)) { hasvalues[fo, fld] = 1
                                                       valfields[fo] = valfields[fo] " " fld }
                m = split(vp[3], vv, ",")
                for (j = 1; j <= m; j++) if (vv[j] != "") legal[fo, fld, vv[j]] = 1
            } }
    { sub(/\r$/, "") }                       # a CRLF corpus must read the same as an LF one
    FNR == 1 {
        sub(/^\xef\xbb\xbf/, "")             # a BOM before --- would hide the whole frontmatter
        files[FILENAME] = 1; fm[FILENAME] = ($0 == "---"); opened[FILENAME] = ($0 == "---")
        intags = 0; insources = 0; infence = 0; next
    }

    #    THE BODY IS READ FOR ONE THING ONLY: whether the page marks a slice to ship. A page
    #    carrying `<!-- text -->` and no `governs:` marks text that nothing delivers - the
    #    injector never opens it, so the mark is silent decoration and reads as governed. That
    #    is the inverse of a rule with no `governs:` and it is red for the same reason.
    #
    #    Fences and code spans are stripped first, and both halves are needed here: the vault
    #    CLAUDE.md documents the slice form inside backticks and several pages document it in a
    #    fenced block. This is the sixth place in this repository to need that pass.
    !fm[FILENAME] {
        if ($0 ~ /^```/) { infence = !infence; next }
        if (infence) next
        clean = $0; gsub(/`[^`]*`/, " ", clean)
        if (clean ~ /^<!--[ \t]+text[ \t]+-->[ \t]*$/) marked[FILENAME] = 1
        next
    }
    /^---[[:space:]]*$/ { fm[FILENAME] = 0; closed[FILENAME] = 1; next }

    /^[A-Za-z_]+:/ {
        intags = 0; insources = 0; ingoverns = 0
        split($0, kv, ":"); seen[FILENAME SUBSEP kv[1]] = 1
        if (!((FILENAME SUBSEP kv[1]) in counted)) { counted[FILENAME SUBSEP kv[1]] = 1
                                                    keylist[FILENAME] = keylist[FILENAME] " " kv[1] }
        value = $0; sub(/^[A-Za-z_]+:[ \t]*/, "", value)
        #    Kept for EVERY key, because which fields carry a legal value set is a question the
        #    schema answers, and this parser must not hold a second copy of that answer. First
        #    occurrence only, matching how `type:` and `status:` below already behave.
        if (!((FILENAME SUBSEP kv[1]) in fieldval)) {
            fv = value
            sub(/[ \t]+#.*$/, "", fv)        # a trailing YAML comment is not part of the scalar
            gsub(/^["\047]|["\047]$/, "", fv)
            gsub(/^[ \t]+|[ \t]+$/, "", fv)
            fieldval[FILENAME, kv[1]] = fv
        }
    }
    /^type:/      { if (!(FILENAME in kind))   kind[FILENAME]   = value }
    /^status:/    { if (!(FILENAME in state))  state[FILENAME]  = value }
    /^authority:/ { if (!(FILENAME in claim))  claim[FILENAME]  = value }
    /^render:/    { if (!(FILENAME in rendermode)) rendermode[FILENAME] = value }
    /^governs:/   { if (!(FILENAME in destination)) destination[FILENAME] = value
                    #    THE BLOCK FORM IS LEGAL YAML AND IS REFUSED, the owner ruled it 2026-08-21.
                    #    An empty value here means the destinations are meant to follow as `- `
                    #    items, which neither this parser nor the injector reads - so the text
                    #    would render into a subset of its destinations and the gate would read
                    #    the remainder as drift. A YAML editor and PyYAML both accept it, which
                    #    is exactly why a silent refusal would be a trap: the page looks right
                    #    and the parser agrees.
                    if (value == "") ingoverns = 1 }
    #    Reset on the next key line, alongside `intags` and `insources` above, so a `- ` item
    #    belonging to some later block-valued field is never read as belonging to this one.
    ingoverns && /^[ \t]*-[ \t]/ { blockgoverns[FILENAME] = 1 }
    /^decided:/   { dated[FILENAME] = 1 }

    # `sources:` is list-valued and YAML spells such a field at least five ways: inline,
    # inline wrapped over two lines, a block list quoted or not, and a bare scalar. The whole
    # field is buffered here and read once in END rather than decided line by line - an
    # earlier version asked "is the sources: line blank?" and treated "not blank" as
    # "complete", which silently dropped every entry after the first on four of those five
    # spellings. That is not hypothetical: the longest `sources:` line in this corpus is 196
    # characters against a 100-column rule, so the first librarian who wraps it loses its
    # citations - on the one field whose entire purpose is that citations resolve.
    /^sources:/ {
        if (!(FILENAME in sourced)) { sourced[FILENAME] = 1; srcbuf[FILENAME] = value; insources = 1 }
        next
    }
    insources && /^([ \t]|-)/ { srcbuf[FILENAME] = srcbuf[FILENAME] " " $0; next }

    /^tags:/ {
        if (FILENAME in tagsseen) print "duptags|" FILENAME "|"
        tagsseen[FILENAME] = 1
        rest = value
        gsub(/[\[\]]/, "", rest)
        gsub(/["\047]/, "", rest)            # `tags: ["vault"]` is legal YAML and means vault
        if (rest ~ /[^ \t]/) {
            n = split(rest, a, ",")
            for (i = 1; i <= n; i++) {
                gsub(/^[ \t]+|[ \t]+$/, "", a[i])
                if (a[i] != "") { print "tag|" FILENAME "|" a[i]; count[FILENAME]++ }
            }
        } else {
            intags = 1          # a block list follows, one `- name` per line
        }
        next
    }
    intags && /^[ \t]*-[ \t]*/ {
        one = $0; sub(/^[ \t]*-[ \t]*/, "", one)
        gsub(/["\047]/, "", one); gsub(/^[ \t]+|[ \t]+$/, "", one)
        if (one != "") { print "tag|" FILENAME "|" one; count[FILENAME]++ }
        next
    }

    END {
        for (f in files) {
            # One buffer per page, read here, so every spelling of the field lands in the
            # same place: quoted entries first, then unquoted list items, then a bare scalar.
            if (f in srcbuf) {
                line = srcbuf[f]; found = 0
                while (match(line, /"[^"]*"/)) {
                    print "source|" f "|" substr(line, RSTART + 1, RLENGTH - 2)
                    line = substr(line, RSTART + RLENGTH); found = 1
                }
                if (!found) {
                    line = srcbuf[f]
                    while (match(line, /(^|[ \t])-[ \t]+[^ \t]+/)) {
                        item = substr(line, RSTART, RLENGTH)
                        sub(/^[ \t]*-[ \t]+/, "", item)
                        print "source|" f "|" item; found = 1
                        line = substr(line, RSTART + RLENGTH)
                    }
                }
                if (!found) {
                    t = srcbuf[f]; gsub(/^[ \t]+|[ \t]+$/, "", t)
                    sub(/^\[/, "", t); sub(/\]$/, "", t)
                    if (t != "") print "source|" f "|" t
                }
            }

            # An unterminated block is not a frontmatter: everything below it was read as
            # fields, so a prose line beginning `authority:` became a claim. Obsidian shows
            # such a page no properties at all, and nothing here said so either.
            if (opened[f] && !(f in closed)) print "unterminated|" f "|"

            folder = f; sub(/\/[^\/]*$/, "", folder); sub(/.*\//, "", folder)

            #    Required and allowed both come from `wiki/<folder>/_schema.yaml`. A folder
            #    with no schema was already reported once, by name, before this pass ran;
            #    repeating it per page would bury the one line that matters under sixty.
            if (folder in hasschema) {
                for (i = 1; i <= reqn[folder]; i++)
                    if (!((f SUBSEP reqof[folder, i]) in seen)) print "missing|" f "|" reqof[folder, i]
                m = split(keylist[f], kk, " ")
                for (i = 1; i <= m; i++)
                    if (kk[i] != "" && !((folder SUBSEP kk[i]) in allowed)) print "unknownkey|" f "|" kk[i]

                #    A field is judged on its value only where the schema names a legal set for
                #    it, and only when the page carries it: a missing field is already the
                #    `missing` verdict above, and saying it twice buries the line that matters.
                vn = split(valfields[folder], vf, " ")
                for (i = 1; i <= vn; i++) {
                    if (vf[i] == "" || !((f SUBSEP vf[i]) in fieldval)) continue
                    fv = fieldval[f, vf[i]]
                    if (!((folder SUBSEP vf[i] SUBSEP fv) in legal)) print "badvalue|" f "|" vf[i] "=" fv
                }
            }

            #    The singular comes from the swept map at the top of this file and not from a
            #    second `sub(/s$/)` written here. Rule 11 needs the same correspondence in the
            #    other direction, and two derivations of one rule are two answers waiting to
            #    differ - which is the whole argument the folder set already lost once.
            want = single[folder]
            if (kind[f] != want) print "type|" f "|" kind[f]
            if (folder == "decisions" && !(f in dated)) print "decided|" f "|"

            # A rule answers with `governs:` and never with `authority:`. The two fields would
            # otherwise share a slug on every decision-and-rule pair - the rule states what the
            # decision decided - and rule 3 below would print a contradiction on each of them,
            # whose obvious "fix" is to break one of the two pages that are both correct.
            # `governs:` is required because a rule naming no destination renders nowhere.
            # It was ALSO unique across current rules until 2026-08-17, when the owner removed
            # that: the argument confused a region with a file, and a file carries as many
            # regions as it has rules. The removal is argued where the verdict used to print,
            # below rule 3. Nothing about uniqueness is checked here any more.
            #    ONLY THE FIRST AND THIRD OF THESE STAY NARROW (2026-08-18). `governs:` became a
            #    property of any page, and reading that as "drop the gate" would drop three
            #    verdicts that want three different fates:
            #
            #    - `nogoverns` is rules-only and must stay so. A rule that names no destination
            #      renders nowhere, which is what makes it required THERE; widening it would
            #      demand `governs:` on all 258 pages, most of which deliver nothing by design.
            #    - `ruleclaim` is rules-only and stays so because its argument is rule-specific:
            #      the decision-and-rule pair shares a slug. Whether a `concepts/` page may own
            #      an `authority:` AND render is a shape nothing in the vault rules on, and
            #      leaving the gate narrow is what preserves that question instead of answering
            #      it by accident here.
            #    - `governs` widens, and it is the one that had to. It builds the pair table
            #      rule 11 joins against, so a page outside `wiki/rules/` was invisible to the
            #      address verdict - reported as neither rendered nor refused.
            #    `ruleclaim` WIDENED 2026-08-19, and the paragraph above is what it answers.
            #    That text kept the gate narrow because "whether a concepts/ page may own an
            #    authority: AND render is a shape nothing in the vault rules on". The vault
            #    now rules on it, so the ruling was wider than the gate enforcing it - the
            #    exact shape this harness exists to make impossible - and the verdict follows
            #    the ruling: it fires on ANY page carrying both. Rules are unchanged in
            #    practice, since `governs:` is required there and a rule with an authority:
            #    always carried both anyway.
            #    THE BLOCK FORM IS NAMED BEFORE `nogoverns` GETS TO IT, and that ordering is the
            #    whole of what this verdict adds. A rules page written in the block form already
            #    went red - `destination` is empty, so `nogoverns` fired - but it said "a rule
            #    with no governs:" about a page that names two destinations plainly. Failing
            #    loudly with the wrong diagnosis sends the reader to add a field that is already
            #    there, and this corpus has a page about that exact failure class. It fires on
            #    ANY folder: the spelling is illegal wherever it is written, and a non-rules page
            #    carrying `governs:` has its own verdict for a different question.
            if (f in blockgoverns) print "blockgoverns|" f "|"
            #    The lookup mode has no destination; the two verdicts under it are argued above.
            else if (folder == "rules" && rendermode[f] != "authority" \
                     && (!(f in destination) || destination[f] == "")) print "nogoverns|" f "|"
            if (folder == "rules" && rendermode[f] == "authority" \
                && (f in destination) && destination[f] != "") print "authoritygoverns|" f "|"
            if (folder == "rules" && rendermode[f] == "authority" \
                && (!(f in claim) || claim[f] == "")) print "authoritynoslug|" f "|"
            if ((f in claim) && (f in destination) && destination[f] != "") print "ruleclaim|" f "|" claim[f]

            #    Keyed `folder/slug` and not on the basename alone: with six folders in scope a
            #    basename is no longer an address. There are no collisions in the corpus today,
            #    and the type went into the marker precisely so that there need never be a
            #    lookup that could find two.
            if ((f in destination) && destination[f] != "" && state[f] == "current") {
                slug = f; sub(/\.md$/, "", slug); sub(/.*\//, "", slug)
                #    ONE FACT PER DESTINATION, so rule 11 below can ask `is this file among
                #    them` without learning that the field has a syntax. A page naming one
                #    file emits one fact, exactly as before this became a list.
                delete dests
                ndest = govsplit(destination[f], dests)
                for (di = 1; di <= ndest; di++) print "governs|" f "|" folder "/" slug "|" dests[di]
            }

            #    The inverse of `nogoverns`, and red for the same reason: text marked to ship
            #    from a page that names no destination is delivered by nothing and still reads
            #    as governed. Rules are exempt only because `nogoverns` says it about them
            #    first, and one fault reported twice teaches a reader to skip both.
            if ((f in marked) && folder != "rules" && (!(f in destination) || destination[f] == ""))
                print "slicenogoverns|" f "|"

            #    THE LEGAL STATUS VALUES ARE NOT LISTED HERE, since 2026-08-23. They were, as a
            #    hardcoded pair on this line with the pair restated in the message beside it, and
            #    they moved into every `wiki/*/_schema.yaml` under `values:` - read by the same
            #    generic pass that already read `basis`, `render` and `binding`. The gate is the
            #    reader, not the register ([[the-legal-value-list-lives-in-each-folders-schema]],
            #    [[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).
            #    An illegal value now arrives as `badvalue`, which names the schema that refused it.
            #
            #    WHAT STAYS HERE IS THE CONSEQUENCE OF A VALUE, which is not a legal-set question.
            #    `deprecated` obliges a page to leave `wiki/` and the verdict below says so.
            #
            #    `implemented` DOES NOT, and a verdict saying it did was written here on 2026-08-23
            #    and removed the same day when the owner corrected it. The session read the mark as
            #    NOTE, and this is why the sentence above avoids an apostrophe: every line in this
            #    block sits inside a single-quoted awk program, so one apostrophe ends the quote
            #    and bash starts parsing awk. It happened on this very edit
            #    ([[an-apostrophe-in-an-awk-comment-ends-the-shell-quote]]).
            #    an address - implemented means it lives in `archive/`, so implemented-in-`wiki/`
            #    is an error. It is not. The mark opens a state rather than closing one: a page
            #    takes `implemented`, STAYS here while it is tested for having someone who points
            #    at it, and moves only once it passes, with its citations rewritten on the way.
            #    A red verdict would have refused the whole middle of that, which is where the
            #    page legitimately sits for as long as no successor names it yet.
            #
            #    So nothing here judges `implemented`. What does the testing is
            #    `scripts/vault-archive.sh`, which refuses the move while no live page names the
            #    slug - the same condition at the one moment it decides something. An advisory
            #    listing pages waiting in that state is owed and is not written
            #    ([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).
            #
            #    `archived` JOINS THIS VERDICT 2026-08-28 AND `processed` DOES NOT, and the two
            #    were minted on the same day, which is exactly why the difference is written here
            #    rather than left to be inferred. `archived` is written BY THE SWEEP as it moves a
            #    page, so a page still in `wiki/` carrying it is a move that did not finish - and
            #    the sweep is now allowed to leave one behind, because it continues past a refused
            #    move and reports the refusals at the end (owner, 2026-08-28). This verdict is what
            #    makes that leftover visible instead of silent.
            #
            #    `processed` OPENS A STATE (owner, 2026-08-28), the same ruling `implemented`
            #    carries: the librarian sets the mark, the page STAYS here, and the sweep moves it
            #    as a separate step. So a processed page in `wiki/` is legitimate and expected, and
            #    reddening it would refuse the whole middle of the mechanism. The detail field
            #    carries the value so one message can name whichever mark it found.
            #    `repealed` JOINS IT 2026-08-30, and for the same reason `deprecated` is here
            #    rather than the reason `archived` is. A repealed page was CANCELLED - the thing it
            #    describes no longer exists - so it is false where it stands and there is nothing to
            #    wait for. It leaves by a route of its own, on the decision that cancelled it rather
            #    than on a successor, because a cancellation replaces nothing and can name nobody
            #    (owner, 2026-08-30); `scripts/vault-archive.sh` holds that precondition, since it
            #    applies to a page on its way OUT and this file reads `wiki/` alone.
            #
            #    WITHOUT THIS LINE THE VALUE WOULD HAVE BEEN AN INVITATION TO SIT STILL. Nothing
            #    else in this file names it, so a page could carry `repealed` in `wiki/` for good
            #    while every check stayed green - which is the exact shape of the window this store
            #    already has open between a repeal being decided and the supersession being
            #    performed, and reproducing it in a new value would be paying for the same defect
            #    twice.
            if (state[f] == "deprecated" || state[f] == "archived" || state[f] == "repealed") print "retired|" f "|" state[f]
            #    `idea` IS COLLECTED HERE AND JUDGED IN RULE 5c, and it is collected rather than
            #    re-read because this pass already has the status of every page. Rule 5c resolves
            #    `decided_by:` and opens the page it names; asking it to open the CITING page as
            #    well would be one more process per page carrying the field - twenty-seven of them
            #    today - to re-read a fact this loop is holding.
            if (state[f] == "idea") print "ideapage|" f "|"
            #    Under its folder, so rule 3 compares within a type. Argued above the awk call.
            if (state[f] == "current" && (f in claim)) print "authority|" f "|" folder "/" claim[f]

            print "tagcount|" f "|" (count[f] + 0)
        }
    }' | sort)

  #    A fourth field, because `governs` carries an address AND a destination and the other
  #    kinds carry one detail. Without it `read` folds the remainder into `detail` delimiters
  #    and all, and the join below would compare a key against a key-and-path.
  while IFS='|' read -r kind page detail extra; do
    [ -z "$kind" ] && continue
    case "$kind" in
      missing)  note "$page: missing frontmatter field '$detail'" ;;
      unknownkey) note "$page: frontmatter key '$detail' is in neither the required nor the optional list of $(basename "$(dirname "$page")")/_schema.yaml - add it there, with a decision behind it, or take it off the page" ;;
      badvalue) note "$page: frontmatter field '${detail%%=*}' carries '${detail#*=}', which $(basename "$(dirname "$page")")/_schema.yaml does not list among its legal values - fix the page, or add the value there with a decision behind it" ;;
      type)     note "$page: type '$detail' disagrees with folder '$(basename "$(dirname "$page")")'" ;;
      decided)  note "$page: a decision with no 'decided:' date" ;;
      nogoverns) note "$page: a rule with no 'governs:' - a rule that names no destination renders nowhere. If it is delivered by lookup rather than by injection, say so: 'render: authority' plus an 'authority:' slug" ;;
      authoritygoverns) note "$page: 'render: authority' beside a 'governs:' - that mode is delivered by a lookup on the slug and injects into no file, so the destination is never read. Drop 'governs:', or change 'render:' to the mode that uses it" ;;
      authoritynoslug) note "$page: 'render: authority' with no 'authority:' - the mode is a lookup and the slug is the key it is looked up by, so this rule can never be found. Add the slug the decision behind this page carries" ;;
      blockgoverns) note "$page: 'governs:' is written as a YAML block list, which neither this check nor scripts/vault-inject.sh reads - write it as 'governs: path' or 'governs: [one, two]'. It is legal YAML and that is why it is refused rather than ignored: a half-parsed spelling renders the text into a subset of its destinations and leaves the rest reading as drift" ;;
      slicenogoverns) note "$page: a '<!-- text -->' slice on a page with no 'governs:' - the injector never opens this page, so the marked text is delivered by nothing and still reads as governed" ;;
      ruleclaim) note "$page: carries 'authority: $detail' beside a 'governs:'; a page that renders answers with 'governs:' alone, or the decision it states and the page stating it read as a duplicate authority" ;;
      governs)  #    The pair, because rule 11 below asks the other direction: given the address
                #    written into a region, where is that page supposed to render? Emitted only
                #    for `current` pages - exactly the predicate the address check wants, free.
                rulegoverns="$rulegoverns$detail|$extra
" ;;
      retired)  #    The value is in the detail field from 2026-08-28, because two marks now oblige
                #    a page to leave and the message that names the wrong one sends a reader to the
                #    wrong repair. `deprecated` is a judgement the librarian made and the move is
                #    owed; `archived` is a mark the sweep writes as it moves, so finding one here
                #    means the move did not complete and the page is not where its own frontmatter
                #    says it is.
                #    `repealed` GETS ITS OWN SENTENCE FROM 2026-08-30, for the reason the other two
                #    are separated: it leaves by a different precondition, so a message naming the
                #    wrong one sends a reader to write a `superseded_by:` that the archiver would
                #    refuse - a cancellation has no successor and is forbidden one.
                if [ "$detail" = "archived" ]; then
                  note "$page: status is archived but the page is still in wiki/; the sweep marks a page as it moves it, so this is a move that did not finish - re-run bash scripts/vault-archive.sh for it, or clear the mark if the page is staying"
                elif [ "$detail" = "repealed" ]; then
                  note "$page: status is repealed but the page is still in wiki/; it moves to $VAULT/archive/, and what it owes on the way out is 'decided_by:' naming the decision that cancelled it - never a 'superseded_by:', because a cancellation replaces nothing"
                else
                  note "$page: status is deprecated but the page is still in wiki/; it moves to $VAULT/archive/"
                fi ;;
      #    NOT A VERDICT, A LIST. `status: idea` is legal in `wiki/proposals/` and red everywhere
      #    else, and the `badvalue` verdict above already says so. This only remembers WHICH pages
      #    carry it, so rule 5c can ask its question without opening them again. Each entry ends
      #    with a newline, which is what lets the membership test below be exact rather than a
      #    substring match: a path can be a prefix of another path.
      ideapage) ideapages="${ideapages:-}$page
" ;;
      unterminated) note "$page: the frontmatter block is never closed by a second ---" ;;
      duptags)  note "$page: two 'tags:' lines; YAML keeps one and the count here is wrong either way" ;;
      tagcount) [ "$detail" -ge 2 ] && [ "$detail" -le 4 ] \
                  || note "$page carries $detail tags; the schema says 2 to 4" ;;
      authority) authorities="$authorities$detail
" ;;
      tag)      tagged="${tagged:-}$page	$detail
" ;;
      source)   case "$detail" in
                  \[\[*)        ;;                 # a wikilink, checked by the link rule below
                  http://*|https://*) ;;           # `basis: external` cites articles and docs
                  *) [ -e "$detail" ] || [ -e "$VAULT/$detail" ] \
                       || note "$page: sources names a path that does not exist: $detail" ;;
                esac ;;
    esac
  done <<< "$facts"
fi

# 3. No two current pages OF ONE TYPE claim the same authority. Collected above as `folder/slug`,
#    from frontmatter only, so the comparison is per folder and a slug shared across two folders is
#    legal. The message prints the pair, which names the offending folder without a second lookup.
dupes=$(printf '%s' "$authorities" | grep -v '^$' | sort | uniq -d)
[ -z "$dupes" ] || note "duplicate authority among current pages of one type: $dupes"

#    THERE USED TO BE A SECOND UNIQUENESS HERE - no two current rules governing one destination -
#    and it was REMOVED on 2026-08-17 by the owner, on the first day it was tested against a real
#    tree. Its argument was that a region carries the text of exactly one rule, so two rules on one
#    destination is a question with two answers and a renderer that has to pick. The premise is
#    true and the conclusion does not follow: the renderer keys on the PAIR of file and slug, and a
#    file carries as many regions as it has rules. Measured before it was touched - the injector
#    rendered four rules into one file, four regions, `0 problem(s)`.
#
#    It was also stricter than the text it guarded. The schema says a rule names the one
#    destination ITS text is injected into, and says nothing about a destination taking one rule,
#    which is the shape of a failure already on the record: a hook stricter than its own rule.
#
#    What it appeared to protect is protected without it, and by verdicts that read the tree rather
#    than the frontmatter: rule 11 reddens one slug marking two regions in one file, and the fifth
#    verdict reddens a region sitting in a file its rule does not govern. Nothing here needs the
#    bare path to be unique, and requiring it blocked the migration of the four rules that share
#    `CLAUDE.md` - which is the whole first use of the mechanism.

# 4 and 5. Links resolve, and no page is an orphan.
#    These are two questions about one set - which page names are linked from the curated part
#    of the vault - so the set is built once. Asked per page it meant one recursive grep over
#    the whole vault for every page in it: 71 seconds at 75 pages, and growing as the square.
#
#    The set is built from `wiki/`, `archive/` and the three registers, and deliberately NOT
#    from `raw/` or `brief.md`. `raw/` is immutable: a session that names a page the librarian
#    then decides not to write would leave a broken link that can only be cleared by writing a
#    page nobody wanted or by editing a file the schema forbids editing. And a page reachable
#    only from a derived file is not reachable: the brief is regenerated from the vault, so
#    letting it count would mean the vault vouching for itself.
#
#    Fenced code blocks are stripped, and so are inline code spans: the schema documents the
#    link syntax with placeholder targets, and counting those would make the check fail on its
#    own examples - `supersedes: [[old-page]]` in prose is an illustration, not a link. This
#    project has been bitten by the reverse once already, when prose inside a <script> block
#    satisfied an id search for a slice and a half. Strip both sides, always. The strip is also
#    what makes the orphan half honest: a page named only inside a code fence is not reachable
#    by a reader, and Obsidian does not render it as a link either.
#
#    `[[page|alias]]` and `[[page#heading]]` are Obsidian's own spellings and resolve to
#    `page`. Read whole they produced two violations from one legitimate edit: a broken link,
#    and an orphan that was not one.
#    The registers go through the SAME fence-stripping pass as the pages. They used to be
#    appended after it with `cat`, and that single word was a hole in both directions: a
#    fenced example link in `index.md` was read as a real link and reported broken, and a
#    page whose only inbound link sat in a fenced block in a register was not an orphan when
#    it was one.
#    AND THE EXEMPTION FOLLOWS THE FILE RATHER THAN THE DIRECTORY (2026-08-23). Archiving a
#    journal does not make it mutable, so the paragraph above about `raw/` keeps applying to it
#    after the move - and until this date it stopped applying at exactly that moment, because the
#    sweep reads `archive/` whole. It fired on the first journal that was ever archived while
#    carrying the owner`s own Russian: he asked for a script that reads every wikilink in a record
#    and wrote the brackets to show what he meant, so the move turned an illustration into a
#    broken link to a page called `викиссылки`, and the repair the old rule allowed was to write
#    that page or to edit an immutable file. `vault-archive.sh` reversed its own move and the
#    ingest could not finish its last step.
#
#    So the four RAW kinds are excluded here, by the directory the archive script itself puts them
#    in: `handoffs`, `plans`, `specs`, `notes`. The fifth kind, `pages`, is NOT excluded - a
#    retired wiki page is curated text whose links were always swept and stay swept, and the
#    thirty flat pages at the archive root are reached the same way. None of the four names
#    collides with a `wiki/` folder, so one find still covers both trees.
#
#    They stay in `resolvable` below, which is a different question: what may be POINTED AT is
#    not what must POINT correctly.
linked=$({ find "$VAULT/wiki" "$VAULT/archive" -name '*.md' \
                -not -path '*/handoffs/*' -not -path '*/plans/*' \
                -not -path '*/specs/*'    -not -path '*/notes/*' -print0 2>/dev/null
           for r in index.md tags.md sprint.md; do
             [ -f "$VAULT/$r" ] && printf '%s\0' "$VAULT/$r"
           done; } \
         | xargs -0 --no-run-if-empty \
             awk 'FNR == 1 { inblock = 0 } { sub(/\r$/, "") }
                  /^```/ { inblock = !inblock; next } !inblock' \
         | sed 's/`[^`]*`//g' \
         | grep -o '\[\[[^]]*\]\]' \
         | sed 's/^\[\[//; s/\]\]$//; s/[|#].*$//' \
         | sed 's/[[:space:]]*$//' | sort -u)

#    A link must resolve to a NON-EMPTY page inside wiki/ or archive/. The looser rule -
#    "some file of that name exists anywhere under the vault" - was satisfied on 2026-08-13
#    by a 0-byte file that had appeared at the vault root during a rename. The link check
#    reported green while the reader following the link arrived at nothing, and the file sat
#    outside wiki/ so every other check skipped it too. That is this project's sixth
#    encounter with a check passing for the wrong reason, and it was introduced by the very
#    commit whose message was about that failure. Resolve narrowly, or do not resolve.
resolvable=$(find "$VAULT/wiki" "$VAULT/archive" -name '*.md' -size +0 2>/dev/null \
             | sed 's|.*/||; s|\.md$||' | sort -u)

while IFS= read -r link; do
  [ -z "$link" ] || note "broken wikilink: [[${link}]]"
done < <(comm -23 <(printf '%s\n' "$linked") <(printf '%s\n' "$resolvable"))

#    An orphan is a page nothing links to: reachable only by an exact grep hit, which is the
#    one retrieval path we know fails across languages. This rule exists because the count
#    regressed from 7 to 11 in the very wave that was fixing it - splitting one page into six
#    turned one orphan into five, and nothing was watching.
if [ -n "$pages" ]; then
  while IFS= read -r name; do
    [ -z "$name" ] && continue
    page=$(printf '%s\n' "$pages" | grep -m1 "/${name}\.md$")
    note "orphan page, nothing links to it: ${page:-$name}"
  done < <(comm -23 <(printf '%s\n' "$pages" | sed 's|.*/||; s|\.md$||' | sort -u) \
                    <(printf '%s\n' "$linked"))
fi

# 5c. `decided_by:` NAMES A DECISION, AND ONLY A DECISION. The field arrived 2026-08-23 and was
#     narrowed to `wiki/proposals/` and `wiki/rules/` on 2026-08-23. The schemas make it legal in
#     those two folders and illegal in the other four, and that is the check about the KEY - the
#     `unknownkey` verdict above already carries it. THIS is the check about the TARGET.
#
#     IT IS THE ONLY HALF THE TREE DOES NOT ALREADY ANSWER, measured rather than assumed. In a
#     scratch tree on 2026-08-23: `decided_by: [[no-such-decision-page-anywhere]]` printed
#     `broken wikilink` and exited 1, because a `[[wikilink]]` in frontmatter is swept exactly
#     like one in the body; `decided_by: [[vault-scripts]]` - a page that exists and is an
#     `entity` - printed nothing at all and the gate exited 0. That silence is this verdict.
#
#     SO NO SECOND EXISTENCE CHECK IS WRITTEN HERE, deliberately. It would be a second reader of
#     a fact rule 5 already reads, and two derivations of one rule are two answers waiting to
#     differ - the argument the folder set already lost once.
#
#     The target may live in `archive/`: a rule whose decision was retired still has one, and two
#     of the fifteen rule pages reach their decision only that way. What is forbidden is naming
#     something that is not a decision at all, in either tree.
if [ -n "${VAULT:-}" ]; then
  decidedby_pages=$(find "$VAULT/wiki" "$VAULT/archive" -name '*.md' -size +0 2>/dev/null)
  while IFS= read -r hit; do
    [ -n "$hit" ] || continue
    dbsrc=${hit%%:*}
    dbslug=$(printf '%s\n' "${hit#*:}" \
             | sed 's/.*\[\[//; s/\]\].*//; s/[|#].*$//; s/^[[:space:]]*//; s/[[:space:]]*$//')
    [ -n "$dbslug" ] || continue
    dbtarget=$(printf '%s\n' "$decidedby_pages" | grep -m1 -- "/${dbslug}\.md\$")
    [ -n "$dbtarget" ] || continue
    #    TWO FIELDS OFF THE TARGET IN ONE PASS. `type:` is what this rule has always asked for;
    #    `binding:` is what the pair below needs, and it is read here because the page is already
    #    open. A second awk would be a second process per page carrying `decided_by:`.
    dbfields=$(awk -F': *' '
      /^type:/    && dt == "" { dt = $2 }
      /^binding:/ && db == "" { db = $2 }
      END { printf "%s\t%s\n", dt, db }
    ' "$dbtarget")
    dbkind=${dbfields%%$'\t'*}
    dbbinding=${dbfields#*$'\t'}
    [ "$dbkind" = "decision" ] || \
      note "$dbsrc: decided_by names [[${dbslug}]], whose type is '${dbkind:-none}' - the field names the DECISION that caused this page, and only a decisions/ page can be one"

    #    THE `idea` / `decided_by:` PAIR, NARROWED - owner, 2026-08-24.
    #
    #    A page carrying `status: idea` while naming the decision that caused it is a contradiction
    #    in the ordinary case: an idea is a half-thought nobody ruled on, and a proposal a decision
    #    produced is past that stage.
    #
    #    EXCEPT WHERE THE CAUSE IS A `deferral`, AND THAT EXEMPTION IS THE WHOLE RULING. Deferring
    #    something is a decision here and keeps its page in `decisions/`; the corpus holds
    #    twenty-four of them, and a deferral with a proposal behind it is the ORDINARY shape rather
    #    than the corner. Without the exemption a half-thought that was deferred could not be an
    #    idea at all - which is the objection `wiki/proposals/_schema.yaml` has carried in the
    #    session's own words since the value was minted, and this is the answer to it.
    #
    #    IT FIRES ON NOTHING TODAY AND THAT IS EXPECTED. The back-fill method sets `status: idea`
    #    only where no decision exists, so an idea page carries no `decided_by:` and the two halves
    #    cannot meet. This is a guard against a future page, not a sweep of the present one; the
    #    selftest is where it is observed firing.
    #
    #    WHICH WAY THE IMPLICATION RUNS was never settled and did not need to be: both readings
    #    select the same pages - the intersection - and differ only in which field the message
    #    blames. A third reading, that a proposal which is NOT an idea must carry the field, is
    #    forbidden by [[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]], which
    #    rejected making it required in this folder.
    case "$NL${ideapages:-}" in
      *"$NL$dbsrc$NL"*)
        [ "$dbbinding" = "deferral" ] || \
          note "$dbsrc: carries 'status: idea' and names [[${dbslug}]] as its cause, whose binding is '${dbbinding:-none}' - an idea is a half-thought nobody ruled on, so either this is not an idea or that decision did not cause it. A 'deferral' cause is exempt and this one is not"
        ;;
    esac
  done < <(grep -rn --include='*.md' '^decided_by:' "$VAULT/wiki" 2>/dev/null)
fi

# 5b. The repository's own CLAUDE.md points into the vault, and nothing else checks those
#     pointers. It is the file every session reads first: a rule there that names a page which
#     does not exist sends the reader after nothing, which is worse than not pointing at all -
#     and the page it meant may have been renamed by an ingest that never looked outside the
#     vault. Fenced blocks and inline code are stripped for the same reason as above.
#
#     These links deliberately do NOT count towards reachability: an orphan is a page the vault
#     itself cannot reach by walking, and CLAUDE.md is not part of the walk.
if [ -f CLAUDE.md ]; then
  while IFS= read -r link; do
    [ -z "$link" ] || note "CLAUDE.md names a page that does not exist: [[${link}]]"
  done < <(comm -23 \
             <(awk 'FNR == 1 { inblock = 0 } /^```/ { inblock = !inblock; next } !inblock' CLAUDE.md \
               | sed 's/`[^`]*`//g' \
               | grep -o '\[\[[^]]*\]\]' \
               | sed 's/^\[\[//; s/\]\]$//; s/[|#].*$//' | sed 's/[[:space:]]*$//' | sort -u) \
             <(printf '%s\n' "$resolvable"))
fi

# 6. Tags. The dictionary and the corpus must describe each other: a tag used on a page but
#    absent from the dictionary has no definition, so the next librarian guesses at its
#    meaning. The tags themselves were collected in the frontmatter pass above, in both of
#    YAML's spellings; the 2-to-4 rule was applied there too, which is why a page with no
#    tags at all is now loud rather than silent.
registered=$(grep -o '^- tag: .*' "$VAULT/tags.md" 2>/dev/null | sed 's/^- tag: //' | sort -u)
used=$(printf '%s' "${tagged:-}" | cut -f2 | grep -v '^$' | sort -u)

while IFS= read -r t; do
  [ -z "$t" ] || note "tag '$t' is used on a page but is not in $VAULT/tags.md"
done < <(comm -23 <(printf '%s\n' "$used") <(printf '%s\n' "$registered"))

# 7. Advisories. These print and do NOT fail, and the difference is deliberate: both are
#    conditions the vault grows into rather than breaks into, and neither has a fix that is
#    correct to apply on the spot - splitting a tag means re-tagging pages this session never
#    touched, which is a /lint job and the owner's call. An alarm that fires on every run and
#    cannot be acted on is one you learn not to read; `tags.md` itself calls the split
#    threshold a /lint flag rather than a rule.
while IFS= read -r t; do
  [ -z "$t" ] || echo "VAULT-CHECK: advisory: tag '$t' is registered but used on no page"
done < <(comm -13 <(printf '%s\n' "$used") <(printf '%s\n' "$registered"))

#    The split advisory is measured **inside a folder**, and the number is ten.
#
#    Neither half is arbitrary. **Ten is the ceiling already written into the librarian**:
#    "if you find yourself opening more than about ten pages for one question, stop and say
#    what you could not narrow down". It is a property of the reader and it does not grow
#    with the corpus, which is what a threshold has to be here - an earlier alarm in this
#    project named a size outright and that number was made up, so thresholds are calibrated
#    against something measured rather than chosen (`the-growth-signal-is-the-brief`).
#
#    **Per folder, because folders grow at different rates for different reasons.** Decisions
#    grow monotonically and are never pruned; lessons grow only when something burns us. A
#    count over the whole corpus therefore tracks the project's age rather than the tag's
#    power to classify, and would have to be raised every time the project stayed alive.
#    Measured per folder against a fixed reading limit it tracks neither. Two things fall out
#    for free: the floor - a folder of ten pages or fewer can never produce a slice over ten -
#    and the fact that a tag can be healthy in one folder and useless in another, which one
#    corpus-wide number cannot say. `archive/` is not measured: nothing is answered from it.
if [ "$LINT" = 1 ]; then
printf '%s' "${tagged:-}" | awk -F'	' '
    NF == 2 && $2 != "" {
        if (match($1, /wiki\/[^\/]+\//)) {
            folder = substr($1, RSTART + 5, RLENGTH - 6)
            dense[folder "	" $2]++
        }
    }
    END {
        for (k in dense) if (dense[k] > 10) {
            split(k, part, "	")
            print "VAULT-CHECK: advisory: tag " part[2] " selects " dense[k]                   " pages in " part[1] "/ - more than the ten a reader opens for one"                   " question; a split candidate for /lint at the retrospective, not an"                   " action for this run"
        }
    }' | sort
fi

# 8. A journal keeps every section of the template it was written from. An empty section is a
#    legal answer - the word "none" - but a dropped one is knowledge that was never asked for,
#    and `Feedback to the librarian` in particular is the only channel through which a miss
#    against the librarian is ever reported. Nothing else in this repository looks inside raw/
#    at all: a journal short of a section would pass every other check here and lose a category
#    in silence.
#
#    THE SET IS READ FROM THE TEMPLATE, never copied here. That is the same shape as
#    `catalogue.md`: regenerate and compare, rather than compare against a list somebody wrote
#    down. The numbers this rule used to count are gone - the cut is by heading text now, because
#    a number moved every time a section was inserted and a name does not move. What that costs
#    is stated plainly: a RENAMED heading is indistinguishable from a dropped one plus a new one,
#    and this rule reports it as exactly that, which is the loudest it can be.
#
#    A JOURNAL IS JUDGED ONLY WHILE IT IS UNCOMPILED - it has no `.coverage.tsv` sidecar beside
#    it. The rule exists to protect the ingest that is about to read the journal, so it applies
#    to what that ingest has not yet read. Afterwards the form is history: `raw/` is immutable,
#    the journal can never be corrected, and a rule that fails forever on a file nobody may edit
#    is an alarm you learn not to read. This is also what lets the template change at all - the
#    journals written to the older, numbered form stop being judged the moment they are compiled,
#    and nothing has to be moved or rewritten to make the new form legal.
#
#    The hole this leaves, named rather than hidden: a journal written malformed and compiled
#    before anyone runs this check is never judged. `/handoff` closes it by running the gate as
#    its last step, before `/ingest` - the one moment the journal is still being written rather
#    than standing as testimony.
HANDOFF_TEMPLATE=".claude/templates/handoff.md"
#    THE LEVEL IS AN ARGUMENT FROM 2026-08-30, and the default keeps rule 8 exactly as it was. Rule
#    16 below judges `wiki/` pages, which write their sections as `# ` - 900 first-level headings
#    against 395 second-level ones in `decisions/` alone - while a journal writes `## ` because that
#    is what the template writes. A second helper reading the other level is two readers of one
#    question, which is the shape this file has lost cases to; a parameter is one reader.
sections() {          # sections <file> [level, default '##'] - headings outside fences, sorted
  awk -v pfx="${2:-##} " '
      FNR == 1 { inb = 0 }
      { sub(/\r$/, "") }
      /^```/   { inb = !inb; next }
      !inb && index($0, pfx) == 1 {
          #    `index` and not a regex: the level is data here, and a `#` glued into a pattern
          #    would make `# ` match `## ` as a prefix. Anchored at 1 and including the trailing
          #    space, `# ` matches a first-level heading and never a second.
          s = substr($0, length(pfx) + 1)
          sub(/^[ \t]+/, "", s); sub(/[ \t]+$/, "", s)
          if (s != "") print s
      }' "$1" | sort -u
}
if [ ! -f "$HANDOFF_TEMPLATE" ]; then
  note "missing file: $HANDOFF_TEMPLATE - rule 8 reads the section set from it and cannot run"
else
  want=$(sections "$HANDOFF_TEMPLATE")
  [ -n "$want" ] || note "$HANDOFF_TEMPLATE carries no '## ' headings - rule 8 would pass everything"
  for src in "$VAULT"/raw/handoffs/*.md; do
    [ -f "$src" ] || continue
    #    A journal carries a DATE in `session:`; a form carries the placeholder. The rule used to
    #    skip the template by filename, which is an exception that outlives what it excepted - the
    #    template has left `raw/` and a name-based skip would go on protecting a file that is not
    #    there. A property cannot go stale that way.
    grep -qE '^session:[[:space:]]*[0-9]{4}-[0-9]{2}-[0-9]{2}' "$src" || continue
    [ -f "${src%.md}.coverage.tsv" ] && continue
    have=$(sections "$src")
    [ "$have" = "$want" ] && continue
    missing=$(comm -23 <(printf '%s\n' "$want") <(printf '%s\n' "$have") | tr '\n' ';' | sed 's/;$//')
    extra=$(comm -13 <(printf '%s\n' "$want") <(printf '%s\n' "$have") | tr '\n' ';' | sed 's/;$//')
    #    Only the half that has content is printed. It used to print `unexpected [none]` when
    #    there was nothing unexpected, and "none" is the exact word this template tells a writer
    #    to put in an empty section - so the message read as though a section called "none" had
    #    appeared. A placeholder that collides with real data is a message that has to be decoded.
    detail=""
    [ -n "$missing" ] && detail="missing [$missing]"
    [ -n "$extra" ] && detail="${detail:+$detail, }unexpected [$extra]"
    note "$src: its sections do not match $HANDOFF_TEMPLATE - $detail; write \"none\", never drop one"
  done
fi

# 9. RETIRED 2026-08-17, and its number is not reused.
#
#    It asked whether `catalogue.md` still matched what `vault-catalogue.sh` produces. That file
#    is gone: the list of every page is `pages.base`, an Obsidian base, which is a query rather
#    than an answer and therefore cannot be stale. Nothing to regenerate, nothing to diff, and
#    the trap this rule carried a warning about - a generated file that links to every page must
#    never join the link register, or the orphan rule runs, passes and proves nothing - cannot
#    arise, because a base holds no wikilinks.
#
#    The number stays empty on purpose. Pages in the vault cite these rules BY NUMBER, and
#    reusing a retired one would repoint every one of those citations without touching a word of
#    them. That is the failure this whole harness exists to make impossible, so it is not going
#    to be introduced by tidying a sequence.
#
#    What was lost, named rather than hidden: an agent could read one file and see the whole
#    corpus, and now cannot. `bash scripts/vault-catalogue.sh` still prints exactly that list on
#    demand - the script survived the file.

# 10. A title carries no measurable quantity, and neither does the filename. The rule is
#     unconditional in both halves and was written on 2026-08-16; the page that states it was
#     followed the next day by one titled "...the five per-folder advisories stand" while the
#     check printed seven - written by the librarian, a day after the librarian wrote the rule.
#     Prose does not stop an agent, which is the whole argument for this rule being here
#     instead of only there.
#
#     THIS RULE ONCE ASKED AND NOW JUDGES, and the change is the important part. No lexical
#     predicate separates the two shapes: "Two staleness checks, at two different times" is a
#     violation, because there were three and the third arrived without touching the page,
#     while "...are two different properties" reads as a page a third would make wrong rather
#     than stale. The titles are grammatically identical, and what separates them - whether the
#     counted set belongs to the page or to the world outside it - no script can read.
#
#     So the page used to answer, once, in a `quantity:` field. THE FIELD IS WITHDRAWN (owner,
#     2026-08-18) and the corpus was cleared of it on 2026-08-19: twenty-four pages carried it,
#     twenty-seven titles were repaired, and the sixteen addresses underneath them were renamed
#     in one sweep. A number that genuinely cannot drift - a status code, a rule's address, the
#     reading of one past day - now leaves the title like any other.
#
#     WHY THE HATCH WENT, IN ONE FACT: two of those twenty-four declarations were false while
#     they stood. One page declared that a third property would make it wrong rather than
#     stale, and a third had already been added to that same page. Another declared its count
#     enumerated in its own title, over a body naming a fourth member. Neither was caught by
#     anything mechanical, and neither could be: a declaration silences the one instrument that
#     would have noticed it drifting. That is the argument against ever minting a field of this
#     shape again, and it is stronger than the tidiness argument made at the time.
#
#     AND A WORD IN THE LIST BELOW IS NOW A PROMISE. While a page could declare itself, a word
#     only had to be usually a count - a false positive cost one line of frontmatter. With no
#     appeal, a false positive is paid for by rewriting correct prose, so a word is added only
#     when it is always a count. The known exception is deliberate: `second` is in the list and
#     three of three uses in this corpus mean *another* rather than the second of n ("not a
#     second unattended writer", "needs a second instrument"). The owner was shown that
#     measurement on 2026-08-18 and ruled it in, preferring a predicate with no exemptions to
#     remember over one that is right more often. The first author who loses a correct title to
#     it is answered here rather than surprised.
#
#     A title is corrected IN PLACE and that is not supersession (owner, 2026-08-17): in this
#     vault the filename is the identity - it is the search surface and it is what every
#     wikilink resolves to - so removing a number from a title moves no address and strands
#     nothing. Superseding on a title change would mean a page is identified by its title,
#     which is not how anything here addresses a page.
#
#     Exempt, each because it is not a count:
#       - anything inside a code span, which is how this corpus writes identifiers - though
#         never a rule number, which it writes in prose: measured 2026-08-18, `rule 11` and
#         `rule 12` appear 28 and 47 times unspanned against one code-spanned rule citation in
#         the whole wiki, so backticks around one would be typography invented to make this awk
#         skip the string;
#       - an ISO date, which is a fixed boundary and cannot drift;
#       - a digit glued to a letter - cp1252 is a name, not twelve hundred and fifty-two;
#       - the words "one" and "first", both measured rather than assumed. Every one of the 14
#         titles using "one" used it as a pronoun ("a known one") or an invariant ("exactly one
#         finaliser"); every one of the 13 pages using "first" used it as a position or a
#         pronoun ("the first hit", "the first narrowing", "migrates first"). They are the same
#         number in two words and they are treated the same way.
#
#     AND THE FILENAME IS READ WITH THE SAME PREDICATE (owner, 2026-08-17; built 2026-08-18).
#     A title is corrected in place and the slug underneath it is left as it was, so the corpus
#     accumulated names whose own titles had already been repaired - one of them for six days.
#     The sweep of 2026-08-19 cleared all sixteen and the advisory has printed nothing since.
#
#     IT IS AN ADVISORY WHERE THE TITLE HALF IS RED, and the asymmetry is the design (owner,
#     2026-08-18). Repairing a title costs nothing. A filename is the address - it is what every
#     wikilink resolves to - so repairing one moves every inbound link, both registers, and
#     `log.md`, which rules 4 and 5 do not even read. That is a scheduled sweep, not something a
#     session does because a check went red. Reddening on a repair that is unavailable would
#     make this file exit 1 on every run until the sweep lands, and a gate that is always red is
#     not a gate. What the owner asked for - "a twelfth is never minted silently" - a printed
#     line delivers in full: a NEW page with a counting name is renamed in the minute it is
#     written, before anything cites it, and this is what tells its author to do that.
#
#     Measured on the sweep of 2026-08-19, so the next one is priced from a reading rather than
#     from a fear: sixteen renames moved 148 inbound wikilinks inside the set rules 4 and 5
#     read, and 14 more in `log.md`, which is outside it and was swept by hand. The whole of it
#     was `git mv`, one `sed -f` and a verification pass. The rewriter-and-detector pair the
#     renames were said to be blocked on was never built and was never needed.
#
#     AND `sed` CANNOT TELL AN ADDRESS FROM A QUOTATION. That sweep rewrote two slugs that pages
#     were quoting as examples of counting names, and one of those sentences came to say the
#     opposite of what it was written to say. Nothing in a slug distinguishes the two uses, so
#     the next sweep reads its own diff for code spans rather than trusting the substitution.
#
#     The exemptions carry over unchanged instead of being re-tuned for slugs, because the
#     decision said the same predicate over a different string and a second, subtly different
#     predicate is two rules. Two are inert on a slug - it has no code span, and the naming rule
#     keeps dates out - and one diverges: `cp1252` stays glued and stays exempt, while `htmx-2`
#     is split by its hyphen and counts as a digit. No filename hits that today; it is written
#     down so the first one that does is answered rather than argued about.
fn_advisory=""
fn_count=0
while IFS=$'\t' read -r kind page hit; do
  [ -z "$page" ] && continue
  if [ "$kind" = "title" ]; then
    note "$page: the title counts ($hit) - retitle it, naming what is counted instead of counting it"
  else
    fn_slug=${page##*/}; fn_slug=${fn_slug%.md}
    # One name per line rather than the single comma-run the two advisories above use. Owner's
    # choice, 2026-08-18: six names on one line is a paragraph nobody reads to the end, and this
    # list shrinks one name at a time as the renames land.
    #
    # EVERY LINE CARRIES THE `VAULT-CHECK:` PREFIX AND NONE OF THE CONTINUATIONS CARRIES
    # `advisory:` - both halves are the owner's, on the same day, and both are load-bearing. The
    # prefix keeps the output greppable line by line, which is what a line-oriented tool owes a
    # caller. Withholding the second word keeps `grep -c 'advisory:'` counting advisories rather
    # than names - the brief reports that number, and six continuation lines would have turned
    # twenty into twenty-five overnight with nothing having changed.
    fn_advisory="$fn_advisory
VAULT-CHECK:   $fn_slug ($hit)"
    fn_count=$((fn_count + 1))
  fi
done < <(printf '%s\n' "$pages" | tr '\n' '\0' | xargs -0 --no-run-if-empty awk '
    function counts(s,   t, low, w, n, i, hit) {
        t = s
        gsub(/`[^`]*`/, " ", t)
        gsub(/[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]/, " ", t)
        gsub(/[A-Za-z][A-Za-z0-9]*[0-9][A-Za-z0-9]*/, " ", t)
        hit = ""
        if (t ~ /[0-9]/) {
            hit = "a digit"
        } else {
            low = " " tolower(t) " "
            gsub(/[^a-z]+/, " ", low)
            n = split("two three four five six seven eight nine ten eleven twelve thirteen " \
                      "fourteen fifteen sixteen seventeen eighteen nineteen twenty dozen " \
                      "both twice thrice " \
                      "second third fourth fifth sixth seventh eighth ninth tenth " \
                      "eleventh twelfth thirteenth fourteenth fifteenth sixteenth " \
                      "seventeenth eighteenth nineteenth twentieth", w, " ")
            for (i = 1; i <= n; i++) if (index(low, " " w[i] " ")) { hit = w[i]; break }
        }
        return hit
    }
    function verdict(   slug, hit) {
        hit = counts(title)
        if (hit != "") print "title\t" FILENAME "\t" hit
        slug = FILENAME
        sub(/^.*\//, "", slug)
        sub(/\.md$/, "", slug)
        hit = counts(slug)
        if (hit != "") print "file\t" FILENAME "\t" hit
    }
    FNR == 1 { opened = 0; inb = 0; done = 0; title = "" }
    done { next }
    { sub(/\r$/, "") }
    /^---[ \t]*$/ {
        if (!opened) { opened = 1; inb = 1; next }
        if (inb)     { inb = 0; done = 1; verdict(); next }
    }
    inb && /^title:[ \t]*/     { title = $0; sub(/^title:[ \t]*/, "", title); gsub(/^"|"$/, "", title) }
')
[ "$fn_count" -eq 0 ] || printf 'VAULT-CHECK: advisory: %d filename(s) count - each waits for a rename, which moves an address and is a scheduled sweep, not something a session repairs:%s\n' "$fn_count" "$fn_advisory"

# 11. Marked regions in the harness's own markdown, and the rules behind them.
#
#     A region is a paired HTML comment named for a rule's slug, alone on its line at column
#     zero: `<!-- rule: some-slug -->` ... `<!-- /rule: some-slug -->`. The file owns the
#     skeleton and the wiki owns the text, so a rule can be corrected in one place and rendered
#     into every file that carries it. Seven harness divergences are on the record and not one
#     of them was caught by anything mechanical; the handoff mapping had been copied into six
#     files and was found only because they happened to share the distinctive string
#     `section 7`. A renamed heading would not have been findable that way.
#
#     THE GOVERNED SET IS SWEPT, NEVER LISTED. Two lists of the same set drift, and this project
#     has already lost two selftest cases to exactly that. The sweep is both `CLAUDE.md` files
#     and every markdown file under `.claude/` - so a skill added tomorrow is governed the day
#     it exists rather than the day somebody remembers this line.
#
#     AND THE SWEEP IS MARKDOWN, which is a property rather than a list of exceptions. The
#     marker is an HTML comment: `.claude/settings.json` cannot carry one because JSON has no
#     comment syntax at all, and `.claude/hooks/*.ps1` cannot because `<!--` is a syntax error
#     there. They are not exempt files - they are files in which a region cannot exist, and
#     they are governed whole or not at all. That mechanism is designed and not built, and
#     saying so here is cheaper than a list of names that will outlive its reason.
#
#     A FILE WITH NO REGION IS AN ADVISORY, NOT A FAILURE (owner, 2026-08-17). Markup is
#     gradual and starts at zero, so a rule that reddened on absence would be born failing on
#     every governed file and would have to carry an exemption list written before a single
#     region existed - guessed at, in other words. What is red is markup that is broken, which
#     is checkable today: a region opened and never closed, a close with no open, a close with
#     the wrong slug, nesting, one rule marking two regions in one file, a marker that is not
#     alone on its line, and a region naming a rule page that does not exist. Absence is
#     reported as a number that shrinks as markup proceeds - the same move that made the
#     ingest's completeness mechanical rather than a claim.
#
#     Markers are detected LOOSELY and judged STRICTLY. A pattern that only matched the exact
#     form would make a typo invisible rather than wrong, which is this project's most-recorded
#     failure: six checks have reported green while examining nothing. Anything that looks like
#     a rule marker is picked up, and anything that is not exactly the form is named as
#     malformed.
#
#     Fenced blocks and inline code spans are stripped first, and both halves matter here: the
#     skills and this file document the marker form in prose, and a documented example counted
#     as a marker would report the harness broken for describing itself. This is the fourth
#     rule in this file to need that pass and the third time it was nearly forgotten.
#
#     AND A REGION IS CHECKED AGAINST THE `governs:` OF THE RULE IT NAMES (added 2026-08-17).
#     The verdicts above prove the markup is well formed and that a page stands behind the slug;
#     rule 12 proves the region the injector wrote carries what that page says. Neither asks
#     whether the region is in the file the rule governs, and the injector cannot be asked: it
#     walks rule pages and opens only the one destination each `governs:` names, so a region
#     anywhere else sits in a file it never holds. The comparison belongs here because it is
#     about a region ADDRESS, which only a sweep can see, and not about its content, which is
#     the writer's to own.
#
#     WHAT IT CATCHES IS THE LEFTOVER, which is narrower than the hole first reads. A rule that
#     governs A while its region sits only in B is red today already - the injector reports that
#     A carries no region for it. The case that survives every other verdict is the region
#     present in A *and also* in B: rule 11 passes, because its duplicate check is keyed per
#     file, and rule 12 passes, because B is never opened. B then keeps whatever it was handed
#     on the day it was copied, for good, while reading as governed text. The first rule
#     migration is exactly when that happens - copying a marker pair into the wrong SKILL.md is
#     one keystroke - which is why this went in before it.
#
#     Only a `current` rule answers here. A region naming a deprecated one is left alone on
#     purpose: a deprecated rule does not render, and widening the join to archived pages would
#     re-open a question closed on 2026-08-17. A rule with no `governs:` at all is already
#     reported by the frontmatter pass, so it stays silent here rather than saying it twice.
harness=$({ [ -f CLAUDE.md ] && printf '%s\n' "CLAUDE.md"
            [ -f "$VAULT/CLAUDE.md" ] && printf '%s\n' "$VAULT/CLAUDE.md"
            find .claude -name '*.md' 2>/dev/null; } | sort -u)

if [ -n "$harness" ]; then
  marked=0; governed_files=0; unmarked=""
  while IFS='|' read -r kind file detail line; do
    [ -z "$kind" ] && continue
    case "$kind" in
      slug)      #    `detail` is the address the marker spells: its type word resolved to a
                 #    folder, then the slug. The scanner has already refused any type word whose
                 #    folder does not exist, so this only ever names a real category.
                 want_slug=${detail#*/}
                 if [ ! -f "$VAULT/wiki/$detail.md" ]; then
                   #    WHERE THE SLUG EXISTS UNDER ANOTHER TYPE, SAY WHICH (2026-08-18). The
                   #    bare "no page behind it" is true and costs the reader a search to act
                   #    on, and this is the likeliest way to misspell an address now that the
                   #    type is part of it. The verdict is the same red; only the diagnosis
                   #    improves. It replaces a proposed verdict for "the marker's type
                   #    disagrees with the page's `type:`", which cannot fire: the type word
                   #    picks the folder and rule 2 above requires every page in a folder to
                   #    carry its singular, so a disagreement is rule 2 failing, not this.
                   elsewhere=$(find "$VAULT/wiki" -mindepth 2 -maxdepth 2 -name "$want_slug.md" 2>/dev/null \
                               | sed 's|/[^/]*$||; s|.*/||' | sort -u | tr '\n' ' ')
                   elsewhere=${elsewhere% }
                   if [ -n "$elsewhere" ]; then
                     note "$file:$line: the region resolves to $VAULT/wiki/$detail.md, which does not exist - '$want_slug' is in $elsewhere, so the marker names the wrong type"
                   else
                     note "$file:$line: the region resolves to $VAULT/wiki/$detail.md, which does not exist - a region with no page behind it renders nothing"
                   fi
                 else
                   #    A leading ./ is stripped from both sides. The sweep never writes one and
                   #    `governs:` may, and how a path is spelled is not the question this asks.
                   #    Empty means the page is deprecated or carries no governs: at all - both
                   #    are somebody else's verdict, and this one stays quiet.
                   #    EVERY destination, not the first (2026-08-21). `governs:` names a list
                   #    and the rule emits one fact per address, so the question this asks is
                   #    membership rather than equality. Reading the first row was correct while
                   #    a page could name one file and silently wrong the moment it could name
                   #    two: it accused the region in the OTHER governed file, which is the one
                   #    place the verdict must stay quiet.
                   wants=$(printf '%s' "$rulegoverns" | awk -F'[|]' -v s="$detail" '$1 == s { d = $2; sub(/^\.\//, "", d); printf "%s|", d }')
                   here=${file#./}
                   if [ -n "$wants" ]; then
                     case "|$wants" in
                       *"|$here|"*) ;;
                       *) note "$file:$line: the region names $detail, which governs $(printf '%s' "${wants%|}" | sed 's/|/, /g') - the injector writes there and never here, so this region drifts and nothing can correct it" ;;
                     esac
                   fi
                 fi ;;
      unclosed)  note "$file:$line: the region '$detail' is opened and never closed" ;;
      unopened)  note "$file:$line: closes a region '$detail' that was never opened" ;;
      mismatch)  note "$file:$line: a region is closed with the wrong address ($detail)" ;;
      nested)    note "$file:$line: region '$detail' opens inside another; regions do not nest or overlap" ;;
      dupslug)   note "$file:$line: '$detail' marks two regions in one file" ;;
      malformed) note "$file:$line: not a marker alone on its line at column zero, or its type word is not a category this vault has: $detail" ;;
      fence)     note "$file:$line: a code fence is opened and never closed ($detail); every marker below it is invisible to this rule" ;;
                 #    A region OR whole generation, per criterion 6 as the owner reworded it on
                 #    2026-08-20. The generated flag rides the FOURTH field of the same fact, which
                 #    this loop names `line` because every other kind puts a line number there.
      regions)   governed_files=$((governed_files + 1))
                 if [ "$detail" -gt 0 ] || [ "$line" = "1" ]; then marked=$((marked + 1))
                 else unmarked="${unmarked:+$unmarked, }$file"; fi ;;
    esac
  done <<< "$(printf '%s\n' "$harness" | tr '\n' '\0' | xargs -0 --no-run-if-empty awk -v typemap="$typemap" '
    #    THE NET WIDENS FROM `rule` TO ANY WORD, AND THE JUDGE DOES NOT (2026-08-18). The marker
    #    carries its records type, so the literal that used to be the net is gone. Detection now
    #    takes anything shaped like `<!-- word: ... -->`, and only then asks whether the word is
    #    a type this vault has - an unknown one is MALFORMED, by name and line, and never
    #    "a marker for a type nobody has heard of". Narrowing the net to the known words instead
    #    would move every typo in the type word into silence, which is the one failure this file
    #    has recorded six times.
    #
    #    Legality is "its folder exists", read off the swept map rather than a literal list of
    #    six. The map is built from the same tree rule 1 checks, so a category added tomorrow is
    #    a legal marker word the day its folder exists.
    #
    #    An unterminated fence is reported, and that is not tidiness. The fence-stripping pass is
    #    what makes a documented example safe to write, and it is also the one thing that can
    #    blind this rule completely: a fence opened and never closed swallows every marker below
    #    it, and the file reports zero regions rather than broken ones. Silence that looks like
    #    cleanliness is the failure this repository has repeated most, so it is named out loud.
    #    (No apostrophes below this line: the whole program is inside a single-quoted shell
    #    string, and one of them ended it mid-comment while this rule was being written.)
    BEGIN { n = split(typemap, pairs, " ")
            for (i = 1; i <= n; i++) { split(pairs[i], p, ":"); if (p[1] != "") plural[p[1]] = p[2] } }
    function closefile() { if (opened) print "unclosed|" prevfile "|" oaddr "|" oline
                           if (inb)    print "fence|" prevfile "|opened here|" fenceline }
    FNR == 1 {
        closefile()
        inb = 0; opened = 0; oaddr = ""; oline = 0
        prevfile = FILENAME
    }
    { sub(/\r$/, "") }
    /^```/ { if (!inb) fenceline = FNR; inb = !inb; next }
    inb { next }
    #    A FILE THE INJECTOR OWNS WHOLE SATISFIES THE CRITERION WITHOUT A REGION (owner,
    #    2026-08-20): criterion 6 reads *carries a marked region OR is fully generated*. A region
    #    protects an insert into a file that has other content around it; a generated file has
    #    none, so there is nothing for a region to do there and it could never acquire one.
    #    Counted here rather than by a grep per file, because this pass already reads every one of
    #    them and the gate runs about ninety times per selftest.
    #    RECOGNISED EXPLICITLY, and that is not tidiness. The line below would otherwise fall to
    #    the `malformed` verdict, which is RED - it escapes today only because the filter wants
    #    [a-zA-Z]+ before the colon and `vault-inject` carries a hyphen. A marker spelled
    #    `<!-- generated: ... -->` would redden the gate on every generated file, so the escape is
    #    an accident of spelling and is replaced here by a rule that means it.
    /^<!--[ \t]+vault-inject:[ \t]+generated[ \t]+from[ \t]+/ { gen[FILENAME] = 1; next }
    #    A MEASURE REGION IS OUT OF SCOPE BY NAME, and for the reason directly above. `<!-- measure
    #    -->` carries no colon, so it slips past the filter below without ever being judged - the
    #    same accident of spelling the generated-file marker escaped by, and the same repair. This
    #    rule asks about RULE regions: a measure region names no rule page and renders nothing, and
    #    it is checked by `scripts/vault-measure.py --check` instead.
    #
    #    A MISSPELLED ONE IS STILL RED. `<!-- measure: subject -->` does not match here, falls
    #    through, and is printed as `malformed` - which is what it is, since the form is exactly
    #    the two markers below and nothing else.
    #
    #    AND SAY OUT LOUD WHAT THIS DOES NOT REACH. Rule 11 walks the harness sweep alone - both
    #    CLAUDE.md files and every markdown file under `.claude/`. Every measure region the corpus
    #    will hold lives in a `wiki/` page, which this pass never opens, so this exemption is about
    #    the few that could appear in a harness file and about nothing else.
    /^<!--[ \t]*\/?[ \t]*measure[ \t]*-->[ \t]*$/ { next }
    {
        clean = $0
        gsub(/`[^`]*`/, " ", clean)
        if (clean !~ /<!--[ \t]*\/?[ \t]*[a-zA-Z]+[ \t]*:/) next

        #    The address is `folder/slug`, built here and never downstream: the caller joins on
        #    it and opens it as a path, and a second place computing the folder from the word is
        #    a second answer waiting to differ.
        if (clean ~ /^<!--[ \t]+[a-z]+:[ \t]+[a-z0-9][a-z0-9-]*[ \t]+-->[ \t]*$/) {
            body = clean
            sub(/^<!--[ \t]+/, "", body); sub(/[ \t]+-->[ \t]*$/, "", body)
            word = body; sub(/:.*$/, "", word)
            slug = body; sub(/^[a-z]+:[ \t]+/, "", slug)
            if (word in plural) {
                addr = plural[word] "/" slug
                if (opened)                             { print "nested|" FILENAME "|" addr "|" FNR; next }
                if ((FILENAME SUBSEP addr) in seenaddr) { print "dupslug|" FILENAME "|" addr "|" FNR; next }
                seenaddr[FILENAME SUBSEP addr] = 1
                opened = 1; oaddr = addr; oline = FNR; count[FILENAME]++
                print "slug|" FILENAME "|" addr "|" FNR
                next
            }
        }
        if (clean ~ /^<!--[ \t]+\/[a-z]+:[ \t]+[a-z0-9][a-z0-9-]*[ \t]+-->[ \t]*$/) {
            body = clean
            sub(/^<!--[ \t]+\//, "", body); sub(/[ \t]+-->[ \t]*$/, "", body)
            word = body; sub(/:.*$/, "", word)
            slug = body; sub(/^[a-z]+:[ \t]+/, "", slug)
            if (word in plural) {
                addr = plural[word] "/" slug
                if (!opened)        { print "unopened|" FILENAME "|" addr "|" FNR; next }
                if (addr != oaddr)  { print "mismatch|" FILENAME "|" oaddr " closed as " addr "|" FNR
                                      opened = 0; oaddr = ""; next }
                opened = 0; oaddr = ""
                next
            }
        }
        print "malformed|" FILENAME "|" clean "|" FNR
    }
    #    The coverage total is walked off ARGV, not off the files awk actually entered: awk runs
    #    no rule at all for a 0-byte file, so a governed file that is empty would drop out of the
    #    denominator and make the number read better than the tree is. An empty harness file is
    #    exactly the case this rule most wants counted.
    END { closefile(); for (i = 1; i < ARGC; i++)
              print "regions|" ARGV[i] "|" (count[ARGV[i]] + 0) "|" (gen[ARGV[i]] + 0) }
  ' | sort)"
  #    Sorted, because awk walks `for (f in files)` in hash order and an advisory whose text
  #    reorders between two runs over an unchanged tree reads as a change that did not happen.
  #    One line, not one per file. Eighteen advisory lines that never change is a way of
  #    teaching a reader to skip the advisories, and five of them already stand by decision.
  echo "VAULT-CHECK: advisory: a region or whole generation covers $marked of $governed_files harness markdown files${unmarked:+; neither yet: $unmarked}"
fi

# 12. Every current rule agrees with the region it governs.
#
#     Rule 11 proves the markup is well formed and that a region has a page behind it. It cannot
#     prove the region carries what the page says, and a region that agrees with nothing is
#     decoration - the whole point of writing a rule once is that the copies cannot drift, and
#     six copies of the handoff mapping drifted while every one of them was well formed.
#
#     ASKED BY RUNNING THE RENDERER, never by a second implementation of it. That is rule 9's
#     shape exactly: regenerate and compare, so the check and the writer cannot disagree about
#     what the right answer is. A comparison written twice is two answers waiting to differ.
#
#     What this guarantees is agreement and never truth, and that was demonstrated the day the
#     mechanism was designed: a draft rule text said `/ingest` runs at the retrospective, it was
#     false, and every mechanism here would have rendered it flawlessly. `/vault-lint` is still
#     the only thing that reads for sense.
INJECTOR="scripts/vault-inject.sh"
if [ ! -f "$INJECTOR" ]; then
  note "missing file: $INJECTOR - rule 12 asks its question by running it and cannot run"
else
  while IFS= read -r line; do
    case "$line" in
      "vault-inject: every rule agrees"*) ;;
      "vault-inject: "*) note "${line#vault-inject: }" ;;
      "") ;;
      *)  note "$INJECTOR --check said something rule 12 does not understand: $line" ;;
    esac
  done < <(VAULT="$VAULT" bash "$INJECTOR" --check 2>&1)
fi

# 13. The index the admission rule is decided by: every page can be looked up, and the register
#     that groups the lookups agrees with the tree.
#
#     WHY THIS RULE EXISTS AT ALL. `/ingest` had no valve on its intake - a unit became a page by
#     default - and the corpus reached 479 pages in nine days with 27 retirements against it. The
#     owner's ruling of 2026-08-21 makes not-multiplying-entities the ground rule, and the lookup
#     it is decided by is `authority:` plus the families in `$VAULT/authority.md`
#     ([[no-new-entity-where-an-existing-one-can-carry-the-claim]]).
#
#     ASKED BY RUNNING THE LOOKUP, never by a second implementation of it - rule 12's shape
#     exactly, and for its reason: a check that re-derives what the tool derives is two answers
#     waiting to differ. What counts as a page nothing can look up is defined once, in
#     `vault-authority.sh`, including the two exemptions that a per-folder schema cannot express -
#     a `rules/` page answers with `governs:`, and so does a `concepts/` page that renders.
#
#     IT WAS ADVISORY FOR THE LENGTH OF ONE BACK-FILL AND IS RED NOW, AND THAT ORDER IS THE POINT.
#     Red before the corpus carried the field would be read by `lock-the-librarian.ps1` as a refusal
#     to dispatch - locking out the only writer permitted to clear it, which is a deadlock this
#     repository has already built once ([[the-librarian-lock-hook]],
#     [[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]). So it printed advisories while
#     470 slugs were minted and grouped, and the flip to `note` in the same session IS the
#     acceptance test for that marking: if the gate is red after it, the marking is not finished.
AUTHORITY_TOOL="scripts/vault-authority.sh"
if [ ! -f "$AUTHORITY_TOOL" ]; then
  note "missing file: $AUTHORITY_TOOL - rule 13 asks its question by running it and cannot run"
else
  # ONE INVOCATION FOR BOTH MODES, 2026-08-24. It was two - `--orphans`, then `--check` - and this
  # tool walks the corpus once per RUN with every subcommand reading that one pass, so asking it
  # twice walked 577 pages twice. Its argument dispatch has looped over the argumentless modes
  # since 2026-08-22, so nothing in the tool had to change for this.
  #
  # MEASURED, AND THE NUMBER IS SMALL: 0.55 s and 0.99 s became 1.30 s, which buys about 0.24 s of
  # a 15.3 s gate. It is written down because "two walks became one" invites a reader to assume a
  # halving, and the walk is not what dominates this tool.
  #
  # THE TWO VERDICTS ARE STILL TWO AND NEITHER IS READ OFF THE OTHER'S SILENCE. Each mode has its
  # own good sentence; anything else from either becomes a note.
  #
  # AND THE `grep '^VAULT-AUTHORITY:'` THAT USED TO FILTER THE ORPHANS CALL IS GONE, deliberately.
  # It discarded every line the tool wrote that did not carry the prefix - a shell error, a stderr
  # word from something it shells out to - so half of this rule swallowed what the other half would
  # have reported. One loop, and the stricter half's behaviour is the one that survived.
  while IFS= read -r line; do
    case "$line" in
      "VAULT-AUTHORITY: every page outside"*) ;;
      "VAULT-AUTHORITY: the register and the tree agree"*) ;;
      "") ;;
      *) note "${line#VAULT-AUTHORITY: }" ;;
    esac
  done < <(VAULT="$VAULT" bash "$AUTHORITY_TOOL" --orphans --check 2>&1)
fi

# 14. A block attributed to the owner is written in his own Russian. Where a session understood
#     rather than heard, it writes in its own voice and does not sign `owner:`.
#
#     WHY THIS EXISTS. `advisory-is-the-default-for-a-hook` carried a quote block signed `owner:`,
#     stamped `basis: human`, and decided three things over three days. He had never said it: the
#     words were a previous session's English paraphrase, written into a journal under `**owner:**`
#     and compiled into a quotation. The chain runs every session - he speaks Russian, a session
#     paraphrases into English, the librarian renders the paraphrase as a quote, later sessions
#     reason from it as his word - and nothing ever showed him the paraphrase.
#
#     AN ADVISORY AND NOT RED, ON HIS OWN COUNTER-EXAMPLE: «не применимо например для случая когда
#     цитата будет на английском. То есть правило не универсальное». A genuine English quotation
#     from him exists as a case, so a red verdict would fire on a correct page.
#
#     BEHIND `--lint`, DECIDED 2026-08-22. 27 blocks would print on every bare run until the sweep
#     that reads them happens, and that sweep waits on the owner. This is a statement about the
#     corpus's history, not about the run in front of you - the same distinction that moved the
#     tag-density advisories, taking a bare run from twenty-one advisories to one.
#
#     WHAT CATCHES A NEW ONE IS NOT THIS. The ratification step in `/retro` puts every attributed
#     line to him before `/handoff` routes it, which is before it can become a page. An alphabet
#     separates a quotation from a paraphrase; only he separates a faithful paraphrase from a
#     wrong one, so the mechanical half was always the weaker one.
#
#     THE READER IS BYTES, NOT A CHARACTER CLASS, AND THAT IS A MEASUREMENT RATHER THAN A STYLE.
#     `grep -c` with a Cyrillic character class reported this corpus's split REVERSED - it is
#     byte-oriented here, the letter range does not map onto UTF-8 sequences, and it misses the
#     two letters sitting outside the alphabetic run in Unicode order. It agreed with itself
#     across two separate runs, which is how the wrong figure survived a correction and reached
#     three files. Cyrillic is U+0400-U+04FF, whose UTF-8 lead bytes are exactly 208 to 211; the
#     class is built from those codes under `LC_ALL=C` so no locale can reinterpret them, and it
#     was proved in both directions on planted input before it was wired in here.
if [ "$LINT" = 1 ] && [ -n "$pages" ]; then
  quotes=$(printf '%s\n' "$pages" | tr '\n' '\0' | LC_ALL=C xargs -0 awk '
      BEGIN { for (b = 208; b <= 211; b++) lead[sprintf("%c", b)] = 1 }
      /^> \*\*owner/ {
          cyr = 0; n = length($0)
          for (i = 1; i <= n; i++) if (substr($0, i, 1) in lead) { cyr = 1; break }
          if (!cyr) print FILENAME ":" FNR
      }' | sort)
  if [ -n "$quotes" ]; then
    #    THE COUNT IS ON THE FIRST LINE AND THE NAMES ARE ONE PER LINE, which is the shape the
    #    filename advisory already fixed: a reader greps the first line for the number and reads
    #    the rest as a list, and a name never has to be split out of a sentence.
    echo "VAULT-CHECK: advisory: $(printf '%s\n' "$quotes" | wc -l | tr -d ' ') owner-attributed block(s) carry no Cyrillic - a quotation keeps his own words, a paraphrase is written in the session's voice and is not signed 'owner:'; each is a candidate for the ratification sweep, not an action for this run"
    # THE CONTINUATIONS LOST THE WORD `advisory:` ON 2026-08-29, and they should never have had it.
    # The owner's ruling of 2026-08-18 is that every line carries `VAULT-CHECK:` and no continuation
    # carries the second word, because the brief reports `grep -c 'advisory:'` and a list of names
    # would be counted as advisories. The filename advisory has obeyed it since the day it was made;
    # this one and the `decided_by:` one below were written afterwards and copied the wrong shape.
    printf '%s\n' "$quotes" | sed 's/^/VAULT-CHECK:   /'
  fi
fi

# 15. Every measure region in the corpus is well formed.
#
#     THE NUMBER IS 15 AND NOT 14 EVEN AFTER 14 IS RETIRED. A retired rule number is never reused:
#     a verdict quoted in a journal, a page or a selftest case has to keep meaning what it meant.
#
#     ASKED BY RUNNING THE WRITER IT CHECKS - rules 12 and 13's shape, and here for their reason.
#     A check that re-derives what the writer derives is two answers waiting to differ.
#     `scripts/vault-measure.py` owns the grammar; this rule owns the question and nothing else.
#
#     AND IT READS THE LINES, NEVER THE EXIT CODE. That script uses 2 for a refusal AND for a
#     usage error, following `vault-archive.sh`, while the gate, the catalogue, the coverage and
#     the authority scripts use 2 for a usage error alone. The fork is real and is named in the
#     script's own docstring; reading the code here would make this rule depend on which side of
#     that fork a later change lands on.
#
#     WHAT IT DELIBERATELY DOES NOT DO IS RUN THE GAUGES. `--check` executes nothing, because
#     comparing every gauge against a fresh run would execute arbitrary commands taken from page
#     content at unbounded cost, and one gauge may name a command costing 38 minutes. What
#     protects a gauge from a lie is that it names the command anyone can re-run.
#
#     AND THIS IS THE ONLY THING THAT REACHES A MEASURE REGION AT ALL. Rule 11 walks the harness
#     sweep - both `CLAUDE.md` files and every markdown file under `.claude/` - while every
#     measure region lives in a `wiki/` page, which that pass never opens.
#
#     THE INTERPRETER IS FOUND AND NOT ASSUMED, AND `uv run` IS NOT USED. The selftest sandbox
#     copies `scripts/` and the vault and nothing else - there is no `pyproject.toml` in it - so
#     `uv run` inside a case would build an environment or fail. The script imports only the
#     standard library precisely so that a bare interpreter is enough. An interpreter that is
#     present but broken does not fall through silently: whatever it writes fails to match the
#     good sentence and becomes a note, which is the loud direction.
#
#     MEASURED IN THE UNIT THAT MATTERS, WHICH IS THIS GATE AND NOT THE SCRIPT. Three runs each
#     way on 2026-08-26: with this rule 20.20 / 20.44 / 20.46 s, without it 19.92 / 20.13 /
#     20.25 s. The delta is 0.28 s, so the suite's ~171 gate runs pay about 50 seconds - not the
#     four minutes estimated from rule 13's 1.5 s, and not the 0.124 s the script shows when timed
#     on its own. THE STANDALONE FIGURE UNDERSTATES IT BY MORE THAN HALF and was nearly written
#     here as the answer; it omits the interpreter search and the process this gate spawns.
#
#     AND THE GATE ITSELF READS 20.2 s HERE, against the 15.3 s the corpus records. That is the
#     machine drift already on the register and not something this rule did.
MEASURE_TOOL="scripts/vault-measure.py"
if [ ! -f "$MEASURE_TOOL" ]; then
  note "missing file: $MEASURE_TOOL - rule 15 asks its question by running it and cannot run"
else
  MEASURE_PY=""
  #    A CANDIDATE UNDER `WindowsApps` IS SKIPPED WITHOUT BEING RUN, and the order is unchanged
  #    otherwise. On this machine `python3` resolves to the Microsoft Store stub -
  #    AppData/Local/Microsoft/WindowsApps/python3 -> PythonSoftwareFoundation.PythonManager - which
  #    neither answers nor exits. The paragraph above provides for an interpreter that is "present
  #    but broken" on the ground that whatever it writes fails to match the good sentence and
  #    becomes a note; that reasoning holds for one that RETURNS. A hanging one writes nothing, so
  #    there is no note and no verdict - the gate simply never finishes, which cost this session an
  #    hour on 2026-08-26 and was diagnosed as a starved machine twice before it was diagnosed here.
  #    THE GUARD RUNS BEFORE THE PROCESS AND NOT AROUND IT, deliberately: `timeout 15 python3 -c`
  #    did not return in 90 s on this machine, because an MSYS signal does not reach a native
  #    Windows process - the same property that made `kill -9` useless against this suite's orphans
  #    and left `taskkill //PID <winpid> //F //T` as the only thing that worked. A wrapper cannot
  #    save a probe from a process it cannot kill, so the candidate has to be refused unrun.
  for measure_candidate in python3 python py; do
    command -v "$measure_candidate" >/dev/null 2>&1 || continue
    case "$(command -v "$measure_candidate")" in *WindowsApps*) continue ;; esac
    MEASURE_PY="$measure_candidate"; break
  done
  if [ -z "$MEASURE_PY" ]; then
    #    A NAMED VERDICT RATHER THAN SILENCE. A check that cannot run and says nothing reads
    #    exactly like a check that passed, which is the shape of green this file has shipped six
    #    times.
    note "no python interpreter on PATH - rule 15 runs $MEASURE_TOOL and cannot"
  else
    while IFS= read -r line; do
      case "$line" in
        "VAULT-MEASURE: every measure region is well formed"*) ;;
        "VAULT-MEASURE: "*) note "${line#VAULT-MEASURE: }" ;;
        "") ;;
        *)  note "$MEASURE_TOOL --check said something rule 15 does not understand: $line" ;;
      esac
    done < <(VAULT="$VAULT" "$MEASURE_PY" "$MEASURE_TOOL" --check 2>&1)
  fi
fi

# 16. A page written under the decision lifecycle carries the body sections and the frontmatter
#     keys its folder declares - and only from the date that folder declares.
#
#     WHY A DATE AND NOT A BACK-FILL. `wiki/decisions/` holds 299 pages that have never been read
#     as a set, and the owner's prohibition of 2026-08-29 is that the folder's state is established
#     by a census before its type system is changed - a census that is the decisions agent's second
#     mode and has never run. A dated cut changes the type system for what is written from here on
#     and leaves the older population untouched, so the prohibition is not crossed and the census
#     stays owed rather than blocking every other piece of work behind it.
#
#     AND THE KEYS ARE `optional:` IN THE SCHEMA, NOT `required:`. The `missing` verdict of the
#     frontmatter pass knows nothing about dates, so a key required there would redden all 299 at
#     once - and a red gate is what `lock-the-librarian.ps1` reads as a refusal to dispatch, which
#     locks out the only writer permitted to clear it. This is the order this file set has already
#     run three times, on `basis`, `authority` and `binding`: legal and optional, then the fill,
#     then the promotion. `required_from:` is the middle step made mechanical instead of remembered.
#
#     TWO LISTS OF ONE SET DRIFT, so a key named in `required_from:` is checked against the folder's
#     own key set first. A key obliged here and allowed nowhere would make this rule demand exactly
#     what the `unknownkey` verdict then reddens - a page that cannot be written correctly at all,
#     and the sort of trap that is only ever found by walking into it.
#
#     A FOLDER THAT DECLARES NEITHER IS NOT JUDGED, and that is why four of the six carry no block
#     at all rather than an empty one. An empty `sections:` would have to mean "no sections are
#     required", which reads identically to a block somebody meant to fill and did not - and the
#     doctrine everywhere else in this file is that a block parsing to nothing is red precisely
#     because the silent reading runs in the direction of passing. Absence says it once and says it
#     honestly.
lc_block() {          # lc_block <schema> <key> - the list items under a top-level key
  awk -v k="$2:" '
      { sub(/\r$/, "") }
      index($0, k) == 1 && $0 == k { m = 1; next }
      /^[a-z]/ { m = 0 }
      m == 1 && /^[ \t]*-[ \t]*/ {
          sub(/^[ \t]*-[ \t]*/, ""); sub(/[ \t]+$/, "")
          if ($0 != "") print
      }' "$1"
}
while IFS= read -r lfolder; do
  [ -n "$lfolder" ] || continue
  lfile="$VAULT/wiki/$lfolder/_schema.yaml"
  [ -f "$lfile" ] || continue
  grep -q '^lifecycle_from:' "$lfile" || continue

  lfrom=$(sed -n 's/^lifecycle_from:[[:space:]]*//p' "$lfile" | head -1 | tr -d ' \r')
  case "$lfrom" in
    [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;;
    *) note "wiki/$lfolder/_schema.yaml: lifecycle_from: reads '$lfrom', which is not a YYYY-MM-DD date - rule 16 scopes itself by that date and will not guess one"
       continue ;;
  esac

  lwant=$(lc_block "$lfile" sections)
  lkeys=$(lc_block "$lfile" required_from)
  #    THE CONDITIONAL SECTION SET, added 2026-08-30 and read the same way as the two above. It is
  #    owed only by a page whose `target_kind:` is `rule`, because it carries the text that becomes
  #    the rule page - and a decision targeting an action or a repeal has no such text. A flat
  #    `sections:` list cannot say that, which is why the condition lives here.
  lwantrule=$(lc_block "$lfile" sections_when_target_kind_rule)
  #    A header present and parsing to nothing is red here for the same reason it is red for
  #    `required:` and `values:` above: an empty set turns the check into "everything passes",
  #    silently, in the direction that hides a defect.
  if grep -q '^sections:' "$lfile" && [ -z "$lwant" ]; then
    note "wiki/$lfolder/_schema.yaml: a sections: block that parses to nothing - an empty set would let every page through, silently and in the direction of passing"
  fi
  if grep -q '^required_from:' "$lfile" && [ -z "$lkeys" ]; then
    note "wiki/$lfolder/_schema.yaml: a required_from: block that parses to nothing - an empty set would let every page through, silently and in the direction of passing"
  fi
  if grep -q '^sections_when_target_kind_rule:' "$lfile" && [ -z "$lwantrule" ]; then
    note "wiki/$lfolder/_schema.yaml: a sections_when_target_kind_rule: block that parses to nothing - an empty set would let every page through, silently and in the direction of passing"
  fi
  [ -n "$lwant$lkeys$lwantrule" ] || continue

  lallowed=$( { lc_block "$lfile" required; lc_block "$lfile" optional; } | sort -u)
  while IFS= read -r lk; do
    [ -n "$lk" ] || continue
    printf '%s\n' "$lallowed" | grep -qx -- "$lk" \
      || note "wiki/$lfolder/_schema.yaml: required_from: names '$lk', which is in neither required: nor optional: - rule 16 would oblige a key that the unknownkey verdict then reddens, so no page in this folder could be written correctly"
  done < <(printf '%s\n' "$lkeys")

  #    ONE PASS OVER THE FOLDER AND NOT FOUR PROCESSES PER PAGE. The note on rules 4 and 5 records
  #    what the per-page shape cost when it was tried: 71 seconds over 75 files, growing as the
  #    square. Frontmatter keys are read only between the opening and closing `---`, so a prose
  #    line beginning `target:` is not mistaken for a field, and headings are read only outside
  #    fenced blocks, so a documented example is not mistaken for a section.
  while IFS='|' read -r lkind lpage ldetail; do
    [ -n "$lkind" ] || continue
    case "$lkind" in
      lcsection) note "$lpage: created $ldetail and is missing the '# ' section(s) its folder declares in sections: - write the heading, with \"none\" under it if there is nothing to say, rather than dropping it" ;;
      lcrulesection) note "$lpage: created $ldetail - a decision carrying 'target_kind: rule' owes the '# ' section its folder declares in sections_when_target_kind_rule:, because that section carries the sentence the rule page is assembled from. Write the heading, with the clause under it" ;;
      lckey)     note "$lpage: created on or after wiki/$lfolder/_schema.yaml's lifecycle_from: and carries no '$ldetail:' - the field is optional in the schema so the older pages stay legal, and required from that date by rule 16" ;;
    esac
  done < <(find "$VAULT/wiki/$lfolder" -maxdepth 1 -name '*.md' -size +0 -print0 2>/dev/null \
    | xargs -0 --no-run-if-empty awk -v from="$lfrom" -v want="$lwant" -v keys="$lkeys" \
                                     -v wantrule="$lwantrule" '
        BEGIN {
            wn = split(want, wa, "\n"); kn = split(keys, ka, "\n")
            rn = split(wantrule, ra, "\n")
        }
        FNR == 1 { f = FILENAME; files[f] = 1; fm = 0; seenfm = 0; inb = 0 }
        { sub(/\r$/, "") }
        FNR == 1 && $0 == "---" { fm = 1; seenfm = 1; next }
        fm && $0 == "---" { fm = 0; next }
        fm {
            if (match($0, /^[A-Za-z_][A-Za-z_0-9]*:/)) {
                k = substr($0, 1, RLENGTH - 1)
                haskey[f, k] = 1
                if (k == "created") { v = substr($0, RLENGTH + 1); gsub(/[ \t"]/, "", v); created[f] = v }
                if (k == "target_kind") { v = substr($0, RLENGTH + 1); gsub(/[ \t"]/, "", v); tkind[f] = v }
            }
            next
        }
        /^```/ { inb = !inb; next }
        !inb && index($0, "# ") == 1 {
            s = substr($0, 3); sub(/^[ \t]+/, "", s); sub(/[ \t]+$/, "", s)
            if (s != "") head[f, s] = 1
        }
        END {
            for (f in files) {
                c = created[f]
                #    A page with no `created:` is already the frontmatter pass "missing" verdict,
                #    by name. Saying it a second time here buries the line that matters.
                if (c == "" || c < from) continue
                miss = ""
                for (i = 1; i <= wn; i++)
                    if (wa[i] != "" && !((f, wa[i]) in head))
                        miss = miss (miss == "" ? "" : "; ") wa[i]
                if (miss != "") print "lcsection|" f "|" c ", missing [" miss "]"
                #    Ranges over one value of one field, so it is only asked of a page that has
                #    something to write under the heading.
                if (tkind[f] == "rule") {
                    rmiss = ""
                    for (i = 1; i <= rn; i++)
                        if (ra[i] != "" && !((f, ra[i]) in head))
                            rmiss = rmiss (rmiss == "" ? "" : "; ") ra[i]
                    if (rmiss != "") print "lcrulesection|" f "|" c ", missing [" rmiss "]"
                }
                for (i = 1; i <= kn; i++)
                    if (ka[i] != "" && !((f, ka[i]) in haskey))
                        print "lckey|" f "|" ka[i]
            }
        }')
done < <(find "$VAULT/wiki" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | sed 's|.*/||' | sort)

# 17. The handshake: a decision whose target EXISTS names it back.
#
#     A decision declares its target forward, in plain text, at the moment it is ratified; the page
#     it names declares the decision back in `decided_by:` when it lands. Only both together let
#     the decision leave `wiki/decisions/`. Before this a decision closed on the backward pointer
#     alone, and that reads causation as carriage: `the-lessons-collector-is-a-reading-dispatch`
#     left `wiki/` because four live proposals named it, and every one of them was a draft it had
#     produced rather than a page describing it.
#
#     A TARGET THAT DOES NOT EXIST IS NOT RED, AND THAT IS THE WHOLE SHAPE OF THE RULE. It is what
#     "this decision is still open" means, and it is the state the owner asked to be able to see.
#     What is red is the half-finished landing: the page is there and does not name the decision.
#
#     SCOPED TO `rule` AND `proposal` TARGETS, and the scope is not a convenience. `decided_by:` is
#     legal in `wiki/proposals/` and `wiki/rules/` alone - ratified four times, most recently on
#     2026-08-29 - so a target anywhere else CANNOT name the decision back and a verdict over it
#     could never be cleared. `repeal` is the sharp case: such a decision never leaves the folder
#     and its target exists by definition, so an unscoped verdict would redden it for good. This
#     store has built a verdict that cannot fire twice already, both times caught at exactly this
#     point in the process, and this is the third one refused rather than the third one shipped
#     ([[the-unreachable-verdict-is-dropped-and-replaced]]).
#
#     THE TARGET IS RESOLVED IN THE TWO FOLDERS AND NOWHERE ELSE, for the same reason. A slug that
#     resolves in neither is an open decision, not a broken link - `target:` is plain text and joins
#     no link sweep, which is what lets it name a page that has not been written yet.
hs_pages=$(grep -rl --include='*.md' -E '^target_kind:[[:space:]]*(rule|proposal)[[:space:]]*$' \
             "$VAULT/wiki/decisions" 2>/dev/null | sort)
if [ -n "$hs_pages" ]; then
  while IFS= read -r hp; do
    [ -n "$hp" ] || continue
    hslug=${hp##*/}; hslug=${hslug%.md}
    htgt=$(sed -n 's/^target:[[:space:]]*//p' "$hp" | head -1 | tr -d ' \r' | tr -d '"')
    [ -n "$htgt" ] || continue
    hfile=""
    for hdir in proposals rules; do
      if [ -f "$VAULT/wiki/$hdir/$htgt.md" ]; then hfile="$VAULT/wiki/$hdir/$htgt.md"; break; fi
    done
    [ -n "$hfile" ] || continue
    #    The target must name THIS decision's slug, not its own. `decided_by:` is read here by
    #    searching the line for the slug rather than by taking the last wikilink on it, which is
    #    what the frontmatter pass does with a greedy `s/.*\[\[//`. The difference matters in one
    #    direction only and it is the safe one: a line carrying two links resolves to the last for
    #    that pass and to "names me" for this one, so this rule cannot manufacture a red out of a
    #    field it read differently from everybody else.
    if ! grep -qE "^decided_by:.*\[\[$hslug(\|[^]]*)?\]\]" "$hfile" 2>/dev/null; then
      note "$hp: its target '$htgt' exists at ${hfile#"$VAULT/"} and does not name this decision in decided_by: - the landing is half done, and the decision cannot be released until both halves agree"
    fi
  done < <(printf '%s\n' "$hs_pages")
fi

# THE `decided_by:` SHORTFALL, under `--lint`, and it is the second half of acceptance criterion 3
# of S3. The criterion asks for the field to be LEGAL and for the shortfall to be COUNTED - it does
# not ask for the back-fill, which is separate work and is deferred.
#
# THE POPULATION IS `wiki/proposals/` AND `wiki/rules/` ALONE, because those are the two folders
# the field is legal in after the narrowing of 2026-08-23. Elsewhere its absence is not a shortfall
# but a category error, and the `unknownkey` verdict already reddens a page that carries it there
# ([[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]]). Counting all six would
# report a number nobody can act on - the shape the `314 pages` figure already had.
#
# BEHIND `--lint` AND NEVER ON A BARE RUN. A bare run answers one question - is anything wrong with
# the tree in front of me - and a field waiting for its back-fill is not. A counter that prints the
# same number every run is the class of alarm this project has removed three times.
#
# THE COUNT IS ON THE FIRST LINE AND THE NAMES ARE ONE PER LINE, the shape the filename advisory
# fixed and the quote advisory above copies: a reader greps the first line for the number and reads
# the rest as a list.
if [ "$LINT" = 1 ]; then
  dbmissing=$(find "$VAULT/wiki/proposals" "$VAULT/wiki/rules" -name '*.md' -size +0 2>/dev/null \
              | while IFS= read -r dbf; do
                  grep -q '^decided_by:' "$dbf" || printf '%s\n' "$dbf"
                done | sort)
  if [ -n "$dbmissing" ]; then
    echo "VAULT-CHECK: advisory: $(printf '%s\n' "$dbmissing" | wc -l | tr -d ' ') page(s) in proposals/ and rules/ carry no decided_by: - the field names the decision that caused the page; it is REQUIRED in rules/ from 2026-08-23, so every page named below is a proposals/ page; the back-fill there is S3 work rather than an action for this run"
    printf '%s\n' "$dbmissing" | sed 's/^/VAULT-CHECK:   /'
  fi
fi

# A LIVE PAGE LINKS A PAGE THAT WAS RETIRED. An advisory and never a red: linking a deprecated page
# is legal and often right - "why did we change this" is a legitimate question and the deprecated
# page is where it is answered ([[a-live-page-can-argue-from-a-deprecated-one]]). Ordered built by
# the owner on 2026-08-28, overturning a refusal of two days earlier.
#
# IT KEYS ON THE LITERAL VALUE `deprecated`, NOT ON "the target's status", and that narrowing was
# taken before a line of it was written. From 2026-08-29 about 240 pages in `archive/` carry
# `status: archived`, so a verdict phrased about the status in general would have grown from forty
# lines to hundreds on the day the sweep first ran. `archived` means the page finished its job;
# `deprecated` means it went false. Only the second is worth naming.
#
# ONE LINE PER DEAD TARGET, chosen by the owner over one per citing page and one per edge. The name
# that matters is the target's: the list shrinks one name at a time as pages are repointed, which is
# the case the one-name-per-line ruling was made for.
#
# `decided_by:` IS A SEPARATE KIND AND NOT A WIDER COUNT. Such a pointer is already ruled to be KEPT
# as it stands and to become a lesson candidate; folding it in with body links loses exactly the
# distinction that ruling drew.
#
# ONE WALK, NOT ONE GREP PER PAGE. The note on rules 4 and 5 records the per-page shape at 71
# seconds over 75 files, growing as the square - but that shape was N recursive greps over the whole
# tree. This is a single pass that keeps FILENAME beside every link it finds, which is linear, and
# it sits behind `--lint` so a bare run does not pay for it at all.
if [ "$LINT" = 1 ]; then
  dep_slugs=$(grep -rl --include='*.md' -E '^status:[ \t]*deprecated[ \t]*$' \
                "$VAULT/wiki" "$VAULT/archive" 2>/dev/null \
              | sed 's|.*/||; s|\.md$||' | sort -u)
  if [ -n "$dep_slugs" ]; then
    dep_edges=$(find "$VAULT/wiki" -name '*.md' -size +0 -print0 2>/dev/null \
      | xargs -0 --no-run-if-empty awk '
          FNR == 1 { inblock = 0; f = FILENAME; sub(/.*\//, "", f); sub(/\.md$/, "", f) }
          { sub(/\r$/, "") }
          /^```/ { inblock = !inblock; next }
          inblock { next }
          {
            kind = (index($0, "decided_by:") == 1) ? "d" : "b"
            line = $0
            gsub(/`[^`]*`/, "", line)
            while (match(line, /\[\[[^]]*\]\]/)) {
              t = substr(line, RSTART + 2, RLENGTH - 4)
              sub(/[|#].*$/, "", t); sub(/[ \t]+$/, "", t)
              if (t != "" && t != f) print kind "\t" f "\t" t
              line = substr(line, RSTART + RLENGTH)
            }
          }')
    dep_agg=$(printf '%s\n' "$dep_edges" | awk -F'\t' -v deps="$dep_slugs" '
        BEGIN { n = split(deps, a, "\n"); for (i = 1; i <= n; i++) if (a[i] != "") dep[a[i]] = 1 }
        NF < 3 || !($3 in dep) { next }
        { key = $1 "\t" $3; occ[key]++; if (!seen[key "\t" $2]++) pgs[key]++ }
        END { for (k in occ) print k "\t" occ[k] "\t" pgs[k] }')
    dep_body=$(printf '%s\n' "$dep_agg" \
      | awk -F'\t' '$1 == "b" { printf "%s (%s link(s) from %s page(s))\n", $2, $3, $4 }' | sort)
    dep_db=$(printf '%s\n' "$dep_agg" \
      | awk -F'\t' '$1 == "d" { printf "%s (named in decided_by: by %s page(s))\n", $2, $4 }' | sort)
    if [ -n "$dep_body" ]; then
      echo "VAULT-CHECK: advisory: $(printf '%s\n' "$dep_body" | wc -l | tr -d ' ') retired page(s) are still linked from live pages under wiki/ - the link is legal and is often right, since a deprecated page is where 'why did we change this' is answered; this list shrinks as pages are repointed at the successor that carries the claim"
      printf '%s\n' "$dep_body" | sed 's/^/VAULT-CHECK:   /'
    fi
    if [ -n "$dep_db" ]; then
      echo "VAULT-CHECK: advisory: $(printf '%s\n' "$dep_db" | wc -l | tr -d ' ') retired page(s) are named in a decided_by: field - that pointer is KEPT as it stands and is a lesson candidate rather than a repair"
      printf '%s\n' "$dep_db" | sed 's/^/VAULT-CHECK:   /'
    fi
  fi
fi

[ "$fail" -eq 0 ] && echo "VAULT-CHECK: ok"
exit "$fail"
