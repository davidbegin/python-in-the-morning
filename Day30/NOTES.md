2020 - 1 - 13
======



Goal: I need to learn when to do something and when not to
When to Test
Overtest or you can undertest

Someone gives you a rule, when do you break it???

Strategy:
=========
	* You can HAM and overuse it everywhere.
		This is not the final goal
		Everytime it hurts to use, you want pay attention, learn
		research, figure out why its painful
		Eventually: you'll have a bunch of experiences when it's painful
		AND the skills to use it painful places if needed, or use it anywhere.


TOOOO Many Tests
TOOOO Much Documentation
TOOOO Many Code Comments
TOOOO many MemoryViews

Go Overbaord
Learn when to real back


do this in your code
not in open source
company code is fine







Personal Opinion on Inheritance:
=================
  * Not a Fan
  * Use it sparingly
  * Only one level deep
  * Every child needs to use every method inherited


No Personal Opinion on Multiple Inheritance
I have no real experience with it
It scares


Python does have multiple inheritance


Daily Goal
==========
  * Say "Take that and double it!" to real people


Questions
=========
  * Is there a pep to fix this crazy built-in subclasses
    C is the problem.
  * What made super() so great in python3

  * How does MRO work with Mixins



in Ruby Module versus class



Claim on the internet: mixins only exist in multiple-inheritance languages. 
What about Ruby?
  include module
  thats a Mixin


Who are the Gang of Four?


Is this inheritance ripe for delegation?
	Are there any methods that aren't this classes job??
		Maybe you could delegate that job!!!!



Learnings
=========
	* because subclassing is a form of tight coupling,
 		and tall inheritance trees tend to be brittle.
	* Me Personally "I Favor Object Composition Over Class Inheritance."
	* Concrete classes should have zero or at most one concrete superclass.
 		In other words, all but one of the superclasses of a concrete class
 		should be ABCs or mixins.
  * Me: Woah woah, don't subclass a built-in type
    Them: Why
    Me: Listen them built in types list `list` or `dict`, they have
        methods implemented in C, for optimizations and what not.
        If you override these in your subclass, it won't be called,
        instead the C will be called. could be Confusing
    Them: OMG you're so smart
    Lesson: Don't Subclass built in types
    Then what do I do: collections module using:
    UserDict, UserList, and UserString,
    which are designed to be easily extended.

  if you subclasses of built-in types on the streets, out in the wild,
  in open source, stop and clean that up

  * How do Mixins Work???
    * Are the just classes? Yep
    * Mixin Classes are made to stand on their own
    * In Python a Mixin is a Mixin, if it ends with Mixin
    * while a mixin should never be subclassed alone except by another




Ponderings
==========

  * Alan Kay says - creating an instance of something, is inheritance.

  * if you are breaking Method Resolution Order, is that a code smell?
    you have a complex inheritance, and you are saying, naw, not
    what I want?


  What were the original ideas of the OO pioneers
  Things Change

  [We] started to push on the inheritance idea as a way to let novices build on frameworks that could only be designed by experts.
    - Alan Kay


Method Resolution Order
Ancestor Chain

I have a method
  * Who can fufill this message



Two Types of Inheritance
---
  Inheritance of interface creates a subtype, implying an “is-a” relationship.
  Inheritance of implementation avoids code duplication by reuse.


inheritance of interface      - Is A
  * are you building a framework of some sort? cuz if so cool, and keep it up
interface   of implementation - Shared Code
  * it can often be replaced by composition and delegation


One restriction applies to ABCs and not to mixins:



Why is this cool or mean anything?

"""
	the concrete methods implemented in an ABC should only collaborate
	with methods of the same ABC
	and its superclasses.
	This implies that concrete methods in an ABC are always for convenience,
	because everything they do,
	a user of the class can also do by calling other methods of the ABC.
"""



TODO Later
==========
  * https://www.python.org/download/releases/2.3/mro/
	* Look up arguments against Class based views
		Find the holdouts
		Go Deep on the Orange Site and look for the haters
		Rails Haters

	* What would Django Look without Multiple Inheritance?
		Blog or Tech Talk
