# 2020 - 6 -1

NOOOO!!!! YOU CAN'T JUST MAKE AN APP THAT ALREADY EXISTS,
YOUR FIRST PROGRAMS HAVE TO BE UNIQUE, WELL-TESTED,
SCALABLE, AND WORTH A BILLION DOLLARS EACH!
YOU ARE WASTING YOUR TIME, AND WILL NEVER LEARN TO PROGRAM!!!!!!!!!!!!

haha calculator app go brr

## Personal Goals

Read Our depencies before install, just a cursory glance.

## Set The Stage

- Protests all over, some rioting and looting.
- We have a simple website:
  - How do we make it public?
  - Option 1: A little server
    - EC2 -> start up flask server
    - "Serverless" -> Lambda to fetch Data
    - Dockerize -> Deploy in a million ways
  - Option 2: Generate and Host HTML
    - Generating
    - Syncing

Goal: Generate a bunch of HTML, iterating through users and commands.
Jinja to generate all

meetthejoker: the ogang meet the joker kekw

!iasip The Gang Meets the Joker
!alwayssunny Begin Can Maybe Code

Things I need to do to Stream:

- Find Pi
- Boot up said Pi install some OS
- Get SSH working

!iasip Begin Gets Kicked Off Twitch for His Big Mouth

## Graphviz

Packages (5) gd-2.3.0-1  ghostscript-9.52-1  gts-0.7.6.121130-2  netpbm-10.73.31-3
             graphviz-2.44.0-2

## Priority

## Idea

### Ride Or Die Change

If someone changes their Ride or Die,
Then we should generate a Friendship Ended Meme
Using Image Magick

- <https://knowyourmeme.com/photos/1168682-friendship-ended-with-mudasirs>

#### HTML For The People

Premature Optimizations:

- I do not want to expose an API
- I do not want to store my data in the Cloud
- I do not want to run a Server

What We Want:

- Generate HTML Pages, linking to other HTML Pages
- Store in S3
- Link to user and command in the URL chat

V1: Build out all the pages, and sync with S3
V2: Only update files when needed

S3 Will Be Our Server
Soon it will make more sense to use a server to pull in data.
However, I would like to go the other route, and do something
simpler than S3. And then brainstorm how we want host Beginworld
on our own Hardware. NGINX?

We are going to host a HTML somewhere:

if you want my advice I'd give if I knew you

I would say that now is the perfect time to take that detour. It will not be too
hard, and is the perfect reason to switch....the exact reason why we have
distributed sharing, to help each other and share!

beginworld, advice

Also soooo many issues are soo subtle, like literally missing a `.` or `,`,
so sharing the actual code is essential for help

for example, I have seen many a beginner issue around python imports begin

```
from employee import Employee

from .employee import Employee
```

---

BeginWorld Will Have 7 Servers:

- Arch
- Debian
- Fedora
- FreeBSD
- Gentoo
- NixOS
- Void Linux

All on different machines, doing different stuff for my stream.
When someone comes in with a problem, I want to just have a server to SSH into
that is being used on stream.

Fake Breakdown of How the Computers could work:

Arch: Run 24/7 Stream
Debian: Host Website that contains market data
Fedora: Hosts our Database for the Economy
FreeBSD: Handles controlling hardware, to control my guitar pedals
Gentoo: Generate Images and Videos for the Stream
NixOS: Run Data Analysis on Economy and Stream
Void Linux: Security / Monitoring System

This will lead to nearly infinite rabbit holes

---

- Long Run:
  - Dedicated Hardware:
    - Various Raspberry Pis
  - What OS on for our Server
    - Arch (The Obvious Choice):
      - We are using Arch!
      - More Arch Practice!
    - Gentoo???
      - For the Memes
      - For the compiling
      - For the learning
      - For the Friendship
    - NixOS
    - FreeBSD
    - "Oh that's Good Distro for Servers"
    - Debian
    - Rasbian (Easy Mode)
    - Fedora
    - Solaris
    - Alpine Linux
      - Not excited
    - <https://github.com/minexew/Shrine>
       <https://aws.amazon.com/sumerian/>

- A serious of small computers, all hosted the bots,
  able to talk to each other, or whatever.

- 20 Various Pis, junk computers, all running various Linux distros
  - All managing my stream

- This is to try OS's people say they actual like.

Why:

- Get experience, running actual services on small computer hardware,
  with various linuxes, and then all the problems that will occur.

- Guitars Solos
  - Small Devices that can trigger guitar pedals and move knobs
  - Continue our songwriting/music video bot
- Rubix Cube Betting
  - Build out a more a full fledged betting market
