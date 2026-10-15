"""
=====================================================================
 LESSON 04.3 - Dictionaries
=====================================================================
 GOAL   : Look values up by key, add, change and remove entries, loop
          over keys and values, and count things with a dict.
 RUN    : uv run python -m course.l04_collections.lesson03_dicts.dicts
 OUTPUT :
          ages: {'Ada': 36, 'Linus': 54}
          ages['Ada'] = 36
          get('Grace') = None  get('Grace', 0) = 0
          'Linus' in ages: True
          after add and change: {'Ada': 37, 'Linus': 54, 'Grace': 85}
          pop('Linus') -> 54, left: {'Ada': 37, 'Grace': 85}
          keys: ['Ada', 'Grace']
          values: [37, 85]
          Ada -> 37
          Grace -> 85
          merged: {'Ada': 37, 'Grace': 85, 'Alan': 41}
          letter counts: {'b': 1, 'a': 3, 'n': 2}
          by first letter: {'a': ['apple', 'avocado'], 'b': ['banana']}
          oldest: Grace
          prices sorted by value: [('pen', 1.5), ('book', 12.0), ('bag', 30.0)]
 NEXT   : lesson04_sets/sets.py
=====================================================================
"""


def value_of(pair: tuple[str, float]) -> float:
    return pair[1]


def main() -> None:
    # -- 1. CONCEPT: key -> value -----------------------------------------
    # Curly braces with key: value pairs. Keys are unique and must be
    # hashable (str, int, tuple, ...). Since Python 3.7 a dict keeps the
    # order in which keys were inserted.
    ages = {"Ada": 36, "Linus": 54}
    print("ages:", ages)
    print("ages['Ada'] =", ages["Ada"])
    # get() returns None (or your default) instead of crashing on a missing key.
    print("get('Grace') =", ages.get("Grace"), " get('Grace', 0) =", ages.get("Grace", 0))
    print("'Linus' in ages:", "Linus" in ages)  # `in` checks the KEYS

    # -- 2. CONCEPT: add, change, remove ---------------------------------
    ages["Grace"] = 85  # new key: added
    ages["Ada"] = 37  # existing key: value replaced
    print("after add and change:", ages)
    removed = ages.pop("Linus")
    print(f"pop('Linus') -> {removed}, left: {ages}")

    # -- 3. CONCEPT: looping ---------------------------------------------
    print("keys:", list(ages.keys()))
    print("values:", list(ages.values()))
    for name, age in ages.items():  # items() gives (key, value) tuples
        print(name, "->", age)

    # | merges two dicts into a NEW dict; on equal keys the right side wins.
    print("merged:", ages | {"Alan": 41})

    # -- 4. CONCEPT: counting and grouping -------------------------------
    counts: dict[str, int] = {}
    for letter in "banana":
        counts[letter] = counts.get(letter, 0) + 1
    print("letter counts:", counts)

    groups: dict[str, list[str]] = {}
    for word in ["apple", "banana", "avocado"]:
        groups.setdefault(word[0], []).append(word)  # create the list on first use
    print("by first letter:", groups)
    # (lesson 04.7 shows Counter and defaultdict, which make both even shorter.)

    # key= works with max/min/sorted on dicts too:
    # value_of (top of the file) picks the value out of a (key, value) pair.
    oldest_name, _ = max(ages.items(), key=value_of)
    print("oldest:", oldest_name)
    prices = {"book": 12.0, "pen": 1.5, "bag": 30.0}
    print("prices sorted by value:", sorted(prices.items(), key=value_of))

    # -- 5. WHY: lookups by key are instant ------------------------------
    # Finding a name in a list checks items one by one. A dict jumps
    # straight to the key, however many entries it has. Use a dict
    # whenever you look things up by a name or an id.

    # -- 6. PITFALL: missing keys and unhashable keys --------------------
    #   ages["Bob"]              # KeyError: 'Bob'
    #   {["a"]: 1}               # TypeError: unhashable type: 'list'
    # And never add or remove keys while looping over the same dict:
    #   for key in ages: del ages[key]
    #   # RuntimeError: dictionary changed size during iteration

    # -- 7. TRY IT -----------------------------------------------------
    # a) Count the words in "the cat and the hat" with get().
    # b) Build a dict from two lists with dict(zip(names, ages)). What does zip do?
    # c) Print the youngest person with min() and key=.


if __name__ == "__main__":
    main()
