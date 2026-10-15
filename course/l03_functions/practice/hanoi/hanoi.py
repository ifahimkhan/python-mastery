"""
=====================================================================
 PRACTICE 03.C - Towers of Hanoi
=====================================================================
 GOAL   : Solve a famous puzzle with a three-line recursive function.
          Move all disks from peg A to peg C, one disk at a time, never
          putting a bigger disk on a smaller one.
 RUN    : uv run python -m course.l03_functions.practice.hanoi.hanoi
 OUTPUT :
          Moving 3 disks from A to C:
          disk 1: A -> C
          disk 2: A -> B
          disk 1: C -> B
          disk 3: A -> C
          disk 1: B -> A
          disk 2: B -> C
          disk 1: A -> C
          7 moves (2 ** 3 - 1 = 7)
          64 disks would need 18446744073709551615 moves.
 DESIGN : solve() returns the move count and prints moves through a
          `report` function it receives. Tests pass their own function
          to collect the moves instead of printing them.
 NEW    : The trick: to move n disks from A to C, move n - 1 disks out
          of the way to B, move the biggest disk to C, then move the
          n - 1 disks from B onto it. The two smaller jobs are the SAME
          puzzle with one disk fewer: recursion.
 EXTEND : Count the moves with a formula instead of solving: 2 ** n - 1.
=====================================================================
"""

from collections.abc import Callable

DISKS = 3
LEGEND_DISKS = 64

Report = Callable[[int, str, str], None]  # a name for a type (level 08)


def print_move(disk: int, source: str, target: str) -> None:
    print(f"disk {disk}: {source} -> {target}")


def solve(disks: int, source: str, target: str, spare: str, report: Report) -> int:
    """Moves ``disks`` disks from source to target and returns how many moves it took."""
    if disks == 0:
        return 0  # base case: nothing to move
    moves = solve(disks - 1, source, spare, target, report)  # clear the way
    report(disks, source, target)  # move the biggest disk
    moves += 1
    moves += solve(disks - 1, spare, target, source, report)  # stack the rest on top
    return moves


def main() -> None:
    print(f"Moving {DISKS} disks from A to C:")
    moves = solve(DISKS, "A", "C", "B", print_move)
    print(f"{moves} moves (2 ** {DISKS} - 1 = {2**DISKS - 1})")
    print(f"{LEGEND_DISKS} disks would need {2**LEGEND_DISKS - 1} moves.")


if __name__ == "__main__":
    main()
