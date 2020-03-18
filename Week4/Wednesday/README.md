# 2020 - 3 - 18

Future of Python explorations: Type Hinting Generics and Twitch/Vim Integration
Shgher bs Clguba rkcybengvbaf: Glcr Uvagvat Trarevpf naq Gjvgpu/Ivz Vagrtengvba

We are going to try and understand what the python
community is currently discussing and understand
the different opinions. We are also going to
continue attempt to bridge the Twitch chat / Vim / Mind barrier.

## Resources

- <https://en.wikipedia.org/wiki/Adam_Osborne>
- <https://en.wikipedia.org/wiki/Osborne_Computer_Corporation>
- <https://www.python.org/dev/peps/pep-0585/>
- <https://mail.python.org/archives/list/python-dev@python.org/thread/VYUM3GLXCDFKU6URHN5IPT2UTVESEO4B/>
- [Type Hints  - Guido van Rossum - PyCon 2015](https://www.youtube.com/watch?v=2wDvzy6Hgxg)
- <https://stackoverflow.com/questions/32557920/what-are-type-hints-in-python-3-5>
- <https://www.wikiwand.com/en/Dependent_type>

## History of Types

- <https://www.python.org/dev/peps/pep-0484/>
- <https://www.python.org/dev/peps/pep-0526/>
- <https://www.python.org/dev/peps/pep-0544/>
- <https://www.python.org/dev/peps/pep-0560/>
- <https://www.python.org/dev/peps/pep-0563/>

## Bounties

## Viewer Questions

codenectar: Also Begin as I am working more Lambda stack now. I know Python is
not very heavy as in serverless development its more like DevOps what are your
ideas on improving on and getting better iwth Lambdas , Step functions etc.

Burning Monk Yan Chui

<https://theburningmonk.com/>
How are you logging, tracing, tagging you're lambdas

Important to Remember: What is loaded on cold-start, and what as loaded every time
Libraries cost you time:

- Be careful about runtime, versus develop time deps

Windows Server VS Linux Server

therewillbememes: so is dict a class or class factory ? Keepo
begin: class??????

lemorz56: Hey man! I hope you are good, is there any plugins for VIM that you
can recommend? :D

Begin Top Plugins:

- Goyo and Limelight
- Plug 'godlygeek/tabular'

myusernamefrank: does this PEP mean that Python becomes as easy to read as C++
template metaprograms?
begin: Don't know, but don't think so

## Questions

literallymyname: I think he meant like when doing things with WPF or WinForms?
Windows Presentation Format?
literallymyname: C# .NET

- Why do we want .Net Core
- C# is what people like
- Is this a replacement, WPF and c# for React??
- Desktop Applications
  - Often for Windows
  - but can run on Linux too?
  - Desktop Applications
    - Often for Windows

Why do we go down this path at all?

- Is this because we develop on a Windows machine?

spartangtr: electron is the worst
spartangtr: C# may very well be a really good language they're just a little too
late, no one takes it seriously even though you can run dotnet core on linux now
spartangtr: they wont be able to shake that stigma

## Learnings

Given that the proxy type which preserves __origin__ and __args__ is mostly
useful for runtime introspection purposes, we might have disallowed
instantiation of parameterized types.

In fact, forbidding instantiation of parameterized types is what the typing
module does today for types which parallel builtin collections (instantiation of
other parameterized types is allowed).
List()

The original reason for this decision was to discourage spurious
parameterization which made object creation up to two orders of magnitude slower
compared to the special syntax available for those builtin collections.

Objects created with bare types and parameterized types are exactly the same.
The generic parameters are not preserved in instances created with parameterized
types, in other words generic types erase type parameters during object
creation.

 Literal types are subset of dependent types?

isidentical: yea, you can do whatever you want to do with future annotations. at
the end they became string. like a: (yield)

- When we use mypy, there are often times, when people choose either list or
  typing.List dict and typing.Dict. This is because Static typing as defined by
  PEPs 484, 526, 544, 560, and 563 was built incrementally on top of the
  existing Python runtime and constrained by existing syntax and runtime
  behavior.

- This PEP proposes to enable support for the generics syntax in all standard
  collections currently available in the typing module.

Like this?
`list[str] ??? ??? ???`

Goal: Remove is Dict and List

Removes some ambguity on typing collections
sets up to deprecate typing.Dict and List etc
makes it easier for people to type, less to import

Generic (n.) -- a type that can be parameterized, typically a container. Also
known as a parametric type or a generic type. For example: dict.

parameterized generic -- a specific instance of a generic with the expected
types for container elements provided. Also known as a parameterized type. For
example: dict[str, int].

## Ponderings

### Visual Studio Big Ole IDE Versus VIM

When I help someone debug in a BOIDE, we end up researching all
this stuff about the IDE

When debugging in vim, we end up learning about various linux tools, or
python etc.

iacchus: types are still werid for me mainly cause im still learing

Type Hype:

You pick the path of No Types: you end up wanting types
You pick the path of Types: You discover you freedom of no-types

## Opinions

bzzzt_bzzzt: documentation is 90% of developing
bzzzt_bzzzt: if you are doing it right

## Debates

### Anti-PEP-585

isidentical: I think List looks better then list, and List[int] looks better
then list[int] vivax3794: agree ^ vivax3794: the list constructor, and the List
type hint are different thing. they should not be combined!

is this anti explicit is better than implicit

isidentical: PascalCase specifies it is a class isidentical: Most of the builtin
objects both operate like functions but they are classes isidentical: but for
types, I'd prefer PascalCase. e.g: Tuple[int] but for utilities like range (even
they are classes) i'd prefer lower case

