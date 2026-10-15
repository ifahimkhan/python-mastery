"""
=====================================================================
 LESSON 07.6 - itertools
=====================================================================
 GOAL   : Use the standard toolbox for iterators: slice, chain, group,
          accumulate, pair up, batch and combine, all lazily.
 RUN    : uv run python -m course.l07_functional.lesson06_itertools.itertools_tour
 OUTPUT :
          count + islice: [10, 15, 20, 25]
          cycle: ['A', 'B', 'A', 'B', 'A']
          repeat: ['-', '-', '-']
          chain: [1, 2, 3, 4, 5]
          pairwise: [(1, 4), (4, 9), (9, 16)]
          batched: [('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]
          zip_longest: [('a', 'x'), ('b', 'y'), ('-', 'z')]
          accumulate (running total): [3, 8, 10, 17]
          accumulate max: [3, 5, 5, 7]
          accumulate product: [3, 15, 30, 210]
          takewhile < 6: [3, 5, 2]
          dropwhile < 6: [7]
          product: ['A1', 'A2', 'B1', 'B2']
          permutations: ['AB', 'AC', 'BA', 'BC', 'CA', 'CB']
          combinations: ['AB', 'AC', 'AD', 'BC', 'BD', 'CD']
          groupby unsorted: {'a': ['asp'], 'b': ['bee', 'bat'], 'c': ['cow']} (ant and ape lost!)
          groupby sorted: {'a': ['ant', 'ape', 'asp'], 'b': ['bee', 'bat'], 'c': ['cow']}
 NEXT   : lesson07_functools/functools_tour.py
=====================================================================
"""

import itertools
import operator

SALES = [("mon", 3), ("tue", 5), ("wed", 2), ("thu", 7)]
WORDS = ["ant", "ape", "bee", "bat", "cow", "asp"]


def main() -> None:
    # -- 1. CONCEPT: endless and slicing ---------------------------------
    print("count + islice:", list(itertools.islice(itertools.count(10, 5), 4)))
    print("cycle:", list(itertools.islice(itertools.cycle("AB"), 5)))
    print("repeat:", list(itertools.repeat("-", 3)))

    # -- 2. CONCEPT: joining and splitting streams ------------------------
    print("chain:", list(itertools.chain([1, 2], (3,), range(4, 6))))
    print("pairwise:", list(itertools.pairwise([1, 4, 9, 16])))
    print("batched:", list(itertools.batched("ABCDEFG", 3)))
    print("zip_longest:", list(itertools.zip_longest("ab", "xyz", fillvalue="-")))

    # -- 3. CONCEPT: running totals and conditions ------------------------
    amounts = [amount for _, amount in SALES]
    print("accumulate (running total):", list(itertools.accumulate(amounts)))
    print("accumulate max:", list(itertools.accumulate(amounts, max)))
    print("accumulate product:", list(itertools.accumulate(amounts, operator.mul)))
    print("takewhile < 6:", list(itertools.takewhile(lambda n: n < 6, amounts)))
    print("dropwhile < 6:", list(itertools.dropwhile(lambda n: n < 6, amounts)))

    # -- 4. CONCEPT: combinatorics ----------------------------------------
    print("product:", ["".join(pair) for pair in itertools.product("AB", "12")])
    print("permutations:", ["".join(p) for p in itertools.permutations("ABC", 2)])
    print("combinations:", ["".join(c) for c in itertools.combinations("ABCD", 2)])

    # -- 5. PITFALL: groupby only groups NEIGHBOURS -------------------------
    first_letter = operator.itemgetter(0)  # same as lambda word: word[0]
    unsorted = {key: list(group) for key, group in itertools.groupby(WORDS, first_letter)}
    print("groupby unsorted:", unsorted, "(ant and ape lost!)")
    ordered = sorted(WORDS, key=first_letter)
    grouped = {key: list(group) for key, group in itertools.groupby(ordered, first_letter)}
    print("groupby sorted:", grouped)

    # -- 6. WHY ------------------------------------------------------------
    # These tools are fast (written in C), lazy, and well known: a reader
    # sees `pairwise` and knows what happens, where a hand-written index
    # loop must be read line by line.

    # -- 7. TRY IT -----------------------------------------------------
    # a) Use pairwise on the sales amounts to print each day's change.
    # b) How many 3-letter codes can you build from "ABCDE"
    #    with product(..., repeat=3)? With permutations(..., 3)?
    # c) Group the numbers 1..20 into "even" and "odd" with groupby.


if __name__ == "__main__":
    main()
