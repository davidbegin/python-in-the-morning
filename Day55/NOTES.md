2020 - 2 - 14
=============



### TheDirtyDemon:
- What are you goals?


- If you say you goal is to learn python and get a job


Goals
=====
- Learn Python
- Have Fun
- review rune_trimmed code
- maybe more code review?
  https://github.com/vivax3794/PyRay-project


TODO:
- add !mark command in chat


Arbaya:
-------




### Final Advice:
- Centralize Config loading into one place
  - look into common patterns for handling config for a python project
- Centralize all the Mongo logic into one place
  - import mongo should only be in one file
- Separate out logic from routing code



# you run the whole file when you import it
# you want to "run" one file
you don't your functions being called when you just import the file
You only want the "script file" or entry point to run"






If you want to use your file as both a module and a script,
you need to surround the "script calling" in __name__ == "__main__":








- whats your experience
- What are your tying learn or get (job?)
- whats the exact code you want looked at


### General I want my first job as programmer:
Some comes to your github, where do I go to learn about your hot stuff?
what are most proud of
wheres your code


- make sure you have your repos in the popular section
- with a clear indication of what the language, the project,
  what code will we see
- mark areas as work in progress
- lead people to your best code
- lead them away from work in progress
- be obessed with tests



### I'm self taught, I lean towards getting jobs through:
- Github
- Meetups
- Open Source




Arbaya
------
- move the requirements file into requirements/
- it would be nice to enable DEBUG on and off, maybe through an env variable
- what happens if there is no HOST or PORT?
  - Metaquestion: How do you handle missing configuration?
- Kiki: why is the environment variable handling everywhere
- I would only have mongo imported in one file!!!
  all DB logic should go through there for now.


### Goal: Centralize the Config
     - put it someone generic where everyone can see the full lay of the land



I am looking to dig into some interesting pieces when reviewing
early on you don't have that much really interesting, in the
you want to show off you ability to build abstractions and a proper domain.


- when refactoring, ask yourself, what is your dream interface?
  what would this look like if I could program anything


In the beginning of programming: make it work first, no matter what
- hardcode anything
- steal anything
- get it working
-


Big ole problems Junior at companies
------------------------------------
- Build everything yourself
- you build trivial things that isn't your companies core competency






You wanna be the best Junior
----------------------------
- Destroy your ego
- have no ego
- accept everyone is super genius about something and idiot about other things
- and the key is have fun, destroy your ego everyday


Vim Advice
==========
- Find to something else hard to learn
  - First Programming
  - Learning Arch Linux
  - Machine Learning
  - Networking and so confused about DNS
  - learn a whole new language or paradigm



Power Junior Advice:
====================
- You see a syntax or deprecation warning in a library, check it out on github and see if there is a fix or you can add one
- if there is a fix, but it isn't merged, read through and try it out.
- if there is some validation people need, like does it work on this version of python, or on this OS do that.
- Be careful in not providing value,



I got 10,000 lines JS I need to crank
Ill switch to vim
ARGGGG I know what to type and I can't



Code in Whatever in you want
Don't be afraid of tools
Don't be intimidated by tools
Don't be intimidated by Neckbeards











Personal Begin Advice:
----------------------
- ALL Junior Programmers should be worship cult of TDD, until they escape
  - at least a year
- you learn how to think tests, which are a design while learning to program
  - this is like learning the suszki method, you will have deeper intution,
  - instead of retrofitting

### How do you know you're ready to leave in Cult:
- If some asks you about mocking something 2 classes deep and you start getting
  anxiety
- You have a complicated and emotional relationalship with fixtures


- I don't know if this applies to data-science, I don't networking deployment

Distinction: Are we writing code that is continually going to be run and maintained

they don't know how to write tests
they gotten jobs, maybe its first data science job?
go to school


They know scripting


What are you goals?
-------------------
-





2 Juniors:
- 1 gonna program until they need tests
- 2 gonna write tests all the way

My Theory: 2 is a much more valuable and hirable indivual after less time
company: ohh I can recognize bad tests better
         I have more experience writing tests, which is a great way,
         to get your foot in the door, and learn a code that you want
         to contribute to.




using python cuz excels fails them.




Speed Running
=============
- hello world category
  - number of languages
    - 50
    - 100
  - Wether install or not
    - on what system
  - dockerized or not
- arch install -> specific goal
  - install minecraft




Viewer Questions
================
- main and init


__init__ in a folder, tells python, hey this is a module
import this sucker
and then you import __init__

Questions
=========
- !lurk what should it do???

Learnings
=========
- IBM's real name =  The Computing-Tabulating-Recording Company
  - TCTRC
  The Computing/Tabulating/Recording Company

Ponderings
==========

Opinions
========
- I don't like seeing referecnes to the database library in the routing layer
- further more I don't like seeing the database interacted with directly, I feel like
- a light weight abstraction is boiler-platey a little, but it sets you up for success.

Debates
=======

- Push on War
  - push on friday
  - push at midnight
  - push at 6AM
  - push all weekend
  - push 20 times a day
  - pushing in the mornign, pushing in the evening, pushing at suppertime
  - if pushing is a problem on friday, then pushing is a problem at anytime.



### When should you learn type-hinting as a python junior?
- I don't think its too hard

You are going to invvest a lot in learning types
and then if you go to job without typed python:
  - Outcome 1: your knowledge is not that useful if they don't type
  - Outcome 2: they do type and your super valuable!
  - Outcome 3: they don't have types and your bring in types, and you're a hero



Begin's Assumptions
===================
- We are trying to get a job now, we don't have years to learn, we don't have a year
  - We have 6 months

I would run infrastructure builds in a tmux pane, and when it finished



At some Jobs getting a development env up can be painful:
- install some specific bash tools
- install a templating tool will insert various Make targets that will reference docker containers for common commands
- have docker-compose to have a 160 micro-services and 10+ mocked AWS services running











How do more releases?
How do you release on weekends?
How do you release on friday?

Question: Just do it
You do a friday release, it goes terrible
everyone is pisssed
its friday night and they want to get drunk
but we have problems
ugh I hate this

ok how do we make sure we can get drunk next friday
ok we need more automated testing, alerting, DR











Confessions
===========

Python Interview
================

Quotes
======

Scraps
======

