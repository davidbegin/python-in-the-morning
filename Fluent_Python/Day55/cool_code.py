print('\033c')

fact = "Feb 14, 1924 - The Computing-Tabulating-Recording Company changes its name to International Business Machines Corporation (IBM)."

print(f"\n{fact}\n")

from dis import dis
import opcode

def __init__(self, *args, **kwargs):
    print("Args and Kwargs and Horseshoes: {args} {kwargs}"


# This is a primitive version of class
# class or klass
# marx  was class orientedj
#
# instead of using the built in class keyword
# we inside create diction of method names, to unbound methods
# bougoisnese

# cls_attrs = dict(__slots__ = field_names,
#                  __init__  = __init__,
#                  __iter__  = __iter__,
#                  __repr__  = __repr__)

# Klass = type(cls_name, (object,), cls_attrs)






# def record_factory(cls_name, field_names):
#     try:
#         field_names = field_names.replace(',', ' ').split()  # <1>
#     except AttributeError:  # no .replace or .split
#         pass  # assume it's already a sequence of identifiers
#     field_names = tuple(field_names)  # <2>

#     def __init__(self, *args, **kwargs):  # <3>
#         attrs = dict(zip(self.__slots__, args))
#         attrs.update(kwargs)
#         for name, value in attrs.items():
#             setattr(self, name, value)

#     def __iter__(self):  # <4>
#         for name in self.__slots__:
#             yield getattr(self, name)

#     def __repr__(self):  # <5>
#         values = ', '.join('{}={!r}'.format(*i) for i
#                            in zip(self.__slots__, self))
#         return '{}({})'.format(self.__class__.__name__, values)

#     cls_attrs = dict(__slots__ = field_names,  # <6>
#                      __init__  = __init__,
#                      __iter__  = __iter__,
#                      __repr__  = __repr__)

#     return type(cls_name, (object,), cls_attrs)  # <7>
# # END RECORD_FACTORY

