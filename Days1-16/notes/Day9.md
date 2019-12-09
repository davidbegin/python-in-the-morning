Day 9
=====


Questions
=========
  * Why Was PIL forked for Pillow?
  * Why the naming? `memv_oct = memv.cast('B')`
  * Whats up with .npy Filetype?
  * numpy.load('floats-10M.npy', 'r+')
    Is this a memory-mapped array? Is it numpy.load(), r+  ?
    Is .npy only for numpy saved info?


Learnings
=========
  * Assign value 4 to byte offset 5.
    * memv_oct[5] = 4
    - The 5 here is more specific just the 5th Element
      Since Memoryviews can only be created from other sequences
      that store their information in memory (not reference),
      it is always the byte offset

  * If you are popping and appending to list, thats cool
    If you shifting the left most value. sounds like you
    want a double ended queue
  * It is also the way to go if you need to keep a list of “last seen items” or something like that, because a deque can be bounded—i.e., created with a maximum length—and then, when it is full, it discards items from the opposite end when you append new ones.
  * Note that extendleft(iter) works by appending each successive item of the iter argument to the left of the deque, therefore the final position of the items is reversed.
    - >>> dq.extendleft([10, 20, 30, 40])  5
			>>> dq
			deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)
	* The append and popleft operations are atomic, so deque is safe to use as a FIFO queue in multithreaded applications without the need for using locks.
	* There is no __contains__ method for a dequeue


Ponderings
==========
  * How long does it take to load numpy?
	* How long is appending to the middle of list versus a deque?
	* Is remove() ineffifenct for deqeues, versus a list
	* I want to see a heapq used in Open Source


How to Learn
============
  * You need a project that has stakes
    - Friend might use it
    - Write a blogpost about it
    - Use it for your job

  * Ending Point, what's MVP - Minimum Viable Product.
    Once I have these features, then I'm done with V1.









