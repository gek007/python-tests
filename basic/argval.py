my_dic = {
    "name": "Kostya",
    "age": "57",
    "email": "kostya.shilkrot@gmail.com",
    "messages": ["Hello", "Hi", "Goodbye"],
}


def my_func(**kwargs):
    name = kwargs.get("name", "No name")
    age = kwargs.get("age", "No age")
    email = kwargs.get("email", "No email")
    messages = kwargs.get("messages", [])
    print(f"Name: {name}, Age: {age}, Email: {email}, Messages: {messages}")


def my_func2(name: str, **kwargs):
    name = name
    age = kwargs.get("age", "No age")
    email = kwargs.get("email", "No email")
    messages = kwargs.get("messages", [])
    print(f"Name: {name}, Age: {age}, Email: {email}, Messages: {messages}")


my_func(**my_dic)
my_func2(
    "Kostya",
    age=57,
    email="kostya.shilkrot@gmail.com",
    messages=["Hello", "Hi", "Goodbye"],
)
print(my_dic)
