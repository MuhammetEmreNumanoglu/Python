import asyncio

async def fetch_data(name, delay):
    print(f"Fetching {name}...")
    await asyncio.sleep(delay)
    return f"Data from {name}"

async def main():
    result1 = await fetch_data("database", 0.3)
    result2 = await fetch_data("api", 0.2)
    print(result1)
    print(result2)
    print("Sequential done")

asyncio.run(main())
