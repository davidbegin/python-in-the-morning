2020 - 2 - 10
=============


Problem: We have bunch data stored in a Database, and we are sick of writing code to get it out.

Dawgz:
- name
- breed
- fave_toy


Descriptor
==========
- sharing logical for connecting an attribute name to the value
- ORM:

d = Dawg()
d.name
Desriptor -> says woah name, on a class called Dawg, well,
I will give the name out the DB



What we do here
---------------
- Yes we are learning python
- we also compare against other lanaguages
- try to think why python chose a direction
- are there other methods better



























Fake Interview Questions
========================
- What is the difference between a factory and a constructor?
  - factories can create objects of other classes (or their own class?)
  - factories can also return already created objects (ala a singleton, eigenclass)
  - constructors contstruct objects of the class they are defined?

Big Goals
=========
- Break the perception, that you are or are not a programmer,
  instead of someone who knows how to do any programming

  Analogy: when do I call myself a gamer?

  Philosopical Debates:
  ---------------------
  - when are you "good" enough to call yourself something?
  - why does a hobby have to be an identity?


Goals
=====
- Learn some python
  - metaprogramming
- Have fun
- By tomorrow, I want to try and do a mini Takayoshi presentation using suck
- Understand what happened when I make clean installed sent and farbfeld



Things Begin Broke
==================
- Copy and Pasting
- Black is crashing my terminal!!!



Things Begin Like
=================
- in ruby, there were some regional style differences
  - seattle style of ruby

```
a_func(a_param)

# Seattle Style
a_func a_param
```

What is New England Python Style?


Viewer Questions
================

Questions
=========
- Metaclass Confusion is confusing to me




Learnings
=========
- Special methods are only invoked on the class, not on an instance of a class,
  if you overroad a special method

  When discussing special method lookup, we are really discussing pythons
  implementation of operator overloading

  python - don't override the exact method, override these special dunder or __ methods
           and we (python) will give you some cool syntax and override some behavoir.

           Caveat:

           you can't override these special "dunder" methods on just an instance,
           you have to do it on a "type" (I want to "class" - begin)


What are descriptors?
- reusing logic the connects a name to the value of a attribute.
Example: ORM, we say this name, and the ORM knows where to look
in a DB (reusing the logic) to find the value




API Design Review
-----------------
- a method comes across our desk that has the following characteristics:
  - no arguments (besides self)
  - returns a value
  - pure function, no side affects

Sounds like a read-only property to me



Defintions associated with using Descriptors

Managed Class

Managed Instance
  - an instance of the class that uses descriptors for class attributes
  -
Descriptor class
  - defines the flow of data from name to value

Descriptor Instance
  - instance of the descriptor class, that wraps a class attribute of a Managed class

Managed attribute:
  - A public attribute in the managed class that will be handled by a descriptor instance, with values stored in storage attributes. In other words, a descriptor instance and a storage attribute provide the infrastructure for a managed attribute.

Storage attribute:
  - An attribute of the managed instance that will hold the value of a managed attribute for that particular instance.


When coding a __set__ method, you must keep in mind what the self and instance arguments mean: self is the descriptor instance, and instance is the managed instance. Descriptors managing instance attributes should store values in the managed instances. That’s why Python provides the instance argument to the descriptor methods.



Descriptors are used as Class attributes.
This means that if we have thousands of instances of said class,
we will only have the single defition of the descriptors as a class attribute.

So if you changed attributes on a Descriptor, you are changing every single
managed instance's class attribute (since its shared (hence why its a class attr not an instance attr))


















Begin Book Rant
===============
- People only want to finish books for their ego
- Example: Tech book, can you absorb all of it over a reading period?
- Personal Tech Book Style: read until you want to program and mess up stuff,
  don't pick it back up until you are stuck.
  I need to brush up on Stubs: Im pulling GOOSE growing object oriented software guuided by tests
- You can have 10 tech books juggling. Git, Database, Architecture, Language specific

Stupac Opinion: don't read on the same but different subjects at the same time.
Example: MongoDB and Postgresql
Caveat: Experience Matters
Begin's Counter Argument: if you are reading and activly comparing the two.


Ponderings
==========

Opinions
========

Debates
=======

Confessions
===========

Python Interview
================

Quotes
======

Scraps
======

