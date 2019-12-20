print('\033c')

print("\t\033[35;1;6;4;5mBest Thursday Ever!\033[0m\n")


from dis import dis
import opcode





class Person():

    def __format__(self, kwargs):
        return "Fake Formatting"

    # __bytes__ has to return bytes
    def __bytes__(self):
        return b"\033c"


person = Person()

# print(format(person))
# print("Hello".format())
# print(person.format())
# print(bytes(person))



# 'ABC'
# 123
# Person(name="bane")
# [][][][][][][1]
# [][][][][][][][][][]["A"]["B"]["C"]

# double - mininum of 8 bytes


# We want to store some info
# What size????
# This size?
# Double Size - Info


from array import array


class Vector2d():
    typecode = 'd'

    @classmethod
    def frombytes(cls, octets):
        # ord('d') == 100
        # chr(100) == 'd'
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

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

    # How does this make me money?

    # If we have a way of taking Bytes and then returning
    # a Vector2d, we can save money on Storage
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                                bytes(array(self.typecode, self)))


    def __abs__(self):
        return 5.0

    def __bool__(self):
        return self.x != 0 or self.y != 0





v1 = Vector2d(3, 4)
print(v1.x, v1.y)

# This is cool tuple behavoir
# TypeError: cannot unpack non-iterable Vector2d object
x, y = v1


# __repr__ is for developers
# If you do repr right, then you should be able
# to instansiate an object with eval
# <__main__.Vector2d object at 0x10342bb50>
v1_clone = eval(repr(v1))


v2 = Vector2d(1, 2)

print(v1 == v1_clone)
print(v1 == v2)
# True

print(v1 is v1_clone)
# # False


print(v1)
# # (3.0, 4.0)


octets = bytes(v1)
print(octets)
# # >>> octets

print(abs(v1))
# # 5.0

print(bool(v1))
print(bool(Vector2d(0, 0)))



raw_bytes = bytes(v1)
print(raw_bytes)
raw_bytes = b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'

# memv = memoryview(octets[1:]).cast(typecode)
# TypeError: memoryview: length is not a multiple of itemsize
v2 = Vector2d.frombytes(raw_bytes)
import pdb; pdb.set_trace()









