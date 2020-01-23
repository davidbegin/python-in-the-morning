# import random

# def d6():
#     return random.randint(1,6)

# # We give iter a function that takes no arguments
# # and be called repeatly
# # 2nd arg == when the result of the first arg == 2nd arg
# # StopIteration!
# d6_iter = iter(d6, 7)

# # for roll in d6_iter:
# #     print("\033c")
# #     print(f"\t\033[35m{roll}    \033[0m")



# matches = ["hearts", "bar", "cherries"]

# def pull_the_level():
#     return random.choice(matches)

# slot_machine = iter(pull_the_level, "cherries")

# for gamble in slot_machine:
#     print(gamble)





import types
e1 = range(100)
next(e1)
l1 = list(e1)
breakpoint()

g1 = (x for x in e)

# range is not a generator
# why?
# because its not one time consumable

print(type(e).__mro__)
print(type(g).__mro__)
print(isinstance(g, types.GeneratorType))

# Range = lazy iterable
