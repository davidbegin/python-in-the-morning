print('\033c')

daily_fact = "\033[35m231 Years ago on this date Febuary 4th (1789)\33[0m\n\n\tGeorge Washington is unanimously elected\n\tas the first President of the United States\n\tby the U.S. Electoral College."

print(f"\t\033[35;1;6m{daily_fact}\033[0m\n")


from dis import dis
import opcode
import asyncio
import time



# @asyncio.coroutine
async def other_func():
    print("entering other_func")
    await asyncio.sleep(2)
    print("exiting other_func")


def gen():
    value = yield("Started")
    print(value)


loop = asyncio.get_event_loop()
loop.run_until_complete([other_func(), gen()])


# a = gen()
# breakpoint()
# a.send(None)
# a.send("Done")
