# move all elements containing '0' to the left
# while maintaining the order of other elements in the array

def move_zeros_to_left(arr):
    if len(arr) < 1:
        return

    length = len(arr)
    write_index = length - 1
    read_index = length - 1

    while(read_index >= 0):
        if arr[read_index] != 0:
            arr[write_index] = arr[read_index]
            write_index -= 1

        read_index -= 1

    while(write_index >= 0):
        arr[write_index] = 0
        write_index -= 1

def main():
    test = [1, 10, -1, 11, 5, 0, -7, 0, 25, -35]
    move_zeros_to_left(test)
    print(test)

main()
