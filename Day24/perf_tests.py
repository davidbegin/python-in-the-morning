import timeit
import array

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 100000

SETUP = """
class Vector2d():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

class Vector2d2():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

v1 = Vector2d(3, 4)
v2 = Vector2d2(3, 4)
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


# clock("Our __repr__  : ", "x = repr(v1)")
# clock("Their __repr__: ", "x = repr(v2)")

clock("Our __str__: ", "x = str(v1)")
clock("Their __str__: ", "x = str(v2)")
