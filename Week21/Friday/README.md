# 2020 - 7 - 10

## Get around in Vim

- Search by Filename
- Search by contents
- Go To Definition
- Keeping a file open, and backgrounding it, or splitting and focusing

ctrl-z and fg -> Background and reopen file

:vs -> Split current file -> then ctrlp search for new file
:vs -> Split current -> Go to Definition on another method or class

## 4 Distractions

- Wine   -> Drinking should be mostly always social
- Weed   -> Love Weed, can used to fantastic purposes.
- Wooing -> Dating is time-consuming and distraction
- Web    -> All Media, podcasts, youtube, reddit, twitter, social media, twitch

## Begin Approved Vices

- Smoke some weed -> Workout! Ride your bike! Read! Play Music, Write Music,
  write some code.
- Don't smoke weed -> Watch TV/Youtube

## Begin's Life

### Begin's Diet Rant

If you are changing your diet, find out what they make the best.
Don't just eat bullshit versions of the you used to like.

Both going for Keto:

Person 1: I Love pizza! I jsut a keto pizza
...pizza is mostly things you should on Keto
...if you get a pizza, it will never be as good.
Why not embarace whats awesome.

I eat "keto" icecream -> makes me mad, and makes me want REAL ice cream.

Person 2:

Steak Veggies -> Best Steak you've had. Tasty veggies.
If spend less money on "bad" food, you got more for good food.

All veggies are not grown equally -> you pay a little more for better
veggies, they actually taste better.

Once you quit sugar, everything tastes good again.

Certain Things I avoid typically:

- Dairy -> Very Sad, but Whole 30 unveiled it to me.
- Sugar
- Bread

Sous-Vide -> Joule
Steamer -> Cut some veggies, put a timer on, check everyone in a while.
Salmon -> Sear on top, in the oven 20 mins 400

2 years -> Went from 9AM -> 3:30

Stream starting 6AM Everyday
That means I go to sleep at 9PM
....timing can be hard.

...especially when I got a million things to do!

Everyone is different, you need to find what works for you:

- Do work for myself before Job:
  - Then when I get off work, theres not stress of, oh no
    now I have more work.

You won't ever love hopping out of bed early:

- It will become automatic and routine eventually

However, you will start feeling Goddamn amazing, with all the things you're
getting done, and the less stress.

zackariep: If you go to bed at a reasonable time, waking up early sucks less lol
beginbot: if you get "Quality" sleep, waking up is easier.
  if you sat on your computer for 4 hours, starting at terrible content.
  and then just role over in bed....thats good sleep.
  Drink yourself to sleep -> Not good sleep
  Drink some water, no electronics for an hour before bed.
  Maybe Meditate and Read. You'll fall asleep like a baby
  and wake up refreshed.

You're night routine is just as important as the morning routine.

## A Community

It's super hard to find a squad of programmers you like
hanging out with, that hype you up, motivate you
and make you think different.

AS Programmers we follow tribal lines.
...I'm pythonista....so I should just talk to Pythonista
you got to a meetup its all people who do the same as you,
but not YOUR people.

Maybe every language meetup, might have a potential best friend.

So Twitch is helpful for cross language, industry, age range communities.

If someone is an asshole to you, cuz you don't know about their language,
....just remember they are probably mean to everyone.

## Begin Grind Goals

- 5 Days of Week Today in History Podcast
- 3 Videos out a Week
- More Blogs

## Adding Types to our project

<https://mypy.readthedocs.io/en/stable/kinds_of_types.html#type-aliases>
You should types, at the most decoupled, lowest levels first.

---

No Jumper Interviews -> Soo many of the young amazing rappers,
have lived in multiple places.

Parents ain't perfect:
Begin Opinion: You should be teaching your kids, all the time.
Reading, Writing, Math, interacting with world

....if you let that up to school.....see what get

isaiahvander: begin I'm gonna throw a wrench in here. Hear me out: I think a lot
of people have really shitty world views (racist anti-intellectual southern
people in my experience) and i think a school environment provides a more
neutral, secular experience to help social people better to our common values as
a nation.

Racist Parents and Racist Friends make you racist.

## The Sad State of American System

We value kids fitting into a bare-minimum box of random learning
that only works for certain styles of learners and personalities.
Then we call all people who reject, dumb, lazy, stupid.

