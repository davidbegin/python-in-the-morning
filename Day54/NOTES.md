2020 - 2 - 13
=============

Goals
=====
- Learn about Python
- Have Fun
- Learn how to pronouce Otatome


Advice
======
- Begin Advice for Beginners: try to match the style of the community as closely
  as possible in the begnning. Don't rebel until you've mastered, and you have
  more concrete arguements why you don't like something
- get a linter, use a linter, try to understand what the linter is doing to your
  code, so you can start writing idiomatics





`pip install black`


How this Stream can Work
------------------------
- LEarn some things (typcially abotu pyhton)
- go down any rabbit whole that seems interesting
- I like to consider and debate different approaches and philoshpies of programing
- Help people, code review, help with project design management.

If you want help:
- Open an issue in the python-the-morning
- Join the discord, and ask in the #all-things-code



Viewer Code
-----------

these are the only fils I have in my pycharm right? but when I commit and push to my github, a "Data" folder is there and I cannot delete it for some reason


Do you know about .gitignore?









[Viewer](Viewer) Questions
================
rbaya: is this reflection? or is that something completely different?
	- to metaprogram, you need relfection
	- being able to introspect your running state to make decisions

Bounty
======
- Public debates that has happened where one person is supplying both arguments, without the public knowing

- How can I see when my dictionary resizes and we restart dict_item creation?
https://github.com/python/cpython/blob/c0052f3fe3d19820b2d4f76e383035439affe32c/Objects/dictobject.c#L2236-L2294



Viewer Projects
===============
- Flask and Mongo DB
  - Where and how are you going to deploy this sucker?
  - Heroku
    - Deploy early and often
  - Next Step after Heroku: What is one part you could do on your own to make it cheaper











Resources
=========

- https://12factor.net/



Questions
=========

Learnings
=========

Ponderings
==========

Opinions
========

Debates
=======
- why is JS more popular than python. Cuz worse is better. True or not?






When you misread some code, that is a sign, theres information in there.

2 trains of thought:
- I'm dumb
  - Never think you're dumb, you just don't know things
- This code is not explict and clear
  - What confused about this code
  - Do I not understand the syntax
  - Do I not understand the intention


Junior / Don't know the Language Code Review
============================================
- Question: How can I junior Code Review a Seniors Code???
- Answer  : How does this code read from a more junior perspective
  Hackting: It's 2 years from now, that Senior is gone, theres a whole
            new crop of Juniors, and they have to look at this code.
            What is there life like? What do they wish was commented on?
            What do they not understand?

### Type of Comments I am leaving as a Junior:
- I don't understand why you chose this versus that?
- You don't understand the syntax?
- Explain what confused you and why you thought that?











Should You Switch Keyboard Layouts
----------------------------------
- Better for hands/wrists all those things
- We are gonna type for the rest of our lives, so a lil annoying 2 weeks, aint bad.
- it aint bad to rewire the brain every once in a while






I learned to program and vim at the same time.
I was typing soooo close.....and I also didn't know what to type.

I'm gonna change my whole keyboard life, now that im on Arch.
Because I don't know how to type the commands to make Arch do what I want to.

Match up typing slow, with learning something hard.

Learn about machine learning


We know Qwerty was built for typewriters
it built to prevent keys from sticking
move letters that are commonly close far away.

People figure out btter things.

who the heck is Colemak and Dvorark????









Python Debates
--------------
- explict self for instance attributes, do we like it
  - Begin Opinion: Yes, or some other way. `@instance_var` or `self.instance_var`
- do we like self as an explicit first argument or do like alternative methods for declaring
  a method in a class. (Need to do a language comparison),

Confessions
===========

Python Interview
================

Quotes
======

Scraps
======

Problems
========
- self
- camera is lagging behind
  - maybe look at bitrate - 6000
  - maybe look up upload time
  - maybe look at system resources
  - we just restarted and it fixed it. Wonder how we can identify,
    - how can we know through measuring something, that the video is behind?
    - monitor GPU or GPU, or Dropped frames, or number of processes

Hackting
========
- It's Spring of 1989, you're on the porch of your tiny AI LISP startup, hackers surrounding you.
  Someone asks, hey why do p- why is JS more popular than python. Cuz worse is better. True or not?eople think C + Unix is better than LISP?
    - Richard P. Gabriel


Nickieben Bourbaki - opposed to "worse is better", pretending to be a single person, who was a childhood friend, but is actually
a collective of writers. Who is a reference to 1930s Math Collectives



Back in the Day - Before 1914
===============
- You couldn't prove I didn't write the star-spangled banner



Mass Confusion
==============

Python is implemented in C as a:
classic stack-based
byte code interpreter
or “virtual machine”
along with a collection of primitive types also implemented in C.
The underlying architecture uses “objects” throughout,
but since C has no direct support for objects,
they are implemented using structures and function pointers.
- Ole BDFL

https://python-history.blogspot.com/2009/02/adding-support-for-user-defined-classes.html



  in C there are no Classes


  the way python represents "classes" or "objs" in C,
  is by through more primitive data structures.



Python’s unique approach to introspection comes from its ability to make the type structure itself available at run-time as an object like all others.

```
typedef struct _str { int result ; // to store the resut Operation opt; // funtion pointer } STR;
```

```
 typedef int (*Operation)(int a , int b );
 ```

  people suggest conventions/functions where the first param is the struct, so it's basically like a 'method' but instead you're passing in the struct. and actually C++ kind of works that way where 'this' is always the first argument to a class' method and its implied (iirc)




  had another struct, and had a pointer to that list of func_names and pointers
  I kinda a class.
  array of these things is like a list of methods
  {"func_name", pointer_to_a_function


