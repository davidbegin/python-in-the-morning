import string


print("\033c")

# Challenge: Make a datastructure with every two letter combination
# Points for:
#   - Cleverness
#   - Shortness
#   - Speed
#   - Readability


all_the_letters = string.ascii_uppercase

a1 = list(all_the_letters)


# create a list the length of a1, consisting only of a single character
# list(len(a1), "A")

def gen_letters():
    letters = list(string.ascii_uppercase)
    for letter in letters:
        for letter2 in letters:
            yield f"{letter}{letter2}"


g1 = gen_letters()
next(g1)

for x in g1:
    print(x)


# breakpoint()






