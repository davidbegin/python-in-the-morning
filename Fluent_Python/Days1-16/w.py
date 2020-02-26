# Clears Terminal
print('\033c')
print("\t\033[36;1mWednesday!\033[0m\n")


from array import array
from random import random

a1 = array('u')
print(a1.typecode)

cool_array = array('d', (random() for i in range(10**6)))
print(cool_array.itemsize)
print(len(cool_array))

a_list = [1, 2, 3]
cool_array.fromlist(a_list)

print(len(cool_array))










# fp = open("floats.bin", "wb")
# cool_array.tofile(fp)
# fp.close()

# fp = open("floats.bin", "rb")
# a2 = array("d")

# # How do I say read the whole file???
# a2.fromfile(fp, 10**7)
# fp.close()

# print(len(a2))


