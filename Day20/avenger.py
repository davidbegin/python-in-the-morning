print("\033c")


class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)



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

avg = make_averager()

avg(10)
avg(11)
print(avg(12))





# print(avg.__closure__[0].cell_contents)
# avg(108)
# print(avg.__closure__[0].cell_contents)
# avg(420)
# print(avg.__closure__[0].cell_contents)
# import pdb; pdb.set_trace()
# print(avg.__code__.co_varnames)
# print(avg.__code__.co_freevars)

# avg(10)
# avg(420)
# avg(108)
# print(avg(1000))
