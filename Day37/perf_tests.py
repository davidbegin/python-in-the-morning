import timeit
import array

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")

from memory_test import measure_memory

TIMES = 1

SETUP = """
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

"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


clock("slow(): ", "slow()")
clock("fast(): ", "fast()")