- Economy Soundboard
  - We need host a market
  - We need host 24/7 station where the market is always running
  - Data Opportunities, Stats and Fun
  - Potential Machine Learn (Throw it in AWS with the default ALGs)
  - Small Devices with Different Distros
  - Infrastructure Problems
  - Networking and Security
  - Avatar News People Delivering Breaking News

## BeginWorld

How can Begin have an opinion about FreeBSD? Without real use of it.
We must FIND A USE for every OS

v0idrose: have u used bsd
v0idrose: I don't see any benefit of running bsd over Linux
beginbot: Me neither! ....but I've never tried.

When people say things are maintence problems:

- Begin notices: "What were all the problems? OOhhhh just this one thing"

v0idrose: i was on arch
v0idrose: I quit everything and went back to ubuntu
spydas02: i use elementaryOS because i cannot afford a macbook
stupac62: pop!_OS > ubuntu

dann_y: I use Manjaro and I like it very much, but it's basically arch with a skin
beginbot: how long you been on that majaro

## TODO

- Fix the betting interface:  allow 10s, looking at bets get mixed up.

- Automate the start of stream better,
  delete welcome file
  purge various DBs
  backup DBs

- Save cube times, with !cubed

- When an issue you submit is fixed, you should get something
  special bug finder sounds
  What are bug finder sounds

- Expose User information
  - Upload the JSON at regular times, somewhere public.
    S3
    Prices

- beginbotbot
  - 24/7 channel
  - Where all Trading happens
  - News Will Automatically

## Exposing User Data Plan

- S3
- Simple HTML Website

## New Feature

## Code Refactors

- Decorators for route commands
- Better interface for models, returning, either a TinyDB object or our own
- Context Managers for Timer changing

## Resources

- <https://www.freenas.org/>

## Goals

- Never use a Windows product (Github, NPM aside (for now)) again.
  15 years clean.
- Never Watch Fake Movie again

## Bugs

## Feature

## Code TODO

## Workflow Practices

Enabled OBS hotkeys everywhere using the Hyper Key (ErgoDox)

Twitch I3 Shortcuts

$mod+y = prizes
$mod+t = basic commands
$mod+v = list of users

Search By File Contents
ctrl-p

Search by File
ctrl-t

