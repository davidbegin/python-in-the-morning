print("\033c")

import asyncio

# Regular function
# that is executed right away
def meth():
    print("meth executed")
    return "meth"

# This returns a generator object,
# that runs until the yield statement
# when when you can call next, it resumes exuection
def gen():
    yield

# this is the old style of coroutines,
# or passing data between a generator and subgenerator
def old_coro():
    yield from gen()

async def coro():
    pass

async def async_gen():
    yield

m1 = meth()
print(f"meth() class: {type(m1)}")
g1 = gen()
print(f"gen() class: {type(g1)}")
c1 = coro()
print(f"coro() class: {type(c1)}")
c2 = old_coro()
print(f"old_coro() class: {type(c2)}")
a1 = async_gen()
print(f"async_gen() class: {type(a1)}")
