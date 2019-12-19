print('\033c')

print("\t\033[35;1;6;4;5mBest Wednesday Ever! \033[0m\n")


from dis import dis
import opcode



a1 = [1, 2]
print(id(a1))
b1 = a1[:]
print(id(b1))


a1 = (1, 2)
print(id(a1))
b1 = a1[:]
print(id(b1))


t1 = (1, 2, 3)
t3 = (1, 2, 3)
print(t3 is t1)

s1 = 'ABC'
s2 = 'ABC'
print(s2 is s1)
