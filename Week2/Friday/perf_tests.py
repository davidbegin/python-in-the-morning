import timeit
import array

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 100000

SETUP = """
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


clock("frozenset(): ", "frozenset([1, 2, 3])")
