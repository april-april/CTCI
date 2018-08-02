# Given three integer arrays sorted in ascending order, 
# find the smallest number that is common in all three arrays.
def find_smallest_common_number(a, b, c):

    #initialize 3 pointers
    i = 0
    j = 0
    k = 0

    while i < len(a) and j < len(b) and k < len(c):

        #found smallest common number
        if a[i] == b[j] and b[j] == c[k]:
            return a[i]
        
        # move iterators forward

        if a[i] <= b[j] and a[i] <= c[k]:
            i += 1
        elif b[j] <= a[i] and b[j] <= c[k]:
            j += 1
        elif c[k] <= a[i] and c[k] <= b[j]:
            k += 1

    return None

def main():
    v1 = [1, 6, 10, 14, 50]
    v2 = [-1, 6, 7, 8, 50]
    v3 = [0, 6, 7, 10, 25, 30, 50]
    #prints 6
    print(find_smallest_common_number(v1, v2, v3))


main()