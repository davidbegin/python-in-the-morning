# 2020 - 7 - 9

ML / AI -> Theres the technical side.

WE need more not-as-technical people -> focusing on using creatively

https://docs.gitlab.com/ee/topics/gitlab_flow.html

lunchboxsushi: @beginbot in your work experience how do you manage scope creep
and just new things coming up that you didn't design for originally ? Do you end
up updating your estimates or just work extra time to get er done

Where is Scope Creep Coming From:

- Yourself
- PM/POs
- Clients
- Other Developers
- QA

What could we deliver right now!
What can we feature flag
What is a feature that will be HARDER to add later (so you let it creep
potentially)

The difference in a Junior and Senior Programmer:
Seniors knows when to Gold Plate and When to Duct Tape

If you a release cycle, keeping it complete locked.
People then know, they got to finish, to get this chunk deployed,
otherwise.

## QA is whole other story

- When is QA QAing in the development process?
- How many untested features/bug fixes are tested at once?
- Whats the QA to Dev important.

QA means radically different things to different people/companies:

- Does QA mean following predefined scripts checking the functionality
  works according to Spec.
- Is QA Exploratory manual testing
- Automating End-to-End Tests, that are run constantly (even against production)

Do you have a branch that always represents what is deployed?
  -> could be Master -> just have to make sure master is  being deployed to

Q: Do you need a release Branch?
Real Question: an deploy to production every time you merge a feature branch?
Situations where this is true:

- Mobile Apps with approval steps
- Downtime concerns
- Enterprise Contracts

What is the difference in:

- Github flow
- Gitlab flow
- Git Flow

abk16: What if I have a very early stage project and a couple of collaborators,
no release, just development stuff. Can I use master instead of develop until an
eventual release gets made, if ever?

beginbot:

Main Branch
Feature Branches
Do we have customers? if yes then introduce a develop branch.

Include a Develop Branch

artmattdank: Branch Davidians

## Git Fun

Confusion:

- Differece in Gitflow and Gitlab Flow

Personal Git Opinions:

- Feature Branches SHOULD ALWAYS be short-lived
- think about the reviewer when you are commiting (if you commit 5000 lines),
  you just told someone else they have to read 5000 lines.

dreytoxic1: @beginbot perhaps covering the different flows of git ~ trunk base
vs git flow

There is a big problem learning/teaching git.

Git Flow or Trunk based become more userful based on the Team Size, Release
Schedule.

If you have a huge commit that is automated:

- Generate Docs
- Generate Stubs
- Ran a formatter through everything
- Update everyfile for deperaction

Important: to separate changes made by humans and computers.
Worst Example: Someone lints a whole project and fixes a 1 line bug
  .....then if I go back in history, I see 5000 line commit....that contains
  the bug fix.

Open Up Chat Thief for PRs:

-> Do a couple weeks of Git Flow
-> Do Weeks Trunk Based

Git Flow:
-> Master always releasable
-> Develop -> always up to date as possible

3 Branch Strategy:
  -> Feature Branch -> do you work -> 1 branch
  -> develop Branch -> integrate often
  -> Releaser       -> always releasble...and what is released.

Long Term Feature Branches are Torture Chambers

zanuss: That seems excessive
beginbot: yes it is for 1 person
    get 20 people working on repo.....you'll be begging for it.


- Everytime we hired a new employee, they ask, why not Git Flow?
  Small Startup crammed into a WeWork....and then people would argue for 2 hours
  ....until we made rule, no more bringing git practices outside that are
  related to git.

## Refactor

Fix generating of Website
- Remove all user

## Scraps

pikaprogram: @beginbot what actually is ur specialty?

Beginbot: I like to work at small startups, where you HAVE TO BE a generlist.
What do need to get done?
Write some code a backend?
Build Deploy Pipelines
Figure out business
Hire and Recruit people
Performance Testing and Optimization do that.

