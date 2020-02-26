

# Does a have __iadd__?
# 	if it does, use that
# 	now if thats used, we have the same a as before.
# 	if not, we have a new object, since it uses __add__ a + b




# class FakeList():
#     def __init__(self, arr):
#         self._arr = arr

#     def __repr__(self):
#         return f"{self._arr}"

#     def __str__(self):
#         return f"{self._arr}"

#     def __add__(self, b):
#         return self._arr + b

#     def __iadd__(self, b):
#         return FakeList(self._arr + b)

# a = FakeList([1])
# b = [2]

# import pdb; pdb.set_trace()





# Flat Sequence Versus Container Sequence
# I think this is a container sequence
# Which means [30, 40] is a list reference
t = (1, 2, [30, 40])

# Return a brand new tuple, that has [50, 60] on the end?
# Now, you can't concate different types??
# t[2] += [50, 60]


# This is a list on list

# Don't think its this!
(1, 2, [30, 40], [50, 60])

# Don't think it's this!
(1, 2, [30, 40], 50, 60)

# syntax, can't concat tuple and list???

# this is my bet!!!!
(1, 2, [30, 40, 50, 60])
import pdb; pdb.set_trace()














