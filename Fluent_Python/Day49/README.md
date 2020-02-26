2020 - 2 - 7
============

Sweeku Project
===
- Scraping Out Cards from the Web

Python Survey
===

### Question: How do people manage their virtualenvs

Begin: `python -m venv venv`

# mkdirvirtualenv

I keep hearing: I used to use this, now I just use `venv`


ZeebZ: nix?????


Haze: Pyenv

#### Current Setup:
- Scraping into a JSON file

#### Interests In:
	- PySpark
	- Apache Spark

Where are we storing all this data?
- Lots of Data
- Unstructured

Why do we need to store this data?
- Faster to operate on data we don't have to fetch remotely
- Our data will already be normalized (make it look normal to you)
- Don't want to keep hitting the website and get blocked


### How do we choose our Database??
	- SQL
		- Pros:
			- Everyone uses SQL
			- its a computer base skill
		- Postgresql
			- Begin Choice
			- Aurora RDS Postgresl AWS™
		- MariaDB
		- MySQL
		- sqlite (Begin is mixed on this one, you wouldn't use it in production)
	- Document DB
		- Pros:
			- Already using JSON
		- Cons:
			- How are you gonna learn normalization
		- Document DB by AWS™
		- Mongo DB
	- Datawarehouse
		- Redshift
	- S3
		- Begin non-negiotable: You need S3
	- TinyDB if you want a local NoSQL type db.


We need an ETL Pipeline:
- Extract -> Transform -> Load

Sweeku -> Gimmie Cards Pokemon Site -> S3

We build out ETL:
	- take this raw data, extract this info out,
    transform (normalization) -> load into a DB of our choice

Why S3
======
	- 11 9s of durability
	- Intelligent Tiering
		- Tiers - You can pay less, but it takes longer to get your data back
		- AWS - will move them through the tiers based on their usage
		- for Data-Science, where its not accessing the data constantly, it gets
      real cheap

	- Its really easy to build ETL pipelines fast




What beginbot community need out of this?
===
- bold new analysis of pokemon





### Depends on the Dataset:
- Graph
	- AWS™ Neptune
- Example:
	- Social Network
		- this friend is friends with this friends who friends with those friends
- Open Questions:
	- do they work with Machine Learning





#### What are the hot Databases the python data engineers use?


Troll Option:
- Oracle
	- is it true they can't have Null
- SQL Server
- .txt








Thought Exercise
===
- avdi grimm
	- thinking about a world with no null value
	- Null Object Pattern


### Entry Example
```
Card Name:"Sobble - SWSH003" Set Name:"SWSH: Sword & Shield Promo Cards" Card Number:"SWSH003" Rarity:"Promo" Card Type:"Water" HP:"60" Stage:"Basic" Attack 1:"[1W] Bind (20)Flip a coin. If heads, your opponent's Active Pokemon is now Paralyzed." Weakness:"Lx2" Resistance:"None" Retreat Cost:"1" Market Price Foil:"$3.00" Median Price Foil:"$2.99" Url:"https://shop.tcgplayer.com/pokemon/swsh-sword-and-shield-promo-cards/sobble-swsh003" Scraped Date:"2019-11-18"
```


TODO:
===
- Start using assert in my non-python test code




The Plan
===
  - Saturday 10 AM PST - Build PC
	- Arch
		- If then if I panic PopOS
	- https://arcolinux.info/choose-your-project/
	- Get back to evoling into my final form
		- Neckbeard

  - Take the stuff  the confused me the most on stream
    try and understand better, then write up a blogpost/make dedicated
    video for that.


Core Takeaway
===
- You need a need for Async
  - don't mash it in, the complexity isn't worth it
- Typical Needs
  - Efficeny
  - Speed
  - Non-Blocking

Goals
=====
  - Learn about Asyncio
  - Have Fun

Viewer Questions
================
- stupac62: Anyone know how to get the character count of a line in vim? (other than g<C-g>

- are graph dbs meant to be acyclical?
	- one directionalm

- What is Zappa?
	- You have Django or a Flask App working all lovely lcoally
	- You want to deploy as a lambda
	- Zappa helps you take a Flask-like WSGI Restful app and turn it 
    into a Lambda, also helps you deploy to lambda, also helps
    you connect to various resources to your lambda.

Questions
=========

- How are Graph Databaes and Networking useful together

Learnings
=========

You can't use requests with asnycio.
you have to use `aiohttp`

also shouldn't do regular file manipulation
you sound use `aiofiles`

OF course you can't use requests with asyncio,
requests is built of urllib3
and urllib3 is built off of sockets
and sockets aren't awaitable
ok

Note: You may be wondering why Python’s requests package isn’t compatible with async IO. requests is built on top of urllib3, which in turn uses Python’s http and socket modules.

"By default, socket operations are blocking. This means that Python won’t like await requests.get(url) because .get() is not awaitable. In contrast, almost everything in aiohttp is an awaitable coroutine, such as session.request() and response.text(). It’s a great package otherwise, but you’re doing yourself a disservice by using requests in asynchronous code."
	- https://realpython.com/async-io-python/



aiofiles
===

I can write in files with just open right???

I/O file writing isn't truly blocking, because C python interperator knows
to Release the GIL






Open Job Position for Event Loop:
  - monitor coroutines
  - take feedback on what's idle
  - look for things that can be executed


By default, an async IO event loop runs in a single thread and on a single CPU core.
Usually, running one single-threaded event loop in one CPU core is more than sufficient.

It is also possible to run event loops across multiple cores.

Event Loop has two implementations
	- Based on selectors module
		https://docs.python.org/3/library/selectors.html#module-selectors
	- windows one


Potential Business
===
- I want to learn data-science
- I need data
	- test data ain't real data
	- I want dirty data
- you want you unique data

Avoid:
	- Taking the same data, and writing the same program against

You have two options:
	- Unique Data
		- It's hard to get this data
		- all your problems might become data collection and sanitation
	- Unique Analysis
		- This is harder, you should be learning the classics

Ponderings
==========

Opinions
========
-  Adults use: pathlib.Path(__file__).parent and joinpath()

#### When someone tells me theres an old style and new style:
- Who still uses the old style?
  - specific need to fine-tune control over the event loop management,
- Are there advantages to the old style?
- Who uses the new style?
- Whats the split of new stylers to old stylers??

Begin Big Pokemon:
===
- Red
- Blue
- Pokemon Snap

Styles of Pokemon:
- Scrapin`
	- you fight every battle to be almost dead
	- never train
- Zen lifestyle
	- stay outside of pallet, maybe veridian, and just kill
    ratattas and pidgeys until you level 99.
- Safari Zone
	- Two people enter the safari, catch some pokemon
	- Fight right after
- Personal Gym
	Cute Pokemon: Jiggly Puff, Wiggly Tff, Clarifiy Clafable, Eeevee


Hot Take
===
  - NPM did not learn from Ruby Gems
  - Anything is better than NPM


NPM is better, because its not global by default

Begin Opinion: NPM users are the most carefree when adding packages they don't need
  - DID WE LEARN NOTHING FROM LEFT PAD


When you are debating a Tool:
- The Tool
- The Community
  - if the community is all doing something dumb
  - thats the tools problem
      - unless people are really using your tool weird



where is Global installs a problem??
What community
what people???


Python Problems
  - virtualenv is confusing, advice is conflicting, things are influx
  - you have python installed on your computer already, and its needed 
    for lots of stuff.
  - you already python installed, and then homebrew installed another one,
    in a different location, and tried to update the default to be the brew one.



## All depedencies have to Code Reviewed
  - You actually start reading the dependencies code
  - you will start including a lot less 














Debates
=======
- Ruby versus Python for a total Noob

Confessions
===========

Python Interview
================

Quotes
======

I will need to learn all the stuff I don't know eventually
	- David Begin

very programming langauge is bad, and my favorite is the ones where
im most famiilar with the ways it bad.
  - brianlovreswords

"All lamgauges are bad...except whatever functional langauge im learning now"
- Zeebz91

Crates don't exists without Gems
  - David Begin


Ruby versus Python opinion:
  - both are fine for web
  - both are fine for internal tools
  - both fine for automating, devops
  - both can be fun
  - Ruby and Rails is a good path for a career, cuz you be
    real productive fast, lots of work
  - Python, we got data-science, we web, we got devops, we got AI


Which community appeals to you more?

If I was choosing:
  - Go to meetup for each language
  - Find a a podcast for each one
  - Find some projects in each one

And then see which one just feels more appealing, it gut feeling

Begin Opinion:
  - Gems > virtualenvs

tryruby.org


I learned vim and Ruby Koans at same time:
# Ruby Koans










Scraps
======


Ideas to Steal
===
https://libuv.org/
	- Big "Show Me the Code" Button on the Splash page

Fears
===

### Arch Fears
- I will be streaming on the Mac for longer

What are the opprotunities:
- First arch install is the hardest
- I will need to learn all the stuff I don't know eventually

Best Case Scenario:
	- I total fail, and struggle to get anything working
	- and I get a big list of areas I need to learn about
    for a practical reason

Other Projects
===

* OBS uses Websockets to interact with it's scenes programatically
  - send websocket requests and you can change scenes, mute stuff.

  - https://github.com/KirillMysnik/obs-ws-rc

  - Once the new computers up and running, we will return, hooking
    up our code to OBS


Problems
========

```
ClientConnectorCertificateError(ConnectionKey(host='1.1.1.1', port=443, is_ssl=True, ssl=None, proxy=None, proxy_auth=None, proxy_headers_hash=None), SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))

```


Facts
===
- certificate verify failed
- unable to get local issuer ceriticate


Open Questions:
===
	- Why do we need to send a local cert?
	- can we not require sending a cert?
	- Why does this not work for me right now?


Ignorant about:
===
- I don't understand SSL Really
- I don't understand the concept of a local cert

Other Certs:
	- come from an authority

Local Cert?
	- Is like Mac the authority?

I am trying to prove, that I am a real computer????

I am the site I am say I am, and lets encrypt traffic with this key?



Perf Results
===


regular file()
```
real    0m3.490s
user    0m0.672s
sys     0m0.110s
```

```
real    0m4.443s
user    0m0.705s
sys     0m0.110s
```



aiofiles()
```
real    0m3.328s
user    0m0.706s
sys     0m0.135s
```

```
real    0m3.678s
user    0m0.716s
sys     0m0.138s
```

#### Conclusion
- Either the example is too small to see differences
- Or the example is running in a way, not to take advantage of the asynchronous abilities of
  aiohttp
