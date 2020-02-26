2020 - 1 - 14
=============

Difference in Typing:
	* C versus MyPy or Typescript

	* If your language does memory management
		in rust, then you think about size

DraconianDeveloper:
Whats I don't know the official name for it,
but I simply treat Python types as C types
but there's no static typing in Python like we see in C.

I should be learning the C Types

Also Decimal


'Complex',
'Integral',
'Number',
'Rational',
'Real',


C types are based around space and type??


float
chr
int

double

Ration
Real
Complex
Number

(<class 'numbers.Integral'>,
 <class 'numbers.Rational'>,
 <class 'numbers.Real'>,
 <class 'numbers.Complex'>,
 <class 'numbers.Number'>,
 <class 'object'>)




OOP Feelings
============
	* I hate modifying state
		when Im doing, I want it so explict, isolated
		almost functional
	* More complex to implement, slower



Çhallenge
=========
  What are the Python Number types in order?
  Integral?

	Make this compile in your languge?
		a ™ b = ab™
		Entrants: https://en.wikipedia.org/wiki/Operator_overloading#Catalog

I wanna do:
		* Eiffel
		* Smalltalk
		* Io

		* ALGOL 68
		* Clojure
		* Fortran
		* F#
		* Haskell
		* R
		* Raku
		* Scala
		* Seed7
		* Swift


Quotes
======
	*  "i dont know anything, i just make money from programming"
		- me



Questions
=========
  infix: + and |
  unary: - and ~

  * What makes a pleasurable APIs?
    - Well Documented
    - Obvious
    - Simple
    - Powerful??

  * What is an operator in this function?
    - any function we define, that gives us access to + or - etc.

  * What is Bitwise inverse?
    111 -> 000
    101 -> 010
    ~7=0

	* What will go wrong if we do modify an object in place when overloading a unary operator

	* python is always pass by reference, why is it fundamentally wrong to modify object in place?


	This isn't about pass by refrence:


Why don't you modify objects in place:

Pro:
	* If you don't modify it's to easy to reason about state

Con:
	* More memory
	* More Code


Top 3 Cliche:
	- "Premature optimization is the root of all evil."



Don't care about performance at allllll.
Make it readable
Make it explict
Make it extensible

Identify to optimize once you got a problem





Why do you have no problem modifying state:

We are all cool with modifying state in our code.
Then someone else modifys the state of object



When do you start becoming a state modifier hater:
	* Work in a project, with too many objects changing state all the time,
		spending all this time reasoning about what state it could.
		testing hard, because you can't accurate define what states.


Java didn't implement operator overloading, because of PTSD from C++

If is it good to make design decisions based off of PTSD

Hey now, I got state modification PTSD, don't modify


Is this a fact, or proveable?

If you don't modify state, the program is easier to:
	* debug
	* reason about


Medium
Achieving 33% Less bugs through Strong Typing

Scientists say:


This is the state modification:
```
order = Order()
order.status = "Paid"
import pdb; pdb.set_trace()

order = Order()
order = OrderPayer(order).pay()
```

Force people to think real hard when they are changing state
Consolidate it somewhere, make it explict



# Order
# 	status: Pending
#
# Order
# 	status: Paid




Is it best practice to always to return a new object, for all method overloading?










Favorite TDD Game:
	* Play in pair
	* Someone writes the tests
	* Someone writes the code
		- Person who writes is evil
		- Write to simplest, dumbest code to get past the solution.
		- Lazy and Evil



Xtreme Programming Stream:
	- all the things
	- Cards



Bring back Webrings


When was the downfall of content on the web, in terms of like
content to ad ration



Facebook Google
---
	* Advertising companies
	* want your attention



FAAMG

Amazon
Apple

Haze Opinon: Microsoft is the most evil


Netflix:
	- Cool company
	- Cool tech
	- Chaos
	- pay comedians
	- people to make stuff


Don't hire juniors
......they built on AWS


All are platforms except

F
AWS ->
A
M
G




What would it take for Netflix to move off of AWS???
	* Are there all comparable products each AWS does?


Theory:
	* Cloud Agnostic Dream is Sham
		- Write containers, Kubernetes
		- Isomorphic 2.0
			Write app, Android, Iphone, Web App Noooo


Terraform
	* AWS, GCP, Microsoft


