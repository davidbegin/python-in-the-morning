2020 - 1 - 10
=============

TODO:
=====
  * Write up / Look up more on Goose Typing

Questions
=========
	* would you ever use this syntax, in pyhton 3.4+
 			`class Tombola(metaclass=abc.ABCMeta):`
  * How do classes register themselves, when you fufill a protocol
    __len__
    sized -> ABC
    collections.ABC.sized
  * If you build your own custom ABC,
    can you get this lookup behavoir, like Sized

  * Why do  some ABCs self-register?

  * Ruby Doesn't have ABCs
  * 



Challenge
=========
  * I’ve never seen subclasses of either Callable or Hashable. 

  * Name the Numerical Tower: Top to Bottom:
    * Number
    * Complex
    * Real
    * Rational
    * Integral

  NCRRI
  NC-Double-R-I

Learnings
=========
  * Just cuz its works debugger, doesn't mean imports are correct
  * Mix functional and OO is the wave of future
      - OO to Nth is kinda crazy
      - Pure functional, while cool, impractical
  * why are some namespaced under ABC?
      - they all are, the others are being deprecated
  * is collections.MutableSequence an ABC?
    - Yes it is!!

  * bool (which subclasses int)

	* An abstract method can actually have an implementation. Even if it does, subclasses will still be forced to override it, but they will be able to invoke the abstract method with super()

	* When abstractmethod() is applied in combination with other method descriptors, it should be applied as the innermost decorator,

```
Somewhat surprisingly, decimal.Decimal is not registered as a virtual subclass of numbers.Real. The reason is that, if you need the precision of Decimal in your program, then you want to be protected from accidental mixing of decimals with other less precise numeric types, particularly floats.
```



When passed in some data, or an object into a class:
  * Can we copy the data?
  * Will we need to modify the data?


Ponderings
==========


Personal Opinions
===============


Ponderings
==========



Later
=====

embraced that functions operate on data.

Person as a datatype with functions that operate on it is how I like to code now.

think of Person as a Datatype, not as a "class"
classes are Data-Containers with functions to operate on them

is this is stateful, or its not



Variation:
  - Mallard Typing
    - Multi-Duck Typing
      - Are you this duck
      - Are you another duck

Smaller Waterfowl

```
Duck-Typing
person.name()

Goose-Typing
if isstance(person, abc.Talker):
  person.name()

Swan-Typing
if isstance(person, Person):
  person.name()
```




Duck Typing
  - Don't care about your class
  - Do you have the right interface, right methods?


Goose Typing
  - You need to be part of the Abstract Base Class Family
# isinstance and are checking against an Abstract Base Class
isinstance(d, collections.abc.Sized)




Does it have the behavoir of a the 
