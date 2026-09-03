def quick_sort(items):
    if len(items) <= 1:
        return items

    pivot = items[len(items) // 2]
    left = [x for x in items if x < pivot]
    middle = [x for x in items if x == pivot]
    right = [x for x in items if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

data = [3, 6, 8, 10, 1, 2, 1]
print("Original:", data)
print("Sorted:", quick_sort(data))

print(quick_sort([5, 2, 4, 6, 1, 3]))
print(quick_sort(["banana", "apple", "cherry"]))
