import glob
import os

print("\033c")

with open("country_codes.txt") as cc:
    country_codes = set(cc.read().split())

gifs = set([ gif[10:12].upper() for gif in glob.glob("downloads/*.gif") ])
breakpoint()
# we want a list of all the Gifs in the downloads folder


# some fileutils to get all file names
