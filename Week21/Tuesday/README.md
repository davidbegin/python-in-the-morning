# 2020 - 7 - 7

 Life Aquatic > Royal Tennenbaums > Rushmore > Darjeeling Limited

 Moonrise Kingdom Grand Budapest > Isle of Dogs > Fantastic Mr. Fox

## Best Knowledge per Second Videos

DAS -> Destroy All Software
Best Talks Ever

- <https://www.destroyallsoftware.com/screencasts>
- <https://www.destroyallsoftware.com/talks>

Gary Bernhardt is the William Gibson of Software (Thanks to the Birth and Death
of Javascript)

## Personal Goal

Use Bellows more this year

What are items that powered by bellows

Should you ever use the lower case dict, versus Dict for typing.

## What is your keyboard cleaning routine

- Back in the day, every 2 weeks, sit down change you're guitar strings,
  its a meditative thing.
  Same for skateboard (setup)
  Keyboard

Once a Month, take the keycaps Off

## Today

- Add Some Types

## Typing Debates

Benefit difference in:

- Writing Types from the Beginning
- Writing Types after it works

mac__gyver: Sigh, you write them from the beginning of course. Else you do
double the work.

- Sometimes its harder to figure out the project, abstractions, direction,
  before you'be even thinking of Types.

mac__gyver: Sigh, you write them from the beginning of course. Else you do
double the work.  mac__gyver: Sure, sometimes you may settle on the wrong type.
However, generally speaking, it is more work to go back and rework all types. By
the end of the day, it is better to think and do the types from the get go
because it will help you catch type errors also.
beginbot: how do you know this?

- Whose worked somewhere, where you're focused on that good code, abstractions,
  nicely typed, full test coverage.....ut oh we have pivot or die.

Premature Optimization is the Root of All Evil

I've watched Very Experienced programmers, say I've done this before, heres the
vision:

- Over engineered, garbage that doesn't money

andyjamesadams: LUL no two projects are EVER exactly the same

Opinion: typing isn't premature optimization
Whos your team, whats the code for, how do you make money

## Yesterday

## Learnings

Okey, for optionals, you should only annotate with the original annotation

```python
def foo(item: int) -> int:
    if item < 0:
        raise ValueError
    else:
        return item
```

isidentical: If it always raises an error, use NoReturn. If it is a possibility,
you shouldn't be worried about the exceptions at all, just add the original
return annotation.

<https://www.python.org/dev/peps/pep-0484/#exceptions>

## Resources

- <https://github.com/github/gitignore/blob/master/Python.gitignore>
- <https://martinfowler.com/articles/mocksArentStubs.html>
- <https://www.wikiwand.com/en/Core_War>
- <https://tree.science/>
- <https://github.com/dropbox/pyannotate>
- <https://github.com/instagram/MonkeyType>

## Bounties

## Viewer Questions

kendaryth: begin im adding tests to my project (thanks to you!) and im facing a
problem. I use a linux library, because my code is deployed on a rpi, but i want
to test it on my desktop (macos) where the library does not exist ... Any advice
on how to achieve that? Maybe mocking?

Options:

Working on Mac and Linux:

- Use the library in a Docker Container
- Find an alternative library in Mac, and write something switching based on
  environment
- You could Mock, but it all depends on if you can be sure of the behavior of
  the library

stupac62: if you have 2 optional params to a function and in the function you
check against the params to handle the optional nature. But when I start using
it in the function I get mypy warnings about mismatched types. I just put #type:
ignore You ever ran into this?

2 Optional Types might be Hard.

- Why do you want to ignore these files?
  Answer: These files are specific to your computer, secrets, compiled code,
  things not needed to run, logs, dependencies, datasets

You have a project:

- List your dependencies in a requirements.in and .txt file
  - You don't want to bundle the actual

## Questions

## Ponderings

## Experiences

Beginbot: I've wroked with AMAZINGLY productive engineers who don't type fast at
all, they actually could be considered slow. They type less, the type the right
thing first more often.

Others:

