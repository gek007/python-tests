class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"

    def __eq__(self, other: "Person") -> bool:
        return self.name == other.name and self.age == other.age
