# 2020 - 2 - 4

## Resources

OBS / Twitch-chat / vim integration

automatically allow:

- VIPs
- Mods
- Subscribers

Mode for allow all, during BRB

Adjust the sound affects to work on all scenes

Make an easier soundbank set:

- trigger soundaffects multiple
- easy pipeline for pulling in soundaffects
- personal soundaffects
  - Everyone cheers when Will shows up

### Maybe Additional Schedule

M - F | 6AM - 9AM
Saturday | Afternoon or night stream
2 or 3 days for night streams
T,T,F -> 6PM - 8/9

/raid fullstacklive

### Current Begin Strategy for Non-Burnout

- Do whatever I want on stream
- Make sure we don't work on the stream all the time off stream

- <https://www.wikiwand.com/en/Osborne_1>

Form a Mysterious Label:

- Aesthetics

./hit_machine

Wolves
minor=true
bpm=80

Input:

- Minor or Major
- BPM
- Search Term
- (Band Name)

Steps:

- Generate the song midi
- Generate the song wav
- Download images for the search
- Generate separate album art images
- combine the albums art images into a video plus music

Output:

- Music Video

```bash
fluidsynth --quiet -a pulseaudio -g 5 -m alsa_seq -l \
  -i /usr/share/soundfonts/FluidR3_GM.sf2 -F ooh.wav -F save_file.mp4

ffmpeg -i audio.mp3 -i video.avi video_audio_mix.mpg
ffmpeg -i flute_jam.wav -i test.mp4 video_audio_mix.mp4
ffmpeg -i violin_jam.wav -i space_whale.mp4 violin_music_video.mp4

ffmpeg -i input.mp4 -ss 01:19:27 -to 02:18:51 -c:v copy -c:a copy output.mp4

ffmpeg -i input.mp4 -ss 00:00:02 -to 00:00:04 -c:v copy -c:a copy output.mp4

ffmpeg -r 2 -f image2 -s 1920x1080 -pattern_type glob -i '*.jpg' -vcodec libx264
\ god.mp4
```

## Micro Goal

- Clean Markdown

## Bounties

## Questions Viewer

gottzstreams: @stupac62 well if you don't need it, don't use it. i just started
mentioning it because beginbot could have done that rather than quitting ranger
and using cd to get into the same exact folder gottzstreams: ¯\_(ツ)_/¯ i'm on
windows 10 right now though dougthecoder: @GottZStreams Don't worry, I'm also
cursed to live in the Windows ecosystem LUL gottzstreams: hm. well i use arch on
6 servers.  gottzstreams: hm. well i host a chat rpg game with 500k players on
arch

## Viewer Questions

sweeku: what does midi stand for

## Questions

## Learnings

man identify
man pv

## Ponderings

levinson2504: Apollo mission craft used some insane specs

## Opinions

## Debates

## Advice

You need someone who will code review and approve your jokes
Dev-Shopping
QA-Shopping
It's ok for jokes

> usuallyhigh: Laravel does too much for you and uses a lot of bad practices.
> It's nice to get started but if you need to use a framework, use Symfony

gottzstreams: btw one reason why i'm on windows right now: nvidia gottzstreams:
problem about the proprietary driver for nvidia cards (pretty much the only
choice if you want to game) when doing hibernation (s2disk) it will not dump the
gpu ram into swap gottzstreams: when you come back up, your qt windows will be
broken due to flushed framebuffers

## Things I don't want to explore, but maybe some else should

- Docker not on Linux
  - Docker on Mac
  - Windows

## Confessions

- One of the main working reasons I switched to linux, was Docker
- Mac at work
- Dockerized Microservice, plus all these other fake Dockerized Cloudservices,
  Streams, Databases
- Docker for Mac
  - Destroy your battery
  - Burn your legs
  - Go sooooooooooo slow

## Cool Stuff

hazeanderson: the MIDI spec went unchanged for nearly 40 years

## Python Interview

## Quotes

## Scraps

## TODO

- Create different classes/levels of gifs and soundaffects you can trigger
- AFK mode, where everyone can control

dougthecoder: There's a composer, David Bruce that tried to recreate a piece of
electronic music using a live orchestra - brilliant.

sadukie: Have you guys seen the music21 Python library? We can analyze MIDI
files with it... oh this looks sweet.
sadukie: <https://www.kaggle.com/wfaria/midi-music-data-extraction-using-music21>

- Create generate generic link markdown

sadukie: If you're looking for a not-so-expensive way to get into algorithms,
look into "Grokking Algorithms" from Manning. Much cheaper than college.

gottzstreams: you know you can spawn a shell from ranger right?

gottzstreams: hm. you could pipe stuff through pv to see some progress
gottzstreams: Server = <https://archive.archlinux.org/packages/.all>

```vimrc
" ------ basic maps ------
"
" move visual selection up/down line at a time
xnoremap <silent> K <Esc>'<kdd'>pgv
xnoremap <silent> J <Esc>'>jdd'<Pgv
```

<https://trac.ffmpeg.org/wiki/Scaling>
<https://drama-sans.github.io/drama-sans/>

baldclap: how about gettting a sentiment from the song then doing color efects
based on different moods
usuallyhigh: And I have been scammed, once again
gottzstreams: identify -format %wx%h bla.png will output the size as described
by the format argument. 800x600 for example
