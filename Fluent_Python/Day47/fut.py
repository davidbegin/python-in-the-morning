print('\033c')

daily_fact = "\033[36m2020 - 2 - 5\n\n\t\033[35m1971 – 2 - 5\n\tAstronauts alledgedlly land on the moon in the Apollo 14 mission.\033[0m"

print(f"\t\033[35;1;6m{daily_fact}\033[0m\n")


from dis import dis
import opcode
import asyncio

# fut API
# add_done_callback',
# 'cancel',
# 'cancelled',
# 'done',
# 'exception',
# 'get_loop',
# 'remove_done_callback',
# 'result',
# 'set_exception',
# 'set_result'



# What kind of methods take Futures?
# Async code we want to know when is finished
# AKA: Callbacks
async def set_after(fut, delay, value):
    breakpoint()
    # Sleep for *delay* seconds.
    fut.set_result(value)
    await asyncio.sleep(delay)
    return "Hello"

    # Set *value* as a result of *fut* Future.
    # If we don't set_result
    # this never returns????
    # When we set the future result
    # does it return right away???
    # fut.set_result(value)


async def main():
    # Get the current event loop.
    loop = asyncio.get_running_loop()

    # Create a new Future object.
    fut = loop.create_future()

    # Run "set_after()" coroutine in a parallel Task.
    # We are using the low-level "loop.create_task()" API here because
    # we already have a reference to the event loop at hand.
    # Otherwise we could have just used "asyncio.create_task()".
    loop.create_task(
        set_after(fut, 1, '... world'))

    print('hello ...')
    print(f"Loop is running: {loop.is_running()}")
    # print("world")
    print(await fut)
    print(f"Loop is running: {loop.is_running()}")

    # Wait until *fut* has a result (1 second) and print it.


asyncio.run(main())

