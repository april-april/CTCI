def binary_search_rec(a, key, low, high):
    if low > high:
        return -1
    
    mid = low + ((high - low) // 2) #this prevents overflow

    if a[mid] == key:
        return mid
    elif key < a[mid]:
        return binary_search_rec(a, key, low, mid-1)
    else:
        return binary_search_rec(a, key, mid+1, high)

def binary_search(a, key):
    return binary_search_rec(a, key, 0, len(a)-1)

def main():
    arr = [1, 5, 9, 50, 70, 75, 98, 500, 750, 1000]
    print binary_search(arr, 9) #2
    print binary_search(arr, 750) #8
    

main()