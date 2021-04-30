def InsertionSort(arr):
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i - 1
        while j>= 0 and arr[j] > item_to_insert:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = item_to_insert
    
    return arr