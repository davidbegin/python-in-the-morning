import timeit
import array

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 100000

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


SETUP = """
import re
import reprlib

RE_WORD = re.compile('\w+')
class IterSentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.finditer(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word


s1 = Sentence("Time to master yield")
s2 = IterSentence("Time to master yield")
"""


clock("finditer(): ", "next(s1)")
clock("findall(): ", "next(s2)")
