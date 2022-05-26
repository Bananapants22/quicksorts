def partition(a, low, high):
    pivot = a[(high+low)//2]

    i = low
    j = high

    while True:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i >= j:
            return j

        a[i], a[j] = a[j],a[i]

def quicksort(a, low, high):
    if low < high:
        p = partition(a, low, high)

        quicksort(a, low, p)
        quicksort(a, p+1, high)

a = [2,5,1,4,3]
quicksort(a, 0, len(a)-1)
print(a)