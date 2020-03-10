2020 - 2 - 9
============

Python sockets, netcat lsof ip ss, irc chatbot, Arch Linux, Man/Module Page Monday

Resources
=========
- https://www.wikiwand.com/en/The_Wealth_of_Nations
- https://realpython.com/python-sockets/
- https://tools.ietf.org/html/rfc1459.html
- https://dev.twitch.tv/docs/irc/guide
- https://www.wikiwand.com/en/Unix_domain_socket
- https://github.com/dylanaraps/birch/blob/master/birch
- https://www.wikiwand.com/en/Internet_Relay_Chat
- https://www.wikiwand.com/en/Inter-process_communication
- https://docs.python.org/3/library/socketserver.html
- https://www.wikiwand.com/en/Transmission_Control_Protocol
- https://www.wikiwand.com/en/IPX/SPX
- https://www.wikiwand.com/en/Fail-fast
- https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?&page=6

```
man socket

man netcat

man lsof

man ip

man ss


ss -at
# show all listening and non-listening connections for TCP

-p show Process


 lsof -wni tcp:65432 | grep -v PID | awk '{print $2}'

```

Bounties
========
- paid gaming companies did a thing that wrapped IPX/SPX over TCP.. allowing lan only games over the ineternet
  - I want a blog post, a youtube video, some more fun of that story

- a tool  for this: isidentical: I wish I can forbid all relative imports

Viewer Questions
================
- could you give some examples of what sockets could be used for besides a chat program? I know its a good way to show how it works but I keep getting a creative block when I try to think of other projects to use it in :/
  - Home Automation
    - Talking between your computers on your home network
    - your own personal dropbox
    - Games!!!
      - Multiplayer specially
    - OBS, interact with OBS
    - port scanner

- idevjoe: Is there a way to reject a connection, as if to refuse the connection and skip past it in the queue?
 - What do we reject on?
   - addr?
 - Whose job is it to reject connections:
   - router or firewall

- What is the equivalent of netstat -an in ip or ss

Questions
=========
- When would we not use -n for lsof

+|-w     Enables (+) or disables (-) the suppression of warning messages.

- Why in python 3.4 did socket objects() become no longer inhertiable

- strager: see /usr/include/asm-generic/errno.h or something. (I am not at my computer.)

- listen() has a backlog parameter. It specifies the number of unaccepted connections that the system will allow before refusing new connections. 
  - How do I determine a backlog number?
  - experimentation?

- What is there other than the BSD sockets API
- Why does SOCK_STREAM mean TCP
- My client never calls close(), but the program exits

- How do I decide how much data to recv from a client or server:
  - 1024
  - 2048

- send versus sendall
  - when would you send, versus sendall
    - cool lower level thingS?
      - extra logging around failures
      - Congestion and Saturation

- Should we specify AF_INET and SOCK_STREAM, when its the default?

- Why did we choose 65432?
  - non-privledged is above 1023
  - but why this specific number

- Why would we want our ports registered versus NOT for a socket application?
- register is like if you have a service on a server and want anybody to be able to connect to it, private ports are for clients so the server can respond, and they dynamically assigned

- Some systems may require superuser privileges if the port is < 1024.
  - Why would we want this


Learnings
=========

An open file may be a regular file, a directory, a block special file, a character special
       file, an executing text reference, a library, a stream or a network file (Internet socket,
       NFS file or UNIX domain socket.)

Counter: strager: processes are not files. FeelsBadMan process are files on Windows though. "everything is a file" is horseshit propaganda.

- strager: ifconfig and ip dont look at sockets, only network config and statistics. You wont find an equivalent to netstat or ss.


-n       inhibits the conversion of network numbers to host names for network files.   Inhibiting  conversion  may make lsof run faster.  It is also useful when host name lookup is not working properly.
- steve7411: It means it won't do things like convert 64.233.177.101 to google.com



- listen() creates a listener, waiting for new connections
- accpet() blocks are returns a new socket representing someone connected?

- private ports are 49152 to 65535
- you can register ports from 1023 to 49151

Why should you use TCP?
- Is reliable: packets dropped in the network are detected and retransmitted by the sender.
- Has in-order data delivery: data is read by your application in the order it was written by the sender.


Should you use TCP or UDP?
- Do you can about the order of data?
- Do you care about lost data?

Networks are a best-effort delivery system

Create listening server:
- socket()
- bind()
- listen()
- accept()


non-privileged ports are > 1023

cough* IPX/SPX protocol Kappa

“If you use a hostname in the host portion of IPv4/v6 socket address, the program may show a non-deterministic behavior, as Python uses the first address returned from the DNS resolution.


It's because the lower ports are typically used to common, registered things like http, https, ssh, telnet, file sharing, etc. The higher ports are considered ephemeral

If your server receives a lot of connection requests simultaneously, increasing the backlog value may help by setting the maximum length of the queue for pending connections. The maximum value is system dependent. For example, on Linux, see /proc/sys/net/core/somaxconn.


Ponderings
==========

Opinions
========

- I don't want to see a movie, until I'm in it.


- If you get option to choose ports, teach people about things your interested in:
  - 1987
  - 1917



- Programmers are scared to stream, cuz they don't know everything, prepared
  to teach - basically imposter syndrome


- Why make a python with no depedencies or libraries
  - beginniners get stuck on the depedencies
  - Too many files in library overwhelming
  - Simple instructions to quickly collect and send messages



We are programmers:
  - That doesn't mean we shouldn't shower
  - Don't plan on NOT going outside
  - Take care of yourself
  - Move around



Debates
=======

- Relative import worse or import * worse?

Confessions
===========
- I am torn up, on whether im happy I never got Starcraft, and Warcraft


- Someone said the only thing you need to be good at streaming:
  - talk non-stop
  - be excited
  
  - OMG - thats my whole personality

Python Interview
================

Quotes
======

> bzzzt_bzzzt: did he mention that monads are how haskell has mutability and state, I didn't see if he mentioned it

> bzzzt_bzzzt: monads can be the boundary between purity vs impurity of state

> amrhossam96: golden rule for programmers: don't call yourself an expert. just don't

> bzzzt_bzzzt: if you wanna practice being a streamer, buy a duck and talk to it when you program


> If its raining, just take off your clothes and bike - Beginbot


Scraps
======

TODO
====
- Read The Wealth of Nations
- Get better at vim-surrond or eat vim sandwich
- @beginbot there is a twitch app register they suggest using for "production" apps that provides new type of authentication password. 
- Memorize 65535
  - because TCP ports are 16-bit uunsigned bits
  - 65535 is 2^16 - 1
- Add a !SO @Streamer
  - Shoutout twitch chat
  - @ for autocomplete
  - @ for autocomplete
  - @ for autocomplete
