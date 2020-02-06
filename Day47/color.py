import asyncio
import random

# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
    "\033[33m",  # Yellow
)

async def makerandom(idx: int, threshold: int = 6) -> int:
    print(c[idx + 1] + f"Initiated makerandom({idx})." + c[0])

    # once we hit the 6, its all over
    i = random.randint(0, 10)

    while i <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")

        await asyncio.sleep(idx + 1)

        i = random.randint(0, 10)

    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return i


async def main():
    gather_meat = (makerandom(i, 10 - i - 1) for i in range(4))
    res = await asyncio.gather(*gather_meat)
    return res

if __name__ == "__main__":
    # Big Jay0Z Gan
    random.seed(444)
    awaited_tasks = asyncio.run(main())
    breakpoint()
    # print()
    # print(f"r1: {r1}, r2: {r2}, r3: {r3}")
