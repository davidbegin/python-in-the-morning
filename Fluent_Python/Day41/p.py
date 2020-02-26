print("\033c")

# RESULT = yield from EXPR
breakpoint()


yield from averager()

# These are generators.
# Which are Iterable
_i = iter(EXPR)

try:
    # this should already be primed at this time???
    # this it the last yielded value of the subgenerator
    _y = next(_i)
except StopIteration as _e:
    _r = _e.value
# This happens on success of try
# which is counter intutiive to our typical thinking of else
else:
    # This is Psuedo Code
    while 1:
        # assign the yield to _s nd return the _y
        # _y => subgenerator yielded value
        _s = yield _y
        try:
            # _i -> Is the delegating generator
            _y = _i.send(_s)
        except StopIteration as _e:
            _r = _e.value
            break

RESULT = _r 
