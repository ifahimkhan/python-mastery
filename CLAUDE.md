# python-mastery: notes for Claude

Hands-on Python course repo (sister of `kotlin-mastery`). Learners use PyCharm + uv on Windows/macOS/Linux.

**Read first:** [docs/CONVENTIONS.md](docs/CONVENTIONS.md). It is the source of truth for
layout, lesson headers, exercises and style. Don't restate it here; update it there.

## Commands

```bash
uv sync                                  # install
uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest
uv run pytest -m exercise tests/lNN_x    # every exercise test must FAIL with a hint until solved
uv run python -m course.<level>.<lesson>.<module>
```

## Build plan (one phase per level)

| Phase | Content |
|------:|---------|
| 0 | Scaffold: pyproject, CI, start.py, docs, lesson output test, exercise selection rule ✅ |
| 1-12 | Levels 01-12 (topics in README levels table) |
| 13 | Capstones: library CLI (JSON file), weather aggregator (httpx + Open-Meteo, fake source in tests), asyncio task scheduler |

Capstone folder shape: `README.md` (brief, milestones M1..Mn), `contract.py` (Protocol),
`starter/` (NotImplementedError), `reference/`, `main.py`. Acceptance tests grouped per milestone
class; reference tests run by default, starter tests marked `exercise`.

Per level, in order: lessons -> level README -> `tasks.py` -> solutions -> exercises ->
contract tests -> practice + tests -> ROADMAP entries -> README status. Then run all checks,
confirm exercise tests fail with hints, review hints/determinism/forward references/ASCII output.

**Stop after each phase**, summarise, suggest commit message `feat: add level NN <topic>`,
and wait for the user's OK. Never weaken a test to make it pass.
