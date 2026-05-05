from tenacity import retry, stop_after_attempt, wait_exponential
import random

count = 0

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=15))
def make_retry():
    global count
    count += 1

    print(f"attempting ... {count}")
    num = random.randint(0, 10)
    if num > 2:
        print(f"raising exception ... {num}")
        raise Exception("Random number is less than 5")
    return "Success"



make_retry()
