2020 - 2 - 12
=============

Fake Interview Questions
========================
- What is a descriptor?
  - What are the components of a descriptor
	- How do you use a descriptor? (as a class attribute of a Managed Class)

Goals
=====
- Learn some python
- Have some fun
- continue to learn more about new Arch system


Arch Begin Problems
===================
- My 2nd monitor doesn't work
  `xrandr DP-2 --right-of HDMI-1 --auto`
  .xinitrc


Pipenv
======
- No release in a year, but 650 commits
- problem with venv, But we really do need a lock file









TODO
====
- figure out what vim plugin to use and use it! (Tabularize)
- get some real classy auto-completing
- figure out how to use breakpoint, while running your file from inside vim
- look into i3 startup functionality
- setup GNU Stow, clean up my dotfiles and share it the world
-




Buy ArtMatt Melodica in exchange for Make Emotes
Ribbon Synth for some Emotes
Otamatone
Stylophone

Bribe your friends, buy them dumb instrument





Rant incoming
=============
- AWS Reinvent
- DevOps, I use lots of AWS servies, mostly around Lambda
- Every other, we are hot new Serverless startup.
  - you can drag and drop and deploy lambdas!
  - we have 40 environments, 200 Lambdas in each. Whats happens
    when I want to rename one......ask an intern to drag and drop.
  - Programmer, dev-ops, building



Begin's Journey
===============
- Musican, gather gear, starting recording, starting making music
on programs, get broke, start programming to afford gear,
find out that programming is just fun!!!








Viewer Questions
================
- Do you think learning assembly is useful
  - define useful, if you don't have a need for it already
  - you reverse engineers
	- Just because its not useful, doesn't mean not to learn it.
	-

Questions
=========

Learnings
=========
- Theres an asymettry in attribute reading and writing.
  Reading instance attributes in python, first checks the instance, then
  checks the class. However, writing on an instance, only writes on the instance


### Descriptor ABC API:
```
descr.__get__(self, obj, type=None) -> value

descr.__set__(self, obj, value) -> None

descr.__delete__(self, obj) -> None
```


Data and non-data descriptors differ in how overrides are calculated with respect to entries in an instance’s dictionary.

 If an instance’s dictionary has an entry with the same name as a data descriptor, the data descriptor takes precedence. If an instance’s dictionary has an entry with the same name as a non-data descriptor, the dictionary entry takes precedence.

Look up in the instance dictorry, is it a data-descriptor, use that
Is not a data descriptor


For objects, the machinery is in object.__getattribute__() which transforms b.x into type(b).__dict__['x'].__get__(b, type(b)).

object._getattribute() transforms

`b.x`
Becomes this:
`type(b).__dict__['x'].__get__(b, type(b))`





Ponderings
==========

#### 2 Types of Descriptors:
- Decriptor with __get__ and without __set__
  - Non-data Descriptor
  - AKA: Shadowable Descriptor
- Descriptor with __set__ and no __get__
  - OverridingNoGet
- Decriptor with __get__and __set__
  - Data Descriptor
  - AKA: Enforced-Descriptor

- Descriptors full API is the following:
- __get__, __set__ and __delete__
- you don't need to implement all 3 of these



### Components:
Managed Class
Managed Instance

Descriptor Class
Descriptor

Managed Attribute
Attribute Value







Opinions
========

You need to live in some differenct places to know if you like it:
- I lived in DCish
- Lived PNW
- Lived in LA
- Missing NYC
  - too expensive
  - people who are from there, seem too excited about it
  - music bigger in LA
	-


PDX -> lots of wackyness, people
theres a guy in the middle, painted blue looking like a wizard
directing traffic

I like a lil chaos
I like biking through venice
and hearing the people scream

I'd rather see some crazy people screaming, than a bunch of boring people




I move somewhere
They ask me how I like it
I always say I like it
.....however, whereever I live, I'm gonna like
lets say its boring
.....you mean more quiet time to learn
its load, more interesting loud things to explore.











