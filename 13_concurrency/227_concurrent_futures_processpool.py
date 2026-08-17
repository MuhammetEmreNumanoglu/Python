from concurrent.futures import ProcessPoolExecutor
import time

def cpu_work(n):
    return sum(i ** 2 for i in range(n))

if __name__ == "__main__":
    inputs = [100_000, 200_000, 150_000, 250_000]

    start = time.time()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(cpu_work, inputs))
    elapsed = time.time() - start

    print("Results:", results)
    print(f"Done in {elapsed:.2f}s")
