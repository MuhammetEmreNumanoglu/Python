def insertion_sort(items):
    arr = items[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

data = [12, 11, 13, 5, 6]
print("Original:", data)
print("Sorted:", insertion_sort(data))

almost_sorted = [1, 2, 4, 3, 5]
print("Almost sorted:", insertion_sort(almost_sorted))
