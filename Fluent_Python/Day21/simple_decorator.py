print('\033c')

print("\t\033[35;1;6;4;5mBest Monday Ever!\033[0m\n")


from dis import dis
import opcode


registry = []

# # DecoratOR
# def register(func):
#     # __repr__ of the func
#     print('running register(%s)' % func)
#     registry.append(func)
#     return func

# # DecoratED function
# @register
# def f1():
#     print('running f1()')

# f1()








# Perf test set versus list in this context
registry = set()


# A Factory in this case is just a function
# that returns a function
# and this function happens to be a decorator
# which is a function that returns a fucntion?????
# So then what is the difference in a Factory and Decorator
# A Factory is producing a func, without really be supplied a function?
def register(active=True):
    def decorate(func):
        if active:
            print('running register(active=%s)->decorate(%s)'
                  % (active, func))
            registry.add(func)
        else:
            print('removing from registry: %s' % func)
            registry.discard(func)

        return func

    return decorate

@register(active=False)
def f1():
    print('running f1()')

@register()
# @register This don't work!!!!!
def f2():
    print('running f2()')

def f3():
    print('running f3()')
