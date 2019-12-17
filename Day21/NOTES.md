2018 - 12 - 16
==============

Questions
=========
	* What is a Kind 3 Closure??
  * What is the overlap between Decorator and Factory?
    @decorate
    @factory()
    @factory(some_option=True)
    * if its not invoked with parenthesis its a decorator?
    * if it is, then its a factory?
  * When do we need a triple layer decorator cake?
    A function pyramid??
    Maybe Answer: Decorator takes Arguments
                  Affect the Decoration of the inner decorator
                  function?
  * What were the motivating factors to creating Scheme?
    Was it to implement lexical scoping instead of LISP's dynamic??
  * What is a modern language that uses dynamic scoping?
	* Are there any languages with Native Predicate Dispatch?
		- Elixir???
	* What is the true difference in predicate and multiple dispatch?
		- pure type of args, versus artibtray properties of arguments
	* Who uses Morepath for Production?



Kind 1 Closure: a function for which all free variables have a known binding
Kind 2 Closure: a function that can refer to environments that are no longer active
		- Some people say it depends on how you use the function


# Some people would argue that inner is not a Closure in this example
def outer(y):
	x = "Woah" + y
	def inner():
		print("Cool thing {x}")

	inner()


Learnings
=========
  * If we want a decoraTOR to take parameters (always optional),
    we actual we need a DecoraTOR, somewhere to build us
    this fancy new decorator
  * Parameterized decorators almost aways involve at least two nested functions, maybe more if you want to use @functools.wraps to produce a decorator that provides better support for more advanced techniques. One such technique is stacked decorators, which we briefly covered.
  *  Perl 5 offers both lexical and dynamic scoping.
  * If you have first class functions
    - pass them as args
    - assign as variables
    - other thing that make it first class
    and you have lexical scope
    Then you need you to implement closures
  * Erich Gamma, John Vlissides, Richard Helm, Ralph Johnson
	* Note that I am not suggesting that function decorators should be used to implement the Decorator pattern in Python programs. 
	* all you need to know is that in Python, all functions are closed, and free variables bind to variable names in lexically nested outer scopes.

Ponderings
==========
  * What is the most pythonista equivilent to set().discard()?
    list comp?
  * Graham Dumpleton and Lennart Regebro—one of this book’s technical reviewers—argue that decorators are best coded as classes implementing __call__, and not as functions like the examples in this chapter. I agree that approach is better for non-trivial decorators, but to explain the basic idea of this language feature, functions are easier to understand.


Detours
=======
  * Graham Dumpleton’s blog and wrapt module for industrial-strength techniques when building decorators.
	* Same implementation with:
		- Raw Decorators
		- wrapt
		- decorator library
		- wrapt versus decorator?


things I like
=============
  * Touring function pyramids is our next adventure.
  * popularize `________` by showing various non-trivial examples





Decorator ABC
Component ABC

These need the same API, the same Abstract base class

component = Compontent()

# decorator function plays the role of a concrete Decorator subclass
decorated_component = Decorator(component)

func = component
def decorate(func):
	return func() + "!"
