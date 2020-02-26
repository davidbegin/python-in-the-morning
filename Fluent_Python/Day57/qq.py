def decorator_one(func):
    print("[1] decorator_one body")

    def decorator_one_inner(function):
        print("[2] decorator_one_inner body")
        function()
        print("[4] decorator_one_inner returning")

    print("[5] decorator_one returning")
    return decorator_one_inner


@decorator_one
def decorator_two(function, *args, **kwargs):
    print("[6] decorator_two body")
    # return function(*args, **kwargs)


@decorator_two
def blow_minds():
    print("Blow ya mind")




# print("[1] decorator_one body")
# print("[5] decorator_one returning")
# print("[2] decorator_one_inner body")
# print("Blow ya mind")
# print("[4] decorator_one_inner returning")

# [1] decorator_one body
# [5] decorator_one returning
# [2] decorator_one_inner body
# Blow ya mind
# [4] decorator_one_inner returning











# @decorator_two
# def function_one():
#     print("[7] function_one body")


# print("[1] decorator_one body")
# print("[5] decorator_one returning")
# print("[8] running function_one")


# [1] decorator_one body
# [5] decorator_one returning
# [2] decorator_one_inner body
# [7] function_one body
# [4] decorator_one_inner returning


# function_one()
# print("[9] done")
