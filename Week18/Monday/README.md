# 2020 - 6 - 15

## Python Stragegy Pattern / Command

We have a bunch commands we respond to:

- All go through routers
- hit "Command" classes and Model classes
- Return a string, that is printed to Twitch Chat
  - Metadata object, about what happened

commands/

routers
commands/

UserEvents to be Tracked

CentralCommandRouter -> SpecificRouter -> SpecificCommand -> Performs Operations -> Returns to Twitch Chat

CentralCommandRouter -> in charge of creating the events after the result back
from the Command Class

Then deciding if it wants to send to Tiwtch Caht.

2 Phases:

Generic Parsing;
  - Separate user, command and args

Once we reach a SpecificRouter Class, that class chooses which Parser to use,
based on the command

Parsing soundeffect requests is different than buy

SpecificRouter classes: Help pair a Parser class (or options) with a Command class

New_Commands

## Holes in the Economy

- Dropping effeects for free
  - Cost Money From the Fed
- Halving the price
  - Feds the FEd
- cube Solve winners, sounds appeared
  - Cube winners, steal sounds

## Economic Brainstorming

### Economic Overview

StatsDepartment

- Total Street Cred
- Total Cool Points
- Amount of the Fed
- Total Unrealized wealth of sound effects
- Total User Wealth
- Total User Sound Propertiy

!dropeffect tinkernthink

!keinelust
!impressive

The Part of the Government that reports numbers:

- Raw Numbers
- Other People can construct the models

## STOP BEING LAZY BEGIN

- Move all Github to Gitlab
- Setup some repos, for early blog posts, projects etc. for other user

### Store all events, and expose them for people

- Every sound played
- Every action taken by a user
  - Save the request, and the result

UserEvent
-> request
-> result
-> metadata about the current state

## Goals

- Stats
- GDP
- AGDP
- Deflated GDP indicator

## Phase II

- All the values and rules our economy should be extracted to config:
  - If we make our economies rules config based:
    - easier time running experiments
    - Users to propose Law (Political)

## TODO

- add help info on user page about Custom CSS
- Store Econ Stats
- Upload Econ Stats to site
- Fix the donate
- Fix cube drop
- Build Government taxes

### Government Taxes

- When the government gives out sounds, they must pay
- When sound costs are halved, that is essentially taxes
- Where is the Federal Reserve located
  - Do we treat a regular user as the Federal Reserve
  - We could create our own class concept

### BeginWorld Economic Flaws

We have to fix goverment hand-outs:

Currently: we can drop any soundeffects however much want.
Next     : All sounds given to people, will cost money from the  goverment.

Start of the Stream:

- The cost of all the commands is halved
- that amount is allocated to the government
  - Need a Government Account
- When soundeffect are dropped for the people
  it will cost that amount from the goverment to droppeffects

## API

```bash
curl https://mygeoangelfirespace.city/db/commands.json | jq
curl https://mygeoangelfirespace.city/db/users.json | jq
curl https://mygeoangelfirespace.city/db/cube_stats.json | jq
```

## The New Holy Trinity

I      Geocities
II.    Angelfire
III.   Myspace

## Cube Rules

- If you guess right on the money you win a cube
- You can only win Once (I have 11 Cubezzz)

- Over 50s you get a mini Cube (2 Mini Cubes)
- 30s - 50s You get a Pretty Nice Cube (6 Regular Cubes)

- Sub 30s you get a Great Cube (2 Great Cubes)

## Bugs

## Code Refactors

- Decorators for route commands
- Better interface for models, returning, either a TinyDB object or our own

## Resources

<https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/>
<https://treyhunner.com/2019/01/no-really-pathlib-is-great/>

## Workflow Practices

Twitch I3 Shortcuts

$mod+y = prizes
$mod+t = basic commands
$mod+v = list of users

