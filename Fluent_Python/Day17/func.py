print("\033c")

print("\t\033[35;1;6;4;5mMonday Back From Re:invent!\033[0m\n")


# from faker import Faker
from dis import dis
import opcode
from inspect import signature


from functools import reduce
from operator import mul


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


def fact2(n):
    return reduce(mul, range(1, n + 1))


metro_data = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("Sao Paulo", "BR", 19.649, (-23.547778, -46.635833)),
]

from operator import itemgetter

# for city in sorted(metro_data, key=itemgetter(1)):
#     print(city)


# print("\n\n")

# for city in sorted(metro_data, key=lambda city_info: city_info[1]):
#     print(city)


# from collections import namedtuple

# LatLong = namedtuple("LatLong", "lat long")
# Metropolis = namedtuple("Metropolis", "name cc pop coord")

# metro_areas = [
#     Metropolis(name, cc, pop, LatLong(lat, long))
#     for name, cc, pop, (lat, long) in metro_data
# ]

# from operator import attrgetter
# name_lat = attrgetter('name', 'coord.lat')

# for city in sorted(metro_areas, key=attrgetter('coord.lat')):
#     print(name_lat(city))



from operator import methodcaller
import operator

x = [1, 200, 2, -2, 400, 108, -108]

power_of_2 = methodcaller("ipow", 2)
power_of_2(10)




# Can I sort and change the keys at the same time with a single function?


# result = sorted(x, key=power_of_2)
# print(result)



# What is a function that takes a single argument from operator that
# use augmented assignment?






# s = 'The time has come'

# upcase = methodcaller('upper')

# print(upcase(s))

# hiphenate = methodcaller('replace', ' ', '-')
# hiphenate(s)







