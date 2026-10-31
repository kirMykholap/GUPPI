"""`guppi links <slug or path>` and `guppi links --write` — the graph of the links between the
vault pages and the harness files (case 967).

A node is a live page of `vault/wiki/`, a file that `guppi render` writes, or a path that a
path field of a page names. A page links out by:

- each slug of its `LINK_FIELDS` and each `[[slug]]` of its body outside a code span, as
  `links_of` of `.guppi/guppi/lint.py` reads them from the page with its `## History` left out;
- each path of `REWORD_PATH_FIELDS` of `.guppi/guppi/generate.py` — `implementation_ref`,
  `governs` and `code_ref`;
- each slug of a live page that its body names outside `## History`, in a code span or not.

A rendered file links out by each name it holds: an agent of `.claude/agents/` anywhere, a
skill of `.claude/skills/` after a slash, alone in a code span or in a `skills:` list, and a
command of `COMMANDS` of `.guppi/guppi/cli.py` as `guppi <name>`. The name of an agent or a
skill links to the page that renders its file, the name of a command to each page whose
`implementation_ref` names its module. The text of a rendered file is the text `guppi render`
writes — `render_units`, `fill_placeholders` and `plan` of `.guppi/guppi/render.py` — so the
graph does not depend on whether `render --sync` has run.

Each link out of one node is a link into the other, and a file inside a folder that a page
names links into that page. The purpose line of a page is its `purpose`, of a lesson its
`root_cause` and of an insight its `pattern`. No page under `vault/wiki/decisions/` is read or
printed, as `rule-search-leaves-out-decisions` sets it.

`guppi links <slug or path>` prints the block of one node: a line `## <slug or path>`, its
purpose line, then one line per neighbour, `out` or `in`, the kind of link and the neighbour,
with the purpose line of a neighbour that is a page. A slug or path that is neither a live
page nor a file prints one line and exits 1. `guppi links --write`, the `SessionStart` hook of
`rule-link-graph-at-session-start`, writes every block into `.guppi/links.md`, which git
ignores; an error prints one line on stderr, and the hook always exits 0, since a
`SessionStart` hook cannot block (case 967.3). Entity page:
`vault/wiki/entities/entity-link-graph.md`.
"""

import argparse
import re
import sys
from dataclasses import dataclass, field, replace
from pathlib import Path

from guppi.event import project_root
from guppi.generate import REWORD_PATH_FIELDS
from guppi.guard import key, relative
from guppi.lint import links_of
from guppi.pages import CATEGORIES, HISTORY, Page, read_category, wiki_root
from guppi.render import RenderError, fill_placeholders, plan, render_units

OUTPUT = Path(".guppi") / "links.md"
DECISIONS = "vault/wiki/decisions"  # its pages are never read or printed
PURPOSE_FIELD = {"lessons": "root_cause", "insights": "pattern"}  # else `purpose`
SLUG = re.compile(r"(?<![\w-])([a-z][a-z0-9]*(?:-[a-z0-9]+)+)(?![\w-])")
AGENT_FILE = re.compile(r"^\.claude/agents/([^/]+)\.md$")
SKILL_FILE = re.compile(r"^\.claude/skills/([^/]+)/SKILL\.md$")
SKILLS_LIST = re.compile(r"^skills:\s*\[([^\]]*)\]", re.MULTILINE)
COMMAND = re.compile(r"(?<![\w.-])guppi ([a-z][a-z-]*)")  # not the `.guppi` of the project
HEADER = (
    "# Links\n\n"
    "Written by `uv run --project .guppi guppi links --write` at the start of the session; "
    "one block per live page and per file, each neighbour out and in.\n"
)


class LinksError(Exception):
    pass


