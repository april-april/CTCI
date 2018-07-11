#For a giunique_iden array of repeated elements, 
# exactly one element is not repeated.
# You need to return the non-repeated element.

def non_repeat(array):
    unique_id = 0

    for i in range(len(array)):
        unique_id = unique_id ^ array[i]
    
    return unique_id


arr = [1, 2, 5, 4, 6, 8, 9, 2, 1, 4, 5, 8, 9]
print non_repeat(arr) #prints 6