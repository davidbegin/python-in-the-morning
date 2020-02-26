2020 - 2  - 6
=============

Python Quiz
===
- What is the use of an Asynchronous Generator??
  - They don't concurrently process the "agents of iteration"
  - They let those agents of iteration, within themselves,
    not-block event loop


They’re merely designed to let the enclosing coroutine
 allow other tasks to take their turn.

The `async for` and `async with` statements are only needed to the extent
 that using plain `for` or `with` would “break” the nature of await in the coroutine.
This distinction between asynchronicity and concurrency is a key one to grasp.


when do you use `async for` or `async with`....when using for or with,
but within async code that needs to allow other tasks to take their turn.


Goals
=====
- Learn more about Asyncio programming in Python
- Have Fun

Viewer Questions
================

Morning! I Need advice:

I’m trying to help complete beginners learn python.
There are so many resources out there,
how do I choose the best resources?
Or should I not curate and just provide them with all the resources and let them decide?

One Begin suggestion for total beginner:
	- Learn Python the Hard Way - Zed Shaw

Theres a focus on typing repetivive things, and it emphasis, the practice
portion that is really important in code in the beginning.

Learn Python the Hard Way, helps you learn to learn, or teach yourself.
It feels similar musical practice.






Go Opinions incoming
====
	- Go is made for large teams
		- are you on a large team?
	- Go not that "cool" syntax
		- C-like, nothing to fancy
      - Elixir, pattern matching! its looks like ruby!!!
      - Rust, woah, whole new model for thinking about memory
      - Go, yeah pretty musch the usual, but trust us it works
  - Go is cool that concurrency is part of lang
  - Go is cool in that you ship a binary, that easy to use everywhere
  - Go is NOT COOL, it that it disrespected golang Soooooo much






- What is asyncio?
  - in the context of python, its a module, full of tools for doing asyncronous programming
- What is async programming?
  - As opposed to syncronouos programming - where you do one wait for the response and then do
    the next thing.
  - asyncronous programming, you can do many things at once (and this is where `asyncio` module
    helps)


- Question: when is that project going to be done?

Classic synchronous : Conversation
    I am going to sit here waiting, doing nothing until you respond
Classic Async: Email



Question: How do I know if something should be async or not?
- More Questions:
  - Do you need to do something with the response right away?
  - Can I do other work before this request finishes?
  - Is our code blocked by I/O or CPU???


Question: Why Async when its soo much more complicated?
  - Speed, Efficency
  - Fault Tolerance





Meta-Stream
===========
- vim-cave
- rabbit-hole
  - wikipedia article
  - 2 weeks later
- perf-tests
- office-chair - bill jumping the chair emote
  - bill mean mugging a chair
  - Balmer - Developers,

PandaPersonTTV: put ur weird faces in green screen
PandaPersonTTV: as emote




Chair and Desk Suggestion
===

- https://www.amazon.com/Ergohuman-Swivel-Chair-Headrest-Chrome/dp/B002LK1YNO/?tag=wellgrt-20
- Is my chair holding me back from streaming

`https://www.amazon.com/dp/B07V3TB9NN/ref=twister_B07VXX6DLF?_encoding=UTF8&psc=1`






Questions
=========
- what was before an integrated circuit?
  - before, it was all legos
    Kilby made the first kit
    before that megabricks, tubes

Learnings
=========
- itertools.repeat is a thing, but when should we use it.

- when you get a syntax error in python, and the line has no syntax errors, look up

- BeginBux™ - 50 point per 5 mins

Ponderings
==========


Do you need to know about Python asyncio?
  - Depends, but one major factor, is your work's infrastructure
    around asyncrounous processing
  - Do you have Queues already?
  - do you have Streams
  - Enterprise Service Bus??




### 2 Async Styles

#### Style 1
 each task (future) is composed of a set of coroutines
 the coroutines - explicitly await each other and pass through a single input per chain.

#### Style 2

- Producers
	- add items to queue, whenever and whereever we want
- Consumers

	- Pull items as they show, greedily without waiting of signal

### Customer Support is an Example of Style 2

- Producers: Customers "producing" compliants
					   Lots of people can complain at random times, and
             it just gets added to a Queue.
- Consumers: Customer Support employees, who all can just pull
             from the queue.




When we split into producers and consumers,
we need to await on the producer tasks and the queue to be empty

- Create producer Tasks, that puts things onto a Queue
- Create consumer Tasks to read off the queue.
- inside the `main` asyncio.run() on:
  - await on the producer tasks
  - await on the queue.join(), which means the queue is empty?
    - once the producer tasks have finished and the queue is empty
      - cancel the consumers






Opinions
========

### Begin's Streaming Philosophy

Stream, what you already do and hopefully people like it.


TODO
====
- Get a hot plate
- Make ArtMatt an Admin Emotes
- setup camera and adjust gear info in twitch bio


Coffee Recomendations
===
- Chemex
- Scale
- Brrr Grinder
- Filters
- Some Good Coffee

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


Confused
========
there is a particularly unconventional mechanism by which these coroutines actually get run.

Their result is an attribute of the exception object that gets thrown when their .send() method is called.


send() raises an error, this is needed for the coroutine implementation


Coroutines are repurposed generators that take advantage of the peculiarities of generator methods.

Old generator-based coroutines use yield from to wait for a coroutine result.
 Modern Python syntax in native coroutines simply replaces yield from with await as the means of waiting on a coroutine result.
 The await is analogous to yield from, and it often helps to think of it as such.

The use of await is a signal that marks a break point. It lets a coroutine temporarily suspend execution and permits the program to come back to it later.

