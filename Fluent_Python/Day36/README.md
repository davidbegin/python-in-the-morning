2020 - 1 - 21
=============



Viewers
=======

aiur100

Question: Is it stupid to have a single handler lambda function as an abstraction to do CRUD options on a "resource"?

 So it just used one endpoint? /resource/{resourceName} If GET and primary key is available return data. If POST and body is avaiable create. If PUT and body is available and ID then Update? You would just abstract any requirements for each resource in module abstraction for each resource. i.e. VideoGames, get, create, update delete. Sorry for the huge question.,



API Gateway or ALB -> Lambda

GET /dogs
POST /dogs
PUT /dogs

### Option 1:

def lambda_handler(event, context):
	# handle all HTTP Methods
	# inspect the request, and figure out
  # the verb and the location


### Option 2:
	def get_dog():
	def post_dog():
	def put_dog():

-----


Q: Should this even be a Serverless (or Lambda) or should it be a traditional server?

Questions We Need To Ask:
	- What is the latency expectation????
		- Sooo GD dang its wild - You don't want Serverless
	- What is the Request/Response Type:
			- Async: Serverless
			- Sync: We need to ask more question





-----



usertwitchuser
	- product architect / software architect.
 		but need some guidance in system design

What does this mean to you?

What does software architect mean??
	Options:
		- You design the high-level architecture for a team to execute
			(this could be any balance/ratio of implementing)



Questions:
---
	* How big is the team?
	* How big is the company
	* How much are you implementing?
	* Whats the breakdown of the team?
		- Juniors, Seniors, Contractors, Interns
	* What space are you?
		- Cloud Native
		- On-Prem
		- Startup
		- Enterprise
		- Do have to Hippa, PCI, or financial services
	* Type of business
		- high demand, performance heavy
		- Location Sensistive
		- Data Intensive


We need generic system design-help:
	* Books you should read
		- Books on Enterprise Architecture
		- Chaos from Netflix
		- Google SRE guide thing
		- O-reilly
		- Designing Data-Intensive Applications
	* Meetups with other people in the field, to talk and share
		- Someone will save you months of work, from a chat saying don't go down that route
	* Find a mentor, open source projects, Discords and Slack, Streams
	* Podcasts, Youtube Videos
		- Podcasts find people with your job, and listen to their experience
			- Software Engineering Daily
			- Changelog Podcasts
		- Youtube - Conference Talks
	* Build smaller subsections of architecture to experiment things



















Python Interview
================
	* What type of object is range and why?
		Why is range NOT an Iterator?

		range does respond to the next() method
		range is consumable multiple times, without being exhausted
		this is confusing, because range is lazy, and range is an iterable

		lazy iterable, or a lazy sequence










Quest
=====

Pep Hunters
---
  * find the PEP where map, filter, reduce where set to built-in

Questions
=========
	* Does a generator every store its full sequeunce in memory,
		Begin's Guess: No, unless you explicitly convert its type (AKA to a list).
									 otherwise, using `x for x in generator`, is streaming the
                   input

	* Is Range a Generator???


Generator Function
	-> has yield, so it returns a Generator object


Generator object


iterators are lazy iterables

Iterables return Iterators
Iterators are also Iterables, because __iter__ returns self, which is an Iterator,
Lazy iterable. Iterators are lazy


Range is a lazy iterable
	-> well its a next method



Question: so range() knows that list() is being called on it,
 					so it converts itself to an iterable?


list method is ask the object, hey do you have __getitem__, __iter__,
use those methods to build out the sequence in memory, until its
hits StopIteration





Question: sometime can you talk about how you use sensitive data in code? Like where to put urls and keys that are sensitive so it's not exposed to the world?

Configuration should always be environment variables
If its a secret, it should be encrypted
if its a secret, it should never be commited to Github, so we have the classic
secret, how do you introduce the secret.

Local:
	- Type in once at the command line somewhere
Deployed
	- manually store it somewher once in AWS, paramter, secrets manager

Worship the 12-Factor, Architect
	- memorize the 12 factors, getting experiences with the 12 factors,





Opinions
========

YOU HAVE TO LEARN VIM AT ONE POINT
DON'T BE SCARED DO IT NOW


Should you Read Gang of Four?
	- Is there alterantive in your language
	- Ruby - Design patterns in Ruby, its GOF minus patterns you don't need anymore

It won't code better right away. But its good to recognize the patterns in their orgiinal form,
and be able to use the language everyone uses, ITerable and ITerator are first referenced there.

At one point you should read it. But when?
You're getting paid, you you're bored











Learnings
=========

mro = Number.__mro__
Method Resolution Order
If you have a Class
You can see the order of classes python is going to look for a method defint
ion on.
Ruby = ancestory tree, method lookup


Ponderings
==========
	* SRE
		- Site Relibility Engineer is an Actuary?
		- SRE , DevOPs, Chaos Engineers is Actuarial Science?


In software, we love to steal other fields terms,
Im an engineer, architect, Actuary science boy



Do you mock out S3 Services:
	- Option 1 - Moto AWS Server
	- Option 2 - Record and playback calls Placebo


Placebo:
	Pros:
		- You can ensure things work against real calls
		- You can rerecord calls to make sure they are up-to-date
		- You can run generally with AWS
		- Supports everycall obviously, since its recording
	Cons:
		- Figuring out when you record, recording drift can happen
		- where do you store the records?? (These are huge JSON blobs),
      commit them???


Moto:
	Pros:
		- Never Connect to AWS
		- Don't have to figure recording calls from AWS
	Cons:
		- It only supports 33%
		- You can't use it everywhere, and often has large gaps
		- If you working on newly relesed AWS features, support will take a while
		- Moto can drift from AWS (maybe we shouldn't worry about that)
		- Run Moto Server







History of Deploying
---




We need some hardware, buy it, rack it, stack it, boot it, shoot it.

Companies hey you rent some space on our hardware!
Hooray!
How??
	- Use this great website

CLI - aws cli
SDK - boto

build a database
build a queue
give the database permissions to put things on the queue
We have to figure the exact right order of how to do things
and thats whole life.

Cloudformation + Terraform
	- Dependency Resolution for Infrastructure

Gimmie Database
Gimmie a Queue that can read frmo the DB
Gimmie a stream

YOU figure out the order!!!!

This is not code, this is configuration.
its not a full language on purpose,
since its a not a full language, we can figure out the dependency tree

Pulumi + CDK
---
	* Abstractions on top of Terraform and Cloudformation,
		- that lets use our programming lang of choice:
			- Python
			- Typescript
			- Go
		- but handles that dependency resolution
		- also provides abstractions for larger pieces of infrastructrue.
		- Example: Gimmie an API Gateway
								- would build out like 10 resources




Code
v
Config
v
Code

































Debates
=======

Scraps
======

