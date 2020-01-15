import timeit
import array

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 100000

SETUP = """
from array import array
import reprlib

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)


class Vector2:
    typecode = 'd'


    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        return reprlib.repr(list(self._components))

v1 = Vector(range(100))
v2 = Vector2(range(100))
"""


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


clock("Vector() : ", "repr(v1)")
clock("Vector2(): ", "repr(v2)")
