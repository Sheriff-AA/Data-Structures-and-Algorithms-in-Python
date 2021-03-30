def selection_sort(array: list):
    for i in range(len(array)):
        min_val = i
        val = array[i]
        for j in range(len(array)-1):
            if array[j] < min_val:
                min_val = j

        array[i], array[min_val] = array[min_val], val

    return array
