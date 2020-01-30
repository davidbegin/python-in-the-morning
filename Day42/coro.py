print("\033c")

def subgen():
    print("Priming")

    while True:
        value = yield
        print(f"We got a new value all the way in the subgenerator() {value}")
        if value is None:
            break

    return "You can do it Peter"


def gen(results):
    while True:
        results["key"] = yield from subgen()


# is this technically a coroutine?
# When does something become a coroutine???

results = {}

gen_obj = gen(results)
next(gen_obj)

y = gen_obj.send(10)
breakpoint()





