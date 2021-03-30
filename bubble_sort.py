def bubble_sort(array: list):
    length = len(array)
    x = 0
    while x < length:
        for i in range(length - 1):
            if array[i] > array[i+1]:
                array[i+1], array[i] = array[i], array[i+1]
            else:
                pass
        x += 1
    return array


print(bubble_sort([6, 5, 3, 1, 8, 7, 2, 4]))
