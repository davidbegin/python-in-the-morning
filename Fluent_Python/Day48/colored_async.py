print("\033c")

import asyncio
import itertools as it
import os
import random
import time


async def makeitem(size: int = 5) -> str:
    print(f"\t\t\tmakeitem: {size}")

    # this uses /dev/urandom
    # uses entropy from device drivers
    # like you mouse movements!
    # This is a Blocking I/O operation??
    return os.urandom(size).hex()


async def randsleep(a: int = 1, b: int = 5, caller=None) -> None:
    i = random.randint(0, 10)

    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


# The fact that this takes a single letter
# env var, kinda makes me sad, but the they of asyncio.Queue
# I don't like single letter vars, but I am much more
# forgiviing if it's typed
async def produce(name: int, q: asyncio.Queue) -> None:
    print(f"\033[96m\tTop of Produce: {name}\033[0m")

    n = random.randint(0, 10)

    # This is valuable performance improvement
    for _ in it.repeat(None, n):  # Synchronous loop for each single producer

        await randsleep(caller=f"Producer {name}")
        i = await makeitem()
        t = time.perf_counter()

        # this is passing data from producer to consumer
        # The queue facilitates the data passing
        # not the task scheduling
        await q.put((i, t))

        print(f"Producer {name} added <{i}> to queue.")


async def consume(name: int, q: asyncio.Queue) -> None:
    print(f"\t\033[91mTop of Consume: {name}\033[0m")


    try:
        while True:
            await randsleep(caller=f"Consumer {name}")

            i, t = await q.get()
            # This will raise an error, when theres nothing in the Queue
            now = time.perf_counter()
            print(f"Consumer {name} got element <{i}>" f" in {now-t:0.5f} seconds.")
            q.task_done()
    except Exception as err:
        print(f"WE CAUGHT THAT EXCEPTION: {err}")


# We are passing create_task a coroutine
async def main(nprod: int, ncon: int):
    q = asyncio.Queue()

    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]

    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]

    # This waits on producers only
    # so if the producers finished before the consumers consumed
    await asyncio.gather(*producers)

    # await q.join()  # Implicitly awaits consumers, too
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    import argparse

    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--nprod", type=int, default=3, help="Number of Producers"
    )
    parser.add_argument(
        "-c", "--ncon", type=int, default=3, help="Number of Consumers"
    )

    ns = parser.parse_args()
    start = time.perf_counter()
    asyncio.run(main(**ns.__dict__))
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")
