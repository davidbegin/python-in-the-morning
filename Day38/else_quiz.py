print('\033c')

import pytest

def while_with_else_1():
    x = True
    while x:
        print("It's been a while!")
        x = False
    else:
        return "Goodbye my sweet love"


def while_with_else_2():
    x = True
    while x:
        print("It's been a while!")
        break
    else:
        return "Goodbye my sweet love"



def for_with_else_1():
    l1 = [1, 2, 3]

    for x in l1:
        print(x)
    else:
        return "Full Loop Bonus Round!!!!"


def for_with_else_2():
    l1 = [1, 2, 3]

    for x in l1:
        print(x)
        break
    else:
        return "Break Bonus Round!!!!"


def for_with_else_3():
    l1 = [1, 2, 3]

    for x in l1:
        if x == 2:
            continue
        print(x)
    else:
        return "Continue Bonus Round!!!!"


def for_with_else_4():
    l1 = []

    for x in l1:
        print(x)
    else:
        return "Empty List Bonus Round!!!!"

def for_with_else_5():
    l1 = [1,2,3]

    for x in l1:
        print(x)
        raise TypeError
    else:
        return "Raise an Error Bonus Round!!!!"

def for_with_else_6():
    l1 = []

    for x in l1:
        print(x)
        raise TypeError
    else:
        return "Another Raise an Error Bonus Round!!!!"

def try_with_else_1():
    try:
        print("We try")
    except:
        return "An Exception!"
    else:
        return "To Win!"


def try_with_else_2():
    try:
        print("We try")
        raise TypeError
    except:
        return "Another day another error"
    else:
        return "To Win!"



def test_q1():
    result = while_with_else_1()
    your_answer = INSERT_ANSWER
    assert result == your_answer

def test_q2():
    result = while_with_else_2()
    your_answer = INSERT_ANSWER
    assert result == your_answer

def test_q3():
    result = for_with_else_1()
    your_answer = INSERT_ANSWER
    assert result == your_answer

def test_q4():
    result = for_with_else_2()
    your_answer = INSERT_ANSWER
    assert result == your_answer

def test_q5():
    result = for_with_else_3()
    your_answer = INSERT_ANSWER
    assert result == your_answer

def test_q6():
    result = for_with_else_4()
    your_answer = INSERT_ANSWER
    assert result == your_answer

def test_q7():
    result = for_with_else_5()
    your_answer = INSERT_ANSWER
    assert result == your_answer

def test_q8():
    result = for_with_else_6()
    your_answer = INSERT_ANSWER
    assert result == your_answer

def test_q9():
    result = try_with_else_1()
    your_answer = INSERT_ANSWER
    assert result == your_answer

def test_q10():
    result = try_with_else_2()
    your_answer = INSERT_ANSWER
    assert result == your_answer




