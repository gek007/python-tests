from pathlib import Path

# def add_user(name: str, tags=None):
#     if tags is None:
#         tags = []
#     tags.append(name)
#     return tags


# print(add_user("John", ["tag1", "tag2"]))
# print(add_user("Jane"))

# ========================

# def create_multipliers():
#     multipliers = []
#     for i in range(3):
#         def multiply(x, i=i):
#             return x * i
#         multipliers.append(multiply)
#     return multipliers

# funcs = create_multipliers()
# print(funcs[0](10))  # What prints?
# print(funcs[1](10))  # What prints?
# print(funcs[2](10))  # What prints?


# =========================


# class User:
#     def __init__(self, user_id, name):
#         self.user_id = user_id
#         self.name = name

#     def __eq__(self, other):
#         if not isinstance(other, User):
#             return False
#         return self.user_id == other.user_id

#     def __hash__(self):
#         return hash(self.user_id)  # ✅ Hash based on same field as __eq__


# # SET (now works correctly)
# users = {User(1, "Alice"), User(1, "Bob"), User(2, "Charlie")}
# print(len(users))  # 2 ✅ Correct! (user_id 1 is same, 2 is different)

# # DICT (now works correctly)
# users_dict = {User(1, "Alice"): "admin"}
# users_dict[User(1, "Bob")] = "user"  # ← Overwrites previous value
# print(len(users_dict))  # 1 ✅ Correct! Same user_id = same key
# print(users_dict[User(1, "Charlie")])  # "user" ✅ Retrieves correctly


# ========================

# def func(a, b, c):
#     return a + b + c

# args = (1, 2, 3)
# print(func(*args))  # Unpacks to: func(1, 2, 3)

# =========================


# def proc(data: dict):
#     if data is None:
#         return
#     print(data)


# proc(None)
# proc({"a": 1, "b": 2, "c": 3})


# def func1(value: int, data=None):
#     if data is None:
#         data = []
#     data.append(value)
#     return data

# print(func1(1))
# print(func1(5, [1, 2, 3]))

# ========================


# def func2(a, b, c):
#     sum = a + b + c
#     if sum:
#         return "a" * sum
#     return None


# func2(1, 2, 3)

# =========================


# class MyClass:
#     _instance = None

#     @classmethod
#     def get_instance(cls):
#         if cls._instance is None:
#             cls._instance = cls()
#         return cls._instance


# instance1 = MyClass.get_instance()
# instance2 = MyClass.get_instance()

# print(instance1 is instance2)


# # ========================= singleton pattern

# class MyClass2:
#     _instance = None

#     @classmethod
#     def get_instance(cls):
#         if cls._instance is None:
#             cls._instance = cls()
#         return cls._instance


# =====================

# val = None

# if val is None:
#     print("val is None")
# else:
#     print("val is not None")

# result = 0

# if result:
#     print("result is not None")
# else:
#     print("result is None")


# ============


# def func(a, b, c):
#     return a + b + c

# args = (1, 2, 3)
# func(*args)
# func(1,2,3)


# kwargs = {'a': 1, 'b': 2, 'c': 3}
# func(**kwargs)
# func(a=1, b=2, c=3)

# =========

# data = {'a': 1, 'b': 2, 'c': 3}

# for key in data:
#     if key == 'b':
#         del data[key]

# print(data)


# for k in data.copy():
#     if k == 'c':
#         del data[k]

# print(data)

# =====================

# data = {'a': 1, 'b': 2, 'c': 3}


# for key in data:
#     data[key] *= 3

# print(data)  # ✅ {'a': 2, 'b': 4, 'c': 6}


# for key in data.copy():
#     data['new_key'] = 99

# print(data)  #


# data2 ={"a": 1, "b": 2, "c": 3}

# for key in data2.copy():
#     if key == 'b':
#         del data2[key]

# print(data2)

# =====================

# data = {'a': 1, 'b': 2, 'c': 3}

# # Modify values
# # data = {key: value * 2 for key, value in data.items()}
# # print(data)  # {'a': 2, 'b': 4, 'c': 6} ✅


# data = {key: value * 3 for key, value in data.items()}
# print(data)

# def process_dict(data: dict) -> dict:
#     keys_to_remove = [key for key in data.keys() if key == 'b']
#     for key in keys_to_remove:
#         del data[key]
#     return data

# def process_dict2(data: dict) -> dict:
#     for key in data.copy():
#         if key == 'b':
#             del data[key]
#     return data

# print(process_dict({"a": 1, "b": 2, "c": 3}))
# print(process_dict2({"a": 1, "b": 2, "c": 3}))


# ===============

# original = [[1, 2], [3, 4]]
# shallow = original.copy()  # ← Shallow copy (top-level only)

# shallow[0][0] = 99

# print(f"original: {original}")    # [[99, 2], [3, 4]] ❌ CHANGED!
# print(f"shallow: {shallow}")      # [[99, 2], [3, 4]]

# ===========

# import copy

# original = [[1, 2], [3, 4]]
# deep = copy.deepcopy(original)  # ← Deep copy (recursive)

# deep[0][0] = 88

# print(f"original: {original}")    # [[1, 2], [3, 4]] ✅ Unchanged
# print(f"deep: {deep}")            # [[88, 2], [3, 4]]


# deep2 = [row[:] for row in original]

# =============

# import copy

# def change_list(lst):
#     new_lst = lst.copy()
#     new_lst.append(4)
#     new_lst[0] = 100
#     return new_lst


# my_list = [1, 2, 3]
# new_list = change_list(my_list)
# print(new_list)
# print(my_list)

# depp = copy.deepcopy(my_list)

# =============


# def get_number(max: int) :
#     return [num for num in range(max)]

# print(get_number(10))


# def gen_number(max: int) :
#     for num in range(max):
#         yield num

# for num in gen_number(10):
#     print(num)

# print(list(gen_number(10)))

# =============

# import time

# # List approach
# start = time.time()
# result1 = sum([i * 2 for i in range(1_000_000)])
# time_list = time.time() - start

# # Generator approach
# start = time.time()
# result2 = sum(i * 2 for i in range(1_000_000))
# time_gen = time.time() - start

# ============
#
# =


# # def get_number():
# #     for num in range(10):
# #         yield num


# # lst = get_number()

# # num_list = list(lst)
# # print(num_list)

# # # =============


# # def get_number():
# #     for num in range(10):
# #         yield num


# # lst = get_number()
# # num_list = list(lst)
# # print(num_list)


# # def process_large_file(filename):
# #     def process_line(line):
# #         return line.strip()

# #     with open(filename) as f:
# #         for line in f:
#             yield process_line(line)

# =============

# class MyClass:
#     def __new__(cls):
#         print("__new__ called")
#         return super().__new__(cls)

#     def __init__(self):
#         print("__init__ called")

# obj = MyClass()


# class MyClass2:
#     _instance  = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance

#     def __init__(self):
#         print("__init__ called")

# obj2 = MyClass2()
# obj3 = MyClass2()

# print(obj2 is obj3)

# =============

cur_path = Path(__file__).parent
file_path = cur_path / "test.txt"


def process_file(file_path):
    def handle_line(line):
        return line.strip()

    with open(file_path, "r+", encoding="utf-8") as file:
        for line in file:
            yield handle_line(line)


for line in process_file(file_path):
    print(line)
