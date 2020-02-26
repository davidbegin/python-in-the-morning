import timeit
import array

TIMES = 1000000

SETUP = """
from unicodedata import normalize

s1 = 'cafe'
s2 = 'café'
s3 = 'cafe\u0301'
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


print("\033c")
print("\t\033[35;1;6;4mLet's Time Some Stuff!!\033[0m\n")

clock("NFC  e:", "normalize('NFC', s1)")
clock("NFD  e:", "normalize('NFD', s1)")
clock("NFKC e:", "normalize('NFKD', s1)")
clock("NFKD e:", "normalize('NFKD', s1)")
print("")
clock("NFC  é:", "normalize('NFC', s2)")
clock("NFD  é:", "normalize('NFD', s2)")
clock("NFKC é:", "normalize('NFKC', s2)")
clock("NFKD é:", "normalize('NFKD', s2)")
print("")
clock("NFC  é:", "normalize('NFC', s3)")
clock("NFD  é:", "normalize('NFD', s3)")
clock("NFKC é:", "normalize('NFKC', s3)")
clock("NFKD é:", "normalize('NFKD', s3)")


# clock("NFC Shortening :", "normalize('NFC', s1) == normalize('NFC', s2)")
# clock("NFD Decomposing:", "normalize('NFD', s1) == normalize('NFD', s2)")
