print('\033c')


daily_fact = "\033[35m61 Years ago on 1959 - 2 - 6\n\n\t\033[97mJack Kilby of Texas Instruments files the first patent for an integrated circuit."

print(f"\t\033[35;1;6m{daily_fact}\033[0m\n")


from dis import dis
import opcode

import asyncio
import random
import time


async def part1(n: int) -> str:
    print(f"\t\tenter #part1 {n}")
    await asyncio.sleep(n)
    print(f"\t\t\tdone sleeping in #part1 - {n}")
    result = f"part1: {n}"
    return result

async def part2(n: int, arg: str) -> str:
    print(f"\t\tenter #part2 {n}")
    await asyncio.sleep(n)
    print(f"\t\t\tdone sleeping in #part2 - {n}")
    result = f"part2: {n}"
    return result

async def chain(n: int) -> None:
    print("\tEnter #chain")
    p1 = await part1(n)
    print(f"\033[95mresult of p1 - n: {n} {p1}\033[0m")
    p2 = await part2(n, p1)
    print(f"\033[96mresult of p2 - {n}: {p2}\033[0m")




async def main(*args):
    print("Enter #main")
    await asyncio.gather(*(chain(n) for n in args))



if __name__ == "__main__":
    import sys
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()


    # asyncio.run is standard way to quick off a async program
    # pass it async function that will handle all the tasks
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    # print(f"Program finished in {end:0.2f} seconds.")


