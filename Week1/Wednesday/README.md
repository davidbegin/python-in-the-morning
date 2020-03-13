2020 - 2 - 26
=============

Resources
=========
- https://www.python.org/dev/peps/pep-0519/#standard-library-changes
- https://www.python.org/dev/peps/pep-0584/
- https://www.wikiwand.com/en/Nick_Leeson
- https://vim.fandom.com/wiki/Copy,_cut_and_paste

Bounties
========
- Fake screenfetch or neofetch that shows windows 95
  - Sub

- Make Pep Graaveyard of all the features rejevcted from PEP


strager: I am against |= because list += is fscked


Do you mean we matching the syntax of +=
Why is += evil


Giving a pipe operator to mappings is an invitation to writing code that doesn't scale well. Repeated dict union is inefficient: d | e | f | g | h creates and destroys three temporary mappings.

isidentical: I am against it because there are already 2 different ways to do this (unpacking for |, update for |=). It is really rare that you need to care about subtypes


gainst it because there are already 2 diff


When we are adding things to a language, we have ask ourselves, are we
making easier for users from code










Viewer Questions
================

Questions
=========
- BDFL = Benevolent Dictator for Life
  - How does Delegate BDFL work?
  - There were delegates always
- When will we want to use update and {**, **}

Learnings
=========
This PEP proposes adding merge (|) and update (|=) operators to the built-in dict class.

```
{} | {}
{} |= {}
```

dict.update
d1.update(d2) modifies d1 in-place. e = d1.copy(); e.update(d2) is not an expression and needs a temporary variable.

{**d1, **d2}
Dict unpacking looks ugly and is not easily discoverable. Few people would be able to guess what it means the first time they see it, or think of it as the "obvious way" to merge two dicts.


Why do we need this PEP:
- We need to python merging
- Problems with the current way:
  - ** method undiscoverable, doesn't work for dictionary subclasses
  - update always modifies in place



Why would you use Chainmap:
- Multiple Mappings
  - Mappings with backups

Page people
- Grab from this mapping, no one there, go to this default mapping

Aliases for bot command, with fallbacks


>>> d1 = {'spam': 1}
>>> d2 = {'eggs': 2}
>>> merged = ChainMap(d2, d1)
>>> merged['eggs'] = 999
>>> d2
{'eggs': 999}



+ and += for list.extend
| and |= for dict.update




ChainMap resolves first seen
Dict update, resolves to the right side



dict merging is commutative
commutative means you reverse the operand and get the same result

d | e != e | d


d1.update(d2)
d1 |= d2


```
>>> import types
>>> a.barFighters = types.MethodType( barFighters, a )
>>> a.barFighters
<bound method ?.barFighters of <__main__.A instance at 0x00A9BC88>>
>>> a.barFighters()
barFighters
```

we can use the new Union syntax with any thing that implements the mapping
protocal: __getitem__ keys(), or iterables of key value pairs


isidentical: you can actually try it by checking the master (alpha 4), and compiling it
isidentical: it is really easy just 2 commonds ./configure && make -j8

bpo = bugs.python.org



PEP-584: starting as + in C



 if you This was an error before, but it is legit now (totally disagree and doesnt make any sense to add dicts so this is still an error, because the PR changed union from plus and sum isn't work)

sum([{2:3}, {2:3}]) = {2:3} + {2:3}. 



Why does adding functionality to dicts, make the collections tests fail.


We were testing functionality threw an error:
  - Add that functionality, update the test, from error from functionality
  - Debate: is that a good test?




Ponderings
==========

Opinions
========



Begin Big Believer in waking up ealier
Controverisal programmer opinion
The key to waking up early, going to sleep early

Waking up early pro-tip: remember its 5 minutes of war
 - survive that 5 minute
 - drink some water
 - to the bathroom
 - do a lil dance



Junior Engineers are afraid to delete code
Even worse, they are double afraid to remove their own


Don't just comment out code, unless you plan on commenting, then
maybe it make it configurable


Debates
=======
Why are you obssessed KDE?

{**d1, **d2}
is dict merging with ** pythonic?

ArtMattDank: ive liked lubuntu because ive been able to install it on any garbage machine ive had


isidentical: C++ sucks more then every language


Brainfuck can be more optimized than C++

Theres more security research, pen-testing, exploits



hjkl

There is no such koan. "Only One Way" is a calumny about Python originating long ago from the Perl community.




userman2: i think dicts supporting | will not be used very often, and so seeing as it should not be used often, its a case of "will the side effects of possible value removed, and performance possiblities impact this use case"


TODO:
=====
- blurbit
https://github.com/python/cpython/pull/18609/files

Confessions
===========

Python Interview
================
- Why is python merging with update or {**, **} not commutative?

Quotes
======

"Everything is fast for small enough N"

You do whatever want in whatever language, just have fun while you doing
- Begin



Scraps
======

TODO
====
- http://pythontutor.com/
