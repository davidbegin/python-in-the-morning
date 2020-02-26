print('\033c')

fact = "1996 - In Philadelphia, world champion Garry Kasparov beats the Deep Blue supercomputer in a chess match."

print(f"\t{fact}!\n")

from dis import dis
import opcode


# class MyClass(MySuperClass, MyMixin):

class MyMixin:
    pass

class MySuperClass:
    pass


MyClass = type('MyClass', (MySuperClass, MyMixin),
               {'x': 42, 'x2': lambda self: self.x * 2})

a1 = MyClass()
breakpoint()


