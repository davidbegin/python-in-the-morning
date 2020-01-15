print('\033c')

print("\t\033[31;1;6;4;5mTuesday and Time to Learn!\033[0m\n")


from dis import dis
import opcode


import decimal

# What do yall do with decimals in this file, lemme hold on to
# those settings
ctx = decimal.getcontext()
ctx.prec = 40
one_third = decimal.Decimal('1') / decimal.Decimal('3')
# import pdb; pdb.set_trace()

# decimal.Decimal('0.3333333333333333333333333333333333333333')
print(one_third == +one_third)
ctx.prec = 2
print(+one_third)
# print(one_third == +one_third)



from collections import Counter

from array import array
import reprlib

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = list(components)
        # self._components = array(self.typecode, components)

    def __eq__(self, other):
        return all(x == y for x, y in zip(self, other))

    def __iter__(self):
        return iter(self._components)

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __invert__(self):
        return Vector((~x for x in self))

    def __add__(self, other):
        return Vector([ x + y for x, y in zip(self, other) ])

        # pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        # return Vector(a + b for a, b in pairs)
