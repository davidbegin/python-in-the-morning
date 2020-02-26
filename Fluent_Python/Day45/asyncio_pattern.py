print("\033c")

import asyncio
import time
import logging
import structlog
import colorama

logger = structlog.get_logger()
logger.error("We are debugging")

async def a_cool_task():
    await asyncio.sleep(3)

    with open("cool_file.txt", "w") as f1:
        f1.write("Something cool")

    while True:
      try:
        print("Super Cool things")
        await asyncio.sleep(1)
      except asyncio.CancelledError:
        break

async def slow_task():
    await asyncio.sleep(3)
    return 108

async def supervisor():
    task = asyncio.create_task(a_cool_task())
    # task = asyncio.shield(asyncio.create_task(a_cool_task()))
    print(f"\033[37mTask Cancelled:\033[0m {task.cancelled()}")
    # result = await slow_task()
    task.cancel()
    # await asyncio.sleep(0.1)

    print(f"\033[37mTask Cancelled:\033[0m {task.cancelled()}")
    await asyncio.sleep(10)
    # return result

result = asyncio.run(supervisor(), debug=True)
print(result)
