def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def take(gen, n):
    for _ in range(n):
        print(next(gen), end=" ")
    print()

fib = fibonacci()
take(fib, 10)

def read_large_file_lines():
    import tempfile, os
    tmp = tempfile.mktemp()
    with open(tmp, "w") as f:
        for i in range(100):
            f.write(f"Line {i}\n")
    with open(tmp) as f:
        for line in f:
            yield line.strip()
    os.remove(tmp)

gen = read_large_file_lines()
for _ in range(5):
    print(next(gen))
