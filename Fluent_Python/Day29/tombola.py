print("\033c")
import abc

class Wow():
    pass

class Durf(abc.ABC):
    pass

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable."""

    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it.

        This method should raise `LookupError` when the instance is empty.
        """

    def loaded(self):
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())


    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


import random

class BingoCage(Tombola):

    def __init__(self, items):
        # What is SystemRandom!!!??
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)

        # this must be modifying the order of self._items in place
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


import random


class LotteryBlower(Tombola, Wow):

    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty BingoCage')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


@Tombola.register
@Durf.register
class FakeClass():
    pass

l1 = LotteryBlower(range(1000))
b1 = BingoCage(list(range(1000)))
f1 = FakeClass()

print(BingoCage.__subclasses__())

x = abc._get_dump(Tombola)
import pdb; pdb.set_trace()

virtual_subclasses = [ref() for ref in abc._get_dump(Tombola)[0] if ref()]
print(virtual_subclasses)


# print(isinstance(l1, Tombola))
# print(isinstance(b1, Tombola))
# print(isinstance(f1, Tombola))
# print(isinstance(f1, Durf))

import pdb; pdb.set_trace()

