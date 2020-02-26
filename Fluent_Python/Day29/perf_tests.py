import timeit
import array

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 10000000


SETUP = """
list_field_names = ["name","age","sign"]
str_field_names = "name,age,sign"

def swan_method(field_names):
    if isinstance(field_names, str):
        field_names = field_names.replace(',', ' ').split()

    field_names = tuple(field_names)

def try_method(field_names):
    try:
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:
        pass
    field_names = tuple(field_names)
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


clock("swan_method list(): ", "swan_method(list_field_names)")
clock("try_method list() : ", "try_method(list_field_names)")

clock("swan_method str() : ", "swan_method(str_field_names)")
clock("try_method str()  : ", "try_method(str_field_names)")
