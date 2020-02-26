print("\033c")
import pytest
import numpy as np



# m = np.zeros((2,2,2,2))
# print("m = np.zeros((2,2,2,2))")
# print(m)

import random


# for i in range(2):
#     0, 1
#     print (subject[0][i][0][0])

# def access_thang(multi_arr):
#     pass

def test_multi_access():
    subject = np.full([3,2,9,9], 0)
    expected_result = np.array((range(9)))
    for i in range(2):
        result = subject[0][i][0][0]
        assert list(result) == list(expected_result)
