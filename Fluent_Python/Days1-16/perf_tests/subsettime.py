import timeit
import array

TIMES = 10000000

SETUP = """
a = {1, 2, 108, 420}
b = {3, 4, 109, 777}
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


print("\033c")
print("\t\033[35;1;6;4;5mLet's Time Some Stuff!!\033[0m\n")

clock("a <= b:        ", "y = a < b")
clock("a.issubset(b): ", "y = a.issubset(b)")
