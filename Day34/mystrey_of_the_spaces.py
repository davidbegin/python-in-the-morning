print('\033c')

print("\t\033[36;1;6;4;5mFriday Friday Friday!\033[0m\n")


from dis import dis
import opcode

import re
import reprlib

RE_WORD = re.compile('\w+')


# We are making this class an Iterable:
#   - because it returns an Iterator

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return

    def iter2(self):
        for word in self.words:
            yield word



s1 = Sentence("Time to master yield")

i1 = iter(s1)

print("__iter__ with the return\n")
print(dis(s1.__iter__))

print("2 NO return\n")
print(dis(s1.iter2))



# import pdb; pdb.set_trace()








