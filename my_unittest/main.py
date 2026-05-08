from unittest.mock import MagicMock

obj = MagicMock()
obj.a.b.c.d.e.f.return_value = "Hello"

print(
    "obj.a.b.c.d.e.f.return value = ",
    obj.a.b.c.d.e.f.return_value,
)
