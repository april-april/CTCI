# move all elements containing '0' to the left
# while maintaining the order of other elements in the array

def move_zeros_to_left(A):
    if len(A) < 1:
        return

    length = len(A)
    write_index = length - 1
    read_index = length - 1

    while(read_index >= 0):
        if A[read_index] != 0:
            A[write_index] = A[read_index]
            write_index -= 1

        read_index -= 1

    while(write_index >= 0):
        A[write_index] = 0
        write_index -= 1

