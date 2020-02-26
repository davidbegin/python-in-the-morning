import timeit
import array

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 5000

SETUP = """
import itertools

def big_range(n):
    for _ in range(n):
        x = "Assignment just so we do something"

def it_repeat(n):
    for _ in itertools.repeat(None, n):
        x = "Assignment just so we do something"
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))



clock("big_range(): ", "big_range(1000)")
clock("it_repeat(): ", "it_repeat(1000)")
