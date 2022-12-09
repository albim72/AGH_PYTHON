import time
import asyncio

async def count():
    print("START")
    await asyncio.sleep(2)
    print("END")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} wykonany w {elapsed:0.2f} s")
