"""`guppi materialize [--date YYYY-MM-DD] [--show]` — the ledger and the Spec as one yaml.

Reads `vault/raw/<date>/ledger.md` and every Spec of the date — `vault/raw/<date>/spec.md`
when the date has one (dates before case 73), then `vault/raw/<date>/<HHMM>/spec.md` in
folder order — and writes `vault/raw/<date>/materialize.yaml`: one entry per record line
of the ledger, in ledger order, with its route computed from `index.md` §5 and its content
lifted from the `then` block of its Case in the Spec. The yaml's `spec` field lists the
files read and each decision entry names the file its Case was found in; a Case heading
found in two files stops the walk with exit 1 (case 73.5). One decision entry per Case; a
sub-case's `context`, `problem`, `recommend` and `given` are its own when present and its
parent's otherwise, `when` never. What is missing is named (`incomplete`), never invented.
A line the grammar does not parse goes under `unparsed`. `new_tags` declared in the `then`
block of any Case, with decision lines or without, reach the yaml once each.

The Estimate of a Leaf is derived from its Case (case 72.3). A `create` of a rule or an
entity whose `then` item carries `method` yields, right after its own entry, a second
`create` entry with no line of its own: category `estimates`, slug `estimate-<target minus
its prefix>` or the item's `estimate_slug`, `ref` the target, `tags` the target's, `origin`
and `decision` the line's, `derived: true`, sections Context (the Case's `problem`),
Criterion (a `### case N` block: the Case's `when` and `then` verbatim, with their
operands) and Method. An `update` whose item carries `contract: changed` yields an
`update` entry of the target's Estimate — the first slug of the live page's `estimates`,
`incomplete: [estimate]` when there is none — with `criterion_block`, `set: {status:
pending}`, `sections: {Method}` when the item carries `method` and `change`; `contract:
same` yields nothing. A line with `{supersedes:case N}` also yields a `remove_criterion`
entry with `case_removed`, for `generate` to find the Estimate that holds the block. The
decision entry carries `criterion`, one `{estimate, case}` per Estimate the Case shaped. A
nested `estimate` in an older Spec becomes its own `create` entry as before, for a line
with its slug; a standalone estimate `create` with `ref` maps `context`, `criterion` and
`method` into `sections` the same way.

An existing yaml is extended with the lines it does not hold and never rewritten. Without
`--date` the script walks every `vault/raw/<date>/` that holds a `ledger.md`, in date
order, so a line written after the librarian's commit of its date is picked up by the next
run; an error on one date stops the walk with exit 1. With `--show` (case 76) the same walk
prints to stdout the yaml each date would be written with, one document per date, `---`
between two, and writes nothing under `raw/`. Rule page:
`vault/wiki/rules/rule-materialize.md`.
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml

from guppi.event import project_root
from guppi.ledger import body as line_body

RECORD = re.compile(r"^- (?:\d\d:\d\d:\d\d )?(decision|estimate|lesson)(\[.*)$")
BRACKETS = re.compile(r"\[([^\]]*)\]")
BRACES = re.compile(r"\{(\w+):([^}]*)\}")
HEADING = re.compile(r"^#{1,4} (.*)$")
CASE_HEADING = re.compile(r"^#{2,4} Case (\S+)")
FENCE = re.compile(r"^ {0,3}```(\S*)\s*$")
QUOTE = re.compile(r"^> ?(.*)$")
SECTION_START = re.compile(r"^\*\*(\w+):\*\*\s*(.*)$")
DECISION_KINDS = ("create", "update", "delete", "defer")
PREFIXES = {
    "rule-": "rules",
    "entity-": "entities",
    "estimate-": "estimates",
    "lesson-": "lessons",
    "insight-": "insights",
    "decision-": "decisions",
}
RULE_CLASS = {
    "index": "vault/wiki/index.md",
    "glossary": "vault/wiki/glossary.md",
    "case-schema": "vault/wiki/case-schema.md",
    "migration-plan": "docs/migration/migration-plan.md",
}
CATEGORIES = ("entities", "rules", "estimates", "lessons", "insights", "decisions")
REQUIRED = {
    "rules": ("type", "kind", "purpose", "tags"),
    "entities": ("type", "kind", "purpose", "tags"),
    "estimates": ("kind", "criterion", "method"),
    "insights": ("pattern", "children", "tags"),
}
CASE_SECTIONS = ("context", "problem", "recommend", "given", "when", "then", "ratification")
INHERITED = ("context", "problem", "recommend", "given")  # a sub-case reads these from its parent
DERIVED_CATEGORIES = ("rules", "entities")  # the targets whose Estimate a Case derives (72.3)
DERIVED_KEYS = ("method", "contract", "estimate_slug", "estimate_kind")  # never the target's
SESSION_FOLDER = re.compile(r"^\d{4}$")  # raw/<date>/<HHMM>/, one session's Spec (case 73)


class MaterializeError(Exception):
    pass


# --- the ledger ---------------------------------------------------------------------


def parse_line(text: str) -> dict | None:
    """The record of one ledger line, or None when the grammar does not match."""
    match = RECORD.match(text.rstrip())
    if not match:
        return None
    kind, rest = match.groups()
    heads = BRACKETS.findall(rest)
    tail = rest[BRACKETS.search(rest).start() :]
    if kind == "decision":
        if len(heads) < 3 or not heads[0].startswith("case "):
            return None
        options = {k: v.strip() for k, v in BRACES.findall(tail)}
        if heads[1] not in DECISION_KINDS:
            return None
        return {
            "record": "decision",
            "case": heads[0][5:].strip(),
            "kind": heads[1],
            "slug": heads[2].strip(),
            "ref": options.get("ref"),
            "source": options.get("source"),
            "supersedes": _case_of(options.get("supersedes")),
            "tags": _tags(options.get("tags")),
        }
    if kind == "estimate":
        if len(heads) < 2 or heads[1] not in ("passed", "failed"):
            return None
        after = tail[BRACKETS.match(tail).end() :]
        after = after[BRACKETS.match(after).end() :].strip()
        return {"record": "estimate", "slug": heads[0].strip(), "status": heads[1], "result": after}
    if len(heads) < 2 or heads[0] not in ("error", "knowledge"):
        return None
    after = tail[BRACKETS.match(tail).end() :]
    after = after[BRACKETS.match(after).end() :]
    options = {k: v.strip() for k, v in BRACES.findall(after.split(" trigger:", 1)[0])}
    after = after[after.find("trigger:") :] if "trigger:" in after else after.strip()
    trigger, _, root_cause = after.partition("root_cause:")
    trigger = trigger.strip()
    if trigger.startswith("trigger:"):
        trigger = trigger[len("trigger:") :].strip()
    return {
        "record": "lesson",
        "kind": heads[0],
        "slug": heads[1].strip(),
        "trigger": trigger,
        "root_cause": root_cause.strip(),
        "tags": _tags(options.get("tags")),
        "source": options.get("source"),
    }


def _case_of(value: str | None) -> str | None:
    if not value:
        return None
    value = value.strip()
    return value[5:].strip() if value.startswith("case ") else value


def _tags(value: str | None) -> list[str]:
    if not value:
        return []
    return [t.strip() for t in value.split(",") if t.strip()]


def category_of(slug: str) -> str | None:
    for prefix, category in PREFIXES.items():
        if slug.startswith(prefix):
            return category
    return None


def rule_class_path(slug: str) -> str | None:
    if slug in RULE_CLASS:
        return RULE_CLASS[slug]
    match = re.match(r"^(\w+)-schema(-yaml)?$", slug)
    if match and match.group(1) in CATEGORIES:
        name = "schema.yaml" if match.group(2) else "schema.md"
        return f"vault/wiki/{match.group(1)}/{name}"
    return None


# --- the Spec -----------------------------------------------------------------------


def split_cases(spec: str) -> dict[str, list[str]]:
    """Case id → the lines under its heading, up to the next heading of any level."""
    cases: dict[str, list[str]] = {}
    current: str | None = None
    for line in spec.splitlines():
        heading = HEADING.match(line)
        if heading:
            case = CASE_HEADING.match(line)
            current = case.group(1).rstrip(":") if case else None
            if current is not None:
                cases.setdefault(current, [])
            continue
        if current is not None:
            cases[current].append(line)
    return cases


def spec_files(project_dir: Path, date: str) -> list[Path]:
    """Every Spec of a date: `raw/<date>/spec.md` when it exists, then each
    `raw/<date>/<HHMM>/spec.md` in folder order (case 73.5)."""
    raw = project_dir / "vault" / "raw" / date
    files = [raw / "spec.md"] if (raw / "spec.md").is_file() else []
    if raw.is_dir():
        folders = sorted(p for p in raw.iterdir() if p.is_dir() and SESSION_FOLDER.match(p.name))
        files.extend(p / "spec.md" for p in folders if (p / "spec.md").is_file())
    return files


def read_specs(project_dir: Path, date: str) -> tuple[dict[str, list[str]], dict[str, str]]:
    """The Cases of every Spec of the date, and the file each Case was found in (relative
    to the project); a Case heading in two files is an error."""
    cases: dict[str, list[str]] = {}
    found: dict[str, str] = {}
    for path in spec_files(project_dir, date):
        name = path.relative_to(project_dir).as_posix()
        for case, lines in split_cases(path.read_text(encoding="utf-8")).items():
            if case in found:
                raise MaterializeError(f"Case {case} is in both {found[case]} and {name}")
            cases[case] = lines
            found[case] = name
    return cases, found


def unquote(line: str) -> str:
    match = QUOTE.match(line)
    return match.group(1) if match else line


def then_blocks(lines: list[str]) -> tuple[dict, list[str]]:
    """The merged content of every fence tagged `then` under a Case, and the parse errors."""
    merged: dict = {}
    errors: list[str] = []
    fence_open = False
    recording = False
    buffer: list[str] = []
    for raw in lines:
        line = unquote(raw)
        match = FENCE.match(line)
        if match:
            if not fence_open:
                fence_open = True
                recording = match.group(1).lower() == "then"
                buffer = []
            else:
                fence_open = False
                if recording:
                    _merge_block(merged, "\n".join(buffer), errors)
                recording = False
            continue
        if recording:
            buffer.append(line)
    return merged, errors


def _merge_block(merged: dict, text: str, errors: list[str]) -> None:
    try:
        data = yaml.safe_load(text) or {}
    except yaml.YAMLError as exc:
        errors.append(f"then block is not YAML: {exc}")
        return
    if not isinstance(data, dict):
        errors.append("then block is not a mapping")
        return
    for key, value in data.items():
        if isinstance(value, list):
            merged.setdefault(key, []).extend(value)
        else:
            merged[key] = value


def case_text(lines: list[str]) -> dict[str, str]:
    """The seven quoted sections of a Case, name → text, from `> **name:**` blocks."""
    sections: dict[str, str] = {}
    current: str | None = None
    buffer: list[str] = []
    in_fence = False

    def close():
        if current is not None:
            sections[current] = "\n".join(buffer).strip("\n")

    for raw in lines:
        match = QUOTE.match(raw)
        if not match:
            if FENCE.match(raw):
                in_fence = not in_fence
            if not in_fence and current is not None and raw.strip() == "":
                close()
                current = None
            continue
        text = match.group(1)
        start = SECTION_START.match(text)
        if start and start.group(1) in CASE_SECTIONS:
            close()
            current = start.group(1)
            buffer = [start.group(2)] if start.group(2) else []
        elif current is not None:
            buffer.append(text)
    close()
    return sections


def case_texts(cases: dict[str, list[str]], case: str) -> dict[str, str]:
    """The sections of a Case, with a missing `context`, `problem`, `recommend` or `given`
    read from its parent (case 60), never `when`; a Spec older than the seven-block form
    gives its text whole as `then`."""
    lines = cases.get(case, [])
    texts = case_text(lines)
    if not texts and lines:
        texts = {"then": "\n".join(lines).strip("\n")}
    if "." in case:
        for name, text in case_text(cases.get(case.rsplit(".", 1)[0], [])).items():
            if name in INHERITED:
                texts.setdefault(name, text)
    return texts


def find_item(block: dict, kind: str, slug: str) -> tuple[dict | None, str | None]:
    """The `then` item for a decision, and the kind of the create it was nested in."""
    for item in block.get(kind) or []:
        if isinstance(item, dict) and item.get("slug") == slug:
            return item, None
    if kind == "create":
        for item in block.get("create") or []:
            nested = item.get("estimate") if isinstance(item, dict) else None
            if isinstance(nested, dict) and nested.get("slug") == slug:
                return dict(
                    nested, parent_create=item.get("slug"), parent_tags=item.get("tags")
                ), "estimate"
    return None, None


# --- entries ------------------------------------------------------------------------


def page_exists(project_dir: Path, category: str, slug: str) -> bool:
    wiki = project_dir / "vault" / "wiki"
    if (wiki / category / f"{slug}.md").exists():
        return True
    archived = project_dir / "vault" / "archived"
    return archived.is_dir() and any(archived.rglob(f"{slug}.md"))


def decision_entry(record: dict, number: int, text: str, date: str, block: dict, project_dir: Path):
    kind, slug = record["kind"], record["slug"]
    entry: dict = {
        "line": number,
        "text": text,
        "case": record["case"],
        "kind": kind,
        "slug": slug,
        "origin": f"raw/{date}/ledger.md#case-{record['case']}",
        "decision": f"decision-case-{record['case']}",
    }
    for key in ("ref", "source", "supersedes"):
        if record.get(key):
            entry[key] = record[key]
    if record.get("tags"):
        entry["tags"] = record["tags"]
    item, nested = find_item(block, kind, slug)
    incomplete: list[str] = []
    path = rule_class_path(slug)
    if item is not None and item.get("file"):
        path = str(item["file"])
    category = category_of(slug)
    if path is not None:
        entry["category"] = "file"
        entry["path"] = path
    elif category is not None:
        entry["category"] = category
    else:
        entry["category"] = "unknown"
        incomplete.append("category")
    if item is None:
        incomplete.append("then")
    else:
        _lift_item(entry, item, kind, nested, incomplete)
    if (
        kind == "create"
        and entry["category"] in CATEGORIES
        and page_exists(project_dir, entry["category"], slug)
    ):
        entry["exists"] = True
    if kind == "defer" and entry["category"] in CATEGORIES:
        entry["exists"] = page_exists(project_dir, entry["category"], slug)
    if incomplete:
        entry["incomplete"] = incomplete
    return entry


def _lift_item(entry: dict, item: dict, kind: str, nested: str | None, incomplete: list[str]):
    if kind == "create":
        skipped = ("slug", "sections", "estimate", "file", "parent_create", "parent_tags")
        if nested != "estimate" and entry.get("category") != "estimates":
            skipped += DERIVED_KEYS  # the Estimate's keys stay off the target (case 72.3)
        fields = {k: v for k, v in item.items() if k not in skipped}
        if nested == "estimate" or entry.get("category") == "estimates":
            fields.setdefault("type", "estimate")
            for key in ("context", "criterion", "method"):  # sections either way (case 53.3)
                if key in fields:
                    entry.setdefault("sections", {})[key.capitalize()] = fields.pop(key)
        if nested == "estimate":
            if "parent_create" in item and not entry.get("ref"):
                entry["ref"] = item["parent_create"]
            if item.get("parent_tags") and not entry.get("tags") and not fields.get("tags"):
                fields["tags"] = list(item["parent_tags"])
        entry["fields"] = fields
        if item.get("sections"):
            entry.setdefault("sections", {}).update(item["sections"])
        if item.get("tags") and not entry.get("tags"):
            entry["tags"] = list(item["tags"])
        category = entry.get("category")
        needed = REQUIRED.get(category, ())
        present = (
            set(fields)
            | set(entry.get("sections") or {})
            | ({"tags"} if entry.get("tags") else set())
        )
        present |= {k.lower() for k in entry.get("sections") or {}}
        for name in needed:
            if name not in present and name.capitalize() not in (entry.get("sections") or {}):
                incomplete.append(name)
        if (
            category == "rules"
            and fields.get("kind") == "Leaf"
            and not (entry.get("ref") or fields.get("parent"))
        ):
            incomplete.append("parent")
    elif kind == "update":
        for key in ("set", "sections", "replace", "change"):
            if item.get(key) is not None:
                entry[key] = item[key]
        if "change" not in item:
            incomplete.append("change")
    elif kind == "defer":
        fields = {k: v for k, v in item.items() if k not in ("slug", "file")}
        entry["fields"] = fields
        if "purpose" not in fields:
            incomplete.append("purpose")
    else:  # delete
        if item.get("impact") is not None:
            entry["impact"] = item["impact"]
        if item.get("change") is not None:
            entry["change"] = item["change"]


# --- the derived Estimate (case 72.3) -----------------------------------------------


def derived_slug(slug: str) -> str:
    """`estimate-<target minus its prefix>`: `rule-x` → `estimate-x`."""
    for prefix in PREFIXES:
        if slug.startswith(prefix):
            return "estimate-" + slug[len(prefix) :]
    return "estimate-" + slug


def criterion_block(case: str, texts: dict[str, str]) -> str:
    """The `### case N` block of an Estimate's Criterion: the Case's `when` and `then`
    verbatim, with their operand lines; a missing section is left out, never invented."""
    parts = [f"### case {case}"]
    if "when" in texts:
        parts.append(f"When:\n{texts['when']}")
    if "then" in texts:
        parts.append(f"Then:\n{texts['then']}")
    return "\n\n".join(parts)


def page_estimates(project_dir: Path, category: str, slug: str) -> list[str] | None:
    """The `estimates` field of a live page, None when the page does not exist."""
    path = project_dir / "vault" / "wiki" / category / f"{slug}.md"
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return []
    head, _, _ = text[3:].partition("\n---")
    try:
        front = yaml.safe_load(head)
    except yaml.YAMLError:
        return []
    value = front.get("estimates") if isinstance(front, dict) else None
    return [str(v) for v in value] if isinstance(value, list) else []


def derived_entries(entry: dict, item: dict | None, texts: dict, project_dir: Path) -> list:
    """The entries a decision line yields beside its own: the Estimate's `create` for a
    create with `method`, its `update` for `contract: changed`, a `remove_criterion` for
    a `supersedes`. None has a line of its own."""
    out: list[dict] = []
    base = {k: entry[k] for k in ("line", "text", "case")}
    tail = {k: entry[k] for k in ("origin", "decision")}
    case = entry["case"]
    if item is not None and entry.get("category") in DERIVED_CATEGORIES:
        if entry["kind"] == "create" and item.get("method") is not None:
            derived = {
                **base,
                "kind": "create",
                "slug": item.get("estimate_slug") or derived_slug(entry["slug"]),
                "category": "estimates",
                "ref": entry["slug"],
                **tail,
                "derived": True,
            }
            if entry.get("tags"):
                derived["tags"] = list(entry["tags"])
            derived["fields"] = {"type": "estimate", "kind": item.get("estimate_kind") or "QA"}
            sections = {}
            if "problem" in texts:
                sections["Context"] = texts["problem"]
            sections["Criterion"] = criterion_block(case, texts)
            sections["Method"] = item["method"]
            derived["sections"] = sections
            if page_exists(project_dir, "estimates", derived["slug"]):
                derived["exists"] = True
            missing = [n for n in ("problem", "when", "then") if n not in texts]
            if missing:
                derived["incomplete"] = missing
            out.append(derived)
        elif entry["kind"] == "update" and item.get("contract") == "changed":
            estimates = page_estimates(project_dir, entry["category"], entry["slug"]) or []
            named = item.get("estimate_slug") or (estimates[0] if len(estimates) == 1 else None)
            derived = {
                **base,
                "kind": "update",
                "slug": named,
                "category": "estimates",
                **tail,
                "derived": True,
                "criterion_block": criterion_block(case, texts),
                "set": {"status": "pending"},
            }
            if item.get("method") is not None:
                derived["sections"] = {"Method": item["method"]}
            derived["change"] = f"criterion: case {case} added"
            missing = [n for n in ("when", "then") if n not in texts]
            if named is None:  # none to take, or a choice the item did not make (case 90.1)
                missing.append("estimate")
            if missing:
                derived["incomplete"] = missing
            out.append(derived)
    if entry.get("supersedes"):
        removed = entry["supersedes"]
        out.append(
            {
                **base,
                "kind": "remove_criterion",
                "category": "estimates",
                **tail,
                "derived": True,
                "case_removed": removed,
                "change": f"criterion: case {removed} removed",
            }
        )
    return out


def estimate_entry(record: dict, number: int, text: str, date: str) -> dict:
    return {
        "line": number,
        "text": text,
        "kind": "estimate",
        "category": "estimates",
        "slug": record["slug"],
        "status": record["status"],
        "result": record["result"],
        "origin": f"raw/{date}/ledger.md#L{number}",
    }


def lesson_entry(record: dict, number: int, text: str, date: str, project_dir: Path) -> dict:
    entry = {
        "line": number,
        "text": text,
        "kind": "lesson",
        "category": "lessons",
        "slug": record["slug"],
        "origin": f"raw/{date}/ledger.md#L{number}",
        "fields": {"type": "lesson", "kind": record["kind"], "root_cause": record["root_cause"]},
        "sections": {"Trigger": record["trigger"], "Root cause": record["root_cause"]},
    }
    incomplete = []
    if record.get("tags"):
        entry["tags"] = record["tags"]
    else:
        incomplete.append("tags")
    if record.get("source"):
        entry["fields"]["source"] = record["source"]
    elif record["kind"] == "knowledge":
        incomplete.append("source")
    if page_exists(project_dir, "lessons", record["slug"]):
        entry["exists"] = True
    if incomplete:
        entry["incomplete"] = incomplete
    return entry


def fold_estimate(entries: list[dict], record: dict, number: int) -> bool:
    """Fold an estimate line into the create of its page in this yaml; False when none
    is there or the create is already applied. The create remembers the folded line."""
    for entry in entries:
        if entry.get("kind") == "create" and entry.get("slug") == record["slug"]:
            if entry.get("applied"):
                return False
            entry["status"] = record["status"]
            entry["result"] = record["result"]
            entry.setdefault("folded", []).append(number)
            return True
    return False


def mark_superseded(entries: list[dict], decisions: list[dict], case: str, by: str) -> None:
    for entry in entries:
        if entry.get("case") == case and entry.get("kind") in DECISION_KINDS:
            entry["superseded_by"] = by
    for decision in decisions:
        if decision.get("case") == case:
            done = decision.setdefault("superseded_by", [])
            if f"decision-case-{by}" not in done:
                done.append(f"decision-case-{by}")


def decision_record(
    case: str,
    entries_of_case: list[dict],
    date: str,
    texts: dict,
    block_errors,
    spec: str | None = None,
):
    targets = []
    tags: list[str] = []
    supersedes: list[str] = []
    criterion: list[dict] = []
    for entry in entries_of_case:
        if entry.get("derived"):  # the Estimate a Case shaped, named under criterion (72.3)
            if entry.get("slug"):
                criterion.append({"estimate": entry["slug"], "case": case})
            continue
        target = {"kind": entry["kind"], "category": entry["category"], "slug": entry["slug"]}
        if entry.get("category") == "file":
            target["path"] = entry.get("path")
        for key in ("ref", "source"):
            if entry.get(key):
                target[key] = entry[key]
        targets.append(target)
        for tag in entry.get("tags") or []:
            if tag not in tags:
                tags.append(tag)
        if entry.get("supersedes") and f"decision-case-{entry['supersedes']}" not in supersedes:
            supersedes.append(f"decision-case-{entry['supersedes']}")
    record = {
        "case": case,
        "decision": f"decision-case-{case}",
        "origin": f"raw/{date}/ledger.md#case-{case}",
        "targets": targets,
        "tags": tags,
        "case_text": texts,
    }
    if spec is not None:
        record["spec"] = spec
    if criterion:
        record["criterion"] = criterion
    if supersedes:
        record["supersedes"] = supersedes
    needed = ("context", "problem")
    if any(e.get("kind") != "defer" for e in entries_of_case):  # the short form of Retro (56)
        needed += ("given", "when")
    missing = [name for name in needed if name not in texts]
    if missing or block_errors:
        record["incomplete"] = missing + list(block_errors)
    return record


# --- assembly -----------------------------------------------------------------------


def sprint_id(project_dir: Path) -> str:
    path = project_dir / "vault" / "wiki" / "sprint.md"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                return line[3:].split(" ", 1)[0].strip()
    return "unknown"


def assemble(project_dir: Path, date: str, existing: dict | None, stderr) -> tuple[dict, int]:
    raw = project_dir / "vault" / "raw" / date
    ledger_path = raw / "ledger.md"
    if not ledger_path.exists():
        raise MaterializeError(f"{ledger_path.relative_to(project_dir).as_posix()} does not exist")
    ledger = ledger_path.read_text(encoding="utf-8").splitlines()
    cases, spec_of = read_specs(project_dir, date)
    data = existing or {
        "date": date,
        "sprint": sprint_id(project_dir),
        "ledger": f"vault/raw/{date}/ledger.md",
        "spec": [],
        "entries": [],
        "decisions": [],
        "unparsed": [],
    }
    data["spec"] = [p.relative_to(project_dir).as_posix() for p in spec_files(project_dir, date)]
    texts_of: dict[str, dict] = {}
    entries: list[dict] = data.setdefault("entries", [])
    decisions: list[dict] = data.setdefault("decisions", [])
    unparsed: list[dict] = data.setdefault("unparsed", [])
    known = {e["line"]: e for e in entries if "line" in e}  # the librarian's own entries have none
    folded = {n for e in entries for n in e.get("folded") or []}
    known_unparsed = {u["line"] for u in unparsed} | folded
    blocks: dict[str, tuple[dict, list[str]]] = {}
    added = 0
    for number, line in enumerate(ledger, start=1):
        if not line.startswith("- "):
            continue
        text = line_body(line)
        if number in known:
            if known[number].get("text") != text:
                print(
                    f"materialize: line {number} changed since the yaml was written; entry left alone",
                    file=stderr,
                )
            continue
        if number in known_unparsed:
            continue
        record = parse_line(line)
        if record is None:
            unparsed.append({"line": number, "text": text})
            continue
        if record["record"] == "estimate":
            if fold_estimate(entries, record, number):
                added += 1
                continue
            entries.append(estimate_entry(record, number, text, date))
            added += 1
            continue
        if record["record"] == "lesson":
            entries.append(lesson_entry(record, number, text, date, project_dir))
            added += 1
            continue
        case = record["case"]
        if case not in blocks:
            blocks[case] = then_blocks(cases.get(case, []))
        block, errors = blocks[case]
        entry = decision_entry(record, number, text, date, block, project_dir)
        if errors and "then" in (entry.get("incomplete") or []):
            entry["incomplete"] = [e for e in entry["incomplete"] if e != "then"] + errors
        entries.append(entry)
        added += 1
        item, nested = find_item(block, record["kind"], record["slug"])
        if case not in texts_of:
            texts_of[case] = case_texts(cases, case)
        for derived in derived_entries(
            entry, None if nested else item, texts_of[case], project_dir
        ):
            entries.append(derived)  # no line of its own (case 72.3)
            added += 1
        if record.get("supersedes"):
            mark_superseded(entries, decisions, record["supersedes"], case)
    # new_tags: from the then block of every Case of the Spec, lines or none (case 61)
    for case, lines in cases.items():
        if case not in blocks:
            blocks[case] = then_blocks(lines)
        for tag in blocks[case][0].get("new_tags") or []:
            if isinstance(tag, dict) and tag not in data.setdefault("new_tags", []):
                data["new_tags"].append(tag)
    # decisions: one per case, from the entries of that case
    by_case: dict[str, list[dict]] = {}
    for entry in entries:
        if entry.get("kind") in DECISION_KINDS and "case" in entry:  # not the librarian's
            by_case.setdefault(entry["case"], []).append(entry)
    present = {d["case"]: d for d in decisions}
    for case, group in by_case.items():
        block, errors = blocks.get(case) or then_blocks(cases.get(case, []))
        if case not in texts_of:
            texts_of[case] = case_texts(cases, case)
        record = decision_record(case, group, date, texts_of[case], errors, spec_of.get(case))
        if case in present:
            present[case]["targets"] = record["targets"]
            present[case]["tags"] = record["tags"]
            for key in ("supersedes", "criterion", "spec"):
                if key in record:
                    present[case][key] = record[key]
        else:
            decisions.append(record)
            present[case] = record
    for decision in decisions:
        for earlier in decision.get("supersedes") or []:
            target = present.get(earlier[len("decision-case-") :])
            if target is not None:
                done = target.setdefault("superseded_by", [])
                if decision["decision"] not in done:
                    done.append(decision["decision"])
    return data, added


def yaml_path(project_dir: Path, date: str) -> Path:
    return project_dir / "vault" / "raw" / date / "materialize.yaml"


def load_yaml(path: Path) -> dict | None:
    if not path.exists():
        return None
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else None


def yaml_text(data: dict) -> str:
    return yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=100)


def dump_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml_text(data), encoding="utf-8", newline="\n")


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi materialize", description=__doc__.split("\n\n")[1])
    p.add_argument("--date", default=None, help="one raw/<date> folder; without it, every date")
    p.add_argument(
        "--show",
        action="store_true",
        help="print the yaml each date would be written with; write nothing (case 76)",
    )
    return p


def dates_with(project_dir: Path, name: str) -> list[str]:
    """Every `vault/raw/<date>/` that holds `name`, in date order."""
    raw = project_dir / "vault" / "raw"
    if not raw.is_dir():
        return []
    return sorted(p.name for p in raw.iterdir() if p.is_dir() and (p / name).is_file())


def materialize_date(project_dir: Path, date: str, now, stdout, stderr, show=False) -> int:
    """One date: extend or write its yaml; one line on stdout, exit 1 on an error. With
    `show` the yaml goes to stdout instead and no file changes (case 76)."""
    try:
        path = yaml_path(project_dir, date)
        existing = load_yaml(path)
        data, added = assemble(project_dir, date, existing, stderr)
        if show:
            stdout.write(yaml_text(data))
            return 0
        dump_yaml(path, data)
    except MaterializeError as exc:
        print(f"materialize: {exc}", file=stderr)
        return 1
    except Exception as exc:  # noqa: BLE001 — report, never traceback
        print(f"materialize: materialize.yaml not written: {exc}", file=stderr)
        return 1
    verb = "extended with" if existing else "written with"
    print(
        f"materialize: {path.relative_to(project_dir).as_posix()} {verb} {added} entries",
        file=stdout,
    )
    return 0


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        args = parser().parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code not in (None, 0) else 0
    dates = [args.date] if args.date else dates_with(project_dir, "ledger.md")
    if not dates:
        print("materialize: no vault/raw/<date>/ledger.md to read", file=stderr)
        return 1
    for index, date in enumerate(dates):
        if args.show and index:
            print("---", file=stdout)  # one yaml document per date (case 76)
        code = materialize_date(project_dir, date, now, stdout, stderr, show=args.show)
        if code:
            return code
    return 0
