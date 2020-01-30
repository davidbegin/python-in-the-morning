2020 - 1 - 29
=============


### rune_trimmed
```
Goal: The project I was wanting to do was make a file of all the songs in my "liked" playlist on spotify.

Then take each song and send songrequests on twitch streams
```

Sub-Goals:
  * Interact with Spotify API to get list of liked songs
    - Skills: Interacting with APIs, Auth
  * Save the list of songs somewhere (file, or maybe a database)
  * Create a Twitch Chat Bot to send song requests
    - Coding a Chatbot

### rune_trimmed notes:
	* is it a Webscaper
	* what are the .idea files for? editor files right?
		- can we add them to a .gitignore
	* Needs a README

Open Questions
===
	* Does spotify have an API?
		- Yes!
	* Is the spotify free to use?


We do need to scrap in life
and its pretty intereting as first
interacting with an API is much more userful



API Versus Scraping:

API
	- Once I have a JSON Reponse, I can throw it in a test
	- You gonna learn about rate limiting

Scraping
	- Much slower test/development cycle
	- Fragile, dependent on UI




What are the install requirements?
===
	* chromedriver


### Resources
- https://developer.spotify.com/documentation/web-api/
- https://spotipy.readthedocs.io/en/latest/
- https://github.com/tscheer100/SpotifyWebscraper








Dreams:
======
  * Notes to act as Docs, to act as Slides
    - Deckset
    - Git Pitch
    -> Turns MD into a Slide Deck


Iterator
	-> When you have a sequence and you want to operate on items
Decorator
	-> Its in the name
	-> wrap functions, with extra functionality
Generator
	-> Generate Values
Context Manager
	-> Allows you to change the bread of function
Coroutines
	->  Accumlators
	-> Coordination of Events



Python Interview Question
===
  * Is a Generator a Coroutine in python?  Why?
		Yes it is an actual Generator Object
  * Whats the difference between a Generator and a Coroutine?
			The use case???
    	And whats the different use cases

			A generator is essentially a cut down (asymmetric) coroutine. The difference between a coroutine and generator is that a coroutine can accept arguments after it's been initially called, whereas a generator can't.


asymmetric coroutine == generator

  * What is the difference between a thread and a coroutine in python?

### Generators: def functions that contain one or more yield expressions.

### Generator-based coroutine: A generator (def + yield) that is wrapped by types.coroutine. You need to wrap it in types.coroutine if you need it to be considered a coroutine object.

### Asynchronous Generator: async def functions that contain a one or more yield expressions. These can also contain await expressions.

### Coroutine: async def without zero or more awaits and no yields.
### Coroutine: async def with no yields, and can contain awaits


Is this a bad sentence, or I am dumb?



Goals
=====
  * Understand the uses of Coroutines in Python
  * Understand some downsides to Coroutines in python
  * understand `yield` and `yield from` much better
  * Understand what the phrase preemptive multi-tasking


Advice
======
  * Learn your ASCII Escape characters

TODO:
=====
  * Add Solve the Rubix Cube to BeginBux™ Chanel points
  * Upload All the old to You Videos to Youtube


Viewer Questions
================
  - Learn about virtualenv's and VS Code's use of them.


  - How can I import a module with pip in VS Code

    Questions I would Ask:
      - How does VS Code handle your python environment?
        You have a shell inside of VS Code

      Have you learned about Virtual Environments
        - Without a virtualenv you install everything global
          and that creates a mess
          might seem convinent, but its a dangerous road to go down.

        - Isolated Space, to install all your pacakages just for your project.
        -   How does VS Code handle virtual environments??

        - Why is the bash inside VS code using python 2?
          - How does your typical bash know to use python 3





IS the Lord of the Rings available in a single .txt online



who is sweaty
---
Balmer??
Werner???


Questions
=========
	* Are subgenerators only used within the context of Coroutines in Python???
	* Lexing versus Parsing
		- Separated out text
		- Lexing converting Text to Tokens that means something in a language

Learnings
=========
	* A generator is essentially a cut down (asymmetric) coroutine. The difference between a coroutine and generator is that a coroutine can accept arguments after it's been initially called, whereas a generator can't.

Art Matt Project
================
	* I want a tiny Usher Twitch Bot. written in Circuit py

Computer Concerns
=================
	Liquid Cooler:
		- maintence problem
			- how often?? 6-8 Months
				- What if I don't??
				- can I can I get a computer pool guy??
			- How hard is it to change liquid cooling??
			- like fish tank
		- is installation harder??

- Rhyzen 7 and Fans
	7 3800x



Ponderings
==========

Opinions
========
  What is Refactoring:
    Improving the underlying code implementation, without changing the outcome

  Types of Refactoring:
    - Refactor to Improve == Optimizing


	Stupac62 - Pop OS is basically Ubuntu but better
		What does better mean???

https://qtile.org/ for window manager written in python

2 Pop Dealers: Stupac Funky Jamma

Begin and PandaPerson we are ready to be sold

Will there be stuff I cna't install on Pop OS, I could on Ubuntu,
is this more work???
and if its more work, should I just use Mangaro


Debates
=======

Python Interview
================

Scraps
======

This is coool:
g  I saw a guy coding 2 coroutines communicating with each other. e he created a cat and mouse game where he had the cat go toward (send) the mouse pos and the mouse away from the cat position

```
https://www.youtube.com/watch?v=Ut0-_eMVakU
```

PC Part Picker Conspiracy
=========================
  Theory: If you build a computer on PC Part Picker, it always tries to
          make sure to buy one item from each store.
          AKA: You build a whole computer, it will all be Amazon,
               then a single best buy, newegg, b&H.

  Can someone show me a recommendation all Amazon..


https://pcpartpicker.com/list/g7xTzN



Math Detour
===========

### Exponential distribution.
```
random.expovariate(lambd)
```

lambd is 1.0 divided by the desired mean.


It should be nonzero.



Returned values range from 0 to positive infinity if lambd is positive,
and from negative infinity to 0 if lambd is negative.

What does this mean? Poisson Process events.




## Confessions

I am scared if I switch Arch, how long it will take me to
transisiton back into a full stream on Arch

Should I hop to PopOS first, transistion, then do Arch
on the side on another computer, working out the details.

- Audio Setup
- OBS Setup
- Programming











