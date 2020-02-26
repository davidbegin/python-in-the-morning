# import collections.abc
import collections

class Durf():
    pass

d = Durf()

# This works in debugger, but not when running the program
import pdb; pdb.set_trace()
print(isinstance(d, collections.abc.Sized))