I'm anti-computer science school
Anti-Certifactions
Open Source
Projects with friends
Making something for work and that makes money
People who don't think you need to be a programmer to program
Arch Linux





Hey what certs do I need to get a job?
None

What degree do I need
None

What language do I need to know
None

If you choose a programming language based on how much money or the demand,
you going down a dark path.

I got hired as frontend contractor
I just started doing backend work

Get hired as QA
automate a bunch of stuff
build a test suite
move into development
etc.


2 programmers in this world:

- People who list out every version of every software they've used
- Good Programmers
-

Java: Spring 8.1, 8.2, 8.3alpha, Junit 4, J
Stackoverflow, bash, http, CURL, REST, JSON, HTML


Begin does this: Rewrite your resume for every job


Personal Experience
===
- Jobs gotten from connections

Example: Apply for a job in a typical, resume, HR, meet a recruiter,
         don't get the job. You'll meet some engineers, or a rectuiter,
         someone who will get closer to a real conection for job.


HR and Recruiters - they know nothing about technology. They are seriously confused about the difference in everything.



NO ONE IS HIRED FROM A RESUME
NEVER EVER
IF WE TALK IN PERSON OR ON THE PHONE AND IT ISN'T GOOd
NO ONE IS SAYING, BUT HEY LOOK AT THEIR RESUME

WE ALL KNOW RESUMES ARE BULLSHIT


Interviews are Scary
--------------------

### Techniques
- Interview a bunch for jobs you don't want
	- Practice, see what things you tripped up on
    what things you had a hard time explain
    what made you nervous
  - Reflect on the interview


Leave a job, it wasn't the greatest leaving
you do an interview
your kinda bitter
don't get the job

you don't reflect
you say
screw the company

you reflect
you go
....oh wait, I went in there


Interviewing it's mental and you have to treat it like a 2-way streak
=====================================================================
- I want a job to learn and do awesome work, grow, you need some to do
  awesome work, learn grow. This is dating, is enslavement. You should
  like the company. Less money cooler job == more money in the long run +
  more happiness


Someone sounds desperate, thats not a good show of skills
Extra confidence does soo much.


You don't know whats expected from a Junior Role:
---
- Have a good attitude, be excited, code is fun in the beginning
- Always try and figure out your problem, before reaching out to a Senior
  and take good notes. (You do this, you will level up so fast)
  no more than 2 hours banging your head against the wall
- Every StackOverflow post READ EVERY WORD OF THE TOP UPVOTED
  COMMENT.


First Day:
 - Git problems

I can't figure rebasing
what does this mean
when I do this, this happens but I expect this

2 Types of Knowledge:
---
- vertical Knowledge, Horizontal Knowledge

learning a new concept is vertical
 - how a programming language can open a file

horizontonal more practical applications of how to use that knowledge:
 - how to open a file in a language.




Programming is a long journey
Take your time in the beginning and learn things throughly
and you're going to save time in the long run.

struggle with git and never stop and learn it in their first 2 years.
be too afraid to stop and read the docs
"What if a senior caught me reading about how the internals of git worked?"

Everyday that person waste 30 mins on stupid Git stuff.
The other person read for 2 hours.


Real First Job Problems
- Git
- SQL
- Flakey Test / CI
- JIRA
- Depenency problems











Debates
=======

Is it better to checking a potentials "class"es type, and then look for type
or check if something is a class?

What is the pythonista way, to check if something is a class


Begin: prefers using isinstance, to converting and looking for type
```
def class_name(obj):
  if isinstance(obj):
    type(obj).__name__
  else:
    obj.__name__

  klass = type(obj)
  if klass is type:
    obj.__name__
  else:
    klass.__name__
```

Confessions
===========

Python Interview
================

Quotes
======
ArtMattDank: learn everything and start by learning the concept of prioritizing things

Scraps
======