Versus:

Find out what a kid enjoys, finds interesting, is naturally talented at.
And give them resources to excel at that.

We will have more people happy in life, becasue they won't have heard
the message, ah you're not good, so your dumb.
Cuz the only to show your smart, is still and complete made up by someone else.

This is what the router returns:

```python
Optional[Union[List[str], str]]:
```

Whatever is returned from the router, is sent to twitch chat:

- None -> Do nothing
- str  -> send the str
- List -> send the list of strs

## Null Object

-> Templates

User Page:

user.name
user.email
user.age

What happens if we pass in Null user

Errors: None doesn't name  method
Errors: None doesn't email method
Errors: None doesn't age method

You go in the template: and you add if

if user:
  user.name
  user.email
  user.age

if the user is Null before we pass it to the Template:

Wrap it as a NullObject

class NullUser:
  def name(self):
    return "Please Login to see name"

Do you want more logic in your template?
beginbot's default answer is: No

## Null Opinions

trgwii: Do you have a preference / code style in terms of null / None vs actual
Option types?

Return null
return a wrapped null

I like the idea of a language with no Nulls

Another problem with "Null" -> it means so many things.

...so on one hand, I like separating Null from undefined...
...on the other hand....theres still sub-types for Null.

### Imagine a World with NO Nulls

- Think about what you would have to do in code
- How many of us, have found a bug, because we allowed null
  into the system, and then it got passed deeper down,
  where you can't have a Null.

## Philistines

- 5 A Week -> Me and Art Matt
  I used to read Wikipedia article for the day everyday.
  starting doing it on stream a while ago, and dropped
  as I got more viewers.

  5 Days, we review what happened that day.
  We record, crack jokes, publish. -> Trying to be 30-60 mins

## Today

- Keep adding Types
- Improve Revolution Coup System
- Make the website update faster

Folding Desires:

- Imports folded when opening a file.
- hide lines that start with inports

Can we write a neovim plugin -> That looks for groups of imports and folds

Reference in Lua: <https://github.com/tjdevries/manillua.nvim>

Can COC Help?

## Yesterday

## Resources

- <https://mermaid-js.github.io/mermaid/#/>
- <https://gitea.io/en-us/>
- <https://www.wikiwand.com/en/Regular_expression>
- <https://inventwithpython.com/cracking/chapter23.html>
- <https://www.wikiwand.com/en/Decorator_pattern>
- <https://www.youtube.com/watch?v=YR5WdGrpoug>

trgwii: Rich Hickey argues that Option / Maybe is not the right solution either,
and he has a good reason for claiming so, but he doesn't like null either (Talk:
"Maybe not" with Rich Hickey)

trgwii: Let's say you have Optional[str], and then you relax the API, you can
suddenly guarantee that you always provide it, so you change it to str

trgwii: Rich Hickey argues that should be a non-breaking API change

Begin: Writes an API, returns an optional str
Users: Consume API
Begin: Changes API, to always return str
Users: ....this is a breaking change
       ....yes, if before Null represetned a state,
          that you now have to determine from the string.

## Bounties

## Viewer Questions

## Questions

## Learnings

## Ponderings

## Experiences

one time, something heavy fell on the low keys, while I was on some ambient
setting. And I got freaked, I've been aducted once, so I thought it was
a twofer.

When you limit yourself to a small number of foods, you realize
you're not hungry that often. You more just crave Dopimine, a distraction.

I switched to Keto -> 4 years ago, to get more energy
working 3 programming jobs, working out.

I was one Soylet 0.1
-> Violently Ill

Soylet 0.7 -> Angry and sick all time.

70% of your food should be Vegetables for 95% of people
Begin doesn't care bout the rest.

Begin Veggies:

- Aspargus
- Brussel Sprounts
- Green beans
- Squash
- Carrots

We need to get some Facts on Soy

When we talk about and the body.....everyones different.

cachesking: not all veggies are equal. corn is shit
cachesking: i think it's more about the abrupt change in diet that affects americans.
cachesking: going from very little soy to drinks and powders is a huge swing

Whole-30: You feel great!
....and you find out, that all your favorites make you tired.

People that get bloated from eating vegetables are ususally not used to the
"healthy" amount of fiber. It goes over after eating the recommended amount of
fiber after few days.

