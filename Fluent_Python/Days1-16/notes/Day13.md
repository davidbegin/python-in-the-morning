Day 13
======

Goals:
------
  * Learn some Python!
  * Take detours for fun!
  * Try out the new AWS Lambda Destinations™
  * Try out the new X-Ray abilities
  * Update our Lambda Functions to Python 3.8
  * Maybe some Dungeon Crawl in the Afternoon

Questions
---------
  * In Math, what is the name for 1st set versus 2nd set
  * How do we see the free_dicts in python? Not in Cpython
  * Why did iteritems go???

Learnings
----------
  * Use MappingProxyType to make a Mapping Immutable
  * There’s no literal notation for the empty set, so we must remember to write set()
  * S ⊆ Z = Subset
  * S ∈ Z = Contains
  * set dunder methods
    - le = subset
    - lt = proper subset
    - ge = superset
    - gt = proper superset
  * If your program does any kind of I/O,
      the lookup time for keys in dicts or sets is negligible,
      regardless of the dict or set size (as long as it does fit in RAM).
  * What does class Person() inherit from? to give it __hash__
      - User-defined types are hashable by default because their hash value is their id() and they all compare not equal.
  * id() - CPython implementation detail: This is the address of the object in memory.
  * For user-defined types, the __slots__ class attribute changes the storage of instance attributes from a dict to a tuple in each instance.
  * Optimization is the altar where maintainability is sacrificed.
  * The dict implementation is an example of trading space for time:
  * DONT LOOP OF DICTS AND ADD TO THEM AT THE SAME TIME!!!!
  * Module contents are also represented as a dictionary, most notably the _ _builtin_ _ module that contains built-in identifiers such as int and open. Any expression that uses such built-ins will therefore result in a few dictionary lookups.
    - If you are iterating over the dictionary keys and changing them at the same time, your loop may not scan all the items as expected—not even the items that were already in the dictionary before you added to it.
  * The PyDictObject also contains space for an eight-slot hash table. Small dictionaries with five elements or fewer can be stored in this table, saving the time cost of an extra malloc() call. This also improves cache locality; for example, PyDictObject structures occupy 124 bytes of space when using x86 GCC and therefore can fit into two 64-byte cache lines. The dictionaries used for keyword arguments most commonly have one to three keys, so this optimization helps improve function-call performance.
  * > 50,000 keys use ma_used*2
  * < 50,000 keys use ma_used*4
  * This means dictionaries are never resized on deletion.

Ponderings
----------
  * Is there a speed difference in built in infix operators?
  * Written by A.M. Kuchling—a Python core contributor and author of many pages of the official Python docs and how-tos—Chapter 18, “Python’s Dictionary Implementation: Being All Things to All People,” in the book Beautiful Code (O’Reilly) includes a detailed explanation of the inner workings of the Python dict. Also, there are lots of comments in the source code of the dictobject.c CPython module. Brandon Craig Rhodes’ presentation The Mighty Dictionary is excellent and shows how hash tables work by using lots of slides with… tables!
  *  I could not find a PEP for setcomps; apparently they were adopted because they get along well with their siblings—a jolly good reason.
    - THE Case of the Missing PEP: Setcomps
  * I want an open source bug because of: dictionaries never resizing on deletion.



# (The extensive comments in Objects/dictobject.c discuss the history of this optimization in more detail.)
# Rewrite this in Python
```
  /* Starting slot */
  slot = hash;

  /* Initial perturbation value */
  perturb = hash;
  while (<slot is full> && <item in slot doesn't equal the key>) {
      slot = (5*slot) + 1 + perturb;
      perturb >>= 5;
  }
```
