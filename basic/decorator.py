import functools
import time


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result

    return wrapper


@timeit
def slow_func(num: int) -> int:
    time.sleep(1)
    return sum(range(num))


print(slow_func(1000_000))
