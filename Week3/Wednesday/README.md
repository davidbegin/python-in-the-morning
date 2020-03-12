# 2020 - 3 - 11

Future of Python, How Do Languages Evolve

## Resources

- <https://www.wikiwand.com/en/Tim_Berners-Lee>
- <https://www.wikiwand.com/en/CERN>
- <https://www.wikiwand.com/en/World_Wide_Web>
- <https://mail.python.org/archives/list/python-dev@python.org/>
- <https://mail.python.org/mailman3/lists/python-ideas.python.org/>

## Bounties

### What's New In

- Ruby:
- Rust:
- Elixir:
- JS: PHP:
- Haskell:
- INSERT_YOUR_LANGUAGE:

- Show me a Repealed PEP!

- What are uses of this `function.__code__`?

The JVM supports bytecode instrumentation (via class loaders).
It works well, as it provides a clear way for third party tools
to modify the behavior of a particular piece of code without
violating any of the invariants of the interpreter.
We don't really advertise setting `function.__code__` as a way to
add low-impact breakpoints or profiling, but it is there.

## Viewer Questions

## Questions

## Learnings

### Stalemate

What are real world use cases for the feature, to help influence the stalematedirection

What opaque mean in this situation?

- <https://www.wikiwand.com/en/Opaque_data_type>
- KieKAEMODAiwiECo: At least in C and C++ "opaque" is used
to refer to type for which you don't see any internals
and can just copy and pass to the library who created it.
- <https://www.wikiwand.com/en/Opaque_data_type>

I don't Understand PEP 523

What is up PyInterpreterState?

- isidentical: PyInterpreterState is an internal struct that is used to
create new interpreters and interpret python bytecode
- When did this happen?
  - Was there debate?

- We are trying to hide something ...... but from everyone! I'm down here
  I'm an adult, gimmie access!

  - no, hiding things makes maintainability and improvements easy.
  Like if they dont shadow some members, and when needed they can't
  remove them because C-APIs might use that members.
  So they are defining a subset of structs and their members
  that can be used in anytime and they guarentee
  that that members wont be removed

- ABI is application binary interface.
  - <https://www.python.org/dev/peps/pep-0384/>
  - The primary source of ABI incompatibility are changes to
    the lay-out of in-memory structures.

- Is Microsoft influencing python?

A key question is at what API level should setting the
frame evaluation function live at?

No one is suggesting the stable ABI,
but there isn't agreement between CPython or the
internal API
(there's also seems to be a suggestion to potentially remove PEP 523 support
entirely).

- How does aa Frame Evaluation API make us money?
  - Click: Make Fast Cash with Advanced Python Frame Evaluation

- control over the execution of Python code comes down to
  individual objects instead of a
  holistic control of execution at the frame level.

- What does holistic control of execution at the frame level MEAN?????
- The normal python code compiles to bytecode form

- wanting to have influence over frame evaluation may seem a too low-level,
it does open the possibility for things such as a method-level JIT
to be introduced into CPython without CPython itself having to provide one.
- We can have different types of JIT

### Isidentical Teaches Begin

The normal python code compiles to bytecode form
And after that there is a big switch loop that has all bytecodes
and it processes that bytecodes one by one
Imagine x.py has 2 + 2,
python compiles to (without any opts)
LOAD_CONST 2 LOAD_CONST 2 BINARY_ADD
and then python creates a frame object (for the global context)
and then it executes frames one by one
and every instruction inside of that frames also one by one
this PEP proposes a way to change that executing function / loop

Proposal to Postpone

python -m dis (and CTRL+D after you write your code) can show the bytecode.
Python/ceval.c is the interpreter loop

- <https://github.com/python/cpython/pull/13600>
- isidentical: this is kind of PR that is really hard because it touches everywhere.
The reason this feature wanted for coverage tools
(because when python optimizes some expressions they might loose some information)

This then allows for a JIT to conditionally recompile Python bytecode
to machine code as desired while still allowing
for executing regular CPython bytecode when running the JIT is not desired.

Python doesn't do many optimizations because the optimizations must be done
if it affects everyone. But if you have specific concepts that might be optimized,
you can just switch the evaluator function and do your optimizations and save time

#### What are uses for PEP 523

- Tracing
- Profiling
- Debugging
- JIT
- analyzing bytecode frequency (which probably could be done with other
means) to inspecting type information from function calls.

#### Stalemate Timeline

PEP Propopser says ha, this thing has stalled, cuz it ain't possible no more
and we disagree on the direction

Kind stranger says hey I use this thing and love it! Heres some of my use cases

Another friendly figure, I think it should be at the CPython Level, heres a PR
Doing that.

> I'm in favor of adding a public C API to get and set the frame
evaluation function. API excluded from the limited API.

until the tstate question is resolved.

What is the is the tstate question?

However, I'm still not convinced that this is functionality we want to expose
through the public API.

