# 2020 - 3 - 28

## Resources

- <https://www.wikiwand.com/en/2_Pallas>
- <http://ix.io/2fQi>

## Goals

- Options for affecting pictures
- Random Mode
- Hook it up to song generation
- random band name generation
- We need more info about processing
- Progress bar
  - python standard library progress bar
- Ponder the affects of the ordering of effects

## Bounties

## Viewer Questions

sweeku: Hey, so I recently started using Git. I stored a csv file of ~15k
entries but am not sure if I should do that. Should I try to zip it or should I
even have it there in the first place?

Options:

- Git
- S3

Does it need to be version controlled, meaning you want to look through changes.

sweeku: Do you have any advice on picking out a aws service for compute. Right
now I am webscraping data and using autothrottle so I do not DDOS. It takes ~4
hours though. I am looking into EC2 and I think I would want a spot instance, so
I can pick a daily consistent time to scrape and run for a duration and save
cost

Begin Advice:

- Yes on Spot! Always yes on spot!
- There is a fear that your spot will be taken away while you are working.

Hey AWS you got any extra space, could I rent a little for cheap,
you can kick me out whenever.

Stages of Spot:

- Just use Spot
- Monitor when the spot is going to be taken away
  - this is rare
- monitor price of spot
- How long are these procesess
- Being able to save incrementally

- have some way to easily try out different Ec2

- Discrete scraping is the goal
- Can you start and stop??

Ec2 Spot instance

- monitoring the price
  
DynamoDB table

Lil S3

intelligent tiering

arjunathefeared: i just started learning python about a week ago. going through
python a crash course. how long before i stop sucking?

Your goal is not to NOT suck
Your goal is to be increasing comfortable admitting you don't know anything
Your goal is to learn to balance asking for help and banging your head on
problem alone

If you don't hate your code from a month ago, you aren't learning

What are we learning NOW
what do I not understand
what is scaring me, that I don't know
What am embarrassed that I don't know about

Real Life Hacks

Pretend to be the dumbest in the room
Then you ask lots of questions
You don't have to worry about preserving your ego

The Goal is not become a badass
The goal is to be ok in a perpetual state of learning

Heroic treadmill
Badass Threadmill

I came into programming, failing as a musican
for a single reason
the fear of publishing
the fear of not be a badass
the fear of putting out something lame

I started programming at 25

When you act/are a beginner/humble mind, masters/badasses like helping

Everyone: Admit your dumb and win

## Questions

## Learnings

stupac62: sample uses just the list items even if it has repeats. choices can
pass a probability for each item in list

## Ponderings

myusernamefrank: @zerostheory thanks, but couldn't get it really to work, it is
just a transparent background terminal and then the screensaver in a background
window :-) stupac62: this is a good tool
<https://github.com/sdushantha/fontpreview> anthonywritescode: import by far is
the most annoying yay -Syu fontpreview anthonywritescode: have you ever chmod +x
a python script, ran it, and then wondered why it hangs forever

- Slow learning is good learning, you can learn alot of stuff and forget it

sample, versus choices

## Opinions

- People think AI is a computer solving all your problems
- it's you sanitizing and annotating data

arjunathefeared: which programming languages are you familiar with? what was
your first gig as a programmer? i'm starting late too, very curious

25 - Ruby
6 months fulltime

Freelancer - Small Websites

- Making websites for small business
- Automate stuff for small businesses

Subcontracting
Contract To Hire
Hire

Speed Up First Job Getting as a career switcher:

- Automate something from your first career
- Go to meet ups if you can ( after quarantine)
  - make friends
  - go regularly
  - participate
  - ideally you wanna speak
- write blog posts
  - if its short hell yeah
  - if its a beginner topic hell yeah
  - if its anything you couldn't find on the internet, and figured out yourself.
    Hell yeah.
- Immerse yourself Community:
  - Podcasts
  - Youtube
  - Github
  - Blogposts
  - Mailing Lists
- Have Fun


You choose what you are interested in.

If you avoiding videogames for 3 days
and only programmed, you wouldn't understand, feel
the appeal of the games.




You are your 5 closest people around.

Set boundaries

Choose your addiction

25 - very addictive
was falling in love with programming

I noticed that this could be a career

Ok, time to create the addiction.

I deleted every bookmark, every podcast, every Youtube subscription

Fall in love
Excited
Happy to participate

## Debates

## Confessions

- I don't know what is exif
- I've never heard of exif until now

- I pronounce tons of words wrong
- And generally struggle with emphasis

- When I was young, every single expensive of clothing was gray.
  - cuz it was verstile

Begin's Top Programming Recruits:

- Musician
- Painter
- Artist
- Drug Dealer
- Hustler

Top Skills for Programming:

- Perservance
- Hustle mentality

stupac62: pacman -U /var/cache/pacman/pkg/package-old_version.pkg.tar.xz

















## Python Interview

## Quotes

## Scraps

## TODO

- follow Guido on twiolo twitch
- <https://github.com/iterative/dvc>

- stupac62: I use the goyo activate function to set scrolloff=999 so that cursor
is always centered in screen
- alacritty explore
- emma says youtube

I am extremely interested in Slang, flexible use of language in creative manners

Uh-LACK-ritty

```python
Pixel Spread: radius=8
Traceback (most recent call last):
File "art.py", line 197, in <module>
produce_samples(args.search)
File "art.py", line 152, in produce_samples
effect(image)
File "art.py", line 116, in pixel_spread_img
img.spread(radius=radius)
AttributeError: 'PosixPath' object has no attribute 'spread'
```

## Long Term Life Goals

Canonical Debates:

Vim vs Emacs

- Vim and Emacs expert
