import timeit

setup1 = "data = list(range(1000))"
stmt1 = "sum(data)"
time1 = timeit.timeit(stmt1, setup=setup1, number=10000)
print(f"sum(list): {time1:.4f}s")

stmt2 = "total = 0\nfor x in data:\n    total += x"
time2 = timeit.timeit(stmt2, setup=setup1, number=10000)
print(f"for loop:  {time2:.4f}s")

list_time = timeit.timeit("[x**2 for x in range(100)]", number=10000)
gen_time = timeit.timeit("list(x**2 for x in range(100))", number=10000)
print(f"List comprehension: {list_time:.4f}s")
print(f"Generator expr:     {gen_time:.4f}s")

result = timeit.repeat("'-'.join(str(n) for n in range(100))", repeat=3, number=1000)
print(f"Best of 3: {min(result):.4f}s")
