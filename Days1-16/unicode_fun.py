print('\033c')

print("\t\033[35;1;6;4;5mBlack Friday\033[0m\n")
# print("\t\033[35;1;6;4;5mBest Friday Ever!\033[0m\n")


from faker import Faker
from dis import dis


from unicodedata import *
import unicodedata


from unicodedata import normalize




import unicodedata
import re






import os
print('\t\t†\u033C\u0342\u034D')
print("\u00b5")
print("\u03bc")



# print(os.listdir('.'))
# print(os.listdir(b'.'))

# pi_name_str.encode('ascii', 'surrogateescape')



# import sys
# print(sys.maxunicode)













# import re

# re_numbers_str = re.compile(r'\d+')
# re_words_str = re.compile(r'\w+')
# re_numbers_bytes = re.compile(rb'\d+')
# re_words_bytes = re.compile(rb'\w+')

# text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
#             " as 1729 = 1³ + 12³ = 9³ + 10³.")

# text_bytes = text_str.encode('utf_8')

# print('Text', repr(text_str), sep='\n  ')
# print('\nNumbers \d+')
# print('  str  :', re_numbers_str.findall(text_str))
# print('  bytes:', re_numbers_bytes.findall(text_bytes))
# print('\nWords \w+')
# print('  str  :', re_words_str.findall(text_str))
# print('  bytes:', re_words_bytes.findall(text_bytes))

















# re_digit = re.compile(r'\d')

# sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

# for char in sample:
#     print('U+%04x' % ord(char),
#           char.center(6),
#           're_dig' if re_digit.match(char) else '-',
#           'isdig' if char.isdigit() else '-',
#           'isnum' if char.isnumeric() else '-',
#           format(unicodedata.numeric(char), '5.2f'),
#           unicodedata.name(char),
#           sep='\t')














# import locale
# import pyuca

# coll = pyuca.Collator()

# fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
# sorted_fruits = sorted(fruits, key=coll.sort_key)

# print(sorted_fruits)






















def shave_latin_marks(txt):
    norm_txt = unicodedata.normalize('NFD', txt)

    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue  # ignore diacritic on Latin base char
        keepers.append(c)
        # if it isn't combining char, it's a new base char
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)

s1 = 'café™\u035B'
# print(shave_latin_marks(s1))


# print(unicodedata.combining("Z"))
# print(unicodedata.combining("\u0301"))

# unicodedata.combining(c)
