# print('\033c')
# print("\n\n\t\033[35;1;6;4;5mThursday Aww Yeah!\033[0m\n")


from dis import dis
import opcode

from array import array
import reprlib
import itertools
import numbers


class Vector2:
typecode = "d"

def __init__(self, components):
    self._components = list(components)
    # self._components = array(self.typecode, components)

def __eq__(self, other):
    return all(x == y for x, y in zip(self, other))

def __iter__(self):
    return iter(self._components)

def __str__(self):
    return str(tuple(self))

def __repr__(self):
    components = reprlib.repr(self._components)
    components = components[components.find("[") : -1]
    return "Vector({})".format(components)

def __invert__(self):
    return Vector((~x for x in self))

def __add__(self, other):
    try:
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(a + b for a, b in pairs)
    except TypeError:
        return NotImplemented

def __radd__(self, other):
    return self + other


class Vector:
typecode = "d"

def __init__(self, components):
    self._components = list(components)
    # self._components = array(self.typecode, components)

def __eq__(self, other):
    return all(x == y for x, y in zip(self, other))

def __iter__(self):
    return iter(self._components)

def __str__(self):
    return str(tuple(self))

def __repr__(self):
    components = reprlib.repr(self._components)
    components = components[components.find("[") : -1]
    return "Vector({})".format(components)

def __invert__(self):
    return Vector((~x for x in self))

def __add__(self, other):
    try:
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(a + b for a, b in pairs)
    except TypeError:
        return NotImplemented

def __radd__(self, other):
    return self + other

def __mul__(self, other):
    if isinstance(other, numbers.Integral):
        return Vector(x * other for x in self)
    else:
        raise TypeError(f"Must be a Integral: {type(other)}")

def __rmul__(self, other):
    return self * other


# v2 = Vector([3, 5])
# v3 = [108, 420]

# # print(v1 + v3)
# # print(v3 + v1)
