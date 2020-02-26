from abc import ABC

class Durf():
    pass

class MyABC(ABC):
    pass

MyABC.register(tuple)

assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)

MyABC.register(Durf)

assert isinstance(Durf(), MyABC)
