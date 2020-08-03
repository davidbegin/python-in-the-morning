# Studying the Holy Texts

## Revelation

The localleader


:help isfname

```
:iabbrev @@    steve@stevelosh.com
:iabbrev ccopy Copyright 2013 Steve Losh, all rights reserved.
```


sello

-- 
David Begin
https://davidbegin.com 
nice cool


:nnoremap <leader>" viw<esc>a"<esc>bi"<esc>lel

viw
a"

  "hello"


---

:nunmap

:nmap dd O<esc>jddk

# Setting Secret Marks

I want to set a mark in a vim remap script,
but not use a named mark,
which of the "Special Marks should I use"

- " <- Last cursor location on exit
- ^ <- The last jump
- `` <- the true last jump

Store the last cursor location

## What's wrong with you Begin

- how do you navigate back to the last jump, in a word

---

:echo verus :echom

:echom saves in :messages

! is toggle
`:set rnu!`
? show the status

## Underused

- :set number?

<space>
<CR> Enter
<c-d> Ctrl+d
<c-R> Ctrl+R

## Modes of Mapping

nmap
vmap
imap


## Remapping in Insert Mode

- Typically you're typing, so you don't want remap any keys you'd type,
  so it's important to remap in insert mode, with something like CTRL
- It's important to escape if you are creating maps in insert mode

Normal Mode is where you spend most your time.
However, if we start a movement, to hang out in Visual Mode,
Would that become normal mode? and what does the old normal mode
become

- Insert Mode -> It's like Tanning <- You can't be in there too long.
  - but sometimes you got to hang out in there, for like 30 mins,
  just to get a base.


imap <c-u> <esc>Ui

  Set up a mapping so that you can press <c-u> to convert the current word to uppercase when you're in insert mode. Remember that U in visual mode will uppercase the selection. I find this mapping extremely useful when I'm writing out the name of a long constant like MAX_CONNECTIONS_ALLOWED. I type out the constant in lower case and then uppercase it with the mapping instead of holding shift the entire time.

Set up a mapping so that you can uppercase the current word with <c-u> when in normal mode. This will be slightly different than the previous mapping because you don't need to enter normal mode. You should end up back in normal mode at the end instead of in insert mode as well.
