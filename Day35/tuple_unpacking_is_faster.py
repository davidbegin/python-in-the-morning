import timeit
import array

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 10000000

SETUP = """
two_elem = ("cool_thang", "no nobody cares")
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


clock("[0]         : ", "meth_name = two_elem[0]")
clock("tuple_unpack: ", "meth_name, _ = two_elem")
