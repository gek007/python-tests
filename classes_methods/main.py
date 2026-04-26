from dataclasses import dataclass
from pathlib import Path


# instance methods
@dataclass
class Person:
    name: str
    age: int
    email: str

    def say_hello(self) -> None:
        print(f"Hello, my name is {self.name}")

    @classmethod
    def create(cls, person: "Person") -> "Person":
        return cls(name=person.name, age=person.age, email=person.email)

    @staticmethod
    def add_age(years: int, age: int) -> int:
        age += years
        return age

    def func_with_args(*args, **kwargs) -> None:
        print(args)
        print(kwargs)


person = Person(name="John", age=30, email="john@example.com")
person.say_hello()


person2 = Person.create(person)
person2.say_hello()

res = Person.add_age(10, person.age)
print(f"The new age is {res}")


person.func_with_args(
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, name="John", age=30, email="john@example.com"
)


@dataclass
class Peope(Person):
    country: str

    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age}, email={self.email}, country={self.country})"


peope = Peope(name="John", age=30, email="john@example.com", country="Israel")
print(peope)


_ROOT = Path(__file__).resolve().parent
data_file = _ROOT / "data" / "data.txt"
print(data_file.read_text())

