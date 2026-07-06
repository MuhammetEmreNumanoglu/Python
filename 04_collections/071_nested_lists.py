matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(matrix[0])
print(matrix[1][2])

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

flat = [value for row in matrix for value in row]
print(flat)

grid = [[0] * 3 for _ in range(3)]
grid[1][1] = 9
print(grid)
