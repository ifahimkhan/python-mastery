"""
=====================================================================
 LESSON 06.4 - Inheritance and composition
=====================================================================
 GOAL   : Build a subclass that reuses and overrides its parent with
          super(), check types with isinstance, read the MRO, and know
          when composition ("has a") beats inheritance ("is a").
 RUN    : uv run python -m course.l06_oop.lesson04_inheritance.inheritance
 OUTPUT :
          Bob earns 4000.00 a month
          Ann earns 10500.00 a month
          Cy earns 1000.00 a month
          isinstance(ann, Manager): True
          isinstance(ann, Employee): True
          type(ann) is Employee: False
          issubclass(Intern, Employee): True
          Manager MRO: ['Manager', 'Employee', 'object']
          D().hello(): B then C then A
          D MRO: ['D', 'B', 'C', 'A', 'object']
          Mini: 136 hp engine: vroom
 NEXT   : lesson05_abc_protocol/abc_protocol.py
=====================================================================
"""

MONTHS_PER_YEAR = 12


# -- 1. CONCEPT: a subclass IS A more specific kind of its parent --------
class Employee:
    def __init__(self, name: str, salary: int) -> None:
        self.name = name
        self.salary = salary

    def monthly_pay(self) -> float:
        return self.salary / MONTHS_PER_YEAR

    def describe(self) -> str:
        # Calls self.monthly_pay(): a subclass's version wins if it has one.
        return f"{self.name} earns {self.monthly_pay():.2f} a month"


class Manager(Employee):
    def __init__(self, name: str, salary: int, bonus: int) -> None:
        super().__init__(name, salary)  # let the parent set name and salary
        self.bonus = bonus

    # OVERRIDE: same name, new behaviour, built on the parent's answer.
    def monthly_pay(self) -> float:
        return super().monthly_pay() + self.bonus


class Intern(Employee):
    pass  # inherits everything unchanged


# -- 2. CONCEPT: the MRO decides which method runs -----------------------
class A:
    def hello(self) -> str:
        return "A"


class B(A):
    def hello(self) -> str:
        return "B then " + super().hello()


class C(A):
    def hello(self) -> str:
        return "C then " + super().hello()


class D(B, C):
    pass


# -- 3. CONCEPT: composition, an object that HAS other objects -----------
class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower = horsepower

    def start(self) -> str:
        return f"{self.horsepower} hp engine: vroom"


class Car:
    def __init__(self, model: str, engine: Engine) -> None:
        self.model = model
        self.engine = engine  # a Car HAS an Engine; it is not an Engine

    def start(self) -> str:
        return f"{self.model}: {self.engine.start()}"  # delegate to the part


def main() -> None:
    staff = [Employee("Bob", 48_000), Manager("Ann", 120_000, 500), Intern("Cy", 12_000)]
    for person in staff:  # one loop, each object answers in its own way
        print(person.describe())

    ann = staff[1]
    print("isinstance(ann, Manager):", isinstance(ann, Manager))
    print("isinstance(ann, Employee):", isinstance(ann, Employee))
    print("type(ann) is Employee:", type(ann) is Employee)
    print("issubclass(Intern, Employee):", issubclass(Intern, Employee))
    print("Manager MRO:", [cls.__name__ for cls in Manager.__mro__])

    print("D().hello():", D().hello())
    print("D MRO:", [cls.__name__ for cls in D.__mro__])

    print(Car("Mini", Engine(136)).start())

    # -- 4. WHY --------------------------------------------------------
    # Inheritance shares code between things that truly ARE a kind of each
    # other: a Manager is an Employee. Code written for Employee works for
    # every subclass (describe() above). For "uses a" / "has a" relations,
    # prefer composition: you can swap the Engine without touching Car.

    # -- 5. PITFALL: forgetting super().__init__ -----------------------
    # class Manager(Employee):
    #     def __init__(self, name, salary, bonus): self.bonus = bonus
    # Manager("Ann", 1, 2).describe()
    # AttributeError: 'Manager' object has no attribute 'name'
    #
    # Deep trees (Animal > Mammal > Dog > Puppy > ...) get hard to change.
    # Keep hierarchies shallow.

    # -- 6. TRY IT -----------------------------------------------------
    # a) Give Intern a describe() that adds " (intern)" using super().describe().
    # b) Swap D(B, C) to D(C, B). Predict D().hello() before you run it.
    # c) Add an ElectricEngine with its own start() and give it to a Car.


if __name__ == "__main__":
    main()
