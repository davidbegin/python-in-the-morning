2019 - 12 - 18
==============

Questions
=========
	* Where else (outside of caching applications) are weak references
		useful?
	* I want a real open-source example of using WeakKeyDictionary

Learnings
=========
	* If an object is immutable, you probably only want to compare value NOT identitiy
		- The exception is immutable collections such as tuples and frozensets: if an immutable collection holds references to mutable items, 
	* The sharing of string literals is an optimization technique called interning. CPython uses the same technique with small integers to avoid unnecessary duplication of “popular” numbers like 0, –1, and 42. Note that CPython does not intern all strings or integers, and the criteria it uses to do so is an undocumented implementation detail.


	* If you need to build a class that is aware of every one of its instances, a good solution is to create a class attribute with a WeakSet to hold the references to the instances.
	* Weak references to an object do not increase its reference count. The object that is the target of a reference is called the referent. Therefore, we say that a weak reference does not prevent the referent from being garbage collected.
  * The del statement deletes names, not objects.
  * Rebinding a variable may also cause the number of references to an object to reach zero, causing its destruction.
  * If in doubt, make a copy. Your clients will often be happier.
  * You: Hey I see you are using a empty list of a default value for a parameter
    in a function defintion.....Don't
    Them: Why?
    You: The problem is that each default value is evaluated when the function is defined—i.e., usually when the module is loaded—and the default values become attributes of the function object. So if a default value is a mutable object, and you change it, the change will affect every future call of the function.
  * When you are coding a function that receives a mutable parameter, you should carefully consider whether the caller expects the argument passed to be changed.

Ponderings
==========
  * Is there a linter out there, that checks for mutable default arguments?
  * What is the full list of built types that are mutable?
    - List

  * Personal Prefer:
    - don't modify the object
    - make a copy, modify and return that
    Pros:
      - Easier to reason about the system
        - you always know what value a variable (typically)
    Cons:
      - Copy objects, more memory! slower! Less performant!
      - More code to copy and maintain
  * upcase, upcase!, upcase?
    upcase, non-mutating
    ! == mutating
    ? == predicate method, is this upcased


don't modify state
return new versions of objects
simple functions that do one thing that are composable


Quote
=====
  * It’s really a matter of aligning the expectation of the coder of the function and that of the caller.




Garbage Collection Algs:
    - reference counting
    - mark and sweep
    - generational garbage





When thinking about Weak References:
	* user-defined classes are always usable as weak references
	* various built-in types, not so much: List, Dict, Int, Tuple
	* But things like Set are
	* This is also based on python interperator




Weak Reference:
	- If I am last Refence to this object, Garbage Collect it
