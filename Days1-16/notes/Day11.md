Day 11
======

Questions
=========
  * Why is called collections.abc?
    IS it because of the ABC language?
    Abstract Base Classes
    This went from `collections to collections.abc in Python 3.3`
  * Deeper understanding of Atomic types in the world of Python
  * What is a defaultdict for?
    only support copy.copy
    default_factory
    We don’t always need it, but when we do, it provides a significant speedup by avoiding redundant key lookups.


Learnings
=========
  * Using isinstance is better than checking whether a function argument is of dict type,
    because then alternative mapping types can be used.
    NO: `isinstance(dict)`
    YES: `isinstance(abc.Mapping)`
  * At the time of this writing, the Python Glossary states:
    “All of Python’s immutable built-in objects are hashable” but that is inaccurate because a tuple is immutable, yet it may contain references to unhashable objects.
  * User-defined types are hashable by default because their hash value is their id() and they all compare not equal. If an object implements a custom __eq__ that takes into account its internal state, it may be hashable only if all its attributes are immutable.
  * index.setdefault(word, []).append(location)

Ponderings
==========
  * Implementations of specialized mappings often extend dict or collections.UserDict, instead of these ABCs. The main value of the ABCs is documenting and formalizing the minimal interfaces for mappings, and serving as criteria for isinstance tests in code that needs to support mappings in a broad sense:
  * I want an example of User defined class with custom hashing, open source prefereably








Special Methods

Pre-Qualifications
  You wanna play with the Lists?


you walk like a duck,
quack like a duck
you are a duck
treat you like a duck





__contains__
x in y

__eq__
x == y

__setitem__
item[k] = v





p.name
p.age
p.catchphrase


p.__len__

def __len__():

```
```


