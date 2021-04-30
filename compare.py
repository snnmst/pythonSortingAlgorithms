from MergeSort.mergeSort import *
from QuickSort.quick_sort import quick_sort
from BubbleSort.bubble import BubbleSort
from SelectionSort.selection import SelectionSort
from InsertionSort.insertion import InsertionSort
from heapq import heappush, heappop
from random import randint

def set_random_array(size = 10, max = 50):
    return [randint(0,max) for _ in range(size)]


def HeapSort(arr):
    heap = []
    for elem in arr:
        heappush(heap, elem)
    
    ordered = []
    while heap:
        ordered.append(heappop(heap))

    return ordered



if __name__ == '__main__':
    print('Algorithms are compering...')

    n = [10,100,1000,10000]

    times = {'Bubble':[], 
            'Selection':[],
            'Insertion':[],
            'Heap':[],
            'Merge':[],
            'Quick':[]}

    from time import time

    sort_map = {'Bubble' : BubbleSort, 
                'Selection' : SelectionSort,
                'Insertion' : InsertionSort,
                'Heap' : HeapSort,
                'Merge':merge_sort,
                'Quick':quick_sort}

    def compare(size, sorting_name):
        a = set_random_array(size, size)
        t0 = time()
        sort_map[sorting_name](a)
        t1 = time()
        times[sorting_name].append(t1-t0)

    for size in n:
        for i in sort_map:
            compare(size,i)
      

    print("b\t  Bubble   Insertion  Selection   Heap    Merge   Quick")
    print(70*"_")
    for i, size in enumerate(n):
        print("{}\t{:9.5f}{:9.5f}  {:9.5f}  {:9.5f}{:9.5f}{:9.5f}".format(
            size, times['Bubble'][i], times['Insertion'][i], times['Selection'][i],
            times['Heap'][i], times['Merge'][i], times['Quick'][i]) 
        )