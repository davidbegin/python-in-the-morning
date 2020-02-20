from abc import ABCMeta

class Durf(metaclass=ABCMeta):

    def __init__(cls, name, bases, namespace):
        print("Welcome to Durf")

class Nerf():
    pass

class Plerf(Durf):
    pass

Durf.register(Nerf)



p = Plerf()
n = Nerf()
breakpoint()
print(isinstance(p, Durf))
print(isinstance(n, Durf))
