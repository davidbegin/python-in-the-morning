# 2020 - 5 - 4

## Workflow improvements

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

### Begincerns

- Burnout
  - Don't want to start missing morning streams.

## Bash Fun

How do I extract out all soundeffect requests?

```bash
cat logs/chat.log | grep "\!soundeffect" | sort | uniq > tmp/soundeffect_requests.txt
```

## GOALS

- Simple README to get chatters started
- Requests System Build
  - Look for repeat requests
- Sharing needs to increase it by a lot aswell. Maybe more than stealing.

## TODO

- Refactor SoundeffectRequest
- Finish Requests interface
- Add Quick Command to Delete Soundeffects and Requests DB

## Code TODO

- Fix godaamn None Problem
- Keep Working Through Random for all Commands
- Make snorlax package
- Normalize Volume
- Make sure all are in a DB transaction
- Rename and rethink Perms parser

## Me

6 AM in LA remixes of Donkey Kong Country
Always do M-F
Starting a Satuday Stream -> Covid messed it up, and I am have been lazy

## Text TODOs

- Update help to include Twitch Clip

## Top TODO

- A quick way to flip my mode, God -> Peasant
- fix help command for aliases
- rescue around unallow and allowuser
- create a bug tracker
- fix requests
- Everyone gets access to certain sounds for free, for a limited
- Add SFX Health
- update presentation, for new commands

## Bugs

## Videos

- Video Explaining Different Parts of the Process
- Street Cred VS Cool Points
- Dependeices Rant
  - Dependency is simple combo of other deps
  - it gets out of date
  - you are chasing down how to update it
  - you are not learning what it does

## View Questions

spartangtr: so if your company runs entirely on serverless, do infra people even
exist there? this is another problem i have with the "cloud everything" approach

A: Yes, me
300 Lambdas, 50 queues, 50 streams, DynamoDB, RDS, S3
Managed in Terraform
CD rolling updates
40 Environments

AWS Versus GCP Versus Azure, based on similar principals
The AWS specific part is small.

Cron, Serverless

tramstarzz: not much ,searching for some rule engine for java or if someone have
some recommendation
tramstarzz: but i am not sure why we dont make our logic instade of using some
rule engine

Rule Engine:
-> an high level abstraction where someone can pass configuration
    for different workflows
-> In Java theres a ton of "products" for Rules Engines
  -> How broad of rules are they applying to
  -> Rules Engine, thats built around Deploys
  -> Rules Engine built around Sales

hanycodes: okey, quick question. I'm trying to write a script that takes some
input and outputs an ffmpeg command. Any idea how can I use python to add input
into the ffmpeg command please ?

python ffcmd_writer.py -v "cool_vid.mov" -e do_something ->
ffmpeg -i cool_vid.mov
youtu7be-dl

Q: How do you download Youtube Clips and Make Them available?

A: `subprocess.call a script`

Someone sends a !soundeffect request, with the youtube id, command name, and the
timestamps

!soundeffect Kg34JLKUTlk cool 00:01 00:04

We save this request in a Database (JSON file)

Then we have another Bot, looking for approved requests (STREAM GODS can approve
requests)

Soundeffect Request Bot ->  Takes the request, constructs a set args to pass
to another script, that other script calls ffmpeg

<https://github.com/kkroening/ffmpeg-python>

## Serverless

Deployment of the bots:
  -> Buncha Lambdas,

## Think We Fixed

## Refactor

## Resources

## Ponderings

The Bot:

5 Separate Bots

- One Bot for collecting the chat, process commands (saving requests to a
  database)
- Soundboard bot, playing sounds
- Soundeffect Request Bot -> taking user requests
- One bot -> Hand of the Market, gives chatters street cred and sounds
- Stock Ticker Bot

No Dependencies:

- TinyDB -> Small lil ORM to use JSON as a Database
- TinyRecord -> Transactions for TinyDB

## I need code and data hosted somewhere

Servers
Databases
data Lakes
Queues
Streams

## Memories

S3 Outage day
Developer Snow Day
PDX -> Drinking in the day

4 or 5 years ago

What the biggest outages:

Config issues are typically the biggest outages

You can never truly test config, Stage and Prod.

## Bounties

## Viewer Questions

## Questions

## Learnings

## Ideas

## Guitar Lessons

## Opinions

spartangtr: i dont understand everyones boner for serverless
-> ETL
-> Cron Jobs
-> Lazy PRocessing (Images, Videos)

## Debates

$7,000 a Month

Begin is willing to bet money, you could get one,
host others websites, up charge and make money

## Advice

Q:  How do you learn to not drop a production Database?
A: Drop a production Database

## Rants

## Working Through Emotions

## Confessions

## Quotes

## Scraps

## AWS TODO

Look at Appsync Graphql Backnone updates
