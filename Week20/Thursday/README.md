# 2021 - 7 - 2

teej_dv: so you can do "setlocal omnifunc=v:lua.lsp.omnifunc" or something like that

_write
_update
_update_table

When did a method dissapear from git

I could write a test, looking for the method
then Git Bisect

updating _last_id to _next_id
https://github.com/msiemens/tinydb/commit/7c1525f603ca597a9e28399c9c1b27ee65cc3a36

Adding _write
https://github.com/msiemens/tinydb/commit/c3124bd8252db404cdf16aba32eb6548badbe002#diff-39a9058e96fc9f9802408d2493c165ad


Removing _write
https://github.com/msiemens/tinydb/commit/50d0cd831761c3959f95cb72a4f9978f75bad493

update _read to _read_table
Should we rely be relying on an "private" method
https://github.com/msiemens/tinydb/commit/128ee57a63d02d948ecaca0c61ef5daaf3a349b7


```python
   data = self.db._read()
   AttributeError: 'Table' object has no attribute '_read'
```

```python
self = <tinyrecord.changeset.Changeset object at 0x7f05d6ffaf70>

  def execute(self):
      """
      Execute the changeset, applying every
      operation on the database. Note that this
      function is not idempotent, if you call
      it again and again it will be executed
      many times.
      """
>       data = self.db._read()
```


## Lets Be Adults

- Update to TinyDb 4
- Pull in the Branch of the TinyRecord update
  - Report any issues we get with TinyRecord PR
- See if we can get type errors stopped

## MyPy

### Questions
\os

unlucksmcgee: @beginbot Is it against the rules to use ML to recognise the pokemon cries Kappa
beginbot: if you already know how to do that, then NO!!!
          if you are learning about ML, then yes

- When would you use the `-c` command

```bash
mypy -c 'x = [1, 2]; print(x())'
```

!so teej_dv

teej_dv: builtin types are comments about code -- there is no runtime safety,
compile time safety, etc. mypy understands the types in a structural and logical
way. it gives you info about places where your comments lie

Q: What are the differences in module lookup between MyPy and Python itself?
  <https://mypy.readthedocs.io/en/stable/running_mypy.html>

First, mypy has its own search path. This is computed from the following items:

- The MYPYPATH environment variable (a colon-separated list of directories).
- The mypy_path config file option.
- The directories containing the sources given on the command line (see below).
- The installed packages marked as safe for type checking (see PEP 561 support)
- The relevant directories of the typeshed repo.

## Big Goals

Get people to stop reffering to Vi-variants as Vim
we should refer them to vi
Sometimes people ARE using vi and NOT vim or neovim

vi = visual

vim = vi improved

teej_dv: vi is very different -- it doesn't have vimscript, plugins, etc.
wantyapps: MEME: BIM
aciduk: vi = visual editor
dustarion: I first tried vim a year ago, still haven't figured out how to exit it
aciduk: its supposed to be "vi"sual editor apparently

## TODO

- Add insurance false to everyone in migration

### Breaking News

- Dev Leaderboard winner
- Homepage Winner
- Revolution And Coup
- Stealest Most Expensive Command

### Revolution / Peace / Coup

- We should only trigger news One
- Speed up the Wealth Transfer Commands
- Look into Triggering of Coup logic
- Upload Breaking News to the Website

### User Page Customization

- Allow turning Commands on and off

## Save Who Adds Sounds

## Resources

## Bounties

## Viewer Questions

## Learnings

## Ponderings

cachesking: i don't like relational data
cachesking: i have trouble with relationships
cachesking: im kidding a little here
cachesking: no. document store vs relational algebra
beginbot: Mongo?
pandapersonttv: hi
vexedkiller0071: pivot tables! FortOne
cachesking: you think relational algebra for mysql. you think... another math
for docdb. let me find the term

What are the problems thinking in one way (relational algebra) versus Math
(Math??????)

## Opinions

## Begin's Real Advice

## Begin's Unethical Advice

## Future Bar Trivia

## Debates

