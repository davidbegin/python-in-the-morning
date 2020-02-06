print('\033c')

daily_fact = "\033[36m2020 - 2 - 5\n\n\t\033[35m1971 – 2 - 5\n\tAstronauts alledegadly land on the moon in the Apollo 14 mission.\033[0m"

print(f"\t\033[35;1;6m{daily_fact}\033[0m\n")


from dis import dis
import opcode
import asyncio


import asyncio
import concurrent.futures


# I don't this doesn't actually block
# because python knows to release the GIL (Global interpeter Lock)
def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    with open('/dev/urandom', 'rb') as f:
        return f.read(100)


def cpu_bound():
    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.
    return sum(i * i for i in range(10 ** 7))


async def main():
    loop = asyncio.get_running_loop()

    ## Options:

    # The executor argument should be an concurrent.futures.Executor instance.
    # The default executor is used if executor is None.
    # 1. Run in the default loop's executor:
    # coroutine 'blocking_io' was never awaited
    # result = await loop.run_in_executor(
    #     None, blocking_io)
    # print('default thread pool', result)

    # 2. Run in a custom thread pool:
    # with concurrent.futures.ThreadPoolExecutor() as pool:
    #     result = await loop.run_in_executor(
    #         pool, blocking_io)
    #     print('custom thread pool', result)

    # # 3. Run in a custom process pool:
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, cpu_bound)
        print('custom process pool', result)

asyncio.run(main())
