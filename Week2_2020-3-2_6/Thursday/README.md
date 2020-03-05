2020 - 2 - 5
============

Viewer Reviews
==============
- vivax3794
  - https://github.com/vivax3794/BCrushPy
- stupac
  - Regex Review
- isidentical
  - https://github.com/davidbegin/pysandbox
- elremingu
  - Talk about terraform


Stupac
======
in the help, doesn't specify the Regular Expression Engine
- maybe not important because we are in python

- why did we choose this particular python shebang

Skywalk:
========
- use separate files for logical groupings of functionality
- make is obviously, where the entry point to our app is,
  as well as the most impotant logic
- you have a life long journey of how to break things into separate files
- ask yourself, do these methods need to live with other methods?
  - are they related?
- Begin Advice: I want you to go module crazy
  - Next one, I should be saying, woah too many small files
- I wanna learn how I should split apart a JS project:
  - Start with How to split
  - Go overboard, and notice when you've gone overboard, thats you learning
    when to split!
  - Where to split
  - Module to Module comunication should be a focus


Meta Code Review
================
- Backup to look at the overall shape and structure
  - squint test: searching for rocketships
    - high level overvieew looking for code smells
    - one huge file
    - super nested code
- if you see something that could be multiple ways, or its done in a way you don't typically do,
  ask!
  - Sometimes you learn some awesome new info
  - you make the person question their own choices
    - junior reviewing senior technique
- Leave comments on stuff you like! With emojis!
- Non-Blocking versus Blocking
- Do I spend time QAing/Testing my code reviewed code:
  - If I am going to have to support it in production,
    ideally I want to QA.
    I am seeing how errors look as I operate with the system.


Resources
=========
- https://www.wikiwand.com/en/March_5
- https://www.python.org/dev/peps/pep-0582/




Terraform
=========


- How we divide out TF state
- How it structred  for inputs and ouputs, is it DAG?
- How are we handling , plan, apply approval, promotion logging around going
  from dev-stage-prod

- The Basics:
  - Are you saving state somewhere remote
  - Are you running Terraform locally?
    - If you are on a team you need to stop, get it somewhere remote


- Blast Radius
  - How are you splitting grouping your state

  - You start with a single terraform state:
    - DB
    - Servers
    - Queues
    - Buckets
    - Alerts

  - One day you need to update a simple alert:
    - and it takes 10 mins, calcuate the state of the others
    - There is a chance you could affect something you don't
    - When I update an alert, I want no risk of deleting the databse
  - As your TF grows you will keep splitting more and more, based on blast radius


Split a single TF Project into Stacks:
- Top-Stack -> Create Roles and Policies that all other stacks want
  - Top-stack has to be run first
  - outputs needed by other stacks
|
v
- Down-Stream -> Server-stack uses those policies
- read in the remote state from the upstream-stack
   - consolidate all remote state reading into one place
     - see your dependencies
- Before out creating


- Inputs and Outputs
  - If you are splitting your state, what are the dependencies of the units to each other
  - What is your pattern for handling remote data?

- How are you handling multiple envs?
  - How are you handling the config
  - Terragrunt?
  - Deployments? Promoting from Stage to Prod?

- How are you handling plans and approvals
  - Are we saving the plans
  - How do we know who approved
  - do we split planning and applying
- Terraform can't actually handle dynamic for loops
- Can you Tear your Terraform down and put it back up?


Do you need Terraform?
======================
- Are you deploying code? Then YEs
- Declare what infra you wnt,  and it will figure out the API calls
  - Infrasttructure in code
  - under version
  - Deploy to another env, trivial
  - taking down and putting trivial






Bounties
========



Hot-Tip
=======
- in Slack or Discord, make a channel called #naming-things-is-hard
- Leann vim while learning something else hard new
  - then you don't need to type fast, cuz you don't understand anything
  - Change OS, Framework, Language, Paradigm


Viewer Questions
================
- What is a Github Code Review?
  - Reviewing your profile, as if you are a canidate whose
    resume came across my desk
- What the heck is dependency injection?
  - Java and Angular
- How do I organize my code in a convential/idiomatic way?
  - It really depends on language
  - Domain
  - Type of project
     - OS Project
     - CLI Tool
     - App
  - Framework:
    - Ember
    - React
    - Vue


- Bebotebe:
  - Make this runnable without the API need
  - Add tests/olerf tests that we can comparison


Questions
=========

- Why use Dict versus dict for typing
   - Dict we can be more specific, we specific the type of the Keys and Values

Learnings
=========

Ponderings
==========

Opinions
========

- As you TDD - Test drive your code, it affects the design
  - it forces you separate dependencies and inject to get isolated

Debates
=======

Confessions
===========

Predictions
===========
- eventually every key will be custom
  - Dream: describing each key should be like J Peterman produce

Python Interview
================

Quotes
======

isidentical: pythons packaging isn't the best one because of linux distros packagin python packages in their own package managers

Scraps
======


TODO
====
- Acquire a ZX81


Saturday: Typescript and Haskell Nerd - 10 AM PST
  
Javascript was shipped after 2 weeks
  - this affects language evolution
Hasklee was shipped after 10 years
