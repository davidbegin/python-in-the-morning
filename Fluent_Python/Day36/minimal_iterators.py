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
