import timeit
import array

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 10000000

SETUP = """
class A:
    def ping(self):
        print('A ping:', self)

class Z:
    def pong(self):
        print("Z PONG!!!!")

# ====================================================================

class B(Z):
    def bpong(self):
        print('B pong:', self)


class C(A):
    def pong(self):
        print('C PONG:', self)

# ====================================================================


class Y:
    def pong(self):
        return "Y PONG"

class X(Y):
    def pong(self):
        super().pong()

class J(Y):
    def pong(self):
        Y.pong(self)


class K():
    def pong(self):
        Y.pong(self)

class E:
    pass

class R:
    def pong(self):
        return "R Pong"


class H(E, R):
    def pong(self):
        super().pong()


class F():
    def pong(self):
        return "F Pong"

class T(F):
    pass

class D(T):
    def pong(self):
        super().pong()
"""


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


# How much is an extra class lookup
clock("No Lookup          : ", "Y().pong()")
clock("Single Lookup      : ", "X().pong()")
clock("Single Explict     : ", "J().pong()")
clock("Single Explict WOI : ", "K().pong()")
clock("Parallel Call      : ", "H().pong()")
clock("2 Deep             : ", "D().pong()")