@dataclass
class Graph:
    pages: dict[str, Page]
    files: dict[str, str]  # key → the path as written
    out: dict[str, set[tuple[str, str]]] = field(default_factory=dict)  # node → (kind, node)
    into: dict[str, set[tuple[str, str]]] = field(default_factory=dict)
    owner: dict[str, str] = field(default_factory=dict)  # file key → the slug that renders it

    def link(self, source: str, kind: str, target: str) -> None:
        if source == target:
            return
        self.out.setdefault(source, set()).add((kind, target))
        self.into.setdefault(target, set()).add((kind, source))


def purpose(page: Page) -> str:
    value = page.props.get(PURPOSE_FIELD.get(page.category, "purpose"))
    return " ".join(str(value).split()) if value else ""


def as_list(value) -> list[str]:
    if value is None:
        return []
    return [str(v) for v in value] if isinstance(value, list) else [str(value)]


def without_history(page: Page) -> Page:
    return replace(page, sections={n: t for n, t in page.sections.items() if n != HISTORY})


def file_node(graph: Graph, path: str) -> str:
    """The node of a path: one spelling per file, the first one written kept for printing."""
    path = Path(path).as_posix()
    graph.files.setdefault(key(path), path)
    return "file:" + key(path)


def command_modules() -> dict[str, str]:
    """`guppi <name>` → the path of the module that carries it. Imported here, not at the top,
    since `cli.py` imports this module."""
    from guppi.cli import COMMANDS

    out = {}
    for name, function in COMMANDS.items():
        module = getattr(function, "__module__", "") or ""
        if module.startswith("guppi."):
            out[name] = ".guppi/guppi/" + module.split(".", 1)[1] + ".py"
    return out


def rendered(project_dir: Path) -> tuple[dict[str, str], dict[str, str]]:
    """The text `guppi render` writes into each file, and the slug of the page that renders
    it — the owner of a `full` file first."""
    units = render_units(read_category(wiki_root(project_dir), "rules"))
    fill_placeholders(units)
    outputs = plan(project_dir, units)
    owner: dict[str, str] = {}
    for unit in sorted(units.values(), key=lambda u: (u.mode != "full", u.page.slug)):
        owner.setdefault(key(unit.governs), unit.page.slug)
    return outputs, owner


def names_in(text: str, agents: dict[str, str], skills: dict[str, str], commands) -> set:
    """`(kind, name)` for each agent, skill and command the text of a rendered file names."""
    found = set()
    for name in agents:
        if re.search(rf"(?<![\w-]){re.escape(name)}(?![\w-])", text):
            found.add(("agent", name))
    listed = {
        n.strip().strip("'\"") for m in SKILLS_LIST.finditer(text) for n in m.group(1).split(",")
    }
    for name in skills:
        word = re.escape(name)
        if (
            name in listed
            or re.search(rf"/{word}(?![\w-])", text)
            or re.search(rf"`/?{word}`", text)
        ):
            found.add(("skill", name))
    for match in COMMAND.finditer(text):
        if match.group(1) in commands:
            found.add(("command", match.group(1)))
    return found


def build(project_dir: Path) -> Graph:
    wiki = wiki_root(project_dir)
    pages = {
        page.slug: page
        for category in CATEGORIES
        if category != "decisions"
        for page in read_category(wiki, category)
        if not page.error
    }
    graph = Graph(pages=pages, files={})
    folders: list[tuple[str, str, str]] = []  # (page slug, field, folder as a key)
    for slug, page in pages.items():
        bare = without_history(page)
        linked = set()
        for kind, target in links_of(bare):
            if target in pages:
                graph.link(slug, kind, target)
                linked.add(target)
        for name in REWORD_PATH_FIELDS:
            for path in as_list(page.props.get(name)):
                graph.link(slug, name, file_node(graph, path))
                if path.endswith("/") or (project_dir / path).is_dir():
                    folders.append((slug, name, key(path)))
        text = "\n".join(bare.sections.values())
        for target in set(SLUG.findall(text)):
            if target in pages and target not in linked:
                graph.link(slug, "name", target)
    outputs, owner = rendered(project_dir)
    graph.owner = owner
    agents = {m.group(1): p for p in outputs if (m := AGENT_FILE.match(Path(p).as_posix()))}
    skills = {m.group(1): p for p in outputs if (m := SKILL_FILE.match(Path(p).as_posix()))}
    modules = command_modules()
    runs = {}  # module key → the pages whose `implementation_ref` names it
    for slug, page in pages.items():
        for path in as_list(page.props.get("implementation_ref")):
            runs.setdefault(key(path), set()).add(slug)
    for path, text in outputs.items():
        node = file_node(graph, path)
        for kind, name in names_in(text, agents, skills, modules):
            if kind == "command":
                targets = runs.get(key(modules[name]), set())
            else:
                target = owner.get(key((agents if kind == "agent" else skills)[name]))
                targets = {target} if target else set()
            for target in targets:
                graph.link(node, f"{kind} {name}", target)
    for file_key in list(graph.files):
        for slug, name, folder in folders:
            if file_key.startswith(folder + key("/")):
                graph.link(slug, name, "file:" + file_key)
    return graph