Spartan PR Adding a Lambda:
Begin has a PR for updating a Database and Adding a Kinesis Stream

Spartan goes first adds the Lambda.
When Begin applies next, he should not have the lamdba




If a Developer wants to build off of something not on Master,
then they have branch off the branch.

If branch off the branch, then you need to coordinate, with branch A developer,
and say don't reset state.




A lot of these problem depends on your state breakdown.

Terraform State starts a monolith, goes through similiar
anything.

Breaking it down into smaller pieces:
	* Two people working on independent.
	* Reduce the potential Blast Radius of changes


You have to be careful about designing a Heircharcy, or Tree of States

Global -> Regional -> Enviromnent -> Data Resources -> Application Code -> Monitoring


Spartan: Adding a new Database
Begin: Adding a Lambda connecting to Said Database


Database State should be separate Lambda Code








































State Locking with DynamoDB with Terraform is easy

2 branches, changing similiar:
	PR I : rename this lambda
	PR II: add these environment variables to this lambda.

PR I: runs renames
PR II: run rename back and add the variables??

Biggest potential problem:
	* Not being updated from the same Base State.









Options to Fix this problem:
	* Run the base state first before applying a PR
		Con:
			- Slower for every PR, because of the extra Terraform Run.
				- Depends on the garbage the last developer left
				- This could be bad for developer relationships, begin left a mess
			- Slowest for Developer
			- Threshold Question: How long are we willing to wait for clean-up TF run??
				5 Mins - I could handle
				10 mins is the threshold, too long. Can't wait that long
				Is 5 builds an hour ok?
		Pro:
			- You know that this is applying exactly from the state you expect


Nike, used to hear this about microsoft
	* Nike only gonna sign you as a contract
		not hire you
		then they will let you contract expire, and wait
		.....until they hire again, so you don't get any benefits


Contract to Hire is a real thing, and can be awesome.
You can get yourself in the door, and prove you are more valuable
than you experience or resume, take more junior, risky applicants.
more confidence

Contract to Hire for Juniors:
	- 3 Months


Adidas
	- Green stuff
		in terms of the environment
		4D crafted, that was for future enviornment plans
		European


Birkensock
Rockport has not Tech



Nike makes money
....I buy Nikes
They are involved in some Real tech?

SNKRS
	- High-Demand Low Invenotry Thundering Problem
Wearables
	- Maybes that cool
Tech for Helping to cheat to win:


LA Lights is going Cloud Native

You can't go Cloud Native unless you're not using Computers
	



La Lights Shoes MODs





*Begin Recommendation*
If you are budget concious
And you have some responsible developers
Clean up their mess

	* Run the base state after done verifying
		Pro:
			- Fastest for PR developers
			- If you make a mess, you clean up your mess
		Con:
			- You can't know for a fact, that the env didn't drift
			- How do trigger when to rerun this base state
			- This depends on humans to do some work

		What happens if you don't:
			- If you don't clean your environment, you lose deploy privilidge system




	* More environments!!!
		Pro:
			Fastests for Developers
		Con:
			* More money
			* more envs to manage
			* still need automation to run base state



AWS:
	* Reservered Instances


Will we be using this??
Will it be the right size??
We will be exist????





CI/CD Pipeline:
	* Sync with Master Option thats easy to run.
		Question: When are you going to run this?




























My Confusion about infix:
=========================
	infix + or -

	unary + or -
	infix + or -

	unary = +1
	infix a + b

	__pos__
	__add__















Learnings
=========
  * A lot Java choices are C++ PTSD
  * James Gosling
  * `d ™ b = db™` get this to run C++

	* If a "typing" in language, if you manage memory, you types will
    reflect that.

	* If you are implementing a unary type, (through the appropiate dunder
		method), always return a new type, don't modify "self"
		What happens if you don't??


	Absolute:
		abs(-32)

		Vector(2, 3)
			-> it exists on a point in space

		Vector(2, 3, ...)
			-> we live in multi-dimensional world

		Always????
			__abs__ is only for a narrow use
			What are all the types of things you want absolutes
			Overrated






Bowling
	- 2 Strikes
	- This is the song you choose: While you see a chance



Ponderings
==========
  * Are the days gone of a single person creating a new language that takes
    the world by storm.

