import timeit

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 100000


SETUP = """
from operator import itemgetter

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


itemgetter_version = """
for city in sorted(metro_data, key=itemgetter(1)):
    x = city
"""

lamdba_version = """
for city in sorted(metro_data, key=lambda city_info: city_info[1]):
    x = city
"""

clock("itemgetter_version:", itemgetter_version)
clock("lamdba_version    :", lamdba_version)

