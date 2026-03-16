from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class Person:
    name: str
    age: int
    email: str


person = Person(name="John", age=30, email="john@example.com")
print(person)


class Person2(BaseModel):
    name: str
    age: int
    email: str


person2 = Person2(name="Mike", age=40, email="mike@example.com")
print(person2)

# class to dict  
res = person2.model_dump()
print(res)

res = person2.model_dump_json()
print(res)


@dataclass
class Car:
    brand: str
    model: str
    year: int


class Car2(BaseModel):
    brand: str
    model: str
    year: int

