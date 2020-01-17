import pytest

from it import NoIterable
from it import LittleIterator
from it import WithoutNextIterator
from it import TrickIter
from collections import abc

def test_not_iterable():
    subject = NoIterable()
    assert not isinstance(subject, abc.Iterator)

def test_without_next():
    subject = WithoutNextIterator()
    assert not isinstance(subject, abc.Iterator)

def test_little_iterator():
    subject = LittleIterator()
    assert isinstance(subject, abc.Iterator)

def test_checking_for_iteratable():
    subject = LittleIterator()
    assert isinstance(subject, abc.Iterable)

# Goal: Make an abc.Iterable check fail, when it shouldn't

def test_checking_for_iteratable_bad():
    subject = TrickIter()
    assert isinstance(subject, abc.Iterable)


@pytest.mark.focus
def test_checking_for_iterator_bad():
    subject = TrickIter()
    assert isinstance(subject, abc.Iterator)






