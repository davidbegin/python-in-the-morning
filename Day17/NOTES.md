2019 - 12 - 9
=============

TODO:
	* DUCK DUCK GO
	* FIREFOX


Questions
=========
	* Is there another way of requiring keyword args, without the * before
    the args???
	* What are the 5 Kinds of arguments for Parameter from Signature?
	* Are there any Standard Library tools as of 3.9 that use annotations
	* why operator.countOf why why why????
	* I want a example augmented assignment operator used from operator

```
def f(a, *b, c, **attrs):
	pass
```


Learnings
=========
	* I should be using attrgetter and itemgetter everywhere!!!

	* Annotations are for us! Not the Python interperator
		Could be used for frameworks or decorators!

* Everything after the * is now a required keyword arg
if you have a variable with `*var_name` then it will suck
all the variables before the keyword args into a Tuple.
You can also leave a blank `*` to go from postional to keyword
args
```
def f(a, *, b):
	return a, b

# Valid
print(f(1, b=2))

# Invalid
print(f(1, 2))
```

* This gives you the arguments of a function
 `clip.__code__.co_varnames[:clip.__code__.co_argcount]`

* POSITIONAL_ONLY
A positional-only parameter; currently unsupported by Python function declaration syntax, but exemplified by existing functions implemented in C—like divmod—that do not accept parameters passed by keyword.

* If you are curious about the kind of a parameter remember:
		If the arg starts with `*`, its starts with VAR_
		*a  = VAR_POSITIONAL
		**a = VAR_KEYWORD


Ponderings
==========

What I want
    - Positional Args
    - Keyword Args
    - Keyword Args as splatted Dictionary

What I don't want
    - Mixed Keyword and positional


* Do people use this syntax for annotations ever?
 	'int > 0'



