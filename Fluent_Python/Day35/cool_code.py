print('\033c')

print("\t\033[35;1;6;4;5mI Have A Dream To Code All Morning!\033[0m\n")


from dis import dis
import opcode

import os


def unpack_or_index(t=(0, 1)):
    _, x = t
    x = t[1]

dis(unpack_or_index)

# 13           0 LOAD_FAST                0 (t)
#              2 UNPACK_SEQUENCE          2
#              4 STORE_FAST               1 (_)
#              6 STORE_FAST               2 (x)

# 14           8 LOAD_FAST                0 (t)
#             10 LOAD_CONST               1 (1)
#             12 BINARY_SUBSCR
#             14 STORE_FAST               2 (x)
#             16 LOAD_CONST               0 (None)
#             18 RETURN_VALUE




# Python 2
# 2           0 LOAD_FAST                0 (t)
#             3 UNPACK_SEQUENCE          2
#             6 STORE_FAST               1 (_)
#             9 STORE_FAST               2 (x)

# 3          12 LOAD_FAST                0 (t)
#            15 LOAD_CONST               1 (1)
#            18 BINARY_SUBSCR       
#            19 STORE_FAST               2 (x)
#            22 LOAD_CONST               0 (None)
#            25 RETURN_VALUE        
