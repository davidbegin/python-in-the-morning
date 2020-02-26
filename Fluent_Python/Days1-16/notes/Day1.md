NOTES
=====

Debugger questions
===
  * Why don't a key error in the debugger?


Python Question
--------
  * Get __getitem__, I know we get the `Dict[key]` syntax, but what else??
  * Where does reversed, sorted come from?
  * How do benchmark python???


Pythonista Questions
====
  * Is it more pythonista to do?
    x = {"hearts": 1}
    # OR
    x = dict(hearts=1)

  * when should you use named tuples????
    - When you need a class with attributes, but no custom methods?
    - Pure Data class?
    - like a database record
    - Can I update the __repr__ of a named tuple?

  * Why would we use a "local", versus a constant in a Class?
    What is the difference to Python



Learnings
=========
	* You should write more special, or dunder, or magic than you use
		Python will use them for you!!
	* Don't create fake dunders, because what if the Python interpertor

  * Iteration is often implicit. If a collection has no __contains__ method, the in operator does a sequential scan

	* But for built-in types like list, str, bytearray, and so on, the interpreter takes a shortcut: the CPython implementation of len() actually returns the value of the ob_size field in the PyVarObject C struct that represents any variable-sized built-in object in memory. This is much faster than calling a method.

	Built in Types dunder methods have CPython optimizations




if __len__ of __getitem__ was called on list, str, bytearray

For len, me Cpython is going ot just just return ob_size

Is it a variable-sized built-in object in memory?




