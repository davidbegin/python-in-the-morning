print("\033c")

import asyncio

async def coro():
    print('starting')
    await asyncio.sleep(2)
    print('done sleep')

async def cancel_it(some_task):
    await asyncio.sleep(0.5)
    some_task.cancel()
    print('cancellation effected')

# this is our supervisor
async def main():
    real_task = asyncio.create_task(coro())
    shield = asyncio.shield(real_task)

    # cancel the shield in the background while we're waiting
    asyncio.create_task(cancel_it(shield))
    await real_task

    # Interesting having asserts not in tests
    assert not real_task.cancelled()
    assert shield.cancelled()

asyncio.get_event_loop().run_until_complete(main())
