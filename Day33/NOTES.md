2020 - 1 - 16
=============





Check Cyclomatic Complexity
ABC Complexity






MorgueBot Goals:
==========

Separate Types of Code:
  * calculating state on the game
    Weapons
    Spells
    Armour
  * infrastructure connecting code
    - Kinesis
    - SNS
    - SQS
  * IRC twitch chat code



dungeon crawl
application code
glue code
infrastructure code














Ruby Book Suggestions
Practical Object Oriented Design in Ruby
	- Sandy Metz

Ruby under the microscope -> Soooo funnnn

Addison Wesley -> Design Patterns, Gang of Four, minus the patterns
 that don't need to exist in Ruby

Confident Ruby
	- Avid Grimm


Metaprogramming the Ruby -> The funniest book in ruby

* a classes class is the eigenclass of the subclasses class








Request:
========
	How can I develop programming logic?
	I need to learn to build pseudocode and flowchart.

see in ruby.
 we have classes we can have same class in different file and when we include those classes we can have all those methods as instance menthods

We have classes in different files
we include



```
from ToolBoxMixin import *
from ToolBoxMixin import hammer
include ToolBoxMixin

hammer()

nail()
```



How can you tell me how to implement Mixins in python?


The same as classes, you just do less.

You define a Mixin, you should never, instansiate on its own

Mixins, shouldn't be modify state much
extra shared methods


Add Mixin to the name,
don't mess with internals and couple the classes your mixing
don't instansiate.



```
class SubClass:
	pass


class FormattingMixin:
  def format_long_stuff():
	  pass


class BaseClass(SubClass, FormattingMixin):
	pass



```
mixin = FormattingMixin()
mixin.format_long_stuff()
```

```






















# ========================================================================================



Naming things
Caching invalidation
Off by one errors


```
def fetch_parts:
	pass

def fetch_inventory:
	pass

def filter_inventory:
	pass

def save_inventory:
	pass
```

Fetch All the Parts
v
Fetch all the Inventory
v
Check what parts are in the inventory
v
Filter out certain parts
v
store parts in CSV file



Aggregation over inheritance
perfer composition over inheritance




Psuedo Python Programming Interview Questions
---
  * Oh you know about design patterns?
    Name all Gang of Four
	* What is the difference between an Iterable and an Iterator???
  * What is the difference between a Class and Mixin in Python
      - How do you implement?


Key Phrases
====
	"Python obtains iterators from iterables."
	"Iterators are always iterables, but not the reverse"
		-> I mean Iterator even is a subclass of Iterable


Answer
======
  "Any object that implements the __next__ no-argument method that returns the next item in a series or raises StopIteration when there are no more items. Python iterators also implement the __iter__ method so they are iterable as well."

Submissions:
===
Im a person who knows how to deploy a mini-version of myself, who
is optmized for running

Iterator is that mini person, who you can trigger to do the action, run

Running is the action
Iterator is like a Lazy loaded thing, capable on its own of doing stuff.

Submission:
	a person is someone capable of moving fast or running, running is the process of moving fast





Quiz
====
  * Pros and Cons of language having operator overloading
  * What is Lazy Evaluation?
    - expression that is gonna give you some data, or transform some data,
      but you don't evaluate it right away. You can pass it around, as just
      a lazy evaluated whatever, and then once it needs to be consumed,
      then actually fetch or transform the item.
	* Regex Exprression Quiz:
			+ = 1 or more
			? = 0 or 1
			* = 0 or more
	* Iterator: The actual thing you iterator over???
	* Iterable: The thing that knows how to return iterators

Questions
=========

	* No subclassing or registration is required, because abc.Iterable implements the __subclasshook__,

	* is StopIteration a regular Error, or is it akin to NotImplemented
	* What is `__slots__ = ()` for?




How do I check if I can iterate over something?
How do I check if something truly is an Iterator
When would I check something is an Iterable versus Iterator















Learnings
=========
	* If you making a custom sequence, __getitem__, but you won't be considered truly
		iterable, until you implement __iter__, becasue that triggers the __subclasshook__,
    to register your class as abc.Iterable
	* As of Python 3.4, the most accurate way to check whether an object x is iterable is to call iter(x) and handle a TypeError exception if it isn’t.


This is the suggestion???
```
def isiterable():
	try:
		iter(x)
		return true
	except TypeError:
		return false
```


	* How to check if something is an iterator
	`isinstance(x, abc.Iterator)`

	`isinstance(x, Iterator)`


Ponderings
==========

Opinions:
=========
	Use what you like, change you what you like
	try something new



When your a beginnner, follow all rules blindly, and question them everytime,
eventually you get the confidence to break them, and you have explanations.

Examples:
  * 100% test coverage
  * Sandy Metz Rules
    - classes can't be more than 100
    - method defintions can't be longer than 5 lines
    - Rails -> controller method methods can only take one instance variable


Web request comes -> Routing -> Controller


Goals:
======


Quotes
======
  "Probably about 20 to 30 percent of the population think of operator overloading as the spawn of the devil"
    - James Gosling

  "Then there’s a community of about 10 percent, Math Nerds"
    - James Gosling


  "If your language doesn't support operator overloading (for at least the already existing operators), you hate the Math Community"
  - David Begin

"When I see patterns in my programs,
 I consider it a sign of trouble.
 The shape of a program should reflect only the problem it needs to solve.
 Any other regularity in the code is a sign,
 to me at least,
 that I’m using abstractions that aren’t powerful enough—often
 that I’m generating by hand the expansions of some macro that I need to write."

		--Paul Graham, Lisp hacker and venture capitalist


DRY
Do Not Repeat (Yourself)
This is just a quote advocating for DRY code, however, we don't have the
same language about code.


"Every generator is an iterator: generators fully implement the iterator interface. But an iterator—as defined in the GoF book—retrieves items from a collection, while a generator can produce items “out of thin air.”"



"iterators are also iterable, but iterables are not iterators."
muppets are puppets, but not all puppets are muppets







implement __next__ on a iteratable -> Code Smell






