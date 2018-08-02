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


    return