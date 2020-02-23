2020 - 1 - 1
============

Quotes
======
	* Useful information makes us money, Useless information connects us
		- David Begin
  * The difference in a Senior and a Junior Programming, is the ability
    to know when to go down a Rabbit Hole
      - David Begin


Questions
=========
	* What is Cosine Similiarity?

Learnings
=========
	* Who invented the term Duck Typing? (Alex Martelli???)
		- James Whitcomb Riley
			- This dude wrote Annie!!!!
			- Did you know the inventor of the term duck typing, wrote Annie??
				Was Daddy Warbucks??

  * Don't ask a Skateboarding if they are a Skateboarding, asking them to do a Kickflip
	* What is the Vector Space Model?
		-  or term vector model is an algebraic model for representing text documents (and any objects, in general)
 			as vectors of identifiers, such as, for example, index terms.
	* but the best practice for a sequence constructor is to take the data as an iterable argument in the constructor, like all built-in sequence types do.


	* When you are building a Custome Sequence Class, you must think
		about __repr__ when the sequence is long.
		Use the reprlib module to produce limited-length representations


	* When you create a sequence from a sequence, you are copying
    the values


	* If you contstructors are different, you might not want a subclass
	* In the context of object-oriented programming, a protocol is an informal interface, defined only in documentation and not in code. 



Thoughts on Procedural Programming
	* What are some Procedural
    - Fortron
    - Cobol

C
You can write object orietned C?
You can write functional C?

# Do This
# than this
# this return this

Whats your definition of Object Oriented?

One Way:
  - Inheritence
  - Encapsulation
  - Polymorphism

Other:
  - Work is done, by objects sending messages to each other
    - More close to Smalltalk definition


Was the language made to be OO
Or can it be used OO


Rust Versus C++ Memory Safety
Both can be programmed Memory Safe, C++ you got do it yourself



Personal Opinion
===============
  * If you wanna learn a low level language Rust is the way to go.

1 year of Rust == 4 years of C

C or C++, I think you should be learning Rust.

Are you doing super performant,
Small code to fit on small hardware


Could you do OO Code in Brainfuck?






Rabbit Holes
============







Ponderings
==========
	* Because of its role in debugging, calling repr() on an object should never raise an exception. If something goes wrong inside your implementation of __repr__, you must deal with the issue and do your best to produce some serviceable output that gives the user a chance of identifying the target object.

	Should I always have a try catch in my repr???
	How can I ensure, that something is always returned???



__getitem__


Which do you prefer:
	* index - Old Begin
	* i     - Dumb People
	* elem
	* element - Iacchus, Begin
	* position
	* pos


Which Way:
	* Always use the same argument name √
	* Or dependent on the context




Things to Look at Later
=======================
	* The PyPI package gensim, by Radim Rehurek, implements vector space modeling for natural language processing and information retrieval, using NumPy and SciPy.



n-dimensional vectors (with large values of n) are widely used in information retrieval,
where documents and text queries are represented as vectors, with one dimension per word. This is called the Vector space model. In this model, a key relevance metric is the cosine similarity (i.e., the cosine of the angle between a query vector and a document vector). As the angle decreases, the cosine approaches the maximum value of 1, and so does the relevance of the document to the query.
