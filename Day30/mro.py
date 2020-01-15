def pmro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))

