# Twitch / Vim Chat Integration

## How does this work

2 Commands written in python, expose them in my /bin:

beginchat

pulls the chat

beginbot

posts to chat

3 parts:

- Python programs
- Bash aliases
- Vim Shortcuts

vim-shortcuts

```vimrc
function! s:PostChat()
  let s:chat=system('beginchat')
  let @+ = s:chat
endfunction

:nnoremap <leader>tw :call <SID>SendToTwitch()<cr>
:vnoremap <leader>tw :call <SID>SendToTwitch()<cr>

function! s:SendToTwitch()
  let s:msg=getline('.')
  " Escape "'s or we won't be able to send lines with "
  let s:msg=substitute(s:msg, '"', '\\\"', '')
  let s:regexForUrl='[a-z]*:\/\/[^ >,;)]*'

  let s:uri=matchstr(s:msg, s:regexForUrl)

  if len(s:uri)>0
      let s:twitch_call=system('beginbot " ' .  s:uri. '"')
  else
      let s:twitch_call=system('beginbot " ' .  s:msg . '"')
  endif
endfunction
```

```vimrc
Fraq zft
<leader>tw

Copy last 5 msgs
<leader>tr

Search msgs
<leader>tu

Common Twitch chat commands
<leader>te

Create gist of whole file
normal mode <leader>gi

# TODO: Bug in visual mode
visual mode <leader>gi

Looks for and decrypts the last Rot13 messages
<leader>rr

# TODO: Create one that looks in the last 20 rot13
<leader>ra

# TODO: Create command to get last X messages

# TODO: Create command to search in Dmenu by User

# Handle links for Rot13

# Rot Detector
```
