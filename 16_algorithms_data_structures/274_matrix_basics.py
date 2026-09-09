matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Matrix:")
for row in matrix:
    print(row)

print("\nElement [1][2]:", matrix[1][2])

rows = len(matrix)
cols = len(matrix[0])
print(f"Dimensions: {rows}x{cols}")

transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
print("\nTransposed:")
for row in transposed:
    print(row)

flat = [val for row in matrix for val in row]
print("\nFlattened:", flat)

def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])
    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("\nMatrix product:")
for row in multiply_matrices(A, B):
    print(row)
