"""Shared checks for Level 06.

Subclasses decide WHICH implementation is tested: the learner's exercises
or the reference solutions.
"""

import dataclasses

import pytest

from course.l06_oop.tasks import Light, OopTasks, Shape


class _Square:
    """Not related to Shape at all: it only HAS an area() method."""

    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side**2


class OopContract:
    tasks: OopTasks  # set by the subclass

    def test_ex1_counter_counts_and_resets(self) -> None:
        counter = self.tasks.make_counter(10)
        assert counter.value == 10
        counter.increment()
        counter.increment(5)
        assert counter.value == 16, "Hint: increment(step=1) adds step to self.value"
        counter.reset()
        assert counter.value == 10, "Hint: remember `start` in __init__ so reset() can use it"

    def test_ex1_counters_are_independent(self) -> None:
        first = self.tasks.make_counter(0)
        second = self.tasks.make_counter(0)
        first.increment()
        assert second.value == 0, "Hint: set self.value in __init__, not as a class attribute"

    def test_ex2_temperature_converts(self) -> None:
        temperature = self.tasks.make_temperature(100)
        assert temperature.celsius == 100
        assert temperature.fahrenheit == pytest.approx(212)
        temperature.celsius = -40
        assert temperature.fahrenheit == pytest.approx(-40), "Hint: compute it, don't store it"

    def test_ex2_temperature_rejects_absolute_zero_breaches(self) -> None:
        temperature = self.tasks.make_temperature(20)
        with pytest.raises(ValueError, match="below absolute zero: -300"):
            temperature.celsius = -300
        assert temperature.celsius == 20, "Hint: check BEFORE storing the new value"
        with pytest.raises(ValueError, match="below absolute zero"):
            self.tasks.make_temperature(-274)

    def test_ex2_fahrenheit_is_read_only(self) -> None:
        temperature = self.tasks.make_temperature(0)
        with pytest.raises(AttributeError):
            setattr(temperature, "fahrenheit", 50)  # noqa: B010 - mypy would refuse the plain form

    def test_ex3_vector_repr(self) -> None:
        assert repr(self.tasks.make_vector(1, 2)) == "Vector(1, 2)", "Hint: write __repr__"
        assert repr(self.tasks.make_vector(-3, 0)) == "Vector(-3, 0)"

    def test_ex3_vectors_compare_by_value(self) -> None:
        assert self.tasks.make_vector(1, 2) == self.tasks.make_vector(1, 2), "Hint: write __eq__"
        assert self.tasks.make_vector(1, 2) != self.tasks.make_vector(2, 1)
        as_tuple: object = (1, 2)
        assert self.tasks.make_vector(1, 2) != as_tuple, "Hint: return NotImplemented for others"

    def test_ex3_vectors_work_in_sets(self) -> None:
        vectors = {self.tasks.make_vector(1, 2), self.tasks.make_vector(1, 2)}
        assert len(vectors) == 1, "Hint: __hash__ must hash the same fields as __eq__"

    def test_ex4_playlist_len_and_in(self) -> None:
        playlist = self.tasks.make_playlist("Road trip", ["Africa", "Hey Ya", "Roxanne"])
        assert len(playlist) == 3, "Hint: write __len__"
        assert "Hey Ya" in playlist, "Hint: write __contains__"
        assert "Yesterday" not in playlist

    def test_ex4_playlist_str_and_truth(self) -> None:
        assert str(self.tasks.make_playlist("Mix", ["a", "b"])) == "Mix (2 songs)"
        assert str(self.tasks.make_playlist("Solo", ["a"])) == "Solo (1 song)", "Hint: singular"
        assert str(self.tasks.make_playlist("Empty", [])) == "Empty (0 songs)"
        assert not self.tasks.make_playlist("Empty", []), "Hint: bool() falls back to __len__"

    def test_ex4_playlist_keeps_its_own_copy(self) -> None:
        songs = ["a"]
        playlist = self.tasks.make_playlist("Mix", songs)
        songs.append("b")
        assert len(playlist) == 1, "Hint: store tuple(songs), not the caller's list"

    def test_ex5_employee(self) -> None:
        bob = self.tasks.make_employee("Bob", 48_000)
        assert bob.monthly_pay() == pytest.approx(4000)
        assert bob.describe() == "Bob earns 4000.00 a month"

    def test_ex5_manager_overrides_monthly_pay(self) -> None:
        ann = self.tasks.make_manager("Ann", 120_000, 500)
        assert ann.monthly_pay() == pytest.approx(10_500), "Hint: super().monthly_pay() + bonus"
        assert ann.describe() == "Ann earns 10500.00 a month", (
            "Hint: describe() calls self.monthly_pay(), so the override is used"
        )

    def test_ex5_manager_is_a_subclass_of_employee(self) -> None:
        employee = self.tasks.make_employee("Bob", 1)
        manager = self.tasks.make_manager("Ann", 1, 1)
        assert type(manager) is not type(employee), "Hint: Manager is its own class"
        assert isinstance(manager, type(employee)), "Hint: class Manager(Employee)"

    def test_ex6_circle(self) -> None:
        circle = self.tasks.make_circle(1)
        assert isinstance(circle, Shape), "Hint: class Circle(Shape)"
        assert circle.describe() == "Circle with area 3.14", "Hint: name the class Circle"
        assert self.tasks.make_circle(2).area() == pytest.approx(12.566, abs=0.001)
        assert self.tasks.make_circle(0).area() == 0

    def test_ex6_circle_rejects_a_negative_radius(self) -> None:
        self.tasks.make_circle(1)
        with pytest.raises(ValueError):
            self.tasks.make_circle(-1)

    def test_ex7_largest_works_on_any_object_with_area(self) -> None:
        small, big = _Square(1), _Square(3)
        assert self.tasks.largest([small, big, _Square(2)]) is big

    def test_ex7_largest_edge_cases(self) -> None:
        first, second = _Square(2), _Square(2)
        assert self.tasks.largest([first, second]) is first, "On a tie, the first one wins"
        assert self.tasks.largest([]) is None, "No shapes: None"

    def test_ex8_book_is_a_frozen_dataclass(self) -> None:
        book = self.tasks.make_book("Dune", "Frank Herbert", 1965)
        assert repr(book) == "Book(title='Dune', author='Frank Herbert', year=1965)"
        assert book == self.tasks.make_book("Dune", "Frank Herbert", 1965)
        assert len({book, self.tasks.make_book("Dune", "Frank Herbert", 1965)}) == 1
        with pytest.raises(dataclasses.FrozenInstanceError):
            setattr(book, "year", 2000)  # noqa: B010 - mypy would refuse the plain form

    def test_ex8_book_rejects_an_empty_title(self) -> None:
        self.tasks.make_book("Dune", "Frank Herbert", 1965)
        with pytest.raises(ValueError):
            self.tasks.make_book("", "Nobody", 2000)

    def test_ex9_with_year_returns_a_new_book(self) -> None:
        book = self.tasks.make_book("Dune", "Frank Herbert", 1965)
        newer = book.with_year(2021)
        assert (newer.title, newer.author, newer.year) == ("Dune", "Frank Herbert", 2021)
        assert book.year == 1965, "Hint: dataclasses.replace() builds a copy"

    def test_ex10_parse_light(self) -> None:
        assert self.tasks.parse_light("red") is Light.RED
        assert self.tasks.parse_light(" Green ") is Light.GREEN, "Hint: strip() and lower()"
        with pytest.raises(ValueError):
            self.tasks.parse_light("blue")

    def test_ex10_next_light_cycles(self) -> None:
        light = Light.RED
        seen = []
        for _ in range(4):
            seen.append(light)
            light = self.tasks.next_light(light)
        assert seen == [Light.RED, Light.GREEN, Light.YELLOW, Light.RED]
