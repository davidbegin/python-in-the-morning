2018 - 12 - 20
==============

Quizboy
=======
  * What are some of the pitfalls of slots??
    - enforcing only attributes in the __slots__
    - Can't weak reference, unless it is in the __slots__
    - you must declare __slots__  on all subclass, doesn't work
      with inheritance

Questions
=========
  * Where is mem_test.py?????
"vector in polar coordinates: <r, θ>, where r is the magnitude and θ (theta) is the angle in radians. The rest of the format specifier (whatever comes before the 'p') will be used as before."

  * What does showing  a Euclidian vector in Polar coordinatates mean?
  * Polar Coordinations is a combination, magnitude and theta
  * The __hash__ special method documentation suggests using the bitwise XOR operator (^) to mix the hashes of the components, so that’s what we do.
    - What does any of this mean???

Learnings
=========
  * name mangling
    - What is name mangling???
      - If you give an class attribute a special name (dunder at the beginning, zero or 1 trailing _), python is going to store it with the Class name, prepended,
for namespacing purposes?
    - You need at least 2 `leading _'s and at most 1 trailing
  - A `__slots__` attribute inherited from a superclass has no effect. Python only takes into account __slots__ attributes defined in each class individually.
  * When __slots__ is specified in a class, its instances will not be allowed to have any other attributes apart from those named in __slots__. This is really a side effect, and not the reason why __slots__ exists. It’s considered bad form to use __slots__ just to prevent users of your class from creating new attributes in the instances if they want to. __slots__ should be used for optimization, not for programmer restraint.
  * To build Pythonic objects, observe how real Python objects behave.
      - Ancient Chinese proverb

Ponderings
==========
  * How do you implement a proper __hash__method
    - If the objects are equal, then the hashes should be the same
    - It has to take into account its object attributes
    - Maybe Answer: Hash each indivual attribute, and combine with XOR???

"Never, ever use two leading underscores. This is annoyingly private. If name clashes are a concern, use explicit name mangling instead (e.g., _MyThing_blahblah). This is essentially the same thing as double-underscore, only it’s transparent where double underscore obscures." - Ian Bicking

  * Do you prefer __ or _
    dunder Pros:
      - Python does name mangling for you?
    dunder Cons:
      - it can be suprising when something is name mangled?

    single Pros:
      - Uh Code Golf!!!! saving all those underscores
      - Be more explicit when using Name Mangling
    single Cons:
      - Implement our own Name Mangling convention!!!
