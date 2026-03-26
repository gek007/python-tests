def add_item(item: str, items=None) -> list[str]:
    if items is None:
        items = []

    items.append(item)
    return items


print(add_item("apple"))  # ["apple"]
print(add_item("banana"))  # ["banana"]
print(add_item("cherry"))  # ["cherry"]

# --------------------------------

functions = []

for i in range(5):
    def fn(i=i):
        return i

    functions.append(fn)

results = [f() for f in functions]
print(results)

# --------------------------------


import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(10_000):
        with lock:
          counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()

print(counter)   # Expected: 100000, Actual: ~75000 (random each run!)


# ============


def process(status):
    if status == "active":
        return "Processing..."
    elif status == "inactive":
        return "Skipped"
    return "Unknown"

print(process("active"))     # Expected: "Processing...", Actual: "Unknown" ✗
print(process("inactive"))   # Expected: "Skipped",       Actual: "Unknown" ✗


# --------------------------------


# Task #1 — Valid Parentheses
# Write a function is_valid(s) that takes a string containing only (), [], {} and returns True 
# if the brackets are correctly matched and nested, False otherwise.

def is_valid(s: str) -> bool:
    stack = []
    bracket_map = {")": "(", "]": "[", "}": "{"}


    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else "#"
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


is_valid("{[]}")     

#------------------------

#Task #4 — Top K Frequent Elements
#Write a function top_k_frequent(nums, k) that returns the k most frequent elements in a list.
# pythontop_k_frequent([1,1,1,2,2,3], k=2)   # [1, 2]

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    frequency_map = {} # dict[int, int]

    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    return sorted(frequency_map.keys(), key=lambda x: frequency_map[x], reverse=True)[:k]

print(top_k_frequent([1,1,1,2,2,3], k=2))   # [1, 2]

#------------------------


