#Search a given number in a sorted array that 
#has been rotated by some arbitrary number.

def binary_search(arr, st, end, key):

    if st > end:
        return -1

    mid = st + (end-st)/2

    if arr[mid] == key:
        return mid