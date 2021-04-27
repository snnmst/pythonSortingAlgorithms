from random import randint

def set_random_array(size=10, max=50):
    return [randint(0, max) for _ in range(size)]

def quick_sort(a):
    if len(a) <= 1: return a
    smallar, equal, greater= [], [], []
    pivot = a[randint(0,len(a)-1)]

    for i in a:
        if i < pivot: smaller.append(i)
        elif i== pivot : equal.append(i)
        else:           greater.append(i)
    
    return quick_sort(smaller)+equal+quick_sort(greater)