For Begin Personally: I like to be able to do whatever I think is most
valuable for the company. This role often has many hats.

good intern VS bad intern -> Good intern/JR can see problems themselves, and has
initiative to try and solve, and take good notes on what you're doing.

Editor Will not impact your salary, or career trajectory
it can only affect you're personal happiness

What makes you happy
Which one excited you more
Which community you like more
What do other programmers you like use.

Vi, Vim, NeoVim == Fun
Holy Wars
You have type

hungryed: in actuality, use any editor that you feel comfortable with. develop
your skills, then take some time sometime and if you want to try a new editor
then you can explore it hungryed: I use sublime cause I'm super comfortable with

100,000 -> Having to use an editor in the browser
100,000 -> WTF Fee....who uses Atom anymore????!

- Scammer Coders -> -> GetRichFastCode
- Anti scammer -> Enginered Man

## BeginWorld Law

DO NOT APOLOGIZE FOR ASKING QUESTIONS

---

rishit_coder: I recently installed wifi drivers on my Ubuntu 18.04 to enable
wifi, and set the antenna to 2. It works fine with the routers but when it comes
to connecting to my iPhone's mobile hotspot, it throws an authentication error
despite of password being correct. What could be the cause and how do I fix
this?

## Begin's Main Concern

When you look at company as an example of how to do things, as yourself these
questions:

- Do they make the world better
- Do they make money

Uber is a Ponzi
stupac62: Hot take: Most mature companies are ponzi schemes! They have to
acquire in order to show growth

Visit LAX if you think Uber has made the world better

Look into what UberEats and Postmates, Grubhub are doing to local business
ORDER directly!

## Stream Philosophy

I used to work at startups where everyone was there right and early,
all motivated. Talking code in the morning

...the sTaRtUp sold.....now I want to recreate, that "dream" fun
"programmers"/"polygots"/"weirdos" talking about all sorts of things
to start the day.

I don't think Streaming while you code, is the best for the code.
But it's better for the community.

Heres the other problem with in-person commuinites:

- You can have them, if your physical location has others like you.
What you if live in the middle of no-where

I don't think the people directly in my physical vicinity are going
to be the BEST BEGIN FRIENDS.

Learning to Code, can be greatly expedited, by joining a community:

zeitgeist

When you hang out with Programmers, and the cultural ziegest unveils
itself, that all programmers hate timezones.

You just saved time! No you know, to approach with caution, and your
setup to not be as frustrated.

## Today

- Add Some More Types to our Project
- Fix Bugs

## Life Updates

I want to find 500 BeginWorld Devotees
who are interested in:

- Code
- Jokes
- History
- Philosophy
- Conversations
- Music
- ArtMatt Afficandos

---

$10 Pateron -> will get everything

$50 -> rich programmer, or 1-1 time.

- Extra Writing
- Extra Podcasts
- Group Calls
- Influence what to work on next
- potentail 1 - 1

- Take a crack at Streaming/Making Content/Helping Others Full
  - <https://www.patreon.com/beginbot>
    - 5 a Weekl Art and Begin
  - Podcast me and Art Matt
  - influence content I'm making
  - Group Calls
  - 1-1 Calls

Philistines: Art Matt and Beginbot

Review that day in history:

- Unscripted
- Jokes
- See where it evolves

I worked at started called Rival -> Goal was to defeat ticketmaster
Then we get acquired by ticketmaster
....I hate ticketmaster
....soooo I never planned on staying ever

ImportError: No module named chat_thief.__main__; 'chat_thief' is a package and
cannot be directly executed

Some Exceptions are unexepcted: when this happens, we need to ask ourselves
how can in my code figure out what needs to be done?

-> calling out grab some info from a file
    failed unexepcted.
    You can check do I have the file I need?
    NO? Try again?
    Try 3 times and against.

stupac62: <https://realpython.com/python-exceptions/>

## Yesterday

## Resources

