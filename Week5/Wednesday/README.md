# 2020 - 3 - 25

## Resources

- <https://www.wikiwand.com/en/WikiWikiWeb>
- <https://www.wikiwand.com/en/Portland_Pattern_Repository>
- <https://www.wikiwand.com/en/Ward_Cunningham>
- <http://c2.com/>
- <https://www.ladspa.org/>
- <https://www.oreilly.com/conferences/from-laura-baldwin.html>
- <https://system76.com/laptops/lemur>
- https://www.youtube.com/watch?v=MTr3tHWGv-U
https://youtu.be/tbKGjRoSofA?t=105


stupac62: brb. if you get off here is link https://www.twitch.tv/jesseskinner
*pinkflufflyllama:* now you need to make a neural network that detects rot13 and puts the messages in a file for you

levinson2504: HeyGuys HeyGuys HeyGuys
levinson2504: PogChamp PogChamp PogChamp
levinson2504: wakanda
andyjamesadams: Raid Drums

artmattdank: oooh
hazeanderson: Englebert Humperdink wrote all my fav hits :/
artmattdank: maybe up the volume?
stapotv: yeah, almost cant hear it

tsjost: midi bot? PogChamp there's a coding language called SonicPi specifically
made for creating music

## Bounties

## Viewer Questions

hazeanderson: I have some Arduino code that spits out binary in the form of
simplified MIDI ... and it ... works?

What is Extreme-Programming, XP?

The of Dream of Extreme:

- Meet with a customer
- Gather some requirements
- Write BDD, Cucumber, Acceptance Tests
- Intergration tests
- Unit Tests
- Pair making the tests

## Questions

How do I make the midi louder?

- Fluidsynth
- Midifile itself
- Pipe the fluidsyth output into something else, to make it louder

hazeanderson: 16 channels
hazeanderson: they are channels, not tracks
hazeanderson: tracks are what you record MIDI or audio onto

ls midi_files | xargs -I {} fluidsynth --quiet -a pulseaudio -g
9 -m alsa_seq -l -i /usr/share/soundfonts/FluidR3_GM.sf2 {}

What are these
       -G, --audio-groups
              Defines the number of LADSPA audio nodes

Why would I want to change the number of LADSPA audio notes?

2 Midi Files ain't playin:

- Theory: Same Range?
  Result: Busted

Theory: An issue with my fluidsynth pulseaudio setup
/etc/conf.d/fluidsynth
OTHER_OPTS='-a pulseaudio -m alsa_seq -r 48000'

-m options
'alsa_raw','alsa_seq','jack','oss'
Result: Busted, it ain't the midi-driver


This is the problem????
fluidsynth: warning: Failed to set thread to high priority

## Learnings

## Dreams

Begin Reads the Man Pages

## Ponderings

Emote-Wall: 3 and then it shows
          : move it one temporarily

CoolCat
CoolCat
CoolCat

## Opinions

usuallyhigh: <https://motherfuckingwebsite.com/>

## Debates

hazeanderson: Martin Freeman > Martin Fowler

## Confessions

## Python Interview

## Quotes

> "The best way to get the right answer on the Internet is not to ask a
> question; it's to post the wrong answer." - Ward_Cunningham (Cunningham's Law)

> "Bach be f##kin" - Begin

## Scraps

## Steps to Thought Leaders

- Law named after us
- Invention, section on your wikipedia
<https://gist.github.com/determin1st/ef6218cc544e2bb6a69c9b82ecdec84e>

## TODO

- Sonic Pi

andyjamesadams: Raid Drums stupac62: @beginbot apparently, this gives you much
more control over sound than alsa, etc. https://kx.studio/Applications:Carla
iScreaMan23 uses it stupac62: that's how I learned of it

- Check out the Zeal 
