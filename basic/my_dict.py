import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from classes_methods.my_person import Person  # noqa: E402

people = [Person("John", 30), Person("Jane", 25), Person("Jim", 35)]

people_dict = {person.name: person for person in people}
print(people_dict)

# ========================

men = [
    ("Haim", 25, "Haim@example.com"),
    ("John", 30, "John@example.com"),
    ("Jane", 25, "Jane@example.com"),
    ("Jim", 35, "Jim@example.com"),
]

for ind in range(len(men)):
    print(men[ind])

friends = [
    ("Haim", 25, "Haim@example.com"),
    ("John", 30, "John@example.com"),
    ("Jane", 25, "Jane@example.com"),
    ("Jim", 35, "Jim@example.com"),
]

friends_dict = {age: email for name, age, email in friends}
print(friends_dict)