isaiahvander: Redpill me on arch bro

ArchPill

Mac User Whole Life
Start Developing on the West Coast Startups -> Mac Life

Did that for 8 years.
However all my code that's deployed is on Linux servers.
And really into Vim, Commandline Unix Philosophy

I need to make the switch to Linux for Personal/Work Desktop:

- Control over system
- Learn more about Linux systems work
- Cost way less once you start doing everything youself.

So which distro?

- I am going to be hanging, and having fun on computers for the next 300 years.
I want something longterm, want something that I can personalize to myself,
.....most importantly want impress nerds on the Twitch.

Arch -> Harder to get started
Yes you have to read the docs
Yes there are a lot of docs
Yes you have to do many things yourself

Yes you have to learn things that are useful.

Week 1 was harder than Ubuntu or Pop or Mint
....however I ain't having problems all the time, now or often.

## Opinions

## Debates

freeman42x: how to start a war: types are better than docs

## Advice

- When someone sneezes, don't say bless you.
  Turn them, look them in the eyes, and firmly say: Stop.

We don't control things, we can only build feedback loops,
if you bless people for sneezing, you are encouraging sneezing,
for being who wanted to be blessed.

## Confessions

## Quotes

## Scraps

## TODO

- PEP Jeopardy

## BeginWorld Religion

Anti-Typing Test:

Many new programmers, think the mark of a good programmer is:

- Amount of Code
- Typing Speed

BeginWorld Religion -> These are both sins to covet

If you are working a job, where typing speed is the limiting factor
in your productivity: Then you need a harder job.

Anti-Programming Competitions

---

Programming is not that hard

It's fun

It's a giant field, and almost everyone will find some portion, area, language,
that they enjoy and are good at.

Programming is for Dumb people (I know nothing, words are hard, math is hard, I
know science).

Soooo much of programming, is pattern-matching, and abstracting.

Learn patterns, you learn to extract at different levels.
But its a life-long process (like a craft that you have to Do to improve)

<https://doist.com/blog/feynman-technique/>

Javascript
Python

Interactive Websites -> JS
Command Line, Games, Backend, Data Science -> Python

dreytoxic1: @onyx_pupper answer is no however, you should choose a language that
makes $$$ if you want to get into it. If you're looking for enterprise work C#,
Java. If you're looking for start ups python followed by Golang & Rust.
JavaScript should be also something you'd want to learn in parallel

DO NOT CHOOSE A LANGUAGE THAT MAKES MONEY

CHOOSE THE LANGUAGE YOU FIND THE MOST FUN/INTERSTING
BECASUE YOU WILL END UP PROGRAMMING AND LEARNING ABOUT IT
MORE EASILY.....AND MAKE MORE MONEY

Do one full site:

- HTML
- CSS
- JS
- Some Backend

Find people who work in different categories, and learn what their day to day
is.

- Listen to different podcast for areas.
- Watch Tech Talks
- Meet Programmers

It might take 6 months to find out what you are really interested in
programming, and you might learn a lot of stuff, that isn't directly
related to your new goal...thats ok!

We are talking about a Career.
....doesn't it make sense to maybe spend 6 months figuring out something,
   that you'll do everyday for the rest of your life.

Why Hate Frontend:

- I hate users
- I hate interactive websites
- I hate CSS
- Hate dealing with nit-picky styling
- Hate dealing browsers
- Hate JS landscape

I once spent maybe a couple weeks exploring a bug, or a random
loop in the code happening somewhere.

Learning about Databases
....I learned everything I know about working databases on the job
....why....the data is real, and theres actual expectations.

You have to find a way, to work with real data.

Postgres great first DB, if you have DB and minimal data,
you never learn the skills you need for work, because of
the size of importance of data.

What do devs do the most interacting with Databases:

- Optimizing Queries -> When do you do this? (When you're Data is big)
- writing data-migratrions -> When do you do this -> when you're data is real!

- Run Postgres Locally
- Get it working in a Docker Container Locally, Then for your CI
- Deploy to Cloud, or used a managed version
