import pytest
import collections

import pdb; pdb.set_trace()

class ArithmeticProgression():
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step  = step
        self.end   = end

    def __iter__(self):
        # numeric coercion rules of Python arithmetic
        result = type(self.begin + self.step)(self.begin)

        # Something you have to Rememebr about forever
        # Sometimes Forever ends
        forever = self.end is None

        # Personal Opinion, index = 0 feels like Python
        # code smell

# Option #1
# instead of simply incrementing the result with self.step iteratively,

# What: I opted to use an index variable and calculate each result
#        by adding self.begin to self.step multiplied by index

# Why: to reduce the cumulative effect of errors when working with with floats.
#      floats are annoying, this helps enforce consistency
#     float math pathological

#     These errors will effect you system?

        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            # 0 + 1 * 0 = 0
            # 0 + 1 * 1 = 1
            # 1 + 1 * 2 = 3
            result = self.begin + self.step * index

def test_with_int():
    ap = ArithmeticProgression(0, 1, 3)
    assert list(ap) == [0, 1, 2]

def test_with_half():
    ap = ArithmeticProgression(1, .5, 3)
    assert list(ap) == [1.0, 1.5, 2.0, 2.5]

def test_with_fraction():
    ap = ArithmeticProgression(0, 1/3, 1)
    assert list(ap) == [0.0, 0.3333333333333333, 0.6666666666666666]

def test_with_true_fraction():
    from fractions import Fraction
    ap = ArithmeticProgression(0, Fraction(1, 3), 1)
    assert list(ap) == [Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)]

def test_with_true_decimal():
    from decimal import Decimal
    ap = ArithmeticProgression(0, Decimal('.1'), .3)
    assert list(ap) == [Decimal('0.0'), Decimal('0.1'), Decimal('0.2')]
