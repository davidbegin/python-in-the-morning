Day 4
=====


Questions
=========
  * Whats the difference between a tuple a list? tuples are immutable
  * Why would I want to use a Tuple as a record?
      - The unpacking makes it easy! How??
  * What is the performance difference between Tuple and something with named fields?
  * What is GNU gettext?
	* Whats the performance difference in tuple and namedtuple
	* Why do we not want to be explict and name fields
	* Does tuple unpacking work in debugger?



Ponderings
==========
  * I want an example of iterable object, that we can't unpack
  * How do you swap variable names in all other lanuages
  * If we can't use `_`, then what should we use?
    Show me a PR where this caused a problem, 

Learnings
=========
  * Tuples can be used as records with no field names
  * The cool kids are saying iterable unpacking
  * If you write internationalized software, _ is not a good dummy variable because it is traditionally used as an alias to the gettext.gettext function, as recommended in the gettext module documentation. Otherwise, it’s a nice name for placeholder variable.



I need to explore
=================

```
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
```
