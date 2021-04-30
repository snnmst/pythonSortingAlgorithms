def SelectionSort(arr):
    for i in range(len(arr)):
        lowest_value_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[lowest_value_index]:
                lowest_value_index = j
        arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]
    return arr