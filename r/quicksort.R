partition <- function(a, low, high) {
  pivot <- a[(high + low) %/% 2] # Select the middle value as the pivot

  # Initialise both indexes at either end of the list
  i <- low
  j <- high

  repeat {
    while (a[i] < pivot) {
      i <- i + 1
    }
    while (a[j] > pivot) {
      j <- j - 1
    }
    if (i >= j) {
      return (j) # j in this case is the index of the pivot
    }
  }

  # Swap the values at the indexes
  temp <- a[i]
  a[i] <- a[j]
  a[j] <- temp
}

quicksort <- function(a, low, high) {
  if (low < high) {
    p <- partition(a, low, high)
  }

  # Recursively quicksort the lists on either side of the pivot at index p
  quicksort(a, low, p)
  quicksort(a, p + 1, high)
}