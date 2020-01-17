from dis import dis

y = (x for x in range(2))

print("\n\ny = (x for x in range(2))\n\n")
print(dis(y))



# y = (x for x in range(2))


#  14           0 LOAD_FAST                0 (.0)
#         >>    2 FOR_ITER                10 (to 14)
#               4 STORE_FAST               1 (x)
#               6 LOAD_FAST                1 (x)
#               8 YIELD_VALUE
#              10 POP_TOP
#              12 JUMP_ABSOLUTE            2
#         >>   14 LOAD_CONST               0 (None)
#              16 RETURN_VALUE
# None

