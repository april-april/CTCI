# move all elements containing '0' to the left
# while maintaining the order of other elements in the array

def move_zeros_to_left(A):
    if len(A) < 1:
        return

    length = len(A)
    write_index = length - 1
    read_index = length - 1