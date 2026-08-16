import asyncio
import time

async def task(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done after {delay}s"

async def main():
    start = time.time()

    results = await asyncio.gather(
        task("Task A", 0.3),
        task("Task B", 0.2),
        task("Task C", 0.1),
    )

    elapsed = time.time() - start
    print(f"All done in {elapsed:.2f}s")
    for r in results:
        print(r)

asyncio.run(main())
