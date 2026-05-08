import time
from contextlib import contextmanager


@contextmanager
def observe(name):
    print(f"Starting {name}...")
    start = time.time()

    yield

    elapsed = time.time() - start
    print(f"{name}: elapsed time: {elapsed:.2f}s")


with observe("my_func"):
    time.sleep(1)
    print("Hello, World!")