Ergo Dox 2nd Layer
` + er - {} - curly boi
` + df - () - round bois
` + cv - [] - square

Navigate to COC action
`[g`

Working with emmet-vim

## Viewer Survey

How many meetups until it wasn't akward:

- beginbot: 4
- tinkernthink: 9 - friends and a job
- cachesking: 3 years
- youre_kitten_meh: Four times for each meetup

Want to get a Job:

- Find Meetups
- Go to them
- Make Friends
- Do a Talk
- ???? -> Hey where you work
- Get Job

-> Lightninig Talks

You're a Junior and want your first job.
A here is  what I learned in this X time talk at local
Meetup could you foot in the footdoor

Whats something unique outside of programming your into:
combie that with programming -> quick Talk

Skiiing
Heres a lil app for ski stats

## Bounties

## Viewer Advice

stupac62: but you don't have to donate all
stupac62: definition of donate: give (money or goods) for a good cause, for
example to a charity.
stupac62: it uses give
cachesking: should steal negate give
cachesking: steal -1 give +1

godworrior1: I think if you think you're procrastinating, the way to tell the
difference is to do absolutely nothing (like sit on the couch), and see if you
still don't want to do anything, in which case you're just tired and need to
rest a bit

Fix your Sleep Schedule:

- It's gonna suck for a min (waking up early sucks)
  First days the hardest
- YOU WILL NEVER FEEL LIKE IT

Night Begin
Morning Begin
Drunk Begin

5 minute Begin -> The Begin right after he walks up
  5 minutes of the worst Begin you've ever met
  HES GOT MAD EXCUSES
  HES SOOOOOO WHINING
  MASTER DEBATER -> (YOU CAN IT TOMORROW, YOU DESERVE IT)

He has master the art of debate, don't engage with 5 minute:

-> You need a rock solid 5 minute routine, that you do without thinking.

- Put on Hot Water for Coffee
- Pour class of WAter take a big drink
- Go to the bathroom
- wash you face
- Come meditate 10mins
- Journal - 5mins

## What Am I grateful For

- Every day I get to wake up and hear persepctives from all over the world!!!!!
- Beautiful weather in LA, gonna be a nice Monday
- My Coffee shop open again, and they are roasting beans

## What would make Today awesome

- Have a Fun Stream
- More reading of On Power, with some detailed Notes
- Ride My Bike
- Learn Something
- Automate my Renters insurance

We got the alarm far away
All Lights turn on
Having your lights fade is amazing
I have the lights start fading in during the wake up window 3:30
Whenever I open eyes, I just get

9PM

## Advice

## Opinions

## More Viewer Advice

## Viewer Questions

simplex991: not sure if people can answer but, I'm trying to get a job as a
django dev, what javascript framework would work nice alongside django?
TLDR Beginbot: Vue, React, (ember)
Long Form Beginbot: What are the companies you are applying for, what are they
looking for. Find 10, look at thier stacks, then choose.

## Begin Advice

## Stream Visions

## Stream Memories

## Programming Memories

## Begin Junior Advice

## Learnings

## Stolen Thoughts

## Begin Opinions

## Confessions

## Begin Trade Secrets

## Ponderings

## Musings

## Rants

If you really want to get a job fast:

- Outside of building as real skill as possible
- Its very important to look at your EXACT situation:
  - Where do you live
  - Who Hires
  - What companies are JR friendly near you
  - Where do Devs who do hiring hang out?
  - Whats the hot meetups in town
  - Can I start the hot meetup in town

If I was to hire Simplex as Junior:

You have 2 options:

- Vue
- React

- You get jobs from personal, indivualized, random interactions
- As you get more skills and social proof, these happen more

## Dark Side of Meetups

....Standing around akwardly
....do I just stand in that circle of others nerds
.....I don't know know what thier talking about
.....I don't get these jokes
.....I feel dumb

....Then you make one friend
....Meetup someone at the same spot as you

Something amazing Happens after 4th Meetup:

....YOU SEE SOMEONE MORE NEW AND AKWARD THAN YOU!!!!
....YOU WALK OVER AND MAKE THIER EXPERIENCE LESS AKWARD
    THAN YOURS!!!! THEY ARE SOOOO GRATEFUL, YOURE MAKING
    THE WORLD MEETUPS BETTER

## Begin Rants

## Work Goal

## Debates

People are different

Some people are real close with a big family
Others aren't
Begin is Not

I don't like people, who rely on thier family for things
I can't do this cuz of my family!!

Beginbot: Ya love ya family you wanna live with them
          ....if you don't
          ....then don't

Finding the right people to live with HARD
YOU BEST FRIEND MIGHT BE YOUR WORST ROOMATE

Things that Trigger Begin:

- When people say, I'll do this, once this X happens.
  X happens, family stuff

## Quotes

aquafunkalisticbootywhap: “nobody knows what they’re doing, and there’s two ways
to go with that. one is to be afraid, and the other is to be liberated, and I
choose to be liberated” - conan obrien

glitchybyte: I've interviewed and hired my share of people. The unspoken
questions I'm trying to answer are: 1. Is this person going to help me? 2. Do I
want to interact with this person every day?

beginbot: When shit hits the fan, is this who I want on my side

What matters, that we don't we test for interviews, is those late nights,
those tough bugs, those we haven't slept, do I want to murder.

Beginbot Bias: I rate more hyperactive higher, I incorrectly equate energy == passsion

Passion looks different to differnt people
People are different phases of their life.

2 Devs:

- One shes killing it  for 10 years, got a couple kids,
  not going to stay past 5 everyday and Volunteer
- Nother -> Young Begin, No Friends, No Girlfriend, No Hobbies, Lives Alone
              ..............UH YOU DIDN't ALL OF HACKER NEWS THIS MORNING???
              YOU DIDN"T FOR 20 Hours this week?
- 1st dev gettign more work, 2nd dev.....just dicking around being "passionate"

## Scraps

## Later

- <https://www.wikiwand.com/en/Greeks_(finance)#/Vega>
- <https://www.wikiwand.com/en/Pomodoro_Technique>

## Begin Daily Missions

- You want to be physically exashated at least for 5 seconds
- You Want to be really embarassed (in front of others please)
- You want your brain to hurt real bad, and to feel real dumb

## 3 Feelings You Should Strive

- Embarassed
- Dumb
- Tired

stupac62: @beginbot if someone that is an excel expert and business person asked you "what can you do with python?"
Would you tailor answer to things they do or try to explain that it can do everything?
Sometimes I think "everything" is not understandable by people with no CS experience.

Woah what can you do?
ANYTHING!!!!

....uh ok how?
You are forcing them to think of use case
then hope they as k how it would
