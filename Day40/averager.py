print('\033c')

daily_fact = "2020-1-27\n\n\t53 years ago on this date The Soviet Union,the United States,\n\tand the United Kingdom sign the Outer Space Treaty in Washington, D.C.,\n\tbanning deployment of nuclear weapons in space,\n\tand limiting use of the Moon and\n\tother celestial bodies to peaceful purposes."

print(f"\t\033[35;1;6m{daily_fact}\033[0m\n")


from dis import dis
import opcode
import inspect



from functools import wraps

# from funktools import raps

def coroutine(func):
    """Decorator: primes `func` by advancing to first `yield`"""

    @wraps(func)
    def primer(*args,**kwargs):
        gen = func(    *args,**kwargs    )

        # primed our own generator
        next(gen)
        return gen
    return primer

@coroutine
def a_wannabe_coroutine_func():
    x = None
    x = yield x
    x += 1
    print(f"Cool: {x}")

a1 = a_wannabe_coroutine_func()

try:
    a1.send(108)
except:
    pass


