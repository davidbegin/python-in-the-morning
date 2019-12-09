import timeit
import array

TIMES = 1000000

SETUP = """
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))

# long_way = """
# found = 0
# for n in needles:
#     if n in haystack:
#         found += 1
# """

# clock("Two Set Conversion: ", "found = len(set(needles) & set(haystack))")
# clock("Set Intersection  : ", "found = len(set(needles).intersection(haystack))")
# clock("Long Way          : ", long_way)


clock("frozenset(): ", "frozenset([1, 2, 3])")
clock("set(): ", "set([1, 2, 3])")
clock("{...}: ", "{1, 2, 3}")
