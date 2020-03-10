# 2020 - 3 - 10

Computer Science We Never Learned - Sockets, IRC, TCP, UDP, OSI !schedule

nc -l -p 5000

## Meta-Goals

- Change the narrative: Vim ain't hard it's Fun

## Resources

- <https://www.wikiwand.com/en/Dot-com_bubble>
- <https://realpython.com/python-sockets/>
- <https://dev.twitch.tv/docs/irc/guide>
- <https://docs.python.org/3/library/socketserver.html>
- <https://tools.ietf.org/html/rfc1459.html>
- <https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?&page=6>
- <https://www.wikiwand.com/en/IPX/SPX>
- <https://www.wikiwand.com/en/Inter-process_communication>
- <https://www.wikiwand.com/en/Internet_Relay_Chat>
- <https://www.wikiwand.com/en/Internet_protocol_suite>
- <https://www.wikiwand.com/en/Transmission_Control_Protocol>
- <https://www.wikiwand.com/en/Transport_layer>
- <https://www.wikiwand.com/en/Unix_domain_socket>
- <https://www.wikiwand.com/en/Inode>
- <https://www.revsys.com/tidbits/dataclasses-and-attrs-when-and-why/>
- <https://www.howtogeek.com/465350/everything-you-ever-wanted-to-know-about-inodes-on-linux/>
- <https://github.com/satwikkansal/wtfpython#-strings-can-be-tricky-sometimes>
- <https://www.guru99.com/tcp-vs-udp-understanding-the-difference.html>
- <https://blogs.bmc.com/wp-content/uploads/2018/06/osi-model-7-layers-804x1024.png>

## Bounties

- Example of open source use of selectors
- Build the game - symlink farm manager
- Webserver in R???

## Viewer Questions

- sultantw: why Vim ?
  Begin: I wanna stay in the command line, cuz it's
        fun and cool.
        Its installed on every *nix machine!!!!!!!!!
        At one point we all have to use vim:
          - You'll be on a remote server
          - someones else computer
          - some OS without a Desktop env yet

- amrhossam96: what programming language you think works best for backend development
  - learning or working
  - What kind of problem are you solving
- amrhossam96: managing databases and handling requests
  - Python, JS (Node), Ruby, Elixir, Go
    - Which one of these makes you the mose excited
    - The happiest
    - The most curious

- OGJake: How did you get smooth scrolling like that
in vim? Mines choppy when going up and down on pages

- Swirling: how can we test something's security effectiveness?

## Questions

- Archtype: A command that returns None on success
  - Never assign the output, since erroros will bubble, unless you wanna try

- What are suitable uses for select:
  - Personal project:
  - Work:

- Whats the diff betwee NamedTuple and SimpleNamespace
- isidentical: SimpleNamespace is kind of an internal
data structre so I dont suggest you to use it

- should we always just revc(1024) and that default is just good.
bzzzt_bzzzt: packet length can be up ot 2^16 - 1

## Learnings

- bzzzt_bzzzt: tail recursion is how functional languages
have state, a monad is the structure that makes it explicit

sel.register() registers the socket to be monitored with
sel.select() for the events you’re interested in.
For the listening socket, we want read events: selectors.EVENT_READ.

dethkn1ght: i think that is the standard payload after you
strip off the lower frames so each one is 1024 of application data
dethkn1ght: for a 1544 frame

TCP:

- Order Guaranteed
- No Data Loss!
- Efficent - confuses begin
  - less code?
- HTTP
UDP:
- metrics
- streaming
- DNS
- connectionless
- timeseries - we don't need time guarantees if the data has time encoded in it
- SCTP:
  - SOCK_SEQPACKET:
- VoiP
- This is when we need to gaurentee the delivery of the whole message

Neither have security guarantees

- SCTP provides additional security features that TCP and UDP do not.
In SCTP, resource allocation during association setup is delayed
until the client's identity can be verified using a cookie
exchange mechanism, thus reducing the possibility of Denial of Service attacks.

Never replace TCP for UDP just for security.

The API for Unix domain sockets is similar to that of an Internet socket,

- What is different in Internet and Unix Sockets

but rather than using an underlying network protocol,
all communication occurs entirely within the operating system kernel.

Unix domain sockets may use the file system as their address name space.

- When would you use the filesystem when would you use a bonus linux namespace?

(Some operating systems, like Linux, offer additional namespaces.)

Processes reference Unix domain sockets as file system inodes,

so two processes can communicate by opening the same socket.

## Ponderings

- Disk1of5: i can't wait for the day where linux uses a unified package manager
- TCP - Reliable
- UDP - Fast (unrealiable)
  - Have you seen a UDP packet dropped
  - Always UDP jokes making fun of unrealiable

- Disk1of5: i can't wait for the day where linux uses a unified package manager

## Opinions

HazeAnderson: I think IDEs are crutches that prevent
you from truly memorizing the syntax and available lib
functions of the language you are using

bzzzt_bzzzt: off-topic I think more people in tech need
to learn about social sciences and philosophy

The best trick/life-hack is to convince everyone you're an idiot:

- People are nice to you when you don't know things
- People want to teach you stuff
- People aren't intimidated by you
- No Expectations

isidentical: dataclasses is the best module in the stdlib

HazeAnderson: conspiracy theory for the day ---
silver is tied to gas -- if gas goes up, silver goes up ...
hence why silver has been suppressed, to keep oil prices
artificially down

## Debates

- Is TCP more secure than UDP?
  - dethkn1ght: if no encryption it's all unsecure
  - bzzzt_bzzzt: its not security it is, authentication
  - <https://security.stackexchange.com/posts/165645/revisions>

## Confessions

## Python Interview

## Quotes

## Scraps

## TODO

- <https://www.youtube.com/watch?v=0kXaLh8Fz3k>
- Update Dotfiles
  - GNU Stow
- The idiot brain
- <https://www.youtube.com/watch?v=MCs5OvhV9S4&feature=youtu.be>
- Greatly improve asciicibe program
