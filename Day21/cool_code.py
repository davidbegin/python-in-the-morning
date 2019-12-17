print('\033c')

print("\t\033[35;1;6;4;5mBest Monday Ever!\033[0m\n")


from dis import dis
import opcode


import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

# This is a Decorator Factory
def clock(fmt=DEFAULT_FMT):

    # this is Decorator??
    def decorate(func):

        # Then what is this called???
        # this this *_args, the pythonista way?
        # wraps the decorated function.
        # is this an inner decorator???/
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)

            # HMMMMMMMMM
            # why
            # is this local only to the clocked closure???
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate

if __name__ == '__main__':
    @clock(fmt='{name}({args}) dt={elapsed:0.3f}s')
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)
