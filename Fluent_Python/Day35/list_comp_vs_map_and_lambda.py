import timeit
import array

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 1000000

SETUP = """
list_of_lists = [ [1,2], [1,3], [1,4], [1,5] ]
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


clock("list comprehension: ", "[ a[1] for a in list_of_lists ]")
clock("map and lambda    : ", "[ a for a in map( (lambda a: a[1]), list_of_lists) ]")

