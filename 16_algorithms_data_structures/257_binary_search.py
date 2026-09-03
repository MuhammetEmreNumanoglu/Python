def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

numbers = sorted([4, 2, 7, 1, 9, 3, 8, 5, 6])
print("Sorted:", numbers)

print(f"Found 7 at index: {binary_search(numbers, 7)}")
print(f"Found 1 at index: {binary_search(numbers, 1)}")
print(f"Found 10 at index: {binary_search(numbers, 10)}")

import bisect
pos = bisect.bisect_left(numbers, 5)
print(f"bisect position of 5: {pos}")
