import timeit
import array

TIMES = 100000

SETUP = """
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

def reverse_it(word):
    return word[::-1]
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


print("\033c")
print("\t\033[35;1;6;4mLet's Time Some Stuff!!\033[0m\n")


clock("Sort with Lambda  :", 'x = sorted(fruits, key=lambda word: word[::-1])')
clock("Sort with Function:", 'x = sorted(fruits, key=reverse_it)')

