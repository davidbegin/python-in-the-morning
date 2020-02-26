import timeit
import array

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 100000

SETUP = """
import functools
import numpy as np
import operator

my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
def sum1():
    return functools.reduce(lambda a, b: a+b, [sub[1] for sub in my_list])

my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
def sum2():
    return functools.reduce(lambda a, b: a + b[1], my_list, 0)

my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
def sum3():
    my_array = np.array(my_list)
    return np.sum(my_array[:, 1])

my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
def sum4():
    return functools.reduce(operator.add, [sub[1] for sub in my_list], 0)


my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
def sum5():
    total = 0
    for sub in my_list:
        total += sub[1]
    return total

my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
def sum6():
    return sum([sub[1] for sub in my_list])

my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
def sum7():
    return sum(sub[1] for sub in my_list)
"""


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


clock("sum1: ", "sum1()")
clock("sum2: ", "sum2()")
# clock("sum3: ", "sum3()")
clock("sum4: ", "sum4()")
clock("sum5: ", "sum5()")
clock("sum6: ", "sum6()")
clock("sum7: ", "sum7()")
