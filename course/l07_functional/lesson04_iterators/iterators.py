"""
=====================================================================
 LESSON 07.4 - Iterators
=====================================================================
 GOAL   : See what a for loop really does (iter + next + StopIteration),
          tell an iterable from an iterator, and write your own
          iterator class.
 RUN    : uv run python -m course.l07_functional.lesson04_iterators.iterators
 OUTPUT :
          next: a b c
          StopIteration: the iterator is used up
          next with a default: done
          Countdown(3): [3, 2, 1]
            for loop got 2
            for loop got 1
          first pass: [3, 2, 1]
          second pass: [] (already exhausted)
          iterable, pass 1: ['intro', 'outro']
          iterable, pass 2: ['intro', 'outro']
          4 in squares? True then [9] (`in` used some up!)
 NEXT   : lesson05_generators/generators.py
=====================================================================
"""

from collections.abc import Iterator


# -- 2. CONCEPT: an iterator class needs __iter__ and __next__ -----------
class Countdown:
    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self) -> "Countdown":
        return self  # an iterator is its own iterator

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration  # "no more items": for loops stop quietly
        value = self.current
        self.current -= 1
        return value


# An ITERABLE (not an iterator): every iter() call starts a fresh walk.
class Playlist:
    def __init__(self, *songs: str) -> None:
        self.songs = songs

    def __iter__(self) -> Iterator[str]:
        return iter(self.songs)


def main() -> None:
    # -- 1. CONCEPT: what `for` does behind the scenes --------------------
    letters = ["a", "b", "c"]
    it = iter(letters)  # ask the iterable for an iterator
    print("next:", next(it), next(it), next(it))
    try:
        next(it)
    except StopIteration:
        print("StopIteration: the iterator is used up")
    print("next with a default:", next(it, "done"))

    # A for loop is roughly:
    #   it = iter(letters)
    #   while True:
    #       try: item = next(it)
    #       except StopIteration: break
    #       ...body...

    print("Countdown(3):", list(Countdown(3)))
    for number in Countdown(2):
        print("  for loop got", number)

    # -- 3. PITFALL: an iterator can only be walked ONCE ------------------
    countdown = Countdown(3)
    print("first pass:", list(countdown))
    print("second pass:", list(countdown), "(already exhausted)")

    playlist = Playlist("intro", "outro")
    print("iterable, pass 1:", list(playlist))
    print("iterable, pass 2:", list(playlist))

    squares = map(lambda n: n * n, [1, 2, 3])  # map, filter, zip, enumerate: iterators
    print("4 in squares?", 4 in squares, "then", list(squares), "(`in` used some up!)")

    # -- 4. WHY ------------------------------------------------------------
    # Iterators produce items ONE AT A TIME, on demand. A for loop over a
    # 10 GB file or an endless stream works without loading it all.
    # Anything with __iter__ works in for, list(), sum(), sorted(), `in`...

    # -- 5. TRY IT -----------------------------------------------------
    # a) Make Countdown(start, step=1) count down by `step`.
    # b) Call zip on two iterators of different lengths. When does it stop?
    # c) Turn Countdown into an iterable (like Playlist) so it can be reused.


if __name__ == "__main__":
    main()
