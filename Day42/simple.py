import types

def func():
    yield
    print("func")

@types.coroutine
def coro_func():
    yield
    print("func")

n1 = func()
c1 = coro_func()

breakpoint()


