from dis import dis
import opcode


def binary_search(data, value):
    n = len(data)

    left = 0
    right = n - 1
    while left <= right:

	# // keeps it an int, handle rounding
        middle = (left + right) // 2

        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')
 

 
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(data, 8))
