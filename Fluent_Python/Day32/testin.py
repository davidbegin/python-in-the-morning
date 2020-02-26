import pytest

from cool_code import Vector
from cool_code import Vector2
from csv_parser import parse_csv

def test_adding_thangs():
    a = Vector([2,3])
    b = Vector([3,5])
    assert a + b == Vector([5, 8])

def test_a_list():
    a = Vector([2,3])
    b = [3, 5]
    assert a + b == Vector([5, 8])

def test_adding_a_list_to_vector():
    a = Vector([2,3])
    b = [3, 5]
    assert b + a == Vector([5, 8])


def test_adding_non_sequence():
        a = Vector([2,3])
        result = a + "ABC"
        assert result == NotImplemented


def test_using_not_implemented():
  a = Vector([2,3])
  b = Vector2([3,5])
  assert a + b == Vector([5,8])


def test_scalar_multiplication():
  a = Vector([1,2,3])
  assert a * 10 == Vector([10,20,30])

# @pytest.mark.focus
def test_scalar_reverse_multiplication():
  a = Vector([1,2,3])
  assert 1.0 * a == Vector([10,20,30])



@pytest.mark.focus
def test_reading_in_duplicate_csv():
    result = parse_csv()
    assert result == {
        "wrench": {
        "part_number": "abc1",
        "quantity": 1
    },
    "hammer": {
        "part_number": "abc2",
        "quantity": 7
    }
    }

