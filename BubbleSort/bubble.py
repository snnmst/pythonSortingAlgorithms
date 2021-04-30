def BubbleSort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) -1):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                swapped = True
    return arr