from collections import abc



# isinstance(x, Iterable)
# implement the interface,
# and we have automatic registration
# isinstance(x, abc.Iterator)
# is abc.Iterator the same as Iterator


class NoIterable:
    pass


class WithoutNextIterator:
    def __iter__(self):
        return self


class LittleIterator:
    def __next__(self):
        raise StopIteration

    def __iter__(self):
        return self


class TrickIter(abc.Iterator):
    def __init__(self):
        self.thangs = list(range(10))

    def __getitem__(self, index):
        return self.thangs[index]

    # Both these things needed for Iterator
    def __next__(self):
        return next(self.thangs)

    # def __iter__(self):
    #     return self.thangs






