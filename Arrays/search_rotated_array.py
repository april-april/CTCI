#Search a given number in a sorted array that 
#has been rotated by some arbitrary number.

def binary_search(arr, st, end, key):

    if st > end:
        return -1

    mid = st + (end-st)/2

    if arr[mid] == key:
        return mid
    
    if (arr[st] < arr[mid] and
            key < arr[mid] and
            key >= arr[st]):
        return binary_search(arr, st, mid-1, key)
    elif (arr[mid] < arr[end] and 
            key > arr[mid] and
            key <= arr[end]):
        return binary_search(arr, mid+1, end, key)
    elif arr[st] > arr[mid]:
        return binary_search(arr, st, mid-1, key)
    elif arr[end] < arr[mid]:
        return binary_search(arr, mid+1, end, key)

    return -1

