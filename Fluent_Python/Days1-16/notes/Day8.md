Day 8
=====

year - Month - day
Endianess


Learnings
=========
	* if you need to store 10 million floating-point values, an array is much more efficient, because an array does not actually hold full-fledged float objects, but only the packed bytes representing their machine values—just like an array in the C language.

Questions
=========
	* What is the difference list.copy() versus copy.copy()
	* What is copy.deepcopy for ?
	* Why can't an array.array call s.__reversed__()
	* Why can't an array.array call s.sort()
		As of Python 3.4, the array type does not have an in-place sort method
 		like list.sort()

Ponderings
==========
	* What is an open source usage of byteswap?

Speed Tests
===========
	* What is the speed difference in creating Large Arrays versus List?
	* lookups in Lists versus Lookups in Sets?
		Is it faster to convert a list to set before lookup? NO!!!!!
    OR just look up in the list. YESSSS
