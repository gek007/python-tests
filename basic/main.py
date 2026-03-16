def add(a: int, b: int) -> int:
    if type(a) != int or type(b) != int:
        raise ValueError("a and b must be integers")
    return a + b


def long_list(lst: list[int]) -> int:
    return sum(lst)


def my_func(dic: dict[str, str]) -> list[str]:
    return list(dic.values())

my_list = list[int] = [1,2,3,4,5]

print(my_list[-1])

my_list[::-1]
my_list[1:3]


res =[x**2 for x in range(10)]
print(res)

res2 =[x for x in range(10) if x % 2 == 0]
print(res2)


def read_f(f: filename) -> str:
    data: str = None   
    with open(f, "w") as file:
        file.write(data)




def write_f(f: filename, data: str) -> None:
    with open(f, "w") as file:
        file.write(data)

def append_f(f: filename, data: str) -> None:
    with open(f, "a") as file:
        file.write(data)


rng=range(10)
print(list(rng))

rng2 = range(10, 20, 2)
print(list(rng2))

rng3 = range(10, 20, 2)
print(list(rng3))


my_num = [1,6,2,7,3,8,4,9,5,10]

my_num2 = sorted(my_num, reverse=True)
print(my_num2)



