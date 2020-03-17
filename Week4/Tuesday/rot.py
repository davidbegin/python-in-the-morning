cleartxt = "berlin"

abc = "abcdefghijklmnopqrstuvwxyz"

abzb_abznq: Here is some text.
secret = "".join(
    [
        abc[(abc.find(c)+13)%26] for c in cleartxt
    ]
r
