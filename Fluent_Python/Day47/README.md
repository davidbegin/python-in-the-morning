2020 - 2 - 5
============

Viewer Projects
===

### juscuzryancan:

Problem: I hate planning/organizing so i would want to automate it

Programming is not just writing code, its figuring out how to solve a problem
with code or not. Refining what your objectives.

### Process for figuring out a personal coding project:
- Document your current process
- write down dream process
- write down some individual steps to get to that dream process
- make a list of things you don't know about to solve said problem
- Begin working™


How can you build a system for reminders when to go sleep.
  - how do I get a program to run at a certain time??
  - cron


Automate it if: (time to automate it) + (value gained from building automation tool) >= (time to continue to do it manually)
  - stupac

every program you want to build as a beginner is going to already be built.
Learn,








Async Interview Question:
===
  * When would you use a ThreadPoolExecutor and when ProcessPoolExecuctor?

    - ThreadPoolExecutor
        - threads are heavier weight
        - I/O
    - ProcessPoolExecuctor
        - CPU bound
        - take advantage of multiple cores


  * When would you use Callbacks and when would you use Coroutines?
    - does the async code need to coordinate with each other?
      - if yes, then coroutines
  * when its simple "embarassing parallel" async work, callbacks
    are simple???

Youtube Strategy
===
  - Post raw streams for fun
  - pick some topics that were particularly tough or interesting
    - make a dedicated

- I don't know how to photoshop
- I don't know how to video edit
- I don't anything
- I'm just doing it all, and all of it bad.

Goals
=====
- Learn more about Asyncio
- Have Fun

Bounty:
=======
- free programming language, based on brainfuck
- brainfuck is cool
  - its the smallest turing complete language


- Find me a person who uses their own TODO after one year of building it.


TODO:
=====
  * Checkout AltF4's tool called Quirk. It waits a while after you go live and then gets a screenshot and sends a notification
quirk.gg


Fun to Do at your company
===
  - Buy domain, purchase ones for company to squat and use those.
  .fail
  .exposed
  .wtf


Links:
=====
  * http://www.astronomy.com/news/2019/06/hacking-apollo-14-how-an-mit-computer-scientists-saved-a-lunar-landing
  * https://arcolinux.info/choose-your-project/
  * https://workflowy.com/


What Interests Begin
====
  - NASA says we go to the moon, we need a watch
    Omega makes the speedmaster
    Rolex makes the Cosmograph, Daytona

    Rolex loses

    Paul Newman wore this watch everyday, and raced with it
    and watch nerds omg this is the greatest watch ever.

Viewer Questions
================
- used mkvirtualenv, but now can't
  - first how did you install it the first time?
  - when its installed, where on your computer was it installed

Theory I:
  - you installed it in a virtualenv, and are now not in that virtualenv

- Why is ubuntu better for DevOps (versus Pop OS)
  - https://ubuntu.com/public-cloud
  -  https://ubuntu.com/#developer

we can't say that Ubuntu is better than Pop OS
but, we can say, that Ubuntu is doing better adverstisment
to "DevOps" engineers

How are you deploying to AWS
and how does your environment interact with that.

Does your system have docker???


Big Facts
====
- Begin doesn't need VMs in the Cloud





Python Problems
===
- We aren't concerned about the latency assoiciated with reading from
Disk. Python is smart enough not to block on built in filesystem methods,
it releases the GIL.

Questions
=========
- What is run_in_executor for, int he new world of `async def`?
- What is this endeavouros?
- How does /dev/urandom?
- I don't totally understand entropy within the world of randomness?
- What is entropy
  - the minimum number of yes/no questions, to be able to deduce the seed
- What is are the patterns/best practices around passing Semaphores, in
  async python code.

  Is it common for the individual function that has the lock, to also
  take the lock????


python -m venv name-of-venv
```
python -m venv venv
source venv/bin/activate
```

New Business
====
  * EAAS
    - entropy-as-a-service
    - scalable entropy solutions for the modern developer

Learnings
=========
  /dev/urandom - The random number generator gathers environmental noise from device drivers and other sources into an entropy pool.

Ponderings
==========

If we see a function with the following characteristics,
what does it mean:
- function returning future
- function taking a future.


Programming Hipster Advice
===

Use an obscure language, and be confused that others don't
Begin's personal suggestion: Eiffel






Opinions
========
- You don't want to manage your infrastructure in a UI
  - AWS Console
  - Some other console

- You need your infrastructure in Code.
  - Terraform, Cloudformation, Pulumi, CDK, Serverless framework

Don't just adopt a tool for a problem you don't neccessarily have
  - mkvirtualenv
  - git tools is a common example

Simple virtualenv workflow:
  - create a virtualenv in each project with

```
python -m venv venv
source venv/bin/activate
```

add a requirements.in and requirements.txt
then move to develop.in and develop.txt



Common Junior Mistake:
  - Pulling in libraries, tools, services etc, to solve problems they don't
    have. Then you have to spend time debugging things, that aren't actually
    needed.




Debates
=======

What is the recommened practice for managing virtualenv in Python in 2020?

Begin Opinion: base-level of required knowledge:
  - How do we handle our virtualenvs with JUST python


Beginner:
Seasoned:

### Rolling Release good or bad?
Pro:
  - you are always pulling in small changes, that you can grok
    instead losing a whole day every major update
Con:
  - OMG its unstable (Begin hears this ain't true)

A chicken is a dinosaur: change my mind.
Facts:
- We don't know what sounds Dinosuars make
- Lot of people think Dinos were covered in features
- Laid Eggs

- Jurassic Park Lied
  - Foley Artist

I can decide what animals sound like??






Confessions
===========

Python Interview
================

Quotes
======

It may be harder, but soon it will be easier, once we get smarter
 - Begin (on arch)


Scraps
======

