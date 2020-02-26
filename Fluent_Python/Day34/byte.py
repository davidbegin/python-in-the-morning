print('\033c')


print("\t\033[36;1;6;4;5mFriday Friday Friday!\033[0m\n")


from dis import dis
import opcode


# x = [x for x in range(2)]
# TypeError: don't know how to disassemble list objects

y = (x for x in range(2))

print("\n\ny = (x for x in range(2))\n\n")
print(dis(y))


# print(dis(y))
