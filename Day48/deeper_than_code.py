print("\033c")

import asyncio

@asyncio.coroutine
def py34_coro():
    """Generator-based coroutine"""
    # No need to build these yourself, but be aware of what they are
    s = yield from stuff()
    return s

async def py35_coro():
    """Native coroutine, modern syntax"""
    s = await stuff()
    return s

async def stuff():
    return 0x10, 0x20, 0x30


from itertools import cycle

c1 = cycle((9, 8, 7, 6))

breakpoint()

# old = py34_coro()
# new_new = py35_coro()

# breakpoint()







