2020 - 3  - 7
============


Explain explain monads to a python dev with no functional programming knowledge

- an elementary individual substance which reflects the order of the world and from which material properties are derived
- a monad is a monoid in the category of endofunctors, what's the problem?

- types help us make total functions
- A total function is a function which, for every input, there is an output.
















Begin explain Maybe:
  - Data represents something or nothing, Optional in python
    - the semantics of what you are doing is contained into the structure


def handle_stuff(val):

def handle_stuff(val: Maybe):
  # Haskell woah a maybe, did you handle none




































Determinist
===========
- Use callbacks with fetch in the old style
- optional to return a rejected promise
- Why the multiple options:
- Why livescript?
- Callbacks versus promises?
  - Callbacks:
    - easier to annotate
- Does httpFetch return one type of error always
  - Why you choose that?
- Is Livescript automatically binding object instances to `this`

```javascript
const x = { 
  y: 1,
  f() {
    console.log(this.y + i)
  }
}
```


TODO:
consider googling "reading simple haskell" if you like (i wrote the tut, full disclosure).

Goals
=====
- Make money from math

Topics
======
- Explain what the heck this Kleene was all about??????
- Code Review
- Haskell in Python

Kleene Quiz
-----------
- Kleene Star
- Kleene Hierarchy
- Kleene Alegebra
- Kleene Recursion Theory
- Kleene fixed-point theorem

Resources
=========

Bounties
========
- I want baby named: Zermelo

Viewer Questions
================
- bobboross0: Do you konw what algo it uses for the pattern match ?
- haskell useful in bioinformatics ??
- haskell versus elixir
  - elixir types have nothing on Haskell
  - 
- livecoding: better Q about currying is why bother not providing all args at once
  - 

Questions
=========

- How does associativity make us money?
  - Some expensive computation
  - We need to paralellize
  - time = money
  - We can prove, the grouping, we can go fast like Sanic
  - Embarassing parallel?


-  axiomatizations == assumed truth????
   self-evident truth
   taken for granted

standard axiomatic set theory ZFC

Learnings
=========
- reification (reify)
  - The type by 
- Monads are algebraic structures
  - Algebraic?????

  Alegebra is a class (not a code class)

  Abstract Alegebra

  Philosophy of Math or Meta-Math

  Not using Math, the logic of math
  

Zach's Math Pitch
=================
- 
- I only need one: https://www.wikiwand.com/en/Principia_Mathematica

Ponderings
==========

- Why Haskell likes it one file?


Opinions
========
ZazH: one compontent per file seems like overkill

Learning one language helps you with other langs
  - Haskell helps with Typescript
Zach: The education for Math Sucks
Begin: How do we fix it

Zach: Haskell will help with anything


WE don't learn abstract


Abstract Alegebra
=================
- useful for programming
- interfaces of AA, are similiar programming, API, contract
  - numerical equations in the wild, what are the laws
    - 2 + 2
    - 100 - 19
      - Theres a pattern, theres things, the theory of twos:
        - 
  - Monoid
V - Rules Monoids:
    - A structure equipped with a binary associative operator
      which obeys the following laws:
      Given:
        - (M,*,i) -> our system
          -> M is a set
          - set of anything
          - let e 3 M
            e * i = e
        - * is a binary associative operator
        - i: (identity)
          - (a * i) = a
          - (5 + 0) = 5
          - ([1,2,3] + []) = [1,2,3]
          - When we apply an empty elements -> no affect
        - let a, b, c E M
          - a * (b * c) = (a * b) * c
          - This can expand to more values
          - associative law
          - The sequence of the values, but the groups

Show the associative on strings (Bonus: List)

""
"ca" + "t" = "c" + "at"

[1,2] + [3,4] = [1,2,3] + [4]

- * doesn't mean multiplication, it means whatever the binary
  operator in the language
      

- putStrLn $ show $ inc 3 
- I want to call chaining
- you say its adjusting parentheses
- function calling is left associative





If I have something, and use a binary associative operator with
the 2nd element 



Variadic function

Given a set 

Terms:
======
- Type class similiar to an ABC
- identity or id or unit: 
  - Identity, some element of a set, that when applied to another element of that set, has no change
  Addition on Natural Numbers
  infinite..infinite
  What is a thing that applied to anything in this set
  it wouldn't change
  (M,*,i)
    M = Lists
    i = []
  (M,+,i)
  (M,-,i)
- Data-constructor

Maybe Not:
----------
- Kind and type constructor are the same thing
suppipi: type constructors are types that take a type and return a type
suppipi: kind is the type of a type

* -> *
Type constructors have kinds!





- mappend is an overloaded function for every monoid

- mempty
  -> return the empty element, the unit





mappend is a binary associative operator
- its definition changes based on type


Haskell Selling Points
======================
- Infinite Data Structures
- Define Operators
- You use $$$$ all the time
- Parallel By default
- everything is curried
- any binary operator can be infix
- Everything operator is a function
- Zach at checkout


- Type constructor - like a function at the type level?
- Type versus Kind
  - type is the type of term
  - kind is the type of types


class type
type is a metaclass that creates classes
the type of type is Metaclass aka kind?



  add(1,2,3)
  add(1) (2) (3)



- Not knowing the type of a parameter greatly limits the set
  of operations that can be performed on a term of that type.
  - Begin Speak: The more we know, the more wee can do safely








- Ints have multiple Monoids:
  - explain Integer Addition Monoid
  - Sum is Monoid
    - Hoist integer into o

One Monoid associatied with List built-inn


- What does mappend mean?
  - Monoid append
  - binary associative operator



      
- this is a secret math, that the goverment doesn't know about

Debates
=======
- Polyfill or Ponyfill
  - Is all code you write a Ponyfill
  - Dolphinfill
    - not smart
    - sex crazed bros of the seaworld
    - toxic
  - Frenchiefill
  - Crowfill

Confessions
===========

Python Interview
================

Quotes
======
strager: Abstract types drops you into the pit of success

- abstract algebra is talking about obvious things that seem
  self-evident, and making them really hard.
- Like  telling a computer how to do everything literally

Zach: Monoids are everywhere, and you are already using them

slashformotion: axiom is a theorem you consider true
                you don't  prove it

Zach: you build theorems with Axioms

Scraps
======

TODO
====
