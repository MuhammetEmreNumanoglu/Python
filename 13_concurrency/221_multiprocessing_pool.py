import multiprocessing

def square(n):
    return n * n

def cube(n):
    return n ** 3

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    with multiprocessing.Pool(processes=4) as pool:
        squares = pool.map(square, numbers)
        print("Squares:", squares)

    with multiprocessing.Pool() as pool:
        cubes = pool.map(cube, numbers)
        print("Cubes:", cubes)

    with multiprocessing.Pool() as pool:
        results = pool.map(square, range(10))
    print("Results:", results)
