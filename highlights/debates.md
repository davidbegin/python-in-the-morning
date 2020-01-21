Debates
=======

## Should we scope our test methods in a class or not?

In a Class
	Pros:
    Namespaced, which is a honky good idea
	Cons:
    More overhead for setting up tests

Raw Methods:
	Pros:
		- See in the wild
	Cons:
    - Could potentially have a namespacing issue


## When should a failing test halt the execution of the rest of the tests?


Test Setup Preference:
	* Single Unit Tests
		- the method name, gives the description of the tests
		- Its annoying making fake method names with descriptions
			- Counter example: Rspec it "testing nil values get a default"
				versus `nil_values_get_a_default~
	* One Unit Tests many examples
	* Single Until Pytest.fixtures?


You have a group of checking lower()
	- If one fails you stop testing the others

If you let all run, you know the exact case where lower is working or failing


What Context are tests running in:
	- A CI/CD Pipeline
	- Locally as we develop
		- We show we all the detail failures in the code I'm working on
		- Don't run Acceptance Tests and slow tests


## What is the definition of a Smoke-Test?

Smoke Testing Definitions:
	- Does it turn on not blow up, real basic functionality
	- Does it do a large bredth of simple tasks without blowing, the "Basics"
	- Does it start "smoking" when the system is pushed
		Does it blow up under real use?


# Should you use pytest or unittest by default in Python?

Pytest
	Pros:
		- what you will use at a company
		- You are practicing what you will use to make money
		- Most open source is pytest
	Cons:
		- its a dependency with dependencies!!

Unitest
	Pros:
		- no dependency!
	Cons:


## What's the preferred method for accessing the first element in a sequence?

```
# Option 1
meth_name = meth[0]

# Option 2
meth_name, _ = meth
```

Option 1
	- meth can be any iterable thang
	- it does one thing, grabs the first element, pretty explicit
	- Con: obscures what meth is

Option 2:
	- implies a 2 length tuple
	- faster
	- Maybe: _ hey what did you throw away
