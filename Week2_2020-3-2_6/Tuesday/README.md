2020 - 3 - 3
============

#### Tools
- vim
  - BRE
- find
  - fd
- grep - 3 Options: Posix, extended and Perl
  - default BRE
  - ripgrep
    - Custom Artesian standard
    - PCRE2
- ack - Perl
  - ag
python
 - Perl

```
man -k | dmenu -l 30
man man
man -Tpdf ag | zathura -
```

Python Module
-------------
- re - https://docs.python.org/3.9/library/re.html
- https://pymotw.com/3/re/index.html
- https://pymotw.com/3/difflib/index.html
- https://perldoc.perl.org/perlreref.html

Bounties
========

- Vim-plugin to shown when each engine is used

- Stories of the most specific bug:
  - American Somoa Timezone

- Who other than Kleene has more things named aafter them
  in math, science, computers

  - Euler
  - https://en.wikipedia.org/wiki/Category:Lists_of_things_named_after_mathematicians

- Make an engine that pareses a regular expression into and english
statement, feed that to say
  - Does it have to be its own regular expression engine

is (?:) only part of PCRE?

Viewer Questions
================
- Building a twitch from scratch or from libraries:
  - Is it for using or for learning:
    - Learning - scratch
    - Using    - using a library

Haze Regex Puzzle
die "invalid format: $code\n" unless $code =~ /x[spq][0-9]+_[0-9a-z]+/;



1. An old, backtracking engine that supports everything.
2. A new, NFA engine that works much faster on some patterns, possibly slower
   on some patterns.



When refactoring the use of regexs:
- Did you change when you choose each engine or force one-engine by default?


What are the context for writing regular expressions:
- Inside you editor
- unixy
- in your programming langauge



Questions
=========
- Whats the difference in the 2 Vim Regex Engines?

- What does grep standfor
globally search a regular expression and print

- Who were regular expressions invented

It is a technique developed in theoretical computer science and formal language theory.



Who uses Chomsky type 3
- compilers and parsers

- What is Raku
  - Perl 6
  - What is so hot about Raku Rules?
    - What are some patterns or usecases

- Learn about lookaheads
  - Where do exist in the world of regular expressions

- Comparision of POSIX -> Perl -> Raku


what are SEXEGERs?

Quotes
======


Learnings
=========

Why no just the full syntax of PRCE?
  - Speed, we don't need to do fancy lookaheads and whatnot
    we can speed


```
# BRE
# () are literal
a*(bc)

# () are metacharacters
a*\(bc\)

# ERE
# () are metacharacters
a*(bc)

# () are literal
a*\(bc\)
```


vim - is BRE?
    - is it its own thing
    - is that are patterns are?

However (and this is the fun part), the characters () {} are treated as metacharacters in BRE if they are escaped with a backslash, whereas with ERE, preceding any metacharacter with a backslash causes it to be treated as a literal.

What’s the difference between BRE and ERE? It’s a matter of metacharacters. With BRE, the following metacharacters are recognized: ^ $ . [ ] * All other characters are considered literals. With ERE, the following meta-characters (and their associated functions) are added: 

#### BRE
  - ^ $ . [ ] * 

#### ERE
- ( ) { } ? + |

#### PCRE AKA Perl
- (?:) Non-Capture Group
- Lookaheads introduced in PCRE

2 Top Rexep Implementations:
- Perl
- POSIX

students of Alonzo Church, Kleene, along with Rózsa Péter, Alan Turing, Emil Post, and others, is best known as a founder of the branch of mathematical logic known as recursion theory,


Leader -> Alonzo Church
Students AKA the squad -> Kleene, Turing Peter, Post
Invent -> Recursion Theory


This regex apparently is trash?
(x+x+)+y
The solution is simple.
When nesting repetition operators, make absolutely sure that there is only one way to match the same match.
If repeating the inner loop 4 times and the outer loop 7 times results in the same overall match as repeating the inner loop 6 times and the outer loop 2 times, you can be sure that the regex engine will try all those combinations.


Kleene Quiz
-----------
- Kleene Star
- Kleene Hierarchy
- Kleene Alegebra
- Kleene Recursion Theory
- Kleene fixed-point theorem
- https://www.wikiwand.com/en/Free_monoid
- https://www.wikiwand.com/en/Intuitionism
- https://www.wikiwand.com/en/Powerset_construction
- https://www.wikiwand.com/en/Quine_(computing)
- https://www.wikiwand.com/en/Lattice_(order)
- https://www.wikiwand.com/en/Complete_partial_order


{\displaystyle (L,\sqsubseteq )}

Introduction to Metamathematics



What is a Quine?
https://www.wikiwand.com/en/Quine_(computing)



How does a programmers learn math who dropped out of H





Fear of the Uprade
------------------
- Write dowm what version you are on and what version you area upgrading to
- get the changelog
- upgrade
- take diligent notes on what seems broken, your theories,
  steps you take to fix
- read the changelog
- use google and record the sites you read for information

This ends up being our job as computer programmers working
on legacy systems


Fenyman Technique - Keep learning until you can explain 
it simplfy

Ponderings


What are the context for writing regular expressions:
- Inside you editor
- unixy
- in your programming langauge


What are the context for writing regular expressions:
- Inside you editor
- unixy
- in your programming langauge
==========



Opinions
========

- I love when libraries have why you shouldn't use section!!!

Debates
=======

Regex
=====

Confessions
===========

Python Interview
================

Regex Interview
---------------

- . ^ $ * + ? { } [ ] \ | ( )

. = anything
^ = the start of anchor to start
$ = anchor to end
* = 1 or more
? = 0 or more
\ = escape character
() = matches or capture groups
[] = character class [a|b]
{} = quantifiers

\w
\W
\s
\S
\d
\D



Programmer Trivia
-----------------
- What is the difference in POSIX, extended POSIX, and Perl regex


Scraps
======

```
ag 'Quotes\n(-|=)*\n*(---|===)*'
ack 'Quotes\n(-|=)*\n*(---|===)*'
```


TODO
====
- Learn about lookaheads
- continue to work on parsing python in the morning, 
- stupac mod
- install ripgrep
  - I use 2 aliases for rg (rga stands for ripgrep all): alias rga="rg -S --trim --no-ignore --hidden" alias rg="rg -S --trim --ignore"
  - History the tale of Balkanization



Tests need to be written for output:
- Comparision:
  - all the syntax 
    - BRE
    - ERE
    - PCRE2
    - Vim
  - tools:
    - timing and the syntax






Next Monday
-----------
- sockets

Next Friday: https://www.youtube.com/watch?v=S0AdB36WuAU

