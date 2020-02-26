print("\033c")

import asyncio

async def bug():
    raise Exception("not consumed")

# How do we capture 
async def main():
    try:
        task = asyncio.create_task(bug())
    except Exception:
        print("We did it!!!")
    # No cancelling
    task.cancelled()
    # no error handling

asyncio.run(main())
