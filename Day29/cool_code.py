print('\033c')

print("\t\033[36;1;6;4;5mFriday Friday Got Get Down on Friday!\033[0m\n")


from dis import dis
import opcode
import collections.abc

# __len__
#     sized -> ABC

class Durf():
    def __len__(self):
        return 0

d = Durf()

# isinstance
# isinstance and are checking against an Abstract Base Class
isinstance(d, collections.abc.Sized)


# If you build your own custom ABC,
# can you get this lookup behavoir, like Sized



# field_names = ["name","age","sign"]
field_names = "name,age,sign"

if isinstance(field_names, str):
    field_names = field_names.replace(',', ' ').split()

field_names = tuple(field_names)

print(field_names)
