def hello():
    print("cool")
    yield

x = hello()

next(x)
