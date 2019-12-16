import timeit
import array

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 500

SETUP = """
def slow_make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager


def make_averager():
    # series = []
    count = 0
    total = 0

    def averager(new_value):
        nonlocal total, count
        total += new_value
        count += 1

        return total/count

    return averager

fast_avg = make_averager()
slow_avg = slow_make_averager()
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


clock("slow_avg(): ", "[slow_avg(i) for i in range(10)]")
clock("fast_avg(): ", "[fast_avg(i) for i in range(10)]")
