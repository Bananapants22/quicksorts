def partition(a: list, low: int, high: int) -> int:
    """Select a pivot, then move all values lower than the pivot left of it,
    and all values greater than it to the right.
    Once both pointers are at the same point, return that point (the pivot).
    """
    pivot = a[(high+low) // 2] # Select the middle value as the pivot

    # Initialise both indexes at either end of the list
    i = low
    j = high

    while True:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i >= j:
            return j # j in this case is the index of the pivot
    
    a[i], a[j] = a[j], a[i] # Swap the values at the indexes


def quicksort(a: list, low: int, high: int):
    """Quicksort the list a."""
    if low < high:
        p = partition(a, low, high)

        # Recursively quicksort the lists on either side of the pivot 
        # at index p
        quicksort(a, low, p)
        quicksort(a, p+1, high)
