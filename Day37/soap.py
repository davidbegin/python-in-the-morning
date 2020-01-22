def f():
    x = 0
    while True:
        x += 1
        yield x


# g = f()

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))



# ========================================================================================
def f():
    def do_yield(n):
	# do yield is a generator function
	# f is not a generator function
        yield n

    x = 0
    while True:
        x += 1
        yield from do_yield(x)

g = f()

print(next(g))
print(next(g))
# print(next(f()))
