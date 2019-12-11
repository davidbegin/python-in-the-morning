import timeit

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 1000000

SETUP = """
from operator import mul
from functools import partial
triple = partial(mul, 3)
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


clock("list comprehension: ", "[ triple(i) for i in range(1, 10) ]")
clock("map version       : ", "list(map(triple, range(1, 10)))")
