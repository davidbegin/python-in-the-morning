2020 - 2 - 3
============


Begin Advice for Programming Beginners:
====
  * you want to hang with out with programmers, even when its all gibberish
  * github
  * twitch
  * Meetups
  * Reddit
  * Slacks and Discords
  * Twitter and Podcats and Podcasts
  * Youtube
  * random people with editors open at coffee shop

You want to start learning, the lingo, the common phrases, the jokes,
the memes, the constant warnings.




















End of the year Goals
===
  * Average under 30 seconds on the Cube
	- Sub Goals
		- Average 12 moves for the cross
		- Memorize all of OLL and PLL


Viewer End of the year Goals
===
	* ZeeB - half of your game developed



BeginBux™ Suggestions
===

Challenge
=========

Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

We need some sample datasets

Goals
=====
  * Learn about Asyncio
  * Have fun

Viewer Questions
================


`ZeeB__:` whenever i run my code im just getting an exit code in the run console

Often when you get no error show and just an exit, you have a file named something
that is trying to loaded, not by your code.

Example:

```
hash.py
```


Questions
=========
  * Can someone explain what Tropical Geomoetry is and for (how to make money with it),
    for dummies.

  * What does this mean?
      - 635m/552m/2044 memory (VIRT/RES/SHR)


	* Can you always call await on a syncronous (def no await) function????
    I think no!!!!

- What does return_exceptions True vs False do in the context of asyncio.gather?
  - True | stop on the first task
  - False (default) | Keep running all the tasks


Good Band Names
===
- def no await

TODO
====
  * Read this whole thing for fun: https://mail.python.org/pipermail/python-list/2009-February/525289.html
  * Create the classic Streambot


Learnings
=========
  * what does xrange do?
    xrange is range in python 3, it returns a range object,
     that hasn't been "generated yet"
    range in python2 returns a list.

	* There is the possibility that “dummy thread objects” are created. These are thread objects corresponding to “alien threads”, which are threads of control started outside the threading module, such as directly from C code. Dummy thread objects have limited functionality; they are always considered alive and daemonic, and cannot be join()ed. They are never deleted, since it is impossible to detect the termination of alien threads.



On the conceptual level, shield is like a bullet-proof vest that absorbs the bullet, but remains unusable afterwards. shield absorbs the cancellation, and reports itself as canceled, raising a CancelledError when asked for result, but allows the protected task to continue running. (Artemiy's answer explains the implementation.)



Pattern for Asyncio:
- 3 Parts:
	- Calling the supervisor
	- Supervisor
	- Tasks

```python
import asyncio

async def a_cool_task():
    while True:
      try:
        print("Super Cool things")
        await asyncio.sleep(1)
      except asyncio.CancelledError:
        break

async def slow_task():
    await asyncio.sleep(3)
    return 108


async def supervisor():
    task = asyncio.create_task(a_cool_task())
    result = await slow_task()
    task.cancelled()
    return result


result = asyncio.run(supervisor())
print(result)
```

### What consistutes a "supervisor" function?
- its an "async def"
- it creates tasks with create_task()
- it manages the tasks, canceling and what not
- might return a result
- *Maybe:* You can only `await` and `asyncio.create_task`
           or interact with those threads
					 when refering other functions

### What does a proper "Async Task" look like?
- its an "async def"
- it has error handling for asyncio.CancelledError
		- calls break when the error is found
- *Bonus:* if it wants to do sleep, it needs asyncio.sleep() with await




An event loop runs in a thread (typically the main thread) and executes all callbacks and Tasks in its thread. While a Task is running in the event loop, no other Tasks can run in the same thread. When a Task executes an await expression, the running Task gets suspended, and the event loop executes the next Task.


Event Loop runs in a Thread
	- executes all callbacks and Tasks in the Thread
	- When one Task is running, no other tasks can run
	- until that task calls an await expression, then
	- that thread gets suspended, and the loop executes the next Task
Task is running in a event Loop









Ponderings
==========

Learning the stories and catch phrases in a programming community can really help
feel more comfortable.
  - there are two hard things in computer science (with the optional off-by-1 joke agument)

Opinions
========

- Do people like asyncio?
- Do people NOT like asyncio just becasue
  they don't understand it?

Debates
=======
   How do you pronouce idempotent?
    - item-potent
    - eye-demp-po-tent

Confessions
===========
  * I've never built a computer

I make a playlist on youtube of computer videos, common pitfalls,
noob mistakes, best build, worst build.


Python Interview
================

Scraps
======

Quotes
======
  Concurrency is about dealing with lots of things at once.
  Parallelism is about doing lots of things at once.
  Not the same, but related.
  One is about structure, one is about execution.
  Concurrency provides a way to structure a solution
  to solve a problem that may (but not necessarily) be parallelizable.
    - Rob Pike, Co-inventor of the Go language

What are the two hardest things in programming:
 There are two major sins in science:
    - using different words to mean the same thing
    - using one word to mean different things.
      - Professor Imre Simon



“For every complex problem there is an answer that is clear, simple, and wrong.”
  - HL Mencken


 “All models are wrong. Some are useful.”
  - George Box



What are the 3 qualities of a good programmer according to Larry Wall?
  - Laziness
  - Impatience
  - Hubris

We have a problem:
  - Ugh I don't want to have to do this everytime
  - Ugh, I just want it to work now
  - I can solve anything








Hackting
========
  * when someone mentions asyncio, you have to pretend not to know
    what it is, and then act excited when you realize it looks like tulip.
    tulip was the code name for asyncio

    Acting Preperation - What PEP introduced it, the time frame etc.
    It landed in Python 3.4, but you can use it use it 3.3










Hardware
========
  * https://sleekeyboards.com/#groupbuys
