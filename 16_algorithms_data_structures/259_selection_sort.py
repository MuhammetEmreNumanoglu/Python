def selection_sort(items):
    arr = items[:]
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

data = [64, 25, 12, 22, 11]
print("Original:", data)
print("Sorted:", selection_sort(data))

words = ["banana", "apple", "cherry", "date"]
print("Words:", words)
print("Sorted:", selection_sort(words))
