2020 - 3 - 4
============

PEPs to Review:
- PEP-558: Type Hinting Generics In Standard Collections
  - https://www.python.org/dev/peps/pep-0558/
- PEP-614: Relaxing Grammar Restrictions On Decorators
  - https://www.python.org/dev/peps/pep-0614/
  - https://github.com/python/cpython/pull/18570/files
- PEP-585: Defined semantics for locals()
  - https://www.python.org/dev/peps/pep-0585/
- PEP-615: Support for the IANA Time Zone Database in the Standard Library
  - https://www.python.org/dev/peps/pep-0615/

Bounties
========
- eval in the wild in an used opensource project
  - how could we update without eval
  - all parsing: ast.literal_eval
    - why use eval
    - speed?

- Are you excited excited 614:

Viewer Questions
================

-  i started to work this week! Can you give me some tips how to understand/read codebase (of one service)

- Take copious notes
  - first job is to improve the onboarding for the next person
  - anything that confused you is gonna confuse the next person
  - Find out where people are documenting ahead of time:
    - third-party: Google Docs, Quip, Confluence, github wiki
    - In code
    - In READMEs
  - Git Blame and take notes often, as well as look at Repo insights:
    - stitch together who are the Domain experts and where do people work
      across
  - Run everything, run the tests of everything the sooner the better!

Questions
=========
-  path traversal attacks
- https://www.wikiwand.com/en/Directory_traversal_attack
Directory traversal is also known as the ../ (dot dot slash) attack, directory climbing, and backtracking. Some forms of this attack are also canonicalization attacks.

- Will PEP 615 be good for windows?
  - cuz windows doesn't have system TZ?

- What is the CLDR?
The Unicode CLDR provides key building blocks for software to support the world's languages, with the largest and most extensive standard repository of locale data available. This data is used by a wide spectrum of companies for their software internationalization and localization, adapting software to the conventions of different languages for such common software tasks.

- How do you get PEPs accepted:

PEP Acceptance Techniques:
- Reference original implementation
  - What were the authors OG intent
- Explain what bad patterns come from the current syntax:
 - This is balance
- In short: if we're removing somewhat arbitrary restrictions, we should remove all of them.
  - don't just keep adding to or removing some particular syntax, back
    up and reapproavh
- This new grammar is fully backward-compatible with the existing grammar.
- Invoked the authority of standards??? This is standard to the web
- If there are some system specific implementation details, then we should
  allowing config
  - How should should these customizations be used? or interacted with?
- If something is configurable, we need to consider wether it will
  typically be configured by default. And explain how future design
  decisions will be made based off that.
- Call out potential security issues with implementation



- When is proper time to use eval?
  - isidentical: never
  - beginbot:    to impress your friends


- What is graminit.c  for?
  - genererated from Grammer
  - That file is generated to go from an NFA -> DFA


What is wrong with tzinfo?

Why do return the same ZoneInfo object if initialized with the same key?

What does a TZif byte stream look like?

Why is this a problem:
Unlike the primary constructor, this always constructs a new object. There are two reasons that this deviates from the primary constructor's caching behavior: stream objects have mutable state and so determining whether two inputs are identical is difficult or impossible, and it is likely that users constructing from a file specifically want to load from that file and not a cache.
A: If you have a contructor that should always return the same object on input
   that input shouldn't be mutable. Otherwise people could be confused

Learnings
=========

```
>>> reset_tzpath(to=["/my/custom/tzdb"])
>>> a = ZoneInfo("My/Custom/Zone")
>>> reset_tzpath()
>>> b = ZoneInfo("My/Custom/Zone")
>>> del a
>>> del b
>>> c = ZoneInfo("My/Custom/Zone")
In this example, My/Custom/Zone exists only in the /my/custom/tzdb and not on the default search path. In all implementations the constructor for a must succeed. It is implementation-defined whether the constructor for b succeeds, but if it does, it must be true that a is b, because both a and b are references to the same key. It is also implementation-defined whether the constructor for c succeeds. Implementations of zoneinfo may return the object constructed in previous constructor calls, or they may fail with an exception.
```


TZINFO Path allows customizing lookup:
- Global configuration via a compile-time option
  - Who should use this one: System maintainers, AKA people provided a python
    version to use.
- Per-run configuration via environment variables
  - Users of a program, who own the system?
  - Who want the lookup constant?
- Runtime configuration change via a reset_tzpath function
  - Change Lookup TZ lookup at runtime
  - Why are you doing this?
  - Plz say a test
  - plz plz plz
  - This is likely to be primarily useful for (permanently or temporarily) disabling the use of system time zone paths and forcing the module to use the tzdata package.




What is an Expression?
  This can be summarized as "anything that's valid as a test in if, elif, and while blocks". This differs subtly from a perhaps more popular definition, which can be summarized as "anything that's valid as string input to eval".
  - Begin thinks of lambda, because thats where I want more freedom
  - isidentical: When I describe expression, I say anthing that can be put inside a list as an element

- Don't say you are more popular than jesus

General Rating System: -1 -0 0 +0 1

isidentical: you can hack with grammar by changing Grammar/ file in your fork and doing make regen-all && make -j8


How do you say IANA time zone database?
 - I-ANA


