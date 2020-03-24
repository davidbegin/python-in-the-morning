import pytest

from haskell2 import Sum, Product ,m_concat

# TDD - Test Driven Development
# Red - Write a failing test
# Green - Make it pass
# Refactor - Refactor code, while the tests still

def test_sum():
    assert Sum.append(Sum(107), Sum(1)) == Sum(108)
    assert Sum.append(Sum(107), Sum(1)) != Sum(109)

def test_sum_inquality():
    assert Sum.append(Sum(107), Sum(1)) != 1
    
def test_sum_id():
    i = Sum.empty()
    assert Sum.append(Sum(107), i) == Sum(107)
    assert Sum.append(i, Sum(107)) == Sum(107)

def test_product():
    assert Product.append(Product(107), Product(2)) == Product(214)

def test_product_id():
    i = Product.empty()
    assert Product.append(Product(107), i) == Product(107)
    assert Product.append(i, Product(107)) == Product(107)


def test_m_concat():
    xs = [Sum(10), Sum(15), Sum(20)]
    assert m_concat(Sum, xs) == Sum(45)

    xs = [Product(2), Product(5), Product(10)]
    assert m_concat(Product, xs) == Product(100)


def test_m_concat_with_empty():
    xs = []
    assert m_concat(Product, xs) == Product(1)
    assert m_concat(Sum, xs) == Sum(0)


