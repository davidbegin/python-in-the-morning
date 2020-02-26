from math import hypot
# class Person():
#     pass

# p1 = Person()
# p2 = Person()

# couple = p1 + p2

class Vector():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # return "%s(%r)" % (self.__class__, self.__dict__)
        return f"Vector({self.x}, {self.y})"
        # return "Vector({x!r}, {y!r})".format(x=self.x, y=self.y)
        # return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __len__(self):
        return 2

    def __bool__(self):
        if abs()

    # def __bool__(self):
    #     return False



v2 = Vector(2, 4)

import pdb; pdb.set_trace()

# v3 = v1 + v2
# v3 == Vector(4, 5)
