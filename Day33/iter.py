print("\033c")
print("\n\t\033[36mHello Begin\033[0m")

import re
import reprlib


# I don't like saying compile
# it doesn't feel natural in the context of a regular expression
RE_WORD = re.compile('\w+')



class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    # def __iter__(self):
    #     pass

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


s1 = Sentence("Probably about 20 to 30 percent of the population think of operator overloading as the spawn of the devil")







class Iterator(Iterable):

    # How we store variables in memory?
    __slots__ = ()

    @abstractmethod
    def __next__(self):
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration

    def __iter__(self):
        return self

    @classmethod
    def __subclasshook__(cls, C):

        # this is prevent subclasses of Iterator, from getting
        # Automatic registration????
        if cls is Iterator:
            if (any("__next__" in B.__dict__ for B in C.__mro__) and
                any("__iter__" in B.__dict__ for B in C.__mro__)):
                return True
        return NotImplemented





