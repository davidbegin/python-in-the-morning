# 2020 - 5 - 28

## Exposing User Data

## Stream Life

!dropeffect arbysboys 8

- Working on Common Questions
- Topics People Asked Me About
- Share my work in progress, with subscribers

whatsinmyopsec: !soundeffect CC5ca6Hsb2Q whatsinmyopsec 2:05 2:10

!requests
!approve 1
python fake_bot.py -m "\!soundeffect CC5ca6Hsb2Q whatsinmyopsec 2:05 2:10" -u whatsinmyopsec

Year-Oh
Yo-Shi

## IASIP FIX

If you are more popular in the chat, you need less support
How do we figure out who knows how to make a proper:
It's Always Sunny Joke
Past: IASIP_FAN

!hate sonicdrown

## Priority

## TODO

- Automate the start of stream better,
  delete welcome file
  purge various DBs
  backup DBs

- Save cube times, with !cubed

- When an issue you submit is fixed, you should get something
  special bug finder sounds
  What are bug finder sounds

- Expose User infomation
  - Upload the JSON at regular times, somewhere public.
    S3
    Prices

- beginbotbot
  - 24/7 channel
  - Where all Trading happens
  - News Will Automatically

## Done

## Sev 0

## Sev 2

## Sev 3

Fix bug in buy Cool Point Price output

## New Feature

!iasip Begin Avoids JS at all costs
!support

!soundeffect YOUTUBE_ID COMMAND 00:00 00:05

## Code Refactors

- Decorators for route commands
- Better interface for models, returning, either a TinyDB object or our own
- Context Managers for Timer changing

## Breaking News

- Hand of the Market
  - Drops streetcred
  - Drops random soundeffects
  - Checks for New Richest Users and Commands and Reports on Them

- Breaking News Bot
  - Reads a News Story, and figures out what to do

- More info for news stories
- Hook Up Coup to Stories
- More info about what happened

Scenarios:

- Richest User Cool Points
- Richest User Street Cred
- Most Expensive Command
- Coup

## Ideas

isidentical: @beginbot, what do you think about adding a way to announce start
and end of bets. Something like !openbets, !endbets

!dropeffect emacs 5

## Resources