IANA time zone database (also called the "tz" database or the Olson database

```
a = ZoneInfo(key)
b = ZoneInfo(key)
assert a is b
```

We return the same ZoneInfo singleton, because we use an `is` check
when doing arithmetical operations

ZoneInfo.nocache(key: str)
This is an alternate constructor that bypasses the constructor's cache. It is identical to the primary constructor, but returns a new object on each call. This is likely most useful for testing purposes, or to deliberately induce "different zone" semantics between datetimes with the same nominal time zone.



We must take careful consideration around ZoneInfo and caching.


str for computer
repr for humans
so of course ZoneInfo shows the key for the str, because computers know about this,
thanks to IANA

Ponderings
==========

- In order to avoid forcing all datetime users to import zoneinfo, the zoneinfo module would need to be lazily imported, which means that end-users would need to explicitly import datetime.zoneinfo (as opposed to importing datetime and accessing the zoneinfo attribute on the module). This is the way dateutil works (all submodules are lazily imported), and it is a perennial source of confusion for end users.

Guido did not accept syntax without a use case

The value of syntax is super important on context:
- Company Library Code
- Opensource Library Code
- Personal Project
- Company Application


decorator: '@' dotted_name [ '(' [arglist] ')' ] NEWLINE

This PEP proposes that it be simplified to:

decorator: '@' namedexpr_test NEWLINE

Opinions
========

- You start something new, look up awesome-that-thing on github
  - collection useful links and resources

Lambda Logging: Applications Logs
  - Are you using structured logs?
    - structlog in python
  - How are you tracing logs between Lambdas and other services
  - Are you using log levels correctly:
    - Pro-Tip: Sample Debug Logs
  - Take some time to get the balance of INFO, to WARN to ERROR.
    - Look at the overall patterns of your info logs, and see are they useful
  - All logs, keep specific data, like IDs, out of the message and in the metadata
  - are you using AWS X-Ray
  - Your logs go automatically to Cloudwatch, you always want to ingest from there
    - if you send logs early, you could slow down the Lambda,
      so you want AWS to flush em at the end

- Cloudwatch - Logs
  - What happened at this point in time, an event
- X-Ray      - Traces
  - a node on a graph of the request path

When Begin first came to Python from Ruby he was hating on date, datetime, time, API

- DNS is the most annoying to debug:
  - Aks yourself: did my fix not work, or do I need to be patient

- This was rejected properly:
  - https://www.python.org/dev/peps/pep-0666/

PEP-614:
  - isidentical - don't think it's needed?

The buttons in a list example, wasn't incredibly convincing

I don't like the definition of something being where it can be used


Debates
=======

- What are commit messages for?
  - When debugging

Confessions
===========

Python Interview
================

- What is a Python "Expression"?
  - the only valid body for a lambda
    - can't have assignment

Quotes
======

HazeAnderson: I read someone explaining that Java is essentially a language with no verbs, only nouns (and the VERY end there is a verb but you can't see it)

Sales
=====
 -  readable, idiomatic, and maintainable

Scraps
======

Beautiful Code:
===============

```
self._purifier.visit(tree)
```


Begin's a Weirdo:
=================

### Morning
- Avoid the computer for just a while!
- 30 mins to an hour and the whole day feels more wide open
- prepare for the day
- read
- journal
- meditate
- exercise


### Sleep
- go to sleep earlier 9PM
- setup some social pressure to wakeup
- avoid things that wind you up at night
  - Not computer, no phone, no TV
  - Books
  - Meditate
  - Clean
  - Journal
    - What made today awesome!!!
       - Feel good
       - Feel appreciative and grateful
       - You notice how much you've done
    - What would have made it better???
      - You get to reflect
      - you get some simple action items
      - feel like the day is done and you can close the chapter and go
        to sleep
- Make a time minimum for sleep
  - if you wake after that, stay up.
  - Example: at least 5 hours
    - Sleep at midnight, woke up at 4, going back to sleep.
      - but if I wake up at any time after 5, I am staying up
      - despite what the alarm clock says
- Wake up natural, your alarm first should be no alarm, then light,
  then sound


Begin at night problem:
- I stop working and I just keep planning and acting like its work
  - Ill do this tomorrow
  - clean up my email
  - organize my cal
  - Ill make a list of things I want to do for the stream


Work / Life Balance:
--------------------
- I do solve lots of stuff not in regular hours
- Don't try to feel obligated to be super inspired during hours
- Need some rules about when to shut off (unless you are on call at the time)



Work / Home Life Synergy
========================
- How can I build something fun, that will help me learn about something
  that would be relevant to my work. Can I stream it?


TODO
====

- Friday: Discuss the std lib / Pypi hybrid modules
It is also not yet clear how these hybrid standard library / PyPI modules should be updated, (other than pip, which has a natural mechanism for updates and notifications) and since it is not critical to the operation of the module, it seems prudent to defer any such proposal.


ArtMattDank: update the cube code to say "faster!!" if you don't beat the record
  - ast.literal_eval - got to check that out
- Check out: https://github.com/python-discord/snekbox
-  song Toilet Brushes

beeware is the hottest organization in the python ecosystem, they are writing a gui toolkit that natively compiles to android package, ios package, linux, windows, even the smart tv systems


- https://wiki.archlinux.org/index.php/System_time


- Talk about best git practices:
  - At my work we banned talking git workflows for while
  - some things are a holy war
  - rebase versus merge
  - development branch
  - git flow
  - it all depends, number pf developers, deploy cycle, CI/CD,


- General Git Advice:
  - Nicely named and consistent branches:
    - include that ticket number
    - nice commit messages
      - follow some standards

Separate subject from body with a blank line
Limit the subject line to 50 characters
Capitalize the subject line
Do not end the subject line with a period
Use the imperative mood in the subject line
Wrap the body at 72 characters
Use the body to explain what and why vs. how

- https://keepachangelog.com/en/1.0.0/


- importlib.resources [15] access patterns and older access patterns like pkgutil.get_data [16] .
