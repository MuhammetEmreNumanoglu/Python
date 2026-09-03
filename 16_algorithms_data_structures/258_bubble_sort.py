def bubble_sort(items):
    arr = items[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

data = [64, 34, 25, 12, 22, 11, 90]
print("Original:", data)
sorted_data = bubble_sort(data)
print("Sorted:", sorted_data)

already_sorted = [1, 2, 3, 4, 5]
print("Already sorted:", bubble_sort(already_sorted))
