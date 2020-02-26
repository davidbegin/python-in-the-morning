# this is quadratic complexity
n^2
def bubble_sort(data):
    swapped = True

    while swapped:
        swapped = False

        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
    


if __name__ == '__main__':
    data = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
    bubble_sort(data)
    print(data)



