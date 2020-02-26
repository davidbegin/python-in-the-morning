2020 - 1 - 17
=============

Begin's Suggestion
---
  * Get good at vim
    - shortcut the path to your vimrc
      - AKA Make it easy to be in there all the time
      - shortcut to open the file,
      - multiple shortcuts to source the file
    - Don't use your mouse
    - Disable arrows keys
    - Remap to caps to ctrl
        - ctrl-[ => escape
    - spend 70% of your time in normal mode
    - you have to start customizing, experimenting




Hobby
=====
  * Whenever you hear about a language direction argument, ask yourself, what would you do?
    Python is adding powerful generator expressions, do we add a new `gen` keyword,
    `yield` magic.

Team `gen`:
  Pros:
    - More explicit
  Cons:
    - New Syntax is annoying to learn

Team `yield`:
  Pros:
    - Its a syntax construct, that you use, without having to think about generators?
  Cons:
    - More implicit

Python Interview:
===
  * What are python generator functions?
    A: Any Python function that has the yield keyword in its body is a generator function:
    a function which, when called, returns a generator object.
    In other words, a generator function is a generator factory.



BuzzFeed Poll How Pythonista are you?
===

# These all do the same thing:
```
def fake_func():
  # does something
  return None

def fake_func():
  # does something
  return

def fake_func():
  # does something
```

Which do you use when?
or do you just use one the whole time?







Getting into the mind of a BDFL
===

If we do this, it exposes questions about this, which requires explaining things people,
 it will be waste of time, scare of noobies, make people think about a lower level
 abstraction that they shouldn't, that would lead them to writing bad code.



Questions
=========
  * What do the spaces mean for the dis library?
  * is  yield in ruby and python is pretty similiar?

  * Is there ever a reason to return something from an __iter__ generator expression?
      - Examples plz!!!

  * What does any of this mean???
      - Jython requires that the compiler be able to determine potential suspension points at compile-time, and a new keyword makes that easy. 
  * CPAN

  * what file doe pypi look for to display your docs?
  *  here is a term to add to your queue of things to look into when you are bored at work: "data sheets"
  * How do you pronouce sinusoidal?

  * What are the "numeric coercion rules of Python arithmetic"?
  * What is this in Python 3.4 versus 3.8?
       `print([ x for x in dir(itertools) if not x.startswith("_")])`
        1 thing is missing!








Generators:
---

When do we use them?

How do you tell some good is ripe for a generator refactor
  - Generator Refactor Code Smells


When is it bad to use a Generator?


What does return do???
```
def __iter__(self):
    for word in self.words:
        yield word
    return
```



Goals
=====
* A way to measure memory size difference between
    -  using yield and using a for loop


Definitions
===========
  Code Smell = Indicting Factor, that things are going wrong, or down a bad path
    - Doesn't quite feel right
    - Not necessarily, super concrete


Smoke Tests
====
  * What are they in the context of software???

  Begin Guess: simple high level tests, making sure the most basic thing works,
               will the service even start up?
  Haze Guess: wide coverage across multiple platforms




Learnings
=========
  * How does python know to return a generator expression?
    A: if the function has yield in the body, you're getting a generator
  * functions return values, generators yield or produce
  * My rule of thumb in choosing the syntax to use is simple:
    if the generator expression spans more than a couple of lines,
    I prefer to code a generator function for the sake of readability.


Ponderings
==========
  * is a explict of return None, the preffered python way
  * Become Documentation master

  * Can you always substitue the lazy version of something,
    if it exists?
    - I want to yes
    - Potentially declaring lazy and then consuming right away,
      is just a waste
    - Begin Plan: I'm going go lazy as possible
                  I Will know every lazy version, interface

Opinions
========
  * Read some PEPs
      - its nice

Haze:
  * MS is still trying to destroy Open Source

Microsoft trying to make it appear as if they are embracing open-source.

Microsoft -> Bill Gates and Balmer running stuff
              Things are more and more commitee

companies don't have monothilic ideas



Vim Setup
====
```
# ,t => run the current file
# ,f => run the pytest marked focus
# ,p => run the current file tests in pytest

# %:p => current file
# %:h => current directory
```

# ,t => run the current file


Quiz
====

Quotes
======
  "def it stays. No argument on either side is totally convincing,
   so I have consulted my language designer's intuition. "
              - BDFL



```
print([ x for x in dir(itertools) if not x.startswith("_")])
print(len([ x for x in dir(itertools) if not x.startswith("_")]))
```



