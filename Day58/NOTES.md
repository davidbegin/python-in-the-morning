2020 - 2 - 19
=============


Goals
=====
- learn some python
- get better at typing on the ergodox
- have fun!

Next Goals:
-----------
- Pink Fluffy Job Application Review

Bounty
======
- find me someone who use fira code, with others
- find the source for type's class being type
  - https://github.com/python/cpython/blob/master/Objects/clinic/typeobject.c.h
  - Bounty Has increased: breakdown of the magic
  - https://github.com/python/cpython/blob/4dee92b0ad9f4e3ea2fbbbb5253340801bb92dc7/Objects/typeobject.c#L5314-L5319
- Make something that doesn;t have object in its MRO Method Resolution Order
  - remove object from the mro

Abstrct Base Method Meta

TODO
======
- check asciiquarium
- look into st and why certain chars arent showing
- Learn about vim pasting
- Learn Norwiegen geography
- Begin brush on C


Viewer Questions
================
- __mro__ always ends up at object?
  - Begin's Guess: yess

What languages outside of work?
- What am I building?
- What do I want to learn:
  - More practice with a lang
  - Try a new lang
  - Experience withn a library


Especially if you are new:
- line up what to learn with job hunting
  - Look up python companies in the area, look at their tech stack. Make something with that:
    - Database
    - Cloud Provider
    - Testing Framework



2 People:
- Study everything deep, going through rabbit holes, but not learning practicular
  - Similiar to School
  - Learn deeper concepts that will come in handy
  - You don't know how to not rabbit
- Focus entirely on being productive
  - Similiar to Bootcamp
  - you end slowing down, because you don;t understand
  - understnd how to work


     What does a dev need to know before they can start applying for jobs?
 - NO, start now, You can get rejected a lot at the same company
 - If you apply and are too junior, and you apply 6 months, with huge visible growth,
   thats a huge hiring sign for me
- interviews take practuice, do lots

 Should I just start emailing companies applying for jobs with a small variety of projects I've done that utilise a wide range of skills and knowledge that I have obtained?
 - Yes
 - Meetups in the area, start going, learning, making friends, "networking".
 - Resumes:
   - Github
   - Website / Blog
   - Personal Projects

 I have done stuff like homemade neural network libraries the only stuff I havent really learnt how to use shaders and to use the GPU.

Find a project did, write a blogpost about, clean up the project for presentation,
Write a resume start sending to companies.

You gonna get rejected a bunch, so you need multi-pronged approach:
- Peers:
  - Github on projects
  - meetups
  - discords and slacks
- Mentors:
  - You get rejected for a job, but they say let me help you out

Identify tech companies around you

Don't just apply for jobs, join the community you want to be a part of:
- Where did they hangout
- How can you provide value:
  - Better Docs
  - Blogsposts for beginniners

Recruiters is an option

Getting a Job when you don;t live in a tech Hub:
- No Meetups:
  - Go hard on the interwebs
  - Start the meetup




  Python VS JS for Webgames
  ==========================================
  - Which community is more exciting a fun
  - Which language can you find a mentor
  - are there meetups in town
  - what are some confernce talks that

Noxza Meetups:
- go to 4 each of JS and Python
- make friends (THIS IS AKWARD, IT GETS BETTER)
- Figure which one you like better, theres your langauge


```
import abc


def auto_meta(cls):
    class new_cls(metaclass=cls):
        pass
    return new_cls


@auto_meta
class TestingMeta(type):
    def __new__(cls, *args, **kwargs):
        cls = type.__new__(cls, *args, **kwargs)
        print(f"created class {cls.__name__}")
        return cls


class SomeClass(TestingMeta):
    pass
```

```

```



### Personal Bias on getting a job:
- No School
- No Bootcamps
- No Certifications
- No Recruiters









Questions
=========
- How are module files read when only importing a singlemethod or class?
- A: the whole file is read despite a `from`


- How are metaclasses handled when subclasses:
  - Make a metaclass that changes the __init__
  - Make a class inheriting from that subclass
  - Make a class inheriting from the previous subclass
  - Q: What __init__ will be run
  - A: Metaclass isn't run until the object is instansiated


Learnings
=========

Consider the Python object model: classes are objects, therefore each class must be an instance of some other class. By default, Python classes are instances of type. In other words, type is the metaclass for most built-in and user-defined classes:

- classes == objects
- classes typical class is `type`
- type is metaclass
- To avoid infinite regress, type is an instance of itself, as the last line shows.
- classes are subclasses of object
- all classes are instances of type,
- metaclasses are also subclasses of type, so they act as class factories.

When you ask for the class of tyoe you get the same type

The classes object and type have a unique relationship: object is an instance of type, and type is a subclass of object. This relationship is “magic”: it cannot be expressed in Python because either class would have to exist before the other could be defined. The fact that type is an instance of itself is also magical.

### Blow your friends minds
object is an instance of type
type is a subclass of object



Q: Whats up with abc.ABCMeta?
A: ABCMeta is a Metaclass, for instrance it can create a Iterable instace (which is a class and
an object), ABCMeta's class is type (which is also a metaclass) type is a metaclass that can
produce metaclasses

When inherting from metaclasses, the metaclass init is not run, until an instance of
the sublass is made
other subclasses of that subclass will use the metaclas __init__



Q: Are decorators on methods called when importing a module?
A: yes!


Q: What are virtual subclasses good For?
A: Goose


New class ABC has ABCMeta as its meta class. Using ABC as a base class has essentially the same effect as specifying metaclass=abc.ABCMeta, but is simpler to type and easier to read.


If you want to use a custom metaclass, you got 2 options:
- metaclass = YourMetaClass
- create a class that sets the Metaclass, and then inherit from that class
- No matter what you need to metaclass somewhere??


How name mangling work again?





Ponderings
==========

Money will come
We need to like everyday
Work Smart Hard Not Hard





Opinions
========

When something is waaaay over your head just read as far to get to one hard concept,
and try learn that, then your allowed to give up

Debates
=======

Will the implementation of type and classes change in python (10 years)
When have fundamental changes in a programs object happened
- Ruby the addition of BasicObject

Confessions
===========

Python Interview
================

Quotes
======

"Theres a lot of money in puns in programming"
 - Begin

Scraps
======

