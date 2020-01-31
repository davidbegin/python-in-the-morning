2020 - 1 - 31
=============

Goals
=====
  * Learn some things
  * Have fun
  * Learn more about Futures today


Vim
===
  folding in Vim


o - open
c - close
A - toggle
R - open all folds
M - close all folds


Viewer Questions
================

  * Sweeku: is there an easy way to tell the upper limit to amount of threads you can have?


What is total number of requests, so its like 1000:
  - 1000

What you should measure specifically is the maximum amount of threads in concurrent use (e.g., waiting on a return from the DB call) under load. Then add a safety factor of 10% for example (emphasised, since other posters seem to take my examples as fixed recommendations).


Rube Goldberg Machine
  -> Pee Wee Herman makes eggs





Questions
=========
  * What does thread really mean
  * When talking about Python threads, how do they relate to system threads ?
  * When do you use ThreadPoolExecutor and When do you use ProcessPoolExecutor
      - I/O Bounce
        - ThreadPoolExector
          - We have to adjust the number of workers for the available memory
            requires experiemntation
      - CPU Bound
        - ProcessPoolExecutor
          - this just uses as many cores as possible?
				- For CPU-bound work, you need to sidestep the GIL by launching multiple processes. The futures.ProcessPoolExecutor is the easiest way to do it. 




Learnings
=========
  - sys.maxsize = value reports the platform's pointer size,
                  and that limits the size of Python's data structures
                  such as strings and lists.




```
(Pdb) sys.maxsize // 100
92233720368547758
(Pdb) type(sys.maxsize // 100)
<class 'int'>
```

Ponderings
==========

Whats the point of refactoring?

You write some code
its kinda messy for a feature
then you get a new feature
but you want to clean up the code first

so you have to talk to your PM and try and schedule a refactor task,
they keep telling you to skip.

This is how we build tech debt.

"Make the change easy (to do through refactoring), then make the easy change."
  - Anon

Ugh this code is sooo mixed up, I just need to do this, but it's
tangled up in this way.





Opinions
========

* Why use Vim and not VSoce or Sublime Text, IDE?
  - Every single server has Vi
  - I like staying in Terminal all day
      - I wanna do bash stuff
      - I wanna Vim
      - I wanna ssh
      - psql


If you are more a beginner and you learn you forced to learn bash more.
and thats save a lot of mysterious pain you have for while.

why can't VScode find this thing, its right here??

Some people are veryyyyy afraid of the terminal for some reason.
Black and Green scares people


You have to interact with Vim as programmer sometimes, you are forced to.
the famous how to exit vim!!!!



I don't like ArgumentParser's API, Aka its method names
its akward and hard to remember, and silly.

Begin suggest using black



Begin Safety Measures:
---

```
-15 before you -9
--force-with-lease before you --force
```



Debates
=======
  * In python, what is the preffered CLI argument parser path these days
    - ArgumentParser
    - OptionParser
    - Click

Confessions
===========

Python Interview
================

Scraps
======


Quotes
======
  "If I had 6 hours to chop down a tree, I would spend 4 hours sharpening my axe"
    - Abe


