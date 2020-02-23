2020 - 1 - 9
============


My new ABC class:
	- "enforcing interface conformance since 2020"


How Do you Practice:
====================
	* Side Project
		- Needs a Deadline -> 1 Week share some progress, 3 months you done
		- Needs to be useful -> (Making money)
		- Need to show humans -> Can't hide it from the world

	OpenCV
		- recognize stuff
		- What do you want recognize?


Shoes
=====
	* Lemme build something to recognize shoes
	* Hook that up to Instagram
	* Try and charge some money share with friends


Goals
=====
	* Can I recognize a shoe
	* Can I reconigize 2 different shoes
	* Can I pull in a feed of shoes


Hit a Wall in your project
==========================
	* Stack Overflow
	* Github
	* Meetups meet people
	* Discord / Slack full of people to help


Whats a problem space that are into,
meet some people
Then they will teach you everything..


Get a Job in Programming:
	* Choose a Project you are into, that you can do
	* Work on it
	* Reach out for Help
	* Blog Post
	* Github Repo
	* Talk a Meetup






TODO:
=====
  * Take Supernerd on the ground, put my face over it


Quotes
======


Questions
=========
  * spheres are “hyperspheres” in 4D and beyond.
  * How do I print the cool character from the Unicode Code point?
	* What the heck is atan2, where is atan1? why not just tan?
	* How can I use Hypersherical coordinates to make me money??


Learnings
=========
  * avoid reusing format codes supported by built-in types.
  * U+03C6 = Phi = Φ = Angle in Mathland™
	* Iteration in Python represents an extreme form of duck typing:
 		the interpreter tries two different methods to iterate over objects.

	* What goose typing means is: isinstance(obj, cls) is now just fine… as long as cls is an abstract base class—in other words, cls’s metaclass is abc.ABCMeta.

	You can use isinstance
	but it has to be a ABC
	which means all subclasses that implement the ABC,
  they will work



	SELF DOESN'T DO ANYTHING

What your mentor doesn't want you to know about python
self is a lie!

I want some open source examples of this, non-selfs

Personal Opinions
===============
higher-order function is also known as:
	reduce
  √ fold
  accumulate,
  aggregate,
  compress,
  inject

* List comphrenhenison and lambda in one line is gonna make the people mad



Rabbit Holes
============
	* Later I had a Pythonic insight


Ponderings
==========
	* Established protocols naturally evolve in any language that uses dynamic typing, that is, when type-checking done at runtime because there is no static type information in method signatures and variables. Ruby is another important OO language that has dynamic typing and uses protocols.
		- My Take: its easier to change, so it evolves??

	* What are your feelings on implementing part of protocal?
		- Questions to Determine, partial or all?
			- Does all the functions make sense for the domain
		- Part
			- Cons
				- Someone could think oh, this is a x-like thang, lemme use it like
          that
			- Pros
				- Less Code
		- All
			- Cons
				- writing code you have no current use for is dumb
			- Pros
				- Impress your friends
				- talk down to people
				- safe to keep using as that Duck


	Never give a custom sequence a shuffle method,
  instead random.shuffle(sequence) -> Maybe more pythonnic



to show that every Python method starts life as a plain function, and naming the first argument self is merely a convention.



And, don’t define custom ABCs (or metaclasses) in production code… if you feel the urge to do so, I’d bet it’s likely to be a case of “all problems look like a nail”-syndrome for somebody who just got a shiny new hammer—you (and future maintainers of your code) will be much happier sticking with straightforward and simple code, eschewing such depths. Valē!

Is this Ok???

Things to Look at Later
=======================
	* cladistics


Why is when its not in a list, its faster!!!!
```
my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
def sum6():
    return sum([sub[1] for sub in my_list])

my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
def sum7():
    return sum(sub[1] for sub in my_list)
```





formulas
used to calculate the spherical coordinates
	from the Cartesian coordinates
		in the Vector components array.



Memorization
============


When implementing a class that emulates any built-in type,
it is important that the emulation only be implemented
to the degree that it makes sense for the object being modeled.
	- Python



There is no method __iter__ yet Foo instances are iterable
 because—as a fallback—when Python sees a __getitem__ method,
 it tries to iterate over the object by calling that method with integer indexes starting with 0.
 Because Python is smart enough to iterate over Foo instances,
 it can also make the in operator work even if Foo has no __contains__ method: it does a full scan to check if an item is present.