Python 3.8.0 is now released. The internal C API can be used to access interp->eval_frame.
I no longer want to backport this change to Python 3.8.

Why do you no longer want backport?

We want to merge before the 3.9 feature freeze

@rsumner868: Hi, I saw you approving a few PRs.
Would you mind to elaborate what you reviewed and explain why/how you approve a PR?
This PR is controversial, you cannot simply approve it with no message.

I'm strongly opposed to this change.

PEP 523 does not specify what the semantics of changing the interpreter frame
evaluator actually is Is the VM obliged to call the new interpreter?  What
happens if the custom evaluator leaves the VM in a inconsistent state?  Does
the VM have to roll back any speculative optimisations it has made?  What
happens if it the evaluator is changed multiple times by different modules?
What if the evaluator is changed when a coroutine or generator is suspended, or
in another thread?  I could go on...

IMO this punches a big hole in the Python execution model, but provides no benefit.

Fabio - This allows us to debug, without introducing other de-optimizations

@Mark are you strongly opposed because we're providing an API for changing
the eval function in the CPython API and you think it should be in the
private API? Or you objecting to PEP 523 all-up
(based on your list of objections)? Either way the PEP was accepted
and implemented a while ago and so I'm not quite sure what you are
expecting as an outcome short of a repeal of PEP 523 which would
require a separate PEP.

This is an assumption
That the `eval_frame` is hard to access is a feature not a bug,
as it discourages misuse and enables us to remove it easily,
when a better approach becomes available.

Confusion around where to implement, Mark Shannon might have
thought in the Stable ABI

How do you decide between CPython API and
internal publicly accessible API?

- CPython: "you probably don't want to use this but we won't
yank it out from underneath"

- What does invariants mean in the context of PEP 523

#### Python Lawyer

## Ponderings

- Should I raise in Tau society?

## Opinions

Goyo + Limelight + coc-markdownlint

PEP 498 is my favorite

ETL + Python + AWS Lambda + S3 + Kinesis = This is nice

Extract -> Transform -> Load
We have the "Big Data", now how do we make money
ETL ->

## Debates

- HazeAnderson: simple concept -- every successful language provides
3rd party libraries --- if your code won't compile because
library authors break each others' interfaces? ... that is not awesome
  - How can you mitigate this?
  - Choose batteries included versus not batteries
    - do we give people a standard lib
    - Or let the market decide

isidentical: why should they integrated?
There are advantages and disadventages of both CPython, PyPy.
And this is what makes python good, it is just a set of rules
that defines the language and everyone is welcome to implement
their own versions and create some advantages on their intepreters

Ugly is mutable
Aren't all mutable mutable

Beauty is a Quantum
People are in all states of beauty
When one person observes the beauty, it then settles on final
The end state changes depending on the observer

There is no absolute beauty

Richness is it absolute?
Golden Ratio

But that's not the main issue, IMO. The big problem is that changing out the interpreter
is not composable, unlike bytecode modification.

Suppose we have MyProfiler and YourDebugger.
MyProfiler wants to record calls and YourDebugger wants to support breakpoints.

With bytecode modification, and some care, we can do both.
Swapping out the interpreter is likely to cause all sorts of errors and confusion.

I don't really see a problem in breaking the API in major releases
(so, having access for it in the internal API but without a
backwards-compatibility guarantee seems like a good fit for me).

The suggestion of including PEP specific near an implemtentation

The Core of PEP 523:

- Is this fixing backwards compatibility or introducing a new hole?

Adding getters or setters for something that was previously doable that we
accidentally took away from users is not an expansion of semantics; it's fixing
a backwards-compatibility break in a way that lets us keep the goal of making
PyInterpreterState opaque.

I'm considering this issue at a stalemate and so I'm going to loop in python-dev
to help settle this.
If that still locks up then we can bring this to the steering council.

But given the use cases tend to be "deep" knowledge places that can adapt to
API change and version checks, I think re-exposing it without the need for
Py_BUILD_CORE_MODULE is reasonable.

## Advice

You want to the dumbest or 2nd dumbest in the room

You want friends who you disagree with on a bunch of stuff
.....but they are fun talk about the differences

## Fun Game

in vim how to you connvert a multiline into single line


## Confessions

## Python Interview

## Quotes

## Scraps

## TODO

- fix nightbot
- <[Manage Your Dotfiles With Style!](https://www.youtube.com/watch?v=MJBVA4LeJKA)>
- Friday talk Bottlerocket
- [Monads in 15 minutes](https://nikgrozev.com/2013/12/10/monads-in-15-minutes/)
- [Inside the Debugger: Interview with Elizaveta Shashkova | PyCharm Blog
](https://blog.jetbrains.com/pycharm/2017/03/inside-the-debugger-interview-with-elizaveta-shashkova/)
- Review Thursday: [Runtime python bytecode optimizer](https://gist.github.com/isidentical/7d3f8110fdfc53bb94829b0b63729139)
