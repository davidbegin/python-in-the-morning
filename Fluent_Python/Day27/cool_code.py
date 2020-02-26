print('\033c')

print("\t\033[35;1;6;4;5mWednesday!!!!\033[0m\n")


from dis import dis
import opcode


from array import array
import reprlib
import numbers
import math
import functools
import operator



class Vector:
    # this is for the array, how big is each slot
    # d == 8 unsigned bits
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __len__(self):
        return len(self._components)

    def __setattr__(self, name, value):
        if len(name) == 1:
            cls = type(self)
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = None
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    shortcut_names = 'xyzw'

    def __getattr__(self, name):
        # print(f"We Gettin' {name}")
        cls = type(self)

        if len(name) == 1:
            pos = cls.shortcut_names.find(name)

            if 0 <= pos < len(self._components):
                return self._components[pos]

        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

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


    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes)

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


v1 = Vector([3, 6])
v2 = Vector([2, 7])

v3 = Vector([1])
v4 = Vector([1.5])



# v1 = Vector([1, 2])
# v2 = Vector((1, 2, 3))
# v3 = Vector(range(10))
import pdb; pdb.set_trace()

# v1.x
# no method declared

# v1.x=
# ........ is is declared???

print(v1.x)
print(v1.y)
print(v3.z)
print(v3.w)
print(v1.w)
print(v3.coolstuff)

# print(repr(v3[1]))
# print(repr(v3[1:4]))
# print(repr(v3[1:4:2]))
# print(repr(v3[1:4:2, 9]))
# print(repr(v3[1:4:2, 7:9]))
# print(repr(v3[1,2]))



