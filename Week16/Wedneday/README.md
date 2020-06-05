# 2020 - 6 - 3

## Benchmarks

41.72s

Async Jinja Template rendering
Q: Do you have to `await` on render?

diff -qr build old_build/ | cut -d ' ' -f2

## Sev-0

- Sounds aren't working!
- The reason's why, is I noticed, the play_soundeffect model test
  was talking to the prod database.

## Cube Rules

- If you guess right on the money you win a cube
- You can only win Once (I have 11 Cubezzz)

- Over 50s you get a mini Cube (2 Mini Cubes)
- 30s - 50s You get a Pretty Nice Cube (6 Regular Cubes)

- Sub 30s you get a Great Cube (2 Great Cubes)
- Shenangins - You get the Jelly Cube (1 Jelly)

## Priority

- Generate and Deploy V1 of Dumb Info Site
  - Link for the people
- Fix Bugs

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

[That's My Purse!](https://www.youtube.com/watch?v=2NOdkMRniig)
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
Never Watch any new shows again (unless they are real)
It happened.

## Exposing User Data Plan

- S3
- Simple HTML Website

## New Feature

## Code Refactors

- Decorators for route commands
- Better interface for models, returning, either a TinyDB object or our own
- Context Managers for Timer changing

## Resources

- <https://www.martinfowler.com/bliki/TwoHardThings.html>
- <https://github.com/awesome-selfhosted/awesome-selfhosted>
- <https://thoughtbot.com/blog/sandi-metz-rules-for-developers>

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

## Opinions

## Viewer Advice

nomoreequtity: Tipoftheday: Use asgiref.sync_to_async decorator

kendaryth: though be careful that tinyrecord is not compatible with the new
tinydb 4

lan_four: !windows

porokon7: !buy ayaya

crazytech44: alrighty everyone I'll be off(1:30am) I managed to get my hands on
manjaro lol have a great day everyone! thanks for the amazing stream legendary
@beginbot

## Viewer Questions

stupac62: when you use filename variable, do you mean that to be the full path? I debate between filepath and filename

filename = "name"
filepath = Path()

## Stream Visions

## Stream Memories

## Learnings

## Begin Opinions

## Ponderings

Given: A user with a slideshow
When: I add/update/remove a slide
Then: All the screens refresh

As a user I want my slideshow to update when I add/remove/update a slide.
So I don't have to refresh all the screens I have open.

## Musings

Begins problem with Movies/Shows: I like to participate in things.
If I watch a show, and I can't add to conversation, have interesting
conversations about it. Then  its boring. I don't like others just
repeated the common opinions.

Hetrodox conversation

There are amazing awesome beautiful movies,
same for video games
However, only one begin, got to prioritize. Games and Shows just
didn't make the cut.
And if you make a clean rule.
I'm drink just a lil, OR NO DRINKING

[That's My Purse!](https://www.youtube.com/watch?v=2NOdkMRniig)

loner_lena: We had to implement a feature that makes sure a certain page
refreshes when the user edits some settings that control the page. @beginbot

Refresh data at appropiate times
Cache invalidation

!iasip Begin Once Again Never Codes Because of ADHD

Elimating Disease is cool
Using people as you lab....little scary, when theres no oversight

## Experiences

I started freelancing to get paid,
then started obsessively looking a company who would mentor
as junior.

A Junior Dev is like a gamble, that can really pay off.
You don't know the language, you don't know the problem space,
your new to programmer, BUT HOT DAMN YOU GOT THE RIGHT ATTITUDE.

Every Job ive had, the real work that I get paid for, I haven't done
before.

lucasfernsilva: what I did before starting freelancing was to create some
systems for free for people here in my city, and if they liked they would pay
me, and my portfolio got a lot of experiences with that, and with that I got a
job in a company that interested me a lot

shaheerbadie: I had a problem with manjaro and davinci resolve

zolor: For Mint. There was a hacked ISO that made it into their official
repository or something like that a couple years ago
<https://blog.linuxmint.com/?p=2994>

What gave you confidence in Ubunut versus Mint security wise.

## Debates

## Confessions

Hmmm I need to run some errands, need a podcast to listen
Think we are going to try Gentoo anthoer machine.
Mental Outlaw
2 hour podcast installing

Arch Linux: Choose all the software we want
Gentoo:     The next level, chose all your software and compile it yourself.
            If you want a computer that is tailored to some specific needs.

## Quotes

zolor: "Don't fix the problem until you know how the problem feels like" -
beginbot 2020

## Scraps

## Later

[gerrit](https://www.gerritcodereview.com/)
[Quart](https://pypi.org/project/Quart/)

