2020 - 1 - 27
=============

Python Interview Question
===
  * Is a Generator a Coroutine?
  * Whats the difference between a Generator and a Coroutine?
  * What is the difference between a thread and a coroutine in python?

Goals
=====
  * Understand the uses of Coroutines in Python
  * Understand some downsides to Coroutines in python
  * understand yield and yield from much better
  * Understand what the phrase preemptive multi-tasking is




Show I would Watch
===
  * The elder days of computer science

Python Interview Code Challenge:
===
	Print out a generator in the GEN_RUNNING "state"




Begin Is Confused:
===
  - I wasn't thinking of python starting "coroutines", I thought type of code
    we wrote, followed a coroutine pattern.
    If I actually understand what coroutines are, they aren't a concept,
    they are real.
  Spartan: coroutine is a construct of the python runtime not the OS
           unlike a thread. But in python we still operate on "threads",
           but the language python chooses how to interpote with system threads

  Coroutines are not an OS thing, but they do exist in Computer Science
  Threads are an OS thing, and also exist in Computer Science




Premptive Multi-Tasking:
  OS surrendering control of your CPU time

Ahead of Time
  Many things at once
  CPU, Ima figure how to call all these things

Versus Coroutines
  We don't know what we gonna do ahead of time,
  we are gonna pause, and yield execution to someone else???





Viewer  Advice:
===
	* HazeAnderson: find a cheap copy of this book: The Art Of Electronics ... under $20 .... keep it handy



View Understanding
=============
  * spartangtr: so, the wrinkle in this is the fact that python is interpreted and it's the python runtime doing stuff with your bytecode, so im guessing the secret sauce is in how the python runtime is scheduling your bytecode?

* sweeku: i still like this. generators are data producers. coroutines are data consumers.

* HazeAnderson: it's a framework for iterating thru existing or generated sets without loading them into memory, and can be threadable ... I think 🤔 <-- me thinking



Viewer Questions
================
	* Whats the language for programming micro-controllers?
		- Circuit Py?
		- Rust
		- C
		- Assembler
		- C++


How do you use a linter?
	Choose the files run the script


Simplest Way -> Lint Files as needed, manually

Next -> Make a Script to Lint all Files
	make script?

When do we want to run this formatting:
	- Pre-Commit have it run
		- Warn
		- Update for you
	- Have a CI action run Linting:
		- Warn/Fail versus Commit
		- Update and commit for you


When do run the Linting
	- Locally
	- Somewhere else Github Actions or any CI/CD pipeline (Travis)
How do commit the Linting
	- Do you manually ammend a commit
	- Do you have the CI commit a lint update commit for you


### Advice For Panda Person
- Make A Script to run to all your linting
- Choose one of the following
	- Others Choice:  Git Pre-Commit Hook
	- Begin's Choice: CI Action Hook to run that script on PRs
		- Github Actions
		- Travis CI


How do I steps or actions into my development cycle.

## Current Panada Person Flow
	* Write some code locally
	* Commit
	* Push to the Master
	* Repeat


## Proposed Strategy
	* Create a git branch
	* Write some code locally
	* Run Black
	* Commit
	* Push to the Branch
	* Merge the Branch
	* Checkout master and pull latest
	* Repeat

this give you opprotunity for you and others to code review before better into
master. Master should always be in a working state!
We gives ourselves a stage to perform automated actions with Travis, Github Actions,
Circle CI etc.


## New Linting Proposed Strategy
	* Create a git branch
	* Write some code locally
	* Commit
	* Push to the Branch
	* Github Actions Run Black
	* Merge the Branch
	* Checkout master and pull latest
	* Repeat


Black runs for all people, don't have to remember to run it
We aren't running it locally


CI -> Continous Integration

Problem:
	you wrote tests,
	no one runs them before commiting!!
	sounds like a computer problem to me
	When you open a PR to github/lab, run these tests,
  if they don't pass, don't let this merge this in.

Development Lifecycle, Release Management.




New Debate:
	* Should CI commit back to your code for you?


New Debate:
	* HazeAnderson: how about slow down and deliver more?
			What about move fast and breaks things






Questions
=========
  What does this mean:
    * "We find two main senses for the verb “to yield” in dictionaries: to produce or to give way."

  What is Coroutine?
    - Yielding is part of coroutines.
      - Well a coroutine, pauses execution in the program, and yields it to some other part of the program


  * Where did the word "datum" come from?

  * yield from versus yield

  * How does async work in python? yield based?

  * Is a generator not a coroutine???

Learnings
=========
  * Coroutines and Generators both have yield in the method
    - Coroutines yield usually appears on the right side of an expression (e.g., datum = yield)



"Regardless of the flow of data, yield is a control flow device that can be used to implement cooperative multitasking: each coroutine yields control to a central scheduler so that other coroutines can be activated."



each coroutine methods
```
def coroutine_1():
  dataum = yield

def coroutine_2():
  datum = yield

centeral_scheduler = Scheduler()
```


- Coroutine - "it is a subroutine that can be paused and resumed.
Benefit of Coroutines:
  - idea is to cut down on context switching which is an expensive operation in hardware
  - more predictable CPU cycle allocation?


There is a kind of Coroutine:

uses yield as a signal to the scheduler,
indicating that the coroutine will be waiting until an event (such as IO) is completed.


### Coroutines versus Generators Illumination

 it is relevant only to the kind of coroutine that uses yield as a signal to the scheduler, indicating that the coroutine will be waiting until an event (such as IO) is completed.





How can you use a generator as a coroutine in python?

Well first, does the generator function assign yield to something?
IF yes, proceed

Well, call next with None on it, to "prime" the coroutine,
then you can use `send()` and yield will be the data passed in.





```
4 States of Coroutine:
```
inspect.getgeneratorstate(…) function, which returns one of these strings:

'GEN_CREATED'
Waiting to start execution.

'GEN_RUNNING'
Currently being executed by the interpreter.

'GEN_SUSPENDED'
Currently suspended at a yield expression.

'GEN_CLOSED'
Execution has completed.
```










Ponderings
==========
  How do we explain Coroutines in both Computer Science and Python to someone
  who doesn't know either, but does use `yield`

	* Do we want people having to explicitly call next() for their coroutines? Or do we want to abstract away.

When would we want to delay creation of coroutine/generator object,
and initialization?



Fun Activities to Make the Program Fun
===
	* Act a little bit
			- pick a character
			- program in that character
			- async expert, doesn't care if his hands bleed,
				likes synthwave


Opinions
========
	* Begin Opinion:
			Caveat: If you want to get stuff done on scale
			Programming is a Team Sport.

Debates
=======
	* You are implementing a coroutine decorator as a library/framework creator,
		do you prime the coroutine for your users or not?o

		Or give an option not to Pre-prime off

		Pros of Pre-Priming:
			- People typically have to do less, and not think about priming
			- People's first experience with the library/framework is less
        ceremony at fist.
		Cons of Pre-Priming:


	* What Linter to use in Python!
		- PEP8
		- Black
				- Begin
				- Haze
				- Spartan


Python Interview
================

Scraps
======


Marketing
=========

We ain't just programmers
We trend setters

We see a hot new framework or language, library, or design pattern, or philoshopy,
you want to use it at work.

You are now in Marketing.

We believe that the changes proposed here will help keep Python relevant and competitive in a quickly growing area of asynchronous programming, as many other languages have adopted, or are planning to adopt, similar features


You want to convince your manager to get Terraform in the stack, you got
to sell it.