alanturing1337: I recently quit caffeine by taking caffeine pills. I decreased
the total amount of caffein by like 20mg every third day until i reached 0 mg. I
did not have to deal with any extrem caffeine withdrawl. I recommend

## Opinions

Begin's Personal Opinions:

If you have trouble focusing on programming, and you think streaming will help
because of the social pressure to keep focused.
...what happens when you get viewers?
...now you get no work done
...Begin thinks it's better to figure out how to stay focused on your own.
Pomodoro Technique: <https://www.wikiwand.com/en/Pomodoro_Technique>

- Yes drugs do make you feel different things
......you should have exhausted all other routes first.
depending on a drug to get work done, is super scary.

I know people who don't need adderrall:
They need to:

- Exercise
- Have a regular sleep Schudule
- Stop Eating trash
- Meditate
- Read a Book
- Quite social media

isaiahvander: just for reference, i am prescribed these things, i don't just
take them for funsies, but i have found that they improve my quality of life
significantly

Saying you were perscribed something doesn't mean it's write.

Everyones attention spans are fucked
and drugs help us keep some attention

I couldn't sit still

3-5 I sat separte, because I was sooo distracting
....figuring ways to learn outside of school

stupac62: it's not normal to force kids to sit in a chair for 8 hours a day IMO

teej_dv: Haha, we are considering home schooling specifically ecause of that begin
phasen: CO legalized it right?
trgwii: <https://stackoverflow.com/a/1732454/2902799>
stupac62: <https://github.com/AlDanial/cloc>

phasen: public schooling was just to make good workers under American
Capitalism. It's been slowly changing but like everything in america two steps
forward 1 back.

teej_dv: actually it wasn't about American Capitalism -- it was modelled after
the Prussian (early Fascism) model.

## Debates

## Confessions

## Quotes

Acquired Tastes are a real thing  - Begin

You got to experiment.

Big Fan -> Small oily fish

## Scraps

## TODO

tinkernthink: I started David Reich's Who We Are and How We Got Here

Wray Colorado
1GB Colorado

## Company with too Meetings

- Say you will no longer attend meetings, without agBackground and reopen file

:vs -> Split current file -> then ctrlp search for new file
:vs -> Split current -> Go to Definition on another method or class

## Previous Experiences

-> I've always used an ORM of somesort
-> only don't use ORM, when it's fighting me to write a complicated
SQL statement, that I need for optimization

lunchboxsushi: but the one's i've seen like diesel but it's still quite
raw/string. and similar to golang from when I last checked it out

trgwii: or single-use scripts where single query is easier
ravonus: which a good ORM will give you an ability to just do a straight query.

Can we consolidate the location of Magic String?
Are these magic strings queries?
Enums -> Make make magic -> declared strings

lunchboxsushi: So if i have a

query select * from users -> within ef it's just
db.Users.Select(x => new User{}) with the properties you want

If you are using an ORM: you typically shouldn't be thinking about SQL
at all.

Thats the point of abstraction, not to think about SQL!

...now like we said earlier, any ORM worht it's salt, will let you
execute RAW SQL.......THIS IS ONLY AN ESCAPE HATCH

## DB upate experience

At my last job, we started with MYSQL with RDS python and SQLAlchemy

RDS released an update for the Postgres we wanted to use.

It took 1 develop, like a couple hours to make the switch.

I used to be a NoSQL on Acid Bad Boy

ravonus: to be fair it was fun and now I have a good code base so its doesn't
really matter now.

trgwii: how would you define "non-relational"? I feel like everything is
relational unless it's completely self-contained, like a buffer

lunchboxsushi: @beginbot if you're not going to enforce relationships on the
database you gotta do it on the server; Pro is that it's now in Git. Con is that
it's slower

- <https://github.com/typeorm/typeorm>

## What is difference Between a List, Array and Tuple

Tuples are immutable
List Versus Array -> Lists are dynamic in size

Tuple -> is a data-structure representing something
List and Array -> contain multiple of an item

User = (name, age, height)

User = [name, age, height]

Often Lists in python are called Arrays in other langauges.

Arrays are more when you are working with large amounts
of data, and you can about speed of things or size of thing or size of things/

----

When we can ensure an object has not been modifed, we eliminate
like 50% of bugs
