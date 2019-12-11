import timeit

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 100000

SETUP = """
from operator import mul
from functools import partial
from functools import lru_cache
triple = partial(mul, 3)

def uncached_func():
    x = [ triple(i) for i in range(1, 10) ]

@lru_cache(maxsize=512)
def cached_func():
    x = [ triple(i) for i in range(1, 10) ]

@lru_cache(maxsize=1024)
def more_cached_func():
    x = [ triple(i) for i in range(1, 10) ]

@lru_cache(maxsize=2048)
def even_more_cached_func():
    x = [ triple(i) for i in range(1, 10) ]

@lru_cache(maxsize=16384)
def almost_max_cached_func():
    x = [ triple(i) for i in range(1, 10) ]

@lru_cache(maxsize=65536)
def true_max_cached_func():
    x = [ triple(i) for i in range(1, 10) ]

@lru_cache(maxsize=131072)
def above_the_max_cached_func():
    x = [ triple(i) for i in range(1, 10) ]

@lru_cache(maxsize=100000)
def max_cached_func():
    x = [ triple(i) for i in range(1, 10) ]
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


clock("uncached_func()                   : ", "uncached_func()")
clock("512 cached_func()                 : ", "cached_func()")
clock("1024 more_cached_func()           : ", "more_cached_func()")
clock("2056 even_more_cached_func()      : ", "even_more_cached_func()")
clock("16384 almost_max_cached_func()    : ", "almost_max_cached_func()")
clock("65536 true_max_cached_func()      : ", "true_max_cached_func()")
clock("131072 above_the_max_cached_func(): ", "above_the_max_cached_func()")
clock("100000 max_cached_func()          : ", "max_cached_func()")

