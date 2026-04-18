# Task #1 — Valid Parentheses
# Write a function is_valid(s) that takes a string containing only (), [], {} and returns True if the brackets are correctly matched and nested, False otherwise.

# def is_valid(str: str) -> bool:
#     bracket_map = {")": "(", "]": "[", "}": "{"}
#     stack = []

#     for char in str:
#         if char in bracket_map:
#             top = stack.pop() if stack else "#"
#             if bracket_map[char] != top:
#                 return False
#         else:
#             stack.append(char)

#     # This will return True if the stack is empty (all brackets matched), otherwise False.
#     # When the function finishes checking all characters, any unmatched opening brackets will be left in the stack.
#     # So, 'not stack' means "return True if stack is empty" (all brackets were properly matched and nested).
#     return not stack


# res = is_valid("[()]")
# print(res)

# Task #2 — Group Anagrams
# Write a function group_anagrams(words) that groups a list of strings into lists of anagrams:


# def group_anagram(words: list[str]) -> list[list[str]]:
#     my_map: dict[str, list[str]] = {}

#     for word in words:
#         sorted_word = "".join(sorted(word))
#         if my_map.get(sorted_word) is None:
#             my_map[sorted_word] = [word]
#         else:
#             my_map[sorted_word].append(word)

#     return list(my_map.values())


# res = group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"])
# print(res)


# def two_num(nums: list[int], target: int) -> list[int, int]:
#     my_map: dict[int, int] = {}

#     for i, num in enumerate(nums):
#         delta = target - num

#         if delta in my_map:
#             return list(my_map[delta], i)
#         else:
#             my_map[num] = i


# print(two_num([2, 4, 5, 6], 10))


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

#     return sorted(my_map.items(), key=lambda item: (-item[1], item[0]))[:k]


# my_map2 : dict[str, int] = {}


# class MyStack:
#     def __init__(self):
#         self.stack: list[int] = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)

#     def pop(self, val: int) -> int:
#         return self.stack.pop()

#     def peek(self) -> int:
#         return self.stack[-1]

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

#==============