vivax3794: if a class is going to be used as a function, it should be named like
a function even if it is a class.

vivax3794: what do you like more "Range(10)" or "range(10)" ?  isidentical: for
builtin generators, there is no way to do yield in C level it is why range, all
of the itertools etc. implemented as classes rather then functions isidentical:
with classes they can define __iter__ and __next__ isidentical: I'm in the team
of sometimes-type, like if you are writing scripts dont type at all. If you are
desiging libraries, you have to type etc.  isidentical: @vivax3794,
unfortunately typing decorators sucks isidentical: there is no good way to type
decorators themselves

### Tup-ple vs Tuple vs Tuple vs Tuple

### Lowercase range() Haters

- vivax3794
- OGJake
Big_Rickeo

vivax3794: strange opinion, I want the constructor to be lowercase, but the
class named to be named like a class.

### Why typing-hinting at all

Examples: Typescript Python

#### Pro-Hints

- Replace unit-tests, and we can see documentation in code not tests
  bzzzt_bzzzt: all paths lead to types

#### Anti-Hints

- They don't actually enforce anything unless you build it into your progress
  spartangtr: no that's a bad thing, if you're going to use strong types you
  might as well get the optimizations that speed up runtime with it
  popcorntoohot: anit: you need to create custom "types" like with typescript

bzzzt_bzzzt: IMO the benefit of types like the ones haskell has is it pretty
much tells you how the function works, so much so that in Haskell its called
"type-level programming" myusernamefrank: would be nice to have "dependent
types" in Python as well: <https://en.wikipedia.org/wiki/Dependent_type> looks
like a simplified version of it was accepted:
<https://www.python.org/dev/peps/pep-0586/> bzzzt_bzzzt: internet bzzzt_bzzzt:
there are tons of things that don't use open source cryptography bzzzt_bzzzt: on
the internet stupac62: @bzzzt_bzzzt like SSL?  bzzzt_bzzzt: your micro processor
if you processors with secure crypt modules are usually not open source
bzzzt_bzzzt: if you use yubikey and the like

## Confessions

vivax3794: I need to get better at typing and doc-strings, I do it at the start
of my projects but then I stop :-( begin: samesies

### Cathedral and the Baazar

corbieman: i was always curious when its open-source - isnt it easier to find
vulnerabilities? :D begin: yes! and fix them! versus: a small team looking at it
during development and never again.

I would never use closed-sourced cryptopgraphy Also the Opensource project
itself does matter, how its run

## Python Interview

## Quotes

> You can write good code in any language - begin

## Scraps

## Make Money

- Sell Software to average Joesa
- sell software!
- Sell Software big ole companies
- linux
- huge deals

 Google And Facebook need to die, since they are ad companies At least Apple And
 Microsoft sell you stuff, and not just your data

## TODO

strager: :set makeprg=mypy strager: :make
