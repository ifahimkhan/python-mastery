"""
=====================================================================
 LESSON 04.7 - The collections module
=====================================================================
 GOAL   : Use Counter, defaultdict, deque and namedtuple: ready-made
          containers for counting, grouping, queues and small records.
 RUN    : uv run python -m course.l04_collections.lesson07_collections_module.collections_module
 OUTPUT :
          Counter: Counter({'a': 3, 'n': 2, 'b': 1})
          most common 2: [('a', 3), ('n', 2)]
          count of 'z': 0
          word counts: [('the', 3), ('cat', 2)]
          grouped: {3: ['cat', 'dog'], 5: ['horse', 'zebra'], 4: ['bird']}
          queue: deque(['first', 'second', 'third'])
          served: first, waiting: deque(['second', 'third'])
          last 3 readings: deque([3, 4, 5], maxlen=3)
          Point(x=3, y=4)  x = 3  distance: 5.0
          moved: Point(x=10, y=4)  original: Point(x=3, y=4)
 NOTE   : For records, @dataclass(frozen=True) (level 06) is usually the
          better choice; namedtuple is common in older code and the stdlib.
 NEXT   : practice/word_stats/word_stats.py
=====================================================================
"""

import math
from collections import Counter, defaultdict, deque
from typing import NamedTuple

READINGS_KEPT = 3


class Point(NamedTuple):
    """A tuple whose items also have names. Immutable, like any tuple."""

    x: int
    y: int


def main() -> None:
    # -- 1. CONCEPT: Counter counts hashable things -----------------------
    letters = Counter("banana")
    print("Counter:", letters)
    print("most common 2:", letters.most_common(2))
    print("count of 'z':", letters["z"])  # a missing key counts as 0, no KeyError

    sentence = "the cat saw the other cat near the door"
    words = sentence.split()
    print("word counts:", Counter(words).most_common(2))

    # -- 2. CONCEPT: defaultdict creates missing values for you -----------
    # defaultdict(list): a missing key starts as an empty list.
    by_length: defaultdict[int, list[str]] = defaultdict(list)
    for animal in ["cat", "horse", "dog", "zebra", "bird"]:
        by_length[len(animal)].append(animal)
    print("grouped:", dict(by_length))

    # -- 3. CONCEPT: deque, a fast double-ended queue -----------------------
    # Adding/removing at BOTH ends is instant. (list.pop(0) has to shift
    # every other item, which gets slow for long lists.)
    queue = deque(["first", "second"])
    queue.append("third")
    print("queue:", queue)
    served = queue.popleft()
    print(f"served: {served}, waiting: {queue}")

    # maxlen keeps only the newest items: perfect for "the last N".
    recent: deque[int] = deque(maxlen=READINGS_KEPT)
    for reading in [1, 2, 3, 4, 5]:
        recent.append(reading)
    print("last 3 readings:", recent)

    # -- 4. CONCEPT: NamedTuple, a tuple with field names ------------------
    p = Point(3, 4)
    print(p, " x =", p.x, " distance:", math.hypot(p.x, p.y))
    moved = p._replace(x=10)  # a NEW Point; the original can't change
    print("moved:", moved, " original:", p)

    # -- 5. WHY: don't rebuild what the standard library has -------------
    # Counter replaces the "get(key, 0) + 1" loop, defaultdict replaces
    # setdefault, deque replaces slow list.pop(0). They are tested,
    # fast, and every Python programmer recognises them.

    # -- 6. PITFALL: defaultdict creates keys just by LOOKING -------------
    #   by_length[99]         # no error, but now 99 -> [] is in the dict!
    # Use `99 in by_length` or by_length.get(99) to check without adding.

    # -- 7. TRY IT -----------------------------------------------------
    # a) Which letter is most common in "mississippi"?
    # b) Group ["apple", "bean", "avocado", "corn"] by first letter with defaultdict.
    # c) Make a NamedTuple Book(title, year) and sort three books by year.


if __name__ == "__main__":
    main()
