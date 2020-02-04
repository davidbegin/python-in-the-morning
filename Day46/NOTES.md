2020 - 2 - 4
============

Editor Options:
---
	√ Vim
	* Vscode
	* PyCharm

Stupac Advice
---
  * GNU Stow. Easy way to manage dot files (config files) and git-able.


mecermecer1 Personal Project
===

**Goal:** want to make a software where you can draw things on a map and it gets saved,
 so you can repopen it,
 update the map and have the drawing still there


### Questions for mecermecer1?
- What do you mean draw?
- what do you mean update the Map?
- What kind of maps are these?
- Where do you fetch these maps from?
- What type of programming is going to "Draw on these maps?"

### Examples:
 - draw Lines
 - write Stuff
 - mark stuff on the map
 - Get the latest Satelite images
 - Just to show somethign like a territory for example

### Homework:
- What are the libraries that people use for this type of Work
- What would be an MVP for this project, AKA minimum viable project,
  Whats 1 useful thing this program can do.
- What are individual steps that need to be figured out to reach the MVP
  - Fetch Maps from an API
  - Edit Maps
- You want a Github with all your work.

### You want to document the following (in Github):
  - assumptions
  - open questions
  - things you learned about


This is a way of superspeeding your learning when asking for help with others.

Before you can ask for help, you must get clarity on what you are asking.
What are you confused on





### Resources
- https://github.com/googlemaps/google-maps-services-python 
- https://github.com/mapbox/mapbox-sdk-py








TODO:
=====
	* Add RC commands for returning bashrc, vimrc, tmuxrc


Book Suggestions:
====
- Refactoring Legacy Systems - Michael Feathers
	- Explains how to get parts of the system under test and then change.

Goals
=====
- Learn more about asyncio
- Go Down Rabbit Holes - GDRH
- Have Fun
- Work on vim folding more

### Async Goals
- Couroutines, Tasks, EventLoop
- understand the evolution and current best practices of the syntax.
  - What is going to be deprecated


Questions
=========

L1 cache is further divided into two sections: L1 Data Cache and L1 Instruction Cache. The latter contains the instructions that need to be executed by the CPU while the former is used to hold data that will be written back to the main memory.

Question: What is the Difference in L1 versus L2 cache???
Answer: L1, L2 and L3 cache, in order of increasing size and decreasing speed. L3 cache is the largest and also the slowest

- Fact: L1 is faster than L2
- Fact: L1 is smaller than L2
- Fact: L1 and L2 are separate for each core.

What is L3?


To answer this question:
  - first we must discuss static RAM VS dynamic RAM (SRAM vs DRAM)

### Static RAM
- made of CMOS technology and transistors (six for every block)
- Why no capacitors??


### Dynamic RAM
- uses capacitors and transistors.
- needs to be constantly refreshed
	 (due to leaking charges) to retain data for longer periods.
  - Dynamic RAM Leaks???

Haze: capacitors have two functions in this context: to filter out interference (by sending it to ground) and to provide VERY temporary energy reservoirs if and when power surges (think of them storing energy and puking their guts out when power is suddenly not present)




What is eDRAM?
- you put the RAM inside the chip in question for eDRAM

What is BJT?
	-  bipolar junction transistor
What are Flip-Flops??

Viewer Questions
================

Learnings
=========

- CMOS - Complementary metal–oxide–semiconductor (CMOS), also known as complementary-symmetry metal–oxide–semiconductor (COS-MOS), is a type of MOSFET (metal–oxide–semiconductor field-effect transistor)



the original exception chained using the raise X from Y syntax introduced in PEP 3134 — Exception Chaining and Embedded Tracebacks.
```
raise FetchError(cc) from exc
```


Ponderings
==========

## Breaking down the need for async

Facts:
	- We need some IO
	- IO is slow (Ryan  Dahl would saying blocking)
	- There are 2 ways to prevent blocking calls from making your program suck
		- Run each blocking operation in a separate thread.
		- Turn every blocking operation into a nonblocking asynchronous call.

