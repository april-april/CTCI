def wiggleSort(arr):

    #   return if array is empty
        if not arr:
            return

        n = len(arr)

        # starting at 1, increment i by 2 
        # until n because you only need to compare the 
        # odd numbers
        for i in range(1, n, 2):
            # if it is less than its previous number,
            # then swap
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
            
            # if you haven't reached the end of the array,
            # and if the current number is less than its
            # next number, then swap
            if i + 1 < n and arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        
        return arr
                
print wiggleSort([3,5,2,1,6,4])