def node_of(graph: Graph, name: str, project_dir: Path) -> str | None:
    if name in graph.pages:
        return name
    path = relative(name, project_dir)
    if path is None or key(path).startswith(key(DECISIONS) + key("/")):
        return None
    node = "file:" + key(path)
    if key(path) in graph.files:
        return node
    if (project_dir / path).is_file():
        file_node(graph, path)
        for slug, page in graph.pages.items():
            for field_name in REWORD_PATH_FIELDS:
                for named in as_list(page.props.get(field_name)):
                    if key(path).startswith(key(named) + key("/")):
                        graph.link(slug, field_name, node)
        return node
    return None


def label(graph: Graph, node: str) -> str:
    return graph.files[node[5:]] if node.startswith("file:") else node


def purpose_of(graph: Graph, node: str) -> str:
    if node in graph.pages:
        return purpose(graph.pages[node])
    owner = graph.owner.get(node[5:])
    if owner and owner in graph.pages:
        return f"rendered from {owner}: {purpose(graph.pages[owner])}"
    return "a file"


def neighbour(graph: Graph, node: str) -> str:
    if node in graph.pages:
        text = purpose(graph.pages[node])
        return f"{node} — {text}" if text else node
    return label(graph, node)


def block(graph: Graph, node: str) -> str:
    lines = [f"## {label(graph, node)}", "", purpose_of(graph, node), ""]
    for direction, edges in (("out", graph.out), ("in", graph.into)):
        for kind, other in sorted(edges.get(node, ()), key=lambda e: (label(graph, e[1]), e[0])):
            lines.append(f"- {direction} {kind}: {neighbour(graph, other)}")
    return "\n".join(lines).rstrip("\n") + "\n"


def write(graph: Graph, project_dir: Path) -> None:
    nodes = sorted(graph.pages) + sorted(
        ("file:" + k for k in graph.files), key=lambda n: label(graph, n)
    )
    text = HEADER + "".join("\n" + block(graph, node) for node in nodes)
    path = project_dir / OUTPUT
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi links", description=__doc__.split("\n\n")[0])
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("name", nargs="?", help="a slug of a live page or a path of a file")
    mode.add_argument("--write", action="store_true", help=f"write every block into {OUTPUT}")
    return p


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    try:
        args = parser().parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code not in (None, 0) else 0
    if args.write:
        try:
            write(build(project_dir), project_dir)
        except Exception as exc:  # noqa: BLE001 — a SessionStart hook stops no session (case 967.3)
            print(f"links: {OUTPUT.as_posix()} not written: {exc}", file=stderr)
        return 0
    try:
        graph = build(project_dir)
    except RenderError as exc:
        print(f"links: {exc}", file=stderr)
        return 1
    node = node_of(graph, args.name, project_dir)
    if node is None:
        print(f"links: {args.name} is neither a live page nor a file", file=stdout)
        return 1
    stdout.write(block(graph, node))
    return 0