## Problems with Threads
	- Threads work fine, but the memory overhead for each OS thread—the kind that Python uses—is on the order of megabytes, depending on the OS.
	- Python uses OS threads

Begin reads the phrase "Ryan Dahl advocates callbacks for their simplicity and low overhead.", the first thing I think.

simplicity of implementation is not the same as simplicity of use
Ryan Dahl is advocating for Node.JS.


Finish the Phrase:
	I'm in Callback _____


Coutines avoid the dreaded “callback hell,”



Question: Is coroutine hell a thing?



There is a memory overhead for each suspended coroutine,
but it’s orders of magnitude smaller than the overhead for each thread.


We should be very grateful:
- event loop underlying our asynchronous applications can rely on
  infrastructure that uses interrupts, threads, polling, background processes,

There are hardware things???


Fact: Generators and asyncio coroutines - are different things.
Fact: Coroutines are implemented using generators,



What is the difference in a Mutex and Semaphore?



Is around some Data-protecting, against who can write to some resource
Our current use, is limiting the maximum


KieKAEMODAiwiECo: Semaphore with max count 1 would be similar to mutex

Mutex is a Semaphore, but not all Semaphores are Mutexs?
Muppet - Puppet principal???





`@asyncio.coroutine` and `yield from` can be replaced with `async def` and `await`

If you scheduling async tasks to run
and they have blocking in them,
but they throw an error,
we don't want to keep blocking

How do we interact with errors from coroutines or async calls??


### Desiging against an API or server
	- We should handle throttling, rate-limitnig, so we don't DDOS the server
	- Problem: You don't want to get bogged down, protecting against things,
		 when you don't even know how to do anything fun yet. At the same
		 when you're new you are more likely to DDOS a server by accident.
	- Begin Opinion: It's ok to accidently DDOS a couple servers, its ok to accidently
		 drop a database. I am more inclined to hire someone who has accidently
		 dropped a DB, or DDOS their own server, emailed all the customers in a test,
		 than someon who hasn't.



First we just code first
Then we start writing our tests first
Then we start writing our READMEs first
Then should we start just writing our Custom Errors first???




```









#### How do Threads work in ruby??
Ruby doesn't?????? Green threads versus some other thread?
Rubys own lighter weight version of threads

Opinions
========

Debates
=======
	* PyPi - Pie-Pie OR Pipee
	* Flupy - Flu-pie OR Floopy
	* aiohttp - A-Eye-O-HTTP OR ehh-O-HTTP

Phrases
===

...if we don’t make mistakes.

Confessions
===========
	- Im nervous what is choose the wrong OS???
	- What its really hard to set everything up again???


Begin's Internal Linux Debate
===
X Ubuntu
	- Not Cool!!!!
	- bloatware, spyware, not cool
	- also the most common
- Pop OS
	- cooler, but not as cool as others
	- might be as easy ubuntu
- Mangaro
	- new, shiny, flavor of Arch
	- maybe harder to setup?
- Arch
	- coolest
	- Fear: too much time
	- it will be harder, but I will become smarter,
    eventually, it will be the least work in the long run (after years)


### spartan linux debate
- solus


Begin Advertisment for Arch
===
- We are going to need to learn everythng that we need to know
  to setup Arch eventually


### How Begin Choose Vim:
	- I said its on every server
	- I will use it eventually
	- I probably would switch one day





Explain how RSpec syntax works

```ruby
it "works" do
	subject.equals(expected)
end
```










Python Interview
================

Quotes
======
	* Choosing a distro is a personal struggle, that only you can through that.

Scraps
======


New Band
===

### Von Neumann Bottleneck

We write surf rock, rockabilly, 50s Doo-Wop, early rock-n-roll,
All our lyrics are about obscure scientists
We will dress the part as well

Oliver Heaviside

### def and await

My Chemical Romance, but only about what ever the current most
popular supernatural young fiction is

## Other things to learn

https://en.wikipedia.org/wiki/Message_Passing_Interface

### Clickbait
- Avoding Coroutine Hell in your Python Code
- REPL without a cause

