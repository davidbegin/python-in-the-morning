2020 - 1 - 30
=============


Programmer Trivia Questions:
===
	* Name all 5 Smalltalk Keyboards:
	*


Goals
=====
  * Learn some things
  * Have Fun
  * Figure out more details of building a new comp
    - https://pcpartpicker.com/list/g7xTzN

Viewer Questions
================

Questions
=========
  * When would you use process-based versus thread based concurenncy
		- Depends on if you are I/O Bound or CPI Bound
		- I/O Bound
			- use ThreadPoolExecutor, and you will ahve to experiemtn
        with the number of workers it needs based on available memory
		- CPU Bound
				- ProcessPoolExecutor
				- you dont need a limi of works
					- it makes more sense to have more workers than CPUs
    - ProcessPoolExecutor for the flags download example or any I/O-bound job.
    - ThreadPoolExecutor.__init__ requires a max_workers 



Do we always need to call enumerate on these objects
		- <generator object Executor.map.<locals>.result_iterator at 0x10a9306d0>,

to force _result to be called


Speed Tests
===========
20 Workers all flags
real    0m11.442s
user    0m3.933s
sys     0m0.980s

194 Workers all Flags
We are done, you don't a need a length

real    0m9.041s
user    0m3.951s
sys     0m1.171s


100 Workers
real    0m9.043s
user    0m3.863s
sys     0m1.117s

50 Workers
real    0m10.510s
user    0m3.810s
sys     0m1.029s


Learnings
=========
	* If you are doing CPU-intensive work in Python, you should try PyPy.

Ponderings
==========
	* Which do you use?
		- concurrent.futures.Future and asyncio.Future
		- are you already importing asycio on concurrent
    - should we think about package size of each.
    - different in the .result()
      - concurrency.futures.Future .result() will block the caller’s thread
        until the result is ready. 
      - asycio.Thread - we should use yield from
      - 



	* There are some things that are holy wars
		- Keyboards
	  - git
		- Editors
		- tabs versus whitespace


	When you see a thread basher ask
		- Are you a systems or applications programmer?

Quotes
======


Elk Cloner: The program with a personality
It will get on all your disks
It will infiltrate your chips
Yes, it's Cloner!

It will stick to you like glue
It will modify RAM too
Send in the Cloner!

	- Elk Cloner Poem

Opinions
========
  * Write your poem alongside your virsus, don't write the virsus


Next Book Options:
===
	* Machine Learning in Python
	* Python Machine Learning by Sebastian Raschke 


Debates
=======

Python Interview
================

Scraps
======

New Comp
========
  * New Keyboard suggestion
    - Open for suggestions
  * Motherboard suggestion
  * 7200 versus 5400 RPM for a harddrive
    - Sketchy Scripts said I only need 5400
    - stupac 7200
    - videos youtube, and now im confused.

7200 RPM increases the file transfer speed

things to consider about HDD RPM:
	- where the data is locoated on the platter can affect look up
	- What is setup, do you have two and on in Raid 0


What brand
What line of their brand
WD
	- Blue
	- Black
	- Red

 https://www.seagate.com/in/en/internal-hard-drives/hdd/barracuda/

Keyboard suggestions:
	PandaPerson: https://www.razer.com/gaming-keyboards-keypads/razer-huntsman
	Stupac: https://zealpc.net/products/zilents

linear or tactile for streaming
linear means you cannot feel the actuation point (when key registers on screen).
Tactile means you will feel some pressure then the pressure releases when key is registered
I honestly think the tactility is useful for better typing. Fewer errors because you know if the key registered without looking at the screen because you can feel it register (tactile)

Whats the most obnoxious version of this




Confessions:
============
	* I don't know how to play Go
	* I don't know how to program Go
	* I don't know what all the Raid 0, Raid 1
	* I don't know about Grammer,
			fewer == tangible
			less  == intangible
			less upset
			fewer keyboards


Problem
=======
	* I want to get into mechnical keyboards,
		theres too much info
		too many opinions
		too many updates coming at you

	* How do I know what I want???

	* 6 Weeks Program
		- 6 sets of switches
		- some keyboards
		- heres a roadmap of ways to try, what it should feel like,
			and then some questions to prompt your experience

https://kbdfans.com/collections/switches-tester/products/zealpc-switches-tester
https://kbdfans.com/collections/switches-tester/products/kailh-box-14-switches-tester





TODO:
=====
	* Watch this http://www.skrenta.com/2007/08/spooky_elk_cloner_movie.html
  * Upgrade Python anyway
  * figure out "{x=}"
  * Terminal Cube Timer
  * Get a cube with no green
  * Or an all Green Cube





Missing Flags
====
{'PM', 'NC', 'MS', 'BV', 'VG', 'WF', 'TF', 'DO', 'MP', 'PN', 'NF', 'SJ', 'GF', 'CX', 'BM', 'RE', 'MO', 'HK', 'PR', 'NU', 'EH', 'GP', 'HM', 'SH', 'IO', 'AW', 'MQ', 'FK', 'GL', 'YT', 'AS', 'TC', 'FO', 'PF', 'VI', 'CC', 'UM', 'CK', 'CS', 'PS', 'AQ', 'TK', 'KY', 'GI', 'AI', 'GU', 'AN', 'GS'}
