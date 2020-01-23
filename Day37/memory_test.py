# Stolen from: https://medium.com/survata-engineering-blog/monitoring-memory-usage-of-a-running-python-program-49f027e3d1ba

print("\33c")

import tracemalloc


def measure_memory(func):
    tracemalloc.start()
    def measure():

        func()

        current, peak = tracemalloc.get_traced_memory()
        print(f"\n\033[37mFunction Name       :\033[35;1m {func.__name__}\033[0m")
        print(f"\033[37mCurrent memory usage:\033[36m {current / 10**6}MB\033[0m")
        print(f"\033[37mPeak                :\033[36m {peak / 10**6}MB\033[0m")
        tracemalloc.stop()

    return measure


@measure_memory
def slow():
    with open("access-log") as wwwlog:
        total = 0
        for line in wwwlog:
            bytes_sent = line.rsplit(None,1)[1]
            if bytes_sent != '-':
                total += int(bytes_sent)
        return total
        # print("Total", total)



@measure_memory
def fast():
    with open("access-log") as wwwlog:
        bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog)
        bytes_sent = (int(x) for x in bytecolumn if x != '-')
        return sum(bytes_sent)
        # print("Total", sum(bytes_sent))

slow()
fast()
