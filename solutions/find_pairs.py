def find_pairs(nums: list[int], target: int) -> list[tuple[int, int]]:
    seen = set()
    pairs = []


    for num in nums:
      comp = target - num
      if comp in seen:
        pairs.append((num, comp))

      seen.add(num)
    return pairs



res = find_pairs([1, 2, 3, 4, 5], 7)
print(res)