Ergo Dox 2nd Layer
` + er - {} - curly boi
` + df - () - round bois
` + cv - [] - square

Navigate to COC action
`[g`

vim-test

```vimrc
t<C-n> :TestNearest
t<C-f> :TestFile
t<C-s> :TestSuite
t<C-l> :TestLast
t<C-g> :TestVisit
```

tmux split pane focusing
tmux-z to toggle zoom on split

Twitch Practice:

- filtering bot talk for the on screen chat
- I'm watch full screen that chat.
- Not the real chat.

!jr_boss

!approve jr_boss
space_vacation: !me
jr_boss: How do I play my soundeffect?
space_vacation: !perms @jr_boss
space_vacation: Your theme song?

!approve determin0st

## Bot Feedback

## Bounties

5 Sounds -> give me a reason to not always --force-with-lease first.

## Advice

## Opinions

## Viewer Questions

endlessmike133: is there a privacy focused sso
                Enterprise: Okta (begin hates them and their product)

hitokiri_battousaitv: truly sucks when you want to ask a programming question,
but you know the answer is keep coding lol
beginbot: the skill we are trying to build, is how to ask the right question
          we need to be more comfortable living in the Pit of Imposter Land

hitokiri_battousaitv: but its soo real but dammit
yassine_supergodbomber: is there a way to implement 2 or more views in one view
                        in django?
                        nested views
                        iframe???
yassine_supergodbomber: every view has one get_queryset with return just one view

beginbot: I wanted less heavy weight
          against SQLite
          If I was going to use a relational DB,
          I would use the one I was planning on using
          in Production.

## Stream Visions

## Stream Memories

## Learnings

## Begin Opinions

In the future people who drive cars will be functionality
equilivelant to horse girls
Get a ponytail

America: WE CHEAT TO WIN!!!
Japan:   Cheat so everyone gets paid, and can continue making a living
         doing something they love.
andrelamus: Not really, it was yakuza there a bit

## Ponderings

Comparing more smaller characters into larger meanings
hwats the subdivision of the smallest character

!approve codeshow

!so codeshow

!iasip Sunny gets a Website to make up for Beginbot's Racist Computer

!approve qualitycoder

## Musings

We all learn "best practices", and then do them, until one person goes,
uh what about this instead, writes a blogpost, does a talk,
and we all go, "Oh wait! Now thats the best practice"

It is super important, to have time, to go off the rails,
do stuff that ISN'T BEST PRACTICES, Try new ideas you have,
take a concept push it.
Try the opposite direction.

Then you can evalutate your opinions and best practices.

In programming, we are constantly trying to find the right boundaries
for logic

We are trying to separate concerns

Websites have grown to a terrible level of complexity, that requires
some new patterns because of limitations.

React, the mixing of the logic in templates -> Triggers me. JSX
NO NO NO
I work on a huge codebase, and its waaaay better, than how we used to do.
Ala, Rails + Backbone + Marinonette

The way the web has developed, makes this pattern more useful.

Why do you hate React?
I don't like the things React is useful for building
So the argument that the pattern, I think is wrong, is useful is Void to me
personally.

---

Javascript:

- Is your site fast, easy to navigate, have real content,
back button work?
- Then why are you adding Javascript
You can use Javascript, but if your site sucks just HTML
you are polishing a BAD Website

I enjoy talking about history, polictics, philiopshy......as long as you
don't think you know everything, and you are ok, with load and loads of jokes.

Time Theory

Once we expose an API and people build off of it, then its harder
to change the data.

I'm still moving stuff around in the DB
Build out a simple HTML website, and as we notice
database normalization problems, then update.
Then once we have fixed our DB Model, then expose
as an API.

Determine the JSON Format First.

Current DB Model Concerns:

- No Foreign Keys
- Typically we are using name of user or command as the primary ID

## Experiences

downshiftxlr8: Went from Fedora to Pop
whatsinmyopsec: !props 2
pinkflufflyllama: Solaris os
downshiftxlr8: Docker was harder to install and keep working on Fedora at the time
hitokiri_battousaitv: !shaft
pinkflufflyllama: Solaris os
downshiftxlr8: Docker was harder to install and keep working on Fedora at the time
hitokiri_battousaitv: !shaft
determin1st: FreeBSD is quire empty/light..
porokon7: ai virtualize Kali inside of Tails for maximum leetness

If you have a bunch engineers at work, and you have a hacky script:
  Ask the engineers
  A lot times: you'll have 5 hacky scripts

Run a Makefile
That generates a Makefile
That has commands to Generate Dockerfiles
And Boot up Docker Compose
disk1of5: @beginbot Run a make file that makes an Ant File that makes a Maven
file.. to make a Gradel build script
your job: Hook up the Gradel to Webpack
          I could Hook WEb

## Debates

porokon7: trains are the best public transport prove me wrong
beginbot: WHERE ARE ALL THE TRAINS THEN??????
mondaynightfreehotdogs: trains can't even turn left and right
beginbot: Constant problem of Dastardly Bad Guys Tieing Fair Maidens to the
track.

Play Games, and enjoy them
Don't Play Games (Don't Watch TV) to escape.
Or just escape intentionally
plan it out
schedule to unwind, enjoy some art
Watch the addiction

Read-Nonfiction:

- History
- Biographies
- Philosphy
- Theory
- Real Things
- Things to inform

Cybernetic Systems Thinking

Mako VS Jinja

Bill Gates -> Crushing Companies Making Money
  -> Care about product? NO
  -> Care about consumers? NO
  -> Care About Open Source? NO

Jeff Bezos -> Growing and Being more efficent
  -> Care about customers? YES (cheapest faster product)
  -> Care about Open Source? Yes
  -> Pushed Technology in many good ways: YEs

## Confessions

## Quotes

The word best cannot exist without more context, when it comes to programming - Begin

godworrior1: By extension, there is no such thing as a "best practice"
beginbot:  WRONG!!! `git push --force-with-lease`
downshiftxlr8: Best practice git push --force

kiekaemodaiwieco: there isn't "best practice" there are "best practices" from
which you choose applicable ones in current context

godworrior1: I guess my point is that you should have a reason for doing
something, instead of doing it just because it's dogma
beginbot: this is why it's very important to internalize the problems and pain
in an assoicated area.

For Example (In a Learning Context):

- If you are working on something, don't reach for a library right away
  try and solve it yourself, to help internalize, the problems, and
  domain space the librariess will helpe with. Then once you are
  frustrated doing all yourself, explore options, more educatedly.

## Scraps

Ring 0

Terry ran everything in Ring 0, cuz it was fun! and who cares if it crashed.
And this attitude, or who cares if it crashes, is incredbly important in
the World of Computers.

pinkflufflyllama: imagine if google didnt care if it crashed
google is great at crashing, crashing no big deal,
resilience in other ways, fault tolerance, rundencies

## Later
