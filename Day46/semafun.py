print("\033c")

import asyncio

lock = asyncio.Semaphore(5)

async def cool_func(i):
    async with lock:
        print(f"Starting to Sleep... {i}")
        await asyncio.sleep(1)
        print(f"Ending Sleep {i}")


# How do I wait until all tasks are finished in this super simple
async def main():
    for i in range(100):
        asyncio.create_task(cool_func(i))
            # We want to schedule this task
            # await cool_func(i)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

Don't Close the loop before the tasks are done.
loop.close()


# acquire -> this is the main blocking thang

# ', 'locked', 'release'
# breakpoint()

