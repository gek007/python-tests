from dataclasses import dataclass


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


person = Person(name="John", age=30, email="john@example.com")
person.say_hello()


person2 = Person.create(person)
person2.say_hello()

res = Person.add_age(10, person.age)
print(f"The new age is {res}")
