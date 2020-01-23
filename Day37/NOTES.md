2020 1 - 22
===========


History of Hype:
---
	- Peak NoSQL 2012

# ========================================================================================

Noticed a problem with ADA Fruits Scripts on Github,
asking should we do for proper ettiqute

Options:
	- Open an Issue
	- Open a PR

Begin's Advice: Open you a PR if you can

Issue:
	- Issue Template?
	- Bug report template?

Issue Goal:
	- as much info as possible



Stream Problem
==============
  * How do I get a proper Youtube not blasting volume

Goals
=====
  * Maybe learn some python, generator talk
  * Maybe read some PEPs
  * Answer questions
  * Code Viewer Code Review
  * Concrete Example of PEP 380 refactor
  * Want a proper memory measuring decorator, that when you decorator a func,
    it prints out the memory usage when called
  * Want a 4D Matricies python project, that I can work on
    - Weather
    - Graphics

Viewer Questions
================
  * Encrypting Environment Variables


	# *  [25 21 900 900]

	*  [[25, 21, 900, 900], [1, 2, 3, 4]]

		array_name[0][:][0][0]




Viewer Projects
===============

rune_trimmed
```
Goal: The project I was wanting to do was make a file of all the songs in my "liked" playlist on spotify.

Then take each song and send songrequests on twitch streams
```

Sub-Goals:
	* Interact with Spotify API to get list of liked songs
		- Skills: Interacting with APIs, Auth
	* Save the list of songs somewhere (file, or maybe a database)
	* Create a Twitch Chat Bot to send song requests
		- Coding a Chatbot



Database Advice:
================
	* Learn the common patterns for normalizing data in a relational manner
	* Query the DB with SQL and not just through your language
	* Have fun
	* SQL skills are going to lead to a job probably faster
	* NoSQL are needed, but a little rarer, but if you are new and find a company
    who helps help in that part. Mongo, and you only Mongo, you might get hired
    ea


Postgresql:
===

don't know it yet,
make it document until things start to solidfy.
We figure out the right modeling, and now its time to move into Relaitonal.

Its easier to go from document to a relational structure (sometimes), than refactoring
into relational.




Questions
=========
  * Is a string considered an Iterator?
    No!!
    It is a Iterable
    It is not consumable just once and has no next method

	* What's the biggest company that doesn't use a relational database?



Learnings
=========
  Cooperative multitasking == non-preemptive multitasking


  * Generators operate with sequences
  * once the yield word is in a method body, it no longer runs
    any part of it on execution, instead it returns a generator
  * the generic way to consume a generate, would be `next(your_generator)`
  * generator functions (which is any function with the keyword yield in
    it) return generators
  * A generator function is easier way of writing an iterator, you don't
    need to implement the iterator protocal, __next__ and __iter__

	* Why is a range not a generator??
		https://stackoverflow.com/questions/13092267/if-range-is-a-generator-in-python-3-3-why-can-i-not-call-next-on-a-range


	* Generators are useful, when you have to operate on some data in a pipeline
    like fashion, but you don't want temporary variables, or to have
    to load everything into memory, just stream the results from one-pipe-to
    the next.


Grok is a deeper understanding:
---

Grok means "to understand," of course, but Dr. Mahmoud, who might be termed the leading Terran expert on Martians, explains that it also means, "to drink" and "a hundred other English words, words which we think of as antithetical concepts. 'Grok' means all of these. It means 'fear,' it means 'love,' it means 'hate'—proper hate, for by the Martian 'map' you cannot hate anything unless you grok it, understand it so thoroughly that you merge with it and it merges with you—then you can hate it. By hating yourself. But this implies that you love it, too, and cherish it and would not have it otherwise. Then you can hate—and (I think) Martian hate is an emotion so black that the nearest human equivalent could only be called mild distaste.
	 - Stranger in a Strange in Land


Ponderings
==========

  When you have a significantly complicated sytem, and you want to add
  more functionality to it, how do you decide to create a new
  code namespace, or add to the continuing project

Opinions
========
	Haze Opinion: don't like "lazy" for delayed instantiations or lookups
	Alt Option: maybe delayed

delayed instansiation
delayed sequence
delayed iteration


Begin's unfounded opinions:
	- Postgresql is the better choice for your first Database
	- SQL and Relational DB design and queries, super important.
	- Postgresql cooler




Zeebz: Relational DBs are obsolete
			 Dynamocially KV stores are faster,
 			 better more flexible and don't run into the moving schema problem



Deeply complex relationship queries.








Debates
=======
  * The Problem with Syntax Sugar
    - Nows theres 2 ways to do it,
      now your code is not unified


	* Postgresql versus MySql for your first DB
		- Depends on the language and community
		- First Lang is PHP - MySQL
		- Ruby - Postgresql
		- Python - Postgresql
			is python more friendly to MySQL or Postgresql
		- Postgres had some cool stickers, that NoSQL on Acid
				- Postgres, you store arrays and JSON, and Hashes,
				- You do make Mongo and Relational DB.
		- Higher major version == Better projecr


Haze Opinion: languages should be 100% database agnostic
Begin's counter opinion: I agree theortically. But for
a beginner community summort is super important.





	* Git branching strategy

PEP
====
  342 - https://www.python.org/dev/peps/pep-0342/
  Coroutines via Enhanced Generators

  PEP - 380
    - Delegating to SubGenerator
  * https://www.python.org/dev/peps/pep-0380/

Python Interview
================

Scraps
======


Coroutine: This means nothing to Begin

What's the original abstraction for a coroutine.


subroutines
  Do this thing
    - Do this smaller thing
non-preemptive multitasking
  - not-ahead of time, multitasking


generators = data producers
coroutines = data consumers
  -> Iterators -> Which are agents are iteration






using yield is doing non-preemptive multitasking, cooperative-multitaasking, using coroutines

yield

Hey program when you get to this part, let that other part of the program handle it, coroutine



Rants
=====
	* It's scary contributing to Open Source the first times.
		Branching Forking, branching, rebasing, submitting your PR.



After Work
===

Haze's Repo: HTML-Auto-python

2 Options for Contributing:
  * Forking and opening Pull Requests
    - This is the Open Source model, so is nice for extra practice.
    - Open Source is a habit!
  * Permissions on a branch
    - I don't know how to do this in Github!


Questions:
  * How do you see the main github connected thang?
  * How do you ignore virtualenvs?
  * How do you add a .gitignore only for you? .gitignore.local?
  * How do you setup permissions for someone only on a branch in Github



Useful commands for learning more about Git!
```
git help -a
git help -g
```

git remote show origin
