# Clears Terminal
print('\033c')

import bisect
import sys

# Haystack could be all User IDs
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]


# These are some sort of winners
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'
# 31 @ 14      |  |  |  |  |  |  |  |  |  |  |  |  |  |31


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        # print(f"Needle: {needle} | Index: {position}")
        offset = position * '  |'

        print(ROW_FMT.format(needle, position, offset))


# Whats the difference in bisect_left....and I'm assuming right is default
# if __name__ == '__main__':
#     if sys.argv[-1] == 'left':
#         bisect_fn = bisect.bisect_left
#     else:
#         bisect_fn = bisect.bisect

#     print('DEMO:', bisect_fn.__name__)
#     print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))

#     demo(bisect_fn)



import bisect
import random

# SIZE = 7

# random.seed(1729)

# my_list = []
# for i in range(SIZE):
#     new_item = random.randrange(SIZE*2)
#     bisect.insort(my_list, new_item)
#     print('%2d ->' % new_item, my_list)

x = [0, 2, 6, 7, 8, 10, 10.0]
x.sort()

# bisect.insort(x, 3, lo=3)
print(x)


# bisect.insort_left(x, 10)
# print(x)
