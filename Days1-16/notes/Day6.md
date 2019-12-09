Day 6
=====

Questions
=========

Answered Questions
=========
  * How do we know if we got a new object in Python.
    Like in the case of concating sequences, how can we prove
    the new sequence is a new object.
    A: id()


Learnings
=========
  * augmented assignment operators `+= and *=`
  * When the target of the assignment is a slice,
    the right side must be an iterable object,
    even if it has just one item.
    - the Left side assigment is a Slice,
      then the right needs the same number of slices
  * Beware of expressions like a * n when a is a sequence containing mutable items because the result may surprise you.
 For example, trying to initialize a list of lists as my_list = [[]] * 3 will result in a list with three references to the same inner list, which is probably not what you want.
  * The identity of the object bound to a may or may not change, depending on the availability of __iadd__.
  * Repeated concatenation of immutable sequences is inefficient, because instead of just appending new items, the interpreter has to copy the whole target sequence to create a new one with the new items concatenated.
  * Putting mutable items in tuples is not a good idea.
  * Augmented assignment is not an atomic operation—we just saw it throwing an exception after doing part of its job.
  * The list.sort method sorts a list in place—that is, without making a copy. It returns None to remind us that it changes the target object, and does not create a new list. This is an important Python API convention: functions or methods that change an object in place should return None to make it clear to the caller that the object itself was changed, and no new object was created. 



Ponderings
==========
