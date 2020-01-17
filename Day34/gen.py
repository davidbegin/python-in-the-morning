print('\033c')
print("\t\033[36;1;6;4;5mFriday Friday Friday!\033[0m\n")


from dis import dis
import opcode

import re
import reprlib

def fake_func():
    yield 1
    yield 2
    raise TypeError

def fake_func2():
    return 1

f1 = """
def fake_func():
    yield 1
    yield 2
"""


f2 = """
def fake_func2():
    return 1
"""



g1 = fake_func()

# for x in g1:
#     print(x)

print(next(g1))
print(next(g1))
# print(next(g1))
# import pdb; pdb.set_trace()

# print(f"\n\n\033[035m{f1}\033[0m")
# dis(fake_func)
# print(f"\n\n\033[35m{f2}\033[0m")
# dis(fake_func2)
# import pdb; pdb.set_trace()








