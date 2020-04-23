# 2020 - 4 - 23

## Bugs

- You can give anyone props

- Saving invalid commands for SFX requests

- looks like perms for user is broken

## Features

- for cool points you should be able to search.

- All commands have a fixed health
  - We will start configuring this health

- Total num of soundeffects command

- Add a help for a blank !soundeffect

- Build a robust system for approving soundeffects

- Nostalgia mode
  - Save the songs and money, and can swap them in

- Add Each mode together, for a master mode from throughout the week.

- Record a Video on How Chat Thief Works!
  - Clip???
  - Highlight???

- Quick colorscheme command

## Refactor

- Better logging around when we are saving and deleting from the DB
- STOP having real users, and hitting really "Databases" in tests
- Replacing search with get

## Potential Fixed

- Saving invalid JSON somethimes
  - We could just clear the when it gets corrupted?
  - Description of the problem:
    - bot.py            -> writes soundeffect requests
    - soundboard_bot.py -> reads and deletes the soundeffect requests
  - Theory of the bug: Reading and Deleting at the same time
    - When we are writing, write a lockfile
    - When we want to do anything else, wait for the lock to be gone

## Nightmare

12:30 -> Dystopian Future

This is fundamental flaw in the system:

Back Ally dealings, people farming street cred, and swapping it with each
other cool points, without even knowing who the other was.

How do force people to have to have meaningful interaction with each other,
or observe.

## Different Langs

Elixir or Rust

## Future Ideas

- We can simply replay the chat and see where the economy ends up
  - Then we can abstract economic models out, and try out different
    scenario

## Resources

## Vim Goals

We just got to focus on getting one command into our habit a day

## Bounties

## Stream Ideas

[import asyncio: Learn Python's AsyncIO #2 - The Event Loop
import asyncio: Learn Python's AsyncIO #1 - The Async Ecosystem](https://www.youtube.com/channel/UCRF82wX0EPwqvKMBwvB4fQg)

## Viewer Questions

stapotv: are you proud of any of your prevous projects?
NO! - Ego is the root of all problems
NO! - If I don't hate my previous projects, then Im not learning

Stupac: Python on Twitch News Network

Anothywritescode -> writing an editor in python
AlSwiegat -> writer of automate the boring things
@nnajio -> micro python
@dowright -> pen testing

dmfigol: I am glad I discovered your channel, some cool stuff and discussions
here. Any recommendations on another Python developers-streamers?

stupac62: <https://github.com/eugene-eeo/tinyrecord>
stupac62: the post said to look at tinyrecord as a solution <https://github.com/eugene-eeo/tinyrecord>

I take notes for everyday,
When do I review them?

2 Types of Notes:

- Life Notes
- Working Project

Right after, I will review the notes and pull them into my other notes

Keep a folder of all my notes, pulled notes from project notes
Then you a big folder for searching

Review your notes twice a day:

- Morning and Night
- Night one, not too late -> 8PM

## Questions

## Learnings

zerostheory: traditionally irc would do nothing to mask your IP I think thats
why people think it's insecure, it's on the irc server owners to mask it. Twitch
masks so I don't think you'll have an issue with that. Unless there's something
else insecure.
pylang: I hear people "bounce" to work around the IP issue

## Ponderings

Alternatives to Git, and the Git Cult
!so rwgrim

## Opinions

hannylicious: Arch vs. Ubuntu- what is your opinion - GO!@

Beginbot:

Questions:

- Do you plan on using a computer seriously for the rest of your life
- Do you think its valuable to know how your computer works!
- Do you have the time and patience to learn
- Do you like to participate in programming comunnites

ARCH

## Stories

Disclaimer: DON'T DO THIS
I worked at a Ruby startup, where we built everything:

- Web framework
- Testing Framework
- Utils
- ORM

## Rants

Slack is like Uber, first it made the world better, now it is waaay worse.

The way we use Slack
The amount we use slack
the interruptions from slack

Slack blurred lines between what should be an email and wwould should ber a
slack message

more slack messages == more synchronous communication == more interruptions + a
lower threshold for thinking your thoughts and organizing them first.

Sometimes a 50 message Slack FLamewar, could have been
5 nice emails.

irc is simple
its used outside of slack
its been around forever
you can connect to irc

## Debates

usuallyhigh: If you never had the need to try another version control system, it
means that it's perfect because there is nothihng that made you look for
alternatives Kappa

## Million Dollar Ideas

7 Version Control Systems in 7 Weeks
Git
Subversion
CVS
HG - mercurial

## Confessions

## Python Interview

## Quotes

> spartangtr: because javascript is a cancer on programming

## Scraps

## TODO

- starlette
- c4tfive: get this mane some pmenu highlighing stat!
  - autocompletion is the default
- c4tfive: was watching Strager and he did a visual selection followed by a
  !tac, never thought to use that to reverse the selection!

 REPOST lol: @beginbot when you start cube.. you should rest your hand and cube
 on the spacebar and bringing your hand up releasing space.. That is the trigger
 that starts the cube timer
