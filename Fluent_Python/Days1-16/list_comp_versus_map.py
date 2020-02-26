import timeit
import array

TIMES = 100000

SETUP = """
def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)

fact = factorial
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


print("\033c")
print("\t\033[35;1;6;4mLet's Time Some Stuff!!\033[0m\n")

clock("fact with map      :", 'list(map(fact, range(6)))')
clock("fact with list comp:", '[fact(n) for n in range(6)]')
clock("fact with filter   :", 'list(map(fact, filter(lambda n: n % 2, range(6))))')
clock("fact with list if  :", '[factorial(n) for n in range(6) if n % 2]')

