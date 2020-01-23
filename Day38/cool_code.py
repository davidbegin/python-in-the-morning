print('\033c')

print("\n\t\033[35;1;4m22 Years ago \033[37mNetscape\033[35m announced \033[36mMozilla\033[35m on this Date!\033[0m\n")


from dis import dis
import opcode

# While with Else
x = True
while x:
    print("It's been a while!")
    x = False
    # break
else:
    print("Goodbye my sweet love")

# For with Else
l1 = [1, 2, 3]
for x in l1:
    print(x)
    # break
else:
    print("Bonus Round!!!!")


# Try with Else
try:
    print("We try")
    # raise TypeError
except:
    print("Except")
else:
    print("To win")

