print('\033c')

print("\t\033[35;1;6;4;5mTuesday Time To Chase Our Dreams!\033[0m\n")


import itertools
from dis import dis
import opcode

# map
# reduce
# filter

# itertools.compress
# itertools.dropwhile
# itertools.takewhile
# itertools.filterfalse
# itertools.isslice


from collections.abc import Iterator, Iterable



# Not an Iterator
class NotTrickDurf():
    def __next__(self):
        return 1


# Is an Iterator!!! but not an iterable
class TrickDurf(Iterator):
    def __next__(self):
        return 1


# This is an Iterator, that automatically subclassed
class Durf:
    def __next__(self):
        return 1

    def __iter__(self):
        return self



print(isinstance(range(0), Iterator))
print(isinstance(Durf(), Iterator))
print(isinstance(TrickDurf(), Iterator))
print(isinstance(NotTrickDurf(), Iterator))



breakpoint()

# print(isinstance(range(0), Iterable))


# ['Iterable', 'Iterator',

# from collections.abc import Sequence
# breakpoint()


# list(itertools.filterfalse(vowel, 'Aardvark'))
# list(itertools.dropwhile(vowel, 'Aardvark'))
# list(itertools.takewhile(vowel, 'Aardvark'))
# list(itertools.compress('Aardvark', (1,0,1,1,0,1)))
# list(itertools.islice('Aardvark', 4))
# list(itertools.islice('Aardvark', 4, 7))
# list(itertools.islice('Aardvark', 1, 7, 2))









