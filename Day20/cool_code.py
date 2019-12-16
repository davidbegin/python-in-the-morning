print('\033c')

print("\t\033[35;1;6;4;5mBest Thursday Ever!\033[0m\n")


from dis import dis
import opcode



registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

# f1()
# f2()
# f3()

# def main():  8
#     print('running main()')
#     print('registry ->', registry)
#     f1()
#     f2()
#     f3()

# if __name__=='__main__':
#     main()  9
