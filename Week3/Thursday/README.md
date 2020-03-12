# 2020 - 3 - 12

Code Review / Resume / Github / Interview Thursday - Plus Arch Vim Tmux I3
Ricing

Code is a mix of art and science, learning what is "good" code is a life-long
debate. We are here to figure out what is the best attitude to learning, while
simultaneously presenting ourselves in the best position to make $$$$$$.

## Resources

- [GLITCH - A Synthwave Mix](https://www.youtube.com/watch?v=isIj3tuQTDY)
- <https://www.wikiwand.com/en/Simon_Newcomb>
- <https://www.wikiwand.com/en/Ernesto_Ces%C3%A0ro>
- <https://spin.atomicobject.com/2018/07/12/tiling-window-managers-macos/>
- [James Powell: Advanced Metaphors in Coding with Python | PyData Berlin
  2017](https://www.youtube.com/watch?v=R2ipPgrWypI)
- <https://mashable.com/article/chef-ice-seth-vargo.amp>
- [Hallelujah - Otamatone Cover](https://www.youtube.com/watch?v=x8hCe3j8CqU)

## Potential Code Review

- Youtube Markdown Vim Function
- LEvinson2504: <https://github.com/LEvinson2504/passportLogin>

## System Goals

- Kick off various chat commands, from i3, vim, tmux

## Bounties

- navigate through youtube links in markdown, and render a Thumbnail Preview
- stupac62: Didn’t chef steal code from that open source dev?

## Viewer Questions

- My autocomplete is slow what to do?
  - What is your current autocomplete
  - How does it work
  - What happens that autocomplete slow

- Disk1of5: I am working on a open source twitch bot and i am working on a way
  so it doesn't spam.. i want to write all messages to a MessagePool and have
  the pool send out the message but make sure there is a delay between sending
  messages... so im working on an async function that checks an array
  Disk1of5: the hurdle im having is creating the loop that checks the array

- My Programming Job? OR First time I got paid to programming
  - Free Lance
    - Blog
    - Webstore
    - CMS
    - Inventory Management
  - Subcontract
    - Rails sites with Desgin Companies
  - Contract to hire
    - Startups doing Fullstack
  - Hire
    - Go backend

- quadran7: What is a good way to go about removing embedded ec2 credentials in bulk?
- How many Ec2 instances?
- How are they managed?
- Can we rotate these credentials
- How emperhmal are there instances?
  - Multi-AZ 2 regions

## Questions

## Learnings

strager: vivax, I think that logger.exception outside an explicit except block is a bad idea. Pass exc_info explicitly.

BIGFATOROPERATOR is \|. It's called the alternation operator. In PCRE, it's plain |. It's escaped in Vim/ex because | is used elsewhere for general commands

- use :echomsg to explicitly write a message

## Ponderings

- Between Docker and Suckless
  - Docker - install nothing on your system,
  - Suckless - Source based configuration
  - This tug and pull is hurting me

## Advice

If you have a school, still make it look an open source.
Separate Repo, README, running instructions, License (MIT)

## Opinions

- If touching a mouse is bad, then touching a streamdeck is worse

- It is really easy to script AWS infra stuff, but it's a Trap!
  - Continually more error handling, case handling, determining the
    state of the system in you code:
  - Choose Your Fighter: Terraform, Cloudformation, Pulumi, CDK

- We should only practice practical comments, don't write comments
that wouldn't exist code

Code Commenting incredible value
Bad Comments incredibly damaging
We want to practice Good practices always

- Braintax for music is real

- Docker is a skill used for everyjob

## Debates

top rankings

ytop
htop
gotop
top

freedomdao: it's a very frustrating problem . Recently someone bought a
corporation that uses the platform i build with. they decided to use corporation
to try and kill the entire platform. 100s of us were building on it.

## Confessions

I haven't Puppet touched Puppet since I met Chef
I haven't touched Chef since I met Terraform

## Python Interview

## Quotes

## Scraps

## Music Suggestions

[1920s Dance Craze](https://www.youtube.com/watch?v=V6QK0xc3mmo)
 [McCoy Tyner  My Favorite Things](https://www.youtube.com/watch?v=yaPVbKglRu8)

## TODO

- fltrdr

## Vivax Twitchbot

- start with a README
- I don't like projects that start with the langauge
- sample_config.json
- config.example.json
- dotenv might cool to explore - very useful - 12 factor kids

for and else

if the loop finishes run the else, only feels right, if the loops goal
   is to find something
