Day 3
=====


Questions
=========
  * Difference between an Array and a List?
  * list, tuple, collections.deque, set
    - when each???
  * strs and bytes are immutible??? What happens when you concate strs?
  * Why does a mutable sequence get the method reverse??
  * What iadd?
  * What do you use a memoryview?
  * What is a generator expression?
  * why are list comprehensions faster?


Learnings
=========
  * Container sequences hold references to the objects they contain,
    which may be of any type, while flat sequences physically store the
    value of each item within its own memory space,
    and not as distinct objects. Thus, flat sequences are more compact,
    but they are limited to holding primitive values like characters,
    bytes, and numbers.
  * List comps ain't for Side Effects, for the Result
  * If the list comprehension spans more than two lines, it is probably best to break it apart or rewrite as a plain old for loop.
  * In Python code, line breaks are ignored inside pairs of [], {}, or (). So you can build multiline lists, listcomps, genexps, dictionaries and the like without using the ugly \ line continuation escape.
  * To initialize tuples, arrays, and other types of sequences, you could also start from a listcomp, but a genexp saves memory because it yields items one by one using the iterator protocol instead of building a whole list just to feed another constructor.
