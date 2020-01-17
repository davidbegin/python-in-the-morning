

Alot of Ruby is from perl

!? -> Last Error
All these special variables
Perl -> full of cool wierdos
Trend: make an image in perl code
string together the awesomest single line of code




import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0  4

    def __next__(self):
        try:
            word = self.words[self.index]  5
        except IndexError:
            raise StopIteration()  6
        self.index += 1  7
        return word  8

    def __iter__(self):  9
        return self
