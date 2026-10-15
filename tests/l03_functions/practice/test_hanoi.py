import pytest

from course.l03_functions.practice.hanoi.hanoi import solve


def _collect(disks: int) -> tuple[int, list[tuple[int, str, str]]]:
    moves: list[tuple[int, str, str]] = []

    def record(disk: int, source: str, target: str) -> None:
        moves.append((disk, source, target))

    count = solve(disks, "A", "C", "B", record)
    return count, moves


@pytest.mark.parametrize("disks", range(0, 9))
def test_needs_two_to_the_n_minus_one_moves(disks: int) -> None:
    count, moves = _collect(disks)
    assert count == 2**disks - 1
    assert len(moves) == count


def test_three_disks_follow_the_classic_solution() -> None:
    _, moves = _collect(3)
    assert moves == [
        (1, "A", "C"),
        (2, "A", "B"),
        (1, "C", "B"),
        (3, "A", "C"),
        (1, "B", "A"),
        (2, "B", "C"),
        (1, "A", "C"),
    ]


@pytest.mark.parametrize("disks", range(1, 8))
def test_never_puts_a_bigger_disk_on_a_smaller_one(disks: int) -> None:
    pegs = {"A": list(range(disks, 0, -1)), "B": [], "C": []}
    _, moves = _collect(disks)
    for disk, source, target in moves:
        assert pegs[source][-1] == disk, "can only move the top disk"
        assert not pegs[target] or pegs[target][-1] > disk, "bigger disk on a smaller one"
        pegs[target].append(pegs[source].pop())
    assert pegs["C"] == list(range(disks, 0, -1)), "all disks end on C, in order"
