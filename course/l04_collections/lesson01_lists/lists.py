"""
=====================================================================
 LESSON 04.1 - Lists
=====================================================================
 GOAL   : Store items in order, read and change them, add and remove
          items, and sort lists the right way.
 RUN    : uv run python -m course.l04_collections.lesson01_lists.lists
 OUTPUT :
          fruits: ['apple', 'banana', 'cherry']
          first: apple last: cherry len: 3
          slice [0:2]: ['apple', 'banana']
          after change: ['apple', 'blueberry', 'cherry']
          append: ['apple', 'blueberry', 'cherry', 'date']
          insert: ['avocado', 'apple', 'blueberry', 'cherry', 'date']
          extend: ['avocado', 'apple', 'blueberry', 'cherry', 'date', 'fig', 'grape']
          remove('apple'): ['avocado', 'blueberry', 'cherry', 'date', 'fig', 'grape']
          pop() -> grape, left: ['avocado', 'blueberry', 'cherry', 'date', 'fig']
          pop(0) -> avocado, left: ['blueberry', 'cherry', 'date', 'fig']
          'cherry' in fruits: True  index: 1
          sorted copy: [1, 2, 5, 9]  original: [5, 2, 9, 1]
          sorted in place: [1, 2, 5, 9]
          reverse=True: [9, 5, 2, 1]
          by length: ['kiwi', 'apple', 'banana']
          min 1 max 9 sum 17
          grid[1][2] = 6
          list('abc') = ['a', 'b', 'c']
          split -> ['a', 'b', 'c'] -> join -> a-b-c
 NEXT   : lesson02_tuples/tuples.py
=====================================================================
"""


def main() -> None:
    # -- 1. CONCEPT: a list is an ordered, changeable sequence -----------
    # Square brackets, items separated by commas. Indexes and slices work
    # exactly like on strings (lesson 01.4).
    fruits = ["apple", "banana", "cherry"]
    print("fruits:", fruits)
    print("first:", fruits[0], "last:", fruits[-1], "len:", len(fruits))
    print("slice [0:2]:", fruits[0:2])

    # -- 2. CONCEPT: lists are MUTABLE -----------------------------------
    # Unlike strings, you can change a list in place.
    fruits[1] = "blueberry"
    print("after change:", fruits)

    # -- 3. CONCEPT: adding and removing ---------------------------------
    fruits.append("date")  # add one item at the end
    print("append:", fruits)
    fruits.insert(0, "avocado")  # add at a position
    print("insert:", fruits)
    fruits.extend(["fig", "grape"])  # add every item of another list
    print("extend:", fruits)
    fruits.remove("apple")  # remove the first item equal to "apple"
    print("remove('apple'):", fruits)
    last = fruits.pop()  # remove and return the last item
    print(f"pop() -> {last}, left: {fruits}")
    first = fruits.pop(0)  # remove and return the item at index 0
    print(f"pop(0) -> {first}, left: {fruits}")
    print("'cherry' in fruits:", "cherry" in fruits, " index:", fruits.index("cherry"))

    # -- 4. CONCEPT: sorting -------------------------------------------
    # sorted(x) returns a NEW sorted list; x.sort() sorts x itself and returns None.
    numbers = [5, 2, 9, 1]
    print("sorted copy:", sorted(numbers), " original:", numbers)
    numbers.sort()
    print("sorted in place:", numbers)
    print("reverse=True:", sorted(numbers, reverse=True))
    # key= is a function applied to each item; items are sorted by its result.
    print("by length:", sorted(["banana", "kiwi", "apple"], key=len))
    print("min", min(numbers), "max", max(numbers), "sum", sum(numbers))

    # A list can hold anything, even other lists: a grid.
    grid = [[1, 2, 3], [4, 5, 6]]
    print("grid[1][2] =", grid[1][2])  # row 1, column 2

    print("list('abc') =", list("abc"))
    csv_line = "a,b,c"
    letters = csv_line.split(",")
    print("split ->", letters, "-> join ->", "-".join(letters))

    # -- 5. WHY: lists are Python's everyday container -----------------
    # Use a list when order matters and items get added or removed.
    # Usually all items have the same type: list[str], list[int].

    # -- 6. PITFALL: methods that change the list return None ------------
    #   numbers = numbers.sort()   # numbers is now None!
    #   fruits = fruits.append("x")  # same mistake
    # And indexes must exist:
    #   [1, 2, 3][3]               # IndexError: list index out of range
    #   [1, 2].remove(7)           # ValueError: list.remove(x): x not in list
    #   [].pop()                   # IndexError: pop from empty list

    # -- 7. TRY IT -----------------------------------------------------
    # a) Make a list of 5 numbers, then print the 3 largest with sorted() and a slice.
    # b) Remove every "x" from ["x", "a", "x", "b"] with a while loop and remove().
    # c) Sort ["Banana", "apple", "Cherry"]. Why is "apple" last? Try key=str.lower.


if __name__ == "__main__":
    main()
