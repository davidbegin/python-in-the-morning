# Stolen from: https://medium.com/survata-engineering-blog/monitoring-memory-usage-of-a-running-python-program-49f027e3d1ba


print("\33c")

import tracemalloc
import numbers


def measure_memory(func):
    tracemalloc.start()

    # I might want to capture standard output
    func()

    current, peak = tracemalloc.get_traced_memory()
    print(f"\n\033[37mFunction Name       :\033[35;1m {func.__name__}\033[0m")
    print(f"\033[37mCurrent memory usage:\033[36m {current / 10**6}MB\033[0m")
    print(f"\033[37mPeak                :\033[36m {peak / 10**6}MB\033[0m")
    tracemalloc.stop()



# List Comphrehension
#   -> Comsume it right away, not extra generator

# Generator
#  -> Some lazy object, that can produce the sequence on demand
#  -> Not paying the cost of the whoel sequence, but there is some
#  -> for the generator itself
#
#  -> Does the generator ever store the full list, or does it stream it?

Iterables return Iterators when you call the __iter__

Iterators return Iterators (themselves typically) if you call the __iter__
method, which makes Iterators Iterables, since Iterables return Iterators.

Iterable
Iterator



Generator, produce values out of thin air
range(100000)



def vowel(c):
    return c in [1,2]

@measure_memory
def range_is_a_gen():
    range(100000000000000000000000)

# @measure_memory():
# def list_is_not():
#     range(100000000000000000000000)

# @measure_memory
# def filter_meth():
#     return filter(vowel, range(10000000))

# @measure_memory
# def list_meth():
#     return [ c for c in range(10000000) if c in [1,2]]




