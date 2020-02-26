import dis

print('\033c')


b = 6

def f1(a):
    global b
    print(a)
    print(b)
    b = 9

def f2(a):
    global b
    print(a)
    print(b)
    b = 9
    return b


def f3(a):
    print(a)
    print(b)

# Python is made I referenced a global variable
# Then created a local with the same name???

doc2 = """
def f2(a):
    print(a)
    print(b)
    b = 9
"""

doc3 = """
def f3(a):
    print(a)
    print(b)
"""

print(f"{doc2}")
print(dis.dis(f2))
# print(f"{doc3}")
# print(dis.dis(f3))
