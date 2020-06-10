# 2020 - 6 - 5

!issue the random props gives how ever many you specify to 1 random person. It
doesn't give 1 to that many random people

## Chatter Tips

funksh0n: They return 405 on HEAD requests that return 200 for GET -.-

## Friday Goals

- Allow Users to start customizing their pages
- Reduce some noisey output
- Explore Whats the Worse that could happen:

## How Can People Customize Their Page

- Reference a URL for CSS
- Pull in File and upload
  - Curl a website, and reupload
  - Change the URL

Theory to why its not working:

- Different Domains for the CSS

Cascading Styles Sheets

## The New Holy Trinity

I      Geocities
II.    Angelfire
III.   Myspace

MyGeoAngelFireSpaceCities

- People to submit personal CCS to customize their page
- The Amount of CSS get, in lines, will be based on something:
  - Street Cred
  - Cool Points
  - Total Soundeffects

𓁿𓀍𓃢=2;𓅬𓍝=3;print(𓁿𓀍𓃢*𓅬𓍝)

## Bugs

Both our soundeffect request and submit new soundeffects JSON
got corrupted

We should limit to Full URLs

Certain Audio Files not playing
detlion1643: do you have any other programs besides mplayer to see if the file
is causing issues or it might be something codec wise with mplayer and
licensing?

stupac62: @beginbot something like this: Missing or invalid timestamps.
!soundeffect 0892jfss83 [00:05] [00:08]
stupac62: where brackets is what they replace

- Reduce donate,
- Reduce dropeffect,
- reduce street output

## Priority

- Keep Working on Beginworld Finance
  - Link for the people
- Fix Bugs

## Cube Rules

- If you guess right on the money you win a cube
- You can only win Once (I have 11 Cubezzz)

- Over 50s you get a mini Cube (2 Mini Cubes)
- 30s - 50s You get a Pretty Nice Cube (6 Regular Cubes)

- Sub 30s you get a Great Cube (2 Great Cubes)

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

## BeginWorld

## TODO

- Fix the betting interface:  looking at bets get mixed up.

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

## Code Refactors

- Decorators for route commands
- Better interface for models, returning, either a TinyDB object or our own
- Context Managers for Timer changing

## Resources

## Goals

- Never use a Windows product (Github, NPM aside (for now)) again.
  15 years clean.
- Never Watch Fake Movie again

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

## Bounties

## Advice

## Opinions

## Viewer Advice

qualitycoder: if you copy the libraries to the root of your project, when you
distribute it, no one will have to install it. When using an import statement,
Python first checks locally in the project, then in the computer install path.

More reasons that just ease of distribution, not use packages.

People grabbing tools before they know the problem

Packages are ok, But installing onethey should feel like drinking a glass of water
after wandering the desert for 40 years

Try and solve thigns simply yourself
see what patterns
then check out packages and they handle it
then compare it your way

attr_encrypted, ruby gem

it monkey patched 30 methods onto String.
This got into at work

......if this a in-house PR, it would have ripped to shreds
you package it up, NPM install, no one notices.

!css  https://gist.githubusercontent.com/davidbegin/efdbf338ecfcdc14fa9ed792c6056ed3/raw/d7bcdf2f3c9ae4b3e280646601061b0b4de3a2c8/beginfun.css

## Viewer Questions


## Stream Visions

## Stream Memories

## Learnings

## Begin Opinions

## TMUX Life Crisis

Split Conciousnous Life Crisis

Who should split what?

Window Manager
Termimal Emulator
Termimal Multiplexer
Editor

These can all "split"
If I can

- i3 -> DWM
  - DWM splitting is more intituative than terminal splitting
- ST -> alacritty
  - alacritty has Tmux splitting
    so do I drop TMux
  - stupac62: not sure if you saw, but I think alacritty-like splitting is for
    people without a tiling window manager
- vim
  - Could go harder on the VIM
  - :term

## Ponderings

Back in the day, everyones page was unique!!!
Woah Artmattdnk, got some nice new flames
Woah howd you get that Papa Roach right when I visited.

Now.....every site looks the same
every page looks the same
everything is just a cluster fuck ads and garbage.

## Musings

- NEVER BE AFRAID FROM CODE REVIEW
- WHATS THE WORST

- You were fired
- Looked at your code, looked back you, your're fired
  ??? has this even happened

- You look dumb someone
- beginbot: Oh know someone thinks I'm dumb

The best way to really instill the proper practices, protocols, fears
into someone around dropping a production database: Just Drop one.

gaddam: Great way to test your HA setup :D :D

if one person can take the company infra down, thats not that
persons problem, thats a company.
beginbot: Kinda drinking the policy as code koolaid
stupac62: That’s a management problem because a failure of processes

If you are going to program in production:
Best Advice

- Where do you live
- What big hats do people not wear there
- Wear that when coding in production
- New York -> Cowboy
- Cali -> Cheese Hat

- When you see someone with the Cheese:
  - They are in prod be respectful
  - They have a stupid, make fun of them,
    for coding in production.
  - The whole team can notice the frequency

- Whats the first public website that allowed people
to upload their own CSS

- Tripod

## Experiences

IT                 VS Programming
Personal Computers VS Servers

You think the majority of programming jobs on are windows?

Linux VS Windows
THERES MORE LINUX -> 78%
"Enterprise"

What field area etc.
West Coast Startups

Goverment
Transpration

Manfucturing Plants, Automated
OH MY GOD
Ripped off sold the oldest worst tech

I HAVE NEVER USED A WINDOWS COMPUTER
I DON'T HAVE PROBLEMS GETTING JOBS
.....I DON'T HAVE ANY FRIENDS IRL, THAT PRogramming windows

Unix 500 Commands

## Debates

## Quotes

"but most of all, Samy is my hero"

## Scraps

## Later
