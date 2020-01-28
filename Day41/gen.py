print("\033c")


# Rule 1: subgenerator returns from the `yield from`
def subgen():
    print("Priming")

    while True:
        try:
            value = yield
        except TypeError as err:
            value = "Magic!!!!"


        if value is None:
            break

    return "You can do it Peter"


# I know how to return a value from subgenerator to delegating generator
# How  do you return a value from the delegating generator to the caller
#
# We we suggested passing in a Dict, modifying it,
# and then checking the results.
# Can we pass the data back directly
def gen(results):
    # yield from catches StopIteration Errors
    # similiar to how a for loop handles them
    while True:
        results["key"] = yield from subgen()


results = {}
gen_obj = gen(results)
next(gen_obj)
y = gen_obj.send(10)

gen_obj.close()
gen_obj.throw(GeneratorExit)
# Both of these trigger .close() to be called on the Subgenerator
# If no error is raised by .close(), then no error is raised.
# however, GeneratorExit will be propogated back up from Sub, to Delegating
# generator.

# gen_obj.throw(TypeError)
# wannaba_hello = gen_obj.send(None)
# print(wannaba_hello)
print(results)


# # Rule 2: this value sent to send, becomes the yield
# #         then is passed to yield of the subgenerator
# gen_obj.send(10)

# # Rule 2.1: if None is passed, the __next__ method of the subgen is called,
# #           and potentially StopIteration is called.
# gen_obj.send(None)


# (other than GeneratorExit)

# Exceptions thrown into the delegating generator are passed to the throw() method of the subgenerator.

# If the call raises StopIteration, the delegating generator is resumed. Any other exception is propagated to the delegating generator.




# If a GeneratorExit exception is thrown into the delegating generator,
# or the close() method of the delegating generator is called,
# then the close() method of the subgenerator is called if it has one.
# If this call results in an exception, it is propagated to the delegating generator.
#  Otherwise, GeneratorExit is raised in the delegating generator.


# # Begin' don't understand Rule 3:
# # return expr in a generator (or subgenerator) causes StopIteration(expr) to be raised upon exit from the generator.

