print('\033c')

print("\t\033[36;1;6;4;5mIt's Friday!!!\033[0m\n")


from dis import dis
import opcode

from array import array
import math


class Vector2d():
    __slots__ = ('__x', '__y', '__dict__')

    typecode = 'd'

    @classmethod
    def frombytes(cls, octets):
        # ord('d') == 100
        # chr(100) == 'd'
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)


        # If an attribute starts with at least two _'s
        # and ends with at most one _, then it will be name mangeled

        # We have a variable, that used internally in the instance,
        # but should not be exposed to the outside world
        # Not editable, by someone who instansiated an instance of
        # our class

        # Ian - Woah woah, too much magic
        #     - Double underscores is annoying


        # # Not Name mangled
        self._a = 1
        # self.___e__ = 1
        # self.____g__ = 1

        # # Name mangled
        # self.___b = 1
        # self.___d_ = 1
        # self.____c = 1
        # self.____f_ = 1
        # self._____h_ = 1
        # self.______i_ = 1
        # self._______j_ = 1
        # self.________k_ = 1
        # self.__hello_world_how__are_y__ou__ = 2
        # self.________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________z_ = 1



    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __str__(self):
        # return str(tuple(self))
        return f"({self.x}, {self.y})"

    def __repr__(self):
        # class_name = type(self).__name__
        # return '{}({!r}, {!r})'.format(class_name, *self)
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    # If we have a way of taking Bytes and then returning
    # a Vector2d, we can save money on Storage
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                                bytes(array(self.typecode, self)))

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    # Formatting mini-specifically
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)


v1 = Vector2d(3, 4)
v2 = Vector2d(4, 20)
print(bytes(v2))
v2.typecode = 'f'
print(bytes(v2))

class FloatVector2d(Vector2d):
    typecode = 'f'

v3 = FloatVector2d(4, 20)
print(bytes(v3))
print(repr(v3))



