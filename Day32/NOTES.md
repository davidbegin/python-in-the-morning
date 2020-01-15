2020 - 1 - 15
=============


Problem:
 I cant figure out how to merge duplicate rows in the output of a new CSV

name, age
begin, 32
sammy, 27
sammy, 27


Quiz
====
  * What is the difference between:
    - NotImplemented
    - NotImplementedError

Questions
=========
  * What is the arctype of a tall lanky and short stocky duo
    - Wet Bandits
    - Lumiarie and Cogsworth

  * What does commutative mean:
    - binary operators, if you change the order, the results the same
      a + b == b + a
      if a and b or numbers its commutative
      but if its a vector

  * To use a recruiter or not:
    Pro:
      - Less work for you
      - Do lots of interview practice
    Con:
      - They take some of your salary
      - Can be annoying



* You favorite thing should be your hobby,
* 2nd fave your job






Learnings
=========
  * If you implement a custom __add__ method, YOU should you always implement the
    "reverse" method
    Purpose of "Reverse" method:
      - if the left side can't handle the infix, can the right side?


What is the Difference between:
  * NotImplemented
    - is a special singleton value that an infix operator special method
      should return to tell the interpreter it cannot handle a given operand
    - When you return this, you are telling the interprotor, hey
      check if the other side of the infix has a reverse method
  * NotImplementedError
    - raised when you don't write a concrete for an Abstract base Class.





What is the problem with NOT returning a NotImplemented singleton, when you
binary infix can't handle it's shit???
.....You loose the lookup of __radd__, to let the right side of the expression
handle the operation.




Ponderings
==========
  * Should you use errors for control flow????
  * Recruiting has shifted from independents that
    collected a commission versus what it is now
    --- large staffing firms that take a cut of your hourly rate


What to look for in a job:
  * is the product cool
  * is the team smarter that you
  * do you have freedom of technology choices



If you have a comment, ask yourself:
  * Could I change my code, so that it would communicate this
    same message?
    Why? Comments drift from code

    Comments are for the Why
    Code is for the What






Opinions:
=========
  * __radd__: “reflected” or “reversed or "right"
    √ reversed method
  * spartangtr:
    - Django rest framework is particularly bad about this
    - sinatra is too simplistic
  * I like how smaller frameworks, force you think about a decision
    you are making


Working in Sinatra or any micro-framework can be annoying.
I want auth, ugh, find the auth plugin, then add it, customize.


```
Django -> Rails
Flask  -> Sinatra
```




When you start coding, go for 100% test coverage, go test crazy, overtest,
and eventually you'll learn what bad tests, brittle tests, slow, when not to test.


Pick a Project, that makes you money, or helps in some way
Deadline, friends family, other coders
Ship that project, write a blog posts, do a tech talk at a meetup.



Don't get into code just for the money.

Frontend Dev
Backend Dev
Full Stack
Machine Learning
DevOps
Data Science
Big Company
Small Company
Tech Company
Non Tech Company


Some Devs wanna crank out code
others want to architect things
some like to write tests all day
some like ship features fast




Self-Employed as first programming Job:

Pros:
  - Easier to get you foot in the door
  - Pick your projects, based off what you wanna learn
Cons:
  - source clients
  - want mentors looking at your code





How to Refactor:

Take the current functionality:
  * Put it under test





































Goals:
======
  * Not burn out
    How:????
      - Have Fun
      - Learn
      - Don't take life too serious
      - Take breaks
      - Go outside
      - Pet a Dog





Web App
=======
-> Router Code
   rescue any uncaught error and return a 500

-> Model Code
  - catch and reraise
-> Library 1
  - catch and reraise
-> Library 2
  - catch and reraise
-> Library 3
  - catch and reraise
-> Library 4
  - raise an error



do not overbuild, only build what the client asks for
premature optimization is the root of all evil










