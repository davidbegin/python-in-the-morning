from abc import ABC, ABCMeta
import abc
import typing

from typing import TypeVar, Generic, Any

T = TypeVar("T")


# THIS DOESN'T WORK as expected
# class Semigroup(ABC, Generic[T]):

# We need an append,
# Because this is always binary associative operators
# BAO = a two argument function which is associative
# BAO = a two argument function returns 1 thing

# (M,*) =====
# let M = T
# let * = append
# mathematical closure - when combining two elements of of the same type you get
# the same type
class Semigroup(Generic[T], ABC):
    def __init__(self, value: T):
      self.value = value

    @classmethod
    @abc.abstractmethod
    def append(cls: Class[T], a: Generic[T], b: Generic[T]) -> Generic[T]:
        raise NotImplemented

    def __eq__(self, other: Any) -> bool:
        return type(self) is type(other) and self.value == other.value


# (M,*,i)
class Monoid(Generic[T], Semigroup[T]):
    @abc.abstractmethod
    def empty(self) -> 'Monoid[T]':
        raise NotImplemented


# Types are Sets are similiar concetps
# Type int
# Set 0..infinity
# Type str: a..z

# (M,*,i)
# - M is a set
# - * is a binary associative operator
# - i is identity
#
# Example
# let M = str
# let * = +
# let i = ''

# let a, b, c E M (a,b,c are strings)
# such that
# (a + b) + c = a + (b + c)


# if the set and binary associative operator have an "identity"
# then it is Monoid

# 
# do ABC type annotations have any effect on the extender


class Sum(Monoid[int]):

    @staticmethod
    def append(a: 'Sum', b: 'Sum') -> 'Sum':
        return Sum(a.value + b.value)

    @staticmethod
    def empty() -> 'Sum':
        return Sum(0)
    








class Product():
    pass

# strager: Isn't it something like this: @classmethod @abc.abstractmethod def append(cls: Class[C], a: C, b: C) -> C: ...
