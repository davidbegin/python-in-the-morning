# Stolen from: https://medium.com/survata-engineering-blog/monitoring-memory-usage-of-a-running-python-program-49f027e3d1ba

print("\33c")

import tracemalloc


def measure_memory(func):
    def measure():
        tracemalloc.start()

        func()

        current, peak = tracemalloc.get_traced_memory()
        print(f"\n\033[37mFunction Name       :\033[35;1m {func.__name__}\033[0m")
        print(f"\033[37mCurrent memory usage:\033[36m {current / 10**6}MB\033[0m")
        print(f"\033[37mPeak                :\033[36m {peak / 10**6}MB\033[0m")
        tracemalloc.stop()

    return measure


@measure_memory
def method_1():
    return list(range(1000000))

@measure_memory
def method_2():
    return range(1000000)

method_1()
method_2()