Do Snakes Eat Babies???

aciduk: a cat is objectively nicer than a python, so they've got that going for them
nicer means what???
cachesking: begin, i added a gitlab snippet in re to our RDS NoSql discussion

Do Snakes Eat Human Babies???

## Storytime

I worked  a bunch shitty jobs:

- H&M
- coffee
- taught guitar lessons
- Levis
- Radioshock -> reguarlly jobbed, or next store -> Dress Barn
- I never even leared how to activate sell phones

- you have act all professional, remove your personality
  I told myself I want a job wehre I can be wierdself 24/7

- After I worked at radio: Dodge Neon -> Micro -> 6 Guitar Pedals in the
  passanger
  - Microphone -> Delay, Reverb, Distorition, Pitch

1-4th Grade I sat separate from other kids
because I talked too much and was a bad influence

- Begin got banned from the Database admins....from adding more JSON in the
  postgres database. Not more HStore, NO JSON.

I wanna try Graph Database -> free-form gambling social system.

## Confessions

When I watch rw_grim, he talks about things OTHER than Git, and how programmers,
don't think there are any other VCS tools, or advantages.

## Quotes

## Scraps

```bash
curl https://mygeoangelfirespace.city/db/commands.json
curl https://mygeoangelfirespace.city/db/bot_votes.json
curl https://mygeoangelfirespace.city/db/breaking_news.json
curl https://mygeoangelfirespace.city/db/commands.json
curl https://mygeoangelfirespace.city/db/css_votes.json
curl https://mygeoangelfirespace.city/db/cube_bets.json
curl https://mygeoangelfirespace.city/db/cube_stats.json
curl https://mygeoangelfirespace.city/db/issues.json
curl https://mygeoangelfirespace.city/db/notifications.json
curl https://mygeoangelfirespace.city/db/play_soundeffects.json
curl https://mygeoangelfirespace.city/db/proposals.json
curl https://mygeoangelfirespace.city/db/rap_sheet.json
curl https://mygeoangelfirespace.city/db/sfx_votes.json
curl https://mygeoangelfirespace.city/db/soundeffect_requests.json
curl https://mygeoangelfirespace.city/db/the_fed.json
curl https://mygeoangelfirespace.city/db/user_code.json
curl https://mygeoangelfirespace.city/db/user_events.json
curl https://mygeoangelfirespace.city/db/users.json
curl https://mygeoangelfirespace.city/db/votes.json
```

## Rant

- I am morally against SQLite
  - WHO USES SQLite in production (I know people)
  - I would rather just use Postgres, and then if I end moving to the "Cloud",
    stay.
- Goal -> we want scaling problems, we want to CRAVE A new DB
  - Premature optimization is the root of all evil

## Later TODO

- Setup My discord my status
- ty rollin from mobiquity

## Early-Birds

- I got waking up early tips

- dustarion -> get some social pressure

Examples:

-  post a pic somewhere
- talk to someone to another timezone
- you want someone, whose going to say,......hey where are you???

- Fight 5 minute Begin -> You only want to get back in bed, for like 5 mins
make a routine, that takes more than 5 mins....of the easiest stuff to do.

go to bathroom
drink a cup a water
put on my hot water
turn on all my lights
turn on my computer
make my bed

IM AWAKE

- Don't wake up by alarm.

Choose the minimum amount of hours you want to sleep
and then if you wake up naturally in that window,
stay up.

You wake up 10 mins before your alarm, and go ohhhh! I can snooze for 10
You just  decided to torture yourself, becasue ya body just naturally woke
and you are changing the cycle.

---

Weekly List of things I'm Working on:


---

What are you going to get from an Arch Install?
Arch Wiki Excellent.

Be Patient, know you are learning and learning is hard.

Nothing worth doing is easy

12-hours
timeshift-autosnap
Adopt the Arch Mindset, updating things often, all the time.

I knew I was going linux, I knew eventually I'd like to,
do as much customized to myself as possibble.
So I said, I'm going to just suck now, and distro
I think I'd be using long
