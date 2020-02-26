print('\033c')

print("\t\033[35;1;6;4;5mBest Wednesday Ever! \033[0m\n")


from dis import dis
import opcode

# list is mutable
# string, number, tuple nah


# a1 = "strang"
# b1 = "cool"

# Notice how the object identity stays the same!
a1 = [1, 2]
print(id(a1))
b1 = [2, 3]

# Notice how the object identity changes after the +=
a1 = 1
print(id(a1))
b1 = 3

def f(a, b):
    print(id(a))
    a += b

    # this changes identity
    print(id(a))
    return a


c1 = f(a1, b1)
print(id(c1))
# print(c1)
