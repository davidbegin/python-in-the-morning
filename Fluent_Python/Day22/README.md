2018 - 12 - 17
==============

Questions
=========
  * When to use == versus id, compare identity versus values
    Note: Always use is for comparision to singletons
  * Which do you prefer?
    - b = list(a)
    - b = a[:]
    - list might be suprising it copies
    - list() could also be for consuming an iterable, or for converting a type,
    - Personal Begin Preference: `[:]`
  * are tuples less memory intensive and more secure since they are unmutable?
    Yes
    Because the length is fixed
    They are immutable
    and since they are, certain operations are faster.

  * How can I see Python, creating a new tuple for new

  * Whats DUP_TOP_TWO?
        BINARY_SUBSCR
        ROT_THREE
          Lifts second and third stack item one position up, moves top down to position three.
        STORE_SUBSCR

Learnings
=========
  * why you using id()? you probably want to use the `is` function.
  * Every object has an identity, a type and a value. An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. The is operator compares the identity of two objects; the id() function returns an integer representing its identity.
  * A surprising trait of tuples is revealed: they are immutable but their values may change.
  * For example, when talking about a seesaw object in a simulation, she would say: “Variable s is assigned to the seesaw,” but never “The seesaw is assigned to variable s.” With reference variables, it makes much more sense to say that the variable is assigned to an object, and not the other way around.

  Variable `_________` is Assigned to the `_________`.
  * √ - assign variable to object
    After all, the object is created before the assignment.
  * X - assign object to variable
  * The is operator is faster than ==, because it cannot be overloaded, so Python does not have to find and invoke special methods to evaluate it, and computing is as simple as comparing two integer IDs.
  * The easiest way to copy a list (or most built-in mutable collections) is to use the built-in constructor for the type itself. (Copies are shallow by default)
    - For lists and other mutable sequences, the shortcut new_list = old_list[:] also makes a copy.
  * += on a tuple creates a new tuple and rebinds the variable 


```
Person()
assign Person to p???
asssign p to Person
```

Ponderings
==========
  * If you already know something, can you get better at teaching it to others?
  * Am I right to be so fearful aliasing?


Detour
======
  * What does id() do in each of the Python implementation alternatives
  * Why are all the factors to where None ends up in Memory??

```
(Pdb) id(None)
4516302264
```

















