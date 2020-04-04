# 2020 - 4 - 2

## Resources

- <https://github.com/kkroening/ffmpeg-python>

## Story

Begin wanted OBS-Websockets Plugin

- I installed this yesterday, crashing all the time
- Updated OBS no crashing!
- This allows us to trigger Things from vim

## Goals

- use FFMPEG to combine album art into a music video

```bash
ffmpeg -f image2 -i tint-Ka_Statue_of_horawibra.jpg-1585461490.074048 zzz.mp4

ffmpeg -f image2 -i %.jpg zzz.mp4

ffmpeg -r 2 -f image2 -s 1920x1080 -pattern_type glob -i '*.jpg' -vcodec libx264 -crf 25  -pix_fmt yuv420p god.mp4

-pattern_type glob

fluidsynth --quiet -a pulseaudio -g 5 -m alsa_seq -l -i /usr/share/soundfonts/FluidR3_GM.sf2 -F ooh.wav
```

```bash
ffmpeg -i audio.mp3 -i video.avi video_audio_mix.mpg

ffmpeg -i flute_jam.wav -i test.mp4 video_audio_mix.mp4

ffmpeg -i violin_jam.wav -i space_whale.mp4 violin_music_video.mp4
```

stupac62: <https://www.arj.no/2018/05/18/trimvideo/>

```bash
ffmpeg -i input.mp4 -ss 01:19:27 -to 02:18:51 -c:v copy -c:a copy output.mp4
```

```
ffmpeg -r 2 -f image2 -s 1920x1080 -pattern_type glob -i '*.jpg' -vcodec libx264 god.mp4
```


!ahh

- cut up that clip, wyp -> cut the clip -> with ffMPEG
- tentative hook up of chat to obs

## Bounties

## Viewer Questions

plzcompile: does _variableorfunction_name mean it's private and __variableorfunction_name is protected in python?

_ = is not actual private, its a naming convention for private
__ = does do name-mangling, but you can find and access the attribute to
     the mangled

__ = dunder

Short Answer: Yes
Long Answer: No

## Suggestions

stupac62: You should make a Ex command so you can do :tw mypy and it send mypy
to twitch chat. so means source so can't use that
stupac62: just like how you save a file with an Ex command (:w)
stupac62: that way you don't have to mess with the actual file
stupac62: to send message to twitch

kidshenck: Is percent not a reserved character in zsh?

## Questions

## Learnings

## Ponderings

## Opinions

pinkflufflyllama: gitlab is horrid

usernamesarelame: if you dont have freedom coz of your gf, its your fault
hannylicious: Another pour-over coffee fan I see! *high five*
usernamesarelame: :) 
usuallyhigh: I like Microsoft, fight me
usernamesarelame: same 
usernamesarelame: fuckin balmer

## Debates

## Confessions

## Python Interview

## Quotes

## Scraps

## TODO

!idk

stupac62: Is there a vim noun to represent python function block?
stupac62: So I can ya[python block]

```python
Traceback (most recent call last):
File "bot.py", line 64, in <module>
run_bot(server)
File "bot.py", line 50, in run_bot
send_msg(resonse)
NameError: name 'resonse' is not defined
```

- Better ways of pulling chat messages out, dmenu??

We need to save an audio file from the midi file
or can we add a midi file with ffpeg


```
)[swscaler @ 0x557f6e7b4a40] deprecated pixel format used, make sure you did set
range correctlyx
    Last message repeated 5 times
    []
```
