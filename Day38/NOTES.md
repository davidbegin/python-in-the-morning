2020 - 1 - 23
=============

Bounty:
=======
	* Can you exit a loop early and still get an else statement to run?

Goals
=====
  * Learn about Python Context Managers
  * Admit when when we don't know basic concepts
  * Dive down Rabbit Holes
  * Viewer Code Review
  * Ponder Life and Code Questions
  * Have Fun

Viewer Questions
================

Questions
=========
	* whats the difference between reverse() and reversed()?
		- (sort sorted())
	* Why can't you reverse a string with reverse() or .reverse()
	* Why does everyone say not to use else after while and for
		Reasons Against:
			- It's wierd
			- it is different semantics than if/else
			- Not everyone knows what it means
		Reasons For:
			- Cleaner Code?


Should we not use a feature, because its named:
	* Poorly
	* Confusingly
	* Dumb


Language:
	* Python
			- else - for, while, try
	* Ruby
			-
	* Javascript
			- 
	* Java
			- 
	* Rails
			- ActiveRecord is not the ActiveRecord Pattern
	* C++ - cxt



Learnings
=========
  * Brittle Test - A Test that fails when the code still works

    When you have update tests constantly, when refactoring code. They are brittle
    Tests become brittle when you couple to things.
    mock a method to return something for a nice unit test. and that thing is mocked
    is private, so someone refactors it. Code didn't just a refactor. Public method,
    doing the same thing, failed. To Stub or Not Stub.



  * for, while, and try all can use else

  * Inside a breakpoint(), type `interact`
    then you're in a non-pdb shell, so you can use all the cool
    single variable letter names you want

	* It’s cheap to import modules again because Python caches them.

	* When real applications take over standard output, they often want to replace sys.stdout with another file-like object for a while, then switch back to the original. The contextlib.redirect_stdout context manager does exactly that: just pass it the file-like object that will stand in for sys.stdout.

Ponderings
==========
	* Do we like then better than else?
		Wheres the PEP for then?
		What other languages use then?
		What about different keywords, for try, while, and for!??

	else is typically villan,
	if code is story
	if is when things go good.
	else if a little brother if,
	so it always second class

	while, for, try. Its actually a bonus method
	and indicator went right, you get

	while is the complicated version,
	because like break, causes you not to hit else
	however, if the statement becomes falsify.

	what is success to a while statement,
	running for a bit, becoming falsy and moving on.
	otherwise we have infinite loop
	else is still about success.




In Python, try/except is commonly used for control flow,
 and not just for error handling.

Begin has always been told Use Errors and try/except in Ruby for Control
flow is a code smell.








Opinions
========
  * If and especially else is kinda of code smell
    My Goal: Write no ifs if possible

	* Force, don't care if there are conflicts
		Force with lease, says hey do you know the full history,
    and are you just ammending it?
		Or did someone else push up to Git/hub/lab inbetween.

		I ammended by commit, changed history, push that up,
    but only if no one other than me edited history in that time.

		You'll never notice it, and it always work, when it should.
		When it fails, your saved.



For Newbies, it can be great to join a cult/gang/drink the koolaid, just go full
ham, and dive in, until you yourself can realize the limitations of the group.

Example:
  Go Test Crazy:
    Test everything
    Go for 100% Test Coverage
    Refactor your tests waaay to much
    do every type of testing, no matter how small the repo
    Learn how to mock, spy, stub

    ....Until you realize the problems with all of those things,
    and you develop skills to pull back.
    Now you got skills and you just have to excercise at the right time.



Debates
=======
	* Remember, people have different git styles, people are arguning with you
    recruit you. Git Flow, getting into the cult.

 		`Never Modify History Cult`
			Haze potential Cult Member of
			Git is History, stop changing history.
			Some much important info is squashed and ammended away.

		`Perfect Programmer History`
			- Ammend to a single commit add to a commit message, each thing
        I did, until it reached a small logical reaonable chunk.
        Commit and push. and I would ammend, I squah, I flip squash.


"Every Test in the world can pass and production can still be down"
	- David Begin

"Everything Fails all the Time"
	- Werner


When in doubt, go down the Git Flow Rabbit Hole, and debates.





Choose a Git Cult if you aren't:
	- working with others
	- deploying to production

Adopt Some strict git best practices around messages and branches and clean up.
Focusing on History for yourself.


First Job Random things that you need to learn:
	* Git
	* Postgresql/MySQL
	* JIRA



Git Flow Cult:
	- handle dev branches, with production branches, and hotfixes for releases.
	- Collaboration of a fast moving team deploying often.
	- You become rebase expert



Which do you like better?
```
try:
    dangerous_call()
except OSError:
    log('OSError...')
else:
    after_call()

try:
    dangerous_call()
    after_call()
except OSError:
    log('OSError...')
```


### Are EAFP Gang or LBYL Gang?

Begin: I am switching EAFP Gang for Life!

What happens if the condition fails:
  * Return a default value
  * Raise an Error
  * Call some other function to do some work


```
# LBYL
cool_stuff = {"weapon": "knife"}

if "weapon" in cool_stuff:
  return cool_stuff["weapon"]

# EAFP
try:
  return cool_stuff["weapon"]
except KeyError:
  return None

# Python Rouges
return cool_stuff.get("weapon", None)
```




What does context mean in Computer Science, what does context mean in Python.

In the Python case, it means within a setup and teardown framework.
Meaning something happens, you enter the context, something happens when you
leave the context.

Scope and Closure are other words






### Begin's Truth (Universal Truth)
I know things are going to fail
I know I am going to introduce bugs
I know that commit messages could help pinpoint where I introduced the issue.






What Git is For?
	- Not losing your work
	- Begin's Personal Git View: Git History to help debugging.






Current Git Religon:
		Well formatted commit messages plus jokes



Python Interview
================

Scraps
======


https://www.youtube.com/watch?v=aeqnEJpPZVY
