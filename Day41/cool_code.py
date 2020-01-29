print("\033c")

print(
    "\t\033[35;1m2020 - 1 - 28\n\n\t\033[36;1m62 years ago on this day\n\tThe Lego company patents the design of its Lego bricks,\n\tstill compatible with bricks produced today!\033[0m\n"
)

from dis import dis

import opcode

from collections import namedtuple

Result = namedtuple("Result", ["count", "average"])

# the subgenerator
def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        # since we see assigment of the yield,
        # starting to look like a coroutine
        # We are not returning anything from the yield
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


# the delegating generator
# delegating generator always has yield from
# sub generator, will assign yield
def grouper(results, key):
    while True:
        # the yield from handles the SoptIteration
        results[key] = yield from averager()


# the client code, a.k.a. the caller
def main(data):
    results = {}

    for key, values in data.items():
        # this is greating a delegating genarator
        # with some data
        group = grouper(results, key)

        # this is prime the generator
        next(group)

        for value in values:
            group.send(value)

        # this will cause a break in the sub-generator
        # This will raise a StopIteration,
        # which will propogate through the delegating
        # generator.
        group.send(None)

    report(results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(";")
        print(
            "{:2} {:5} averaging {:.2f}{}".format(
                result.count, group, result.average, unit
            )
        )


data = {
    "girls;kg": [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    "girls;m": [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    "boys;kg": [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    "boys;m": [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}


main(data)
