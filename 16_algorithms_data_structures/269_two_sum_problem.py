def two_sum(numbers, target):
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

tests = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([1, 5, 3, 7, 2], 9),
]

for nums, target in tests:
    result = two_sum(nums, target)
    if result:
        i, j = result
        print(f"{nums}: indices {result} -> {nums[i]} + {nums[j]} = {target}")
    else:
        print(f"{nums}: no solution for target {target}")
