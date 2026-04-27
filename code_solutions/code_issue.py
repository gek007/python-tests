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
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)  # Expected: 100000, Actual: ~75000 (random each run!)


# ============


def process(status):
    if status == "active":
        return "Processing..."
    elif status == "inactive":
        return "Skipped"
    return "Unknown"


print(process("active"))  # Expected: "Processing...", Actual: "Unknown" ✗
print(process("inactive"))  # Expected: "Skipped",       Actual: "Unknown" ✗


# --------------------------------


# Task #1 — Valid Parentheses
# Write a function is_valid(s) that takes a string containing only (), [], {} and returns True
# if the brackets are correctly matched and nested, False otherwise.

# def is_valid(s: str) -> bool:
#     stack = []
#     bracket_map = {")": "(", "]": "[", "}": "{"}


#     for char in s:
#         if char in bracket_map:
#             top_element = stack.pop() if stack else "#"
#             if bracket_map[char] != top_element:
#                 return False
#         else:
#             stack.append(char)

#     return not stack


# is_valid("{[]}")

# ------------------------

# Task #4 — Top K Frequent Elements
# Write a function top_k_frequent(nums, k) that returns the k most frequent elements in a list.
# pythontop_k_frequent([1,1,1,2,2,3], k=2)   # [1, 2]

# def top_k_frequent(nums: list[int], k: int) -> list[int]:
#     frequency_map = {} # dict[int, int]

#     for num in nums:
#         frequency_map[num] = frequency_map.get(num, 0) + 1
#     return sorted(frequency_map.keys(), key=lambda x: frequency_map[x], reverse=True)[:k]

# print(top_k_frequent([1,1,1,2,2,3], k=2))   # [1, 2]

# ------------------------

# Task #5 — Two Sum (return indices)
# Write a function two_sum(nums, target) that returns the indices of two numbers in a list that add up to the target.

# two_sum([2, 7, 11, 15], target=9)   # [0, 1]
# two_sum([3, 2, 4], target=6)        # [1, 2]
# two_sum([3, 3], target=6)           # [0, 1]

# O(n) time, O(n) space
# Return indices, not values
# Each input has exactly one solution

# def two_sum(nums: list[int], target: int) -> list[int]:
#     my_map: dict[int, int] = {}

#     for i, num in enumerate(nums):
#         if (target - num) in my_map:
#             return [my_map[target - num], i]
#         my_map[num] = i


# print(two_sum([3, 2, 4], target=6))        # [1, 2]


# ============================

# # Task #6 — Reverse a Linked List
# # pythonclass ListNode:

#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# # 1 → 2 → 3 → 4 → 5 → None
# # becomes
# # 5 → 4 → 3 → 2 → 1 → None

# reverse_list(head)   # returns new head (5)


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# def reverse_linked_list(root: ListNode) -> ListNode:
#     prev = None
#     current = root

#     while current:
#         next_temp = current.next
#         current.next = prev
#         prev = current
#         current = next_temp

#     return prev


# ===========

# Count word frequencies in a string, return top k words
# sorted by frequency desc, alphabetically for ties

#
# top_words("the cat sat on the mat the cat", k=2)
# → [("the", 3), ("cat", 2)]


# def count_words(words: list[str], k=2) -> list[dict]:
#     my_map: dict[str, int] = {}

#     for word in words:
#         if my_map.get(word) is None:
#             my_map[word] = 1
#         else:
#             my_map[word] += 1

#     # This line sorts the items in my_map (which are word-frequency pairs)
#     # by frequency descending (item[1], so -item[1]) and then alphabetically (item[0])
#     # Then, it returns only the top k elements from this sorted list
#     return sorted(my_map.items(), key=lambda item: (-item[1], item[0]))[:k]

# =======================


# Return all unique permutations of a string
# def permutations(s: str) -> list[str]:
#     if len(s) <= 1:
#         return [s]

#     result = []
#     for i in range(len(s)):
#         for perm in permutations(s[:i] + s[i + 1 :]):
#             result.append(s[i] + perm)
#     return result


# permutations("abc")  # ["abc","acb","bac","bca","cab","cba"]
# permutations("aab")  # ["aab","aba","baa"]  ← no duplicates!
# permutations("a")  # ["a"]
# permutations("")  # [""]

# ===================

# Task #16 — Implement a Stack Using Queues
# python# Implement a LIFO stack using only queue operations
# push, pop, peek, empty — all must work correctly

# class MyStack:
#     def __init__(self):
#         self.queue = []

#     def push(self, x: int):
#         self.queue.append(x)

#     def pop(self) -> int:
#         return self.queue.pop()

#     def peek(self) -> int:
#         # The peek method returns the element at the top of the stack
#         # Since this stack is implemented using a list as a queue,
#         # the "top" of the stack is the last element in the list,
#         # so we return the last item using -1 index
#         return self.queue[-1]


# ======================

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return isinstance(other, Point) and self.x == other.x and self.y == other.y

#     def __hash__(self):
#         return hash((self.x, self.y))

# p1 = Point(1, 2)
# p2 = Point(1, 2)

# print(p1 == p2)          # True  ✓ — expected

# my_set = {p1, p2}
# print(len(my_set))       # Expected: 1, Actual: 1  ✓

# my_dict = {p1: "first"}
# print(my_dict.get(p2))   # Expected: "first", Actual: "first"  ✓

# ===========

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

#================================

# def longest_common_prefix(strs: list[str]) -> str:
#     if not strs:
#         return ""

#     prefix = strs[0]
#     for i in range(1, len(strs)):
#         while strs[i].find(prefix) != 0:
#             prefix = prefix[:-1]
#             if not prefix:
#                 return ""
#     return prefix

# print(longest_common_prefix(["flower","flow","flight"]))  # "fl"
# print(longest_common_prefix(["dog","racecar","car"]))  # ""
# print(longest_common_prefix([]))  # ""
# print(longest_common_prefix(["a"]))  # "a"
# print(longest_common_prefix(["ab","a"]))  # "a"

#================================

# def length_of_last_word(s: str) -> int:
#     return len(s.split()[-1])

# print(length_of_last_word("Hello World"))  # 5
# print(length_of_last_word("   fly me   to   the moon  "))  # 4
# print(length_of_last_word("luffy is still joyboy"))  # 6
# print(length_of_last_word(""))  # 0
# print(length_of_last_word("a"))  # 1
# print(length_of_last_word("ab"))  # 2


#=======================

#  Mirror Distance of an Integer
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer n.

# Define its mirror distance as: abs(n - reverse(n))​​​​​​​ where reverse(n) is the integer formed by reversing the digits of n.

# Return an integer denoting the mirror distance of n​​​​​​​.

# abs(x) denotes the absolute value of x.

 

# Example 1:

# Input: n = 25

# Output: 27

# Explanation:

# reverse(25) = 52.
# Thus, the answer is abs(25 - 52) = 27.
# Example 2:
# Input: n = 10
# Output: 9
# Explanation: reverse(10) = 1. Thus, the answer is abs(10 - 1) = 9.

#===========    

# def mirror_distance(n: int) -> int:
#     reversed_n = int(str(abs(n))[::-1])
#     return abs(n - reversed_n)


# print(mirror_distance(25))   # 27
# print(mirror_distance(10))   # 9

