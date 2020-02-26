import pytest


from cool_code import Vector

def test_something():
    v1 = Vector((2, 3))
    v2 = Vector((3, 4))
    assert v1 + v2 == Vector([5, 7])
