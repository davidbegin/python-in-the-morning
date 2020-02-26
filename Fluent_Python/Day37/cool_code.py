print('\033c')

print("\t\033[35;1;6;4;5mWednesday!!!\033[0m\n")


file_o_data.filter {|f| f.contains("FILTER")}.map {|f| f.upper()}


from dis import dis
import opcode

def chain(*iterables):
    for it in iterables:
        yield it

def cool(thang):
    yield thang


# all
# any



# I have a check for all

allowed_values = [0, 0.0, 7, 8]
g = (n for n in allowed_values)
print(any(g))


