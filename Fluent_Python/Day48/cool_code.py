print('\033c')


daily_fact = "\033[35m61 Years ago on 1959 - 2 - 6\n\n\t\033[97mJack Kilby of Texas Instruments files the first patent for an integrated circuit."

print(f"\t\033[35;1;6m{daily_fact}\033[0m\n")


from dis import dis
import opcode

import asyncio
import random
import time

# If I call a regular method in an async method
# I can get the result, and its blocking
# or I can call an async method, and use await
# and its blocking, but I could use that method asynchronously

def part3(n: int) -> str:
    result = "\033[96mPART 3 in the HOUSE!!!!\033[0m"
    time.sleep(1)
    print(result)
    return result


# when you have an async def method,
# and await on it, it only affects the single
# coroutine process it is blocking
async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(f"part1({n}) sleeping for {i} seconds.")

    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"Returning part1({n}) == {result}.")
    return result

async def part2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"part2{n, arg} sleeping for {i} seconds.")

    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(f"Returning part2{n, arg} == {result}.")
    return result

# this is async method of individual work
# this is what we are parallelizing
# anytime we writing a method that is gonna
# be parallelized, all other methods it calls have
# to be awaiting, or called in another task

# if you don't await an async task
# then your error will look like this:
#   `coroutine 'part1' was never awaited`
async def chain(n: int) -> None:
    start = time.perf_counter()

    # We can call non-async methods, we just can't rely on their output
    p3 = part3(n)
    print(f"P3 inside chain: {p3}")


    p1 = await part1(n)
    p2 = await part2(n, p1)
    end = time.perf_counter() - start
    print(f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")

# We await on the this asyncio.gather, to wait on all the tasks
# typically you are going to await in the main `async def main`
# does this method in a asycio pattern have a name?
# This is a coordinating
async def main(*args):
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
    print(f"Program finished in {end:0.2f} seconds.")


