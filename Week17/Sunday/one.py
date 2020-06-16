def cool_func(func):
    def inner_func():
        print("Im on top")
        func()
        print("Im on bottom")
    return inner_func

@cool_func
def other_method():
    print("do stuff")

other_method()
