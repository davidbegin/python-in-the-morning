print('\033c')

print("\t\033[35;1;6;4;5mSaturday!\033[0m\n")


from faker import Faker
from dis import dis
import opcode

import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bingo_cage = BingoCage([1, 420, 108])

# How do I assign user attributes to this function????

from random import choice
def hello():
    """JUST THIS STUFF"""
    # __dict__
    print(f"Hello {hello.__dict__}")

hello.greeting = "Nerd!"

# a function uses the __dict__ attribute to store user attributes assigned to it.


print(hello.__doc__)
print(choice.__qualname__)
print(hello.__annotations__)
# import pdb; pdb.set_trace()


