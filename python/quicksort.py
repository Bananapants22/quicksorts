def partition(a, low, high):
    pivot = a[low]

    i = low - 1

    for j in range(low, high):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    
    a[i+1], a[high] = a[high], a[i+1]

    return (i+1)

def quicksort(a, low, high):
    if low < high:
        p = partition(a, low, high)

        quicksort(a, low, p-1)
        quicksort(a, p+1, high)