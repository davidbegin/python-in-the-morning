print("\033c")

daily_fact = "2020-1-27\n\n\t53 years ago on this date The Soviet Union,the United States,\n\tand the United Kingdom sign the Outer Space Treaty in Washington, D.C.,\n\tbanning deployment of nuclear weapons in space,\n\tand limiting use of the Moon and other celestial bodies to peaceful purposes."

print(f"\t\033[35;1;6m{daily_fact}\033[0m\n")


from dis import dis
import opcode
import inspect

{"one": 1, "two": 2}


# Adding the yield keyboard, means the first
# invocation will return a generator
def simple_coroutine():
    breakpoint()
    print("-> coroutine started")
    # print(inspect.getgeneratorstate())
    # Just because of the assigment, this is a now coroutine??
    x = yield
    print("-> coroutine received:", x)


my_coro = simple_coroutine()

# Coroutines have to be initialized!!!
print(inspect.getgeneratorstate(my_coro))
next(my_coro)
print(inspect.getgeneratorstate(my_coro))
try:
    my_coro.send(42)
except:
    pass
print(inspect.getgeneratorstate(my_coro))
# my_coro.send(108)
