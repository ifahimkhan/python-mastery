"""Reads the OUTPUT block from a lesson's header docstring.

See docs/CONVENTIONS.md for the header format. The OUTPUT block starts on the
line after "OUTPUT :" and ends at the next header label or "=====" ruler.
"""

import ast
import re
from pathlib import Path

LABELS = ("GOAL", "RUN", "OUTPUT", "NEXT", "NEW", "DESIGN", "EXTEND", "NOTE")
_ANY_LABEL = re.compile(rf"^\s*({'|'.join(LABELS)})\s*:")
_OUTPUT_LABEL = re.compile(r"^\s*OUTPUT\s*:(?P<rest>.*)$")
_RULER = re.compile(r"^\s*={5,}\s*$")


class HeaderError(ValueError):
    """The lesson header doesn't follow docs/CONVENTIONS.md."""


def expected_output(source: str, name: str = "<lesson>") -> list[str] | None:
    """Returns the expected stdout lines, or None when the lesson opts out.

    A lesson opts out with text in parentheses on the OUTPUT line itself,
    e.g. ``OUTPUT : (example session: you type 7)``.
    """
    docstring = ast.get_docstring(ast.parse(source), clean=False)
    if docstring is None:
        raise HeaderError(f"{name} has no module docstring header")

    lines = docstring.splitlines()
    start = next((i for i, line in enumerate(lines) if _OUTPUT_LABEL.match(line)), None)
    if start is None:
        raise HeaderError(f"{name} has no 'OUTPUT :' line in its header")

    match = _OUTPUT_LABEL.match(lines[start])
    assert match is not None
    same_line = match.group("rest").strip()
    if same_line.startswith("("):
        return None
    if same_line:
        raise HeaderError(f"{name}: OUTPUT opt-out text must start with '(', was: {same_line}")

    body: list[str] = []
    for line in lines[start + 1 :]:
        if _ANY_LABEL.match(line) or _RULER.match(line):
            break
        body.append(line.rstrip())

    indents = [len(line) - len(line.lstrip()) for line in body if line.strip()]
    indent = min(indents, default=0)
    result = [line[indent:] for line in body]
    while result and not result[-1].strip():
        result.pop()
    return result


def expected_output_of(path: Path) -> list[str] | None:
    return expected_output(path.read_text(encoding="utf-8"), name=str(path))
