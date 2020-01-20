2020 - 1 - 20
=============



HTML AUTO Python
================
	* All Markdown files should have all caps names
		- README.md
		- CONTRIBUTING.md


	* Are there no dependenciess???
	* What should we use for formatting
		- Flake8
		- Black

	* Why don't all the tests run in once collection


File Naming:
	* Whats with the numbering for the tests
	* I hate -'s in file names


Why unittest versus pytest???



Avoid variable shadowing
Avoid all keywords, as variable:
	- hex
	- array
	- list
Avoid saying array when you mean python list



TDD Philoshopy:
	* Red it fails
		- Why does it matter to see a red failure?
			We need to prove that our test is not going to a false positive
	* Green it works
	* Green again after I refactor


How could this apply to a curcuit

Do you have actual tests?

What is a test??
	- Way of checking if partial functionality works under some constraits



















Twitch User Twitch
===
  * https://github.com/jeffa/HTML-Auto-python


list(map((lambda a: a[0]), thingy))
the question what should thingy be named

sort this thing by the 1st element in each inner list and return a list that contains the 2nd elements from each inner list (sorted by 1st)

array = [ [2,'apple'], [4,'banana'], [5,'candy'], [1,'zebra'] ]


* don't capitalize python file names
* underscores for python files is not a convention
* make sure to add pycache and other files you don't want to you .gitignore
* directly import your other classes or mixins ala: `from file import module`
* dependencies go in a specific order:
  - Standard Library
  - Third Party
  - First Party

Example:
```
import json

import django

from our_code import some_cool_stuff
```


Why does this matter:
  * Saying which method to use potentially
    - And this market, we say our code, open source code, standard library








Gitignore
---
https://gitignore.io/




Opinions
=======

Steps to Embracing Python:
	- Stop saying Array, say List
		unless you are explicitly talking about a python array
	- Drop postfix conditionals when working in Python
		- I've heard pythonistas say they are confusing or not explicit



Begin Bucks the Python Community:
	- I like lining things up! It makes it easier to read!
Stupac fights back
	- Assume whitespace means comment


I have no compelling reason to swtich to Iterm2 versus Terminal


Never don't run unit tests, when something fails.
Unit tests should be fast, if they aren't, are they unit tests??



I HATE I HATE A HATE PRE COMMIT HOOKS
	- Within Github or Gitlab run those things.
	- You always end up using `-n, --no-verify`
	- If you want developrs to not commit
    untested or formatter code, then have the CI Pipeline
    do that. Github Actions.







TODO:
=====
  * https://github.com/rjsnh1522/py-class-in-multi-files

Goals
=====
  * Convert to UTC
    - Say all dates in UTC
    - ZST
      - The day moves based on when the sunsets

Tip:
====
  * isort can order you dependenices for you

Questions
=========
  * How does inspect.ismethod work???
      - What are checking to know??
      - The python interprator


	* export PYTHONPATH=.:../HTML-Auto-python/


Learnings
=========

  * Multiple Inheritance, or Inheritance in general, should be used sparingly
    - People from certain languages are have deep PTSD around multiple inheritance.

  * in refactoring, you constantly reference the rule of 3:
    - you see 3 of something, time for a refactor
    - you see 2, just hold off, things will change once get once 3

	* What is the difference:
		- virtualenv venv
			- This is some third party implementation
		- python -m venv venv
			- This is the real deal
			- this is all built in python?? Don't need virtualenv installed???

Quotes
======
  * Remember when you are excited about a new language feature to you, it might
    have already scared someone else.
  * It is super useful to do useless things, just don't do them for a company, or to
    be the defacto open source solution.
  * I just add things to .gitignore as git complains about them
        - Haze

Ponderings
==========

  * Private in Python is not truly private

    If I think something is private:
      - I mean the class itself, is the only one who will use the method,
        this is inner-workings of the method.
      - If I have to check the system if every method is being used by someone else,
        that is gonna majorly slow me down.


	* transpileception
		- The type of code programmers write in one language when coming from another
		- 	"They write Rubyesque-Python, Haskelly-Typescript"



Opinions:
========

The one true way to create a virtual environment:

Virtual Env Ritual:
`python -m venv venv`



Pythonista Debates
====


### Debate 1
```
# Option 1
meth_name = meth[0]

# Option 2
meth_name, _ = meth
```

Option 1
	- meth can be any iterable thang
	- it does one thing, grabs the first element, pretty explicit
	- Con: obscures what meth is

Option 2:
	- implies a 2 length tuple
	- faster
	- Maybe: _ hey what did you throw away




### Debate 2

unittest or pytest by default?

Pytest
	Pros:
		- what you will use at a company
		- You are practicing what you will use to make money
		- Most open source is pytest
	Cons:
		- its a dependency with dependencies!!

Unitest
	Pros:
		- no dependency!
	Cons:




What about Hypothesis
	- Type of Testing, generating results
	- Should be typing, with MyPy
	- have to careful about how much test data to generate

Additional testing, never replace unit testing, integration, acceptance testing





Smoke Testing Definitions:
	- Does it turn on not blow up, real basic functionality
	- Does it do a large bredth of simple tasks without blowing, the "Basics"
	- Does it start "smoking" when the system is pushed
		Does it blow up under real use?








## Debate 3


Test Setup Preference:
	* Single Unit Tests
		- the method name, gives the description of the tests
		- Its annoying making fake method names with descriptions
			- Counter example: Rspec it "testing nil values get a default"
				versus `nil_values_get_a_default~
	* One Unit Tests many examples
	* Single Until Pytest.fixtures?



You have a group of checking lower()
	- If one fails you stop testing the others

If you let all run, you know the exact case where lower is working or failing



What Context are tests running in:
	- A CI/CD Pipeline
	- Locally as we develop
		- We show we all the detail failures in the code I'm working on
		- Don't run Acceptance Tests and slow tests



Debates #4
---
	* Scope tests in a class

In a Class
	Pros:
	Cons:

Raw Methods:
	Pros:
		- See in the wild
	Cons:





Fixture might mean different things to different people

	- Iterm
		- A daily helpful tip
	- Terminal
		- It's on every Mac
Switch from Bash to ZSH or Fish







Start with 


The unicode Consortium has aggreed on these things:

&dagger;      -> HTML Entity
†             -> Printed Version
chr(8224)     -> Decimal Version
2020          -> Hex Version



Bytes Version -> b'\xe2\x80\xa0'
























