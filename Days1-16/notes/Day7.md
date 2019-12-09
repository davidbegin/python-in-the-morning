Day 7
=====

Questions
---------
	* sort() or sorted() - The key optional keyword parameter can also be used with
 		the min() and max() built-ins and with
 		other functions from the standard library
 		(e.g., itertools.groupby() and heapq.nlargest()).

	* ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

	* bisect.bisect(HAYSTACK, 23, lo=2, hi=6), why does this return the
    "hi", if we can't find the desired value?
    I think I understand

Answered Questions
------------------

Learnings
---------
  * x.sort() modifies in-place, sorted(x) creates a new copy
    sorted takes in any sequence type, and returns a List
    sort() always is modifying itself, so it returns the same type
  * reverse() Desceding Order
	* bisect is actually an alias for bisect_right,
 		and there is a sister function called bisect_left.
 		bisect_right returns an insertion point after the existing item,
 		and bisect_left returns the position of the existing item,
 		so insertion would occur before it.
 		With simple types like int this makes no difference,
 		but if the sequence contains objects that are distinct yet
 		compare equal, then it may be relevant.
	* use bisect as a faster replacement for the index method
 		when searching through long ordered sequences of numbers.
	* If you are handling lists of numbers, arrays are the way to go.

Ponderings
----------




Goal
====
	* bisect_left or bisect in open source library
		bisect_left, 

Speed Tests
-----------
	* What is the speed difference in using biset versus index for
 		long ordered sequences
	* Speed difference in randrange and choice(range(start, stop, step))

