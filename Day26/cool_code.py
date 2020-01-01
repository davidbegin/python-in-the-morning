print('\033c')

print("\t\033[35;1;6;4;5mNew Year New Me!\033[0m\n")


from dis import dis
import opcode


from array import array
import reprlib
import numbers
import math


class Vector:
    # this is for the array, how big is each slot
    # d == 8 unsigned bits
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __len__(self):
        return len(self._components)

    def __getitem__2(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return Vector(self._components[index])
        elif isinstance(index, int):
            return self._components[index]
        elif isinstance(index, tuple):
            return [ self[element] for element in index ]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        # What are all the options to reprlib?
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    # Absolute Value of a Vector, is apparently
    # the square root of the sum of all parts
    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)



v1 = Vector([1, 2])
v2 = Vector((1, 2, 3))
v3 = Vector(range(10))

print(repr(v3[1]))
print(repr(v3[1:4]))
print(repr(v3[1:4:2]))
print(repr(v3[1:4:2, 9]))
print(repr(v3[1:4:2, 7:9]))
print(repr(v3[1,2]))




