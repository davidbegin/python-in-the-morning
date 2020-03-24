from abc import ABC, ABCMeta
import abc
import typing

from typing import TypeVar, Generic, Any, Type, List

T = TypeVar("T")
C = TypeVar("C", bound="Semigroup")
M = TypeVar("M", bound="Monoid")

class Semigroup(Generic[T], ABC):
    def __init__(self, value: T):
      self.value = value

    @classmethod
    @abc.abstractmethod
    def append(cls: Type[C], a: C, b: C) -> C:
        raise NotImplemented

    def __eq__(self, other: Any) -> bool:
        return type(self) is type(other) and self.value == other.value




# (M,*,i)
class Monoid(Generic[T], Semigroup[T]):
    @classmethod
    @abc.abstractmethod
    def empty(cls: Type[M]) -> M:
        raise NotImplemented


class Sum(Monoid[int]):

    @classmethod
    def append(cls: Type[C], a: C, b: C) -> C:
        return cls(a.value + b.value)

    @classmethod
    def empty(cls: Type[M]) -> M:
        return cls(0)


class Product(Monoid[int]):
    @classmethod
    def append(cls: Type[C], a: C, b: C) -> C:
        return cls(a.value * b.value)

    @classmethod
    def empty(cls: Type[M]) -> M:
        return cls(1)


# Generic function, Operator on any monoid
# return a single value
def m_concat(monoid: Type[M], xs: List[M]):
    if not len(xs):
        return monoid.empty()
    x, *xs = xs
    return monoid.append(x, m_concat(monoid, xs))


