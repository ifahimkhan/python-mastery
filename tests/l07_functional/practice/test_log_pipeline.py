import itertools
from collections.abc import Iterator

import pytest

from course.l07_functional.practice.log_pipeline.log_pipeline import (
    SAMPLE_LOG,
    Entry,
    Level,
    at_least,
    count_by_service,
    parse,
    parse_line,
    per_minute,
    read_lines,
)


def _entry(time: str, level: Level, service: str = "api") -> Entry:
    return Entry(time, level, service, "msg")


def test_read_lines_skips_blank_lines_and_strips() -> None:
    assert list(read_lines("  a \n\n b\n   \n")) == ["a", "b"]


def test_parse_line_reads_every_field() -> None:
    entry = parse_line("09:00:07 WARNING db slow query (812 ms)")
    assert entry == Entry("09:00:07", Level.WARNING, "db", "slow query (812 ms)")


@pytest.mark.parametrize("line", ["garbage", "09:00 INFO", "09:00:01 LOUD api hi", ""])
def test_parse_line_rejects_malformed_lines(line: str) -> None:
    assert parse_line(line) is None


def test_parse_skips_bad_lines() -> None:
    entries = list(parse(read_lines(SAMPLE_LOG)))
    assert len(entries) == 9
    assert all(isinstance(entry, Entry) for entry in entries)


def test_stages_are_lazy() -> None:
    def endless() -> Iterator[str]:
        for second in itertools.count():
            yield f"10:00:{second % 60:02d} ERROR api boom"

    first_two = list(itertools.islice(at_least(Level.ERROR, parse(endless())), 2))
    assert [entry.time for entry in first_two] == ["10:00:00", "10:00:01"]


def test_at_least_keeps_the_level_and_above() -> None:
    entries = [_entry("1", level) for level in Level]
    kept = [entry.level for entry in at_least(Level.WARNING, entries)]
    assert kept == [Level.WARNING, Level.ERROR, Level.CRITICAL]


def test_count_by_service() -> None:
    entries = [
        _entry("1", Level.INFO, "db"),
        _entry("2", Level.INFO, "db"),
        _entry("3", Level.INFO),
    ]
    assert count_by_service(entries).most_common() == [("db", 2), ("api", 1)]


def test_per_minute_groups_consecutive_minutes() -> None:
    entries = [_entry(time, Level.ERROR) for time in ("09:00:01", "09:00:59", "09:05:00")]
    assert per_minute(entries) == {"09:00": 2, "09:05": 1}
    assert per_minute([]) == {}
