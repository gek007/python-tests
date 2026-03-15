def my_func(dic: dict[str, str])-> list[str]:
    return list(dic.values())
    

res = my_func({"a": "1", "b": "2", "c": "3"})
print(res)


def my_func2(lst: list[int])-> int:
    return sum(lst)


res2 = my_func2([1, 2, 3])
print(res2)

my_l: list[str] = ["a", "b", "c"]
my_d: dict[str, int] = {"a": 1, "b": 2, "c": 3}

print(my_l)
print(my_d)

names:list[str] = []
ages:dict[str, int] = {}

ages['Jone'] = 50
ages['Haim'] = 45

names.append("Hohn")
names.append("Haim")
names.append("Moishe")

print(ages)
print(names)

x = [el for el in range(10)]
print(x)

