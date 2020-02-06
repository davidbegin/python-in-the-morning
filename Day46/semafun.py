print("\033c")

import asyncio


# If a function takes a future, should
# it always be first, last or random argument
# async def cool_func(i, fut):
#     async with lock:
#         print(f"Starting to Sleep... {i}")
#         await asyncio.sleep(1)
#         print(f"Ending Sleep {i}")
#         fut.set_result(i)


async def cool_func(lock, i):
    # The Loop here is different than Semaphore loop
    # When we create the semaphore loop outside the function
    async with lock:
        print(f"Starting to Sleep... {i}")
        await asyncio.sleep(1)
        print(f"Ending Sleep {i}")

# got Future <Future pending> attached to a different loop
# How do I wait until all tasks are finished in this super simple
async def main():
    # lock = asyncio.Semaphore(5)
    # loop = asyncio.get_event_loop()

    lock = asyncio.Semaphore(5)
    # lock = asyncio.Semaphore(5, loop=loop)
    await asyncio.gather(*(cool_func(lock, i) for i in range(100)))
    # await asyncio.gather(*(cool_func(lock, i) for i in range(100)))
    # futures = []

    # for i in range(100):
    #     fut = asyncio.Future()
    #     futures.append(fut)
    #     task = asyncio.create_task(cool_func(i, fut))

    # [await future for future in futures]

asyncio.run(main())
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

# Don't Close the loop before the tasks are done.
# loop.close()


# acquire -> this is the main blocking thang

# ', 'locked', 'release'
# breakpoint()

