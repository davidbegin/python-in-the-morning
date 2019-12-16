2019 - 12 - 12
==============

Questions
=========
  * Show we real world example of NOT using decorators when Metaprogramming
	* How can I see the bytecode difference be defining a local variable
    in a function? See var_scope.py
	* We are Told: "The name of the specialized functions is irrelevant; _ is a good choice to make this clear." However I thought _ was bad, because it could mess with internalization? What Gives???

Learnings
=========
	* singledispatch gives us Elixir style pattern matching!
  * When was PEP 318 pulled into Python?
    - 2.4 is when Decorators were pulled in
    - we got nonlocal in 3.0
  * You can always just call the decorator function like a regular callable,
    and sometimes this is useful when metaprogramming
  * Decorators are executed immediately when a module is loaded.
	* Python does not require you to declare variables, but assumes that a variable assigned in the body of a function is local.
	* free variable: This is a technical term meaning a variable that is not bound in the local scope.
		A variable becomes free when initialized in an outer functions, and referenced
    in an inner function. Now it is no longer local, and is bound the inner
    functions closure.
	* Note that the only situation in which a function may need to deal with external variables that are nonglobal is when it is nested in another function.
  * What was life like using decorators before nonlocal?
		- so if you want to modifying a immutable datastructure (a number!), in python 2,
      inner function, you would wrap it in a mutatable object
	* functools.wraps can help pass kwargs and the function_name for decorated    functions
		- functools.wraps, a helper for building well-behaved decorators
	* The letters LRU stand for Least Recently Used, meaning that the growth of the cache is limited by discarding the entries that have not been read for a while.
	* By the way, because lru_cache uses a dict to store the results, and the keys are made from the positional and keyword arguments used in the calls, all the arguments taken by the decorated function must be hashable.
	* You cannot use LRU_CACHE if the arguments you are caching are unhashable
	* When possible, register the specialized functions to handle ABCs (abstract classes) such as numbers.Integral and abc.MutableSequence instead of concrete implementations like int and list.
	* The advantage of @singledispath is supporting modular extension: each module can register a specialized function for each type it supports.

```
b = 6
def f2(a):
    print(a)
    print(b)
    b = 9
```
local variable 'b' referenced before assignment 

Ponderings
==========
  * Decorator Pattern from Gang of 4
    Decorators in Python, is more based around the complier
    - walking syntax and annotating
  * The Default __repr__ for functions will always tell
    you its a decorated function????
  * Should we always define our decorators separately from the functions
    we are decorating? Examples of not that?
	* I want to see some open source examples in Python of using singledispatch

