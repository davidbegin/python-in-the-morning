# 2020 - 2 - 25

Resources
=========
- https://www.wikiwand.com/en/Masatoshi_G%C2%BCnd%C3%BCz_Ikeda
- https://www.wikiwand.com/en/Depth-first_search
- https://www.wikiwand.com/en/Breadth-first_search
- https://www.wikiwand.com/en/Best_worst_and_average_case
- https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
- https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/
- https://wiki.python.org/moin/TimeComplexity

Bounties
========

What are resources other than time and memory, do we measure BigO for?
Is Big-O a type Probabilistic analysis of algorithm?

Find me someone who has got paid for heapsort



Viewer Questions
================

Questions
=========

Learnings
=========


Ponderings
==========

BigO is lot about gambling

Best Case
Worse Case
Average Case

Time Complexity = How long = Time == Money


As Computer Scientist, we are particularlly conercerned about the worse case.
It's our job to know about it and have a plan.




The Big O starts with an O and everything in the () is there to
represdetn teh relationshipo between input and the steps our algorithm takes.

When the input gets bigger, whatchu gonna do



O(n) == We love this == we love linear, its a simple relationship

Constant	O(c)
Linear	O(n)
Quadratic	O(n^2)
Cubic	O(n^3)
Exponential	O(2^n)
Logarithmic	O(log(n))
Log Linear	O(nlog(n))


Whats the difference between Lograthmic and Log Linear?


O(n · n!)

The reason why this is factorial, is if it is determistic bogo, we are going through
every variation.


lancemaker: are you using python ? oh man one cool thing to do would through the most known big O examples as code and plot the results of multiple searches.o


In mathematics, the logarithm is the inverse function to exponentiation.



inverse function, reverses the value back to it's original form

b^n inversed log n

log base 2 of n to 2^n

Log N

stupac62: I think it's implied that log(n) is log base 2 of n



stupac62: "In addition to fade2black's answer (which is completely correct), it's worth noting that the notation "log(n)" is ambiguous. The base isn't actually specified, and the default base changes based on context. In pure mathematics, the base is almost always assumed to be e (unless specified), while in certain engineering contexts it might be 10. In computer science, base 2 is so ubiquitous that log is frequently assumed to be base 2."

https://cs.stackexchange.com/a/78131




Log Base Gangs
==============

CS - Log 2
Everyone - Log 10
Math Nerds - Log E
  - Actuary
  - Biology
  - econonmy




n log n == quasilinear


heapsort
timsort
mergesort
radixsort
radixsort



lancemaker: one thing to notice is that some algos are heavy on the memory and light on the processing .









Let's take a concrete example of this, mergesort. For n input elements: On the very last iteration of our sort, we have two halves of the input, each half size n/2, and each half is sorted. All we have to do is merge them together, which takes n operations. On the next-to-last iteration, we have twice as many pieces (4) each of size n/4. For each of our two pairs of size n/4, we merge the pair together, which takes n/2 operations for a pair (one for each element in the pair, just like before), i.e. n operations for the two pairs.


From here, we can extrapolate that every level of our mergesort takes n operations to merge. The big-O complexity is therefore n times the number of levels. On the last level, the size of the chunks we're merging is n/2. Before that, it's n/4, before that n/8, etc. all the way to size 1. How many times must you divide n by 2 to get 1? log(n). So we have log(n) levels. Therefore, our total runtime is O(n (work per level) * log(n) (number of levels)), n work log(n) times.


Is logN always a binary search?

lancemaker: nLogn is bigger than linear.








Opinions
========

If you don't experience for a first programming job, find someone, without
experience with programming.


Begin Opinion: just venv for now




Debates
=======
- Editor doesn't really matter
- But its also home, and fun to make nice

Vim can do everything, you might need to hook up some things up yourself


Confessions
===========

Python Interview
================


Best interview of my life
-------------------------
- sat me down with a failing test suite and some bugs in an application
- fix the tests, solve thne bugs
- paired, I used the tools I use typical


- Pair with peers
- Pair with Juniors
- Pair Seniors

Opinion, its good to pair with people who have totally different workflows
so its hard for you to over

Begin Opinion:
- Sometimes pair programming is the most fun way to code



Pair Programmming
=================
- one person types
- other is reading along
and then discussing
and you have 2nd set of eyes

Pairing Test Game
-----------------
- One person writes the tests
- Other makes it pass in the most simple (evil) possible






ShiraZull
---------
Just a fun thought I've been thinking for a while (this is more philosophical and haven't read it anywhere)... In every base, can't divide elegantly, as I would call it, except for binary. 

If we take base 10 as example, if you want to write one half, you either write 0,5 or 1/2, but in binary you write 0,1 or 1/10 (which is much easier) 3/8 is 0,375, in binary its 11/1000 or 0,011. Of course binary is mostly used as bits and you can't have anything between bits of information. But it's a fun thought :) (this got super long, but i wanted to share)

Quotes
======

Scraps
======

TODO
====
- https://www.youtube.com/watch?v=duvZ-2UK0fc
- !topic or !agenda
- vifm image previews


Types of Dramatic Readings
