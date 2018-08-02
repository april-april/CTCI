# Given three integer arrays sorted in ascending order, 
# find the smallest number that is common in all three arrays.
def find_smallest_common_number(a,b,c):

    #initialize 3 pointers
    i = 0
    j = 0
    k = 0

    while i < len(a) and j < len(b) and k < len(c):

        #found smallest common number
        if a[i] == b[j] and b[j] == c[k]:
            return a[i]
        
        # move iterator forward

        if a[i] <= b[j] and a[i] <= c[k]:
            i += 1
        elif b[j] <= a[i] and b[j] <= c[k]:
            j += 1
        elif c[k] <= a[i] and c[k] <= b[j]:
            k += 1

    return None