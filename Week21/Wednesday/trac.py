import sys

def tracer(frame, event, arg):
    print(frame, event, arg)
    return tracer

sys.settrace(tracer)

breakpoint()

x = len([1,2,3])

# breakpoint()
