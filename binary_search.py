'''
    Runs in logarithmic time in the worst case
'''
def binary_search(data, num):

    if len(data) < 1:
        return -1


    min = 0
    max = len(data) - 1


    while min <= max:

        mid = (min + max) >> 1

        if data[mid] < num:
            min = mid + 1

        elif data[mid] > num:
            max = mid - 1

        else:
            return mid

    return -1




if __name__ == '__main__':


    data = [0, 3, 6, 12, 14, 26, 36, 56, 72, 123]

    assert -1 == binary_search(data, 1)
    assert data.index(3) == binary_search(data, 3)
    assert data.index(56) == binary_search(data, 56)
    assert data.index(72) == binary_search(data, 72)
