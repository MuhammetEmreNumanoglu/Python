import asyncio

async def countdown(name, seconds):
    for i in range(seconds, 0, -1):
        print(f"{name}: {i}")
        await asyncio.sleep(0.5)
    print(f"{name}: Done!")

async def delayed_message(delay, message):
    await asyncio.sleep(delay)
    print(f"[After {delay}s] {message}")

async def main():
    await asyncio.gather(
        countdown("Counter A", 3),
        delayed_message(0.7, "First message"),
        delayed_message(1.2, "Second message"),
    )

asyncio.run(main())
