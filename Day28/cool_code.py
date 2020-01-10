print('\033c')

print("\t\033[35;1;6;4;5mBest Thursday Ever!!!!\033[0m\n")


from dis import dis
import opcode


from array import array
import reprlib
import numbers
import math
import functools
import operator
import itertools



class Vector:
    # this is for the array, how big is each slot
    # d == 8 unsigned bits
    typecode = 'd'

    def __init__(begin, components):
        begin._components = array(begin.typecode, components)

    def __len__(begin):
        return len(begin._components)

    def __setattr__(begin, name, value):
        if len(name) == 1:
            cls = type(begin)
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

    def __getattr__(begin, name):
        cls = type(begin)

        if len(name) == 1:
            pos = cls.shortcut_names.find(name)

            if 0 <= pos < len(begin._components):
                return begin._components[pos]

        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __getitem__(begin, index):
        cls = type(begin)
        if isinstance(index, slice):
            return Vector(begin._components[index])
        elif isinstance(index, int):
            return begin._components[index]
        elif isinstance(index, tuple):
            return [ begin[element] for element in index ]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __iter__(begin):
        return iter(begin._components)

    def __repr__(begin):
        # What are all the options to reprlib?
        components = reprlib.repr(begin._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(begin):
        return str(tuple(begin))

    def __bytes__(begin):
        return (bytes([ord(begin.typecode)]) +
                bytes(begin._components))


    def __hash__(begin):
        hashes = map(hash, begin._components)
        return functools.reduce(operator.xor, hashes)

    def __eq__(begin, other):
        return len(begin) == len(other) and all(a == b for a, b in zip(begin, other))

    # Absolute Value of a Vector, is apparently
    # the square root of the sum of all parts
    def __abs__(begin):
        return math.sqrt(sum(x * x for x in begin))

    def __bool__(begin):
        return bool(abs(begin))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    # What is n???
    def angle(begin, n):
        # what is magnitude
        r = math.sqrt(sum(x * x for x in begin[n:]))
        a = math.atan2(r, begin[n-1])
        if (n == len(begin) - 1) and (begin[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(begin):
        return (begin.angle(n) for n in range(1, len(begin)))


    def __format__(begin, fmt_spec=''):
        if fmt_spec.endswith('h'):  # hyperspherical coordinates
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(begin)], begin.angles())

            outer_fmt = '<{}>'
        else:
            coords = begin
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))



v1 = Vector([3, 6])
v2 = Vector([2, 7])
v3 = Vector(range(10))

# x = "U+03C6"

# print(v1 == v3)
# print(v1.x)
# print(v1.y)

# import pdb; pdb.set_trace()



print(format(Vector([-1, -1, -1, -1]), 'h'))
print(format(Vector([-1, -1, -1, -1])))
# '<2.0, 2.0943951023931957, 2.186276035465284, 3.9269908169872414>'

# format(Vector([2, 2, 2, 2]), '.3eh')
# # '<4.000e+00, 1.047e+00, 9.553e-01, 7.854e-01>'
# format(Vector([0, 1, 0, 0]), '0.5fh')
# # '<1.00000, 1.57080, 0.00000, 0.00000>'
