import json
from dataclasses import asdict, dataclass


@dataclass
class Person:
    name: str
    age: int
    email: str
    is_active: bool


event = {"body": '{"productName":"Test Product","quantity":3}'}
print(type(event))
print(type(event["body"]))
order_details = json.loads(event["body"])
print(type(order_details))
print(order_details)


json_str = '{"name": "John", "age": 30, "email": "john@example.com", "is_active": true}'
print(type(json_str))
data_dict = json.loads(json_str)
print(type(data_dict))
person = Person(**data_dict)
print(person)
dic1 = asdict(person)
print(type(dic1))
print(dic1)


my_dict = {"name": "John", "age": 30, "email": "john@example.com"}
dic_str = json.dumps(my_dict)
print(type(dic_str))
print(dic_str)
