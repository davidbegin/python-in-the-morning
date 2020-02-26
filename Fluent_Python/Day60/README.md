2020 - 2 - 21
=============

Today in History
================

1842 - John Greenough is granted the first U.S. patent for the sewing machine.
1848 - Karl Marx and Friedrich Engels publish The Communist Manifesto.


Whats makes a senior:
=====================
- Balancing MVP with Gold Plating
- recoqnizing Yak shaving and bike shedding
- knowing when to build


Long Term Goal:
===============
- Never miss a f-string for 24 hours
- A Collectional historic debates:
    - Vim vs Emacs
    - Curly Brace Debate
    - Space and Tabs
    - Git Vs the World
    - React vs Angular vs VueJS

Goals
=====
- Finish Fluent Python
- Learn some python
- Collect Opinions on next weeks schedule
    - https://github.com/davidbegin/python-in-the-morning/blob/master/PROPOSAL.md
- Viewer Code Review?
- Have Fun!

TODO:
=====
- Nightbot collect suggestions
- asciiquarium
- uppdate points disclaimer

Viewer Questions
================
tramstarzz: @beginbot what should backend dev need to know about linux servers?install database,connect app with db and deploy app?

youaresourcecode: Are microvm the same as containers? I guess they arent?


Viewer Opinion
==============
dzbanek16: Practise project idea: GitHub has recently published a CLI feature which allows you to use github features like issues, PRs etc via command line. Github also has public http API, so the idea is to create the same cli but from scratch with python
dzbanek16: Another one. Create a website with online python interpreter, so u can access it with your mobile phone or whathever you want


Begin's Advice:
---------------
- When you are learning, you should be deploying the whole time
- Start a project, ask your how you gonna deploy
- Start easier and get harder, as you get smarter/want more control
    - Heroku
    - When Heroku becomes annoying or too expensive, look into the next thing
- Some backend developers don't nothing about deploy
    - Depends on your, job project:
        - Big Company - Ops Team | No Knowledge
        - Small Startup - DevOps | Some knowledge
            - Ask how its done and learn
        - Freelance depends:
            - How are we maintaining this?
            - How much are charging for maintence?
            - What kind of requests and how often they are going come?
            - Can the client entirely own and support the infrastructure


I want to save you:
Trap: Make someone a website, cheap to deploy host at X, don't charge for
maintence and you end up working for free and the worst stuff



stupac62: is len(list) O(n)?
Games_Maik: "len is an O(1) because in your RAM, lists are stored as tables (series of contiguous addresses). To know when the table stops the computer needs two things : length and start point. That is why len() is a O(1), the computer stores the value, so it just needs to look it up."


Questions
=========
- Isn't sewing the first type of programming

- What does this mean?
    Web object publishing solution


Bounties
========
- Opensource explain of mro()
    - AKA custom method resolution order
- What do you call a program you programs iun the style of one in another lang
  - Java programmer in python
- Opensource explain of test checking that, that could  moved into type


Learnings
=========


### Hacting Advice:

Q: What does cls.__subclasses__ mean?

Junior: This method returns a list of the immediate subclasses of the class.

Nerdy Senior: The implementation uses weak references to avoid circular references between the superclass and its subclasses—which hold a strong reference to the superclasses in their __bases__ attribute.

Cool Senior: Hey kid you ever check the referemces you get back from that __subclasses__?
weak references

Junior: Why?

Cool Senior: To avoid circular references




Resources
=========
-  https://docs.python.org/3/reference/datamodel.html#metaclasses
- https://www.python.org/dev/peps/pep-3129/

Ponderings
==========

Is pythonic a vague term:
- Does everyone beleive that


frenck: I think the term is a culture term more or less. What is culture? How do you know if you belong to a culture?

Its important to join/explore/participate culture of the lang


Pythonista Koolaid Drinking
===========================
- Start everyday `python -m this`




Opinions
========

- If you go full-OO, you end up functional


### Whats Lambda good for?
- Anything async
    - sending emails or notifications
    - When you dont care about consistent startup times
    - You wanna be cheap

FAAS - Functions as a Service

Only pay for what you use

Debates
=======
- Is every single day an anniversery?


- OOP in Python sucks
    - levinson2504: just funny syntax for constructors
    - Begin: tools for functional programming like map, are traps

- Curly Braces - New Line ot Not???


- Should you abandon functional in python, cuz reaons


- Does everyone think get and setter patter boiler plate bad?



There are two schools of thought about teaching computer science. We might caricature the two views this way:

The conservative view: Computer programs have become too large and complex to encompass in a human mind. Therefore, the job of computer science education is to teach people how to discipline their work in such a way that 500 mediocre programmers can join together and produce a program that correctly meets its specification.

The radical view: Computer programs have become too large and complex to encompass in a human mind. Therefore, the job of computer science education is to teach people how to expand their minds so that the programs can fit, by learning to think in a vocabulary of larger, more powerful, more flexible ideas than the obvious ones. Each unit of programming thought must have a big payoff in the capabilities of the program.7



Is using MyPy, AKA type hinting un-pythonic?

strager: MyPy sucks!!!11
strager: Mypy gives no confidence for all projects I used it in. The type checker is too slow to iterate with. Running tests is often faster.

Begin' Thoughts: Unit Tests Replace Types and vice-versa (for certain types)

If you are gonna use mypy: Are you more concerened classes or built

strager: I disagree, streamer. Show me such a test which is redundant in a statically typed language.

strager: You could argue that your None test is still needed until the entire code base is covered by Mypy. But Mypy is not designed for 100% coverage.





Confessions
===========

Python Interview
================

Quotes
======

Scraps
======

