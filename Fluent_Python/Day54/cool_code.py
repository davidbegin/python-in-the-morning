print('\033c')

print("\n\t106 years ago on this date in 1914 - Copyright: In New York City the American Society of Composers, Authors and Publishers is established to protect the copyrighted musical compositions of its members.\n")


from dis import dis
import opcode



# Dog = record_factory('Dog', 'name weight owner')
# rex = Dog('Rex', 30, 'Bob')
# print(rex.name)


# field names is a string, is that the desired API
# Personally: I don't like passing in multiple arguments as white-spaced delimited strings

# a string of whitespace delimited or command-delimited
# or pass in a list

def record_factory(cls_name, field_names):
    # If I was in Ruby, I would move this to another method,
    # santize_args

    # It would be helpful to list out the supported field types
    # we support X, Y and this


    # 2 Options: LBYL vs EAFP
    #           - Always try and parse and it we fail, no big deal -> EAFP
    #           - Check if whether we need to split then split     -> LBYL

    try:
        # We only have a try, to be a to support this unbegin-friendly syntax
        # field_names = field_names.split()
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:  # no .replace or .split
        pass  # assume it's already a sequence of identifiers

    field_names = tuple(field_names)

    # If you generic initializer, that can handle any args throw at it
    # then you need this signature
    def __init__(self, *args, **kwargs):
        # Typical we use __slots__ to change the data structure type
        # we are storign attributes
        # memory savings
        # dictionary
        # self__slots__ => where we store dictionary values for a class?

        # Get all the args bassed in a mo
        print(f"ARGS: {args}")
        breakpoint()
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)

        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        values = ', '.join('{}={!r}'.format(*i) for i
                           in zip(self.__slots__, self))
        return '{}({})'.format(self.__class__.__name__, values)



    # we are creating a dictionary
    # __slots__ stored all the attributes

    # We have a dictionary
    # we have methods we defined on that different
    cls_attrs = dict(__slots__ = field_names,
                     __init__  = __init__,
                     __iter__  = __iter__,
                     __repr__  = __repr__)

    breakpoint()
    # this is the line, where __init__ is called
    # type(cls, (object, ), cls_attrs
    # type("Dorg", (object, ), {})
    # return type(cls_name, (object,), cls_attrs)



Dorg = record_factory("Dorg", "name age breed")
d1 = Dorg("Bill", 64, "Poodle")

