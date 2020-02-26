2020 - 2 - 24
=============

Fact of the Day
===============
Claude Shannon died on this date:
  - https://www.wikiwand.com/en/Claude_Shannon
  - https://www.wikiwand.com/en/A_Mathematical_Theory_of_Communication

"He is also well known for founding digital circuit design theory in 1937, when—as a 21-year-old master's degree student at the Massachusetts Institute of Technology (MIT)—he wrote his thesis demonstrating that electrical applications of Boolean algebra could construct any logical numerical relationship."

Goals
=====
- Learn About Pathlib
- Learn About searching text from the command line
- Read something on the Arch Wiki

Resouces
--------

Tools:
- grep
- find
- ack
- ag | alt to awk
- fd | alt for find

```
pacman -S the_silver_searcher

man man

man -Tpdf ag | zathura -
```

- https://stackoverflow.com/questions/7727640/what-are-the-differences-among-grep-awk-sed
- http://www.theunixschool.com/2012/09/grep-vs-awk-examples-for-pattern-search.html
- https://github.com/ggreer/the_silver_searcher

Python Module
-------------

- https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/
- https://treyhunner.com/2019/01/no-really-pathlib-is-great/
- https://realpython.com/python-pathlib/
- https://docs.python.org/3/library/pathlib.html


Arch Wiki
---------
- udev
  - https://wiki.archlinux.org/index.php/Udev
- encrypted socks
  - https://wiki.archlinux.org/index.php/OpenSSH#Encrypted_SOCKS_tunnel
- environment variables:
  - https://wiki.archlinux.org/index.php/Environment_variables

Questions
=========
- When should you use grep vs awk vs find vs ag?
- what language is each bash tool in?
  - Are there variations
- how are they included on your computer
- When should we not use Pathlib?
  - certain shutil functions and chdir
  - some zip functions didnt support pathlib in 3.6.
  - When pathlib IS the performance performance
- When was Pathlib introduced
- What is resolve()
  - Gives us the fully qualified path
- Can we give the advice to never type `os.path.join` again and always use `Path(".").joinpath("logs")`
- When should we use glob? not apart of Pathlib
- Why is pathlib so much faster
- When looking for files by pattern in bash, what is the preferred tool
- What are all the versions of find?
- What was the first find?
- What is find written in



Later
-----
If you are using find in an environment where security is important
(for  example  if  you  are using it to search directories that are
writable by other users), you should read the `Security  Considera-
tions'  chapter  of  the  findutils  documentation, which is called
Finding Files and comes with findutils.



Perf Results
------------


Bounties
========
- Python AST to Brainfuck

Viewer Questions
================
tramstarzz: anyone know some free cloud linux server where i dont need to put my credit card/visa

kibal89: how change languaje es_ES in git bash windows


History
=======
-  https://www.wikiwand.com/en/Censorship_of_GitHub#/Turkey


Learnings
=========

- We have to use os.path.join, versus just string concat to handle windows as well as if theres a / or not

- Pathlib for globbing is way faster


- https://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html



So "foo -a -bc --now -d bar -- baz -e" runs command "foo" with options a, b, c, d, and --now, option d has argument "bar", and the "baz" and "-e" are not options


not options is what is confusing



Using a CLI program:
- Options = configuration for the program
- Non-Options = things for the program to operate on



doas -- pacman -Syu 


## Difference in:
- argument
- option
- parameter

A command is split into an array of strings named arguments.

A parameter is an argument that provides information to either the command or one of its options,

An option is a documented type of argument modifying the behavior of a command



what does depth first mean

What is find's typical traversal Algorithm



# Spelling in Vim
z=
1z=
zg = add to dictonary


Ponderings
==========
- When are you allowed to say you know a programming langauge?
- In this case python
- can you solve your problems with it


Fake Rune Trimmed:
- Have a project on your github that you're proud of
- Contribution to a Python Open Source Library
- Write a Python Blog Post


SMART GOALS:
S – Specific M – Measurable A – Achievable R – Relevant T – Time-Bound






Opinions
========

When you are learning to program,  if your head don't hurt, you're not learning

You will full days, where nothing makes, and you are confused all day.
then you go to sleep and wake up it will make sense

or you hear something for the millionth time and it clicks



You trying to learn to:
- Google
- How to know what to learn




Tips for Learning Programming:
------------------------------
- Be formalized in your lack of knowledge


You're Stuck
Make a small Goal: get this thing to print
What's currently happening
What's your theory for why its not working
What's sometihing to learn to get that answer



Goal: Get Git in English
Current: Its in Spanish
Theory: My system is setup for Spanish, and git is using that setup 
Knowledge to Acquire: How does git choose a language
https://www.git-scm.com/book/en/v2/Customizing-Git-Git-Configuration


kibal89 Questions
-----------------
- What is a locale


Debates
=======

Confessions
===========

Python Interview
================

Quotes
======
Speed is byproduct of efficiency

J'SON is a name
JSON is a object notation

frenck: so Pythonic is adjusting to the context :)


Scraps
=====

TODO
====
- Get the PEP command working
- add !python and !linux
- Add something that saves cube times, for highscores
- Figure out why autocomplete keeps stop-working
  - might have to do with putting vim in the background
