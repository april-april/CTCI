''' 
first_list     = [3, 4, 6, 10, 11, 15]
list_2 = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print merge_lists(first_list, list_2)

'''

def merge_lists(first_list, second_list):
    # Set up our merged_list
    merged_list_size = len(first_list) + len(second_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0

    #TO BE CONTINUED