[Larry Hastings - Solve Your Problem With Sloppy Python - PyCon 2017](https://www.youtube.com/watch?v=Jd8ulMb6_ls)

## Goals

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

- CubeCoin

!dropeffect countoren

zanuss: @Lan_Four Yeah lol
zanuss: Begin, make a game where we can guess as many sounds in the database as possible
zanuss: nononono, not the total, the names

## Bounties

## Advice

## Opinions

endlessmike133: i get motivated to do a project but then i find someone has
already done it 100 times better. i was thinking of building a cli image viewing
app then i found feh and got demotivated.
beginbot: YOU ARE NEW, WHY DO YOU THINK YOU'LL THE BEST EVER
THATS ALL EGO TALK
WELCOME TO PROGRAMMER
GET USED TO AN IDIOT

Person: I don't know what project to work on
begin:  Excellent, we need to work on the skill of
        designing, brainstorming, spiking a project.
nukeslion: As a rookie, ideas for feasible project are difficult for me!
begin:     Ya thinking too big. Small. Super small.
ABV Calculator -> You would put in the OZs and ABV -> Alachol by Volume, and it
sort, but total alchol content.

People Who want a Job WAnt a Programming:

- Thinking doing X will them Y
- If they aren't already doing the majority
- How many Treehouse courses until I can make a project
- Then Compettive programming, then later

- I like to write in Emojicode for a weekend
- maybe some smarter
- Fun

Basketball == Programming
Programming == Physical Fitness

Whats the final Goal:

I know nothing about competetive programming, and it makes no sense to me.

Goal: USe computers to solve problmes to provide value, with your unique
perspective
Compettive Programming Goal: Sport

- Solving already solved problems
- For Ego???
- Entertainment??
- Networking
- Fun
- Learn

Beginbot: NO SPORTS OR VIDEO GAMES

- Write songs
- Write things

If you don't understand anything
then thats where you wanna hangout
you wanna hangout with other programmers who know more
and then you absorb

isidentical: urllib > requests

How People Think You Learn: You read something, you understand it

How Begin Learns: You keep hearing variations of the same topic, but
different opinons, and it's all confusing, but soon, I start to get
that this is how this works etc.

## Viewer Questions

Favorite Python CLI Library: Click

eitanfuturo: is it easy to migrate all the configs and plugins from vim to nvim?
beginbot:    yes

whatthehekk321: Disable arrow keys? Why?
beginbot: it's import with vim, or learning anything new,
to drink the koolaid, and try and adopt there way of doing things.
in Vim land, you don't ever touch the arrow keys, cuz its slow!
you are taking hand off the home row
but we have a habit. So we just disable the ability to do the habit.
disable arrows, hang out in normal 70% of the time./disable arrows, hang out in
normal 70% of the timen

dk09_: do you prefer object oriented approach or a script approach while
r_u_ri_ui: @whatthehekk321 So you're not tempted to use them to navigate.
developing a python library
r_u_ri_ui: They're not mutually exclusive.
isidentical: using top-level-functions != script style

lan_four: @crazytech44 Welcome myman
beginbot: Ruby land, its very OO all the time. Everything in a class
functions ain't just defined in files. Python land, thats not the normal.
My personal default, is I wanna OO. But lots of python convetions,
seem to be based on scripted.

stupac62: I wonder what it's like for big repos with many people working on
them. Do you think they have like 5 minutes to get their code into the repo
before they'd have to rebase?

Big Ole Repo:

- Lotta people working in it
- Big ole tests suite that has to pass
- You end up in Jump-rope mode.
- Put up the PR
- Wait for the tests to pass
- After they pass, someone else has merged into master
- So you rebase
- Wait for the tests to pass
- Someone else merged into master
- etc

Mergebot: Mark a PR as mergable after tests are passing:

- Then have ya bot, waiting for the tests to pass, if they do,
  and its rebased on master, it merges itself. If not,
  it rebases itself (And if it hits errors notifications)

thegoat9098: hey man any tips on someone becoming a game engineer
beginbot: don't play or make games
          there are many other game developer
          Tim Beadut
beginbot: start making games
phaqui: Game engineer? Learn math (linear algebra), physics, and systems level
        programming languages.

zerostheory: Morning! how's the coffee?
single origin Coffee lover
Africa
West Africa
Verve LA - Ethopian

I haven't "taken" or done math outside of direct work
context since I was.

Teaching myself Math on Stream for Funsises

## Stream Visions

## Stream Memories

## Learnings

## Begin Opinions

When I'm 35 and I run for president, Platform:

- --force-with-lease = default
- --force renamed --force-i-know-what-im-doing

## Ponderings

## Open Source Path Advice

## Musings

Programming is Creative and Problem solving
building something to solve a prolbem
CodeWars -> Laerning to Bowl with Bumpers
Project  -> More Real, harder maybe, more satistifying

You need to learn HOW TO STRUCTURE YOURSELF
Thats the skill

You're no dumb for doing a structured course.....YOU ARE JUST BEING
TARGETED

how many ads are you getting for learning courses.

## Experiences

## Debates

Whats googles goal:
Make Money:
Strategy: Ads
Sell them to companies
How do you sell them
You track people

It's not all about hiding, being secure
Support companies, who you like the mission

biged_twitch: !me :nukeslion!nukeslion@nukeslion.tmi.twitch.tv PRIVMSG #beginbot
:Google is inevitably going to be evil because it's a publicly owned capitalist
company. even with the 100% best intentions, the systems just mean it's
inevitably evil.
space_vacation: Ecosia
zerostheory: !props 2
lan_four: !support
qwertimer: do we use gmail

## Confessions

countoren: btw why did you say you dont have money for vscode ? it is not
vsisual studio
beginbot: it may be free now...but you just wait.
          why vscode???
          I'm ready to be sold, no sellers
          Vim is not hard.
          How is it funner
          Why do I want to hang out in this world 8 hours a day.

## Quotes

stupac62: @beginbot lastmiles was commenting on nixos yesterday. He said the
idea is good but implementation is a horrible hack that is not maintainable

## Scraps

## Later

aynstayn: @beginbot add these 2 plugins Plug 'Xuyuanp/nerdtree-git-plugin' Plug 'unkiwii/vim-nerdtree-sync'

Explore :term in vim
