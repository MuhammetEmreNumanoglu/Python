import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(0.1)
    print("World!")

async def main():
    await say_hello()
    print("Done")

asyncio.run(main())

async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

async def main2():
    await greet("Alice", 0.2)
    await greet("Bob", 0.1)

asyncio.run(main2())
