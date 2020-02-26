Notes
=====


Python
======
  * complex can be used to 2D vectors
	* The string returned by __repr__ should be unambiguous and,
 		if possible, match the source code necessary to re-create
 		the object being represented.
	* __str__ should return a string suitable for display to end users.
	* If you only implement one of these special methods,
 		choose __repr__, because when no custom __str__ is available,
 		Python will call __repr__ as a fallback.




	List = [str, int, bool, person]
	__str__(List)
	__repr__(str)




This means, in simple terms: almost every object you implement should have a functional __repr__ that’s usable for understanding the object. Implementing __str__ is optional: do that if you need a “pretty print” functionality (for example, used by a report generator).


Question
========
  * What really are Euclidean vectors
    - Versus other vectors??

	* How do you calculate the magnitude of a Vector?
		Also called: Euclidean norm (or Euclidean length)
	* violates the commutative property of multiplication.
	* <Vector object at 0x10e100070> <= What is the hex number thang
	* What is the code python path difference for calling abs versus __abs__ within a class you redefine __abs__



Problem
=======
	* What version of python am I running in Vim!



Notes:
======
	* abs built-in function returns the absolute value of integers and floats, and the magnitude of complex numbers
