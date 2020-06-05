# 2020 - 6 - 2

## Local Notes Tip

```bash
alias j="nvim ~/journals/DAILY/"$(date '+%F.md')""
```

Alias a shortcut to a daily journal.

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

Things I need to do to Stream:

- Find Pi
- Boot up said Pi install some OS
- Get SSH working

## Cube Rules

- If you guess right on the money you win a cube
- You can only win Once (I have 11 Cubezzz)

- Over 50s you get a mini Cube (2 Mini Cubes)
- 30s - 50s You get a Pretty Nice Cube (6 Regular Cubes)

- Sub 30s you get a Great Cube (2 Great Cubes)
- Shenangins - You get the Jelly Cube (1 Jelly)

!so ChristianParpart

!bet 45

/bin/sh -> dash

## Priority

- New Cube Rules
- Generate and Deploy V1 of Dumb Info Site
- Continue on

## Potential Begin Problems

- I switch sh to use dash instead of bash
- Luke told me to
- Apparently faster
- Less Bloat
- Some some syntax will be missing

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

We are going to host a HTML somewhere: S3

---

I'm not going to keep an infinte stock of cubes,
waves of cubes

Waves of Cubes

stupac62: Cube goes to guess on money AND be a subscriber?! Haha
If your not subbed you can't win?

BeginWorld Will Have 7 Servers:

- Arch
- Debian
- Fedora
- FreeBSD
- Gentoo
- NixOS
- Void Linux

Alts:

- Qubes OS
- Wind OS
- Shrine (Temple OS with Networking)
- Centos or Redhat versus Fedora

All on different machines, doing different stuff for my stream.
When someone comes in with a problem, I want to just have a server to SSH into
that is being used on stream.

**Fake Breakdown** of How the Computers could work:

Arch       : Run 24/7 Stream
Debian     : Host Website that contains market data
Fedora     : Hosts our Database for the Economy
FreeBSD    : Handles controlling hardware, to control my guitar pedals
Gentoo     : Generate Images and Videos for the Stream
NixOS      : Run Data Analysis on Economy and Stream
Void Linux : Security / Monitoring System

This will lead to nearly infinite rabbit holes

Goal:

- No Cross Over
- Different Tasks on Each OS/Hardward
- When someone comes in the stream and asks what distro I use: "I want to say
  ALL OF THEM"

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

## Personal Goals

Read Our dependencies before install, just a cursory glance.

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

## Bot Feedback

## Bounties

## Advice

vimtutor

Learning Vim:

- learn it with something else hard.
- You want to combine not knowing WHAT to type with not knowing HOW to type.

150 WPM
and they have a million words to write and already know what they are
So vim is frustrating

Combine Learning Vim and Elixir

## Opinions

## Viewer Questions

beginbot is there a way for a new game the community can bet on? maybe a RNG
game.. closest guess wins?

aquafunkalisticbootywhap: hey vim users: do you use something other than bash so
you can use vim editing shortcuts on the command line?

sana_rinomi: Elixir?

stupac62: I think it's better to say that a person that types 60 wpm can code
faster in vim than a person in vs code that types 150 wpm disk1of5: Goooooood
morning! Elixer... i barely know er

crazytech44: @beginbot I thought of learning VIM after I figured out my problems
first

aquafunkalisticbootywhap: what constitutes shenanigans
beginbot: If you want a stream discussing the origin and nature of shenanigans,
          we should probably plan a 24 hour stream. Complicated subject.
beginbot: Defining shenanigans, kills shenanigans

awfulwaffl3: what do you use for note taking in the terminal?
beginbot:  Vim and Markdown
          COC markdown Plugin

christianparpart: is this patch using harfbuzz to render emojis, if so, that's
weird, because ligatures are quite implicitly supported then ;-)
sana_rinomi: Quickly corrects themselves

r_u_ri_ui: Yeah, it's using Harfbuzz.

## Why not use the very complicated, expensive editors, maintained by evil companies

- vi on ever server
  - problem on the server, all the Vscode, ahhhh who knows nano or vim
- Stay in Terminal, terminal is where do our work, why leave for a heavy weight
  app
- Peeople use vim or emacs, they keeping using.

Early on in programming, had some mentors, who programming, 30+ years, still
loving it, still using the same editor.

Vim is Fun

## Stream Visions

## Stream Memories

## Learnings

## Begin Opinions

## Ponderings

## Musings

beginbot: I follow the Glenn Gloud Method of programming,
          large text, face to close the screen

## Experiences

## Debates

## Confessions

## Quotes

stupac62: No, it's like saying here's the hamburger patty, which is the essence
of a hamburger. The other items are bloat and will not be included. Then they
whisper "but I've heard there are hamburger related items on the table over
there"

## Scraps

## Later
