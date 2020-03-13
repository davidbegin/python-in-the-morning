2020 - 3 - 2
============

perl -lape'/(foo_\w+)/;$_=$1' SQL.txt

quotes in ag == regex

```
ag 'Quotes\n(-|=)*\n*(---|===)*'

ack 'Quotes\n(-|=)*\n*(---|===)*'
```






#### Unix Tools
- find
  - fd
- grep
  - ripgrep
- ack
  - ag

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

Viewer Questions
================

Maximilian_Hots: Is it true ATMs had a code to access the OS of the ATM from the ATM?


Questions
=========

- Which regex website is best:
  - https://regexr.com/
  - rubular
  - regex101

- parse package

- whats the advantages and disadvantages to using alt unix tools?
  - portability
  - stood the test of time:
    isidentical: well one thing that comes to mind is these default unix tools are maintained for like decades and we can trust them

- Why were ag and ack developed?
  - speed

- What is the search pattern syntax for grep and ag (ack is Perl)?

grep -iRl

Why can't I match


The Fear of Rexexp
------------------
- Copy and pasting the same ancient very complicated regex that no one understands
- Often other ways to solve than regexp

Quotes
------

If you program you have to deal with regular expressions at sometime
- David Begin


Learnings
=========

I don't think ?: has a formal name. From Perl's documentation: "This is for clustering, not capturing; it groups subexpressions like "()" , but doesn't make backreferences as "()" does." From Python's documentation: "A non-capturing version of regular parentheses."
i


in vim this is called Patterns
```
s/dhflkujhs/sdfjklhslkj
```


clustering versus capturing

ack is a replacement for grep
ag is a replacement for ack


 In regex to match exact number or more would be -{3,}|={3,}


Regular expressions can be concatenated to form new regular expressions; if A and B are both regular expressions, then AB is also a regular expression. In general, if a string p matches A and another string q matches B, the string pq will match AB. This holds unless A or B contain low precedence operations; boundary conditions between A and B; or have numbered group references.

Ponderings
==========

You didn't get done your HW
- Answer what you did instead
- Why
- Was it worth



do people say raw string or raw literal or raw string literal or s-string?
 
Where do people often `r` aka raw literal:
- paths
- regex
- anything with lots of /

Begin uses the term raw-string for unsanitized strings:
 - source string
 - source data
 - tainted is perl term

Opinions
========

- Docs can be as long as they are needed, as long as their at the same level of
  information. 

Debates
=======

Regex
Rejex

Which Regular Expression is best:
- Perl - miguelmirq

stupac62: Perl is great at doing anything with text, right?

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
() = matches
[] = character class [a|b]
{}

\w
\W
\s
\S
\d
\D


HazeAnderson: [] indeed implies or
  [] implies or unless you change behavior with special chars

Metacharacters are not active inside classes. 

Scraps
======

TODO
====
You can use the more restricted definition of \w in a string pattern by supplying the re.ASCII flag when compiling the regular expression.

make a !git


- Learn about lookaheads
- continue to work on parsing python in the morning, 
