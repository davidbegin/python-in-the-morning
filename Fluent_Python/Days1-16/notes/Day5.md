NOTES
=====


Questions
=========
	* How do I see the inheritance hiericarhy for a given object
	* Why can't we convert a reversed object to a list (and why can we to a tuple!)
	* Why does reversed return two different objects
		- Lists are Mutable
		- Tuples are immutable
	* What does shallow copy mean?
	* What does __rmul__?
	* What is the most pythonista way to split List in 2 on a index


Learnings
=========
	* tuple lacks the __reversed__ method. However, that is just for optimization;
 		reversed(my_tuple) works without it.

	* .__getnewargs__()
		Support for optimized serialization with pickle
	* The pickle module implements binary protocols for serializing and
 		de-serializing a Python object structure. 
	* It is possible to construct malicious pickle data which will execute arbitrary
 		code during unpickling. Never unpickle data that could have come from an
 		untrusted source, or that could have been tampered with.


Ponderings
==========

1..2

range(0, 4)
a)		2 ≤ i < 13
b)		1 < i ≤ 12
c)		2 ≤ i ≤ 12
d)		1 < i < 13


s[::-1]
'elcycib'




