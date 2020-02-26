print('\033c')

print("\t\033[35;1;6;4;5mBlack Friday\033[0m\n")
# print("\t\033[35;1;6;4;5mBest Friday Ever!\033[0m\n")


from faker import Faker
from dis import dis


import locale

from unicodedata import *
import unicodedata



print("Z")









# s1 = 'café'

# Fat E
# clean_cross = '†'
# s2 = '†\u033C\u0341'
# s2 = '\t\t\033[31;1;5m†\u033C\u0342\u034D\033[0m'

# s2 = "\t\t™\u0362"
# s2 = "\t\t-\u035B"
# s2 = "\t\t.\u0363\u0364\u0365\u0366"


# print(clean_cross)
# print(s2)
# print("\n\n")


# s2 = 'caf™•ª¡´®†\u033C\u0341'
# s2 = 'caf™•ª¡´®†\u0336'
# s2 = 'caf™•ª¡´®†\u0334'
# s2 = 'caf™•ª¡´®†\u032B'

# Clean E
s3 = 'caf\u00E9'
s4 = 'caf\xE9'

s5 = 'caf\xcc\x81'
# s5 = 'caf\x3010'


# 0x301
accent = "COMBINING ACUTE ACCENT"
a = unicodedata.lookup(accent)
a = "é"
# print(hex(ord(a)))
# print(ord(a))
# print(bytes(a, encoding="utf-8"))

# print(s1)
# print(s5)

clean_e = "é"
fat_e = "é"

# print(ord(clean_e))
# print(ord(fat_e))

# print(bytes(clean_e, encoding="utf-8"))
# print(bytes(fat_e, encoding="utf-8"))




# print(bytes(u'\u0301', encoding="utf-8"))



# print(hex(ord(u'\u0301')))

# s1 = "é"
# print(hex(ord(s1)))


# print(s1.encode("unicode_escape")).hex()

# print(unicodedata.bidirectional("é"))

# print(s1)
# print(s2)
# print(s3)

# print(s2 == s3)

# # u"\u00E9"
# s1 = 'café'


# print(bytes(s1, encoding="utf-8"))