## Bounties

## Viewer Questions

isaiahvander: my script has 5-6 stages it runs through and it crashes from time
to time, I'd like it to relaunch itself if that happens

Beginbot: A Script should only crash, if something unexepcted happens.
  if you are running a script, and you know about things that would crash
  the script, in general it's better to handle those cases explictly.

trgwii: freelance web scraping jobs are pretty trash on average, horrible stuff,
since usually you're scraping sites that try to prevent you from doing exactly
that
beginbot: Agree

## Questions

## Learnings

## Ponderings

## Experiences

My company got acquired, and COVID messed up launching.
....my job is building out systems to keep things running.
    monitoring/alerting, runbooks, on-call stuff
    perf runs

.........uh when are we going to use this software???

## Opinions

As programmers, we think we should only get paid a lot from companies.
....but if we wanted to just code, blog, help open source community, mentor all day
....theres an internal stigma....being like you need a life changing project.

....Can I find 500 people who love content I make, and just keep making stuff
that fits me.

Decided what language to learn...shouldnt be done after 10 Twitch Chat messages.
A converstation, questions, introspection, exploration should happen.

## Debates

## Confessions

## Quotes

The only eye I have for things that look good is you. Web design is not one of
them.

## TODO

- Write about BeginWorld Setup

I don't have any great resources yet for it atm. the help docs do some stuff and
checking out neovim/nvim-lsp as a place for configs is good
teej_dv: (to try out builtin lsp, you'll need to build from master)

cyb3rjunkie: i use mpv and chatterino

---

fullstacklive: @HazeAnderson You mean your PHP code was the worst you ever
wrote? :P
hazeanderson: @FullStackLive my PHP code was highly rated by Shutterstock in NYC
when they hired me
fullstacklive: PHP has its baggage but it doesn't deserve the amount of hate it gets.
fullstacklive: I mean, the people at FB weren't idiots for choosing PHP.
fullstacklive: @HazeAnderson So the people using a language determine the worth
of the language? LOL

You can not USE Facebook as an example of whats good to do.

If the value in a language is not what is built with it
....then whats the value???

Tell others you know the language?

dwarvencoder: an argument against lisp lol
:pikaprogram!pikaprogram@pikaprogram.tmi.twitch.tv PRIVMSG #beginbot :This is wy
low level-lang exists

Soooo many of the "problems" langauges, frameworks have,
is from the their primary builder

Rails -> built for Basecamp
  -> if you are building a Basecamp like App -> Ohhh boy is Rails

React -> Built for Spreading Fake News, Starting Racewars, Polorizing Society

UBER MAKES NO MONEY
....why would you listen to the3m,o

Does Uber make the World Better?

Beginbot: No

Soooo people in the gig-economy working multiple jobs no benefits.
....if uber is forced to pay benefits.

I want websites to be fun and usable again.

New York Times -> Terrible
Facebook

I don't want hyper-interactive, gamefiy, notifications, pop-ups everywhere,
no info sites, that are just there, to keep you on the website
and sell you info

UBER MAKES NO MONEY
....why would you listen to the3m,o

Does Uber make the World Better?

Beginbot: No

Soooo people in the gig-economy working multiple jobs no benefits.
....if uber is forced to pay benefits.

I want websites to be fun and usable again.

New York Times -> Terrible
Facebook

I don't want hyper-interactive, gamefiy, notifications, pop-ups everywhere,
no info sites, that are just there, to keep you on the website
and sell you info

UBER MAKES NO MONEY
....why would you listen to the3m,o

Does Uber make the World Better?

Beginbot: No

Soooo people in the gig-economy working multiple jobs no benefits.
....if uber is forced to pay benefits.

I want websites to be fun and usable again.

New York Times -> Terrible
Facebook

I don't want hyper-interactive, gamefiy, notifications, pop-ups everywhere,
no info sites, that are just there, to keep you on the website and sell you info.
