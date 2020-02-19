
[1] decorator_one body
[5] decorator_one returning
[2] decorator_one_inner body
[4] decorator_one_inner returning
[8] running function_one
[3] decorator_one_inner_inner body
[6] decorator_two body

[7] function_one body
[9] done



def decorator_one(func):
    print("[1] decorator_one body")

    def decorator_one_inner(function):
        print("[2] decorator_one_inner body")

        def decorator_one_inner_inner(*args, **kwargs):
            print("[3] decorator_one_inner_inner body")
            return func(function, *args, **kwargs)

        print("[4] decorator_one_inner returning")
        return decorator_one_inner_inner

    print("[5] decorator_one returning")
    return decorator_one_inner


@decorator_one
def decorator_two(function, *args, **kwargs):
    print("[6] decorator_two body")
    return function(*args, **kwargs)


@decorator_two
def function_one():
    print("[7] function_one body")


print("[8] running function_one")
function_one()
print("[9] done")
